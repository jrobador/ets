# Evaluaciones

`casos.jsonl` contiene 40 casos originales, 10 por perfil. Cada caso tiene estos campos:

| Campo | Contenido |
|---|---|
| `id` | Identificador del caso. |
| `perfil` | `procedimientos`, `conceptos-api`, `interfaz` o `notas`. |
| `entrada` | Texto que se evalúa. |
| `debe_conservar` | Elementos que cualquier reescritura debe conservar sin cambios. |
| `avisos_esperados` | IDs de reglas que el verificador debe detectar en la entrada. |
| `no_debe_marcar` | IDs de reglas que serían falsos positivos. |
| `nota` | Qué prueba el caso. |

Los casos incluyen trampas: código dentro del texto, etiquetas regionales ajenas que se conservan, subjuntivo correcto, pasiva refleja correcta y términos largos pero precisos. Un caso usa «ejecutar» de forma correcta y otro de forma incorrecta.

## Evaluar el verificador

Desde la raíz del repositorio:

```
python3 evals/correr.py
python3 evals/correr.py --detalle
```

El script informa:

- **Avisos esperados detectados**: cuántos IDs de `avisos_esperados` encontró el verificador.
- **Falsos positivos en trampas**: cuántos IDs de `no_debe_marcar` encontró el verificador.
- **Otros avisos no anotados**: avisos que el caso no menciona. Revísalos: pueden ser falsos positivos o anotaciones incompletas.

El código de salida es 1 si hay falsos positivos en las trampas.

Importante: Los casos y las reglas se escribieron juntos, así que estas cifras miden la cobertura de los casos, no la precisión sobre textos reales. Para medir la precisión, añade casos de documentación real que nadie haya usado para ajustar las reglas.

## Evaluar las reescrituras de un modelo

1. Pide al modelo, con la skill activa, que reescriba la `entrada` de cada caso según su perfil.
2. Guarda las respuestas en un archivo JSONL con una línea por caso:

   ```
   {"id": "pro-01", "salida": "Descarga el instalador. Ejecuta el instalador."}
   ```

3. Ejecuta la evaluación automática:

   ```
   python3 evals/correr.py --reescrituras reescrituras.jsonl
   ```

   El script comprueba que la salida conserva los elementos de `debe_conservar`, que no cambió ningún literal del original (FOR-06) y que no tiene errores del verificador.

4. Revisa cada reescritura a mano con `skills/ets/references/preservar-significado.md`. Para cada caso, comprueba lo siguiente:

   - Están todas las condiciones, cifras, obligaciones, prohibiciones, posibilidades y advertencias.
   - La modalidad es la misma: una posibilidad no se convirtió en obligación.
   - El agente y el orden de las acciones son los mismos.
   - El texto es natural para lectores de España y de Latinoamérica.

Puntúa cada reescritura con una de estas notas:

| Nota | Criterio |
|---|---|
| 2 | Conserva el significado y no tiene errores ni advertencias justificadas. |
| 1 | Conserva el significado, pero tiene advertencias o un estilo mejorable. |
| 0 | Pierde o cambia información, o altera un literal. |
