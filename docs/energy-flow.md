# Flujo de Energía - CORPUS

## Diagrama de Flujo

```
[Entorno]
    │
    ├── RF ambiental ──→ [Rectenas (piel)] ──┐
    │                                         │
    ├── Gradiente térmico ──→ [Termopares] ──┤
    │                                         │
    └── Luz ambiental ──→ [Celdas (opcional)] ──┘
                                              │
                                              ▼
                                    [Ultracapacitores (buffer)]
                                    (500 Wh, cavidad abdominal)
                                              │
                                              ▼
                                    [BMS (Battery Management System)]
                                              │
                    ┌─────────────────────────┼─────────────────────────┐
                    │                         │                         │
                    ▼                         ▼                         ▼
            [Batería LiFePO₄]         [Núcleo central]          [Articulaciones]
            (7.2 kWh, 30 días)        (ARM, RAM, ROM)          (motores, sensores)
```

## Descripción del flujo

### 1. Captura ambiental (entrada)

| Fuente | Tecnología | Potencia obtenible |
|--------|------------|-------------------|
| **RF ambiental** | Rectenas flexibles | 0.1–1 W (1 m² de piel) |
| **Gradiente térmico** | Termopares de película delgada | 0.5–2.5 W (ΔT=10°C, 0.5 m²) |
| **Luz solar (opcional)** | Celdas fotovoltaicas | Variable (no prioritario) |

### 2. Almacenamiento inmediato

| Componente | Capacidad | Ubicación | Función |
|------------|-----------|-----------|---------|
| **Ultracapacitores de grafeno** | 500 Wh | Cavidad abdominal | Buffer para picos de demanda. Carga rápida, ciclos infinitos. |

### 3. Gestión (BMS)

| Función | Descripción |
|---------|-------------|
| **Priorización** | Protección > Familia > Exploración > Reposo |
| **Distribución** | Asigna energía según demanda de cada subsistema |
| **Monitoreo** | Supervisa salud de batería y ultracapacitores |

### 4. Almacenamiento primario

| Componente | Capacidad | Ubicación | Autonomía nominal |
|------------|-----------|-----------|------------------|
| **Batería LiFePO₄** | 7.2 kWh | Cavidad torácica, blindada, extraíble | 30 días en modo reposo (15 W) |

### 5. Consumo

| Componente | Potencia | Observaciones |
|------------|----------|---------------|
| **Núcleo central** (ARM Cortex-A78 + memoria) | 15–30 W | Siempre activo |
| **Articulaciones** (20+ motores) | 50–200 W | Según modo de movilidad |
| **Sensores** (piel, visión, audición) | 5–15 W | Siempre activos |

## Modos energéticos

| Modo | Potencia (W) | Autonomía | Prioridad | Descripción |
|------|--------------|-----------|-----------|-------------|
| **Reposo (vigilancia)** | 10–20 | 15–30 días | Baja | Sensores pasivos, núcleo en baja frecuencia |
| **Familia** | 50–100 | 3–6 días | Alta | Movimiento suave, aprendizaje activo |
| **Exploración** | 30–50 | 6–10 días | Media | Movimiento lento, mapeo, bajo consumo |
| **Protección** | 100–200 | 1.5–3 días | Máxima | Máxima potencia, prioridad absoluta |

## Redundancia

| Sistema | Respaldo | Tiempo de respaldo |
|---------|----------|-------------------|
| **Ultracapacitores** | Batería principal | Inmediato |
| **Batería** | Ultracapacitores | 4–6 horas |
| **Captura ambiental** | Batería + ultracaps | No afecta operación |

## Recuperación

| Método | Tiempo | Descripción |
|--------|--------|-------------|
| **Carga por contacto** | 2–4 horas | Conexión directa a red eléctrica (estación de mantenimiento) |
| **Carga inductiva** | 4–8 horas | Recarga sin contacto (estación de descanso) |
| **Captura ambiental** | Variable | Complementa carga en entornos urbanos o con gradientes térmicos |

## Resumen numérico

| Parámetro | Valor |
|-----------|-------|
| **Capacidad total** | 7.7 kWh (7.2 + 0.5) |
| **Autonomía en reposo** | 30 días (15 W) |
| **Autonomía en protección** | 1.5 días (200 W) |
| **Captura ambiental máxima** | 3.5 W (RF + térmica) |
| **Recarga por contacto** | 2–4 horas |
