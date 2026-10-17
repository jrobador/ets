---
name: ets
description: Redacta, reescribe y revisa documentación e interfaces de software en español técnico controlado (ETS), claro e inequívoco para lectores de España y Latinoamérica. Úsala cuando pidan «español técnico controlado», «español claro y técnico», «simplificar documentación», «reescribir instrucciones», «lenguaje controlado» o el «equivalente en español de Simplified Technical English», y también siempre que escribas en español procedimientos, guías de instalación, mensajes de error, textos de interfaz, documentación de API, README o notas de versión.
---

# ETS: Español Técnico Simplificado

ETS es una convención de español controlado para software. Su objetivo es que el lector entienda el texto y complete la tarea sin errores, en cualquier país hispanohablante.

Prioridades, de mayor a menor:

1. El significado técnico.
2. Los literales: código, identificadores, rutas, URL, variables y etiquetas de interfaz.
3. Un término por concepto.
4. Oraciones breves y simples.

Si dos reglas entran en conflicto, gana la de mayor prioridad. Nunca elimines una condición, una cifra o una advertencia para acortar una oración.

## Flujo de trabajo

1. **Detecta el perfil** de cada fragmento, o usa el que pida la persona:
   - procedimientos: pasos que el lector ejecuta;
   - conceptos y API: explicaciones, referencia, comentarios de código;
   - interfaz: botones, menús, mensajes de error, notificaciones;
   - notas de versión: cambios entre versiones.
2. **Protege los literales.** No cambies nada que esté entre comillas invertidas, en bloques de código, en URL, en `{variables}`, en opciones como `--force` ni en etiquetas entre «».
3. **Lee el archivo del perfil** en `references/perfiles/`. Lee los archivos del núcleo cuando una regla del perfil remita a ellos o cuando tengas dudas.
4. **Redacta o reescribe** con las reglas del perfil y del núcleo.
5. **Comprueba el significado.** Si reescribes un texto existente, aplica `references/preservar-significado.md`.
6. **Verifica.** Si tienes un entorno con Python 3.10 o posterior, ejecuta el verificador:
   ```
   python3 scripts/verificar.py ARCHIVO --perfil procedimientos
   python3 scripts/verificar.py NUEVO --original ORIGINAL
   ```
   La ruta `scripts/` es relativa a la carpeta de esta skill.
7. **Entrega** el texto y, aparte, los avisos clasificados en error, advertencia y sugerencia.

## Modos

| Modo | Cuándo usarlo | Qué cambia |
|---|---|---|
| Estándar (predeterminado) | Documentación habitual, revisiones rápidas. | Núcleo y perfil. Un término habitual es aceptable si no es ambiguo; el glosario solo produce sugerencias. |
| Estricto | Documentación que se traducirá, textos de seguridad, cuando la persona lo pida. | Todas las reglas. Para los conceptos del glosario, el término preferido es obligatorio. |

Indica el modo con `--modo estricto` en el verificador.

## Diez reglas esenciales

1. **Trata al lector de «tú».** No uses voseo ni «vosotros». No mezcles «tú» y «usted». (VER-01, VER-02, VER-03)
2. **Usa un término por concepto.** Elige el término preferido del glosario y no alternes sinónimos. (TER-01)
3. **Escribe la condición antes de la acción.** Si el token caducó, inicia sesión de nuevo. (ORA-02)
4. **Escribe una acción del lector por paso**, en imperativo. Escribe botones y títulos en infinitivo. (PRO-01, PRO-02, INT-01)
5. **Nombra al agente cuando importa.** Si el lector necesita saber quién actúa, escribe «El servidor valida el token», no «Se valida el token». (API-01, VER-14)
6. **Da a cada pronombre y a cada «su» un solo referente.** Si hay dos candidatos, repite el sustantivo. (TER-08, TER-10)
7. **Usa la modalidad exacta.** «Debes» es un requisito, «puedes» una capacidad, «se recomienda» una recomendación. No uses el condicional para suavizar. (VER-07, VER-09)
8. **Usa el verbo de la acción.** Escribe «Actualiza la configuración», no «Realiza la actualización de la configuración». Revisa las cadenas de tres o más «de». (ORA-07, ORA-08)
9. **Revisa las oraciones largas.** Procedimientos: más de 25 palabras. Descripciones: más de 30. Si puedes dividir la oración sin perder información, divídela. (ORA-03, ORA-04)
10. **Copia los literales exactos.** Escribe el código entre comillas invertidas y las etiquetas entre «». Deja un espacio entre la cifra y la unidad. (FOR-03, FOR-05, FOR-06, FOR-07)

## Qué archivo leer

| Situación | Archivo |
|---|---|
| Pasos, instalación, configuración, solución de problemas | `references/perfiles/procedimientos.md` |
| Explicaciones, referencia de API, README, comentarios de código | `references/perfiles/conceptos-y-api.md` |
| Botones, menús, errores, notificaciones, cadenas de localización | `references/perfiles/interfaz-y-mensajes.md` |
| Notas de versión, registro de cambios, avisos de obsolescencia | `references/perfiles/notas-de-version.md` |
| Elegir un término, pronombres, posesivos, sujeto tácito | `references/nucleo/terminologia-y-referentes.md` |
| Tiempos verbales, subjuntivo, modalidad, pasiva, gerundio | `references/nucleo/verbos-y-modalidad.md` |
| Longitud, condiciones, nominalizaciones, género y plantillas | `references/nucleo/oraciones.md` |
| Mayúsculas, puntuación, números, unidades, fechas, código | `references/nucleo/formato.md` |
| Término de un concepto concreto | `references/glosario.yaml` |
| Variantes regionales, perfil de «usted», voseo | `references/variacion-regional.md` |
| Reescribir un texto existente | `references/preservar-significado.md` |
| Ver ejemplos de antes y después | `references/ejemplos.md` |

Si el proyecto tiene su propio glosario, ese glosario tiene prioridad sobre `glosario.yaml`.

## Cómo entregar

Entrega primero el texto final. Después, si revisaste o reescribiste un texto, añade una sección de avisos:

- **Errores**: problemas que debes corregir, como un literal alterado o una unidad mal escrita.
- **Advertencias**: problemas probables que requieren criterio, como un referente dudoso o una oración larga.
- **Sugerencias**: mejoras opcionales.

Para cada aviso, indica el ID de la regla, el fragmento y la corrección propuesta. Si un cambio puede alterar el significado técnico, pregunta en lugar de decidir.

Al terminar, escribe «Revisado según la convención ETS v0.1». No escribas que un texto es «conforme» ni que está «certificado». El verificador y esta skill detectan problemas frecuentes, pero no garantizan la corrección técnica ni la ausencia de ambigüedad.

## Límites

Esta skill no sirve para:

- textos creativos, publicitarios o de marketing;
- textos jurídicos, contratos o políticas legales;
- lectura fácil para personas con dificultades de comprensión, que sigue otras pautas;
- traducción literal que deba conservar la estructura del original.

ETS es un proyecto independiente. No es una versión oficial de ASD-STE100 ni está afiliado a ASD, a la RAE ni a ninguna empresa.
