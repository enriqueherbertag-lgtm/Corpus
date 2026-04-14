## Mejora 5: Sensores de posición para articulaciones (rueda fónica + Hall)

**Fecha:** 14 de abril de 2026
**Estado:** Especificación conceptual. Sin implementación.

### Componentes seleccionados

**Sensor inductivo de alta velocidad (para articulaciones principales): AS5715R de ams AG**

- **Número de producto:** AS5715R-ZTST (TSSOP-14) o AS5715R-ZTSM (SOIC-8)
- **Código de pedido:** 507920024 / 507920025
- **Certificación:** AEC-Q100 Grade 0 (automotive, -40°C a 160°C) [citation:1]
- **Seguridad funcional:** ISO 26262 ASIL C(D) como Safety Element out of Context (SEooC) [citation:1][citation:3][citation:7]
- **Compatibilidad RoHS y HF** [citation:1]
- **Precisión típica:** <0.075 grados mecánicos con configuración de 4 pares de polos [citation:1][citation:7]
- **Rango de temperatura:** -40°C a 160°C
- **Tecnología:** Inductiva (sin contacto, inmune a campos magnéticos externos)
- **Salida:** SIN/COS diferencial (para cálculo atan2) [citation:1][citation:7]
- **Aplicación:** On/off axis, adaptable a diseño de bobinas personalizado [citation:1][citation:7]
- **Seguridad:** Diagnósticos integrados, watchdog, detección de subtensión/sobretensión, detección de circuito abierto en bobinas [citation:9]

**Sensor GMR de alta precisión (versión compacta para dedos): TLE5012B E5000 de Infineon**

- **Número de producto:** TLE5012B E5000
- **Caso:** PG-DSO-8 (5x6 mm)
- **Certificación:** Safety Integrity Level (SIL) según IEC61508 y ISO 26262 [citation:2]
- **Características de seguridad:** PRO-SIL™ (Infineon), test vectors, CRC para comunicación, BIST (Built-in Self-test) [citation:2]
- **Interfaces:** SSC (tres hilos), PWM, Incremental Interface, Hall Switch Mode, Short PWM Code [citation:2]
- **Comunicación:** Bidireccional, 8-bit CRC para SSC, 4-bit CRC para SPC [citation:2]
- **Tecnología:** GMR (Giant Magneto-Resistive)
- **Resolución:** 0.01 grados
- **NOTA:** El TLE5012B E1000 tiene funcionalidad de seguridad ISO 26262, pero NO está declarado ASIL Ready por Infineon [citation:5][citation:8]. Se debe evaluar en sistema para determinar el nivel ASIL alcanzable.

**Alternativa AMR de alta precisión (para dedos, más precisa que Hall): KMZ80 de NXP**

- **Número de producto:** KMZ80
- **Caso:** SOIC-8 (5x6 mm)
- **Certificación:** AEC-Q100, ISO 26262 [citation:10]
- **Nivel ASIL:** Hasta ASIL B (salida analógica) o ASIL C (salida SENT) [citation:10]
- **Tecnología:** AMR (Anisotropic Magneto-Resistive)
- **Salidas:** SAE J2716 SENT y analógica
- **Calibración:** Multpunto (17 puntos equidistantes o 7 seleccionables), almacenamiento en NVM [citation:10]
- **Memoria:** 8×12 bits para trazabilidad del cliente [citation:10]
- **Robustez:** Campo magnético de trabajo >25 kA/m, sin límite superior [citation:10]
- **Estado:** Producto no recomendado para nuevos diseños (NRND) [citation:10]. Para CORPUS (concepto, no producción), es válido. Para producción, seleccionar alternativa actual.

### Rueda fónica

**Descripción:** Disco metálico estampado con dientes (ej. 60-2 para 6° de resolución, o 36-1 para 10°). Se mecaniza en el propio rotor de la articulación o se añade como un disco independiente de 2-3 mm de espesor.

**Material:** Acero magnético (para sensores Hall) o acero inoxidable (para sensores inductivos AMS AS5715R, que no requieren dientes magnéticos, solo conductores). Para el AS5715R, la rueda fónica puede ser de aluminio o cobre (el sensor es inductivo, detecta metales conductores, no imanes) [citation:1].

**Diseño del sistema de bobinas para AS5715R:** El AS5715R requiere un sistema de bobinas personalizado (TX y dos RX) integrado en un PCB. El objetivo (target) puede ser una rueda fónica conductora (aluminio, cobre) o un estampado metálico. La ventaja de este sensor es que NO necesita imanes, solo un objetivo conductor [citation:1][citation:7].

### Distribución por articulación

**Articulaciones principales (hombro, codo, cadera, rodilla):**
- **Sensor inductivo AS5715R** + sistema de bobinas PCB + rueda fónica conductora
- Proporciona velocidad y posición absoluta (no incremental, el AS5715R es absoluto)
- Resolución <0.075 grados
- Sin contacto, sin desgaste
- Seguridad ISO 26262 ASIL C(D) como SEooC

**Articulaciones secundarias (muñeca, tobillo, cuello):**
- **Sensor GMR TLE5012B** + imán dipolo (2x2 mm)
- Rango ±180°
- Tamaño reducido (5x6 mm)
- Funcionalidad de seguridad ISO 26262 (sin ASIL declarado)
- O **Sensor AMR KMZ80** (hasta ASIL C, NRND)

**Articulaciones de dedos (ultraminiatura):**
- **Sensor GMR TLE5012B** en encapsulado TDSO-8 o **KMZ80** en SOIC-8
- Imán dipolo de 2x2x1 mm (neodimio N52)
- Montaje en PCB flexible de 0.2 mm
- Cableado con hilo de cobre esmaltado de 0.1 mm
- Tamaño total <5x5x2 mm por articulación
- Resolución de 0.01 grados (TLE5012B)

### Integración en CORPUS

Cada articulación tendrá su propio subsistema de sensado. Los datos se procesan localmente (STM32 en cada nodo de extremidad) y se transmiten por fibra óptica (con módulos BiDi) al núcleo principal.

**Conexión del AS5715R:**
- El chip se monta en un pequeño PCB rígido (10x10 mm) en la parte fija de la articulación.
- El sistema de bobinas (TX y dos RX) se integra en el mismo PCB.
- La rueda fónica conductora se fija al rotor (pasador) de la articulación, enfrentada a las bobinas a 0.5-1 mm.
- El chip se alimenta a 5V (o 3.3V) y proporciona salida SIN/COS diferencial.
- Un microcontrolador local (STM32F405) aplica la función atan2 para calcular el ángulo absoluto.

**Conexión del TLE5012B / KMZ80:**
- Se monta en un PCB flexible o rígido-pequeño.
- El imán se fija en el extremo del eje.
- La comunicación es por SPI (o SENT para KMZ80).
- La alimentación es de 3.3V o 5V.

### Estado

- [x] Componentes identificados con códigos de producto.
- [x] Certificaciones ISO 26262 verificadas.
- [x] Distribución por articulación definida.
- [ ] Prototipo de una articulación con AS5715R y bobinas PCB (pendiente).
- [ ] Prototipo de un dedo con TLE5012B y PCB flexible (pendiente).
- [ ] Pruebas de precisión y repetibilidad.
- [ ] Pruebas de temperatura y vibración.

### Referencias

- AS5715R Datasheet (ams AG): AEC-Q100 Grade 0, ISO 26262 ASIL C(D) SEooC [citation:1][citation:3][citation:7]
- AS5715R Safety Manual (disponible bajo solicitud) [citation:3]
- TLE5012B User Manual: ISO 26262 SIL, PRO-SIL™, BIST, CRC [citation:2]
- TLE5012B Functional Safety: ISO 26262 compliant, no ASIL declared [citation:5][citation:8]
- KMZ80 Datasheet: AEC-Q100, ISO 26262 ASIL B/C, AMR technology [citation:10]
- MagnTek MT6620: Alternativa de off-axis con ASIL B(D) [citation:4]
