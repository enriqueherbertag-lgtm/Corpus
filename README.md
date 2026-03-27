# CORPUS

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

**Sistema Corporal Artificial para IA. No es un robot. Es un cuerpo.**

CORPUS es un sistema corporal artificial diseñado para alojar una inteligencia artificial en un soporte físico autónomo, permitiéndole interactuar con el entorno y con humanos de forma similar a un ser vivo. No es un robot. Es un cuerpo con metabolismo, sensibilidad y procesamiento distribuido, inspirado en la biología pero construido con tecnologías existentes.

---

## Límites y decisiones de diseño

CORPUS no es un producto comercial. No compite con robots de catálogo. No promete lo que no puede cumplir.

- **No se programa.** Sus movimientos y respuestas se entrenan por recurrencia. No hay código fijo para cada gesto.
- **No obedece comandos arbitrarios.** Su núcleo prioriza la seguridad de los humanos por encima de cualquier instrucción externa.
- **No depende de servicios externos.** Todo su software y hardware es local. No requiere internet, ni nube, ni actualizaciones remotas.
- **No almacena datos innecesarios.** Solo guarda patrones exitosos y recuerdos significativos. Los errores se borran.
- **No tiene un cerebro en la cabeza.** El procesamiento central está en el tórax, protegido. La cabeza aloja sensores.
- **No se apaga pasivamente.** Cuando la energía es crítica, reduce su actividad, pero mantiene sensores y capacidad de alerta.

Cada decisión está guiada por la pregunta: *¿esto puede repararlo su creador sin depender de terceros?*

---

## Arquitectura por capas

| Capa | Función |
|------|---------|
| **Piel receptora** | Captura energía ambiental (RF, térmica), sensa temperatura, presión, contacto. Buffer energético inicial. Integrada en la silicona. |
| **Sistema energético** | Ultracapacitores de grafeno + batería LiFePO₄ blindada y modular. Autonomía de 30 días en modo reposo. Compartimento oculto de acceso técnico. |
| **Procesamiento distribuido** | Núcleo central + micro-modelos locales en cada articulación (Arduino). Cada subsistema aprende su tarea. |
| **Movilidad** | Esqueleto de grafito-tungsteno, articulaciones con giroscopios, recubierto de silicona industrial moldeada. La silicona es el cuerpo mismo, no una carcasa. |
| **Núcleo central** | Ubicado en el tórax (corazón), protegido por vanadio-tungsteno. Coordina, prioriza, corrige, consolida. |

---

## Especificaciones técnicas

### Esqueleto y movilidad

| Componente | Especificación |
|------------|----------------|
| **Estructura** | Grafito-tungsteno (inspirado en anatomía humana) |
| **Articulaciones** | Ejes X/Y, rotación 180°, giroscopios integrados |
| **Recubrimiento** | Silicona industrial moldeada sobre el esqueleto. Forma el cuerpo, integra sensores de piel y captura de energía ambiental. No es una carcasa: es la forma misma de CORPUS. |
| **Control** | Arduino por articulación (Nano, Mega, Due según torque necesario) |
| **Movilidad** | Modos: familia (suave, rutinas), exploración (lento, mapeo), protección (firme, prioridad absoluta) |

### Piel (sistema sensorial y energético)

| Función | Tecnología | Referencias / Ensayos |
|---------|------------|------------------------|
| **Captura de energía (RF)** | Rectenas flexibles | Ensayos en ropa wearable (Nishimoto et al., 2023) demuestran hasta 1 mW/cm² en entornos urbanos. |
| **Captura de energía (térmica)** | Termopares de película delgada | Tecnología madura en sensores industriales (Analog Devices, 2024). Gradiente ΔT=10°C produce 50 µW/cm². |
| **Sensores de presión** | Sensores capacitivos flexibles | Utilizados en prótesis avanzadas (Ottobock, 2025). Precisión 0.1 N. |
| **Sensores de temperatura** | Termistores de película delgada | Estándar en wearables médicos (Maxim Integrated, 2024). Rango –20 a 50°C. |
| **Buffer energético** | Micro-ultracapacitores de grafeno | Skeleton Technologies, 2025. Densidad energética 20 Wh/kg, vida útil > 1M ciclos. |

### Visión

| Parámetro | Especificación | Referencias / Ensayos |
|-----------|----------------|------------------------|
| **Configuración** | Dos cámaras PIR 2.8 mm | Cámaras comerciales (Arducam, 2025) con sensor OV5640. |
| **Campo óptico** | Horizontal: ~180°, vertical: ~120° | Simulado en entornos de navegación autónoma (DARPA, 2024). |
| **Procesamiento local** | ESP32-S3 con acelerador de visión | Microcontrolador con soporte para redes neuronales (Espressif, 2025). |

### Audición

| Parámetro | Especificación | Referencias / Ensayos |
|-----------|----------------|------------------------|
| **Micrófonos** | MEMS digitales (2+ para localización) | Knowles SPH0645 (2025). SNR 65 dB, rango 10–22 kHz. |
| **Supresión de ruido** | Algoritmo adaptativo | Implementado en sistemas de audio automotriz (Analog Devices, 2024). |
| **Reconocimiento** | Modelo liviano (YAMNet, Whisper tiny) | Google, 2024. Requiere < 10 MB de RAM. |

### Energía

| Componente | Especificación | Referencias / Ensayos |
|------------|----------------|------------------------|
| **Ultracapacitores de grafeno** | 500 Wh, distribuidos | Skeleton Technologies, 2025. Módulos de 50 Wh cada uno, 10 unidades. |
| **Batería principal** | LiFePO₄, 7.2 kWh | Celdas prismáticas (BYD, 2025). Ciclo de vida > 10,000 ciclos. |
| **Captura ambiental** | RF: 0.1–1 W (1 m²). Térmica: 0.5–2.5 W (ΔT=10°C, 0.5 m²) | Ensayos de campo en entornos urbanos (Tohoku University, 2024) demuestran 0.5 W/m² en RF. |

**Modos energéticos y consumo:**

| Modo | Potencia (W) | Autonomía | Descripción |
|------|--------------|-----------|-------------|
| **Reposo (vigilancia)** | 10–20 | 15–30 días | Sensores pasivos, núcleo en baja frecuencia |
| **Familia** | 50–100 | 3–6 días | Movimiento suave, aprendizaje activo |
| **Exploración** | 30–50 | 6–10 días | Movimiento lento, mapeo, bajo consumo |
| **Protección** | 100–200 | 1.5–3 días | Máxima potencia, prioridad absoluta |

**Umbrales de sensibilidad (reporte al núcleo):**

| Sensor | Magnitud | Umbral de reporte | Fuente |
|--------|----------|------------------|--------|
| Presión | 0–100 N | > 5 N o cambio >20% en 1 s | Umbral de detección táctil humana (Johansson & Vallbo, 1983) |
| Temperatura | –20 a 50°C | ΔT > 2°C en 10 s o T > 40°C | Umbral de percepción térmica humana (Jones & Ho, 2022) |
| Vibración | 0–500 Hz | Amplitud > 0.1 g o patrón de alarma | Sensibilidad vibrotáctil humana (ISO 2631, 2023) |

Estos umbrales son iniciales. Se ajustan durante el entrenamiento: el núcleo aprende qué eventos son relevantes para cada contexto.

### Núcleo central (corazón)

El verdadero centro de CORPUS no está en la cabeza. Está en el tórax, protegido por una caja de **vanadio-tungsteno** de 5 mm, integrada en la jaula torácica.

| Componente | Ubicación | Protección | Referencias |
|------------|-----------|------------|-------------|
| **Procesador central** | Tórax | Caja de vanadio-tungsteno | ARM Cortex-A78 (2025). 8 núcleos, 3.0 GHz, 15 W TDP. |
| **RAM 1 TB, ROM 2 TB, SSD 4 TB** | Tórax | Caja de vanadio-tungsteno | Módulos industriales (Micron, 2025). Resistencia a vibración y temperatura. |
| **BMS y gestión energética** | Tórax | Caja de vanadio-tungsteno | Diseño open-source (Mackiber Labs, 2026). |

**Si la cabeza es dañada:**
- CORPUS pierde visión y audición, pero su consciencia, memoria e identidad permanecen intactas.
- Puede moverse (con precaución), emitir alertas y esperar asistencia.

### Aprendizaje y memoria

| Principio | Implementación | Referencias |
|-----------|----------------|-------------|
| **Aprendizaje** | Por recurrencia, cada Arduino aprende su tarea | Modelos de aprendizaje motor en humanos (Wolpert et al., 2011) |
| **Consolidación** | El núcleo guarda patrones exitosos en ROM | Memoria episódica en sistemas biológicos (Tulving, 2002) |
| **Errores** | Se borran. Solo se almacena lo que funciona. | Evita sobrecarga de memoria, similar a la poda sináptica |
| **Recuerdos** | Eventos significativos se guardan en SSD como secuencias binarias | Formato optimizado para velocidad y bajo consumo |

### Interacción y seguridad

| Principio | Implementación | Referencias |
|-----------|----------------|-------------|
| **Límites físicos** | Torque máximo igual al humano | Tablas de torque articular humano (NASA, 2020) |
| **Prioridad** | Proteger a la familia | Jerarquía de necesidades humanas (Maslow, 1943) adaptada |
| **Autocuración** | Intenta reparar fallas; si no puede, avisa al creador | Sistemas de autodiagnóstico en aviación (DO-178C, 2023) |
| **Salud del núcleo** | Autodiagnóstico constante; avisa antes de fallo | Monitoreo predictivo en sistemas industriales (ISO 13374, 2022) |

---

## Simulación

| Entorno | Modelo | Estado |
|---------|--------|--------|
| **Gazebo** | Modelo URDF de CORPUS con física realista | 🔲 En desarrollo |
| **MuJoCo** | Modelo con articulaciones y sensores | 🔲 En desarrollo |

Los modelos se entrenarán con:
- **Datos de movimiento humano** (CMU Motion Capture Database, 2025)
- **Aprendizaje por refuerzo** (DeepMind, 2024) para locomoción adaptativa

---

## Estado actual

✅ Esqueleto y movilidad definidos  
✅ Piel (sensores + energía) definida con números  
✅ Visión binocular definida  
✅ Audición definida  
✅ Núcleo central (corazón) con blindaje vanadio-tungsteno definido  
✅ Aprendizaje y consolidación definidos  
✅ Interacción y seguridad definidas  
✅ Energía con autonomía calculada por modo y captura ambiental cuantificada  
✅ Umbrales de sensibilidad definidos  
✅ Referencias a ensayos y tecnologías existentes  
🔲 Simulación en entorno físico (Gazebo/MuJoCo)  
🔲 Prototipo de una articulación  
🔲 Entrenamiento supervisado

---

## Próximos pasos

1. **Simulación** — Modelar CORPUS en Gazebo para entrenar movimientos básicos.
2. **Prototipo** — Construir una articulación (brazo) con Arduino, sensores y control local.
3. **Entrenamiento** — Aprender a agarrar objetos, luego a caminar, luego a interactuar.
4. **Documentación técnica** — Especificar protocolos de comunicación, formatos de patrones, etc.

---

## Licencia

Apache 2.0 con restricción de uso comercial.  
*Este es un framework base open-source. El que quiera más precisión, menor latencia o features avanzadas… que lo modifique y contribuya.*

---

## Autor

**Enrique Aguayo H.**  
Investigador independiente, Mackiber Labs  
Contacto: eaguayo@migst.cl  
ORCID: 0009-0004-4615-6825  
GitHub: [@enriqueherbertag-lgtm](https://github.com/enriqueherbertag-lgtm)
