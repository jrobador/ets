# Terminología y referentes

Reglas del núcleo para elegir términos y para que cada pronombre, posesivo y sujeto tenga un solo referente posible. Se aplican a todos los perfiles.

Formato de cada regla: ID, regla, motivo, ejemplo incorrecto, ejemplo correcto, excepciones y si el verificador la comprueba.

## Términos

### TER-01 — Un concepto, un término
Regla: Usa siempre el término preferido del glosario para cada concepto. No alternes sinónimos por variedad de estilo.
Por qué: Quien lee interpreta que dos términos distintos nombran dos cosas distintas.
Incorrecto: Sube el fichero de configuración. Después, valida el archivo con la CLI.
Correcto: Sube el archivo de configuración. Después, valida el archivo con la CLI.
Excepciones: Las etiquetas literales de una interfaz ajena se conservan (TER-05). En modo estándar, un término admitido del glosario es válido.
Verificable: parcialmente (TER-01). El verificador marca los términos desaconsejados del glosario; no detecta sinónimos que el glosario no cubre.

### TER-02 — Sin híbridos verbales del inglés
Regla: No formes verbos con raíz inglesa y terminación española. Usa el verbo español del glosario.
Por qué: Los híbridos cambian de forma según el país y suelen ser coloquiales.
Incorrecto: Loguéate y deployá la rama.
Correcto: Inicia sesión y despliega la rama.
Excepciones: Ninguna en prosa. El código y los comandos literales se conservan entre comillas invertidas.
Verificable: sí (TER-02)

### TER-03 — Sin verbos comodín con objetos técnicos
Regla: No uses «dar», «poner» o «hacer» como verbo principal de una acción técnica. Usa el verbo que nombra la acción.
Por qué: Los verbos comodín admiten varias interpretaciones; «poner el servidor» puede significar iniciar, instalar o configurar.
Incorrecto: Dale permisos de escritura y haz un deploy.
Correcto: Concede permiso de escritura y despliega la versión.
Excepciones: Locuciones del glosario como «hacer clic» (TER-11).
Verificable: parcialmente (TER-03)

### TER-04 — Términos ingleses: solo los reconocidos y definidos
Regla: Conserva un término inglés solo si el público lo reconoce como nombre del concepto y la traducción confunde. Defínelo la primera vez que aparece.
Por qué: Una traducción forzada puede ser menos clara que el término original, pero un término sin definir excluye a parte del público.
Incorrecto: Configura el webhook con el payload firmado.
Correcto: Configura el webhook (una URL que recibe avisos de eventos) y firma el contenido de cada aviso.
Excepciones: Si el glosario del proyecto ya define el término, no hace falta repetir la definición.
Verificable: no

### TER-05 — La etiqueta visible manda sobre el glosario
Regla: Reproduce las etiquetas de una interfaz exactamente como aparecen, aunque usen un término desaconsejado.
Por qué: Quien sigue la instrucción busca en la pantalla el texto literal.
Incorrecto: Selecciona «Abrir archivo» (la interfaz muestra «Abrir fichero»).
Correcto: Selecciona «Abrir fichero».
Excepciones: Ninguna. Si la etiqueta es confusa, sugiere el cambio a quien mantiene la interfaz.
Verificable: no. El verificador protege el texto entre «», así que no marca etiquetas literales.

### TER-06 — Sin jerga ni coloquialismos
Regla: Describe el estado técnico con palabras neutras.
Por qué: La jerga cambia entre países y puede ser imprecisa.
Incorrecto: El servidor se colgó y la app petó.
Correcto: El servidor no responde y la aplicación se cerró.
Excepciones: Citas literales de mensajes del sistema.
Verificable: parcialmente (TER-06)

### TER-11 — Locuciones como una sola unidad
Regla: Trata las locuciones del glosario, como «hacer clic» o «iniciar sesión», como una sola entrada. No las evalúes por el verbo genérico que contienen.
Por qué: «hacer clic» es una acción precisa; «hacer» suelto no lo es.
Incorrecto: Realiza un clic en el icono.
Correcto: Haz clic en el icono.
Excepciones: Ninguna.
Verificable: no

## Sujetos y referentes

### TER-07 — Instrucción y descripción en oraciones separadas
Regla: No mezcles en la misma oración una acción del lector y una acción del sistema con el mismo sujeto tácito. Nombra el sujeto de la acción del sistema.
Por qué: Con sujeto tácito, «Valida el token y devuelve un error» puede leerse como dos instrucciones al lector.
Incorrecto: Valida el token y devuelve un error 401 si no es válido.
Correcto: El servidor valida el token. Si el token no es válido, el servidor devuelve un error 401.
Excepciones: Si el contexto deja claro que todo el texto describe al sistema, como en la referencia de una función, el sujeto tácito es aceptable.
Verificable: no

### TER-08 — Un pronombre átono, un referente
Regla: Usa «lo», «la», «los», «las» o «le» solo si en la oración hay un único sustantivo al que puedan referirse. Si hay dos, repite el sustantivo.
Por qué: En «Copia el certificado junto a la clave y elimínala», la persona puede eliminar lo que no debe.
Incorrecto: Copia el certificado junto a la clave y elimínala del servidor.
Correcto: Copia el certificado junto a la clave. Después, elimina la clave del servidor.
Excepciones: Si el género o el número ya distinguen el referente sin dudas, el pronombre es aceptable: Abre el archivo y guárdalo en la carpeta temporal.
Verificable: no

### TER-09 — Repite el sustantivo entre pasos
Regla: En pasos numerados, nombra el objeto en cada paso. No uses un pronombre que remite al paso anterior.
Por qué: Quien sigue un procedimiento suele leer un paso aislado y volver a él más tarde.
Incorrecto: 3. Selecciónala y copia el valor.
Correcto: 3. Selecciona la clave de API y copia el valor.
Excepciones: Dentro del mismo paso, un pronombre con un único referente es aceptable.
Verificable: no

### TER-10 — Posesivo «su» con un solo dueño posible
Regla: Usa «su» o «sus» solo si hay un único dueño posible. Si no, nombra al dueño.
Por qué: «su clave» puede pertenecer a la persona, al servicio o a la organización.
Incorrecto: El administrador crea la cuenta para el servicio y guarda su clave.
Correcto: El administrador crea la cuenta para el servicio y guarda la clave del servicio.
Excepciones: Si la oración tiene un solo sustantivo que pueda ser dueño, «su» es claro: La API valida la solicitud y su firma.
Verificable: parcialmente (TER-10). El verificador sugiere revisar «su» cuando hay varios sustantivos antes.
