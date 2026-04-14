# Historial de cambios de CORPUS

## [Pre-alpha v1.2.0] - 2026-04-14

### Añadido (mejoras documentadas en `update.md`)

- **Integración de piezoeléctricos:** Sensores de vibración y actuadores hápticos en manos y dedos. Coste estimado de 50 USD por mano. Componentes: Murata 7BB-27-4, Noliac NAC2122, ADG732, driver PiezoDrive PDX150.
- **Conectividad entre módulos con fibra óptica:** Backbone de fibra monomodo (9/125 µm) con transceptores BiDi (1000BASE-BX). Reducción de peso, inmunidad EMI y mayor ancho de banda.
- **Transmisión sin contacto para articulaciones:** Alternativa a anillos colectores. Para giro limitado: cables Chainflex CFROBOT (Igus). Para giro continuo: inductiva (Würth WE-ACPR) + óptica (Bytelight).
- **Articulaciones como motores de accionamiento directo:** Rotor = pasador de la articulación, estator = carcasa fija. Eliminación de backlash, ruido y mantenimiento. Refrigeración por el sistema circulatorio de CORPUS.
- **Sensores de posición por articulación:**
  - Articulaciones principales: sensor inductivo AS5715R (ams AG) + rueda fónica conductora. Precisión <0.075°, certificación AEC-Q100, ISO 26262 ASIL C(D).
  - Articulaciones secundarias y dedos: sensor GMR TLE5012B (Infineon) o AMR KMZ80 (NXP) + imán dipolo. Resolución 0.01°.
- **Sistema de Soporte Vital Integrado (Avatar + Paciente):** Mantiene la integridad de CORPUS como extensión física del usuario. Modos: Activo, Pausa, Emergencia. Gestión de baterías duales, refrigeración, comunicaciones redundantes (fibra + LoRa).
- **Parámetros de seguridad para paciente postrado:** Prevención de úlceras por presión, detección de intentos de levantarse, limitación de movimientos bruscos, monitorización de frecuencia cardíaca y temperatura.
- **Integración de gafas de realidad aumentada (AR):** Muestran el estado del avatar y el video de las cámaras de CORPUS. Conexión por fibra óptica.
- **Memoria psiquiátrica:** Almacenamiento y reconocimiento de patrones temporales de signos vitales (EEG, pulso, temperatura) para anticipar crisis. Respuestas preventivas (voz calmante, reducción de velocidad, alerta LoRa).

### Modificado

- **README.md:** Añadidos badges de estado, enlace a `update.md`, y sección de mejoras recientes.
- **README.en.md:** Actualización correspondiente en inglés.
- **Estructura de carpetas:** Añadida carpeta `docs/` con documentación técnica de las mejoras.

### Corregido

- Unificación de checkboxes en `update.md` (formato Markdown).
- Reemplazo de componentes obsoletos: Murata 7BB-20-6 (discontinued) → 7BB-27-4 / TDK PS1240P02BT.
- Costos unificados en la sección de fibra óptica.
- Corrección de enlaces y formato en los READMEs.

### Nota

Todos los cambios son especificaciones conceptuales. No hay prototipos funcionales. Los componentes seleccionados son sugerencias basadas en hojas de datos y disponibilidad comercial. La integración completa requerirá pruebas adicionales.

---

## [Pre-alpha v1.0.0] - 2026-03-31

### Añadido

- Repositorio inicial con README en español e inglés.
- Estructura de carpetas: `cad/`, `docs/`, `hardware/`, `launch/`, `references/`, `simulations/`, `urdf/`.
- Archivos de licencia, código de conducta, contribución y seguridad.
- Concepto de cuerpo artificial con esqueleto de grafito-tungsteno, piel sensible, energía autónoma, refrigeración circulatoria y redundancia activa.
- Simulaciones en Gazebo y MuJoCo.
- Prototipo de articulación funcional.

### Modificado

- N/A (versión inicial).

### Corregido

- N/A (versión inicial).

### Nota

Primera versión documentada del concepto. Sin mejoras adicionales.
## [0.1.0] - 2026-03-26
[Registro inicial...]

### Cambiado
- Licencia actualizada a formato propietario con restricción comercial explícita y contacto para consultas.
