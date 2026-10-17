<!-- ets: perfil=conceptos-api -->
# Perfil: conceptos y API

Para explicaciones de arquitectura, guías conceptuales, referencia de API, documentación de bibliotecas, comentarios de código y README técnicos.

## Cambios sobre el núcleo

| Regla del núcleo | Cambio en este perfil |
|---|---|
| ORA-03 | No se aplica; ORA-04 la reemplaza. |
| ORA-04 | Umbral de aviso de 30 palabras por oración. |
| ORA-02 | La condición al final es aceptable cuando describe el comportamiento del sistema y no hay acción del lector. |
| ORA-05 | Las celdas de tabla de parámetros pueden ser frases nominales breves. |
| VER-06 | El verificador sugiere revisar cada verbo en futuro. |
| TER-07 | En la referencia de una función o un endpoint, el sujeto tácito es aceptable si todo el bloque describe ese elemento. |

## Estructura recomendada para un endpoint o una función

```
### <MÉTODO> <ruta>   o   ### <nombre_de_función>()

<Una oración en presente: qué hace.>

Parámetros

| Nombre | Tipo | Obligatorio | Descripción |
|---|---|---|---|

Respuesta

<Qué devuelve, con un ejemplo en un bloque de código.>

Errores

| Código | Causa | Qué hacer |
|---|---|---|
```

## Reglas

### API-01 — Presente y agente explícito
Regla: Describe el comportamiento en presente y nombra el componente que actúa: el cliente, el servidor, la biblioteca o la tarea.
Por qué: En una arquitectura con varios componentes, un sujeto tácito o un «se» obligan a adivinar quién hace cada cosa.
Incorrecto: Se valida la firma y se reintenta si falla.
Correcto: El servidor valida la firma. Si la validación falla, el cliente reintenta la solicitud.
Excepciones: La pasiva refleja es aceptable cuando el agente no importa (VER-11).
Verificable: no

### API-02 — Requisito, capacidad y posibilidad
Regla: Distingue lo que el cliente debe hacer, lo que el sistema puede hacer y lo que puede ocurrir.
Por qué: Confundir «debe» y «puede» cambia el contrato de la API.
Incorrecto: El cliente puede enviar el encabezado `Idempotency-Key` en las solicitudes `POST` (el encabezado es obligatorio).
Correcto: El cliente debe enviar el encabezado `Idempotency-Key` en cada solicitud `POST`.
Excepciones: Ninguna.
Verificable: no

### API-03 — Literales de API sin traducir
Regla: Conserva tal cual los nombres de campos, parámetros, encabezados, valores enumerados y códigos de error. Escríbelos entre comillas invertidas.
Por qué: El código del lector compara cadenas exactas.
Incorrecto: El campo estado puede valer activo o suspendido.
Correcto: El campo `status` puede valer `active` o `suspended`.
Excepciones: Puedes explicar el significado en español junto al literal: `suspended` (cuenta suspendida por falta de pago).
Verificable: parcialmente (FOR-06)

### API-04 — Estructura fija de referencia
Regla: Usa la misma estructura en todas las entradas de referencia: descripción, parámetros, respuesta y errores.
Por qué: El lector aprende dónde buscar cada dato.
Incorrecto: Un endpoint con los errores en la descripción y otro con los errores en una tabla.
Correcto: Todos los endpoints con una tabla «Errores» después de «Respuesta».
Excepciones: Secciones vacías: escribe «Ninguno» en lugar de omitir la sección.
Verificable: no

### API-05 — Valores predeterminados, límites y unidades
Regla: Para cada parámetro, indica el tipo, si es obligatorio, el valor predeterminado, los límites y la unidad.
Por qué: Un número sin unidad o sin límites obliga a probar para descubrir el contrato.
Incorrecto: `timeout`: el tiempo de espera.
Correcto: `timeout`: tiempo de espera en segundos. Entero entre 1 y 300. Valor predeterminado: 30.
Excepciones: Ninguna.
Verificable: no

### API-06 — Errores con código, causa y solución
Regla: Documenta cada error con el código literal, la causa y lo que el cliente debe hacer.
Por qué: Quien lee un error necesita saber cómo resolverlo.
Incorrecto: `429`: error de límite.
Correcto: `429`: el cliente superó el límite de 100 solicitudes por minuto. Espera el número de segundos que indica el encabezado `Retry-After` y repite la solicitud.
Excepciones: Ninguna.
Verificable: no

### API-07 — Define cada término inglés una vez
Regla: La primera vez que uses un término inglés sin traducción, defínelo en una frase. Después, úsalo sin definición.
Por qué: Un término definido una vez se reconoce después sin interrumpir la lectura.
Incorrecto: Configura el webhook para recibir eventos.
Correcto: Configura un webhook, es decir, una URL de tu servidor que recibe una solicitud `POST` por cada evento.
Excepciones: Términos del glosario del proyecto, que ya tienen definición.
Verificable: no

## Ejemplo completo

### `GET /orders/{id}`

Devuelve un pedido por su identificador.

| Nombre | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `id` | cadena | Sí | Identificador del pedido. |
| `expand` | cadena | No | Objetos relacionados que se incluyen en la respuesta. Valores admitidos: `items`, `customer`. |

El servidor devuelve el pedido en formato JSON. Si el pedido no existe, el servidor devuelve un error `404`.

| Código | Causa | Qué hacer |
|---|---|---|
| `401` | El token de acceso no es válido o caducó. | Solicita un token nuevo y repite la solicitud. |
| `404` | No existe un pedido con ese identificador. | Comprueba el valor de `id`. |
