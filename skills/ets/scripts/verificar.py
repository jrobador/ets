#!/usr/bin/env python3
"""Verificador de la convención ETS v0.1 (Español Técnico Simplificado).

Detecta problemas frecuentes en texto técnico en español según las reglas de
references/. No certifica un texto: un resultado sin avisos significa que el
verificador no encontró los problemas que sabe detectar.

Uso:

    python3 verificar.py ARCHIVO [--perfil procedimientos|conceptos-api|interfaz|notas]
                                 [--modo estandar|estricto] [--formato texto|json]
                                 [--original ARCHIVO] [--glosario ARCHIVO]
                                 [--desactivar ID,ID]

ARCHIVO puede ser «-» para leer de la entrada estándar.
Código de salida: 0 sin errores, 1 con errores, 2 por un problema de uso.

Solo requiere la biblioteca estándar de Python 3.10 o posterior.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path

DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(DIR))

from proteger import (  # noqa: E402
    FIN,
    INICIO,
    MARCADOR,
    Literal,
    apartar_bloques,
    literal_de,
    literales_de_documento,
    proteger,
    restaurar,
)

VERSION = "0.1"
RUTA_REGLAS = DIR / "reglas.yaml"
RUTA_GLOSARIO = DIR.parent / "references" / "glosario.yaml"
PERFILES = ("procedimientos", "conceptos-api", "interfaz", "notas")
MODOS = ("estandar", "estricto")
ORDEN_NIVEL = {"error": 0, "advertencia": 1, "sugerencia": 2}


# ---------------------------------------------------------------------------
# Lector de un subconjunto de YAML
# ---------------------------------------------------------------------------
#
# Admite: mapas y listas por sangría, escalares sin comillas, entre comillas
# dobles (con escapes de JSON) o simples ('' para una comilla), listas en
# línea [a, "b c"], enteros y comentarios con #. No admite anclas, bloques
# literales (| o >) ni mapas en línea. Los archivos del proyecto se escriben
# dentro de este subconjunto para no depender de PyYAML.


class ErrorYAML(ValueError):
    pass


def _leer_escalar(s: str, i: int, en_lista: bool) -> tuple[object, int]:
    """Lee un escalar desde s[i]. Devuelve (valor, posición siguiente)."""
    n = len(s)
    while i < n and s[i] == " ":
        i += 1
    if i >= n:
        return "", i
    c = s[i]
    if c == '"':
        j = i + 1
        while j < n:
            if s[j] == "\\":
                j += 2
                continue
            if s[j] == '"':
                break
            j += 1
        if j >= n:
            raise ErrorYAML(f"Comillas dobles sin cerrar: {s}")
        return json.loads(s[i:j + 1]), j + 1
    if c == "'":
        j = i + 1
        partes = []
        while j < n:
            if s[j] == "'":
                if j + 1 < n and s[j + 1] == "'":
                    partes.append("'")
                    j += 2
                    continue
                break
            partes.append(s[j])
            j += 1
        if j >= n:
            raise ErrorYAML(f"Comillas simples sin cerrar: {s}")
        return "".join(partes), j + 1
    if c == "[" and not en_lista:
        return _leer_lista(s, i)
    # Escalar sin comillas.
    j = i
    fin_set = ",]" if en_lista else ""
    while j < n:
        if s[j] == "#" and (j == 0 or s[j - 1] == " "):
            break
        if s[j] in fin_set:
            break
        j += 1
    texto = s[i:j].strip()
    if re.fullmatch(r"-?\d+", texto):
        return int(texto), j
    if texto in ("true", "false"):
        return texto == "true", j
    return texto, j


def _leer_lista(s: str, i: int) -> tuple[list, int]:
    assert s[i] == "["
    i += 1
    items: list = []
    n = len(s)
    while True:
        while i < n and s[i] == " ":
            i += 1
        if i >= n:
            raise ErrorYAML(f"Lista sin cerrar: {s}")
        if s[i] == "]":
            return items, i + 1
        valor, i = _leer_escalar(s, i, en_lista=True)
        if valor != "":
            items.append(valor)
        while i < n and s[i] == " ":
            i += 1
        if i < n and s[i] == ",":
            i += 1


def _valor_linea(resto: str) -> object:
    valor, j = _leer_escalar(resto, 0, en_lista=False)
    cola = resto[j:].strip()
    if cola and not cola.startswith("#"):
        raise ErrorYAML(f"Texto inesperado después del valor: {resto}")
    return valor


def cargar_yaml(ruta: Path | str) -> object:
    with open(ruta, encoding="utf-8") as f:
        crudas = f.read().split("\n")
    lineas: list[tuple[int, str, int]] = []
    for numero, linea in enumerate(crudas, 1):
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        sangria = len(linea) - len(linea.lstrip(" "))
        lineas.append((sangria, linea.strip(), numero))
    if not lineas:
        return None
    valor, i = _parsear_bloque(lineas, 0, lineas[0][0])
    if i != len(lineas):
        raise ErrorYAML(f"{ruta}: estructura no válida cerca de la línea {lineas[i][2]}")
    return valor


CLAVE = re.compile(r"^([\w\-]+):(?:\s+(.*))?$")


def _parsear_bloque(lineas, i, sangria):
    if lineas[i][1].startswith("- ") or lineas[i][1] == "-":
        return _parsear_lista(lineas, i, sangria)
    return _parsear_mapa(lineas, i, sangria, {})


def _parsear_mapa(lineas, i, sangria, mapa):
    while i < len(lineas) and lineas[i][0] == sangria and not lineas[i][1].startswith("- "):
        m = CLAVE.match(lineas[i][1])
        if not m:
            raise ErrorYAML(f"Se esperaba «clave: valor» en la línea {lineas[i][2]}")
        clave, resto = m.group(1), m.group(2)
        i += 1
        if resto is None or resto.strip() == "":
            if i < len(lineas) and lineas[i][0] > sangria:
                mapa[clave], i = _parsear_bloque(lineas, i, lineas[i][0])
            elif i < len(lineas) and lineas[i][0] == sangria and lineas[i][1].startswith("- "):
                mapa[clave], i = _parsear_lista(lineas, i, sangria)
            else:
                mapa[clave] = ""
        else:
            mapa[clave] = _valor_linea(resto)
    return mapa, i


def _parsear_lista(lineas, i, sangria):
    items = []
    while i < len(lineas) and lineas[i][0] == sangria and lineas[i][1].startswith("-"):
        contenido = lineas[i][1][1:].strip()
        sangria_item = sangria + 2
        i += 1
        if m := CLAVE.match(contenido):
            item: dict = {}
            clave, resto = m.group(1), m.group(2)
            if resto is None or resto.strip() == "":
                if i < len(lineas) and lineas[i][0] > sangria_item:
                    item[clave], i = _parsear_bloque(lineas, i, lineas[i][0])
                else:
                    item[clave] = ""
            else:
                item[clave] = _valor_linea(resto)
            if i < len(lineas) and lineas[i][0] > sangria:
                item, i = _parsear_mapa(lineas, i, lineas[i][0], item)
            items.append(item)
        else:
            items.append(_valor_linea(contenido))
    return items, i


# ---------------------------------------------------------------------------
# Utilidades de texto
# ---------------------------------------------------------------------------


def normalizar(texto: str) -> str:
    """Minúsculas y sin tildes (conserva la ñ). Conserva la longitud."""
    salida = []
    for c in texto:
        if c in "ñÑ":
            salida.append("ñ")
            continue
        base = unicodedata.normalize("NFD", c)[0]
        menor = base.lower()
        salida.append(menor if len(menor) == 1 else base)
    return "".join(salida)


PALABRA = re.compile(r"[^\W\d_]+")
CLITICOS = ("lo", "la", "los", "las", "le", "les", "me", "nos", "te", "se")


def _infinitivo(verbo: str) -> tuple[str, str] | None:
    v = normalizar(verbo.strip().split()[0]) if verbo.strip() else ""
    if v.endswith("se") and len(v) > 4:
        v = v[:-2]
    if len(v) < 3 or v[-2:] not in ("ar", "er", "ir"):
        return None
    return v[:-2], v[-2:]


def _raiz_subjuntivo(raiz: str, conj: str) -> str:
    if conj == "ar":
        if raiz.endswith("c"):
            return raiz[:-1] + "qu"
        if raiz.endswith("g"):
            return raiz[:-1] + "gu"
        if raiz.endswith("z"):
            return raiz[:-1] + "c"
    return raiz


TERMINACIONES = {
    "ar": ["ar", "as", "a", "an", "amos", "ado", "ada", "ados", "adas", "ando", "e", "es",
           "en", "emos", "aron", "aste", "ara", "aran", "aria", "arian", "ad", "ais", "eis",
           "arlo", "arla", "arlos", "arlas", "arle", "arles", "arse", "ate", "alo", "ala",
           "alos", "alas", "ale", "ales"],
    "er": ["er", "es", "e", "en", "emos", "ido", "ida", "idos", "idas", "iendo", "a",
           "as", "an", "amos", "ieron", "iste", "io", "era", "eran", "eria", "erian", "ed",
           "eis", "erlo", "erla", "erlos", "erlas", "erle", "erse", "ete", "elo", "ela"],
    "ir": ["ir", "es", "e", "en", "imos", "ido", "ida", "idos", "idas", "iendo", "a", "as",
           "an", "amos", "ieron", "iste", "io", "ira", "iran", "iria", "irian", "id", "is",
           "irlo", "irla", "irlos", "irlas", "irle", "irse", "ete", "elo", "ela"],
}

FORMAS_IRREGULARES = {
    "hacer": ["hacer", "haz", "hace", "haces", "hacen", "hacemos", "hizo", "hicieron", "hecho",
              "haga", "hagas", "hagan", "hara", "haran", "haciendo", "hacerlo", "hazlo"],
    "dar": ["dar", "da", "das", "dan", "damos", "dio", "dieron", "dado", "des", "den", "dara",
            "daran", "dando", "dale", "dales", "darle", "darles", "dandole"],
    "poner": ["poner", "pon", "pone", "pones", "ponen", "puso", "pusieron", "puesto", "ponga",
              "pongas", "pongan", "pondra", "poniendo", "ponle", "ponerlo"],
}


def formas_verbo(infinitivo: str) -> list[str]:
    """Formas normalizadas (sin tildes) de un verbo, para buscar en el glosario."""
    v = normalizar(infinitivo)
    if v.endswith("se") and v[:-2] in FORMAS_IRREGULARES:
        v = v[:-2]
    if v in FORMAS_IRREGULARES:
        return FORMAS_IRREGULARES[v]
    datos = _infinitivo(v)
    if not datos:
        return [v]
    raiz, conj = datos
    formas = {raiz + t for t in TERMINACIONES[conj]}
    subj = _raiz_subjuntivo(raiz, conj)
    if subj != raiz:
        formas |= {subj + t for t in ("e", "es", "en", "emos")}
    formas.add(v)
    return sorted(formas, key=len, reverse=True)


# ---------------------------------------------------------------------------
# Estructuras
# ---------------------------------------------------------------------------


@dataclass
class Aviso:
    linea: int
    regla: str
    nivel: str
    fragmento: str
    mensaje: str
    sugerencia: str = ""


@dataclass
class Unidad:
    """Una oración, una celda de tabla o un encabezado, ya protegidos."""

    linea: int
    texto: str
    literales: list[Literal]
    tipo: str  # oracion, celda, encabezado
    perfil: str
    cruda: str
    es_paso: bool = False
    primera: bool = False
    norm: str = field(default="", init=False)

    def __post_init__(self):
        self.norm = normalizar(self.texto)

    def fragmento(self, inicio: int, fin: int, maximo: int = 90) -> str:
        texto = restaurar(self.texto[inicio:fin], self.literales).strip()
        if len(texto) > maximo:
            texto = texto[: maximo - 1].rstrip() + "…"
        return texto


@dataclass
class Resultado:
    perfil: str
    perfil_detectado: bool
    modo: str
    avisos: list[Aviso]

    @property
    def resumen(self) -> dict[str, int]:
        cuenta = Counter(a.nivel for a in self.avisos)
        return {n: cuenta.get(n, 0) for n in ORDEN_NIVEL}


# ---------------------------------------------------------------------------
# Verificador
# ---------------------------------------------------------------------------


class Verificador:
    def __init__(
        self,
        glosario_proyecto: Path | str | None = None,
    ):
        cfg = cargar_yaml(RUTA_REGLAS)
        if not isinstance(cfg, dict):
            raise ErrorYAML(f"{RUTA_REGLAS}: se esperaba un mapa.")
        self.cfg = cfg
        self.reglas: list[dict] = cfg["reglas"]
        self.glosario: list[dict] = list(cargar_yaml(RUTA_GLOSARIO) or [])
        if glosario_proyecto:
            propio = {e["id"]: e for e in (cargar_yaml(glosario_proyecto) or [])}
            self.glosario = [propio.pop(e["id"], e) for e in self.glosario] + list(propio.values())
        self.nombres_propios = set(cfg.get("nombres_propios", []))
        self.prefijos_ignorados = {normalizar(p) for p in cfg.get("prefijos_ignorados", [])}
        self.umbral = {
            "procedimientos": int(cfg["longitud_procedimientos"]),
            "conceptos-api": int(cfg["longitud_descripciones"]),
            "notas": int(cfg["longitud_descripciones"]),
        }
        self.etiquetas_documentacion = {normalizar(p) for p in cfg.get("etiquetas_documentacion", [])}
        self.no_infinitivos = {normalizar(p) for p in cfg.get("no_infinitivos", [])}
        self.no_gerundios = {normalizar(p) for p in cfg.get("no_gerundios", [])}

        self._regex = {}
        for regla in self.reglas:
            if regla.get("tipo") == "regex":
                flags = 0 if regla.get("mayusculas") == "exactas" else re.IGNORECASE
                self._regex[regla["id"]] = re.compile(regla["patron"], flags)

        self._construir_formas()
        self._compilar_glosario()

    # -- Preparación ---------------------------------------------------------

    def _verbos(self) -> set[str]:
        verbos = {normalizar(v) for v in self.cfg.get("verbos_frecuentes", [])}
        for entrada in self.glosario:
            if entrada.get("categoria") in ("verbo", "locucion-verbal"):
                for termino in [entrada.get("preferido", "")] + list(entrada.get("admitidos", [])) \
                        + list(entrada.get("desaconsejados", [])):
                    if termino:
                        primera = normalizar(str(termino).split()[0])
                        if _infinitivo(primera):
                            verbos.add(primera)
        return verbos

    def _construir_formas(self) -> None:
        voseo: set[str] = set()
        vosotros: set[str] = {"vosotros", "vosotras", "vuestro", "vuestra", "vuestros", "vuestras"}
        tu: set[str] = {normalizar(f) for f in self.cfg.get("imperativos_tu_irregulares", [])}
        usted_base: set[str] = {normalizar(f) for f in self.cfg.get("imperativos_usted_irregulares", [])}
        tilde = {"ar": "á", "er": "é", "ir": "í"}
        vocal = {"ar": "a", "er": "e", "ir": "i"}

        for verbo in self._verbos():
            datos = _infinitivo(verbo)
            if not datos:
                continue
            raiz, conj = datos
            inf = raiz + conj
            if len(raiz) >= 2 and inf not in ("estar", "dar", "ver", "ser", "ir"):
                voseo.add(raiz + tilde[conj])
                voseo.add(raiz + tilde[conj] + "s")
                # Sin «le», «les», «me» ni «nos»: generarían adjetivos como «generales».
                for c in ("lo", "la", "los", "las", "te"):
                    voseo.add(raiz + vocal[conj] + c)
            if len(inf) > 3:
                vosotros.add(inf[:-1] + "d")
            if len(raiz) < 2:
                continue
            if conj == "ar":
                tu.add(raiz + "a")
                usted_base.add(_raiz_subjuntivo(raiz, conj) + "e")
            else:
                tu.add(raiz + "e")
                usted_base.add(raiz + "a")

        # Formas con pronombre átono (normalizadas, sin tilde).
        tu_completo = set(tu)
        for forma in tu:
            for c in CLITICOS:
                if c != "se":
                    tu_completo.add(forma + c)
        usted = set(usted_base)
        for forma in usted_base:
            for c in CLITICOS:
                if c != "te":
                    usted.add(forma + c)

        ambiguas = tu_completo & usted
        self.f_voseo = voseo
        self.f_vosotros = vosotros
        self.f_tu = tu_completo - ambiguas
        self.f_usted = usted - ambiguas
        self.f_tu_negativo = {f + "s" for f in usted_base} - usted
        self.f_usted_negativo = set(usted_base)

    def _compilar_glosario(self) -> None:
        no_flexionar = {"el", "la", "los", "las", "un", "una", "tu", "tus", "por", "de", "en", "a"}
        self._glosario: list[tuple[dict, str, re.Pattern[str], re.Pattern[str] | None]] = []
        unidades: set[str] = set()

        for entrada in self.glosario:
            categoria = entrada.get("categoria", "")
            for termino in [entrada.get("preferido", "")] + list(entrada.get("admitidos", [])):
                t = normalizar(str(termino))
                if " de " in f" {t} ":
                    unidades.add(t)

            objetos = None
            patron = str(entrada.get("patron", ""))
            if "+" in patron:
                lista = [normalizar(o.strip()) for o in patron.split("+", 1)[1].split("|") if o.strip()]
                if lista:
                    objetos = re.compile(
                        r"(?<!\w)(?:" + "|".join(re.escape(o) for o in lista) + r")(?:s|es)?(?!\w)"
                    )

            for termino in entrada.get("desaconsejados", []):
                palabras = normalizar(str(termino)).split()
                if not palabras:
                    continue
                primera, resto = palabras[0], palabras[1:]
                if categoria in ("verbo", "locucion-verbal") and _infinitivo(primera) \
                        and primera not in no_flexionar:
                    formas = formas_verbo(primera)
                elif primera in no_flexionar:
                    formas = [primera]
                else:
                    formas = {primera, primera + "s", primera + "es"}
                    if categoria == "adjetivo" and primera.endswith("o"):
                        formas |= {primera[:-1] + "a", primera[:-1] + "as", primera + "s"}
                    formas = sorted(formas, key=len, reverse=True)
                cuerpo = "(?:" + "|".join(re.escape(f) for f in formas) + ")"
                cuerpo += "".join(r"\s+" + re.escape(p) for p in resto)
                regex = re.compile(r"(?<![\w\-])" + cuerpo + r"(?![\w\-])")
                self._glosario.append((entrada, str(termino), regex, objetos))

        # Términos de varias palabras preferidos o admitidos: un desaconsejado
        # dentro de uno de ellos (como «request» en «pull request») no se marca.
        compuestos = sorted({
            normalizar(str(t)) for e in self.glosario
            for t in [e.get("preferido", "")] + list(e.get("admitidos", [])) if " " in str(t)
        }, key=len, reverse=True)
        self._compuestos = re.compile(
            r"(?<!\w)(?:" + "|".join(re.escape(c) for c in compuestos) + r")(?!\w)"
        ) if compuestos else None

        unidades_ord = sorted(unidades, key=len, reverse=True)
        self._unidades_de = re.compile(
            r"(?<!\w)(?:" + "|".join(re.escape(u) for u in unidades_ord) + r")(?!\w)"
        ) if unidades_ord else None

    # -- Detección de perfil ---------------------------------------------------

    def detectar_perfil(self, texto: str) -> str:
        m = re.search(r"^\s*<!--\s*ets:\s*perfil=([\w-]+)\s*-->\s*$", texto, re.MULTILINE)
        if m and m.group(1) in PERFILES:
            return m.group(1)
        lineas, _ = apartar_bloques(texto.split("\n"))
        lineas = [l.strip() for l in lineas if l.strip() and not l.strip().startswith("<!--")]
        if not lineas:
            return "conceptos-api"
        puntos = Counter()
        for linea in lineas:
            m = re.match(r"^\d+[.)]\s+\**([^\W\d_]+)", linea)
            if m and normalizar(m.group(1)) in self.f_tu:
                puntos["procedimientos"] += 3
            if re.match(r"^#+\s.*\b\d+\.\d+(?:\.\d+)?\b", linea):
                puntos["notas"] += 3
            n = normalizar(linea)
            puntos["notas"] += len(re.findall(
                r"\b(?:novedades|correcciones|cambios incompatibles|se corrigio|se añadio|"
                r"se agrego|obsoleto|se elimino)\b", n))
            puntos["conceptos-api"] += len(re.findall(
                r"\b(?:get|post|put|patch|delete)\s+/|\bdevuelve\b|\bparametro|\brespuesta\b|"
                r"\bencabezado\b|\bendpoint\b|\bfuncion\b", n))
        cortas = [
            l for l in lineas
            if not l.startswith(("#", "|", "-", "*", ">")) and not re.match(r"^\d+[.)]", l)
            and len(PALABRA.findall(l)) <= 8 and not l.endswith(".")
        ]
        largas = any(len(PALABRA.findall(l)) > 20 for l in lineas)
        if len(lineas) >= 2 and len(cortas) / len(lineas) >= 0.6 and not largas:
            puntos["interfaz"] += 5
        if not puntos:
            return "conceptos-api"
        mejor, valor = puntos.most_common(1)[0]
        if valor <= 1:
            return "conceptos-api"
        return mejor

    # -- Segmentación ----------------------------------------------------------

    def _unidades(self, texto: str, perfil: str) -> list[Unidad]:
        lineas, _ = apartar_bloques(texto.split("\n"))
        if lineas and lineas[0].strip() == "---":
            for j in range(1, len(lineas)):
                if lineas[j].strip() == "---":
                    for k in range(j + 1):
                        lineas[k] = ""
                    break

        unidades: list[Unidad] = []
        perfil_actual = perfil
        ignorar_bloque = False
        ignorar_siguiente = False
        for numero, cruda in enumerate(lineas, 1):
            s = cruda.strip()
            directiva = re.fullmatch(r"<!--\s*ets:\s*(.*?)\s*-->", s)
            if directiva:
                orden = directiva.group(1)
                if orden.startswith("perfil=") and orden[7:] in PERFILES:
                    perfil_actual = orden[7:]
                elif orden == "ignorar-inicio":
                    ignorar_bloque = True
                elif orden == "ignorar-fin":
                    ignorar_bloque = False
                elif orden == "ignorar":
                    ignorar_siguiente = True
                continue
            if not s or s.startswith("<!--") or ignorar_bloque:
                continue
            if ignorar_siguiente:
                ignorar_siguiente = False
                continue
            unidades.extend(self._unidades_de_linea(numero, cruda, perfil_actual))
        return unidades

    ETIQUETA = re.compile(
        r"^(?:\*\*|__)?([A-ZÁÉÍÓÚÑ][\wáéíóúñ]*(?:\s+[\wáéíóúñ]+){0,2})\s*:(?:\*\*|__)?\s+"
    )

    def _unidades_de_linea(self, numero: int, cruda: str, perfil: str) -> list[Unidad]:
        s = cruda.strip()
        piezas: list[tuple[str, str]] = []
        es_paso = False

        if re.match(r"^#{1,6}\s", s):
            piezas.append(("encabezado", re.sub(r"^#{1,6}\s+", "", s).rstrip("#").strip()))
        elif re.match(r"^\|?\s*:?-{3,}", s):
            return []
        elif s.startswith("|"):
            celdas = [c.strip() for c in s.strip("|").split("|")]
            piezas.extend(("celda", c) for c in celdas if c)
        else:
            while s.startswith(">"):
                s = s[1:].lstrip()
            m = re.match(r"^(?:[-*+]|(\d+)[.)])\s+(?:\[[ xX]\]\s+)?", s)
            if m:
                es_paso = m.group(1) is not None
                s = s[m.end():]
            piezas.append(("oracion", s))

        unidades: list[Unidad] = []
        for tipo, contenido in piezas:
            if tipo != "encabezado":
                m = self.ETIQUETA.match(contenido)
                if m:
                    if normalizar(m.group(1)) in self.prefijos_ignorados:
                        if tipo == "oracion":
                            return []
                        continue
                    contenido = contenido[m.end():]
            protegido, literales = proteger(contenido)
            protegido = re.sub(r"\*\*|__", "", protegido)
            protegido = re.sub(r"(?<![\w*])\*(?=\S)|(?<=\S)\*(?![\w*])", "", protegido)
            if tipo == "oracion":
                partes = re.split(
                    r"(?<=[.!?…])\s+(?=[¿¡\"'(\[A-ZÁÉÍÓÚÑ0-9" + INICIO + r"])", protegido
                )
            else:
                partes = [protegido]
            for indice, parte in enumerate(partes):
                if not parte.strip():
                    continue
                unidades.append(Unidad(
                    linea=numero, texto=parte, literales=literales, tipo=tipo, perfil=perfil,
                    cruda=cruda, es_paso=es_paso and indice == 0, primera=not unidades,
                ))
        return unidades

    # -- Verificación ----------------------------------------------------------

    def verificar_texto(
        self,
        texto: str,
        perfil: str | None = None,
        modo: str = "estandar",
        original: str | None = None,
        desactivar: set[str] | frozenset[str] = frozenset(),
    ) -> Resultado:
        if modo not in MODOS:
            raise ValueError(f"Modo desconocido: {modo}")
        detectado = perfil is None
        perfil_doc = perfil or self.detectar_perfil(texto)
        if perfil_doc not in PERFILES:
            raise ValueError(f"Perfil desconocido: {perfil_doc}")

        unidades = self._unidades(texto, perfil_doc)
        avisos: list[Aviso] = []
        for regla in self.reglas:
            rid = regla["id"]
            if rid in desactivar:
                continue
            nivel = regla.get("nivel_estricto", regla["nivel"]) if modo == "estricto" else regla["nivel"]
            if regla.get("tipo") == "regex":
                patron = self._regex[rid]
                for u in unidades:
                    if not self._aplica(regla, u.perfil):
                        continue
                    for m in patron.finditer(u.texto):
                        avisos.append(Aviso(u.linea, rid, nivel, u.fragmento(m.start(), m.end()),
                                            regla["mensaje"], regla.get("sugerencia", "")))
                continue

            funcion = regla.get("funcion")
            if funcion == "mezcla_tratamiento":
                avisos.extend(self._mezcla_tratamiento(unidades, regla, nivel))
            elif funcion == "literales_original":
                if original is not None:
                    avisos.extend(self._comparar_literales(original, texto, regla, nivel))
            else:
                control = getattr(self, "_c_" + str(funcion), None)
                if control is None:
                    raise ValueError(f"Función desconocida en reglas.yaml: {funcion}")
                for u in unidades:
                    if not self._aplica(regla, u.perfil):
                        continue
                    for fragmento, mensaje, sugerencia in control(u):
                        avisos.append(Aviso(u.linea, rid, nivel, fragmento,
                                            mensaje or regla["mensaje"],
                                            sugerencia or regla.get("sugerencia", "")))

        avisos = self._depurar(avisos)
        return Resultado(perfil_doc, detectado, modo, avisos)

    @staticmethod
    def _aplica(regla: dict, perfil: str) -> bool:
        perfiles = regla.get("perfiles", ["todos"])
        return "todos" in perfiles or perfil in perfiles

    @staticmethod
    def _depurar(avisos: list[Aviso]) -> list[Aviso]:
        # Un término ya marcado como híbrido o como verbo comodín no se repite
        # como término del glosario.
        fuertes = [a for a in avisos if a.regla in ("TER-02", "TER-03")]
        salida = []
        vistos = set()
        for a in avisos:
            if a.regla == "TER-01" and any(
                f.linea == a.linea and (a.fragmento.lower() in f.fragmento.lower()
                                        or f.fragmento.lower() in a.fragmento.lower())
                for f in fuertes
            ):
                continue
            clave = (a.linea, a.regla, a.fragmento)
            if clave in vistos:
                continue
            vistos.add(clave)
            salida.append(a)
        salida.sort(key=lambda a: (a.linea, ORDEN_NIVEL[a.nivel], a.regla))
        return salida

    # -- Controles -------------------------------------------------------------
    #
    # Cada control recibe una Unidad y devuelve una lista de
    # (fragmento, mensaje o "", sugerencia o "").

    @staticmethod
    def _primera_palabra(u: Unidad, desde: int = 0) -> re.Match[str] | None:
        """Primera palabra a partir de «desde», si no hay cifras ni letras antes."""
        m = PALABRA.search(u.texto, desde)
        if m and re.search(r"\w", u.texto[desde:m.start()]):
            return None
        return m

    def _c_glosario(self, u: Unidad):
        res = []
        protegidos = [m.span() for m in self._compuestos.finditer(u.norm)] if self._compuestos else []
        for entrada, termino, regex, objetos in self._glosario:
            for m in regex.finditer(u.norm):
                if objetos is not None and not objetos.search(u.norm):
                    continue
                if any(a <= m.start() and m.end() <= b for a, b in protegidos):
                    continue
                preferido = entrada.get("preferido", "")
                sugerencia = f"Usa «{preferido}»."
                if entrada.get("restriccion"):
                    sugerencia += " " + entrada["restriccion"]
                res.append((
                    u.fragmento(m.start(), m.end()),
                    f"«{termino}» está desaconsejado para el concepto «{entrada.get('concepto', '')}» "
                    f"(glosario: {entrada.get('id')}).",
                    sugerencia,
                ))
        return res

    def _c_longitud(self, u: Unidad):
        if u.tipo == "encabezado":
            return []
        umbral = self.umbral.get(u.perfil)
        if umbral is None:
            return []
        palabras = len(re.findall(r"[^\W_]+(?:[-'][^\W_]+)*", u.texto))
        palabras += sum(
            1 for m in MARCADOR.finditer(u.texto)
            if (lit := literal_de(m.group(1), u.literales)) and lit.tipo == "etiqueta"
        )
        if palabras <= umbral:
            return []
        inicio = " ".join(restaurar(u.texto, u.literales).split()[:8])
        return [(inicio + " …", f"La oración tiene {palabras} palabras; el umbral de aviso es {umbral}.", "")]

    def _c_voseo(self, u: Unidad):
        res = []
        for m in PALABRA.finditer(u.texto):
            palabra = m.group(0)
            menor = palabra.lower()
            if menor in self.f_voseo or menor == "vos" or palabra == "sos":
                res.append((u.fragmento(m.start(), m.end()), "", ""))
        return res

    def _c_vosotros(self, u: Unidad):
        res = []
        for m in PALABRA.finditer(u.texto):
            palabra = m.group(0)
            menor = palabra.lower()
            if (normalizar(menor) in self.f_vosotros or palabra == "os"
                    or (re.fullmatch(r"\w+(?:áis|éis)", menor)
                        and menor not in ("dieciséis", "veintiséis"))):
                res.append((u.fragmento(m.start(), m.end()), "", ""))
        return res

    # Verbos que introducen una interrogativa indirecta con «si»: Comprueba si…
    INDIRECTA = {
        "comprueba", "comprobar", "verifica", "verificar", "revisa", "revisar", "mira", "mirar",
        "pregunta", "preguntar", "averigua", "averiguar", "indica", "indicar", "determina",
        "determinar", "consulta", "consultar", "decide", "decidir", "evalua", "evaluar",
        "confirma", "confirmar", "prueba", "probar", "sabes", "saber", "sabe", "ver", "ve",
        "decir", "dice", "muestra", "mostrar", "importa", "depende", "elige", "elegir",
        "compara", "comparar", "detecta", "detectar", "informa", "especifica", "observa",
        "observar", "valida", "validar", "como", "que",
    }

    def _c_condicion_despues(self, u: Unidad):
        if u.tipo == "encabezado":
            return []
        primera = self._primera_palabra(u)
        if not primera or normalizar(primera.group(0)) not in self.f_tu:
            return []
        res = []
        for m in re.finditer(r"(?<!\w)(?:si|en caso de que|solo si|salvo que|a menos que)(?!\w)",
                             u.texto[primera.end():]):
            inicio = primera.end() + m.start()
            previa = PALABRA.findall(u.norm[:inicio])
            if m.group(0) == "si" and previa and (
                previa[-1] in self.INDIRECTA
            ):
                continue
            res.append((u.fragmento(inicio, len(u.texto)), "", ""))
            break
        return res

    def _c_gerundio(self, u: Unidad):
        candidatos = []
        for m in re.finditer(
            r",\s+(\w+?(?:ando|iendo|yendo))(?:se|lo|la|los|las|le|les|me|te|nos)?(?!\w)", u.texto,
            re.IGNORECASE,
        ):
            candidatos.append((m, m.group(1)))
        for m in re.finditer(
            r"(?<!\w)(\w+?(?:ando|iendo|yendo))\s+(?:despu[eé]s|luego|posteriormente|a continuaci[oó]n)(?!\w)",
            u.texto, re.IGNORECASE,
        ):
            candidatos.append((m, m.group(1)))
        if not candidatos:
            return []
        res = []
        for m, palabra in candidatos:
            if normalizar(palabra) in self.no_gerundios:
                continue
            res.append((u.fragmento(m.start(), m.end()).lstrip(", "), "", ""))
        return res

    DETERMINANTES = re.compile(r"(?<!\w)(?:el|la|los|las|un|una|unos|unas|del|al)(?!\w)", re.IGNORECASE)

    def _c_su_ambiguo(self, u: Unidad):
        res = []
        for m in re.finditer(r"(?<!\w)sus?(?!\w)", u.texto, re.IGNORECASE):
            if len(self.DETERMINANTES.findall(u.texto[: m.start()])) >= 3:
                fin = PALABRA.search(u.texto, m.end())
                res.append((u.fragmento(m.start(), fin.end() if fin else m.end()), "", ""))
        return res

    def _c_cadena_de(self, u: Unidad):
        texto = u.norm
        texto = re.sub(
            r"\d{1,2} de (?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre"
            r"|noviembre|diciembre)(?: de \d{4})?", lambda m: "x" * len(m.group(0)), texto)
        if self._unidades_de:
            texto = self._unidades_de.sub(lambda m: "x" * len(m.group(0)), texto)
        patron = re.compile(
            r"(?<!\w)del?(?!\w)(?:\s+[^\s,.;:()]+){1,3}?\s+del?(?!\w)"
            r"(?:\s+[^\s,.;:()]+){1,3}?\s+del?(?!\w)(?:\s+[^\s,.;:()]+)?"
        )
        return [(u.fragmento(m.start(), m.end()), "", "") for m in patron.finditer(texto)]

    def _mayusculas_internas(self, texto: str) -> int:
        palabras = PALABRA.findall(texto)
        cuenta = 0
        for palabra in palabras[1:]:
            if len(palabra) < 2 or palabra.isupper() or palabra in self.nombres_propios:
                continue
            if palabra[0].isupper():
                cuenta += 1
        return cuenta

    def _c_mayusculas_titulo(self, u: Unidad):
        if u.tipo != "encabezado":
            return []
        if self._mayusculas_internas(u.texto) >= 2:
            return [(u.fragmento(0, len(u.texto)), "", "")]
        return []

    def _c_mayusculas_etiqueta(self, u: Unidad):
        # Se analiza la línea completa: en una etiqueta como «Error Fatal: Datos»,
        # lo que precede a los dos puntos también es parte de la cadena.
        if u.tipo == "encabezado" or not u.primera:
            return []
        linea = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", u.cruda.strip())
        m = self.ETIQUETA.match(linea)
        if m and normalizar(m.group(1)) in self.etiquetas_documentacion:
            linea = linea[m.end():]
        protegida, literales = proteger(linea)
        if re.search(r"[.!?]\s+\S", protegida):
            return []  # Varias oraciones: es un mensaje, no una etiqueta.
        if len(PALABRA.findall(protegida)) > 8:
            return []
        if self._mayusculas_internas(protegida) >= 2:
            return [(restaurar(protegida, literales).strip(), "", "")]
        return []

    def _c_signos_apertura(self, u: Unidad):
        res = []
        if "?" in u.texto and "¿" not in u.texto:
            res.append((u.fragmento(0, len(u.texto)), "Falta el signo de apertura de interrogación.", ""))
        if re.search(r"!(?![\[=])", u.texto) and "¡" not in u.texto:
            res.append((u.fragmento(0, len(u.texto)), "Falta el signo de apertura de exclamación.", ""))
        return res

    def _c_ruta_menu(self, u: Unidad):
        res = []
        patron = INICIO + "(.)" + FIN + r"\s*(?:->|→|=>|/|>>|›|\|)\s*" + INICIO + "(.)" + FIN
        for m in re.finditer(patron, u.texto):
            a, b = literal_de(m.group(1), u.literales), literal_de(m.group(2), u.literales)
            if a and b and a.tipo == "etiqueta" and b.tipo == "etiqueta":
                res.append((u.fragmento(m.start(), m.end()), "", ""))
        return res

    def _c_identificador_suelto(self, u: Unidad):
        res = []
        for m in MARCADOR.finditer(u.texto):
            lit = literal_de(m.group(1), u.literales)
            if lit and lit.tipo == "identificador" and lit.valor not in self.nombres_propios:
                res.append((lit.valor, "", f"Escribe `{lit.valor}` entre comillas invertidas."))
        return res

    def _c_paso_infinitivo(self, u: Unidad):
        if not u.es_paso:
            return []
        primera = self._primera_palabra(u)
        if not primera:
            return []
        palabra = re.sub(r"(?<=[aei]r)(?:lo|la|los|las|le|les|se|me|nos|te)$", "",
                         normalizar(primera.group(0)))
        cortos = {"ir", "ver", "dar", "ser"}
        if palabra not in cortos and (
            len(palabra) <= 3 or palabra in self.no_infinitivos
            or not palabra.endswith(("ar", "er", "ir"))
        ):
            return []
        return [(u.fragmento(primera.start(), primera.end()), "", "")]

    def _c_nivel_aviso(self, u: Unidad):
        if not u.primera:
            return []
        m = re.match(
            r"^\s*(?:>\s*)*(?:[-*+]\s+)?(?:\*\*)?(Peligro|Precauci[oó]n|Cuidado|Atenci[oó]n|Ojo|Alerta)"
            r"(?:\*\*)?\s*:", u.cruda, re.IGNORECASE,
        )
        if m:
            return [(m.group(1), "", "")]
        return []

    def _mezcla_tratamiento(self, unidades: list[Unidad], regla: dict, nivel: str) -> list[Aviso]:
        marcas: dict[str, list[tuple[int, str]]] = {"tu": [], "usted": []}
        for u in unidades:
            if u.tipo == "encabezado" or not self._aplica(regla, u.perfil):
                continue
            palabras = list(PALABRA.finditer(u.texto))
            for m in palabras:
                n = normalizar(m.group(0))
                if n in ("tu", "tus", "te", "ti", "contigo"):
                    marcas["tu"].append((u.linea, m.group(0)))
                elif n == "usted":
                    marcas["usted"].append((u.linea, m.group(0)))
            # Imperativo al principio de la oración o después de la coma que
            # cierra una condición inicial.
            posiciones = [0]
            if palabras and normalizar(palabras[0].group(0)) in ("si", "cuando", "antes", "despues", "para", "al"):
                coma = u.texto.find(",")
                if coma > 0:
                    posiciones.append(coma + 1)
            for pos in posiciones:
                primera = self._primera_palabra(u, pos)
                if not primera:
                    continue
                n = normalizar(primera.group(0))
                if n == "no":
                    siguiente = PALABRA.search(u.texto, primera.end())
                    if siguiente:
                        s = normalizar(siguiente.group(0))
                        if s in self.f_tu_negativo:
                            marcas["tu"].append((u.linea, "no " + siguiente.group(0)))
                        elif s in self.f_usted_negativo:
                            marcas["usted"].append((u.linea, "no " + siguiente.group(0)))
                elif n in self.f_tu:
                    marcas["tu"].append((u.linea, primera.group(0)))
                elif n in self.f_usted:
                    marcas["usted"].append((u.linea, primera.group(0)))

        if not marcas["tu"] or not marcas["usted"]:
            return []
        minoria = "usted" if len(marcas["usted"]) <= len(marcas["tu"]) else "tu"
        mayoria = "tú" if minoria == "usted" else "usted"
        nombre = "usted" if minoria == "usted" else "tú"
        res = []
        vistos = set()
        for linea, fragmento in marcas[minoria]:
            if linea in vistos:
                continue
            vistos.add(linea)
            res.append(Aviso(
                linea, regla["id"], nivel, fragmento,
                f"Forma de {nombre} en un texto que usa sobre todo {mayoria}.",
                regla.get("sugerencia", ""),
            ))
        return res

    def _comparar_literales(self, original: str, nuevo: str, regla: dict, nivel: str) -> list[Aviso]:
        orig = literales_de_documento(original)
        nue = literales_de_documento(nuevo)
        cuenta_orig = Counter(l.contenido for _, l in orig)
        cuenta_nue = Counter(l.contenido for _, l in nue)
        res = []
        for valor, veces in (cuenta_orig - cuenta_nue).items():
            linea = next(n for n, l in orig if l.contenido == valor)
            res.append(Aviso(
                linea, regla["id"], nivel, valor[:90],
                f"Este literal aparece en la línea {linea} del original y falta o cambió en el texto nuevo"
                + (f" ({veces} veces)." if veces > 1 else "."),
                regla.get("sugerencia", ""),
            ))
        for valor, _ in (cuenta_nue - cuenta_orig).items():
            linea = next(n for n, l in nue if l.contenido == valor)
            res.append(Aviso(
                linea, regla["id"], "advertencia", valor[:90],
                "Literal nuevo que no aparece en el original. Comprueba que no sea una versión modificada.",
                "",
            ))
        return res


# ---------------------------------------------------------------------------
# Interfaz de línea de comandos
# ---------------------------------------------------------------------------

def _leer(ruta: str) -> str:
    if ruta == "-":
        return sys.stdin.read()
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def formatear_texto(archivo: str, r: Resultado) -> str:
    salida = []
    for a in r.avisos:
        linea = f"{archivo}:{a.linea}: {a.nivel.upper()} [{a.regla}] «{a.fragmento}» {a.mensaje}"
        if a.sugerencia:
            linea += f" Sugerencia: {a.sugerencia}"
        salida.append(linea)
    resumen = r.resumen
    origen = "detectado" if r.perfil_detectado else "indicado"
    salida.append(
        f"Perfil: {r.perfil} ({origen}). Modo: {r.modo}. "
        f"Errores: {resumen['error']}. Advertencias: {resumen['advertencia']}. "
        f"Sugerencias: {resumen['sugerencia']}."
    )
    salida.append(f"Revisado según la convención ETS v{VERSION}.")
    return "\n".join(salida)


def formatear_json(archivo: str, r: Resultado) -> str:
    return json.dumps({
        "archivo": archivo,
        "convencion": f"ETS v{VERSION}",
        "perfil": r.perfil,
        "perfil_detectado": r.perfil_detectado,
        "modo": r.modo,
        "resumen": r.resumen,
        "avisos": [asdict(a) for a in r.avisos],
    }, ensure_ascii=False, indent=2)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="verificar.py",
        description=f"Verificador de la convención ETS v{VERSION}.",
    )
    parser.add_argument("archivo", help="Archivo de texto o Markdown, o «-» para la entrada estándar.")
    parser.add_argument("--perfil", choices=PERFILES, help="procedimientos, conceptos-api, interfaz o notas. Si falta, se detecta.")
    parser.add_argument("--modo", default="estandar", choices=MODOS)
    parser.add_argument("--formato", default="texto", choices=("texto", "json"))
    parser.add_argument("--original", help="Texto original, para comprobar que los literales no cambiaron.")
    parser.add_argument("--glosario", help="Glosario del proyecto; sus entradas reemplazan a las del glosario base con el mismo id.")
    parser.add_argument("--desactivar", default="", help="IDs de reglas separados por comas.")
    args = parser.parse_args(argv)

    perfil = args.perfil

    try:
        texto = _leer(args.archivo)
        original = _leer(args.original) if args.original else None
        verificador = Verificador(glosario_proyecto=args.glosario)
    except (OSError, ErrorYAML) as e:
        print(f"verificar.py: {e}", file=sys.stderr)
        return 2

    desactivar = {d.strip() for d in args.desactivar.split(",") if d.strip()}
    resultado = verificador.verificar_texto(texto, perfil, args.modo, original, desactivar)
    if args.formato == "json":
        print(formatear_json(args.archivo, resultado))
    else:
        print(formatear_texto(args.archivo, resultado))
    return 1 if resultado.resumen["error"] else 0


if __name__ == "__main__":
    sys.exit(main())
