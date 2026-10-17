# ETS: Español Técnico Simplificado

ETS es una skill para agentes de programación que redacta, reescribe y revisa documentación e interfaces de software en un español controlado. El objetivo es un texto claro e inequívoco que se entienda en España y en Latinoamérica.

La skill incluye reglas por tipo de contenido, un glosario organizado por concepto y un verificador en Python que no necesita dependencias externas.

## Para quién

- Equipos que escriben documentación técnica en español: guías, referencia de API, README, notas de versión.
- Equipos que escriben textos de interfaz: botones, mensajes de error, notificaciones.
- Personas que traducen documentación técnica del inglés y quieren un resultado consistente.

## Contenido

```
skills/ets/                      # la skill que se instala
├── SKILL.md                     # flujo, modos y diez reglas esenciales
├── references/
│   ├── nucleo/                  # reglas comunes a todos los textos
│   ├── perfiles/                # procedimientos, conceptos y API, interfaz, notas de versión
│   ├── glosario.yaml            # 99 conceptos de software
│   ├── variacion-regional.md
│   ├── preservar-significado.md
│   └── ejemplos.md
└── scripts/
    ├── verificar.py             # verificador
    ├── proteger.py              # protección de código, URL, variables y etiquetas
    └── reglas.yaml              # reglas deterministas
evals/                           # 40 casos de evaluación y su script
tests/                           # pruebas del verificador y del glosario
docs/                            # informe de base y registro de decisiones
```

## Instalación

### Claude Code

Copia la carpeta de la skill a la carpeta de skills de tu usuario:

```
cp -r skills/ets ~/.claude/skills/
```

Para usarla solo en un proyecto, cópiala a la carpeta `.claude/skills/` del proyecto.

### Claude.ai

Comprime la carpeta `skills/ets` en un archivo ZIP. Después, sube el archivo desde la configuración de Claude.ai, en el apartado de skills. El verificador solo funciona si el entorno permite ejecutar código.

### Otros agentes

La carpeta usa el formato `SKILL.md`, que ya leen varios agentes. Si tu agente no lo admite, añade una instrucción en su archivo de configuración, como `AGENTS.md`, para que lea `skills/ets/SKILL.md` antes de escribir documentación en español.

## Uso

La skill se activa cuando pides escribir o revisar texto técnico en español. Ejemplos de pedidos:

- «Reescribe esta guía de instalación en español técnico controlado.»
- «Revisa los mensajes de error de `es.json` con ETS en modo estricto.»
- «Traduce estas notas de versión al español claro y técnico.»
- «Simplifica la documentación de este endpoint.»

La skill entrega el texto y, aparte, los avisos clasificados en error, advertencia y sugerencia. Al terminar, escribe «Revisado según la convención ETS v0.1». La skill nunca declara que un texto es «conforme» ni que está «certificado».

### Modos

| Modo | Uso |
|---|---|
| Estándar (predeterminado) | Documentación habitual. El glosario produce sugerencias. |
| Estricto | Textos que se traducirán o textos de seguridad. El glosario es obligatorio para los conceptos que cubre. |

### Perfiles

| Perfil | Contenido |
|---|---|
| `procedimientos` | Pasos, instalación, configuración, solución de problemas. |
| `conceptos-api` | Explicaciones, referencia de API, README, comentarios de código. |
| `interfaz` | Botones, menús, mensajes de error, notificaciones. |
| `notas` | Notas de versión y registros de cambios. |

## Verificador

El verificador necesita Python 3.10 o posterior y solo usa la biblioteca estándar. Si spaCy (con el modelo `es_core_news_sm`) o Stanza están instalados, el verificador los usa para confirmar gerundios e infinitivos.

```
python3 skills/ets/scripts/verificar.py guia.md
python3 skills/ets/scripts/verificar.py guia.md --perfil procedimientos --modo estricto
python3 skills/ets/scripts/verificar.py nueva.md --original original.md
python3 skills/ets/scripts/verificar.py textos.md --formato json
```

Sin la opción `--perfil`, el verificador detecta el perfil. Cada aviso indica la línea, el ID de la regla, el nivel, el fragmento y una sugerencia. El código de salida es 1 si hay errores.

Otras opciones:

- `--original ARCHIVO`: comprueba que el texto nuevo conserva el código, las rutas, las variables y las etiquetas del original.
- `--glosario ARCHIVO`: añade el glosario del proyecto. Sus entradas reemplazan a las del glosario base con el mismo `id`.
- `--desactivar ID,ID`: desactiva reglas, por ejemplo `VER-01` en un perfil regional con voseo.
- `--sin-nlp`: no usa spaCy ni Stanza aunque estén instalados.

Dentro de un archivo Markdown, puedes usar estos comentarios:

- `<!-- ets: perfil=interfaz -->` cambia el perfil desde esa línea.
- `<!-- ets: ignorar -->` ignora la línea siguiente.
- `<!-- ets: ignorar-inicio -->` y `<!-- ets: ignorar-fin -->` ignoran un bloque.

El verificador no analiza el texto entre comillas invertidas, los bloques de código, las URL, las rutas, las variables ni las etiquetas entre «».

### Pruebas y evaluación

```
python3 -m unittest discover tests
python3 evals/correr.py
```

Consulta `evals/README.md` para evaluar las reescrituras de un modelo.

## Ampliar el glosario

Cada entrada de `glosario.yaml` describe un concepto, no una palabra. Para añadir un concepto:

1. Copia una entrada existente y cambia el `id`.
2. Escribe el concepto en una frase y el término preferido.
3. Si los términos desaconsejados son correctos en otros contextos, escribe un `patron` con los objetos que delimitan el concepto: `revocar + token | certificado | permiso`. El verificador solo marca los desaconsejados cuando la oración contiene uno de esos objetos.
4. Escribe un ejemplo y un contraejemplo originales.
5. Ejecuta `python3 -m unittest discover tests`. Las pruebas comprueban que el `id` es único, que ningún término desaconsejado es preferido en otra entrada y que el ejemplo no genera errores.

Para un glosario propio del proyecto, crea un archivo con el mismo formato y pásalo con `--glosario`.

## Trabajos relacionados

ETS es un proyecto independiente con reglas, glosario y ejemplos propios. No reproduce contenido de los trabajos siguientes.

- ASD. *ASD-STE100 Simplified Technical English*, Issue 9, 2025. Lenguaje controlado de referencia para documentación técnica en inglés. ETS adapta algunos de sus principios generales a partir de descripciones funcionales; no incluye reglas, ejemplos ni entradas de su diccionario.
- Gobbi, Ilaria. *Español Técnico Simplificado*. Tesis doctoral, Universidad de Bolonia, 2014. Lenguaje controlado para documentación de mantenimiento aeronáutico en español.
- Ruiz-Cascales, R. *A Specification and Validating Parser for Simplified Technical Spanish*. Tesis de maestría, University of Limerick, 2002.
- *Español Técnico Controlado* (ETC): [github.com/PabloPC05/espanol-tecnico-controlado](https://github.com/PabloPC05/espanol-tecnico-controlado).
- UNE. *UNE-ISO 24495-1:2024. Lenguaje claro. Parte 1: Principios rectores y directrices*.

La investigación de base está en `docs/informe-base.md`. Las decisiones de diseño están en `docs/decisiones.md`.

## Límites

- La skill no sirve para textos creativos, comerciales o jurídicos, ni para lectura fácil.
- El verificador detecta problemas frecuentes con reglas y heurísticas. No comprueba la corrección técnica ni todas las ambigüedades. Por ejemplo, los referentes de pronombres (TER-08) y la modalidad (VER-09) requieren revisión humana o del modelo.
- Las convenciones de la versión 0.1 no se validaron todavía con lectores de distintos países.
- ETS no es una versión oficial de ASD-STE100 ni está afiliado a ASD, a la RAE ni a ninguna empresa.

## Licencias

- Reglas, glosario, ejemplos y documentación: [CC BY 4.0](LICENSE-texto).
- Código de `scripts/`, `tests/` y `evals/`: [MIT](LICENSE-codigo).
