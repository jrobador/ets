# Bases para un español técnico simplificado de software y técnica general

Fecha de corte: 16 de octubre de 2026.

Este informe distingue tres niveles: «documentado» identifica información respaldada por las fuentes consultadas; «inferencia» señala una conclusión razonada a partir de esas fuentes; «propuesta» identifica decisiones preliminares para el nuevo proyecto. Las propuestas no constituyen reglas de ASD-STE100 ni recomendaciones oficiales de la RAE.

## 1. Resumen ejecutivo

**Conclusión:** el proyecto es viable, pero conviene diseñarlo como un lenguaje controlado propio del español y del software, no como una traducción ni una correspondencia regla por regla con ASD-STE100. Además, existe un antecedente directo que cambia el punto de partida: Ilaria Gobbi presentó en la Universidad de Bolonia, en 2014, una tesis titulada *Español Técnico Simplificado*, con reglas y diccionario basados en corpus. Antes de elegir el nombre definitivo y redactar la especificación, corresponde estudiar ese trabajo y diferenciar explícitamente el nuevo alcance. [amsdottorato.unibo](https://amsdottorato.unibo.it/id/eprint/6681/1/Tesi_Gobbi_ETS.pdf)

Los principios más transferibles son la consistencia terminológica, las instrucciones con acciones identificables, la separación entre procedimientos y explicaciones, las condiciones explícitas, la prevención de referencias ambiguas y el uso de un vocabulario general acompañado por terminología técnica del dominio. ASD-STE100 ya distingue entre palabras generales aprobadas y sustantivos o verbos técnicos que pueden incorporarse bajo condiciones definidas. [asd-ste100](https://www.asd-ste100.org/about_STE.html)

No conviene trasladar mecánicamente las restricciones del inglés. El español requiere decisiones propias sobre flexión, sujeto tácito, clíticos, pasiva refleja, concordancia, subjuntivo y tratamiento al usuario. Un ejemplo decisivo: prohibir el subjuntivo impediría instrucciones normales como «No cierres la ventana» y las formas de mandato de usted. La RAE distingue, además, entre el imperativo dirigido a una persona y el infinitivo exhortativo válido en instrucciones generales. [rae](https://www.rae.es/espanol-al-dia/infinitivo-por-imperativo)

Para software, la especificación necesita perfiles diferenciados: procedimientos, documentación conceptual/API, interfaz y mensajes, y notas de versión. Un botón como «Guardar» no debe evaluarse como una oración incompleta; una nota de versión necesita pasado; una API debe conservar literalmente identificadores y valores. Esta separación es una propuesta de diseño, apoyada en la diversidad de contenidos que cubren las guías industriales consultadas. [support.apple](https://support.apple.com/guide/applestyleguide/welcome/web)

«Español neutro» debe definirse como un perfil editorial comprensible internacionalmente, no como un dialecto único ni como sinónimo de `es-419`: este último identifica español latinoamericano y no incluye España. La guía neutral de Microsoft ofrece un antecedente operativo, pero también muestra que sus decisiones dependen del producto y de la época. [download.microsoft](https://download.microsoft.com/download/4/3/1/431d9836-40dc-4f2b-aafc-def5c7b5d0f3/spa-neu-StyleGuide.pdf)

La evidencia de eficacia es favorable, pero condicional. Las investigaciones sobre comprensión no demuestran ventajas uniformes en todos los textos ni reducciones sistemáticas del tiempo. En traducción automática, una regla beneficiosa para sistemas antiguos puede resultar neutra o perjudicial para un sistema neuronal. No hay base para prometer un porcentaje general de ahorro para un nuevo español controlado de software. [shs.hal](https://shs.hal.science/halshs-01379559/document)

La vía recomendada es desarrollar una especificación independiente, un diccionario organizado por conceptos, un verificador híbrido y un corpus de evaluación con lectores de España y Latinoamérica. Los modelos de lenguaje pueden proponer y revisar borradores, pero no deben certificar por sí solos la conformidad ni la preservación del significado.

***

## 2. ASD-STE100: historia, estructura, alcance y evidencia

### 2.1. Historia, responsable y edición vigente

La historia oficial permite distinguir varios hitos, que a veces se confunden al resumir el origen del estándar: [asd-ste100](https://www.asd-ste100.org/about_STE.html)

| Fecha | Hito |
|---|---|
| 1979 | La Association of European Airlines solicita a AECMA una solución común para mejorar la comprensión de manuales de mantenimiento en inglés. |
| 1981 | AECMA decide desarrollar su propio lenguaje controlado. |
| 1983 | Se constituye formalmente el Simplified English Working Group. |
| 1986 | Se publica la primera guía AECMA Simplified English. |
| 2004–2005 | La creación de ASD conduce al cambio de denominación y a la etapa ASD-STE100. |
| 2017 | Se publica Issue 7. |
| Abril de 2021 | Se publica Issue 8. |
| 15 de enero de 2025 | Se publica Issue 9, vigente según el sitio oficial consultado. |

La propiedad corresponde a la Aerospace, Security and Defence Industries Association of Europe, ASD. El grupo STEMG —Simplified Technical English Maintenance Group— desarrolla, publica y mantiene el documento, con apoyo de equipos nacionales y multinacionales. [asd-ste100](https://www.asd-ste100.org/about_STE.html)

Issue 9 se presenta como *Standard for technical documentation*. Esa denominación no significa que ASD-STE100 sea una norma ISO: es un estándar de ASD, aunque esté relacionado y alineado con otras normas internacionales. [asd-ste100](https://www.asd-ste100.org/about_STE.html)

### 2.2. Cambios entre ediciones

La comparación reciente mejor documentada es Issue 8 → Issue 9. ASD informa que no se añadieron nuevas reglas sustantivas: se mantuvieron 53 reglas, con cambios de redacción en 31 y actualización de 555 entradas del diccionario, incluidos significados y ejemplos. [asd-europe](https://www.asd-europe.org/news-media/news-events/news/simplified-technical-english-asd-ste100-issue-9/)

Entre los cambios relevantes de Issue 9 figuran:

- Sustitución de la denominación anterior *technical name* por *technical noun*.
- Revisión de la terminología metalingüística.
- Ampliación a 22 categorías de sustantivos técnicos.
- Reorganización de una regla sobre artículos y demostrativos.
- Revisión del cómputo de determinadas unidades textuales.
- Nuevas recomendaciones generales sobre lenguaje inclusivo y posesivos.
- Una lista de verbos aprobados como ayuda de consulta. [asd-ste100](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)

Para ediciones más antiguas, este informe no presenta una comparación exhaustiva de altas, bajas y modificaciones: requeriría cotejar cada edición. Para el proyecto importa registrar la edición de origen de cada análisis, porque una descripción basada en Issue VI, como la tesis de Gobbi, no equivale a una descripción de Issue 9. [amsdottorato.unibo](https://amsdottorato.unibo.it/id/eprint/6681/1/Tesi_Gobbi_ETS.pdf)

### 2.3. Estructura de las reglas, por categoría

La siguiente descripción es funcional y parafraseada; no reproduce el articulado.

| Categoría de ASD-STE100 | Función del control | Implicación para software |
|---|---|---|
| 1. Palabras | Seleccionar vocabulario general y regular el empleo de términos técnicos. | Separar vocabulario común, terminología informática y nombres propios del producto. |
| 2. Sustantivos de varias palabras | Reducir la dificultad de grupos nominales complejos. | Controlar términos compuestos y cadenas como «configuración de la política de acceso del servicio». |
| 3. Verbos | Limitar construcciones y hacer identificables las acciones y sus responsables. | Diferenciar acciones del usuario, del cliente, del servidor y de procesos automáticos. |
| 4. Oraciones | Evitar estructuras difíciles o ambiguas y explicitar relaciones. | Aclarar condiciones, alternativas y referencias. |
| 5. Procedimientos | Presentar instrucciones ejecutables en secuencia. | Separar acciones, requisitos previos y resultados esperados. |
| 6. Descripciones | Explicar funcionamiento y propiedades mediante unidades manejables. | Documentar comportamiento, arquitectura y contratos de API. |
| 7. Instrucciones de seguridad | Comunicar riesgos y formas de evitarlos. | Adaptar a pérdida de datos, credenciales, disponibilidad y operaciones irreversibles. |
| 8. Puntuación y cómputo | Estabilizar la segmentación y la medición del texto. | Definir tratamiento de código, rutas, unidades, etiquetas y variables. |
| 9. Prácticas de escritura | Orientar la reformulación y la consistencia del documento. | Incorporar revisión técnica, terminológica y de usabilidad. |

Estas nueve categorías corresponden a la estructura de Issue 9. [asd-ste100](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)

### 2.4. Lógica del diccionario

El diccionario contiene aproximadamente 900 palabras generales aprobadas y unas 1200 no aprobadas con alternativas o indicaciones de reformulación. Las palabras aprobadas se vinculan, en general, a un significado y una categoría gramatical determinados. [asd-ste100](https://www.asd-ste100.org/about_STE.html)

La precisión «en general» es importante: no debe convertirse el principio pedagógico «una palabra, un significado» en una descripción absoluta de todas las entradas. El propio historial de Issue 9 registra casos con más de un significado aprobado o entradas diferenciadas por categoría. [asd-ste100](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)

El sistema combina:

1. Vocabulario general controlado.
2. Sustantivos técnicos del sector, la empresa o el proyecto.
3. Verbos técnicos admitidos conforme a sus condiciones de uso.

Por tanto, el diccionario general no pretende contener todos los componentes, materiales, procesos o conceptos especializados que puedan aparecer en un manual. [asd-ste100](https://www.asd-ste100.org/STE_faq.html)

Inferencia para el proyecto: el mecanismo importante no es alcanzar una cifra determinada de palabras, sino poder justificar qué significa cada entrada, dónde se permite y cómo se comprueba.

### 2.5. Principios centrales

STE combina restricciones léxicas con reglas de construcción: consistencia de significado, reducción de sinonimia, oraciones breves, preferencia por acciones explícitas, imperativo en procedimientos y separación de instrucciones. Los límites habitualmente asociados al estándar son 20 palabras para oraciones procedimentales y 25 para descriptivas; deben interpretarse junto con sus convenciones de cómputo, no como un conteo informal de espacios. [asd-ste100](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)

Dos precisiones:

- «Una instrucción» no equivale necesariamente a «un verbo»: una condición puede contener un verbo sin añadir una segunda acción exigida al lector.
- «Voz activa» no significa que todo estado o resultado deba reformularse artificialmente como una acción.

La segunda distinción también aparece en guías de software: Google prefiere la activa, pero permite la pasiva cuando el agente es irrelevante o el objeto merece el foco. [developers.google](https://developers.google.com/style/voice)

### 2.6. Uso fuera de la aeronáutica y en TI

ASD documenta expansión hacia defensa, ferrocarril, automoción, petróleo y gas, TI y dispositivos médicos. Esto respalda el uso intersectorial, pero no demuestra por sí solo una adopción generalizada en documentación de API o en interfaces de software. [asd-europe](https://www.asd-europe.org/standards-specifications/simplified-technical-english/)

La distinción necesaria es:

- Uso de STE para documentar software.
- Uso de software para verificar STE.
- Uso de principios parecidos a STE en una guía editorial.

Son fenómenos diferentes. Por ejemplo, un comprobador integrado en un editor XML constituye una herramienta de aplicación del estándar, no un caso de adopción de STE por toda la documentación de ese editor. [oxygenxml](https://www.oxygenxml.com/addons/oxygen-terminology-checker-asd-ste100-styleguide.html)

En la búsqueda aparecieron iniciativas comunitarias recientes orientadas a código y agentes, como STE-Code. Sirven como indicios de experimentación, no como evidencia de eficacia ni de adopción industrial consolidada. [github](https://github.com/NikolaRHristov/STE-Code)

### 2.7. Evidencia empírica: qué se puede afirmar

| Línea de evidencia | Resultado documentado | Límite para este proyecto |
|---|---|---|
| Comprensión de documentación de mantenimiento | Una revisión de 2016 identifica mejoras significativas en algunos estudios, especialmente según complejidad y tipo de documento. Otros no encuentran superioridad general. | No permite asumir el mismo efecto en botones, mensajes breves o API. |
| Tiempo de comprensión | La misma revisión no encuentra mejoras significativas de tiempo consistentes en los estudios examinados. | «Más corto» no garantiza «más rápido». |
| KANT y documentación industrial | Un informe de 1997 describe textos que requerían cerca de una hora de traducción manual y entre 10 y 15 minutos de posedición. | Resultado histórico de un sistema y un dominio concretos, no estimación actual universal. |
| Traducción estadística | Microsoft Research estudió reglas de lenguaje controlado en traducciones a neerlandés, chino, árabe y francés, con evaluación humana, BLEU y distancia de edición. | No incluía español ni los sistemas actuales. |
| Comparación de sistemas, incluido neuronal | Un estudio publicado en 2021 encuentra efectos distintos por regla y sistema, con reglas positivas, negativas y sin efecto significativo. | No se debe aprobar una regla solo porque funcionó para traducción basada en reglas. |

Fuentes: revisión de comprensión; informe KANT; investigación de Microsoft; estudio de Marzouk. [shs.hal](https://shs.hal.science/halshs-01379559/document)

El estudio de Marzouk utilizó 216 oraciones alemanas, nueve reglas y cinco sistemas, con traducciones realizadas a finales de 2016. Es evidencia relevante contra las generalizaciones, pero tampoco constituye una evaluación de los motores de 2026. [link.springer](https://link.springer.com/article/10.1007/s10590-021-09266-0)

No se ha identificado aquí un ensayo que demuestre un porcentaje de ahorro para un español controlado de documentación de software con el alcance propuesto.

***

## 3. Estado del arte

### 3.1. Lenguajes controlados industriales y traducción automática

Conviene separar dos orientaciones:

- Lenguajes orientados principalmente a personas: buscan comprensión, ejecución correcta y reducción de errores.
- Lenguajes orientados al procesamiento automático: buscan análisis predecible, traducción o representación formal.

Pueden compartir reglas, pero no necesariamente optimizan lo mismo. La investigación sobre mensajes de cabina muestra precisamente que un código muy abreviado puede necesitar más entrenamiento que una formulación natural explícita. [shs.hal](https://shs.hal.science/halshs-01379559/document)

#### Caterpillar y KANT

Caterpillar Technical English se desarrolló en relación con una arquitectura de producción y traducción de documentación. KANT utilizaba vocabulario y gramática controlados junto con modelos semánticos del dominio. El control no se limitaba a «escribir frases cortas»: restringía interpretaciones para facilitar el análisis y la generación multilingüe. [lti.cs.cmu](https://www.lti.cs.cmu.edu/research/research-articles/kant.html)

Una publicación de 1999 documenta su uso productivo para traducciones al francés y al español. Esto constituye un antecedente sólido de español como lengua de destino de una cadena industrial controlada; no implica que el español resultante fuese un estándar independiente equivalente a STE. [aclanthology](https://aclanthology.org/www.mt-archive.info/90/MTS-1999-Mitamura.pdf)

#### Otros antecedentes útiles

La literatura recoge Français Rationalisé, lenguajes industriales suecos, Controlled Automotive Service Language, IBM EasyEnglish y propuestas para requisitos de software. Debe evitarse tratarlos como sistemas equivalentes: varían en finalidad, formalización, alcance y mantenimiento. [amsdottorato.unibo](https://amsdottorato.unibo.it/id/eprint/6681/1/Tesi_Gobbi_ETS.pdf)

Dos referencias especialmente pertinentes:

- Français Rationalisé: antecedente de control técnico en una lengua romance.
- Italiano Tecnico Semplificato: antecedente de reformulación específica para otra lengua romance y de mantenimiento institucional. [air.uniud](https://air.uniud.it/retrieve/da459f9d-3c53-469c-934f-4fc642dc46e2/vezzani-vecchiato-frattolin-pubblicato-2025.aielpl-1.3.pdf)

La lección no es copiar sus restricciones, sino estudiar qué fenómenos lingüísticos decidieron controlar y cómo gobernaron las actualizaciones.

### 3.2. Guías de software: coincidencias y diferencias con STE

Las guías empresariales no son, en general, lenguajes controlados cerrados con un diccionario exhaustivo de palabras permitidas.

| Guía | Coincidencias con STE | Diferencia relevante |
|---|---|---|
| Microsoft Writing Style Guide | Palabras precisas, consistencia, frases concisas, cuidado con la polisemia y la jerga. | Usa contexto y estructura para desambiguar; no exige una categoría única para cada palabra. |
| Google Developer Documentation Style Guide | Activa, presente para comportamiento general, segunda persona, claridad para traducción. | Admite excepciones razonadas y se centra en documentación para desarrolladores. |
| Apple Style Guide | Consistencia en documentación, referencias, formación e interfaz. | Combina convenciones editoriales y de producto; incluye preferencias de voz propias del inglés. |
| IBM Style | Terminología, puntuación, marcado, paralelismo y uso apropiado de activa/pasiva. | Es una guía editorial corporativa amplia. |
| Red Hat Supplementary Style Guide | Consistencia, procedimientos, lenguaje internacional y reducción de ambigüedad. | Se aplica junto con IBM Style y guías específicas del producto. |

Fuentes: Microsoft, Google, Apple, IBM y Red Hat. [support.apple](https://support.apple.com/guide/applestyleguide/welcome/web)

Hay desacuerdos que impiden construir una «regla industrial universal». Microsoft y Apple permiten o recomiendan contracciones en determinados contextos ingleses; Red Hat las evita en documentación de producto para reducir ambigüedad y facilitar la traducción. [redhat-documentation.github](https://redhat-documentation.github.io/supplementary-style-guide/)

Propuesta: seleccionar principios por su función y validarlos en español, en lugar de sumar prescripciones de varias empresas.

### 3.3. Guías de localización al español

Microsoft ofrece un caso especialmente útil porque publica tanto una guía neutral como otra para España. La neutral define su objetivo como encontrar formulaciones comprensibles para una audiencia multinacional; ejemplifica la sustitución de computadora/computador/ordenador por «equipo» o «PC». [download.microsoft](https://download.microsoft.com/download/4/3/1/431d9836-40dc-4f2b-aafc-def5c7b5d0f3/spa-neu-StyleGuide.pdf)

También documenta una distribución histórica de tú y usted según producto. Sus referencias a Windows 8, Lync y otras líneas muestran por qué no debe usarse esa tabla como inventario vigente en 2026. La guía de España consultada incorpora contenidos más recientes, como indicaciones sobre Copilot, pero no presenta en el extracto recuperado una fecha editorial inequívoca. [download.microsoft](https://download.microsoft.com/download/4/3/1/431d9836-40dc-4f2b-aafc-def5c7b5d0f3/spa-neu-StyleGuide.pdf)

Conclusiones documentales:

- Hay evidencia de adopción del tuteo en grandes productos.
- No hay uniformidad histórica ni transversal.
- Estas guías no demuestran la aceptación del tratamiento en cada país.
- Una guía localizada en una página web no debe confundirse con una guía normativa específica para redactar en español.

Para Apple, Google, IBM y Red Hat, las fuentes verificadas aquí permiten analizar sus guías generales; no permiten atribuirles una política panhispánica única de tratamiento al usuario.

### 3.4. Antecedentes directos en español

#### Ilaria Gobbi: Español Técnico Simplificado, 2014

Es el antecedente prioritario. La tesis:

- Se presentó en Bolonia en 2014, bajo la dirección de María Pilar Capanaga Caballero.
- Se redactó en italiano.
- Propuso una guía con reglas de escritura y diccionario.
- Utilizó un corpus de mantenimiento aeronáutico en español.
- Tomó como referencia ASD-STE100 Issue VI.
- Planteó la traducibilidad entre español controlado e inglés controlado. [amsdottorato.unibo](https://amsdottorato.unibo.it/id/eprint/6681/1/Tesi_Gobbi_ETS.pdf)

Incluye decisiones como límites de 25 palabras para procedimientos y 30 para descripciones, restricciones verbales y control de cadenas preposicionales. Esas decisiones son antecedentes, no parámetros ya validados para software. [amsdottorato.unibo](https://amsdottorato.unibo.it/id/eprint/6681/1/Tesi_Gobbi_ETS.pdf)

Hay además una explicación de la autora en la revista del Colegio de Traductores Públicos de la Ciudad de Buenos Aires, número 141, páginas 24–27. El artículo describe el corpus, la estructura y los objetivos; sus afirmaciones de ahorro no sustituyen una evaluación experimental comparativa. [biblio.traductores.org](http://biblio.traductores.org.ar/documentos/07777.pdf)

La ficha de *New Voices in Translation Studies* muestra una fecha de publicación web de 2023, pero pertenece al volumen 13 de 2015 y resume una tesis terminada en 2014. Es importante conservar esa cronología correcta. [newvoices.arts.chula.ac](https://newvoices.arts.chula.ac.th/index.php/en/article/download/296/295/447)

#### Ruiz-Cascales: Simplified Technical Spanish, 2002

Una publicación alojada por NIST referencia:

*Ruiz-Cascales, R. (2002). A Specification and Validating Parser for Simplified Technical Spanish. M.Sc. Thesis, University of Limerick, Ireland.* [trec.nist](https://trec.nist.gov/pubs/trec11/papers/ulimerick.sutcliffe.pdf)

La tesis de Gobbi lo estudia como antecedente, especialmente por el parser de validación. No se ha recuperado aquí la tesis original completa; por eso no corresponde atribuirle un inventario detallado de reglas ni resultados no verificados. [amsdottorato.unibo](https://amsdottorato.unibo.it/id/eprint/6681/1/Tesi_Gobbi_ETS.pdf)

#### Implicación para el proyecto

No sería correcto presentar la iniciativa como «el primer español técnico simplificado». Una formulación defendible sería:

> Un lenguaje controlado de español internacional para documentación e interfaces de software, desarrollado con reglas propias y evaluación empírica.

El nombre definitivo debería diferenciarse del ETS de Gobbi.

### 3.5. Lectura fácil, lenguaje claro y lenguaje técnico controlado

| Enfoque | Objetivo principal | Público y método | Qué no garantiza |
|---|---|---|---|
| Lectura fácil | Accesibilidad de la información escrita para personas con dificultades de comprensión. | Reglas de redacción y diseño, con validación de comprensibilidad. | Precisión terminológica suficiente para cualquier especialidad. |
| Lenguaje claro | Que el público previsto encuentre, comprenda y utilice la información. | Redacción, estructura y diseño centrados en lectores y tareas. | Vocabulario cerrado ni conformidad automática. |
| Lenguaje técnico controlado | Reducir variación y ambigüedad mediante restricciones explícitas. | Reglas lingüísticas y terminológicas de un dominio. | Accesibilidad cognitiva universal ni corrección técnica del contenido. |

Estas diferencias se apoyan en UNE 153101:2018 EX, ISO 24495-1:2023 y la literatura sobre lenguajes controlados. [air.uniud](https://air.uniud.it/retrieve/da459f9d-3c53-469c-934f-4fc642dc46e2/vezzani-vecchiato-frattolin-pubblicato-2025.aielpl-1.3.pdf)

Normas pertinentes:

- UNE 153101:2018 EX: *Lectura Fácil. Pautas y recomendaciones para la elaboración de documentos*.
- ISO 24495-1:2023: principios rectores y directrices de lenguaje claro.
- UNE-ISO 24495-1:2024: adopción española de esa norma. [une](https://www.une.org/encuentra-tu-norma/busca-tu-norma/norma?c=N0060036)

ISO 24495-1 contempla expresamente la aplicabilidad a redacción técnica y lenguajes controlados. Por tanto, lenguaje claro y control técnico pueden complementarse. [iso](https://www.iso.org/standard/78907.html)

Como recursos públicos, la Red Argentina de Lenguaje Claro y las guías de contenidos digitales de Argentina.gob.ar aportan métodos de orientación al usuario. Sus elecciones regionales deben distinguirse de los principios generales transferibles. [argentina.gob](https://www.argentina.gob.ar/noticias/la-red-argentina-de-lenguaje-claro-llego-wikipedia)

***

## 4. Tabla de adaptación de principios de STE

La tabla evalúa principios y categorías; no reproduce las 53 reglas ni pretende constituir una traducción normativa.

| Principio o mecanismo | Dictamen | Justificación para español y software | Ejemplo propuesto |
|---|---|---|---|
| Vocabulario general controlado | Se traslada igual | Es un mecanismo útil de consistencia y auditabilidad. | Preferir «usar» de forma estable cuando no haya diferencia conceptual con «utilizar». |
| Reducir sinonimia para un mismo concepto | Se traslada igual | Evita que el lector interprete diferencias inexistentes. | Usar «archivo», no alternar con «fichero» por variedad estilística. |
| Una palabra, un significado | Se adapta | Debe aplicarse por dominio y entrada conceptual, no como prohibición universal de polisemia. | «Ejecutar» una orden o programa; no «ejecutar una factura». |
| Una categoría gramatical aprobada | Se adapta | La flexión y los participios requieren un modelo más rico. | Registrar «guardar» y el estado «guardado» con usos definidos. |
| Sustantivos técnicos fuera del núcleo general | Se traslada igual | El vocabulario de producto no cabe en un núcleo cerrado. | «token de acceso», definido en el glosario. |
| Verbos técnicos autorizados | Se adapta | Deben documentarse argumentos, régimen y efecto. | «Compilar el proyecto», «revocar el token». |
| Grupos nominales ingleses | Se reemplaza | El problema español principal incluye cadenas preposicionales y adjunciones ambiguas. | «Configura cuánto duran los tokens de acceso». |
| Evitar jerga y modismos innecesarios | Se traslada igual | Reduce dependencia regional y cultural. | «El servidor no responde», no «el servidor se colgó». |
| Formas verbales limitadas | Se adapta | Las necesidades cambian según género textual. | Presente en referencia; pasado en notas de versión. |
| Restricciones inglesas sobre formas en *-ing* | No aplica | No existe equivalencia directa con el gerundio español. | Crear una regla propia para evitar «Instala el paquete reiniciando después». |
| Voz activa | Se adapta | Prioridad cuando importa el agente; no prohibición de toda pasiva refleja. | «El servicio elimina los registros». |
| Imperativo procedimental | Se adapta | Exige elegir tratamiento y distinguir instrucciones de etiquetas. | «Abre el archivo»; botón «Abrir». |
| Una instrucción por oración | Se traslada igual | Facilita secuenciación y verificación. | «Guarda el archivo. Reinicia el servicio». |
| Una acción por paso | Se adapta | Puede haber subpasos y un resultado observado sin otra acción. | «Selecciona «Guardar». Aparece un mensaje de confirmación». |
| Condición antes de la acción | Se traslada igual | Evita ejecutar una acción antes de leer su condición. | «Si el token caducó, inicia sesión de nuevo». |
| Límites ingleses de 20/25 palabras | Se adapta | Necesitan corpus, tokenización y ensayos propios. | Avisar por longitud; no recortar información para cumplir. |
| Un tema por párrafo | Se traslada igual | Es compatible con descripción técnica y ayuda. | Un párrafo para autenticación y otro para permisos. |
| Número máximo de oraciones por párrafo | Se adapta | Tablas y referencias API requieren otros formatos. | Separar parámetros, resultado y errores. |
| Evitar omisiones que dificultan entender | Se traslada igual | La concisión no justifica un estilo telegráfico en prosa. | «El servidor devuelve un error», no «Servidor devuelve error». |
| Referencias pronominales inequívocas | Se adapta | Debe abarcar clíticos, sujeto tácito y posesivos. | «Elimina el token», si «elimínalo» puede referirse a dos objetos. |
| Avisos antes del riesgo | Se adapta | Deben incorporar pérdida de datos y seguridad informática. | «Esta operación elimina las copias. Crea una copia externa antes de continuar». |
| Categorías de seguridad aeronáutica | Se reemplaza | No deben trasladarse automáticamente a cualquier mensaje de software. | Definir «Advertencia», «Importante» y «Nota» por función y gravedad. |
| Puntuación y mayúsculas | Se reemplaza | Deben seguir convenciones españolas y excepciones técnicas explícitas. | «Configuración de la cuenta», no mayúsculas de título inglesas. |
| Cómputo especial de palabras | Se reemplaza | Código, etiquetas y clíticos exigen convenciones propias. | Analizar por separado `GET /users/{id}` y su explicación. |
| Reformular antes de inventar vocabulario | Se traslada igual | Evita términos artificiales o innecesarios. | «Escribe la contraseña», no «efectúa la introducción de la contraseña». |
| Revisión y mantenimiento | Se traslada igual | Las reglas deben evolucionar con evidencia y cambios de producto. | Versionar reglas, glosario y excepciones. |

Base documental de los mecanismos de STE: Issue 9 y sus explicaciones oficiales. Las decisiones y los ejemplos de adaptación son propuestas de este informe. [asd-ste100](https://www.asd-ste100.org/STE_faq.html)

***

## 5. Propuesta preliminar de convenciones

### 5.1. Arquitectura: un núcleo y cuatro perfiles

Propuesta:

1. Núcleo común: precisión, terminología, referencias, ortografía y preservación del significado.
2. Procedimientos: acciones, condiciones, secuencia, resultados y riesgos.
3. Conceptos y API: contratos, estados, agentes, posibilidades y requisitos.
4. Interfaz y mensajes: etiquetas, brevedad contextual, accesibilidad y recuperación.
5. Notas de versión: cambios, fechas, versiones y efectos de actualización.

La utilidad de separar tipos de contenido se desprende de las diferencias funcionales que cubren las guías de Apple, IBM y Red Hat, pero esta arquitectura concreta es propia. [support.apple](https://support.apple.com/guide/applestyleguide/welcome/web)

### 5.2. Definición operativa de español neutro

Propuesta de definición:

> Variedad editorial de español escrito que prioriza la comprensión de los públicos previstos en España y Latinoamérica, evita marcas regionales innecesarias y mantiene elecciones terminológicas estables, sin afirmar que esas elecciones sean las únicas correctas.

No se deben confundir:

- `es`: código de lengua sin región explícita.
- `es-ES`: español de España.
- `es-419`: español de Latinoamérica.
- «Neutro/internacional»: objetivo editorial, no garantía contenida en una etiqueta de idioma. [cldr.unicode](https://cldr.unicode.org/downloads/cldr-46)

El español del doblaje tampoco debe tomarse como norma de software: aquí la selección debe responder a tareas, objetos y conceptos técnicos, no a una convención audiovisual.

Propuesta de localización: mantener una base compartida y permitir perfiles regionales cuando una elección cause fricción relevante o cuando deban cambiar formatos. Neutralidad léxica no implica imponer un único separador decimal, moneda o formato de fecha a todos los usuarios.

### 5.3. Tratamiento e instrucciones

Propuesta inicial:

| Contexto | Convención | Ejemplo |
|---|---|---|
| Procedimiento dirigido al lector | Imperativo de tú | «Selecciona la cuenta». |
| Botón o acción de menú | Infinitivo | «Seleccionar cuenta». |
| Título de tarea | Infinitivo | «Configurar la autenticación». |
| Descripción del sistema | Presente y agente explícito cuando sea relevante | «El servidor valida el token». |
| Estado o resultado | Construcción natural y breve | «Los cambios se guardaron». |
| Prohibición | Imperativo negativo de tú | «No cierres la ventana». |

La RAE admite el infinitivo exhortativo en instrucciones generales; elegir imperativo para los pasos no convierte «Hacer clic en…» en incorrecto en todos los contextos. Es una decisión editorial de consistencia. [rae](https://www.rae.es/espanol-al-dia/infinitivo-por-imperativo)

Para reducir marcas regionales:

- No usar voseo en el perfil internacional.
- No usar vosotros.
- Evitar escribir «tú» de manera repetitiva: la flexión suele bastar.
- Usar plural con ustedes cuando realmente se dirija a varias personas.
- No mezclar tú y usted dentro de un mismo perfil de producto.

La exclusión del voseo no implica considerarlo incorrecto: la RAE reconoce formas voseantes de la norma culta. [rae](https://www.rae.es/dpd/ayuda/modelos-de-conjugacion-verbal)

El tuteo es una hipótesis editorial razonable, no un resultado demostrado de preferencia panhispánica. Si el producto exige usted, debe existir un perfil completo y coherente, no una sustitución ocasional.

### 5.4. Léxico regional: selección por concepto

| Variación | Propuesta inicial | Precaución |
|---|---|---|
| computadora / computador / ordenador | «equipo» cuando sea preciso; término específico cuando haga falta | «Equipo» también puede significar grupo de personas o conjunto de dispositivos. |
| archivo / fichero | «archivo» | Conservar literalmente etiquetas ajenas que digan «Fichero». |
| celular / móvil | «teléfono» o «teléfono móvil», según el concepto | «Dispositivo» no siempre equivale a teléfono. |
| hacer clic / pulsar / presionar | «seleccionar» para acciones independientes del dispositivo | No sustituir si seleccionar y activar son operaciones distintas. |
| descargar / bajar | «descargar» | Distinguir descarga, instalación y sincronización. |
| introducir / ingresar / escribir | «escribir» para texto; decidir otros casos por acción | Pegar, cargar e importar no equivalen a escribir. |
| correr / ejecutar | «ejecutar» para código, órdenes y programas | No usar «ejecutar» como verbo universal. |
| carpeta / directorio | Definir por dominio | En algunas explicaciones pueden ser equivalentes; en otras interesa la distinción técnica. |

Microsoft aporta antecedentes para «equipo» y para verbos independientes del método de entrada. Las elecciones de esta tabla son propuestas y requieren pruebas regionales. [download.microsoft](https://download.microsoft.com/download/4/3/1/431d9836-40dc-4f2b-aafc-def5c7b5d0f3/spa-neu-StyleGuide.pdf)

### 5.5. Morfología verbal: restringir por función, no por inventario arbitrario

Propuesta:

- Presente para comportamiento general: «La API devuelve un objeto».
- Imperativo para acciones: «Envía la solicitud».
- Pasado para cambios: «Se corrigió un error de autenticación».
- Futuro cuando el momento futuro sea parte de la información: «El certificado caducará mañana».
- Condicional para hipótesis reales, no para suavizar obligaciones.
- Subjuntivo cuando lo exija la construcción: «Espera a que termine el proceso».

Google recomienda presente para comportamiento general, pero esa preferencia no justifica eliminar distinciones temporales necesarias en español. [developers.google](https://developers.google.com/style/tense)

Una prohibición general del subjuntivo sería especialmente problemática: «No borres» y «No cierre» son instrucciones corrientes construidas con ese modo. [rae](https://www.rae.es/espanol-al-dia/infinitivo-por-imperativo)

También debe distinguirse modalidad:

| Intención | Formulación propuesta |
|---|---|
| Requisito | «Debes disponer del permiso de administración». |
| Recomendación | «Se recomienda crear una copia antes de actualizar». |
| Capacidad | «La herramienta puede exportar archivos CSV». |
| Posibilidad incierta | «La actualización puede tardar varios minutos». |
| Prohibición | «No compartas el token». |

El verificador debe detectar ambigüedad modal, no simplemente contar «deber» o «poder».

### 5.6. Sujeto tácito, clíticos y posesivos

El objetivo debe ser controlar el referente, no prohibir pronombres.

Ejemplos propuestos:

- Claro: «Abre el archivo y guárdalo en la carpeta temporal».
- Ambiguo: «Copia el certificado junto al archivo y elimínalo».
- Preferible: «Copia el certificado junto al archivo. Después, elimina el certificado».

En pasos separados, conviene repetir el objeto cuando el usuario puede leerlos de manera no secuencial.

Para el sujeto:

- «Valida el token» funciona como instrucción.
- «Valida el token y devuelve un error» puede mezclar una instrucción con una descripción del sistema.
- «El servidor valida el token y devuelve un error si el token no es válido» explicita el agente.

Para posesivos:

- Evitar «su clave» cuando pueda pertenecer al usuario, al servicio o a una organización.
- Preferir «la clave del servicio» si esa distinción importa.

Las guías de Microsoft ya advierten sobre posesivos innecesarios y referencias vagas; la cobertura de clíticos propuesta aquí requiere reglas propias de español. [download.microsoft](https://download.microsoft.com/download/4/3/1/431d9836-40dc-4f2b-aafc-def5c7b5d0f3/spa-neu-StyleGuide.pdf)

### 5.7. Activa, pasiva perifrástica y pasiva refleja

Propuesta:

1. Preferir activa cuando importe quién actúa.
2. Admitir pasiva refleja para estados o resultados con agente irrelevante.
3. Revisar pasiva perifrástica si añade longitud sin utilidad.
4. No sustituir «se» por «el sistema» si eso inventa o difumina el agente real.

Ejemplos:

| Texto | Evaluación |
|---|---|
| «El proceso de limpieza elimina los archivos temporales». | Adecuado cuando importa identificar el proceso. |
| «Se encontraron tres errores». | Adecuado como resultado. |
| «Los archivos son eliminados por el proceso de limpieza». | Gramatical, pero normalmente menos directo. |
| «Se debe reiniciar». | Insuficiente si no se sabe quién reinicia ni qué componente. |

La prioridad por activa con excepciones tiene apoyo en Google; la clasificación del «se» español necesita análisis lingüístico específico, no una traducción de un detector inglés de pasivas. [developers.google](https://developers.google.com/style/voice)

### 5.8. Género, concordancia e inclusión

Propuesta:

- Conservar concordancia gramatical.
- Evitar atribuir género a la persona cuando no sea necesario.
- Usar reformulaciones naturales: «Te damos la bienvenida», «Tu cuenta está lista», «Permiso de administración».
- No imponer perífrasis largas que empeoren la comprensión.
- No adoptar `@`, `x` o terminaciones alternativas como mecanismo automático del perfil básico.
- Tratar por separado las preferencias de identidad de personas reales y las referencias genéricas.

Microsoft propone alternativas sin sesgo de género y reformulación mediante segunda persona o sustantivos colectivos. Eso no elimina el género gramatical del español ni permite concatenar fragmentos sin concordancia. [download.microsoft](https://download.microsoft.com/download/4/3/1/431d9836-40dc-4f2b-aafc-def5c7b5d0f3/spa-neu-StyleGuide.pdf)

En ingeniería de interfaz, la consecuencia propuesta es evitar plantillas como:

> «El/La {objeto} está {estado}»

cuando los valores no garantizan concordancia. Es preferible una cadena completa por contexto o una estructura que no dependa de esa combinación.

### 5.9. Nominalizaciones y cadenas con «de»

Propuesta: detectar acumulación y ambigüedad, no prohibir todos los sustantivos de acción.

- Pesado: «Realiza la actualización de la configuración de la política de acceso del servicio».
- Más directo: «Actualiza la política de acceso del servicio».
- Si se modifica solo una propiedad: «Cambia el tiempo de espera de la política de acceso».

No deben eliminarse términos consolidados como «autenticación», «compilación» o «configuración» solo porque son nominalizaciones.

Una cadena puede ser extensa pero inequívoca; otra, breve y ambigua:

> «Registro de errores del cliente».

¿El cliente genera los errores, los registra o posee el archivo? La solución depende del concepto, no del número de preposiciones.

El antecedente de Gobbi ya identifica las cadenas preposicionales como problema de diseño del español controlado. [amsdottorato.unibo](https://amsdottorato.unibo.it/id/eprint/6681/1/Tesi_Gobbi_ETS.pdf)

### 5.10. Longitud y expansión del inglés al español

El 15–30% mencionado en el planteamiento no debe adoptarse como una constante universal. En este informe no se ha verificado una fuente primaria que establezca ese intervalo para todos los géneros de documentación de software.

Hay que medir por separado:

- Palabras.
- Caracteres.
- Anchura renderizada.
- Número de líneas.
- Complejidad sintáctica.
- Cantidad de acciones y condiciones.

Propuesta de piloto, no de norma definitiva:

| Perfil | Umbral inicial |
|---|---|
| Oración procedimental | Aviso de revisión por encima de 25 palabras. |
| Oración descriptiva | Aviso de revisión por encima de 30 palabras. |
| Interfaz | Sin máximo general de palabras; presupuesto por componente y prueba visual. |
| Aviso crítico | Prioridad a integridad del riesgo, condición y acción preventiva. |

Los valores 25/30 tienen un antecedente en el ETS de Gobbi, pero necesitan validación específica para este dominio. [amsdottorato.unibo](https://amsdottorato.unibo.it/id/eprint/6681/1/Tesi_Gobbi_ETS.pdf)

No debe permitirse «aprobar» una oración eliminando una condición, sustituyendo un término preciso por otro vago o suprimiendo artículos necesarios.

### 5.11. Polisemia: «una palabra, un significado» en software

Propuesta: controlar la unidad «lema + categoría + concepto + patrón de uso».

| Verbo | Uso a controlar | Alternativas según intención |
|---|---|---|
| poner | «Pon el servidor» | iniciar, instalar, conectar, configurar |
| dar | «Dale permisos» | conceder permisos, según el modelo del producto |
| hacer | «Haz un deploy» | desplegar una versión |
| ejecutar | Uso extensivo sin objeto preciso | ejecutar una orden, iniciar un servicio, aplicar una migración |
| correr | Calco coloquial de *run* | ejecutar |
| abrir | No necesita prohibición general | abrir archivo, iniciar conexión, expandir panel, si son conceptos distintos |

Las locuciones deben poder ser entradas completas: «hacer clic» no puede evaluarse solamente como un caso del verbo genérico «hacer».

El objetivo es reducir interpretaciones rivales en el contexto de uso, no demostrar que una palabra carece de polisemia en toda la lengua.

### 5.12. Anglicismos y elementos no traducibles

Propuesta de jerarquía:

1. Conservar identificadores ejecutables y literales.
2. Preferir un equivalente español preciso y establecido.
3. Mantener un término inglés cuando sea el identificador conceptual reconocido por la audiencia y la traducción introduzca confusión.
4. Definirlo y estabilizarlo en el glosario.
5. Evitar híbridos verbales improvisados como solución predeterminada.

| Forma | Propuesta | Matiz |
|---|---|---|
| loguearse | iniciar sesión | No confundir con autenticarse en todos los contextos. |
| deployar | desplegar | Definir diferencia entre compilar, publicar y desplegar. |
| backup | copia de seguridad | Fundéu recomienda esta alternativa; también reconoce otras según contexto. |
| commit | Mantener el término cuando designe el objeto de Git, con definición | No traducir el comando `git commit`. |
| endpoint | Elegir y definir por audiencia | «URL» no es siempre un equivalente conceptual completo. |
| token | Admitir como término técnico definido cuando corresponda | No traducir mecánicamente como «ficha». |

La recomendación de «copia de seguridad» está documentada por FundéuRAE; las demás elecciones son propuestas para validar. [fundeu](https://www.fundeu.es/recomendacion/backup-es-copia-de-seguridad-respaldo/)

### 5.13. Elementos de interfaz y código

Propuesta:

- Reproducir exactamente las etiquetas visibles.
- Usar marcado semántico de elemento de interfaz; permitir que cada formato de salida lo represente visualmente.
- En texto sin ese marcado, usar comillas: «Selecciona «Guardar cambios»».
- Para rutas de navegación, fijar un separador consistente: «Configuración > Seguridad».
- Usar formato de código para identificadores: `user_id`, `--force`, `POST`.
- No traducir nombres de campos, valores literales ni mensajes que deban coincidir con una búsqueda exacta.
- No trasladar las mayúsculas de título del inglés a etiquetas españolas nuevas.

Microsoft establece mayúscula inicial de oración para elementos de interfaz y exige preservar la terminología de elementos ya localizados. [download.microsoft](https://download.microsoft.com/download/4/3/1/431d9836-40dc-4f2b-aafc-def5c7b5d0f3/spa-neu-StyleGuide.pdf)

Una documentación puede, por tanto, contener una etiqueta regional ajena aunque el perfil editorial prefiera otra palabra. La coincidencia con la pantalla tiene prioridad sobre la uniformidad artificial.

### 5.14. Puntuación, números, fechas y unidades

Base de referencia:

- RAE/ASALE: *Nueva gramática*, 2009; *Ortografía*, 2010; DPD en línea, que se identifica como segunda edición provisional.
- ISO 80000-1:2022: magnitudes, unidades y símbolos. [download.microsoft](https://download.microsoft.com/download/9/a/1/9a19beca-597c-417b-a2c2-0f1ea5a1e6c3/spa-esp-StyleGuide.pdf)

Propuesta operativa:

| Aspecto | Convención |
|---|---|
| Puntuación | Mantener signos españoles de apertura; evitar estructuras recargadas. |
| Mayúsculas | Mayúscula inicial y nombres propios; respetar identificadores sensibles a mayúsculas. |
| Decimales en prosa | Elegir una política editorial explícita; no afirmar que punto o coma son universalmente incorrectos. |
| Agrupación en prosa técnica | Seguir la referencia académica con espacios cuando corresponda, no punto/coma como agrupadores. |
| Interfaz | Formatear números, fechas y monedas mediante el locale del usuario. |
| Código y protocolos | Conservar la sintaxis exigida por el lenguaje o formato. |
| Unidades | Espacio entre cifra y símbolo; símbolos sin punto ni plural. |
| Fechas para lectores | Preferir una forma inequívoca como «16 de octubre de 2026». |
| Datos y registros | Definir formato interoperable, zona horaria y precisión. |

La RAE admite tanto punto como coma decimal y reserva esos signos para la separación decimal, no para agrupar cifras en su recomendación de prosa. Los símbolos de unidades son invariables y se separan de la cifra. [rae](https://www.rae.es/dpd/n%C3%BAmeros)

ISO 80000-1 no resuelve por sí sola todas las convenciones informáticas de bits, bytes y prefijos binarios; ese apartado necesita una referencia específica adicional. [iso](https://www.iso.org/standard/76921.html)

### 5.15. Terminología y diccionario controlado

#### Recursos de referencia

| Recurso | Utilidad | Precaución |
|---|---|---|
| Microsoft Terminology | Terminología informática y exportación TBX. | Las decisiones responden al ecosistema Microsoft; revisar términos de reutilización. |
| IATE | Conceptos multilingües, incluidos campos de procesamiento de datos. | El contexto institucional europeo puede no coincidir con un producto. |
| Mozilla | Guías y glosarios de localización por variante. | La guía es-ES no constituye español internacional. |
| KDE | Glosario español y exportación TBX para Lokalize. | Revisar variedad, fecha y dominio. |
| GNOME | Corpus de interfaz y documentación traducida. | No asumir que un glosario histórico sigue mantenido. |
| CORPES XXI y CREA | Uso general y distribución de formas. | Frecuencia no equivale a precisión técnica ni neutralidad. |

Fuentes verificadas para Microsoft, IATE, Mozilla, KDE, GNOME y CORPES. [learn.microsoft](https://learn.microsoft.com/en-us/globalization/reference/microsoft-terminology)

La frecuencia debe examinarse por país, época y género textual; sumar ocurrencias de un término no revela automáticamente si es la mejor opción para una API.

#### Estructura propuesta del diccionario

Separar tres capas:

1. Vocabulario general controlado.
2. Terminología transversal de software y técnica.
3. Terminología y etiquetas del producto.

Cada entrada debería incluir:

- Identificador de concepto.
- Lema o expresión completa.
- Categoría gramatical y flexión.
- Definición operativa.
- Dominio y perfil.
- Construcción y complementos admitidos.
- Términos preferidos, admitidos, desaconsejados y literales.
- Ejemplos y contraejemplos originales.
- Equivalentes en otras lenguas.
- Fuente, licencia, fecha y responsable.
- Historial de cambios.

Ejemplo propio:

| Campo | Valor |
|---|---|
| Concepto | Invalidar una credencial antes de su vencimiento |
| Término preferido | revocar |
| Patrón | revocar + token/certificado/permiso |
| Ejemplo | «Revoca el token comprometido». |
| Restricción | No usar como sinónimo general de borrar un archivo. |
| Equivalente inglés | *revoke*, vinculado al concepto, no a todas sus acepciones |

### 5.16. Herramientas y verificación

| Herramienta | Función documentada | Adecuación al proyecto |
|---|---|---|
| Verificadores de STE | Detectan palabras y algunas infracciones del estándar inglés. | No constituyen un verificador español. ASD advierte que no son infalibles. |
| Vale | Marco configurable de reglas de estilo, YAML, expresiones regulares y ámbitos de documento. | Útil para léxico, patrones y formato; no aporta por sí solo una gramática completa del español. |
| LanguageTool | Ortografía, gramática y estilo con soporte de español. | Útil como capa de corrección; no certifica conformidad con un nuevo lenguaje controlado. |
| Acrolinx | Plataforma de control editorial y terminológico. | La matriz pública consultada no enumera español; no asumir soporte equivalente sin confirmación. |
| spaCy | Modelos españoles con análisis morfosintáctico y lematización. | Útil para reglas lingüísticas; necesita evaluación sobre textos técnicos. |
| Stanza | Tokenización, morfología, lemas y dependencias, con recursos españoles. | Especialmente pertinente para expansión de clíticos y análisis morfológico. |

Fuentes: ASD, Vale, LanguageTool, Acrolinx, spaCy y Stanza. [asd-ste100](https://www.asd-ste100.org/software.html)

Los modelos españoles de spaCy publicados se describen principalmente como entrenados para texto periodístico. No debe suponerse el mismo desempeño con comandos, fragmentos de interfaz y terminología de software. [spacy](https://spacy.io/models/es)

Propuesta de verificador híbrido:

1. Extraer estructura y proteger código, URLs, variables y literales.
2. Detectar el perfil textual.
3. Aplicar controles deterministas de terminología y formato.
4. Aplicar análisis morfosintáctico.
5. Emitir advertencias graduadas para ambigüedad y complejidad.
6. Solicitar revisión semántica en casos de riesgo.

Ejemplo de niveles:

- Error: etiqueta incorrecta, variable alterada, unidad mal escrita.
- Advertencia: referente dudoso, agente no identificado, oración extensa.
- Sugerencia: nominalización evitable o formulación más directa.

### 5.17. Legibilidad: indicadores, no certificados

Fernández Huerta y Szigriszt-Pazos estiman dificultad mediante propiedades como longitud de palabra y oración. INFLESZ ofrece una escala interpretativa del índice Flesch-Szigriszt, validada en un contexto de lectura en español, no específicamente para documentación de API. [scielo.isciii](https://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1137-66272008000300004)

Crawford se orienta a estimar escolaridad necesaria y tiene limitaciones de aplicación vinculadas a educación primaria. [periodicos.feevale](https://periodicos.feevale.br/seer/index.php/braziliancreativeindustries/article/download/2677/2906/7991)

Para este proyecto:

- No usar una puntuación como condición única de aprobación.
- No comparar botones y manuales con el mismo instrumento.
- No penalizar automáticamente términos largos pero precisos.
- Separar código de prosa.
- Medir comprensión y ejecución de tareas además de rasgos superficiales.

La literatura sobre informes médicos también documenta límites de los análisis cuantitativos formales de legibilidad. [revistas.ucm](https://revistas.ucm.es/index.php/CLAC/es/article/download/70574/4564456556008/4564456608552)

### 5.18. Traducción automática y modelos de lenguaje

#### Traducción en ambos sentidos

Hay que evaluar separadamente:

1. Español controlado → inglés general.
2. Español controlado → inglés controlado.
3. Inglés general → español controlado.
4. Inglés controlado → español controlado.

La conformidad de la fuente no garantiza la del destino. La traducción puede introducir sinonimia, cambiar modalidad, reconstruir referencias o producir estructuras no permitidas.

La investigación histórica de KANT respalda el valor de controlar la entrada en una arquitectura diseñada para ello. La investigación posterior muestra que el beneficio depende de reglas, sistemas, pares lingüísticos y dirección. [link.springer](https://link.springer.com/article/10.1007/s10590-021-09266-0)

#### ¿Alineación uno a uno con el inglés?

Propuesta: alinear conceptos, no palabras.

Ejemplo:

- *run*: ejecutar un programa, iniciar un servicio, funcionar.
- *save*: guardar un archivo, conservar un valor, ahorrar recursos.
- *issue*: incidencia, emisión, número editorial, según contexto.

Una alineación léxica rígida trasladaría polisemia y segmentación del inglés al español. La relación puede ser uno a varios o varios a uno, siempre con conceptos identificados.

#### Modelos de lenguaje

Un estudio exploratorio de 2025 aplicó prompts de lenguajes controlados a textos médicos en inglés, francés e italiano. Las autoras señalan que tuvieron que revisar y corregir el cumplimiento del número de palabras. La evaluación de comprensión con participantes se presentaba todavía como trabajo futuro. No constituye validación de redacción controlada en español ni de certificación automática. [air.uniud](https://air.uniud.it/retrieve/da459f9d-3c53-469c-934f-4fc642dc46e2/vezzani-vecchiato-frattolin-pubblicato-2025.aielpl-1.3.pdf)

Propuesta de uso:

- Generar alternativas.
- Señalar posibles infracciones.
- Explicar reglas con ejemplos.
- Revisar terminología contra un recurso autorizado.
- Ayudar a comparar el significado antes/después.

Riesgos a controlar:

- Cumplimiento aparente de reglas.
- Omisión de condiciones.
- Cambio de posibilidad por obligación.
- Alteración de identificadores.
- Corrección de una infracción que introduce otra.
- Evaluación circular cuando el mismo modelo redacta y se aprueba.

El flujo recomendado es:

> borrador → verificador determinista → análisis lingüístico → comparación semántica → revisión técnica.

La conformidad formal y la corrección técnica deben permanecer como evaluaciones distintas.

***

## 6. Decisiones de diseño abiertas, en orden de prioridad

| Prioridad | Decisión | Recomendación preliminar | Cómo resolverla |
|---|---|---|---|
| P0 | Relación con el ETS existente | Diferenciar nombre, alcance y materiales. | Revisar la tesis y contactar a la autora si se quiere reutilizar contenido. |
| P0 | Objetivo principal | Priorizar ejecución correcta y comprensión humana. | Definir tareas, lectores y riesgos antes de redactar reglas. |
| P0 | Alcance de conformidad | Un núcleo y perfiles separados. | Clasificar un corpus real de software. |
| P0 | Régimen legal | Especificación y ejemplos originales. | Revisión de derechos, marcas y fuentes léxicas. |
| P0 | Preservación del significado | Hacerla superior a la brevedad. | Crear pruebas de condiciones, modalidades y efectos. |
| P1 | Tú o usted | Tuteo como piloto; perfiles completos si se necesita usted. | Ensayos de comprensión, naturalidad y aceptación por país. |
| P1 | Neutralidad o variantes | Base internacional con excepciones justificadas. | Evaluación regional y prueba de términos conflictivos. |
| P1 | Restricciones verbales | Reglas por función, sin prohibición general del subjuntivo. | Analizar procedimientos, API y notas de versión. |
| P1 | Polisemia | Control por concepto y patrón de uso. | Banco de ejemplos ambiguos y casos legítimos. |
| P1 | Longitud | Avisos iniciales, no rechazo automático. | Comparar umbrales con desempeño real. |
| P1 | Anglicismos | Política por concepto y audiencia. | Medir reconocimiento y precisión. |
| P1 | Modelo de diccionario | Base conceptual con vocabulario y términos separados. | Prototipo exportable e historial de decisiones. |
| P2 | Automatización | Construcción híbrida incremental. | Medir precisión, cobertura y falsos positivos por regla. |
| P2 | Traducción | Evaluación independiente por dirección y motor. | Prueba ciega con poseditores. |
| P2 | LLM | Asistente, no autoridad certificadora. | Evaluación externa y controles deterministas. |
| P2 | Gobernanza | Reglas versionadas y cambios justificados. | Comité editorial y técnico con registro público. |

### Programa mínimo de validación

Propuesta de investigación:

1. Construir un corpus con manuales, ayuda, API, interfaz, errores, operaciones y notas de versión.
2. Incluir textos redactados originalmente en español, no solo traducciones del inglés.
3. Mantener pares original/controlado con equivalencia técnica revisada.
4. Evaluar con lectores de España y varios países latinoamericanos.
5. Estratificar por experiencia técnica.
6. Comparar reglas de forma individual además del paquete completo.
7. Medir:
   - éxito y errores de tarea;
   - tiempo;
   - comprensión de condiciones;
   - identificación del agente;
   - naturalidad;
   - calidad de traducción;
   - tiempo y esfuerzo de posedición;
   - tiempo de autoría y falsos positivos.

La evaluación por regla es importante porque los efectos globales favorables pueden ocultar reglas individuales perjudiciales, como muestra el estudio de Marzouk. [link.springer](https://link.springer.com/article/10.1007/s10590-021-09266-0)

***

## 7. Riesgos legales y de licencia

### 7.1. ASD-STE100 no es una obra abierta por ser gratuita

Issue 9 declara propiedad de ASD y reserva la reproducción o publicación total o parcial salvo autorización escrita. Contiene, además, permisos especiales para determinadas organizaciones e instituciones, incluidas universidades e institutos de investigación con fines educativos. [asd-ste100](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)

Por tanto:

- Obtener una copia gratuita no equivale a obtener una licencia abierta.
- Tener acceso al PDF no autoriza automáticamente a publicar un diccionario derivado.
- Una excepción para investigación o docencia no debe extrapolarse a un producto comercial.
- La atribución no sustituye una autorización que sea necesaria.

### 7.2. Qué puede hacerse con menor riesgo

Propuesta de enfoque independiente:

- Describir y analizar principios con redacción propia.
- Citar edición, páginas o categorías cuando corresponda.
- Crear reglas originales a partir de problemas del español.
- Elaborar ejemplos originales de software.
- Construir el diccionario desde corpus y fuentes con derechos revisados.
- Documentar la procedencia de cada decisión.

La distinción jurídica entre ideas, expresión, citas y adaptación depende de la jurisdicción y del uso concreto. Este informe no concluye que toda paráfrasis o adaptación sea automáticamente lícita.

### 7.3. Qué requiere especial revisión

- Traducir sistemáticamente el articulado.
- Reproducir ejemplos del estándar.
- Volcar sus entradas en JSON, YAML, una base de datos o un paquete de reglas.
- Publicar una transformación casi equivalente de sus reglas y diccionario.
- Usar sus materiales para entrenamiento, recuperación o distribución en herramientas sin revisar las condiciones.
- Presentar el proyecto como versión oficial o certificada de ASD.

El documento identifica ASD-STE100 como marca registrada de la Unión Europea, número 017966390. La denominación y la apariencia de afiliación merecen revisión independiente del copyright. [asd-ste100](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)

### 7.4. Derechos de otros recursos

También deben revisarse por separado:

- El ETS de Gobbi y sus ejemplos.
- Microsoft Terminology y sus condiciones de descarga y reutilización.
- Guías corporativas.
- Glosarios comunitarios.
- Corpus y permisos de redistribución.
- Normas UNE e ISO.

Propuesta de registro legal por recurso:

> titular → licencia → usos permitidos → redistribución → derivados → atribución → fecha de revisión.

La opción más sólida es una especificación propia con licencia explícita para texto, diccionario, corpus de pruebas y software, sin incorporar material protegido de forma incompatible.

***

## 8. Bibliografía comentada y enlaces

Los marcadores de fuente de cada entrada funcionan como enlaces. En las guías web sin edición o fecha editorial verificable se indica «s. f.; consulta: 16-10-2026», en lugar de atribuirles una edición inexistente.

### 8.1. ASD-STE100 y su aplicación

1. ASD. *ASD-STE100 Simplified Technical English. Standard for technical documentation*. Issue 9, 15-01-2025. Fuente primaria para estructura, cambios, copyright y derechos especiales. [asd-ste100](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)

2. ASD/STEMG. *About ASD-STE100* y *FAQ*. S. f.; consulta: 16-10-2026. Historia, organismo responsable y explicación de vocabulario y términos técnicos. [asd-ste100](https://www.asd-ste100.org/about_STE.html)

3. ASD. *A milestone in Simplified Technical English: ASD-STE100 Issue 9*. 29-01-2025. Resumen oficial de la revisión de reglas y diccionario. [asd-europe](https://www.asd-europe.org/news-media/news-events/news/simplified-technical-english-asd-ste100-issue-9/)

4. ASD/STEMG. *STE Software Products*. S. f.; consulta: 16-10-2026. Funciones y límites de los verificadores. [asd-ste100](https://www.asd-ste100.org/software.html)

### 8.2. Antecedentes españoles y lenguajes controlados

5. Gobbi, Ilaria. *Español Técnico Simplificado*. Tesis doctoral, Universidad de Bolonia, 2014. Antecedente directo; contiene metodología, reglas y diccionario. [amsdottorato.unibo](https://amsdottorato.unibo.it/id/eprint/6681/1/Tesi_Gobbi_ETS.pdf)

6. Gobbi, Ilaria. *Simplified Technical Spanish*. Resumen de tesis, *New Voices in Translation Studies*, 13(1), 2015; ficha web publicada en 2023. [newvoices.arts.chula.ac](https://newvoices.arts.chula.ac.th/index.php/en/article/download/296/295/447)

7. Gobbi, Ilaria. *Español Técnico Simplificado: un lenguaje controlado para la traducción*. *Revista CTPCBA*, n.º 141, abril–junio, pp. 24–27; el año no queda identificado en el extracto recuperado. [biblio.traductores.org](http://biblio.traductores.org.ar/documentos/07777.pdf)

8. Ruiz-Cascales, R. *A Specification and Validating Parser for Simplified Technical Spanish*. Tesis de maestría, University of Limerick, 2002. Referencia verificada en publicación de los participantes de TREC; no se consultó el original completo. [trec.nist](https://trec.nist.gov/pubs/trec11/papers/ulimerick.sutcliffe.pdf)

9. Carnegie Mellon University. *KANT: Knowledge-Based Machine Translation*. S. f.; consulta: 16-10-2026. Descripción de la arquitectura. [lti.cs.cmu](https://www.lti.cs.cmu.edu/research/research-articles/kant.html)

10. *The KANT Machine Translation System: From R&D to Initial Deployment*. 1997. Caso histórico de productividad en documentación industrial. [cs.cmu](https://www.cs.cmu.edu/~jgc/publication/The_KANT_Machine_Translation_Sys_From_R&D_LISA_1997.pdf)

11. Mitamura. *Controlled Language for Multilingual Machine Translation*. 1999. Documenta producción en francés y español. [aclanthology](https://aclanthology.org/www.mt-archive.info/90/MTS-1999-Mitamura.pdf)

### 8.3. Evidencia de comprensión, traducción y LLM

12. Jahchan, N.; Condamines, A.; Cannesson, E. *To What Extent Does Text Simplification Entail a More Optimized Comprehension in Human-Oriented CNLs?* 2016, pp. 69–80. Revisión crítica de resultados de comprensión. [shs.hal](https://shs.hal.science/halshs-01379559/document)

13. Aikawa, T.; Schwartz, L.; King, R.; Corston-Oliver, M.; Lozano, C. *Impact of controlled language on translation quality and post-editing in a statistical machine translation environment*. 2007. [microsoft](https://www.microsoft.com/en-us/research/publication/impact-of-controlled-language-on-translation-quality-and-post-editing-in-a-statistical-machine-translation-environment/)

14. Marzouk, Shaimaa. *An in-depth analysis of the individual impact of controlled language rules on machine translation output: a mixed-methods approach*. 2021. Evaluación por regla y sistema; datos traducidos en 2016. [link.springer](https://link.springer.com/article/10.1007/s10590-021-09266-0)

15. Vezzani, F.; Vecchiato, S.; Frattolin, E. *Large Language Models Applied to Controlled Natural Languages in Communicating Diabetes Therapies*. 23-06-2025, pp. 25–29. Estudio exploratorio; no aporta todavía la validación de comprensión anunciada. [air.uniud](https://air.uniud.it/retrieve/da459f9d-3c53-469c-934f-4fc642dc46e2/vezzani-vecchiato-frattolin-pubblicato-2025.aielpl-1.3.pdf)

### 8.4. Guías de software y localización

16. Microsoft. *Writing Style Guide: Word choice* y *Use simple words, concise sentences*. Páginas con fechas publicadas de 2024 y 2022, respectivamente. [learn.microsoft](https://learn.microsoft.com/en-us/style-guide/word-choice/)

17. Microsoft. *Spanish (Neutral) Style Guide*. PDF, s. f.; consulta: 16-10-2026. Útil para neutralidad y decisiones históricas de tratamiento; contiene referencias de producto antiguas. [download.microsoft](https://download.microsoft.com/download/4/3/1/431d9836-40dc-4f2b-aafc-def5c7b5d0f3/spa-neu-StyleGuide.pdf)

18. Microsoft. *Spanish (Spain) Localization Style Guide*. PDF, s. f.; consulta: 16-10-2026. Incluye interfaz, inclusión y consideraciones recientes de producto. [download.microsoft](https://download.microsoft.com/download/9/a/1/9a19beca-597c-417b-a2c2-0f1ea5a1e6c3/spa-esp-StyleGuide.pdf)

19. Google. *Developer Documentation Style Guide*: traducción, voz y tiempos verbales. Guía web continua, sin número de edición; consulta: 16-10-2026. [developers.google](https://developers.google.com/style/voice)

20. Apple. *Apple Style Guide*. Guía web continua, sin edición editorial identificada en la página consultada; consulta: 16-10-2026. [support.apple](https://support.apple.com/guide/applestyleguide/welcome/web)

21. IBM. *IBM Style*. Guía web; consulta: 16-10-2026. [ibm](https://www.ibm.com/docs/en/technical-content?topic=standards-style)

22. Red Hat. *Supplementary Style Guide for Product Documentation*. Guía web continua; consulta: 16-10-2026. [redhat-documentation.github](https://redhat-documentation.github.io/supplementary-style-guide/)

### 8.5. Español, claridad y normas

23. ISO. *ISO 24495-1:2023. Plain language — Part 1: Governing principles and guidelines*. 2023. [iso](https://www.iso.org/standard/78907.html)

24. UNE. *UNE-ISO 24495-1:2024. Lenguaje claro. Parte 1: Principios rectores y directrices*. Adopción española documentada por UNE. [revista.une](https://revista.une.org/76/la-normalizacion-del-lenguaje-claro.html)

25. UNE. *UNE 153101:2018 EX. Lectura Fácil. Pautas y recomendaciones para la elaboración de documentos*. 2018. [une](https://www.une.org/encuentra-tu-norma/busca-tu-norma/norma?c=N0060036)

26. ISO. *ISO 80000-1:2022. Quantities and units — Part 1: General*. Diciembre de 2022. [iso](https://www.iso.org/standard/76921.html)

27. RAE/ASALE. *Diccionario panhispánico de dudas*, versión en línea, segunda edición provisional; consulta: 16-10-2026. Entradas y materiales sobre números e instrucciones. [rae](https://www.rae.es/espanol-al-dia/infinitivo-por-imperativo)

28. RAE. *CORPES XXI*. Recurso en actualización; consulta: 16-10-2026. [rae](https://www.rae.es/banco-de-datos/corpes-xxi)

29. FundéuRAE. *«backup» es «copia de seguridad»*. 22-05-2017. [fundeu](https://www.fundeu.es/recomendacion/backup-es-copia-de-seguridad-respaldo/)

30. Argentina.gob.ar. *Contenidos digitales* y materiales sobre la Red Argentina de Lenguaje Claro. Recursos públicos; consulta: 16-10-2026. [argentina.gob](https://www.argentina.gob.ar/noticias/la-red-argentina-de-lenguaje-claro-llego-wikipedia)

### 8.6. Terminología y herramientas

31. Microsoft. *Microsoft Terminology*. Página fechada en 2024; consulta: 16-10-2026. Recursos y descarga TBX. [learn.microsoft](https://learn.microsoft.com/en-us/globalization/reference/microsoft-terminology)

32. Unión Europea. *IATE*. Base terminológica en actualización; consulta: 16-10-2026. [iate.europa](https://iate.europa.eu/)

33. Mozilla. *Spanish, Spain (es-ES) Style Guide*. S. f.; consulta: 16-10-2026. [mozilla-l10n.github](https://mozilla-l10n.github.io/styleguides/es-ES/index.html)

34. KDE. *Glosario de KDE*. Recurso en actualización; consulta: 16-10-2026. [es.l10n.kde](https://es.l10n.kde.org/glosario_new.php)

35. Vale. *Documentation: Introduction*. Documentación continua; consulta: 16-10-2026. [docs.vale](https://docs.vale.sh/)

36. LanguageTool. *Supported languages*. Documentación continua; consulta: 16-10-2026. [dev.languagetool](https://dev.languagetool.org/languages)

37. Acrolinx. *Language Support*. Matriz pública; consulta: 16-10-2026. [acrolinx](https://www.acrolinx.com/language-support/)

38. spaCy. *Spanish Models*; Stanza. *Overview* y *Combined models*. Documentación continua; consulta: 16-10-2026. [spacy](https://spacy.io/models/es)

39. Barrio-Cantalejo y colaboradores. *Validación de la Escala INFLESZ para evaluar la legibilidad de los textos dirigidos a pacientes*. 2008. [scielo.isciii](https://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1137-66272008000300004)

### Alcance de la investigación

La base documental permite comenzar el diseño, pero quedan tres vacíos materiales: una validación panhispánica de las convenciones propuestas, un ensayo específico de traducción y posedición para software, y una revisión jurídica de los materiales que se pretenda incorporar. Ninguno de esos vacíos se resuelve trasladando automáticamente las reglas inglesas, el ETS aeronáutico previo o las preferencias de una única empresa.
