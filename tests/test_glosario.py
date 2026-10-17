"""Coherencia del glosario: sin conceptos duplicados ni términos contradictorios.

Ejecutar desde la raíz del repositorio:

    python3 -m unittest discover tests
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILL = RAIZ / "skills" / "ets"
sys.path.insert(0, str(SKILL / "scripts"))

import verificar  # noqa: E402

GLOSARIO = verificar.cargar_yaml(SKILL / "references" / "glosario.yaml")
V = verificar.Verificador(usar_nlp=False)

CAMPOS = {
    "id": str, "concepto": str, "preferido": str, "categoria": str, "patron": str,
    "admitidos": list, "desaconsejados": list, "literales_ajenos": list, "restriccion": str,
    "ejemplo": str, "contraejemplo": str, "en": str, "perfiles": list, "nota_regional": str,
    "version": str,
}
CATEGORIAS = {"sustantivo", "verbo", "adjetivo", "locucion-verbal"}
PERFILES_VALIDOS = set(verificar.PERFILES) | {"todos"}

# Conceptos que el informe base (tablas 5.4 y 5.12) exige cubrir.
OBLIGATORIOS = {
    "equipo", "archivo", "telefono", "seleccionar", "descargar", "escribir", "ejecutar", "carpeta",
    "iniciar-sesion", "desplegar", "copia-de-seguridad", "commit", "endpoint", "token",
    "revocar-credencial",
}


def _norm(termino: str) -> str:
    return verificar.normalizar(termino.strip())


class TestEsquema(unittest.TestCase):
    def test_es_una_lista_de_entre_60_y_100_conceptos(self):
        self.assertIsInstance(GLOSARIO, list)
        self.assertGreaterEqual(len(GLOSARIO), 60)
        self.assertLessEqual(len(GLOSARIO), 100)

    def test_campos_y_tipos(self):
        for entrada in GLOSARIO:
            with self.subTest(id=entrada.get("id")):
                self.assertEqual(set(entrada), set(CAMPOS))
                for campo, tipo in CAMPOS.items():
                    self.assertIsInstance(entrada[campo], tipo, campo)
                self.assertIn(entrada["categoria"], CATEGORIAS)
                self.assertTrue(set(entrada["perfiles"]) <= PERFILES_VALIDOS)
                self.assertTrue(entrada["preferido"] and entrada["concepto"] and entrada["ejemplo"])
                self.assertEqual(entrada["version"], verificar.VERSION)
                if entrada["patron"]:
                    self.assertTrue(_norm(entrada["patron"]).startswith(_norm(entrada["preferido"])))

    def test_ids_unicos(self):
        ids = [e["id"] for e in GLOSARIO]
        self.assertEqual(len(ids), len(set(ids)))

    def test_conceptos_obligatorios(self):
        self.assertEqual(OBLIGATORIOS - {e["id"] for e in GLOSARIO}, set())


class TestCoherencia(unittest.TestCase):
    def test_desaconsejado_no_es_preferido_en_otra_entrada(self):
        preferidos = {_norm(e["preferido"]): e["id"] for e in GLOSARIO}
        for entrada in GLOSARIO:
            for termino in entrada["desaconsejados"]:
                with self.subTest(id=entrada["id"], termino=termino):
                    self.assertNotIn(_norm(termino), preferidos)

    def test_desaconsejado_no_es_admitido_en_ninguna_entrada(self):
        admitidos = {_norm(t): e["id"] for e in GLOSARIO for t in e["admitidos"]}
        for entrada in GLOSARIO:
            for termino in entrada["desaconsejados"]:
                with self.subTest(id=entrada["id"], termino=termino):
                    self.assertNotIn(_norm(termino), admitidos)

    def test_sin_conceptos_duplicados(self):
        conceptos = [_norm(e["concepto"]) for e in GLOSARIO]
        self.assertEqual(len(conceptos), len(set(conceptos)))

    def test_mismo_preferido_solo_con_patron_distinto(self):
        vistos: dict[str, str] = {}
        for entrada in GLOSARIO:
            clave = (_norm(entrada["preferido"]), _norm(entrada["patron"]))
            self.assertNotIn(clave, vistos, entrada["id"])
            vistos[clave] = entrada["id"]


class TestEjemplos(unittest.TestCase):
    def _perfiles(self, entrada) -> list[str]:
        if "todos" in entrada["perfiles"]:
            return list(verificar.PERFILES)
        return entrada["perfiles"]

    def test_ejemplos_sin_errores(self):
        for entrada in GLOSARIO:
            for perfil in self._perfiles(entrada):
                with self.subTest(id=entrada["id"], perfil=perfil):
                    avisos = V.verificar_texto(entrada["ejemplo"], perfil).avisos
                    self.assertEqual([a for a in avisos if a.nivel == "error"], [])

    def test_ejemplos_no_usan_terminos_desaconsejados(self):
        for entrada in GLOSARIO:
            with self.subTest(id=entrada["id"]):
                avisos = V.verificar_texto(entrada["ejemplo"], "conceptos-api", "estricto").avisos
                self.assertEqual([a.fragmento for a in avisos if a.regla == "TER-01"], [])

    def test_contraejemplos_con_desaconsejado_se_detectan(self):
        for entrada in GLOSARIO:
            contra = entrada["contraejemplo"]
            if not contra or not entrada["desaconsejados"]:
                continue
            normal = _norm(contra)
            if not any(_norm(t).split()[0][:4] in normal for t in entrada["desaconsejados"]):
                continue
            with self.subTest(id=entrada["id"]):
                reglas = {a.regla for a in V.verificar_texto(contra, "conceptos-api", "estricto").avisos}
                self.assertTrue(reglas & {"TER-01", "TER-02", "TER-03"}, contra)


if __name__ == "__main__":
    unittest.main()
