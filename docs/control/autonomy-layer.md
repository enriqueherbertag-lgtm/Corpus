# Capa de Autonomía de CORPUS (Sistema de Control de Bajo Nivel)

**También denominado:** "Inconsciente" o "Sistema de Reflejos y Homeostasis".  
**Versión del documento:** 1.1.0  
**Última actualización:** 16 de abril de 2026  
**Autor:** Enrique Aguayo H. (Mackiber Labs)  
**Asistencia técnica:** DeepSeek (IA)

---

## 1. Objetivo

Definir la arquitectura de control autónomo de bajo nivel de CORPUS. Esta capa es responsable de:

- **Reflejos:** Respuestas inmediatas a estímulos externos (ej. retirar la mano de una superficie caliente, protegerse al caer).
- **Propiocepción:** Conocimiento continuo de la posición y estado de cada articulación.
- **Homeostasis:** Mantenimiento de las condiciones internas (temperatura, energía, comunicación).
- **Fallback:** Acciones de emergencia cuando se pierde la conexión con el cerebro principal (IA externa o consciencia del paciente).

**Principio fundamental:** Esta capa opera de forma independiente al cerebro principal. No requiere IA. No requiere conexión a internet. Solo requiere sus sensores, sus actuadores y su lógica programada.

---

## 2. Arquitectura de hardware

### 2.1 Unidad de Control Central (Cerebro del Inconsciente)

| Componente | Modelo de referencia | Función |
|------------|----------------------|---------|
| Microcontrolador principal | STM32F746 (o similar) | Ejecuta la lógica de alto nivel de la capa de autonomía (fallback, homeostasis). |
| Microcontroladores secundarios (por módulo) | STM32F405 | Control local de articulaciones (PID, lectura de sensores). |
| Unidad de medición inercial (IMU) | MPU-6050 (o ICM-20948) | Detección de orientación, aceleración lineal, velocidad angular. Base del equilibrio y reflejos de caída. |
| Sensores de temperatura | DS18B20 (1-Wire) | Monitoreo de temperatura en motor, baterías, y ambiente exterior. |
| Gestión de batería | BQ76952 (Texas Instruments) | Monitoreo de voltaje, corriente y temperatura de celdas. |

### 2.2 Comunicación interna

| Bus | Función | Velocidad |
|-----|---------|-----------|
| CAN bus (o RS-485) | Comunicación entre microcontrolador principal y secundarios. | 1 Mbps |
| I2C / SPI | Lectura de sensores (IMU, temperatura, batería). | 400 kHz / 10 MHz |
| GPIO (discreto) | Señales de emergencia (ej. "caída detectada", "batería crítica"). | Inmediato (interrupción). |

### 2.3 Refrigeración y energía (aclaración térmica)

**CARACTERÍSTICA CLAVE DEL DISEÑO:** Las articulaciones SmartJoint operan en **movimiento oscilante acotado** (típicamente 40°-180°), no en rotación continua. Por lo tanto, los picos de potencia (50W por articulación) son de muy corta duración (<5 segundos). En movimiento normal, la potencia media es de 5-15W por articulación.

- **Control de temperatura:** El microcontrolador lee los sensores de temperatura. Si una articulación supera los **70°C**, activa la bomba de refrigeración líquida (solo en las articulaciones que tengan este sistema opcional). Si supera los **85°C**, reduce la potencia de los motores (modo seguro). Si supera los **100°C** (fallo crítico), apaga la articulación.
- **Sistema central de refrigeración:** Capacidad sostenida de **80-120W continuos**. Suficiente para la disipación térmica media de todo CORPUS en actividad normal, gracias al movimiento oscilante y a la inercia térmica de las articulaciones.
- **Gestión de energía:** Si la batería principal cae por debajo del 15%, el sistema conmuta a la batería secundaria y activa una baliza de "batería baja". Si la batería secundaria también cae, entra en modo de ahorro extremo (solo sensores de emergencia y baliza LoRa).

---

## 3. Reflejos (Respuestas Inmediatas)

Los reflejos se ejecutan en el microcontrolador local de cada articulación o en el microcontrolador central, con prioridad máxima (interrupción).

| Reflejo | Sensor | Acción | Tiempo máximo de respuesta |
|---------|--------|--------|----------------------------|
| **Protección de caída** | IMU (acelerómetro, giroscopio) | Detección de aceleración anómala (caída). Se activa el protocolo de relajación de articulaciones y se busca amortiguar el impacto. | < 50 ms |
| **Retirada por calor** | Sensor de temperatura en extremidad | Si temperatura superficial externa > 55°C, se ordena a la articulación retirarse del objeto. | < 100 ms |
| **Protección por sobrecorriente** | Driver de motor (medición de corriente) | Si corriente > 15A (pico), se reduce el par del motor. Si persiste, se desactiva. | < 10 ms |
| **Reflejo de equilibrio** | IMU (ángulo respecto al suelo) | Si el ángulo de inclinación supera el umbral (ej. 15°), se activan los actuadores de corrección en piernas y torso. | < 50 ms |

---

## 4. Propiocepción (Sentido de la Posición)

| Articulación | Sensor de posición | Resolución | Frecuencia de actualización |
|--------------|--------------------|------------|-----------------------------|
| Hombro, cadera | AS5715R (inductivo) + rueda fónica | <0.075° | 1 kHz |
| Codo, rodilla | AS5715R + rueda fónica | <0.075° | 1 kHz |
| Muñeca, tobillo | TLE5012B (GMR) | 0.01° | 500 Hz |
| Dedos | KMZ80 (AMR) | 0.1° (estimado) | 500 Hz |

Los datos de posición se leen continuamente y se almacenan en un buffer circular (últimos 100 valores). El microcontrolador central usa estos datos para:

- **Detectar movimientos involuntarios** (ej. temblor, vibración externa).
- **Suavizar la trayectoria** (filtro de Kalman o media móvil).
- **Detectar fallos mecánicos** (ej. una articulación que no responde a la orden).

---

## 5. Homeostasis (Mantenimiento del Estado Interno)

| Función | Sensor | Acción autónoma |
|---------|--------|-----------------|
| **Temperatura** | DS18B20 (cada módulo) | Si T > 70°C: activar bomba de refrigeración local (opcional). Si T > 85°C: reducir potencia motores. Si T > 100°C: apagar articulación (emergencia). |
| **Energía** | BQ76952 (monitor de batería) | Si batería principal < 15%: conmutar a secundaria, activar baliza. Si batería secundaria < 10%: entrar en modo ahorro (solo baliza). |
| **Comunicación** | Watchdog interno (microcontrolador) | Si no se recibe comando del cerebro principal durante > 5 segundos: entrar en **modo fallback**. |

---

## 6. Modo Fallback (Pérdida de Conexión con el Cerebro Principal)

**Condición de activación:** El microcontrolador central no recibe un "heartbeat" del cerebro principal (IA externa o consciencia del paciente) durante más de 5 segundos.

**Secuencia de acciones:**

1. **Reducción de velocidad:** CORPUS reduce su velocidad de movimiento a un 30% de la máxima.
2. **Búsqueda de lugar seguro:** Utilizando el historial de posiciones (buffer) y los sensores de proximidad (TOF simples o las cámaras estéreo compartidas), CORPUS intenta llegar al último punto conocido como "seguro" (ej. su base de carga, o un punto registrado por el operador).
3. **Activación de baliza:** Envía un paquete de emergencia por LoRa (si está disponible) con su posición, estado de batería, y motivo de fallback.
4. **Modo de bajo consumo:** Si no logra llegar a un lugar seguro después de 2 minutos, o si la batería está baja, se sienta (o se recuesta) y espera, manteniendo solo la baliza activa.
5. **Reconexión:** Si recupera la señal, reanuda la operación normal.

**Tabla de estados del modo fallback:**

| Estado | Acción | Salida |
|--------|--------|--------|
| **F1: Pérdida de señal** | Espera 5 segundos. Si no hay heartbeat, entra en F2. | Incrementa contador de pérdidas. |
| **F2: Regreso a base** | Navegación autónoma hacia la última base registrada. Velocidad reducida. | Envía baliza cada 10 segundos. |
| **F3: Modo seguro** | No puede moverse (obstáculo, batería baja). Se sienta o recuesta. | Envía baliza cada 30 segundos. Espera instrucciones. |
| **F4: Emergencia** | Batería crítica, temperatura extrema, o caída detectada. Apaga motores, solo baliza y sensores. | Envía baliza cada 60 segundos. |

---

## 7. Integración con el Cerebro Principal (Consciente)

| Tipo de orden | Canal de comunicación | Prioridad |
|---------------|-----------------------|-----------|
| **Órdenes de movimiento** (ej. "caminar hacia punto X") | Fibra óptica (backbone) | Normal |
| **Órdenes de emergencia** (ej. "detener todo movimiento") | GPIO (cable directo) o LoRa (respaldo) | Máxima (interrupción) |
| **Órdenes de configuración** (ej. "cambiar umbral de temperatura") | Fibra óptica | Baja |

El cerebro principal (IA externa o consciencia del paciente) envía **comandos de alto nivel**. La capa de autonomía (inconsciente) se encarga de:

- **Traducir** esos comandos a secuencias de movimientos específicas (ej. "caminar hacia punto X" → trayectoria, velocidad, ajuste de equilibrio).
- **Ejecutar** los movimientos a través de las articulaciones.
- **Reportar** el estado (posición, temperatura, batería, etc.) al cerebro principal.

**Si el cerebro principal deja de enviar comandos, el inconsciente no se queda inactivo. Entra en modo fallback (sección 6).**

---

## 8. Componentes críticos y certificaciones

| Componente | Modelo | Certificación | Relevancia para autonomía |
|------------|--------|---------------|---------------------------|
| IMU | MPU-6050 / ICM-20948 | (ninguna específica) | Reflejos de caída, equilibrio. |
| Sensor inductivo | AS5715R | AEC-Q100 Grade 0, ISO 26262 ASIL C(D) | Propiocepción crítica (seguridad funcional). |
| Sensor GMR | TLE5012B | ISO 26262 (SIL), PRO-SIL™ | Propiocepción en dedos. |
| Microcontrolador | STM32F7, STM32F4 | (ninguna específica) | Lógica de control y fallback. |
| Driver de motor | DRV8320 | (ninguna específica) | Control de par y corriente. |

**Nota sobre certificaciones:** La ISO 26262 (seguridad funcional en vehículos) es relevante porque los sensores AS5715R y TLE5012B están diseñados originalmente para aplicaciones automotrices críticas (dirección, frenos). Su uso en CORPUS no requiere la certificación completa del sistema, pero indica que los componentes son robustos y confiables.

---

## 9. Estado de implementación

| Subsistema | Estado | Próximo paso |
|------------|--------|---------------|
| Reflejos de caída (IMU) | 🔲 Pendiente | Prototipo con MPU-6050 y algoritmo de detección. |
| Propiocepción (AS5715R) | 🔲 Pendiente | Diseño de PCB con bobinas y rueda fónica. |
| Homeostasis (temperatura, energía) | 🔲 Pendiente | Integración de sensores DS18B20 y BQ76952. |
| Modo fallback (lógica de estados) | 🔲 Pendiente | Implementación en STM32F746. |
| Integración con cerebro principal | 🔲 Pendiente | Definir protocolo de comunicación (paquetes, checksums). |

---

## 10. Referencias

- `update.md` (documento de mejoras de CORPUS, 16 de abril de 2026).
- Kodiak Robotics: fallback system for autonomous trucks.
- NUbots: falling detection and get-up planner.
- NAO robot: Fall Manager.
- Hägele, M. & Söffker, D. (2016). "Fallback strategies for autonomous systems".

---

## 11. Autor y licencia

**Autor:** Enrique Aguayo H. (Mackiber Labs)  
**Asistencia técnica:** DeepSeek (IA)  
**Contacto:** eaguayo@migst.cl  
**Licencia:** Copyright © 2026 Enrique Aguayo. Todos los derechos reservados. Este documento es parte de la documentación técnica de CORPUS. No se permite su uso comercial sin autorización expresa.
