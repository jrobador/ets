#!/usr/bin/env python3
"""Corre los casos de evals/casos.jsonl contra el verificador ETS.

Uso, desde la raíz del repositorio:

    python3 evals/correr.py                       # verificador sobre las entradas
    python3 evals/correr.py --reescrituras R.jsonl  # evalúa reescrituras de un modelo
    python3 evals/correr.py --detalle             # muestra cada caso

R.jsonl tiene una línea por caso: {"id": "pro-01", "salida": "texto reescrito"}.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "skills" / "ets" / "scripts"))

import verificar  # noqa: E402


def cargar(ruta: Path) -> list[dict]:
    with open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def evaluar_entradas(casos: list[dict], v: verificar.Verificador, detalle: bool) -> int:
    esperados = detectados = trampas = falsos = extra = 0
    por_perfil: dict[str, list[int]] = {}
    for caso in casos:
        avisos = v.verificar_texto(caso["entrada"], caso["perfil"]).avisos
        reglas = {a.regla for a in avisos}
        faltan = [r for r in caso["avisos_esperados"] if r not in reglas]
        fp = [r for r in caso["no_debe_marcar"] if r in reglas]
        otros = sorted(reglas - set(caso["avisos_esperados"]) - set(caso["no_debe_marcar"]))
        esperados += len(caso["avisos_esperados"])
        detectados += len(caso["avisos_esperados"]) - len(faltan)
        trampas += len(caso["no_debe_marcar"])
        falsos += len(fp)
        extra += len(otros)
        p = por_perfil.setdefault(caso["perfil"], [0, 0, 0])
        p[0] += len(caso["avisos_esperados"])
        p[1] += len(caso["avisos_esperados"]) - len(faltan)
        p[2] += len(fp)
        if detalle or faltan or fp:
            estado = "ok" if not faltan and not fp else "REVISAR"
            print(f"{caso['id']:8} {estado:8} esperados={caso['avisos_esperados']} "
                  f"faltan={faltan} falsos_positivos={fp} otros={otros}")

    print()
    print(f"Casos: {len(casos)}")
    print(f"Avisos esperados detectados: {detectados}/{esperados} "
          f"({100 * detectados / max(esperados, 1):.0f} %)")
    print(f"Falsos positivos en trampas: {falsos}/{trampas}")
    print(f"Otros avisos no anotados: {extra}")
    for perfil, (e, d, f) in sorted(por_perfil.items()):
        print(f"  {perfil:15} detectados {d}/{e}, falsos positivos {f}")
    return 0 if falsos == 0 else 1


def evaluar_reescrituras(casos: list[dict], ruta: Path, v: verificar.Verificador) -> int:
    salidas = {r["id"]: r["salida"] for r in cargar(ruta)}
    problemas = 0
    for caso in casos:
        if caso["id"] not in salidas:
            continue
        salida = salidas[caso["id"]]
        perdidos = [e for e in caso["debe_conservar"] if e not in salida]
        resultado = v.verificar_texto(salida, caso["perfil"], original=caso["entrada"])
        errores = [a for a in resultado.avisos if a.nivel == "error"]
        advertencias = [a for a in resultado.avisos if a.nivel == "advertencia"]
        estado = "ok" if not perdidos and not errores else "REVISAR"
        problemas += estado != "ok"
        print(f"{caso['id']:8} {estado:8} perdidos={perdidos} errores={[a.regla for a in errores]} "
              f"advertencias={[a.regla for a in advertencias]}")
    print()
    print(f"Reescrituras evaluadas: {len([c for c in casos if c['id'] in salidas])}. Con problemas: {problemas}.")
    print("Completa la revisión manual con references/preservar-significado.md.")
    return 1 if problemas else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Evalúa el verificador ETS con los casos de prueba.")
    parser.add_argument("--casos", default=str(RAIZ / "evals" / "casos.jsonl"))
    parser.add_argument("--reescrituras", help="JSONL con {id, salida} para evaluar reescrituras.")
    parser.add_argument("--detalle", action="store_true", help="Muestra todos los casos.")
    parser.add_argument("--nlp", action="store_true", help="Usa spaCy o Stanza si están instalados.")
    args = parser.parse_args()

    casos = cargar(Path(args.casos))
    v = verificar.Verificador(usar_nlp=args.nlp)
    if args.reescrituras:
        return evaluar_reescrituras(casos, Path(args.reescrituras), v)
    return evaluar_entradas(casos, v, args.detalle)


if __name__ == "__main__":
    sys.exit(main())
