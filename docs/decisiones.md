# Registro de decisiones

Estado de las decisiones de diseño de la sección 6 del informe de base, más las decisiones que se tomaron al construir la versión 0.1.

Estados posibles:

- **Decidida en v0.1**: la versión 0.1 aplica la decisión; puede cambiar con evidencia nueva.
- **Abierta**: falta información para decidir; la versión 0.1 usa una solución provisional.

## Decisiones de la sección 6 del informe

| Prioridad | Decisión | Estado | Decisión tomada | Cómo validarla |
|---|---|---|---|---|
| P0 | Relación con el ETS existente | Decidida en v0.1 | El proyecto conserva el nombre «ETS: Español Técnico Simplificado» por decisión del equipo. No reutiliza reglas, ejemplos ni entradas de la tesis de Gobbi y la cita como trabajo relacionado. | Revisar el nombre si el proyecto se publica fuera del equipo. |
| P0 | Objetivo principal | Decidida en v0.1 | Comprensión humana y ejecución correcta de tareas. La traducción automática es un objetivo secundario. | Pruebas de tarea con lectores: éxito, errores y tiempo. |
| P0 | Alcance de conformidad | Decidida en v0.1 | Un núcleo y cuatro perfiles: procedimientos, conceptos y API, interfaz y notas de versión. El resultado se expresa como «Revisado según la convención ETS v0.1», nunca como «conforme». | Clasificar un corpus real de documentación y medir cuántos fragmentos no encajan en un perfil. |
| P0 | Régimen legal | Decidida en v0.1 | Reglas, glosario y ejemplos originales. CC BY 4.0 para texto y MIT para código. Sin contenido de ASD-STE100, de Gobbi ni de ETC. | Revisión jurídica antes de una publicación amplia. |
| P0 | Preservación del significado | Decidida en v0.1 | Prioridad máxima, por encima de la brevedad. Lista de comprobación en `preservar-significado.md` y comparación de literales con `--original`. | Casos de prueba con condiciones, modalidades y efectos; revisión manual de reescrituras. |
| P1 | Tú o usted | Decidida en v0.1 | Tuteo. El perfil de «usted» está documentado en `variacion-regional.md`, pero el verificador no lo implementa. | Pruebas de naturalidad y aceptación por país. |
| P1 | Neutralidad o variantes | Decidida en v0.1 | Perfil internacional sin voseo ni «vosotros». Perfiles regionales solo cuando una elección cause fricción comprobada. | Evaluación regional de los términos de `variacion-regional.md`. |
| P1 | Restricciones verbales | Decidida en v0.1 | Reglas por función. El subjuntivo está permitido; se marca el gerundio de posterioridad y la pasiva perifrástica con agente; la pasiva refleja es aceptable para resultados. | Análisis de un corpus de procedimientos, API y notas de versión. |
| P1 | Polisemia | Decidida en v0.1 | Control por concepto. Cada entrada del glosario puede limitar sus desaconsejados con un patrón de objetos. | Ampliar el banco de casos ambiguos y medir falsos positivos por entrada. |
| P1 | Longitud | Decidida en v0.1 | Avisos, nunca rechazos: 25 palabras en procedimientos, 30 en descripciones, sin máximo en interfaz. El código no cuenta. | Comparar los umbrales con el desempeño de lectores reales. |
| P1 | Anglicismos | Decidida en v0.1 | Equivalente español si existe y es preciso; término inglés definido si es el nombre reconocido (`token`, `commit`, `endpoint`); sin híbridos verbales. | Pruebas de reconocimiento con desarrolladores de varios países. |
| P1 | Modelo de diccionario | Decidida en v0.1 | Glosario conceptual en YAML con 99 entradas, esquema fijo y pruebas de coherencia. | Prototipo de exportación a TBX; historial de cambios por entrada. |
| P2 | Automatización | Abierta | Verificador híbrido: reglas deterministas más análisis morfológico opcional con spaCy o Stanza. | Medir precisión y cobertura por regla en textos que no se usaron para escribir las reglas. |
| P2 | Traducción | Abierta | Sin evaluación en la versión 0.1. | Prueba ciega con poseditores, por dirección y por motor. |
| P2 | LLM | Decidida en v0.1 | El modelo redacta y propone; el verificador y la revisión humana comprueban. La skill nunca certifica. | Evaluación externa de reescrituras con `evals/correr.py --reescrituras`. |
| P2 | Gobernanza | Abierta | Reglas y glosario versionados en este repositorio, con cambios en `CHANGELOG.md`. | Definir quién aprueba cambios de reglas y con qué evidencia. |

## Decisiones tomadas durante la construcción de la versión 0.1

| Tema | Decisión | Motivo |
|---|---|---|
| Nombre | Se conserva «ETS» y el slug `ets`, aunque la especificación de la tarea pedía otro nombre. | Decisión explícita del equipo. |
| `revocar-credencial` | Los desaconsejados son solo «anular». La especificación proponía también «cancelar» e «invalidar». | «cancelar» es el término preferido para interrumpir una operación y «invalidar» es el preferido para la caché. Un término no puede ser desaconsejado en una entrada y preferido en otra. |
| Etiquetas de interfaz | El texto entre «» se protege y no se analiza. | Las etiquetas se copian literalmente (TER-05). Como consecuencia, las menciones metalingüísticas también deben ir entre «». |
| Ejemplos incorrectos | Las líneas que empiezan con «Incorrecto:», «Antes:», «Contraejemplo:», «Reescritura defectuosa:», «Ambiguo:» o «Reglas aplicadas:» no se analizan. | Permite verificar la documentación de la skill sin falsos errores. |
| YAML sin dependencias | `verificar.py` incluye un lector de un subconjunto de YAML. | Requisito de usar solo la biblioteca estándar. Una prueba compara el resultado con PyYAML cuando está instalado. |
| Términos compuestos | Los términos de varias palabras del glosario cuentan como una unidad para ORA-08, y un desaconsejado dentro de un término preferido no se marca. | Evita marcar «base de datos» o «pull request» como errores. |
| Voseo con pronombres | El verificador reconoce voseo con «lo», «la», «los», «las» y «te», pero no con «le», «les», «me» ni «nos». | Esas terminaciones producen adjetivos comunes, como «generales» o «iniciales». |
| `evals/correr.py` | Se añadió un script que no figuraba en la arquitectura de archivos. | La especificación pide correr los casos y medir precisión; el script lo automatiza. |
| Separador decimal | Punto decimal en prosa del perfil internacional (FOR-09). | Coincide con el código y los archivos de configuración. Un perfil regional puede elegir la coma. |

## Avisos del verificador sobre la propia skill

El verificador se ejecutó sobre `SKILL.md`, todos los archivos de `references/`, `README.md` y `evals/README.md`, con el perfil detectado y en modo estándar. Resultado: 0 errores y 0 advertencias. Quedan estas sugerencias, que se mantienen:

| Archivo | Regla | Fragmento | Motivo para mantenerla |
|---|---|---|---|
| `preservar-significado.md` | VER-06 | «esperará», «pensará» | Describen la reacción hipotética de un lector, no el comportamiento del sistema. |
| `nucleo/verbos-y-modalidad.md` | VER-06 | «rechazará» | Es el ejemplo correcto de VER-06: un futuro con fecha concreta. |
| `nucleo/terminologia-y-referentes.md` | TER-10 | «su firma» | Es el ejemplo de la excepción de TER-10: «su» con un solo dueño posible. La heurística cuenta determinantes, no dueños. |
| `variacion-regional.md` | TER-10 | «su variedad» | El único dueño posible es «el equipo». |
| `evals/README.md` | TER-10 | «su perfil» | El único dueño posible es «cada caso». |

## Limitaciones conocidas del verificador

- Analiza línea por línea: una oración partida en dos líneas se cuenta como dos oraciones.
- TER-08 (pronombres átonos), TER-07 (sujeto tácito) y VER-09 (modalidad) no se comprueban de forma automática.
- La detección de imperativos depende de una lista de verbos frecuentes y de los verbos del glosario.
- El análisis con spaCy y Stanza solo se usa para confirmar gerundios e infinitivos, y no se probó en esta versión porque ninguno estaba instalado en el entorno de desarrollo.
- Las métricas de `evals/` miden casos escritos junto con las reglas; no estiman la precisión sobre documentación real.
