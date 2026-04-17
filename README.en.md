[![License](https://img.shields.io/badge/License-Copyright%20%28c%29%202026%20Enrique%20Aguayo-red)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Hypothesis%20under%20development-yellow)](https://github.com/enriqueherbertag-lgtm/Corpus)
[![Update](https://img.shields.io/badge/Update-Piezoelectric_Integration-blue)](./update.md)
[![Autonomy](https://img.shields.io/badge/Documentation-Autonomy_%28Unconscious%29-blue)](./docs/control/autonomy-layer.md)
[![Spanish](https://img.shields.io/badge/Spanish-README.es.md-blue)](./README.es.md)
[![AI Assistance](https://img.shields.io/badge/AI%20Assistance-DeepSeek-brightgreen)](https://deepseek.com)

# CORPUS: An artificial body for AI or human brain

Today's robots are machines designed for specific tasks. They are not made to coexist with humans, nor to adapt to extreme environments, nor to naturally host artificial intelligence.

**CORPUS was born to fill that gap.**

## What it is

CORPUS is an artificial body system designed to host an artificial intelligence or connect to a human's nervous system. It is not a robot. It is a body with artificial metabolism, distributed sensitivity, and the ability to interact with the environment on the same energy level as a living being.

Unlike commercial robots, CORPUS does not require motor training. Its architecture already solves balance, force, and reflex control. It can be operated by an AI that makes high-level decisions or by a human through ENA, the brain-machine interface.

## What it does

- **Graphite-tungsten skeleton**: 42 degrees of freedom, 50 kg payload, withstands 100 G impacts.
- **Sensitive skin**: 2000+ tactile points per square meter, pressure range 0.1 to 100 N, temperature from –40°C to +85°C.
- **Vision and hearing**: 4K stereo cameras, directional microphones, edge processing.
- **Autonomous energy**: dual system of graphene ultracapacitors (peaks up to 2 kW) and shielded LiFePO4 batteries (2 kWh). Harvests ambient energy (RF, thermal, solar) to recharge while idle.
- **Circulatory cooling**: closed-loop system with distilled water and propylene glycol, no noisy fans, dissipates 80–120 W continuously.
- **Active redundancy**: triple processing core with failover under 10 ms.

## Who it is for

- **AI researchers** who need a physical body for their models.
- **People with motor disabilities** who can control CORPUS through ENA.
- **Hazardous environment exploration** (radiation, confined spaces, extreme climates).
- **Telepresence** (operating a remote body while feeling what it feels).

## Key advantages

## Control architecture: The "Unconscious"

CORPUS is not a robot that waits for orders all the time. Its **autonomy layer** (or "unconscious") allows it to:

- **Maintain balance** and protect itself from falls (reflexes).
- **Manage its temperature and energy** (homeostasis).
- **Act in safe mode** if it loses connection to its main brain (fallback).

This layer operates on local microcontrollers (STM32) and inertial sensors (IMU), without requiring AI. The main brain (AI or human) only makes high-level decisions; the body already knows how to walk, grasp, and take care of itself.

- **No motor training required**: walks, grasps, and maintains balance from the first moment.
- **Autonomous energy**: harvests energy from the environment and stores it in ultracapacitors + batteries.
- **ENA integration**: allows a human to feel and control the body remotely.
- **Universal platform**: works with AI or human brain without hardware changes.

## Joints: SmartJoint

CORPUS uses **SmartJoint**, a direct-drive actuator (no gears) specifically designed for its 42 degrees of freedom. Each joint is an autonomous module that integrates motor, absolute position sensor, local controller, and high-speed communication.

## Technical specifications

| Parameter | Value |
|-----------|-------|
| Diameter | 60 mm |
| Length | 80 mm |
| Weight | 400-500 g |
| Peak torque | 50 Nm (peak), 20 Nm (continuous) |
| Maximum speed | 300 rpm |
| Power supply | 48V DC |
| Idle consumption | 5 W |
| Motion consumption | 50-200 W |
| Position accuracy | ±0.1 degrees |
| Sensor resolution | <0.075 degrees |
| Sensor range | 360° absolute |
| Communication | UART over fiber optic or RS-485 |
| Control frequency | 1 kHz |
| Cooling | Liquid (optional, up to 50 W dissipated) |

*Note: SmartJoint is optimized for bounded oscillatory motion (typically 40°-180°), not continuous rotation. The 50W and 200W values are short-duration peaks (<5 seconds). In normal use (walking, grasping), average power is 10-30W per joint. CORPUS's 80-120W continuous cooling system is sufficient. See `update.md` for technical details.*

## Conceptual diagram

![SmartJoint conceptual diagram](./docs/media/smartjoint-scheme.png)

*Cutaway conceptual view. Components: liquid cooling channel, rotor with magnets, stator with windings, cable outlet and O-ring seals.*

## Current status

- Concept defined
- Architecture documented
- Simulations in Gazebo and MuJoCo
- Functional joint prototype
- ENA integration (conceptual)
- Distributed processing (pending)
- Full mobility (pending)

## Related projects

- ENA — non-invasive brain-machine interface
- Quantum-Flux — resilient communications
- ShieldAir — oxygen production towers
- Oxygen Engine — clean propulsion

## License

Copyright © 2026 Enrique Aguayo. All rights reserved.

This project is protected by copyright.

PERMITTED:
- Non-commercial use for educational or research purposes.
- Unmodified distribution, provided this license is retained and credit is given to the author.

PROHIBITED without express written authorization:
- Commercial use (including, but not limited to: offering as a service, SaaS, subscription, integration into revenue-generating products, or any use that generates direct or indirect economic benefit).
- Modification for production environments.
- Distribution of modified versions without authorization.

For commercial licenses, technical support, enterprise pilots, or inquiries:
Contact: eaguayo@migst.cl

Any use outside the permitted terms requires prior permission from the author.

Commercial inquiries are welcome and will be answered within a maximum of 7 business days.

## Author

Enrique Aguayo H.
Mackiber Labs
Contact: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentation assisted by Ana (DeepSeek), AI for research and technical optimization.
