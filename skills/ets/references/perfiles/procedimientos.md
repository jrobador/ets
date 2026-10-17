<!-- ets: perfil=procedimientos -->
# Perfil: procedimientos

Para guías paso a paso, instalación, configuración, tutoriales, guías de solución de problemas y cualquier texto que pide al lector una secuencia de acciones.

## Cambios sobre el núcleo

| Regla del núcleo | Cambio en este perfil |
|---|---|
| ORA-02 | Se comprueba siempre: la condición va antes de la acción. |
| ORA-03 | Umbral de aviso de 25 palabras por oración. |
| ORA-04 | No se aplica; ORA-03 la reemplaza. |
| TER-09 | Obligatoria en pasos numerados. |
| VER-10 | Se amplía con PRO-08. |

## Estructura recomendada

```
## Configurar <tarea en infinitivo>

<Una o dos oraciones: qué consigue el lector.>

### Requisitos

- <Permiso, versión o dato necesario.>

### Pasos

1. <Acción en imperativo.>
   <Resultado esperado, si lo hay.>
2. <Acción en imperativo.>

### Resultado

<Cómo comprueba el lector que terminó bien.>
```

## Reglas

### PRO-01 — Una acción del lector por paso
Regla: Cada paso numerado contiene una sola acción del lector. Un paso puede incluir además la condición y el resultado esperado.
Por qué: El lector marca mentalmente cada paso como hecho; dos acciones en un paso hacen que salte una.
Incorrecto: 2. Abre la terminal, instala la CLI y comprueba la versión.
Correcto: 2. Abre una terminal. 3. Instala la CLI. 4. Comprueba la versión instalada.
Excepciones: Dos acciones inseparables sobre el mismo objeto: Copia el token y pégalo en el campo «Token».
Verificable: no

### PRO-02 — Pasos en imperativo, no en infinitivo
Regla: Escribe cada paso con el imperativo de «tú».
Por qué: El infinitivo se reserva para títulos y botones (INT-01), así se distingue qué es una instrucción.
Incorrecto: 1. Abrir la consola de administración.
Correcto: 1. Abre la consola de administración.
Excepciones: Ninguna en los pasos.
Verificable: sí (PRO-02)

### PRO-03 — Título de la tarea en infinitivo
Regla: Escribe el título del procedimiento en infinitivo, con el objeto de la tarea.
Por qué: El título nombra la tarea; los pasos dan las órdenes.
Incorrecto: Configura la autenticación
Correcto: Configurar la autenticación
Excepciones: Una guía para resolver un problema puede usar el síntoma como título: El servidor no inicia.
Verificable: no

### PRO-04 — Requisitos antes de los pasos
Regla: Escribe en una sección «Requisitos», antes del primer paso, los permisos, versiones y datos que el lector necesita.
Por qué: Descubrir un requisito en el paso 6 obliga a deshacer los pasos anteriores.
Incorrecto: 6. Para este paso necesitas permiso de administración.
Correcto: Requisitos: permiso de administración en el proyecto.
Excepciones: Ninguna.
Verificable: no

### PRO-05 — Resultado separado de la acción
Regla: Escribe el resultado esperado en una oración aparte, después de la acción, en presente o con pasiva refleja.
Por qué: El lector distingue lo que debe hacer de lo que debe ver.
Incorrecto: 3. Selecciona «Guardar» y verás el mensaje de confirmación.
Correcto: 3. Selecciona «Guardar». Aparece el mensaje «Cambios guardados».
Excepciones: Ninguna.
Verificable: no

### PRO-06 — Aviso antes del paso de riesgo
Regla: Escribe el aviso antes del paso peligroso, no después. El aviso dice el riesgo, la consecuencia y cómo evitarla.
Por qué: Un aviso después del paso llega tarde.
Incorrecto: 4. Ejecuta `db reset`. Advertencia: este comando elimina todos los datos.
Correcto: Advertencia: El comando `db reset` elimina todos los datos de la base de datos. Crea una copia de seguridad antes de continuar. 4. Ejecuta `db reset`.
Excepciones: Ninguna.
Verificable: no

### PRO-07 — Tres niveles de aviso
Regla: Usa solo tres niveles de aviso, cada uno con una función fija:
- «Advertencia»: pérdida de datos, riesgos de seguridad u operaciones irreversibles.
- «Importante»: requisitos sin los cuales la tarea falla.
- «Nota»: información útil que no cambia el resultado.
Por qué: Pocos niveles con funciones fijas evitan que el lector ignore los avisos.
Incorrecto: Cuidado: el comando borra la caché.
Correcto: Nota: El comando vacía la caché. La primera carga posterior tarda más.
Excepciones: Si el producto ya define otros niveles, usa los del producto.
Verificable: parcialmente (PRO-07). El verificador sugiere cambiar etiquetas como «Cuidado», «Peligro» o «Atención».

### PRO-08 — Recomendaciones con destinatario
Regla: En un procedimiento, no uses «se recomienda» ni «se aconseja». Usa el imperativo o explica la consecuencia.
Por qué: En una secuencia de pasos, el lector necesita saber si la acción es parte del procedimiento.
Incorrecto: Se recomienda crear una rama antes de empezar.
Correcto: Crea una rama antes de empezar. Así puedes descartar los cambios sin afectar la rama principal.
Excepciones: En textos conceptuales, «se recomienda» es la forma de la recomendación (VER-09).
Verificable: sí (PRO-08)

### PRO-09 — Elementos de interfaz con «seleccionar»
Regla: Para activar un elemento de la interfaz, usa «selecciona» seguido de la etiqueta entre comillas angulares. Si el método de entrada importa, usa «haz clic», «toca» o «pulsa».
Por qué: «Seleccionar» sirve para ratón, teclado, pantalla táctil y tecnologías de apoyo.
Incorrecto: Pincha en el botón Guardar.
Correcto: Selecciona «Guardar».
Excepciones: Atajos de teclado: Pulsa Ctrl+S.
Verificable: no

## Ejemplo completo

### Crear una clave de API

Crea una clave de API para que tu aplicación pueda enviar solicitudes al servicio.

Requisitos:

- Permiso de administración en el proyecto.

Pasos:

1. Abre la consola y selecciona el proyecto.
2. Selecciona «Configuración > Claves de API».
3. Selecciona «Crear clave».
   Aparece un cuadro de diálogo con la clave nueva.
4. Copia la clave.
   Advertencia: La consola muestra la clave una sola vez. Si cierras el cuadro de diálogo sin copiar la clave, debes crear otra.
5. Guarda la clave en el gestor de secretos de tu equipo.
