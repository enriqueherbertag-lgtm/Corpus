# Update: Integración de sensores y actuadores piezoeléctricos en CORPUS

**Fecha:** 14 de abril de 2026  
**Versión del concepto:** v1.1.0 (mejora documentada, no implementada)

## Resumen

Se ha añadido al diseño de CORPUS una capa de sensado y actuación mediante piezoeléctricos. No es una piel sensible de alta resolución. Es un complemento de bajo costo (estimado 50 USD por mano) que permite:

- Detectar vibraciones mecánicas (golpes, zumbidos, texturas gruesas).
- Generar retroalimentación háptica básica (vibraciones de 50-200 Hz) para el operador humano a través de ENA.
- Proveer micro-vibraciones de referencia para mejorar la estabilidad de las articulaciones (sin reemplazar los sistemas de control existentes).

## Motivación

Los robots actuales (incluyendo CORPUS en su versión inicial) no tienen capacidad de sentir vibraciones ni de comunicar información táctil al operador. Los sensores táctiles resistivos detectan presión, pero no vibraciones de alta frecuencia. Los piezoeléctricos son baratos, robustos y fáciles de integrar. Añaden una dimensión sensorial nueva sin complejidad excesiva.

## Componentes propuestos (comerciales, no inventados)

| Componente | Modelo de referencia | Función | Costo unitario |
|------------|----------------------|---------|----------------|
| Sensor piezoeléctrico tipo bender | Murata 7BB-20-6 | Detección de vibraciones (10-300 Hz) | 1.50 USD |
| Actuador piezoeléctrico de anillo | Noliac NAC2122 | Vibración háptica localizada (50-200 Hz) | 8.00 USD |
| Multiplexor analógico | ADG732 (Analog Devices) | Leer múltiples sensores con un solo ADC | 12.00 USD |
| Driver de alto voltaje | MPIA (PiezoDrive) | Controlar actuadores (0-150V) | 25.00 USD |

**Total estimado para una mano (4 dedos + palma):** 4 actuadores + 8 sensores + multiplexor + driver ≈ 50 USD.

## Integración prevista

- Los piezoeléctricos se colocan en las yemas de los dedos (sensores y actuadores) y en la palma (solo actuadores).
- Se conectan a un multiplexor analógico (para los sensores) y a un driver de alto voltaje (para los actuadores).
- El microcontrolador principal (triple núcleo redundante) leerá los sensores a 1 kHz y generará señales PWM para los actuadores.

## Impacto en el diseño actual

- **Piel sensible:** No se reemplaza. Se complementa. Los sensores táctiles resistivos siguen midiendo presión estática y fuerza. Los piezoeléctricos miden vibración dinámica.
- **Refrigeración:** No afecta. Los piezoeléctricos disipan menos de 0.1 W cada uno.
- **Energía:** El consumo adicional es mínimo (< 2 W para una mano completa).
- **Software:** Se añadirá un módulo `piezo_control.py` en el repositorio (pendiente).

## Estado actual

- [x] Concepto definido.
- [x] Componentes identificados.
- [x] Costo estimado.
- [ ] Prototipo de un dedo con sensores y actuadores (pendiente).
- [ ] Pruebas de sensibilidad y rango de frecuencia (pendiente).
- [ ] Integración con el firmware existente (pendiente).

## Próximos pasos (si se dispusiera de recursos)

1. Adquirir un juego de componentes (≈ 200 USD para una mano completa).
2. Imprimir en 3D un dedo de prueba con alojamientos para los piezoeléctricos.
3. Conectar a un Arduino (para pruebas iniciales) y medir la respuesta real.
4. Ajustar el diseño y documentar los resultados.

## Nota para el lector

Este documento es una **declaración de intenciones**. No hay prototipo funcional. Los componentes seleccionados son sugerencias, no órdenes de compra. La integración completa en CORPUS requerirá pruebas adicionales y posiblemente cambios de diseño. Sin embargo, la viabilidad técnica es alta porque los piezoeléctricos son componentes maduros y ampliamente utilizados (encendedores, sensores de aparcamiento, altavoces piezoeléctricos).

## Autor

Enrique Aguayo H. – Mackiber Labs  
Asistencia de DeepSeek (IA) en la redacción y estructura.

## Licencia

Copyright © 2026 Enrique Aguayo. Todos los derechos reservados. Este documento se comparte con fines de documentación del proyecto. No se permite su uso comercial sin autorización expresa.
