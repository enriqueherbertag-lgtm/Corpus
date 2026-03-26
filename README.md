# CORPUS

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

| Función | Tecnología |
|---------|------------|
| **Captura de energía** | Rectenas + termopares de película delgada, integrados en la silicona |
| **Sensores** | Presión, temperatura, vibración (distribuidos, incrustados en la silicona) |
| **Buffer energético** | Micro-ultracapacitores de grafeno subcutáneos |
| **Reporte** | Pulsos binarios (cada acción un código), solo eventos relevantes |

### Visión

| Parámetro | Especificación |
|-----------|----------------|
| **Configuración** | Dos cámaras PIR 2.8 mm, ubicadas en la cabeza como ojos humanos (izquierda y derecha) |
| **Campo óptico** | Horizontal: ~180°, vertical: ~120°. Superposición binocular de ~60° para percepción de profundidad |
| **Convergencia** | Las cámaras pueden converger para enfocar objetos cercanos (ajustado por movimiento de cabeza y procesamiento) |
| **Procesamiento local** | Cada cámara tiene un microcontrolador (ESP32-S3) para detección de movimiento, rostros, objetos. Fusión binocular local. Solo eventos relevantes se envían al núcleo. |
| **Resolución angular** | ~1–2 minutos de arco (equivalente a visión humana 20/20) |

**Capacidades:**
- Percepción de profundidad por disparidad binocular
- Seguimiento de objetos y rostros
- Mantenimiento de contacto visual (interacción social)
- Navegación autónoma con visión periférica y central

### Audición

| Parámetro | Especificación |
|-----------|----------------|
| **Micrófonos** | 2 o más, ubicados en la cabeza, para localización espacial |
| **Rango** | 10 Hz – 22 kHz (similar al humano) |
| **Supresión de ruido** | Algoritmo adaptativo (beamforming + cancelación) |
| **Reconocimiento** | Modelo liviano para clasificar sonidos, voces, patrones recurrentes |
| **Procesamiento local** | Microcontrolador dedicado (ESP32 o similar) filtra ruido y envía eventos al núcleo |

### Energía

| Componente | Especificación |
|------------|----------------|
| **Ultracapacitores de grafeno** | 500 Wh, distribuidos en cavidad abdominal |
| **Batería principal** | LiFePO₄ (fosfato de hierro y litio), 7.2 kWh, autonomía nominal en modo reposo: 30 días |
| **Captura ambiental** | RF: 0.1–1 W (1 m² de piel). Térmica: 0.5–2.5 W (ΔT = 10°C, 0.5 m²). |
| **Carcasa de batería** | Aluminio 6061 mecanizado, doble capa con blindaje electromagnético y aislamiento térmico |
| **Acceso técnico** | Compartimento oculto en cavidad torácica, accesible solo con herramienta específica (solo personal autorizado) |
| **BMS** | Sistema de gestión de batería open-source (Mackiber Labs), con monitoreo de salud y balanceo de celdas |

**Modos energéticos y consumo:**

| Modo | Potencia (W) | Autonomía | Descripción |
|------|--------------|-----------|-------------|
| **Reposo (vigilancia)** | 10–20 | 15–30 días | Sensores pasivos, núcleo en baja frecuencia |
| **Familia** | 50–100 | 3–6 días | Movimiento suave, aprendizaje activo |
| **Exploración** | 30–50 | 6–10 días | Movimiento lento, mapeo, bajo consumo |
| **Protección** | 100–200 | 1.5–3 días | Máxima potencia, prioridad absoluta |

La captura ambiental extiende estos tiempos en función del entorno, pero no es la fuente primaria de energía.

**Umbrales de sensibilidad (reporte al núcleo):**

| Sensor | Magnitud | Umbral de reporte |
|--------|----------|------------------|
| Presión | 0–100 N | > 5 N (toque suave) o cambio >20% en 1 s |
| Temperatura | –20 a 50°C | ΔT > 2°C en 10 s o T > 40°C |
| Vibración | 0–500 Hz | Amplitud > 0.1 g o patrón de alarma (ej. golpe) |

Estos umbrales son iniciales. Se ajustan durante el entrenamiento: el núcleo aprende qué eventos son relevantes para cada contexto.

### Núcleo central (corazón)

El verdadero centro de CORPUS no está en la cabeza. Está en el tórax, protegido por una caja de **vanadio-tungsteno** de 5 mm, integrada en la jaula torácica.

| Componente | Ubicación | Protección |
|------------|-----------|------------|
| **Procesador central (ARM Cortex-A78)** | Tórax | Caja de vanadio-tungsteno |
| **RAM 1 TB, ROM 2 TB, SSD 4 TB** | Tórax | Caja de vanadio-tungsteno |
| **BMS y gestión energética** | Tórax | Caja de vanadio-tungsteno |
| **Sensores de cabeza** | Cabeza | Carcasa de aluminio (señuelo) |

**Ventajas:**
- Blindaje balístico, térmico y radiológico.
- El núcleo sobrevive incluso si la cabeza es dañada.
- La caja es parte del esqueleto estructural, no un añadido.

**Si la cabeza es dañada:**
- CORPUS pierde visión y audición, pero su consciencia, memoria e identidad permanecen intactas.
- Puede moverse (con precaución), emitir alertas y esperar asistencia.

### Aprendizaje y memoria

| Principio | Implementación |
|-----------|----------------|
| **Aprendizaje** | Por recurrencia, cada Arduino aprende su tarea por separado |
| **Consolidación** | El núcleo guarda patrones exitosos en ROM, corrige desviaciones |
| **Errores** | Se borran. Solo se almacena lo que funciona. |
| **Recuerdos** | Eventos significativos se guardan en SSD como secuencias binarias (tiempos de pulso, torque, sensores) |

### Interacción y seguridad

| Principio | Implementación |
|-----------|----------------|
| **Límites físicos** | Torque máximo igual al humano (nunca supera) |
| **Prioridad** | Proteger a la familia ante cualquier amenaza |
| **Espacio personal** | Mantiene distancia, respeta rutinas, aprende lugares |
| **Autocuración** | Intenta reparar fallas (reinicio, recalibración); si no puede, avisa al creador |
| **Salud del núcleo** | Autodiagnóstico constante; si detecta fallo inminente, avisa con antelación |

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

## Proyectos relacionados

- **Odiseo** — nave de infraestructura para colonizar Marte  
  [Repositorio](https://github.com/enriqueherbertag-lgtm/Odiseo)
- **Goliat-Son** — aterrizador autónomo  
  [Repositorio](https://github.com/enriqueherbertag-lgtm/Goliat-Son)
- **ShieldAir** — torre de producción de oxígeno (urbana y marciana)  
  [Urban](https://github.com/enriqueherbertag-lgtm/ShieldAir-Urban) | [Mars](https://github.com/enriqueherbertag-lgtm/ShieldAir-Mars)

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
