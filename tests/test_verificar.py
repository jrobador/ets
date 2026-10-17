"""Pruebas del verificador ETS v0.1.

Ejecutar desde la raíz del repositorio:

    python3 -m unittest discover tests
"""
from __future__ import annotations

import io
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILL = RAIZ / "skills" / "ets"
sys.path.insert(0, str(SKILL / "scripts"))

import verificar  # noqa: E402
from proteger import literales_de_documento, proteger, restaurar  # noqa: E402

V = verificar.Verificador()


def ids(texto: str, perfil: str = "conceptos-api", modo: str = "estandar", **kw) -> list[str]:
    return [a.regla for a in V.verificar_texto(texto, perfil, modo, **kw).avisos]


LARGA_PROC = (
    "Para configurar la integración con el proveedor de identidad abre la consola de "
    "administración, ve a la sección de seguridad y escribe la URL del proveedor junto con el "
    "identificador del cliente."
)
LARGA_DESC = (
    "El servicio de colas recibe los mensajes que publican los productores, los guarda en disco "
    "durante el periodo de retención configurado y los entrega a los consumidores en el mismo "
    "orden en que llegaron al servidor."
)

# ID: (perfil, texto que debe generar el aviso, texto que no debe generarlo)
CASOS: dict[str, tuple[str, str, str]] = {
    "TER-01": ("conceptos-api", "Abre el fichero de configuración.", "Abre el archivo de configuración."),
    "TER-02": ("procedimientos", "Loguéate con la cuenta de la organización.",
               "Inicia sesión con la cuenta de la organización."),
    "TER-03": ("procedimientos", "Dale permisos de lectura al equipo de soporte.",
               "Concede permiso de lectura al equipo de soporte."),
    "TER-06": ("conceptos-api", "El servidor se colgó durante la carga.",
               "El servidor no responde durante la carga."),
    "TER-10": ("conceptos-api", "El administrador crea la cuenta para el servicio y guarda su clave.",
               "La API valida la solicitud y su firma."),
    "VER-01": ("procedimientos", "Seleccioná la cuenta y tocá «Continuar».",
               "Selecciona la cuenta y toca «Continuar»."),
    "VER-02": ("procedimientos", "Abrid el panel y revisad vuestra configuración.",
               "Abre el panel y revisa la configuración."),
    "VER-03": ("procedimientos", "Abre el archivo. Después, seleccione «Guardar».",
               "Abre el archivo. Después, selecciona «Guardar»."),
    "VER-04": ("conceptos-api", "Tú debes confirmar el cambio.", "Debes confirmar el cambio."),
    "VER-06": ("conceptos-api", "La API devolverá un error si falta el parámetro.",
               "La API devuelve un error si falta el parámetro."),
    "VER-07": ("procedimientos", "Deberías crear una copia de seguridad antes de migrar.",
               "Crea una copia de seguridad antes de migrar."),
    "VER-10": ("procedimientos", "Se debe reiniciar antes de aplicar los cambios.",
               "Reinicia el servicio antes de aplicar los cambios."),
    "VER-12": ("conceptos-api", "Los archivos temporales son eliminados por el proceso de limpieza.",
               "El proceso de limpieza elimina los archivos temporales."),
    "VER-13": ("procedimientos", "Instala el paquete, reiniciando después el servicio.",
               "Abre el panel pulsando la tecla F2."),
    "ORA-02": ("procedimientos", "Elimina la base de datos de pruebas si ya no la necesitas.",
               "Si ya no necesitas la base de datos de pruebas, elimina la base de datos."),
    "ORA-03": ("procedimientos", LARGA_PROC, "Abre la consola de administración."),
    "ORA-04": ("conceptos-api", LARGA_DESC, "El servicio de colas guarda los mensajes en disco."),
    "ORA-07": ("conceptos-api", "Realiza la actualización de la configuración del servicio.",
               "Actualiza la configuración del servicio."),
    "ORA-08": ("conceptos-api", "Cambia el valor del tiempo de espera de la política de acceso del servicio.",
               "Crea una copia de seguridad de la base de datos."),
    "ORA-11": ("interfaz", "Bienvenido/a a la plataforma.", "Te damos la bienvenida."),
    "ORA-12": ("interfaz", "El/La {objeto} se eliminó.", "Se eliminó el elemento {nombre}."),
    "FOR-01": ("conceptos-api", "## Configuración De La Cuenta", "## Instalar en Claude Code"),
    "FOR-02": ("interfaz", "Quieres eliminar el proyecto?", "¿Quieres eliminar el proyecto?"),
    "FOR-04": ("procedimientos", "Abre «Configuración» → «Seguridad».", "Abre «Configuración > Seguridad»."),
    "FOR-05": ("conceptos-api", "Cambia el valor de max_retries a 5.", "Cambia el valor de `max_retries` a 5."),
    "FOR-07": ("conceptos-api", "El archivo ocupa 512MB y tarda 30s en subir.",
               "El archivo ocupa 512 MB y tarda 30 s en subir."),
    "FOR-08": ("conceptos-api", "Libera 20 GBs de espacio.", "Libera 20 GB de espacio."),
    "FOR-10": ("conceptos-api", "El plan gratuito admite 10.000 solicitudes al día.",
               "El plan gratuito admite 10 000 solicitudes al día."),
    "FOR-11": ("conceptos-api", "El servicio deja de funcionar el 03/04/2026.",
               "El servicio deja de funcionar el 3 de abril de 2026."),
    "PRO-02": ("procedimientos", "1. Abrir la consola.\n2. Copiar la clave.",
               "1. Abre la consola.\n2. Copia la clave."),
    "PRO-07": ("procedimientos", "Cuidado: el comando vacía la caché.", "Nota: El comando vacía la caché."),
    "PRO-08": ("procedimientos", "Se recomienda crear una rama antes de empezar.",
               "Crea una rama antes de empezar."),
    "INT-02": ("interfaz", "Crear Nueva Cuenta", "Crear cuenta nueva"),
    "INT-05": ("interfaz", "Error fatal: operación ilegal.", "No se pudo completar la operación."),
    "INT-06": ("interfaz", "Se eliminaron {n} archivo(s).", "Se eliminaron {n} archivos."),
}


class TestReglas(unittest.TestCase):
    def test_cada_regla_tiene_caso(self):
        verificables = {r["id"] for r in V.reglas} - {"FOR-06"}
        self.assertEqual(verificables - set(CASOS), set(), "Reglas sin caso de prueba")

    def test_positivos(self):
        for rid, (perfil, positivo, _) in CASOS.items():
            with self.subTest(regla=rid):
                self.assertIn(rid, ids(positivo, perfil), positivo)

    def test_negativos(self):
        for rid, (perfil, _, negativo) in CASOS.items():
            with self.subTest(regla=rid):
                self.assertNotIn(rid, ids(negativo, perfil), negativo)

    def test_glosario_respeta_el_patron(self):
        # «correr» solo se marca con objetos de ejecución: comando, script, pruebas...
        self.assertIn("TER-01", ids("Corre las pruebas antes de crear el commit."))
        self.assertNotIn("TER-01", ids("El proceso corre en segundo plano."))
        # «invalidar» es preferido para la caché y no se marca.
        self.assertNotIn("TER-01", ids("Invalida la caché después de cambiar las plantillas."))

    def test_modo_estricto_sube_el_glosario(self):
        texto = "Abre el fichero de configuración."
        estandar = V.verificar_texto(texto, "conceptos-api", "estandar").avisos
        estricto = V.verificar_texto(texto, "conceptos-api", "estricto").avisos
        self.assertEqual([a.nivel for a in estandar if a.regla == "TER-01"], ["sugerencia"])
        self.assertEqual([a.nivel for a in estricto if a.regla == "TER-01"], ["advertencia"])

    def test_subjuntivo_y_pasiva_refleja_no_se_marcan(self):
        texto = ("Espera a que termine el proceso. No cierres la ventana hasta que aparezca el "
                 "mensaje. Se encontraron tres errores.")
        self.assertEqual(ids(texto, "procedimientos"), [])

    def test_usted_plural_no_es_mezcla(self):
        self.assertNotIn("VER-03", ids("Selecciona la cuenta. Si ustedes comparten el equipo, cierra sesión."))

    def test_condicion_indirecta_no_se_marca(self):
        self.assertNotIn("ORA-02", ids("Comprueba si el servicio responde.", "procedimientos"))

    def test_desactivar(self):
        texto = "Seleccioná la cuenta."
        self.assertIn("VER-01", ids(texto, "procedimientos"))
        self.assertNotIn("VER-01", ids(texto, "procedimientos", desactivar={"VER-01"}))


class TestProteccion(unittest.TestCase):
    TEXTO = (
        "Ejecuta `seleccioná --force 512MB 10.000`.\n"
        "\n"
        "```\n"
        "Realiza la actualización de la configuración del servicio. Abrid 03/04/2026 512MB\n"
        "```\n"
        "\n"
        "Abre https://example.com/deployar/12MB y el archivo /etc/app/config_10.000.yaml.\n"
        "Selecciona «Guardar Cambios Ahora».\n"
        "Escribe {nombre_de_usuario} y %s con la opción --dry-run.\n"
    )

    def test_codigo_protegido_no_genera_avisos(self):
        for perfil in verificar.PERFILES:
            with self.subTest(perfil=perfil):
                self.assertEqual(ids(self.TEXTO, perfil), [])

    def test_restaurar(self):
        linea = "Ejecuta `npm install` en https://example.com y abre «Guardar»."
        protegido, literales = proteger(linea)
        self.assertNotIn("npm", protegido)
        self.assertEqual(restaurar(protegido, literales), linea)
        self.assertEqual([l.tipo for l in literales], ["codigo", "url", "etiqueta"])

    def test_url_sin_puntuacion_final(self):
        _, literales = proteger("Visita https://example.com.")
        self.assertEqual(literales[0].valor, "https://example.com")

    def test_barras_de_prosa_no_son_rutas(self):
        _, literales = proteger("Usa deber/poder y y/o con El/La en el texto.")
        self.assertEqual(literales, [])

    def test_literales_de_documento_incluye_bloques(self):
        tipos = [l.tipo for _, l in literales_de_documento("Texto `a`.\n```\nx = 1\n```\n")]
        self.assertEqual(sorted(tipos), ["bloque", "codigo"])


class TestOriginal(unittest.TestCase):
    ORIGINAL = "Ejecuta `npm install` y selecciona «Guardar cambios». Define max_retries."

    def test_literal_cambiado_es_error(self):
        nuevo = "Ejecuta `npm instalar` y selecciona «Guardar cambios». Define `max_retries`."
        avisos = V.verificar_texto(nuevo, "procedimientos", original=self.ORIGINAL).avisos
        errores = [a for a in avisos if a.regla == "FOR-06" and a.nivel == "error"]
        self.assertEqual([a.fragmento for a in errores], ["npm install"])

    def test_literales_intactos(self):
        nuevo = "Selecciona «Guardar cambios». Ejecuta `npm install`. Define `max_retries`."
        self.assertNotIn("FOR-06", ids(nuevo, "procedimientos", original=self.ORIGINAL))


class TestPerfil(unittest.TestCase):
    def test_deteccion(self):
        self.assertEqual(V.detectar_perfil("1. Abre la consola.\n2. Copia la clave.\n"), "procedimientos")
        self.assertEqual(V.detectar_perfil(
            "## 2.1.0 — 3 de abril de 2026\n\n### Correcciones\n\n- Se corrigió un error.\n"), "notas")
        self.assertEqual(V.detectar_perfil("Guardar cambios\nCancelar\nCrear proyecto\n"), "interfaz")
        self.assertEqual(V.detectar_perfil(
            "El endpoint `GET /users` devuelve una lista. El parámetro `limit` es opcional."),
            "conceptos-api")

    def test_directiva_de_perfil(self):
        texto = "<!-- ets: perfil=procedimientos -->\nElimina el entorno si ya no lo usas.\n"
        self.assertIn("ORA-02", ids(texto, None))


class TestCLI(unittest.TestCase):
    def _correr(self, texto: str, *args: str) -> tuple[int, str]:
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(texto)
            ruta = f.name
        salida = io.StringIO()
        with redirect_stdout(salida):
            codigo = verificar.main([ruta, *args])
        Path(ruta).unlink()
        return codigo, salida.getvalue()

    def test_codigo_de_salida(self):
        self.assertEqual(self._correr("El archivo ocupa 512MB.")[0], 1)
        self.assertEqual(self._correr("El archivo ocupa 512 MB.")[0], 0)

    def test_json(self):
        import json

        codigo, salida = self._correr("Abre el fichero.", "--formato", "json", "--perfil", "procedimientos")
        datos = json.loads(salida)
        self.assertEqual(codigo, 0)
        self.assertEqual(datos["perfil"], "procedimientos")
        self.assertEqual(datos["avisos"][0]["regla"], "TER-01")

    def test_nunca_dice_conforme(self):
        _, salida = self._correr("Abre el archivo.")
        self.assertIn("Revisado según la convención ETS v0.1", salida)
        self.assertNotRegex(salida.lower(), r"\bconforme\b|certificad")


class TestDocumentacion(unittest.TestCase):
    """Las referencias y reglas.yaml deben coincidir."""

    def _verificables(self) -> dict[str, set[str]]:
        encontrados: dict[str, set[str]] = {}
        for ruta in (SKILL / "references").rglob("*.md"):
            texto = ruta.read_text(encoding="utf-8")
            regla_actual = None
            for linea in texto.splitlines():
                m = re.match(r"^### ([A-Z]{3}-\d{2}) — ", linea)
                if m:
                    regla_actual = m.group(1)
                m = re.match(r"^Verificable: (sí|parcialmente) \(([A-Z]{3}-\d{2})\)", linea)
                if m and regla_actual:
                    encontrados.setdefault(m.group(2), set()).add(regla_actual)
        return encontrados

    def test_ids_de_referencias_existen_en_reglas(self):
        reglas = {r["id"] for r in V.reglas}
        self.assertEqual(set(self._verificables()) - reglas, set())

    def test_cada_regla_esta_documentada(self):
        reglas = {r["id"] for r in V.reglas}
        self.assertEqual(reglas - set(self._verificables()), set())

    def test_referencias_sin_errores(self):
        archivos = [SKILL / "SKILL.md", *sorted((SKILL / "references").rglob("*.md"))]
        for ruta in archivos:
            with self.subTest(archivo=ruta.name):
                resultado = V.verificar_texto(ruta.read_text(encoding="utf-8"))
                errores = [a for a in resultado.avisos if a.nivel == "error"]
                self.assertEqual(errores, [])

    def test_skill_md_breve(self):
        lineas = (SKILL / "SKILL.md").read_text(encoding="utf-8").splitlines()
        self.assertLessEqual(len(lineas), 160)
        self.assertEqual(lineas[0], "---")
        self.assertIn("name: ets", lineas)


class TestYAML(unittest.TestCase):
    def test_subconjunto(self):
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False, encoding="utf-8") as f:
            f.write('a: 1\nb: "x: y"\nc: [d, "e, f", \'g\'\'h\']\nlista:\n  - id: x\n    v: \'\\b\'\n  - id: y\n')
            ruta = f.name
        datos = verificar.cargar_yaml(ruta)
        Path(ruta).unlink()
        self.assertEqual(datos, {"a": 1, "b": "x: y", "c": ["d", "e, f", "g'h"],
                                 "lista": [{"id": "x", "v": "\\b"}, {"id": "y"}]})

    def test_coincide_con_pyyaml(self):
        try:
            import yaml  # type: ignore
        except ImportError:
            self.skipTest("PyYAML no está instalado")
        for ruta in (SKILL / "scripts" / "reglas.yaml", SKILL / "references" / "glosario.yaml"):
            with self.subTest(archivo=ruta.name):
                self.assertEqual(verificar.cargar_yaml(ruta), yaml.safe_load(ruta.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
