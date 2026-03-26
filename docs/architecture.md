# Arquitectura de CORPUS

## Capas

| Capa | Función | Componentes |
|------|---------|-------------|
| **Piel receptora** | Captura energía, sensa entorno | Rectenas, termopares, sensores de presión/temperatura/vibración |
| **Sistema energético** | Almacena y distribuye energía | Ultracapacitores, batería LiFePO₄, BMS |
| **Procesamiento distribuido** | Control local y coordinación | Arduinos por articulación, núcleo central ARM |
| **Movilidad** | Desplazamiento y manipulación | Esqueleto grafito-tungsteno, articulaciones con giroscopios |
| **Núcleo central** | Coordinación, aprendizaje, memoria | ARM Cortex-A78, RAM 1 TB, ROM 2 TB, SSD 4 TB |

## Flujo de datos

1. **Sensores locales** (piel, visión, audición) capturan datos en tiempo real.
2. **Microcontroladores locales** (Arduino, ESP32) procesan y filtran.
3. **Eventos relevantes** se envían al núcleo central mediante pulsos binarios.
4. **El núcleo** prioriza, decide acciones globales, consolida recuerdos.
5. **Órdenes** se envían a los subsistemas locales para ejecución.
