# Variación regional

ETS usa un perfil base de español internacional: una variedad escrita que prioriza la comprensión en España y en Latinoamérica, evita marcas regionales innecesarias y mantiene elecciones estables. El perfil base no declara incorrectas las demás variedades; solo elige una opción por concepto.

## Qué no es el español internacional

- No es la etiqueta `es-419`, que identifica el español de Latinoamérica y no incluye España.
- No es la etiqueta `es-ES`, que identifica el español de España.
- No es el español del doblaje.
- No obliga a usar un único formato de números, fechas o monedas: la interfaz los formatea según la configuración regional de la persona (FOR-12).

## Elecciones del perfil base

| Concepto | Perfil base | Formas regionales que evita | Entrada del glosario |
|---|---|---|---|
| Tratamiento | tuteo | voseo, «vosotros» | VER-01, VER-02 |
| Equipo personal | equipo | «ordenador», «computadora», «computador» | `equipo` |
| Archivo | archivo | «fichero» | `archivo` |
| Teléfono | teléfono | «celular», «móvil» como sustantivo | `telefono` |
| Escribir texto | escribir | «ingresar», «introducir», «digitar» | `escribir` |
| Activar un elemento | seleccionar | «pinchar», «dar clic» | `seleccionar`, `hacer-clic` |
| Copia de datos | copia de seguridad | «backup» | `copia-de-seguridad` |
| Clave criptográfica | clave | «llave» | `clave-criptografica` |
| Comando de terminal | comando | ninguna; «orden» se admite | `comando` |

## Cuándo crear un perfil regional

Crea un perfil regional solo cuando una elección del perfil base cause fricción comprobada en el público de un producto. Por ejemplo:

- La interfaz del producto ya usa otro término y no se puede cambiar.
- Las pruebas con personas de un país muestran que un término del perfil base no se entiende o se lee como un error.
- El producto se dirige a un solo país y el equipo prefiere su variedad.

Un perfil regional cambia solo las entradas necesarias. Documenta cada cambio con el concepto, el término nuevo, el motivo y la fecha.

## Perfil alternativo de «usted»

El perfil de «usted» es válido si el producto lo exige. En la versión 0.1 está documentado, pero el verificador no lo implementa: el verificador marca como mezcla cualquier forma de «usted» en un texto que también usa «tú».

Reglas del perfil de «usted»:

- Usa «usted» en todo el texto, sin mezclar con «tú» (VER-03).
- Las instrucciones usan el imperativo de «usted».
- Las prohibiciones usan «no» con el subjuntivo de «usted».
- Los posesivos usan «su». Como «su» también puede referirse a terceros, aplica TER-10 con más cuidado.
- Los botones y títulos siguen en infinitivo; no cambian con el tratamiento.
- Omite el pronombre «usted» salvo cuando sea necesario para evitar ambigüedad.

<!-- ets: ignorar-inicio -->
Ejemplos del perfil de «usted»:

- Seleccione la cuenta y elija «Continuar».
- No cierre la ventana hasta que termine la instalación.
- Si el token caducó, inicie sesión de nuevo.
- Escriba su contraseña de la cuenta de la organización.
<!-- ets: ignorar-fin -->

## Perfil regional con voseo

Un producto dirigido solo a Argentina, Uruguay o Paraguay puede usar voseo de forma consistente. En ese caso, desactiva VER-01 en la configuración del proyecto y aplica las demás reglas sin cambios.
