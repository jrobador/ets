# Ejemplos

Pares originales de antes y después, por perfil. Cada par indica las reglas aplicadas. Todos los ejemplos son originales del proyecto ETS y se publican con licencia CC BY 4.0.

<!-- ets: perfil=procedimientos -->
## Procedimientos

### P1. Instalar la CLI

Antes: Para poder empezar a usar la herramienta, primero que nada deberías bajar el instalador y correrlo, reiniciando la terminal al terminar.

Después: Descarga el instalador. Ejecuta el instalador. Cuando termine la instalación, cierra la terminal y abre una terminal nueva.

Reglas aplicadas: TER-01 (descargar, ejecutar), VER-07 (sin condicional de cortesía), VER-13 (sin gerundio de posterioridad), ORA-01 (una acción por oración).

### P2. Eliminar un entorno

Antes: Borra el entorno desde el panel si ya no lo usas, pero ojo porque se pierden los datos.

Después: Advertencia: Al eliminar un entorno, se eliminan también sus bases de datos. Si ya no usas el entorno de pruebas, crea una copia de seguridad de las bases de datos. Después, selecciona «Eliminar entorno».

Reglas aplicadas: ORA-02 (condición antes), PRO-06 (aviso antes del paso), PRO-07 (nivel «Advertencia»), TER-06 (sin coloquialismos), TER-01 (eliminar).

### P3. Conceder acceso

Antes: 1. Ir a Ajustes → Miembros. 2. Darle permisos al usuario y se recomienda avisarle.

Después:

1. Abre «Ajustes > Miembros».
2. Selecciona a la persona.
3. Concede el permiso de lectura.
4. Avisa a la persona por correo electrónico de que ya tiene acceso.

Reglas aplicadas: PRO-02 (imperativo), PRO-01 (una acción por paso), FOR-04 (ruta con « > »), TER-05 (la etiqueta «Ajustes» se conserva), TER-03 (conceder), PRO-08 (sin «se recomienda»), ORA-11 (sin género de la persona).

<!-- ets: perfil=conceptos-api -->
## Conceptos y API

### A1. Comportamiento de reintentos

Antes: Se reintentará la request en caso de fallo hasta 3 veces, esperando 2s entre intentos.

Después: Si una solicitud falla, el cliente la reintenta hasta 3 veces. El cliente espera 2 s entre un intento y el siguiente.

Reglas aplicadas: API-01 (presente y agente), TER-01 (solicitud), VER-13 (sin gerundio encadenado), FOR-07 (espacio antes de la unidad).

### A2. Parámetro obligatorio

Antes: Se puede mandar el header X-Tenant-Id para identificar al tenant, si no la API usará el default.

Después: El cliente puede enviar el encabezado `X-Tenant-Id` para indicar la organización. Si el cliente no envía el encabezado, la API usa la organización predeterminada de la cuenta.

Reglas aplicadas: API-02 (capacidad, no obligación), API-03 (literal entre comillas invertidas), VER-05 (presente), TER-01 (valor predeterminado).

### A3. Descripción de arquitectura

Antes: Los eventos son procesados por el worker que los saca de la cola y realiza la actualización de los datos de la base de datos de reportes del cliente.

Después: El proceso `worker` lee los eventos de la cola. Por cada evento, el proceso actualiza la base de datos de informes.

Reglas aplicadas: VER-12 (activa), ORA-07 (sin «realizar»), ORA-08 (cadena de «de»), ORA-10 (sin complemento ambiguo), FOR-05 (identificador entre comillas invertidas).

<!-- ets: perfil=interfaz -->
## Interfaz y mensajes

### I1. Error de formulario

Antes: Error Fatal: Datos Inválidos

Después: El correo electrónico no tiene un formato válido. Revisa que incluya una arroba y un dominio.

Reglas aplicadas: INT-04 (qué pasó y qué hacer), INT-05 (sin «fatal» ni «inválido»), INT-02 (mayúscula solo inicial).

### I2. Botones de un cuadro de diálogo

Antes: ¿Seguro? [Ok] [Cancel]

Después: ¿Eliminar el proyecto «Tienda»? Esta acción no se puede deshacer. Botones: «Eliminar» y «Cancelar».

Reglas aplicadas: INT-01 (verbo en infinitivo en el botón), FOR-02 (signo de apertura), INT-04 (consecuencia explícita).

### I3. Plantilla con concordancia

Antes: El/La {tipo} "{nombre}" ha sido eliminado/a correctamente.

Después: Se eliminó «{nombre}».

Reglas aplicadas: ORA-12 (sin artículos dobles), ORA-11 (sin barras de género), INT-08 (resultado breve), VER-12 (sin pasiva perifrástica).

<!-- ets: perfil=notas -->
## Notas de versión

### N1. Corrección

Antes: Fixeamos un bug que hacía que los usuarios se deslogueen solos.

Después: Se corrigió un error que cerraba la sesión sin motivo.

Reglas aplicadas: NOT-01 (pasado), TER-02 (sin híbridos), ORA-11 (sin género de la persona).

### N2. Cambio incompatible

Antes: Cambiamos el formato del campo fecha.

Después: El campo `created_at` ahora devuelve la fecha en formato ISO 8601 con zona horaria. Si tu integración lee ese campo como número, actualiza la integración antes de instalar esta versión.

Reglas aplicadas: NOT-04 (acción requerida), API-03 (literal), ORA-02 (condición antes).

### N3. Aviso de obsolescencia

Antes: El endpoint de reportes está deprecado y se va a borrar pronto.

Después: El endpoint `GET /v1/reports` es obsoleto. La versión 4.0.0, prevista para el 1 de marzo de 2027, eliminará el endpoint. Usa `GET /v2/reports`.

Reglas aplicadas: TER-01 (obsoleto), NOT-03 (versión y fecha inequívocas), NOT-06 (literal), VER-06 (futuro con fecha).
