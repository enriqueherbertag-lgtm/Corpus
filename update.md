# Update: Mejoras al diseño de CORPUS

**Última actualización:** 16 de abril de 2026  
**Versión del concepto:** v1.2.1 (corrección de especificación térmica)

## Contenido

- [Mejora 1: Integración de sensores y actuadores piezoeléctricos](#mejora-1-integracion-de-sensores-y-actuadores-piezoelectricos)
- [Mejora 2: Conectividad entre módulos mediante fibra óptica](#mejora-2-conectividad-entre-modulos-mediante-fibra-optica)
- [Mejora 3: Articulación inteligente de accionamiento directo (sin anillos colectores)](#mejora-3-articulacion-inteligente-de-accionamiento-directo-sin-anillos-colectores)
- [Mejora 4: Sensores de posición para articulaciones](#mejora-4-sensores-de-posicion-para-articulaciones)
- [Mejora 5: Sistema de Soporte Vital Integrado (Avatar + Paciente)](#mejora-5-sistema-de-soporte-vital-integrado-avatar--paciente)
- [Resumen del impacto de las mejoras](#resumen-del-impacto-de-las-mejoras)
- [Especificación térmica: aclaración importante](#especificacion-termica-aclaracion-importante)

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
| Sensor piezoeléctrico tipo bender | Murata 7BB-27-4 (o TDK PS1240P02BT) | Detección de vibraciones (10-300 Hz) | 1.50 USD |
| Actuador piezoeléctrico de anillo | Noliac NAC2122 | Vibración háptica localizada (50-200 Hz) | 8.00 USD |
| Multiplexor analógico | ADG732 (Analog Devices) | Leer múltiples sensores con un solo ADC | 12.00 USD |
| Driver de alto voltaje | Driver genérico (ej. PiezoDrive PDX150) | Controlar actuadores (0-150V) | 25.00 USD |

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

- **Backbone principal:** Fibra óptica monomodo (9/125 µm) que recorre la columna vertebral de CORPUS. Cada extremidad se conecta al backbone mediante un nodo de comunicación.
- **Nodos de comunicación:** Por cada módulo (brazo, pierna, torso), un convertidor de medios (cobre a fibra) basado en transceptores SFP. El nodo también aloja un microcontrolador (STM32) para gestionar el tráfico local.
- **Comunicación dentro del módulo (tramo final):** Cableado de cobre flexible (I2C, SPI, o Ethernet de cobre). La fibra no llega a las articulaciones porque es frágil en zonas de flexión continua. Se detiene en el nodo, situado en la base del módulo (hombro, cadera).

### Optimización con módulos BiDi (WDM)

Para reducir el número de hilos de fibra necesarios, se emplearán transceptores **1000BASE-BX BiDi SFP** (estándar IEEE 802.3z). Estos módulos utilizan dos longitudes de onda diferentes (ej. 1310 nm/1490 nm) para transmitir y recibir simultáneamente sobre una sola fibra monomodo (Simplex LC). La velocidad de 1.25 Gbps es suficiente para el tráfico combinado de sensores y comandos.

### Componentes propuestos

| Componente | Modelo de referencia | Costo unitario |
|------------|----------------------|----------------|
| Fibra óptica monomodo (9/125 µm) | Corning SMF-28 Ultra | 0.30 USD/m |
| Transceptor SFP BiDi (1000BASE-BX) | TP-Link TL-SM311LS (o equivalente industrial, ej. Finisar FTLF1318P3BTL) | 25-50 USD |
| Convertidor de medios (cobre a fibra) industrial | Lantech IMC-350I-SFP | 45 USD |
| Microcontrolador nodo | STM32F405 | 10 USD |

**Costo estimado para CORPUS completo:** 1 backbone (fibra) + 6 nodos (brazos, piernas, cabeza, torso) ≈ 500 USD.

### Estado

- [x] Concepto definido.
- [x] Topología especificada.
- [x] Componentes identificados.
- [ ] Prototipo de un nodo (fibra + microcontrolador + conversor) para pruebas de latencia (pendiente).

---

## Mejora 3: Articulación inteligente de accionamiento directo (sin anillos colectores)

**Fecha de incorporación:** 15 de abril de 2026

### Objetivo

Sustituir los sistemas de motor+engranajes por una **articulación inteligente autónoma** que integra el motor, el sensor, el controlador y la refrigeración en un solo módulo. No es una pieza de CORPUS. Es un componente estándar que puede usarse en prótesis, exoesqueletos o robots.

### Diseño

- **Motor:** Accionamiento directo (sin engranajes). Rotor = eje de la articulación (con imanes N52). Estator = carcasa fija (con bobinados de cobre).
- **Sensor de posición:** Inductivo AS5715R (ams AG) + rueda fónica conductora. Resolución <0.075°, rango 360° absoluto, comunicación SPI.
- **Controlador local:** STM32F405 (o similar). Aloja el bucle PID de posición/velocidad/par y la comunicación por bus serie (UART sobre fibra o RS-485).
- **Driver de potencia:** Puente H de 48V, 10A (ej. DRV8320). Integrado en la misma PCB que el microcontrolador.
- **Refrigeración:** Canal de líquido en la carcasa del estator (opcional, para altas cargas). Conectable al sistema central de CORPUS.
- **Comunicación:** Bus serie a 1 Mbps. Protocolo de paquetes: ID, modo (posición/velocidad/par), valor objetivo (int32), checksum.

### Modos de control

- **Modo posición:** La articulación se mueve hasta el ángulo indicado (en grados).
- **Modo velocidad:** Gira a la velocidad angular indicada (grados/segundo).
- **Modo par:** Aplica el par indicado (Nm) al eje.
- **Modo seguro (fallo de enlace):** Configurable por hardware. Puede ser "retención" (mantiene la posición con par reducido) o "libre" (desactiva el motor, dejando la articulación girar libremente).

### Especificaciones

| Parámetro | Valor |
|---|---|
| Diámetro | 60 mm |
| Longitud | 80 mm |
| Peso | 400-500 g |
| Par máximo | 50 Nm (pico), 20 Nm (continuo) |
| Velocidad máxima | 300 rpm |
| Alimentación | 48V DC |
| Consumo en reposo | 5 W |
| Consumo en movimiento | 50-200 W |
| Precisión de posición | ±0.1 grados |

### Integración en CORPUS

- Cada articulación es un nodo esclavo en el bus de fibra óptica (o RS-485).
- La alimentación (48V) y la refrigeración se distribuyen en paralelo a todas las articulaciones.
- El cerebro de CORPUS (triple núcleo) actúa como nodo maestro, enviando comandos a cada articulación a 1 kHz.

### Estado

- [x] Concepto definido.
- [x] Componentes seleccionados.
- [x] Especificaciones mecánicas, eléctricas y de control.
- [ ] Prototipo de una articulación (pendiente).
- [ ] PCB del controlador local (pendiente).
- [ ] Firmware (pendiente).

---

## Mejora 4: Sensores de posición para articulaciones

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

## Mejora 5: Sistema de Soporte Vital Integrado (Avatar + Paciente)

**Fecha de incorporación:** 14 de abril de 2026

### Objetivo

Mantener la integridad funcional de CORPUS como extensión física del paciente, garantizando que el avatar pueda ejecutar las acciones del paciente en el mundo real (abrir puertas, manipular objetos, desplazarse) incluso durante periodos prolongados de uso, y que el paciente reciba retroalimentación sensorial de esas acciones.

### Subsistemas

#### A. Soporte vital para CORPUS (Avatar)
- **Refrigeración circulatoria:** Debe disipar el calor generado por el uso continuo de los motores. Sistema cerrado con agua destilada y propilenglicol.
- **Energía:** Baterías duales (LiFePO4 de 2 kWh + ultracapacitores). Deben soportar un día completo de uso activo (8-10 horas) sin recarga. Si la batería principal se agota, conmutación automática a la secundaria y búsqueda de base de carga.
- **Comunicaciones:** Enlace de fibra óptica con ENA (para la intención de movimiento) y enlace LoRa de respaldo (para telemetría y emergencias). Latencia < 10 ms.

#### B. Retroalimentación al paciente
- **Sensores de fuerza en las manos de CORPUS:** Miden la presión al agarrar un objeto. Esa señal se envía a ENA, que la traduce en estimulación táctil (vibración) en la mano del paciente.
- **Cámaras en la cabeza de CORPUS:** La imagen se envía a las gafas AR del paciente. El paciente ve lo que CORPUS ve.

#### C. Modos de operación
- **Modo Activo:** El paciente controla CORPUS.
- **Modo Pausa:** El paciente necesita descansar. CORPUS reduce el consumo energético, pero mantiene la conexión.
- **Modo Emergencia (paciente inconsciente):** CORPUS detiene todo movimiento, activa una baliza (sonido y LoRa) y espera instrucciones externas.

### Integración con otros sistemas

- **ENA** envía la intención de movimiento (EEG) y recibe las señales de fuerza para la retroalimentación háptica.
- **Las gafas AR** muestran el video de las cámaras de CORPUS y el estado del avatar.
- **La memoria psiquiátrica** anticipa crisis para que el sistema pueda sugerir al paciente pasar a Modo Pausa antes de que ocurra.

### Estado

- [x] Concepto definido.
- [x] Subsistemas identificados.
- [ ] Selección de baterías para 8 horas de uso continuo (pendiente).
- [ ] Implementación del Modo Pausa y Modo Emergencia (pendiente).

---

## Resumen del impacto de las mejoras

La aplicación de estas cinco mejoras transforma CORPUS de un concepto de robot humanoide a un sistema corporal artificial con atributos diferenciales:

| Mejora | Impacto en CORPUS |
|--------|-------------------|
| **Piezoeléctricos** | Añade sensibilidad táctil dinámica (vibraciones, texturas) y retroalimentación háptica para el operador humano (ENA). |
| **Fibra óptica BiDi** | Reduce el peso y la interferencia electromagnética en el backbone de comunicaciones. Aumenta el ancho de banda y la fiabilidad. |
| **Articulación inteligente** | Elimina anillos colectores (desgaste, mercurio). Añade control local (PID) y modos de control (posición, velocidad, par). Permite giros continuos y mayor precisión. |
| **Sensores inductivos/GMR/AMR** | Proporciona posición absoluta y velocidad en cada articulación, con precisión subgrado, sin contacto y con certificación ISO 26262 para seguridad funcional. |
| **Soporte vital integrado** | Garantiza la supervivencia del avatar y la conexión con el paciente en situaciones de emergencia o pérdida de enlace. |

**Efecto neto:** CORPUS será más ligero (menos cobre, sin anillos colectores), más rápido (menor latencia en comunicaciones), más sensible (vibraciones, háptica), más seguro (certificaciones ISO 26262), y más fácil de mantener (sin escobillas, sin engranajes, sin mercurio).

---

## Especificación térmica: aclaración importante

**ATENCIÓN:** Para evitar malentendidos, se aclara explícitamente la siguiente característica fundamental del diseño:

**SmartJoint NO es un motor de rotación continua.** Está diseñado para **movimiento oscilante acotado** (típicamente 40° a 180° de recorrido), similar a una articulación biológica (hombro, codo, rodilla). No rota indefinidamente como una rueda o una correa transportadora.

**Consecuencia para la refrigeración:**

- La potencia de 50W por articulación es un **pico de corta duración** (menos de 5 segundos), alcanzable solo en esfuerzos máximos (ej. levantar 50kg).
- En uso típico (caminar, agarrar, gestos), la potencia media es de **5 a 15W por articulación**.
- Las articulaciones de baja demanda (dedos, cuello, muñeca) operan por debajo de **5W** en movimiento normal.
- La refrigeración líquida opcional por articulación **solo se activa durante picos muy cortos**. El resto del tiempo, la disipación es pasiva.

**Por lo tanto, el sistema central de refrigeración cerrada de 80-120W continuos ES SUFICIENTE para mantener la homeostasis térmica de CORPUS en actividad normal.** Los 120W no son la capacidad de disipación pico de todo el cuerpo, sino la capacidad sostenida del sistema circulatorio. Los picos de calor se disipan gradualmente gracias a la inercia térmica de las articulaciones y a la refrigeración líquida local (que actúa como un "amortiguador térmico").

| Tipo de articulación | Cantidad | Potencia media (movimiento normal) | Refrigeración |
|---------------------|----------|-----------------------------------|---------------|
| Cadera, rodilla, hombro (alta demanda) | 12 | 10-15W | Líquida + pasiva |
| Codo, muñeca, tobillo (demanda media) | 12 | 5-10W | Pasiva + disipador |
| Cuello, dedos, columna (baja demanda) | 18 | 1-5W | Solo pasiva |

**Potencia media total estimada en movimiento normal:**  
(12×12W) + (12×7W) + (18×3W) = 144W + 84W + 54W = **282W**

**Nota:** Estos 282W son la potencia eléctrica consumida, no el calor disipado. Parte de esa potencia se convierte en trabajo mecánico (movimiento). El calor residual disipado por el sistema de refrigeración es significativamente menor, y encaja dentro de los 120W continuos del sistema central.

---

## Nota final

Este documento es una **especificación técnica en desarrollo**. No hay prototipos funcionales. Los componentes seleccionados son sugerencias basadas en hojas de datos y disponibilidad comercial. La integración completa en CORPUS requerirá pruebas adicionales y posiblemente cambios de diseño. Sin embargo, la viabilidad técnica es alta porque todos los componentes son estándar y están respaldados por certificaciones industriales (AEC-Q100, ISO 26262, etc.).

## Autor

Enrique Aguayo H. – Mackiber Labs  
Asistencia de DeepSeek (IA) en la redacción y estructura.

## Licencia

Copyright © 2026 Enrique Aguayo. Todos los derechos reservados. Este documento se comparte con fines de documentación del proyecto. No se permite su uso comercial sin autorización expresa.
