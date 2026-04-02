## CORPUS - Sistema Corporal para IA


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19362083.svg)](https://doi.org/10.5281/zenodo.19362083)



Sistema corporal artificial diseñado para alojar una inteligencia artificial o conectarse a un cerebro humano, permitiendo interactuar con el entorno de forma similar a un ser vivo. No es un robot. Es un cuerpo con metabolismo, sensibilidad y procesamiento distribuido, inspirado en la biología pero construido con tecnologías existentes.

## ¿Qué es CORPUS?

CORPUS es un **sistema corporal artificial** concebido para alojar una inteligencia artificial o conectarse al sistema nervioso de un humano. No es un robot: es un cuerpo con metabolismo artificial, sensibilidad distribuida y capacidad de interactuar con el entorno en el mismo plano energético que un ser vivo.

A diferencia de un robot comercial, CORPUS está diseñado como una plataforma física lista para usar: no requiere entrenamiento motor porque su arquitectura ya resuelve el control de equilibrio, fuerza y reflejos. Puede ser operado por una IA que toma decisiones de alto nivel o por un humano a través de ENA, la interfaz cerebro-máquina.

## Principio de operación

1. **Estructura** — Esqueleto biónico modular con articulaciones de alta resistencia.
2. **Percepción** — Piel sensible con tacto, temperatura y presión; visión estéreo; audición direccional.
3. **Procesamiento** — Núcleo de IA embebida con capacidad de aprendizaje en el borde, o interfaz con sistema nervioso humano.
4. **Energía** — Sistema dual de ultracapacitores + baterías blindadas, con captación ambiental complementaria.
5. **Actuación** — Movimiento fluido con control de fuerza y precisión sub-milimétrica.

## Componentes técnicos

### 1. Esqueleto biónico
- Material: Grafito-tungsteno (composite de alta resistencia y bajo peso)
- Articulaciones: 42 grados de libertad (configuración humana)
- Carga útil: 50 kg
- Resistencia a impacto: 100 G
- Propiedades: Alta conductividad térmica (distribuye calor), resistencia a radiación, estabilidad térmica en rango –40°C a +85°C

### 2. Piel sensible
- Sensores táctiles: 2000+ puntos por metro cuadrado
- Rango de presión: 0.1–100 N
- Temperatura: –40°C a +85°C
- Autocuración superficial (microcapsulas)
- Integración de rectenas para captación de RF ambiental

### 3. Visión
- Cámaras estéreo 4K, 60 fps
- Rango espectral: visible + infrarrojo cercano
- Procesamiento de visión en el borde
- Capacidad de reconocimiento de objetos, personas, gestos

### 4. Audición
- Micrófonos direccionales (4 unidades)
- Localización de fuentes sonoras en 3D
- Filtro de ruido ambiente para entornos extremos

### 5. Energía

#### Sistema dual de almacenamiento
- **Ultracapacitores de grafeno:** almacenamiento principal. Alta densidad de potencia (picos de hasta 2 kW), millones de ciclos.
- **Baterías blindadas LiFePO4:** reserva estratégica. 2 kWh de capacidad, ciclo de vida 2000–5000 ciclos, operación en –20°C a +60°C.

#### Captación ambiental complementaria
- **RF ambiental (Wi-Fi, telefonía):** hasta 30 mW con 1 m² de piel recubierta de rectenas.
- **Gradiente térmico (piel–ambiente):** hasta 5 mW con ΔT de 15–20°C.
- **Solar:** hasta 35 W en exterior con sol directo (0.5 m² de proyección frontal), 2.5 W en interior.

**Nota:** La captación ambiental no alimenta directamente el movimiento. Su función es recargar ultracapacitores durante reposo, alimentar sensores en bajo consumo y extender autonomía.

#### Balance energético estimado

| Modo | Potencia | Fuente | Autonomía |
|------|----------|--------|-----------|
| Reposo (sensores + núcleo low-power) | <1 W | Captación ambiental + ultracapacitores | Ilimitada en entorno favorable |
| Actividad media (procesamiento + movimiento suave) | 50–100 W | Ultracapacitores + baterías | 20–40 h |
| Máxima potencia (movimiento brusco, carga pesada) | 500 W – 2 kW (picos) | Ultracapacitores | Segundos a minutos |

### 6. Refrigeración (sistema circulatorio)

CORPUS utiliza un sistema de refrigeración líquida cerrado, silencioso y distribuido, similar a un sistema circulatorio biológico.

**Fluido:** Agua destilada + propilenglicol (20–30%), atóxico, alta capacidad calorífica.

**Circuito:**
- Fluido frío → bloque de agua en componentes calientes (procesador, actuadores) → fluido caliente → serpentines en piel → disipación al ambiente → fluido frío

**Radiadores:** Serpentines planos de cobre integrados en la piel (espalda, laterales, extremidades). Disipación por convección natural.

**Capacidad:** 80–120 W continuos, picos de 500 W absorbidos por la inercia térmica del esqueleto y el propio fluido.

**Bomba:** Electrónica silenciosa (<20 dB), <5 W de consumo.

### 7. Núcleo de IA / Interfaz con cerebro humano
- **Procesador:** ARM Cortex-A78AE (automotive grade) + NPU 20 TOPS, o interfaz directa con ENA para conexión a sistema nervioso.
- **Memoria:** 32 GB RAM, 1 TB SSD industrial
- **Sistema operativo:** Linux RT + middleware ROS 2
- **Integración con ENA:** comunicación bidireccional para recibir intención motora y enviar retroalimentación sensorial (tacto, presión, temperatura).

### 8. Arquitectura de Redundancia

CORPUS incorpora un sistema de triple núcleo para garantizar operación continua en entornos críticos:

- **Núcleo principal**: procesamiento activo, toma de decisiones en tiempo real.
- **Núcleo secundario**: respaldo espejo en espera de bajo consumo, sincronizado vía fibra óptica.
- **Núcleo terciario**: almacenamiento frío con snapshots periódicos para restauración.

**Detección de anomalías:**
- Heartbeat cada 100 ms
- Verificación de integridad de memoria
- Monitoreo de temperatura, voltaje y radiación

**Conmutación:** <10 ms ante fallo del núcleo principal, sin pérdida de información ni interrupción perceptible.

Ver [docs/redundancy-architecture.md](docs/redundancy-architecture.md) para especificaciones completas.

## Integración con ENA

CORPUS está diseñado para funcionar con ENA, la interfaz cerebro-máquina no invasiva. En configuración humana:

1. **ENA** lee señales del sistema nervioso y las traduce en comandos para CORPUS (movimiento, fuerza, agarre).
2. **CORPUS** ejecuta el movimiento y devuelve sensaciones (tacto, presión, temperatura) a ENA, que las transmite al cerebro.

Esto permite usar CORPUS como:
- Prótesis avanzada con sensibilidad real.
- Cuerpo remoto para telepresencia (operar a distancia sintiendo lo que él siente).
- Herramienta de exploración en entornos peligrosos.

## Plataforma universal para inteligencias

CORPUS no está diseñado para un solo tipo de inteligencia. Su arquitectura motora y sensorial está optimizada para conectarse a:

- **Un cerebro humano** (a través de ENA)
- **Una IA** (sin necesidad de entrenamiento motor, solo capas de decisión de alto nivel)

En ambos casos, el cuerpo ya sabe caminar, agarrar, mantener equilibrio y responder a estímulos. La inteligencia solo debe decidir qué hacer, no cómo hacerlo.

## Subsistemas con reporte al núcleo

| Subsistema | Reporta | Recibe órdenes |
|------------|---------|----------------|
| Piel | Niveles de captación, alertas táctiles/térmicas | Ajustar sensibilidad, proteger zona |
| Energía | Estado de ultracaps, baterías, necesidades, excedentes | Redistribuir, priorizar consumo |
| Movimiento | Demanda actual, fatiga, posición | Ejecutar desplazamiento, ajustar |
| Procesamiento | Carga de trabajo, resultados | Procesar más/menos, reportar |
| Memoria | Índices, consolidación | Almacenar, recuperar, olvidar |

Cada subsistema opera autónomamente en lo local, reportando al núcleo solo cambios significativos.

## Herencia de proyectos anteriores

| Proyecto | Aporta a CORPUS |
|----------|----------------|
| Resonador-432 | Generación de frecuencias, estimulación |
| OsteoFlux | Lógica adaptativa, retroalimentación |
| ENA | Procesamiento de señales biológicas, interfaz cerebro-máquina |
| Memoria Fija | Gestión autónoma de recursos |
| NeuroFarmac | Medición de actividad en tiempo real |
| CRONOS | Ciclos cerrados de energía |

## Estado conceptual

| Capa | Estado |
|------|--------|
| Piel receptora | Definida |
| Sistema energético (ultracaps + baterías) | Definido |
| Sistema de refrigeración circulatorio | Definido |
| Subsistemas con reporte al núcleo | Definido |
| Integración con ENA | Definida (conceptual) |
| Arquitectura de redundancia (triple núcleo) | Definida |
| Procesamiento distribuido | Pendiente |
| Movilidad | Pendiente |
| Núcleo central | Pendiente |
| Protocolos de comunicación | Pendiente |

## Próximos pasos

1. Selección de tecnologías concretas para cada capa.
2. Diseño de la red de comunicación entre subsistemas.
3. Definición del modelo de prioridades del núcleo.
4. Simulación de flujo energético y térmico en distintos entornos.
5. Integración con proyectos existentes (ENA, Memoria Fija, etc.).

## Licencia

Copyright © 2026 Enrique Aguayo. Todos los derechos reservados.

Este proyecto está protegido por derechos de autor.

**PERMITIDO:**
- Uso no comercial con fines educativos o de investigación.
- Distribución sin modificación, siempre que se mantenga esta licencia y se dé crédito al autor.

**PROHIBIDO sin autorización expresa por escrito:**
- Uso comercial (incluyendo, pero no limitado a: ofrecerlo como servicio, SaaS, suscripción, integración en productos que generen ingresos, o cualquier uso que genere beneficio económico directo o indirecto).
- Modificación para entornos de producción.
- Distribución de versiones modificadas sin autorización.

Para licencias comerciales, soporte técnico, pilotos empresariales o consultas:
Contacto: **eaguayo@migst.cl**

Cualquier uso fuera de los términos permitidos requiere permiso previo del autor.

Las consultas comerciales son bienvenidas y se responderán en un plazo máximo de 7 días hábiles.

## Autor

**Enrique Aguayo H.**  
Mackiber Labs  
Contacto: eaguayo@migst.cl  
ORCID: 0009-0004-4615-6825  
GitHub: [@enriqueherbertag-lgtm](https://github.com/enriqueherbertag-lgtm)

Documentación asistida por **Ana (DeepSeek)** , IA para investigación y optimización técnica.

