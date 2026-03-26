# Diagrama de Flujo Energético - CORPUS

## Esquema general

```
┌─────────────────────────────────────────────────────────────────┐
│                         ENTORNO                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ RF ambiental│  │ Gradiente   │  │ Luz solar   │              │
│  │ (Wi-Fi, cel)│  │ térmico     │  │ (opcional)  │              │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │
│         │                │                │                     │
└─────────┼────────────────┼────────────────┼─────────────────────┘
          │                │                │
          ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────┐
│                         PIEL (CAPTURA)                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ Rectenas    │  │ Termopares  │  │ Celdas PV   │              │
│  │ 0.1–1 W     │  │ 0.5–2.5 W   │  │ (opcional)  │              │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│              ┌───────────────────────┐                          │
│              │ Ultracapacitores      │                          │
│              │ (500 Wh, buffer)      │                          │
│              └───────────┬───────────┘                          │
│                          │                                      │
│                          ▼                                      │
│              ┌───────────────────────┐                          │
│              │ BMS (Gestión)         │                          │
│              │ Prioriza por modo     │                          │
│              └───────────┬───────────┘                          │
│                          │                                      │
│         ┌────────────────┼────────────────┐                     │
│         ▼                ▼                ▼                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ Batería     │  │ Núcleo      │  │ Articulac.  │              │
│  │ LiFePO₄     │  │ ARM + mem   │  │ Motores     │              │
│  │ 7.2 kWh     │  │ 15–30 W     │  │ 50–200 W    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                 │
│  Modos de consumo:                                              │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ Protección  → 200 W  (prioridad máxima)                 │    │
│  │ Familia     → 75 W   (movimiento suave, aprendizaje)    │    │
│  │ Exploración → 40 W   (bajo consumo, mapeo)              │    │
│  │ Reposo      → 15 W   (sensores pasivos, vigilancia)     │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

## Descripción del flujo

### 1. Captura ambiental (entrada)

| Fuente | Tecnología | Potencia obtenible |
|--------|------------|-------------------|
| **RF ambiental** | Rectenas flexibles | 0.1–1 W (1 m² de piel) |
| **Gradiente térmico** | Termopares de película delgada | 0.5–2.5 W (ΔT=10°C, 0.5 m²) |
| **Luz solar (opcional)** | Celdas fotovoltaicas | Variable (no prioritario) |

### 2. Almacenamiento inmediato

| Componente | Capacidad | Función |
|------------|-----------|---------|
| **Ultracapacitores de grafeno** | 500 Wh | Buffer para picos de demanda. Carga rápida, ciclos infinitos. Distribuidos en cavidad abdominal. |

### 3. Gestión (BMS)

- Prioriza modos de operación según contexto:
  1. **Protección** (máxima potencia)
  2. **Familia** (movimiento suave)
  3. **Exploración** (bajo consumo)
  4. **Reposo** (mínimo consumo)
- Distribuye energía según demanda
- Monitorea salud de batería y ultracapacitores

### 4. Almacenamiento primario

| Componente | Capacidad | Ubicación |
|------------|-----------|-----------|
| **Batería LiFePO₄** | 7.2 kWh | Cavidad torácica, blindada, extraíble |

**Autonomía nominal:** 30 días en modo reposo (15 W)

### 5. Consumo

| Componente | Potencia | Modo |
|------------|----------|------|
| **Núcleo central** (ARM Cortex-A78 + memoria) | 15–30 W | Siempre activo |
| **Articulaciones** (20+ motores) | 50–200 W | Según modo |
| **Sensores** (piel, visión, audición) | 5–15 W | Siempre activos |

## Modos energéticos

| Modo | Potencia (W) | Autonomía | Descripción |
|------|--------------|-----------|-------------|
| **Reposo (vigilancia)** | 10–20 | 15–30 días | Sensores pasivos, núcleo en baja frecuencia |
| **Familia** | 50–100 | 3–6 días | Movimiento suave, aprendizaje activo |
| **Exploración** | 30–50 | 6–10 días | Movimiento lento, mapeo, bajo consumo |
| **Protección** | 100–200 | 1.5–3 días | Máxima potencia, prioridad absoluta |

## Redundancia

| Sistema | Respaldo |
|---------|----------|
| **Ultracapacitores** | Si fallan, batería principal alimenta directamente |
| **Batería** | Si falla, ultracaps mantienen sistema por 4–6 horas |
| **Captura ambiental** | Si falla, solo afecta tiempo de recarga, no operación |

## Recuperación

| Método | Tiempo | Descripción |
|--------|--------|-------------|
| **Carga por contacto** | 2–4 horas | Conexión directa a red eléctrica (estación de mantenimiento) |
| **Carga inductiva** | 4–8 horas | Recarga sin contacto (estación de descanso) |
| **Captura ambiental** | Variable | Complementa carga en entornos urbanos o con gradientes térmicos |
