<!-- ets: perfil=interfaz -->
# Perfil: interfaz y mensajes

Para etiquetas de botones y menús, títulos de pantalla, textos de ayuda breves, mensajes de error, confirmaciones, notificaciones y cadenas de localización.

## Cambios sobre el núcleo

| Regla del núcleo | Cambio en este perfil |
|---|---|
| ORA-03 y ORA-04 | No se aplican. No hay longitud máxima general (INT-07). |
| ORA-05 | Las etiquetas y los títulos pueden ser frases nominales sin artículo. |
| FOR-01 | Se aplica a cada etiqueta (INT-02). |
| ORA-12 | Obligatoria: es la causa más frecuente de errores de concordancia en interfaces. |
| TER-05 | No aplica a cadenas nuevas: las cadenas nuevas siguen el glosario. |

## Reglas

### INT-01 — Botones, menús y títulos en infinitivo
Regla: Escribe las etiquetas de botones, elementos de menú y títulos de pantalla en infinitivo o como sustantivo.
Por qué: El infinitivo nombra la acción sin dirigirse a nadie y se distingue de las instrucciones.
Incorrecto: Guarda los cambios
Correcto: Guardar cambios
Excepciones: Botones de respuesta a una pregunta pueden usar «Sí» y «No», o repetir el verbo de la pregunta: «Eliminar» y «Cancelar».
Verificable: no

### INT-02 — Mayúscula solo inicial en etiquetas
Regla: En etiquetas, escribe con mayúscula solo la primera palabra y los nombres propios.
Por qué: Es la convención del español (FOR-01) y facilita reconocer los nombres de producto.
Incorrecto: Crear Nueva Cuenta
Correcto: Crear cuenta nueva
Excepciones: Nombres propios y siglas: Conectar con GitHub.
Verificable: sí (INT-02)

### INT-03 — Punto final solo en oraciones completas
Regla: No pongas punto final en etiquetas, títulos ni elementos de lista breves. Ponlo en mensajes que son oraciones completas.
Por qué: El punto indica que el texto es una oración; en una etiqueta, sobra.
Incorrecto: Guardar cambios.
Correcto: No se pudo guardar el archivo. Comprueba la conexión y vuelve a intentarlo.
Excepciones: Ninguna.
Verificable: no

### INT-04 — Mensajes de error: qué pasó y qué hacer
Regla: Escribe en cada mensaje de error qué ocurrió y qué puede hacer la persona. No culpes a la persona.
Por qué: Un mensaje sin salida obliga a buscar ayuda en otro lugar.
Incorrecto: Error: entrada no válida.
Correcto: La fecha de fin es anterior a la fecha de inicio. Elige una fecha de fin posterior.
Excepciones: Si la persona no puede hacer nada, dilo y explica qué pasa después: El servicio no está disponible. Vuelve a intentarlo en unos minutos.
Verificable: no

### INT-05 — Sin términos alarmistas ni técnicos innecesarios
Regla: No uses «fatal», «ilegal», «abortar» ni «catastrófico» en mensajes para personas. Escribe «no válido» en lugar de «inválido».
Por qué: Estos términos asustan o suenan a acusación y no ayudan a resolver el problema.
Incorrecto: Error fatal: operación ilegal.
Correcto: No se pudo completar la operación. Vuelve a intentarlo.
Excepciones: Mensajes de registro para desarrolladores que reproducen la salida literal de una herramienta.
Verificable: sí (INT-05)

### INT-06 — Plurales y concordancia con cadenas completas
Regla: No escribas plurales con paréntesis ni concatenes fragmentos que dependen del número o del género. Usa una cadena completa para cada forma.
Por qué: «1 archivo(s)» es incómodo de leer y muchas lenguas tienen más de dos formas de plural.
Incorrecto: Se eliminaron {n} archivo(s).
Correcto: Se eliminó 1 archivo. / Se eliminaron {n} archivos.
Excepciones: Ninguna. Usa el sistema de plurales de ICU MessageFormat u otro equivalente.
Verificable: sí (INT-06)

### INT-07 — Sin longitud máxima general
Regla: No apliques un límite de palabras a las cadenas de interfaz. Define un espacio máximo por componente y prueba la cadena en pantalla.
Por qué: El espacio disponible depende del componente, no del número de palabras.
Incorrecto: Recortar «Guardar como borrador» a «Guardar borr.» para que entre en el botón.
Correcto: Usar «Guardar borrador» y comprobar que el botón muestra el texto completo en todos los tamaños de pantalla.
Excepciones: Ninguna.
Verificable: no

### INT-08 — Estados y resultados con construcciones naturales
Regla: Escribe los estados y resultados con presente, pasado o pasiva refleja, de forma breve.
Por qué: La persona solo necesita saber qué cambió.
Incorrecto: El proceso de guardado de los cambios se ha completado de forma satisfactoria.
Correcto: Los cambios se guardaron.
Excepciones: Ninguna.
Verificable: no

### INT-09 — Texto accesible igual al visible
Regla: Haz que la etiqueta accesible de un control empiece con el texto visible.
Por qué: Quien usa control por voz dice lo que ve en pantalla.
Incorrecto: Botón visible «Enviar» con etiqueta accesible «Confirmar formulario».
Correcto: Botón visible «Enviar» con etiqueta accesible «Enviar formulario».
Excepciones: Iconos sin texto: la etiqueta accesible describe la acción, como «Cerrar».
Verificable: no

## Ejemplos de cadenas

| Contexto | Cadena |
|---|---|
| Botón principal | Crear proyecto |
| Título de cuadro de diálogo | ¿Eliminar el proyecto? |
| Texto del cuadro de diálogo | Se eliminarán el proyecto y sus 3 entornos. Esta acción no se puede deshacer. |
| Confirmación | El proyecto se eliminó. |
| Error de red | No se pudo conectar con el servidor. Comprueba la conexión y vuelve a intentarlo. |
| Campo vacío | Escribe un nombre para el proyecto. |
