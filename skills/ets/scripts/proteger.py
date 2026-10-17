#!/usr/bin/env python3
"""Protección de literales para el verificador ETS v0.1.

Aparta bloques de código, código en línea, URL, rutas, variables, opciones,
etiquetas de interfaz entre «» e identificadores antes de analizar la prosa.
Cada literal se reemplaza por un marcador de tres caracteres de uso privado
de Unicode, que no coincide con ``\\w`` ni con la puntuación. Así las reglas
no analizan los literales y las posiciones de la prosa no se mezclan con ellos.

Solo usa la biblioteca estándar."""
from __future__ import annotations

import re
from dataclasses import dataclass

INICIO = ""
FIN = ""
BASE = 0xE100
MAX_LITERALES = 0xF8FF - BASE

MARCADOR = re.compile(INICIO + "(.)" + FIN)


@dataclass(frozen=True)
class Literal:
    tipo: str
    valor: str

    @property
    def contenido(self) -> str:
        """Valor sin las marcas de formato, para comparar original y reescritura."""
        if self.tipo == "codigo":
            return self.valor.strip("`").strip()
        if self.tipo == "etiqueta":
            return self.valor[1:-1].strip()
        return self.valor


# El orden importa: cada patrón se aplica sobre el resultado del anterior.
PATRONES: list[tuple[str, re.Pattern[str]]] = [
    ("codigo", re.compile(r"``[^`\n]+``|`[^`\n]+`")),
    ("enlace", re.compile(r"(?<=\])\([^()\s]+(?:\s+\"[^\"]*\")?\)")),
    ("url", re.compile(r"\b(?:https?|ftp)://[^\s<>()«»\"']+|\bwww\.[^\s<>()«»\"']+")),
    ("correo", re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b")),
    ("html", re.compile(r"</?[A-Za-z][^<>\n]*>")),
    ("etiqueta", re.compile(r"«[^«»\n]+»")),
    ("variable", re.compile(
        r"\$\{[^}\n]+\}|\{\{[^}\n]+\}\}|\{[^{}\s]+\}"
        r"|%\(\w+\)[sdif]|%\d+\$[sdif]|%[sdif@](?!\w)|\$[A-Z_][A-Z0-9_]*"
    )),
    ("ruta", re.compile(
        r"(?<![\w/.])(?:~|\.{1,2})?/[\w.\-/@]+"
        r"|\b[A-Za-z]:\\[\w\\.\-]+"
        r"|\b[\w.\-]+(?:/[\w.\-]+)+\.[A-Za-z0-9]{1,5}\b"
        r"|\b[\w\-]+\.(?:md|json|jsonl|ya?ml|py|js|ts|tsx|jsx|toml|txt|sh|env|cfg|ini"
        r"|log|csv|xml|html|lock|go|rs|java|rb|php)\b"
    )),
    ("opcion", re.compile(r"(?<![\w\-])--?[A-Za-z][\w\-]*(?:=\S+)?")),
    ("identificador", re.compile(
        r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b"
        r"|\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b"
        r"|\b[a-z]+[A-Z][A-Za-z0-9]*\b"
        r"|\b\w+\(\)"
    )),
]

PUNTUACION_FINAL_URL = ".,;:!?"


def _marcador(indice: int) -> str:
    if indice > MAX_LITERALES:
        raise ValueError("Demasiados literales en una sola línea.")
    return INICIO + chr(BASE + indice) + FIN


def proteger(texto: str) -> tuple[str, list[Literal]]:
    """Reemplaza cada literal por un marcador y devuelve el texto y los literales."""
    literales: list[Literal] = []

    for tipo, patron in PATRONES:
        def sustituir(m: re.Match[str]) -> str:
            valor = m.group(0)
            resto = ""
            if tipo == "url":
                while valor and valor[-1] in PUNTUACION_FINAL_URL:
                    resto = valor[-1] + resto
                    valor = valor[:-1]
            literales.append(Literal(tipo, valor))
            return _marcador(len(literales) - 1) + resto

        texto = patron.sub(sustituir, texto)

    return texto, literales


def restaurar(texto: str, literales: list[Literal]) -> str:
    """Devuelve los literales a su lugar."""
    def sustituir(m: re.Match[str]) -> str:
        lit = literal_de(m.group(1), literales)
        return lit.valor if lit else m.group(0)

    # Un literal puede contener marcadores de pasos anteriores (por ejemplo,
    # una ruta que incluye una variable), así que se restaura hasta el final.
    anterior = None
    while anterior != texto:
        anterior = texto
        texto = MARCADOR.sub(sustituir, texto)
    return texto


def literal_de(marcador_indice: str, literales: list[Literal]) -> Literal | None:
    indice = ord(marcador_indice) - BASE
    if 0 <= indice < len(literales):
        return literales[indice]
    return None


def apartar_bloques(lineas: list[str]) -> tuple[list[str], list[tuple[int, str]]]:
    """Vacía las líneas de bloques de código delimitados con ``` o ~~~.

    Devuelve las líneas con los bloques vacíos (se conserva la numeración) y
    la lista de bloques como (número de línea inicial, contenido).
    """
    salida: list[str] = []
    bloques: list[tuple[int, str]] = []
    valla: str | None = None
    inicio = 0
    contenido: list[str] = []

    for numero, linea in enumerate(lineas, 1):
        marca = re.match(r"^\s*(`{3,}|~{3,})", linea)
        if valla is None and marca:
            valla = marca.group(1)[0] * 3
            inicio = numero
            contenido = []
            salida.append("")
            continue
        if valla is not None:
            if linea.strip().startswith(valla):
                bloques.append((inicio, "\n".join(contenido)))
                valla = None
            else:
                contenido.append(linea)
            salida.append("")
            continue
        salida.append(linea)

    if valla is not None:
        bloques.append((inicio, "\n".join(contenido)))
    return salida, bloques


def literales_de_documento(texto: str) -> list[tuple[int, Literal]]:
    """Lista todos los literales de un documento con su número de línea."""
    lineas, bloques = apartar_bloques(texto.split("\n"))
    resultado: list[tuple[int, Literal]] = []
    for numero, linea in enumerate(lineas, 1):
        _, literales = proteger(linea)
        resultado.extend((numero, lit) for lit in literales)
    resultado.extend((numero, Literal("bloque", contenido)) for numero, contenido in bloques)
    return resultado

