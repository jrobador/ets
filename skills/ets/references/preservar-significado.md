# Preservar el significado

Preservar el significado es la regla de mayor prioridad. Una reescritura que respeta todas las reglas, pero cambia lo que el texto dice, es incorrecta.

Aplica esta lista de comprobación cada vez que reescribas un texto existente.

## Antes de reescribir: extrae el inventario

Escribe una lista con cada uno de estos elementos del texto original:

1. **Condiciones**: «si», «cuando», «salvo que», «solo si», «antes de», «después de».
2. **Cifras y unidades**: números, límites, plazos, versiones, tamaños.
3. **Obligaciones y prohibiciones**: «debe», «es obligatorio», «no», «nunca», «solo».
4. **Posibilidades y capacidades**: «puede», «es posible», «a veces», «hasta».
5. **Recomendaciones**: «se recomienda», «conviene», «es mejor».
6. **Advertencias**: riesgos, consecuencias, operaciones irreversibles.
7. **Agentes**: quién hace cada acción: la persona, el cliente, el servidor, un proceso.
8. **Literales**: código, comandos, identificadores, rutas, URL, variables, etiquetas de interfaz.
9. **Alcance**: «todos», «cada», «algunos», «el primero», «únicamente».
10. **Orden**: la secuencia de las acciones y lo que debe ocurrir antes de cada una.

## Después de reescribir: compara

Para cada elemento del inventario, comprueba lo siguiente:

- [ ] El elemento sigue en el texto.
- [ ] La modalidad es la misma: una obligación sigue siendo obligación y una posibilidad sigue siendo posibilidad.
- [ ] El alcance es el mismo: «todos» no se convirtió en «los» ni «solo» desapareció.
- [ ] El agente es el mismo: la acción no pasó del servidor al lector, ni al revés.
- [ ] El orden es el mismo.
- [ ] Los literales están intactos. Si tienes el entorno, ejecuta el verificador con la opción `--original`.
- [ ] Las advertencias siguen antes de la acción de riesgo.

Si un elemento no cabe en la oración sin superar el umbral de longitud, divide la oración. Nunca elimines el elemento.

Si no sabes si un cambio altera el significado técnico, no lo hagas. Señálalo como pregunta para la persona que pidió la reescritura.

## Cinco reescrituras que cumplen las reglas y cambian el significado

### 1. Se pierde una condición

Original: Si el clúster tiene más de un nodo, ejecuta la migración solo desde el nodo principal.

Reescritura defectuosa: Ejecuta la migración desde el nodo principal.

Problema: Desaparece la condición «más de un nodo» y el adverbio «solo». En un clúster de un nodo, la instrucción sigue siendo válida, pero la versión nueva ya no prohíbe ejecutar la migración desde otros nodos.

Reescritura correcta: Si el clúster tiene más de un nodo, ejecuta la migración solo desde el nodo principal.

### 2. Una posibilidad se convierte en obligación

Original: El servidor puede tardar hasta 5 minutos en aplicar la configuración nueva.

Reescritura defectuosa: El servidor tarda 5 minutos en aplicar la configuración nueva.

Problema: «Puede tardar hasta» indica un máximo posible; la versión nueva afirma una duración fija. Quien lee esperará 5 minutos aunque el cambio ya esté aplicado, o pensará que hay un error si tarda menos.

Reescritura correcta: El servidor tarda como máximo 5 minutos en aplicar la configuración nueva.

### 3. Cambia el agente

Original: El cliente debe renovar el token antes de que caduque.

Reescritura defectuosa: Renueva el token antes de que caduque.

Problema: El original describe una responsabilidad del código cliente. La versión nueva convierte el requisito en una acción manual del lector.

Reescritura correcta: El cliente debe renovar el token antes de que caduque el token.

### 4. Cambia el alcance de una prohibición

Original: No elimines ninguna de las claves activas.

Reescritura defectuosa: No elimines la clave activa.

Problema: El original protege todas las claves activas; la versión nueva sugiere que hay una sola.

Reescritura correcta: No elimines las claves activas.

### 5. La advertencia queda después de la acción

Original: Antes de ejecutar `db reset`, crea una copia de seguridad: el comando elimina todos los datos.

Reescritura defectuosa: Ejecuta `db reset`. El comando elimina todos los datos. Crea una copia de seguridad.

Problema: Cada oración es breve y tiene una sola acción, pero el orden invierte la secuencia. Quien sigue los pasos pierde los datos antes de llegar a la copia de seguridad.

Reescritura correcta: Advertencia: El comando `db reset` elimina todos los datos. Crea una copia de seguridad antes de ejecutar `db reset`.
