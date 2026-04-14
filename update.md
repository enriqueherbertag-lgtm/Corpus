# Update: Mejoras al diseño de CORPUS

**Última actualización:** 14 de abril de 2026  
**Versión del concepto:** v1.2.0 (mejoras documentadas, no implementadas)

Este documento recoge las mejoras y especificaciones técnicas añadidas al diseño original de CORPUS. No es un manual de construcción. Es una declaración de intenciones y una guía para futuros desarrollos.

---

## Mejora 1: Integración de sensores y actuadores piezoeléctricos

**Fecha de incorporación:** 14 de abril de 2026

### Resumen

Se ha añadido al diseño de CORPUS una capa de sensado y actuación mediante piezoeléctricos. No es una piel sensible de alta resolución. Es un complemento de bajo costo (estimado 50 USD por mano) que permite:

- Detectar vibraciones mecánicas (golpes, zumbidos, texturas gruesas).
- Generar retroalimentación háptica básica (vibraciones de 50-200 Hz) para el operador humano a través de ENA.
- Proveer micro-vibraciones de referencia para mejorar la estabilidad de las articulaciones.

### Componentes propuestos

| Componente | Modelo de referencia | Función | Costo unitario |
|------------|----------------------|---------|----------------|
| Sensor piezoeléctrico tipo bender | Murata 7BB-20-6 | Detección de vibraciones (10-300 Hz) | 1.50 USD |
| Actuador piezoeléctrico de anillo | Noliac NAC2122 | Vibración háptica localizada (50-200 Hz) | 8.00 USD |
| Multiplexor analógico | ADG732 (Analog Devices) | Leer múltiples sensores con un solo ADC | 12.00 USD |
| Driver de alto voltaje | MPIA (PiezoDrive) | Controlar actuadores (0-150V) | 25.00 USD |

**Total estimado para una mano:** 4 actuadores + 8 sensores + multiplexor + driver ≈ 50 USD.

### Integración

- Los piezoeléctricos se colocan en las yemas de los dedos (sensores y actuadores) y en la palma (solo actuadores).
- Se conectan a un multiplexor analógico (para los sensores) y a un driver de alto voltaje (para los actuadores).
- El microcontrolador principal leerá los sensores a 1 kHz y generará señales PWM para los actuadores.

### Estado

- [x] Concepto definido.
- [x] Componentes identificados.
- [x] Costo estimado.
- [ ] Prototipo de un dedo con sensores y actuadores (pendiente).

---

## Mejora 2: Conectividad entre módulos mediante fibra óptica

**Fecha de incorporación:** 14 de abril de 2026

### Motivación

CORPUS es un sistema distribuido. El cableado de cobre tradicional presenta problemas de interferencias, peso y ancho de banda. La fibra óptica es inmune a EMI, pesa menos y tiene ancho de banda ilimitado para las necesidades actuales.

### Topología propuesta

- **Backbone principal:** Fibra óptica multimodo (50/125 µm) que recorre la columna vertebral de CORPUS. Cada extremidad se conecta al backbone mediante un nodo de comunicación.
- **Nodos de comunicación:** Por cada módulo (brazo, pierna, torso), un convertidor de medios (cobre a fibra) basado en transceptores SFP (costo por nodo ≈ 15-20 USD). El nodo también aloja un microcontrolador (STM32) para gestionar el tráfico local.
- **Comunicación dentro del módulo (tramo final):** Cableado de cobre flexible (I2C, SPI, o Ethernet de cobre). La fibra no llega a las articulaciones porque es frágil en zonas de flexión continua. Se detiene en el nodo, situado en la base del módulo (hombro, cadera).

### Optimización con módulos BiDi (WDM)

Para reducir el número de hilos de fibra necesarios, se emplearán transceptores **1000BASE-BX BiDi SFP** (estándar IEEE 802.3z). Estos módulos utilizan dos longitudes de onda diferentes (ej. 1310 nm/1490 nm) para transmitir y recibir simultáneamente sobre una sola fibra monomodo (Simplex LC). La velocidad de 1.25 Gbps es suficiente para el tráfico combinado de sensores y comandos.

### Componentes propuestos

| Componente | Modelo de referencia | Costo unitario |
|------------|----------------------|----------------|
| Fibra óptica monomodo (9/125 µm) | Corning SMF-28 Ultra | 0.30 USD/m |
| Transceptor SFP BiDi (1000BASE-BX) | TP-Link TL-SM311LS | 25 USD |
| Convertidor de medios (cobre a fibra) industrial | Lantech IMC-350I-SFP | 45 USD |
| Microcontrolador nodo | STM32F405 | 10 USD |

**Costo estimado para CORPUS completo:** 1 backbone + 6 nodos ≈ 500 USD.

### Estado

- [x] Concepto definido.
- [x] Topología especificada.
- [x] Componentes identificados.
- [ ] Prototipo de un nodo (fibra + microcontrolador + conversor) para pruebas de latencia (pendiente).

---

## Mejora 3: Transmisión de energía y datos en articulaciones (sin contacto)

**Fecha de incorporación:** 14 de abril de 2026

### Alternativa a los anillos colectores (arcaicos, con mercurio)

CORPUS no utilizará anillos colectores tradicionales. Se opta por tecnologías modernas sin contacto, sin desgaste, y sin materiales tóxicos.

**Para articulaciones con giro limitado (< 360°): codo, muñeca, rodilla, cuello**

- **Cable flexible de alta resistencia a la torsión:** Serie Chainflex CFROBOT (Igus). Soportan ±180° de torsión por metro, radios de curvatura de 10x diámetro, y más de 10 millones de ciclos de flexión.

**Para articulaciones con giro continuo (≥ 360°): hombro, cadera**

- **Energía:** Transmisión inductiva rotativa (acoplamiento magnético). Bobinas primarias y secundarias enfrentadas, con núcleos segmentados. Eficiencia > 90% a 1-2 mm de distancia. Proveedor comercial: Würth Elektronik (serie WE-ACPR) o sistemas integrados por Wiferion.
- **Datos:** Comunicación óptica rotativa (infrarrojos). LEDs modulados (IR) y fotodetectores enfrentados. Ancho de banda típico: 100 Mbps. Proveedor comercial: Bytelight.

### Estado

- [x] Concepto definido.
- [x] Tecnologías identificadas.
- [ ] Prototipo de transmisión inductiva para un brazo (pendiente).
- [ ] Prototipo de comunicación óptica rotativa (pendiente).

---

## Mejora 4: Articulaciones como motores de accionamiento directo

**Fecha de incorporación:** 14 de abril de 2026

### Diseño

- **Rotor:** El propio pasador (eje) de la articulación. Fabricado en acero magnético (o con imanes de neodimio insertados). Diámetro grande (50-80 mm) para maximizar el par.
- **Estator:** La carcasa fija de la extremidad. Aloja los bobinados de cobre y los núcleos de acero al silicio. Envuelve al rotor con un entrehierro de 0.3-0.5 mm.
- **Refrigeración:** El líquido refrigerante (agua destilada + propilenglicol) circula por canales en la carcasa del estator, extrayendo el calor generado.

### Ventajas

- **Sin backlash:** Al no haber engranajes, no hay holgura ni pérdida de precisión.
- **Silencioso:** Eliminación de engranajes y correas.
- **Compacto:** El motor ocupa el espacio de la articulación.
- **Mantenimiento reducido:** Sin engranajes que lubricar ni correas que tensar.

### Desafíos y soluciones

- **Par a baja velocidad:** Se usan motores de par (torque motors) con muchos pares de polos y rotores de gran diámetro. El par puede superar los 50 Nm.
- **Peso:** Al eliminar engranajes, correas y soportes, el peso total puede ser similar o incluso menor.
- **Calor:** La refrigeración circulatoria de CORPUS (80-120 W) es suficiente.

### Estado

- [x] Concepto definido.
- [ ] Selección de materiales magnéticos (pendiente).
- [ ] Diseño electromagnético (pendiente).
- [ ] Prototipo de articulación con motor de accionamiento directo (pendiente).

---

## Mejora 5: Sensores de posición para articulaciones

**Fecha de incorporación:** 14 de abril de 2026

### Componentes seleccionados

**Sensor inductivo de alta velocidad (para articulaciones principales): AS5715R de ams AG**

- **Número de producto:** AS5715R-ZTST (TSSOP-14) o AS5715R-ZTSM (SOIC-8)
- **Código de pedido:** 507920024 / 507920025
- **Certificación:** AEC-Q100 Grade 0, ISO 26262 ASIL C(D) como SEooC
- **Precisión:** <0.075 grados mecánicos
- **Tecnología:** Inductiva (sin contacto, inmune a campos magnéticos externos)
- **Rango de temperatura:** -40°C a 160°C

**Sensor GMR de alta precisión (versión compacta para dedos): TLE5012B E5000 de Infineon**

- **Número de producto:** TLE5012B E5000
- **Caso:** PG-DSO-8 (5x6 mm)
- **Certificación:** ISO 26262 (SIL), PRO-SIL™, BIST, CRC
- **Resolución:** 0.01 grados
- **Tecnología:** GMR (Giant Magneto-Resistive)

**Alternativa AMR (para dedos, más precisa que Hall): KMZ80 de NXP**

- **Número de producto:** KMZ80
- **Caso:** SOIC-8 (5x6 mm)
- **Certificación:** AEC-Q100, ISO 26262 ASIL B/C
- **Tecnología:** AMR (Anisotropic Magneto-Resistive)
- **Estado:** NRND (no recomendado para nuevos diseños), válido para prototipo.

### Rueda fónica

Disco metálico estampado con dientes (ej. 60-2 para 6° de resolución). Se mecaniza en el propio rotor de la articulación o se añade como un disco independiente de 2-3 mm de espesor. Para el AS5715R, la rueda fónica puede ser de aluminio o cobre (el sensor es inductivo, detecta metales conductores).

### Distribución por articulación

| Tipo de articulación | Sensores | Rango de giro | Notas |
|----------------------|----------|---------------|-------|
| Hombro, cadera | AS5715R + rueda fónica (inductivo) | ±180° o continuo | Para giro continuo, añadir transmisión inductiva+óptica. |
| Codo, rodilla | AS5715R + rueda fónica | 0-150° | Rango típico humano. |
| Muñeca, tobillo | TLE5012B o KMZ80 + imán | ±90° | Compacto, sin rueda fónica. |
| Dedos, cuello | TLE5012B o KMZ80 + imán dipolo 2x2 mm | 0-90° | Mínimo espacio, PCB flexible. |

### Integración en CORPUS

- **Articulaciones principales:** El AS5715R se monta en un PCB rígido (10x10 mm) en la parte fija. El sistema de bobinas (TX y dos RX) se integra en el mismo PCB. La rueda fónica conductora se fija al rotor. El chip proporciona salida SIN/COS diferencial; un microcontrolador local aplica la función atan2 para calcular el ángulo absoluto.
- **Articulaciones de dedos:** El TLE5012B o KMZ80 se monta en PCB flexible (0.2 mm). El imán dipolo se fija en el extremo del eje. Comunicación SPI o SENT. Cableado con hilo de cobre esmaltado de 0.1 mm.

### Estado

- [x] Componentes identificados con códigos de producto.
- [x] Certificaciones ISO 26262 verificadas.
- [x] Distribución por articulación definida.
- [ ] Prototipo de articulación con AS5715R y bobinas PCB (pendiente).
- [ ] Prototipo de dedo con TLE5012B y PCB flexible (pendiente).

---

## Nota final

Este documento es una **especificación técnica en desarrollo**. No hay prototipos funcionales. Los componentes seleccionados son sugerencias basadas en hojas de datos y disponibilidad comercial. La integración completa en CORPUS requerirá pruebas adicionales y posiblemente cambios de diseño. Sin embargo, la viabilidad técnica es alta porque todos los componentes son estándar y están respaldados por certificaciones industriales (AEC-Q100, ISO 26262, etc.).

## Autor

Enrique Aguayo H. – Mackiber Labs  
Asistencia de DeepSeek (IA) en la redacción y estructura.

## Licencia

Copyright © 2026 Enrique Aguayo. Todos los derechos reservados. Este documento se comparte con fines de documentación del proyecto. No se permite su uso comercial sin autorización expresa.
