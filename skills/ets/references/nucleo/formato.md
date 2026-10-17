# Formato

Reglas del núcleo sobre mayúsculas, puntuación, etiquetas de interfaz, código, números, unidades y fechas. Se aplican a todos los perfiles.

## Mayúsculas y puntuación

### FOR-01 — Mayúscula de oración, no de título
Regla: En títulos, encabezados y etiquetas, escribe con mayúscula solo la primera palabra y los nombres propios.
Por qué: Las mayúsculas en cada palabra son una convención del inglés y dificultan distinguir los nombres propios.
Incorrecto: Configuración De La Cuenta
Correcto: Configuración de la cuenta
Excepciones: Nombres propios de productos y siglas: Instalar la CLI de GitHub.
Verificable: sí (FOR-01). El verificador lo comprueba en encabezados de Markdown.

### FOR-02 — Signos de apertura
Regla: Escribe los signos de apertura de interrogación y exclamación.
Por qué: Son obligatorios en español y marcan dónde empieza la pregunta.
Incorrecto: Quieres eliminar el proyecto?
Correcto: ¿Quieres eliminar el proyecto?
Excepciones: Código, expresiones regulares y valores literales.
Verificable: sí (FOR-02)

## Interfaz y código

### FOR-03 — Etiquetas literales entre comillas angulares
Regla: Escribe las etiquetas de la interfaz entre comillas angulares y con el texto exacto de la pantalla.
Por qué: Las comillas separan la etiqueta de la prosa, y el texto exacto permite encontrarla.
Incorrecto: Selecciona el botón de guardar cambios.
Correcto: Selecciona «Guardar cambios».
Excepciones: Si el formato de salida tiene marcado semántico para elementos de interfaz, úsalo en lugar de las comillas.
Verificable: no. El verificador protege el texto entre «» y no lo analiza.

### FOR-04 — Rutas de menú con el signo mayor que
Regla: Escribe las rutas de navegación con « > » entre cada nivel, dentro de un único par de comillas angulares.
Por qué: Un separador fijo se reconoce enseguida en todo el documento.
Incorrecto: Ve a «Configuración» → «Seguridad».
Correcto: Abre «Configuración > Seguridad».
Excepciones: Ninguna.
Verificable: parcialmente (FOR-04). El verificador marca flechas y barras entre etiquetas.

### FOR-05 — Identificadores entre comillas invertidas
Regla: Escribe entre comillas invertidas los nombres de variables, campos, funciones, comandos, opciones y valores literales.
Por qué: Así el lector sabe que debe copiar el texto exacto y el verificador no lo analiza como prosa.
Incorrecto: Cambia el valor de max_retries a 5.
Correcto: Cambia el valor de `max_retries` a 5.
Excepciones: Nombres de productos, que se escriben como nombres propios.
Verificable: parcialmente (FOR-05). El verificador sugiere comillas invertidas para identificadores con guion bajo o con mayúsculas internas.

### FOR-06 — Literales intactos
Regla: No traduzcas ni cambies código, comandos, nombres de campo, valores, rutas, URL, variables ni etiquetas de interfaz al reescribir.
Por qué: Un literal cambiado deja de funcionar o no coincide con la pantalla.
Incorrecto: Ejecuta `npm instalar`.
Correcto: Ejecuta `npm install`.
Excepciones: Ninguna.
Verificable: sí (FOR-06). El verificador lo comprueba si recibe el texto original con la opción `--original`.

## Números, unidades y fechas

### FOR-07 — Espacio entre la cifra y el símbolo de unidad
Regla: Separa con un espacio la cifra del símbolo de unidad.
Por qué: Es la convención internacional de unidades y evita lecturas como «5m» por cinco minutos o cinco metros.
Incorrecto: El archivo ocupa 512MB y tarda 30s en subir.
Correcto: El archivo ocupa 512 MB y tarda 30 s en subir.
Excepciones: Código, nombres de producto y valores literales, como `--memory=512m`.
Verificable: sí (FOR-07)

### FOR-08 — Símbolos sin punto ni plural
Regla: Escribe los símbolos de unidad sin punto final ni marca de plural.
Por qué: Los símbolos son invariables.
Incorrecto: Libera 20 GBs de espacio y espera 5 min. antes de reintentar.
Correcto: Libera 20 GB de espacio y espera 5 min antes de reintentar.
Excepciones: El punto que cierra la oración.
Verificable: sí (FOR-08)

### FOR-09 — Separador decimal coherente
Regla: En prosa técnica del perfil internacional, usa el punto decimal y mantenlo en todo el documento.
Por qué: El punto coincide con el código y con los archivos de configuración; mezclar separadores en un documento produce errores de lectura.
Incorrecto: Usa la versión 1,5 del protocolo y un umbral de 0.75.
Correcto: Usa un umbral de 0.75 y un factor de 1.5.
Excepciones: Un perfil regional puede elegir la coma. En la interfaz, el formato depende de la configuración regional de la persona (FOR-12).
Verificable: no

### FOR-10 — Sin punto ni coma para agrupar miles
Regla: No agrupes cifras con punto o coma. Usa un espacio en números de cinco cifras o más, o no agrupes.
Por qué: «1.000» es mil en unos países y uno con tres decimales en otros.
Incorrecto: El plan gratuito admite 10.000 solicitudes al día.
Correcto: El plan gratuito admite 10 000 solicitudes al día.
Excepciones: Valores literales de código y números de versión.
Verificable: sí (FOR-10)

### FOR-11 — Fechas inequívocas
Regla: En textos para personas, escribe las fechas con el nombre del mes. En datos y registros, usa el formato ISO 8601.
Por qué: «03/04/2026» es 3 de abril en unos países y 4 de marzo en otros.
Incorrecto: El servicio deja de funcionar el 03/04/2026.
Correcto: El servicio deja de funcionar el 3 de abril de 2026.
Excepciones: En registros y API, usa `2026-04-03` y especifica la zona horaria.
Verificable: parcialmente (FOR-11). El verificador marca fechas con barras.

### FOR-12 — Formatos de interfaz según la configuración regional
Regla: En la interfaz, formatea números, fechas, horas y monedas con la configuración regional de la persona. No los escribas fijos en las cadenas.
Por qué: Una cadena fija impone el formato de un solo país.
Incorrecto: Último acceso: 10/16/2026 3:00 PM
Correcto: Último acceso: {fecha_hora}
Excepciones: Datos técnicos que el usuario copia, como marcas de tiempo de registros.
Verificable: no
