# Oraciones

Reglas del núcleo sobre estructura, longitud, condiciones, nominalizaciones, cadenas de «de» y concordancia. Se aplican a todos los perfiles, salvo que el perfil indique otra cosa.

## Estructura

### ORA-01 — Una instrucción por oración
Regla: Escribe una sola acción del lector en cada oración. Dos acciones muy unidas sobre el mismo objeto pueden ir juntas con «y».
Por qué: Cada acción separada es fácil de seguir y de comprobar.
Incorrecto: Abre la consola, crea un proyecto, activa la facturación y copia el identificador.
Correcto: Abre la consola y crea un proyecto. Activa la facturación. Copia el identificador del proyecto.
Excepciones: Una condición o una finalidad no cuentan como acción adicional: Si usas un proxy, configura la variable `HTTPS_PROXY`.
Verificable: no

### ORA-02 — Condición antes de la acción
Regla: Escribe la condición al principio de la oración y la acción después.
Por qué: Quien lee la acción primero puede ejecutarla antes de llegar a la condición.
Incorrecto: Elimina la base de datos de pruebas si ya no la necesitas.
Correcto: Si ya no necesitas la base de datos de pruebas, elimina la base de datos.
Excepciones: En descripciones del sistema, la condición al final es aceptable cuando no hay una acción del lector: La API devuelve un error 404 si el recurso no existe.
Verificable: parcialmente (ORA-02). El verificador lo comprueba solo en el perfil de procedimientos.

### ORA-05 — Sin estilo telegráfico en prosa
Regla: En oraciones completas, conserva artículos, preposiciones y verbos.
Por qué: Sin artículos, el lector tiene que adivinar la relación entre las palabras.
Incorrecto: Servidor devuelve error si token caducado.
Correcto: El servidor devuelve un error si el token caducó.
Excepciones: Etiquetas, títulos y celdas de tabla breves.
Verificable: no

### ORA-06 — Un tema por párrafo
Regla: Dedica cada párrafo a un único tema. Si cambias de tema, empieza otro párrafo o usa una lista.
Por qué: Un párrafo con un tema se puede encontrar y releer sin perder el hilo.
Incorrecto: La autenticación usa tokens de acceso. Los permisos se asignan por rol y el límite de solicitudes es de 100 por minuto.
Correcto: La autenticación usa tokens de acceso. Cada token caduca a los 60 minutos.
Excepciones: Ninguna.
Verificable: no

## Longitud

### ORA-03 — Longitud en procedimientos
Regla: Revisa toda oración de un procedimiento que supere 25 palabras. Divídela si puedes hacerlo sin perder información.
Por qué: Las oraciones largas esconden condiciones y acciones.
Incorrecto: Para configurar la integración con el proveedor de identidad debes abrir la consola de administración, ir a la sección de seguridad y escribir la URL del proveedor junto con el identificador del cliente.
Correcto: Abre la consola de administración. En la sección «Seguridad», escribe la URL del proveedor de identidad y el identificador del cliente.
Excepciones: Nunca elimines una condición, una advertencia o un dato para cumplir el umbral. El código, las rutas y las variables no cuentan como palabras.
Verificable: sí (ORA-03). Es un aviso, nunca un rechazo.

### ORA-04 — Longitud en descripciones
Regla: Revisa toda oración descriptiva que supere 30 palabras.
Por qué: La prosa conceptual admite oraciones algo más largas, pero no ilimitadas.
Incorrecto: El servicio de colas recibe los mensajes que publican los productores, los guarda en disco durante el periodo de retención configurado y los entrega a los consumidores en el mismo orden en que llegaron, salvo que se active el modo de prioridad.
Correcto: El servicio de colas guarda en disco los mensajes que publican los productores. Los entrega a los consumidores en el orden de llegada. Si activas el modo de prioridad, el orden depende de la prioridad de cada mensaje.
Excepciones: Igual que ORA-03. En interfaz no hay umbral general.
Verificable: sí (ORA-04). Es un aviso, nunca un rechazo.

## Nominalizaciones y cadenas

### ORA-07 — Verbo de apoyo con nominalización
Regla: No uses «realizar», «efectuar» o «llevar a cabo» seguidos de un sustantivo de acción. Usa el verbo de esa acción.
Por qué: La forma con verbo de apoyo es más larga y no aporta información.
Incorrecto: Realiza la actualización de la configuración del servicio.
Correcto: Actualiza la configuración del servicio.
Excepciones: Si no existe un verbo para la acción, o el verbo cambia el significado.
Verificable: sí (ORA-07)

### ORA-08 — Cadenas de tres o más «de»
Regla: Revisa los grupos con tres o más «de» encadenados. Reformula con un verbo o con un término del glosario.
Por qué: En una cadena larga no queda claro qué complementa a qué.
Incorrecto: Cambia el valor del tiempo de espera de la política de acceso del servicio.
Correcto: Cambia el tiempo de espera en la política de acceso del servicio.
Excepciones: Los términos de varias palabras del glosario, como «copia de seguridad» o «base de datos», cuentan como una unidad.
Verificable: sí (ORA-08)

### ORA-09 — Los términos consolidados se mantienen
Regla: No reemplaces un término técnico consolidado solo porque es largo o es una nominalización.
Por qué: «Autenticación» o «compilación» son términos precisos; una perífrasis los vuelve vagos.
Incorrecto: Revisa cómo el sistema comprueba quién eres.
Correcto: Revisa la configuración de autenticación.
Excepciones: Ninguna.
Verificable: no

### ORA-10 — Complementos con más de un núcleo posible
Regla: Si un complemento con «de» puede referirse a dos sustantivos, reformula para dejar una sola lectura.
Por qué: En «registro de errores del cliente» no queda claro si el cliente genera los errores o es dueño del registro.
Incorrecto: Descarga el registro de errores del cliente.
Correcto: Descarga el registro que guarda los errores que genera el cliente.
Excepciones: Si el glosario del proyecto define el término completo, úsalo tal cual.
Verificable: no

## Concordancia y género

### ORA-11 — Reformula sin marcar el género de la persona
Regla: Si el género de la persona no importa, reformula con segunda persona, sustantivos colectivos o construcciones sin persona. No uses @, x ni terminaciones alternativas en el perfil base.
Por qué: Las reformulaciones naturales se leen sin esfuerzo y las entienden los lectores de pantalla.
Incorrecto: Bienvenido/a, querido usuario. Todxs lxs usuarixs deben confirmar la cuenta.
Correcto: Te damos la bienvenida. Cada cuenta debe confirmarse antes de 7 días.
Excepciones: Cuando el texto se refiere a una persona concreta, respeta cómo se identifica.
Verificable: parcialmente (ORA-11). El verificador marca barras de género, @, x y terminaciones en «-e» frecuentes.

### ORA-12 — Sin artículos dobles en plantillas
Regla: No escribas plantillas como «El/La {objeto}». Escribe una cadena completa para cada caso o una estructura que no dependa del género.
Por qué: Una plantilla que no garantiza la concordancia produce textos como «La archivo».
Incorrecto: El/La {objeto} se eliminó.
Correcto: Se eliminó el elemento: {nombre}.
Excepciones: Ninguna.
Verificable: sí (ORA-12)
