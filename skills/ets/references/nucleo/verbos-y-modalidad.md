# Verbos y modalidad

Reglas del núcleo sobre tratamiento, tiempos verbales, modalidad, voz pasiva y gerundio. Se aplican a todos los perfiles, salvo que el perfil indique otra cosa.

## Tratamiento

### VER-01 — Tuteo sin voseo
Regla: Dirígete al lector con «tú». No uses formas de voseo en el perfil internacional.
Por qué: El voseo es correcto en la norma culta de varios países, pero marca región en un texto para todo el ámbito hispanohablante.
Incorrecto: Seleccioná la cuenta y tocá «Continuar».
Correcto: Selecciona la cuenta y toca «Continuar».
Excepciones: Un perfil regional documentado puede usar voseo de forma consistente (ver variacion-regional.md).
Verificable: sí (VER-01)

### VER-02 — Sin «vosotros»
Regla: No uses «vosotros», sus pronombres ni sus formas verbales. Para varias personas, usa «ustedes».
Por qué: «vosotros» solo se usa en gran parte de España.
Incorrecto: Abrid el panel y revisad vuestra configuración.
Correcto: Abre el panel y revisa la configuración.
Excepciones: Ninguna en el perfil internacional.
Verificable: sí (VER-02)

### VER-03 — No mezcles «tú» y «usted»
Regla: Usa un único tratamiento en todo el texto. El perfil base usa «tú».
Por qué: Mezclar tratamientos parece un error de traducción y confunde sobre quién es el destinatario.
Incorrecto: Abre el archivo. Después, seleccione «Guardar».
Correcto: Abre el archivo. Después, selecciona «Guardar».
Excepciones: El perfil alternativo de «usted» es válido si se usa en todo el texto. El plural «ustedes» no cuenta como mezcla.
Verificable: sí (VER-03)

### VER-04 — No repitas el pronombre «tú»
Regla: Omite el pronombre «tú» como sujeto. La forma del verbo ya indica la persona.
Por qué: El pronombre explícito suena enfático y alarga la oración.
Incorrecto: Tú debes confirmar el cambio antes de continuar.
Correcto: Debes confirmar el cambio antes de continuar.
Excepciones: Cuando contrastas dos agentes: «Tú creas la clave; el servicio la rota cada mes».
Verificable: sí (VER-04)

## Tiempos verbales

### VER-05 — Presente para el comportamiento general
Regla: Describe en presente lo que el sistema hace siempre que se dan las condiciones.
Por qué: El futuro sugiere que el comportamiento todavía no existe.
Incorrecto: La API devolverá un error si falta el parámetro.
Correcto: La API devuelve un error si falta el parámetro.
Excepciones: Notas de versión (pasado) y hechos que ocurren en un momento futuro concreto (VER-06).
Verificable: no

### VER-06 — Futuro solo si el momento es información
Regla: Usa el futuro solo cuando el momento futuro es parte de lo que el lector necesita saber.
Por qué: Así el futuro conserva su valor informativo.
Incorrecto: El servidor validará el token en cada solicitud.
Correcto: El certificado caduca el 1 de marzo de 2027. A partir de esa fecha, el servidor rechazará las conexiones.
Excepciones: Promesas o anuncios explícitos en notas de versión.
Verificable: parcialmente (VER-06). En el perfil de conceptos y API, el verificador sugiere revisar cada futuro.

### VER-07 — Condicional solo para hipótesis
Regla: No uses el condicional para suavizar una obligación o una instrucción.
Por qué: «Deberías» deja dudas sobre si la acción es obligatoria.
Incorrecto: Deberías crear una copia de seguridad antes de migrar.
Correcto: Crea una copia de seguridad antes de migrar.
Excepciones: Hipótesis reales: «Si el disco se llenara durante la copia, el proceso se detendría sin perder datos».
Verificable: sí (VER-07)

### VER-08 — Subjuntivo cuando la construcción lo exige
Regla: Usa el subjuntivo en prohibiciones, en oraciones con «que» que lo piden y en condiciones de tiempo.
Por qué: Evitar el subjuntivo produce oraciones agramaticales o artificiales.
Incorrecto: Espera a que termina el proceso.
Correcto: Espera a que termine el proceso. No cierres la ventana hasta que aparezca el mensaje de confirmación.
Excepciones: Ninguna.
Verificable: no. El verificador nunca marca el subjuntivo como error.

## Modalidad

### VER-09 — Una forma para cada modalidad
Regla: Usa «debes» para requisitos, «puedes» o «puede» para capacidades y posibilidades, «se recomienda» para recomendaciones y «no» con imperativo para prohibiciones.
Por qué: Cambiar la modalidad cambia el significado técnico: una recomendación no es un requisito.
Incorrecto: Puedes tener permiso de administración para instalar el agente.
Correcto: Debes tener permiso de administración para instalar el agente.
Excepciones: Si «puede» admite dos lecturas (capacidad o posibilidad), reformula: «La actualización tarda hasta 10 minutos».
Verificable: no

### VER-10 — «Se debe» solo con agente identificable
Regla: No uses «se debe», «se tiene que» o «hay que» sin que el lector sepa quién actúa. Nombra al agente o usa el imperativo.
Por qué: «Se debe reiniciar» no dice quién reinicia ni qué componente.
Incorrecto: Se debe reiniciar antes de aplicar los cambios.
Correcto: Reinicia el servicio antes de aplicar los cambios.
Excepciones: Requisitos generales de un sistema, cuando el agente es cualquier cliente: El cliente debe enviar el encabezado `Authorization`.
Verificable: sí (VER-10)

## Voz y agente

### VER-11 — Pasiva refleja para estados y resultados
Regla: Usa la pasiva refleja cuando informas un resultado y el agente no importa.
Por qué: Es la forma natural del español para resultados y no oculta información relevante.
Incorrecto: El sistema encontró tres errores en la validación.
Correcto: Se encontraron tres errores en la validación.
Excepciones: Si el lector necesita saber quién actuó, usa la activa con agente (VER-14).
Verificable: no. El verificador no marca la pasiva refleja.

### VER-12 — Pasiva perifrástica con «por»
Regla: Si la oración nombra al agente con «por», reescríbela en activa.
Por qué: La activa es más corta y pone primero a quien actúa.
Incorrecto: Los archivos temporales son eliminados por el proceso de limpieza.
Correcto: El proceso de limpieza elimina los archivos temporales.
Excepciones: Cuando el objeto es el tema del párrafo y cambiar el orden rompe la continuidad.
Verificable: sí (VER-12)

### VER-13 — Gerundio de posterioridad o de acción encadenada
Regla: No uses el gerundio para una acción posterior ni para añadir una segunda acción. Usa una oración nueva o «y».
Por qué: El gerundio indica simultaneidad o modo; con valor de posterioridad, el orden de las acciones queda ambiguo.
Incorrecto: Instala el paquete, reiniciando después el servicio.
Correcto: Instala el paquete. Después, reinicia el servicio.
Excepciones: El gerundio de modo es correcto: Abre el panel pulsando la tecla F2.
Verificable: parcialmente (VER-13)

### VER-14 — No inventes ni ocultes el agente
Regla: Si sabes qué componente actúa, nómbralo. No sustituyas un «se» por «el sistema» si «el sistema» no es el agente real.
Por qué: Un agente falso o vago lleva a buscar el problema en el componente equivocado.
Incorrecto: El sistema elimina los registros antiguos.
Correcto: La tarea programada `cleanup` elimina los registros de más de 30 días.
Excepciones: Si el agente es desconocido o irrelevante, usa la pasiva refleja (VER-11).
Verificable: no
