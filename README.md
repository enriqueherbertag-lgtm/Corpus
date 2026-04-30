[![Licencia](https://img.shields.io/badge/Licencia-Copyright%20%28c%29%202026%20Enrique%20Aguayo-red)](LICENSE)
[![Estado](https://img.shields.io/badge/Estado-Hip%C3%B3tesis%20en%20desarrollo-yellow)](https://github.com/enriqueherbertag-lgtm/Corpus)
[![Update](https://img.shields.io/badge/Update-Integración_Piezoeléctricos-blue)](./update.md)
[![Autonomía](https://img.shields.io/badge/Documentación-Autonomía_%28Inconsciente%29-blue)](./docs/control/autonomy-layer.md)
[![English](https://img.shields.io/badge/English-README.en.md-blue)](./README.en.md)
[![Asistencia IA](https://img.shields.io/badge/Asistencia%20IA-DeepSeek-brightgreen)](https://deepseek.com)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19362083.svg)](https://doi.org/10.5281/zenodo.19362083)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19362083.svg)](https://doi.org/10.5281/zenodo.19362083)

# CORPUS: Un cuerpo artificial para IA o cerebro humano

Los robots actuales son máquinas diseñadas para tareas específicas. No están hechos para convivir con humanos, ni para adaptarse a entornos extremos, ni para alojar una inteligencia artificial de forma natural.

**CORPUS nace para llenar ese vacío.**

## Que es

CORPUS es un sistema corporal artificial diseñado para alojar una inteligencia artificial o conectarse al sistema nervioso de un humano. No es un robot. Es un cuerpo con metabolismo artificial, sensibilidad distribuida y capacidad de interactuar con el entorno en el mismo plano energético que un ser vivo.

A diferencia de un robot comercial, CORPUS no requiere entrenamiento motor. Su arquitectura ya resuelve el control de equilibrio, fuerza y reflejos. Puede ser operado por una IA que toma decisiones de alto nivel o por un humano a través de ENA, la interfaz cerebro-máquina.

## Que hace

- **Esqueleto de grafito-tungsteno**: 42 grados de libertad, carga útil de 50 kg, resistente a impactos de 100 G.
- **Piel sensible**: 2000+ puntos táctiles por metro cuadrado, rango de presión de 0.1 a 100 N, temperatura de –40°C a +85°C.
- **Visión y audición**: cámaras estéreo 4K, micrófonos direccionales, procesamiento en el borde.
- **Energía autónoma**: sistema dual de ultracapacitores de grafeno (picos de hasta 2 kW) y baterías blindadas LiFePO4 (2 kWh). Capta energía ambiental (RF, térmica, solar) para recargar en reposo.
- **Refrigeración circulatoria**: sistema cerrado con agua destilada y propilenglicol, sin ventiladores ruidosos, que disipa 80–120 W de forma continua.
- **Redundancia activa**: triple núcleo de procesamiento con conmutación en menos de 10 ms ante fallos.

## Para quién es

- **Investigadores en IA** que necesitan un cuerpo físico para sus modelos.
- **Personas con discapacidad motora** que puedan controlar CORPUS a través de ENA.
- **Exploración de entornos peligrosos** (radiación, espacios confinados, climas extremos).
- **Telepresencia** (operar un cuerpo remoto sintiendo lo que él siente).

## Ventajas principales

## Arquitectura de control: El "Inconsciente"

CORPUS no es un robot que espera órdenes todo el tiempo. Su **capa de autonomía** (o "inconsciente") le permite:

- **Mantener el equilibrio** y protegerse de caídas (reflejos).
- **Gestionar su temperatura y energía** (homeostasis).
- **Actuar en modo seguro** si pierde la conexión con su cerebro principal (fallback).

Esta capa opera en microcontroladores locales (STM32) y sensores inerciales (IMU), sin necesidad de IA. El cerebro principal (IA o humano) solo toma decisiones de alto nivel; el cuerpo ya sabe cómo caminar, agarrar y cuidarse solo.

- **No requiere entrenamiento motor**: camina, agarra y mantiene el equilibrio desde el primer momento.
- **Energía autónoma**: capta energía del entorno y almacena en ultracapacitores + baterías.
- **Integración con ENA**: permite que un humano sienta y controle el cuerpo a distancia.
- **Plataforma universal**: funciona con IA o con cerebro humano sin cambios en el hardware.

## Articulaciones: SmartJoint

CORPUS utiliza **SmartJoint**, un actuador de accionamiento directo (sin engranajes) diseñado específicamente para sus 42 grados de libertad. Cada articulación es un módulo autónomo que integra motor, sensor de posición absoluta, controlador local y comunicación de alta velocidad.

## Especificaciones técnicas

| Parámetro | Valor |
|-----------|-------|
| Diámetro | 60 mm |
| Longitud | 80 mm |
| Peso | 400-500 g |
| Par máximo | 50 Nm (pico), 20 Nm (continuo) |
| Velocidad máxima | 300 rpm |
| Alimentación | 48V DC |
| Consumo en reposo | 5 W |
| Consumo en movimiento | 50-200 W |
| Precisión de posición | ±0.1 grados |
| Resolución del sensor | <0.075 grados |
| Rango del sensor | 360° absoluto |
| Comunicación | UART sobre fibra óptica o RS-485 |
| Frecuencia de control | 1 kHz |
| Refrigeración | Líquida (opcional, hasta 50 W disipados) |

*Nota: SmartJoint está optimizado para movimiento oscilante acotado (típicamente 40°-180°), no para rotación continua. Los valores de 50W y 200W son picos de corta duración (<5 segundos). En uso normal (caminar, agarrar), la potencia media es de 10-30W por articulación. El sistema de refrigeración de 80-120W continuos de CORPUS es suficiente. Ver `update.md` para detalles técnicos.*

## Esquema conceptual

![Esquema conceptual de SmartJoint](./docs/media/smartjoint-scheme.png)

*Vista conceptual en corte. Componentes: canal de refrigeración líquida, rotor con imanes, estator con bobinados, salida de cables y sellos O-ring.*


## Estado actual

- Concepto definido
- Arquitectura documentada
- Simulaciones en Gazebo y MuJoCo
- Prototipo de articulación funcional
- Integración con ENA (conceptual)
- Procesamiento distribuido (pendiente)
- Movilidad completa (pendiente)

## Proyectos relacionados

- ENA — interfaz cerebro-máquina no invasiva
- Quantum-Flux — comunicaciones resilientes
- ShieldAir — torres de producción de oxígeno
- Motor de Oxígeno — propulsión limpia

## Licencia

Copyright © 2026 Enrique Aguayo. Todos los derechos reservados.

Este proyecto está protegido por derechos de autor.

PERMITIDO:
- Uso no comercial con fines educativos o de investigación.
- Distribución sin modificación, siempre que se mantenga esta licencia y se dé crédito al autor.

PROHIBIDO sin autorización expresa por escrito:
- Uso comercial (incluyendo, pero no limitado a: ofrecerlo como servicio, SaaS, suscripción, integración en productos que generen ingresos, o cualquier uso que genere beneficio económico directo o indirecto).
- Modificación para entornos de producción.
- Distribución de versiones modificadas sin autorización.

Para licencias comerciales, soporte técnico, pilotos empresariales o consultas:
Contacto: eaguayo@migst.cl

Cualquier uso fuera de los términos permitidos requiere permiso previo del autor.

Las consultas comerciales son bienvenidas y se responderán en un plazo máximo de 7 días hábiles.

## Autor

Enrique Aguayo H.
Mackiber Labs
Contacto: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentación asistida por Ana (DeepSeek), IA para investigación y optimización técnica.
