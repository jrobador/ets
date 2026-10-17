<!-- ets: perfil=notas -->
# Perfil: notas de versión

Para notas de versión, registros de cambios (`CHANGELOG`), avisos de obsolescencia y guías de migración entre versiones.

## Cambios sobre el núcleo

| Regla del núcleo | Cambio en este perfil |
|---|---|
| VER-05 | No se aplica a los cambios: se usa el pasado (NOT-01). |
| VER-06 | El futuro es aceptable para anuncios de cambios próximos con fecha o versión. |
| VER-11 | La pasiva refleja es la forma habitual: «Se corrigió», «Se añadió». |
| ORA-04 | Umbral de aviso de 30 palabras por oración. |
| ORA-05 | Los elementos de lista pueden empezar con el verbo en pasado sin sujeto. |

## Estructura recomendada

```
## <versión> — <día> de <mes> de <año>

### Cambios incompatibles
### Novedades
### Cambios
### Correcciones
### Obsoleto
### Eliminado
### Seguridad
```

Omite las secciones vacías.

## Reglas

### NOT-01 — Pasado para los cambios
Regla: Describe cada cambio en pasado, con pasiva refleja o con el componente como sujeto.
Por qué: La nota informa de algo que ya ocurrió en esa versión.
Incorrecto: Corrige un error que impide iniciar sesión con SSO.
Correcto: Se corrigió un error que impedía iniciar sesión con SSO.
Excepciones: El comportamiento nuevo se puede describir en presente después del cambio: Se añadió el parámetro `retry`. El cliente reintenta las solicitudes fallidas hasta 3 veces.
Verificable: no

### NOT-02 — Agrupa por tipo de cambio
Regla: Agrupa los cambios en secciones fijas y en el mismo orden en todas las versiones.
Por qué: Quien actualiza busca primero los cambios incompatibles y los de seguridad.
Incorrecto: Una lista única con correcciones, novedades y cambios incompatibles mezclados.
Correcto: Secciones «Cambios incompatibles», «Novedades», «Correcciones» y «Seguridad», en ese orden.
Excepciones: Versiones con un solo cambio.
Verificable: no

### NOT-03 — Versión y fecha inequívocas
Regla: Escribe el número de versión completo y la fecha con el nombre del mes.
Por qué: Una fecha numérica se lee de dos formas según el país (FOR-11).
Incorrecto: v2.4 (03/04/26)
Correcto: 2.4.0 — 3 de abril de 2026
Excepciones: Archivos que una herramienta procesa, que usan la fecha ISO 8601.
Verificable: parcialmente (FOR-11)

### NOT-04 — Cambios incompatibles con la acción requerida
Regla: Para cada cambio incompatible, escribe qué cambió, a quién afecta y qué debe hacer quien actualiza.
Por qué: Un cambio incompatible sin instrucciones rompe integraciones sin aviso.
Incorrecto: Se cambió el formato de las fechas.
Correcto: El campo `created_at` ahora usa el formato ISO 8601 con zona horaria. Si tu código lee ese campo como número, cambia el analizador antes de actualizar.
Excepciones: Ninguna.
Verificable: no

### NOT-05 — Describe el efecto, no la implementación
Regla: Escribe lo que cambia para quien usa el producto. Deja los detalles internos para el historial del repositorio.
Por qué: Quien lee las notas decide si actualizar según el efecto, no según la implementación.
Incorrecto: Se refactorizó el módulo de caché y se migró a la nueva interfaz de almacenamiento.
Correcto: Las páginas de informes cargan hasta dos veces más rápido.
Excepciones: Bibliotecas para desarrolladores, cuando el cambio interno afecta a quien extiende el código.
Verificable: no

### NOT-06 — Referencias literales
Regla: Escribe los números de incidencia, los identificadores de vulnerabilidades y los nombres de versión tal cual.
Por qué: El lector los usa para buscar más información.
Incorrecto: Se corrigió la vulnerabilidad del mes pasado.
Correcto: Se corrigió la vulnerabilidad `CVE-2026-12345` en el analizador de XML (#482).
Excepciones: Ninguna.
Verificable: no

## Ejemplo completo

## 3.2.0 — 14 de octubre de 2026

### Cambios incompatibles

- El parámetro `limit` se eliminó. Usa `page_size` en su lugar.

### Novedades

- Se añadió la exportación a CSV en la página de informes.

### Correcciones

- Se corrigió un error que duplicaba las notificaciones por correo electrónico (#517).

### Obsoleto

- El endpoint `GET /v1/reports` es obsoleto y se eliminará en la versión 4.0.0. Usa `GET /v2/reports`.
