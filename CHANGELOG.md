# Registro de cambios

Este archivo registra los cambios de las reglas, el glosario y el verificador. Las versiones siguen el formato `MAYOR.MENOR.PARCHE`.

## 0.1.0 — 17 de octubre de 2026

### Novedades

- Primera versión de la skill `ets`.
- Núcleo de reglas en cuatro archivos: terminología y referentes (TER), verbos y modalidad (VER), oraciones (ORA) y formato (FOR).
- Cuatro perfiles: procedimientos (PRO), conceptos y API (API), interfaz y mensajes (INT) y notas de versión (NOT).
- Glosario con 99 conceptos de software, organizado por concepto, con patrones de uso.
- Guía de preservación del significado y ejemplos de antes y después por perfil.
- Verificador `verificar.py` con 36 reglas deterministas, tres niveles de aviso, detección de perfil, modos estándar y estricto, salida en texto o JSON y comparación de literales con el original.
- Protección de código, URL, rutas, variables, opciones, identificadores y etiquetas de interfaz.
- 40 casos de evaluación y pruebas del verificador y del glosario.
