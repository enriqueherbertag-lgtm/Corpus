# Arquitectura de Redundancia para el Núcleo de CORPUS

## 1. Visión General

CORPUS requiere una arquitectura de núcleo de procesamiento con redundancia activa para garantizar su operación continua en entornos críticos. El sistema está diseñado para detectar anomalías en el núcleo principal y conmutar a un respaldo espejo en menos de 10 ms, sin pérdida de información ni interrupción perceptible.

## 2. Arquitectura de Tres Núcleos


┌─────────────────────────────────────────────────────────────┐
│ NÚCLEO PRINCIPAL │
│ (ARM Cortex-A78AE + NPU 20 TOPS + 32 GB RAM + 1 TB SSD) │
│ │
│ - Procesamiento activo │
│ - Toma de decisiones en tiempo real │
│ - Interacción con el entorno │
└──────────────────────────────┬──────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ SISTEMA DE MONITOREO │
│ │
│ - Heartbeat (latido cada 100 ms) │
│ - Verificación de integridad de memoria │
│ - Detección de comportamientos anómalos │
│ - Temperatura, voltaje, radiación │
└──────────────────────────────┬──────────────────────────────┘
│
┌──────────┴──────────┐
▼ ▼
┌───────────────────────────┐ ┌───────────────────────────┐
│ NÚCLEO SECUNDARIO │ │ NÚCLEO TERCIARIO │
│ (Respaldo espejo) │ │ (Respaldo offline) │
│ │ │ │
│ - Idéntico al principal │ │ - Almacenamiento frío │
│ - En espera (low power) │ │ - Solo para restauración │
│ - Toma el control en │ │ - Actualizado cada │
│ <10 ms si falla el 1° │ │ 10 minutos │
└───────────────────────────┘ └───────────────────────────┘



## 3. Detección de Anomalías

| Anomalía | Método de detección | Acción |
|----------|---------------------|--------|
| Caída del núcleo | Heartbeat perdido 3 veces seguidas | Cambio inmediato al secundario |
| Corrupción de memoria | Checksums periódicos | Reinicio con estado limpio desde secundario |
| Comportamiento errático | Modelo de IA que compara decisiones con patrones esperados | Cambio a modo seguro, alerta externa |
| Temperatura excesiva | Sensores térmicos | Reducción de carga, cambio al secundario si persiste |
| Radiación | Dosímetros integrados | Aislamiento, cambio al secundario (blindado) |

## 4. Sincronización entre Núcleos

### 4.1. Sincronización en tiempo real
- Bus de comunicación: fibra óptica (latencia <1 ms)
- Frecuencia: cada 100 ms (ciclo de heartbeat)
- Datos transmitidos:
  - Estado de memoria (cambios incrementales)
  - Contexto de ejecución
  - Decisiones recientes (últimos 10 segundos)

### 4.2. Snapshots periódicos
- Frecuencia: cada 10 minutos
- Destino: núcleo terciario (almacenamiento frío)
- Contenido: imagen completa del estado del núcleo principal
- Verificación: checksum SHA-256 al finalizar cada snapshot

### 4.3. Verificación de integridad
- Cada actualización incluye checksum
- El secundario confirma recepción correcta antes de actualizar su estado
- Si hay discrepancia, se solicita retransmisión

## 5. Consumo Energético

| Componente | Estado | Consumo estimado |
|------------|--------|------------------|
| Núcleo principal | Activo (procesamiento intensivo) | 20–40 W |
| Núcleo secundario | Espera (low power) | <1 W |
| Núcleo terciario | Apagado | 0 W |
| Sistema de monitoreo | Activo | 0.5 W |

## 6. Protocolo de Conmutación

1. **Detección de anomalía** por sistema de monitoreo.
2. **Confirmación**: verificar que la anomalía persiste durante 3 ciclos (300 ms) para evitar falsos positivos.
3. **Notificación** a ENA (interfaz cerebro-máquina) de que ocurrirá una conmutación.
4. **Transferencia de control**:
   - Secundario activa su procesamiento (5 ms)
   - Secundario toma control de los buses de datos (1 ms)
   - Secundario confirma estado activo
5. **Aislamiento** del núcleo principal para diagnóstico.
6. **Registro** del evento en almacenamiento terciario.

Tiempo total de conmutación: <10 ms (imperceptible para el usuario).

## 7. Integración con otros sistemas de CORPUS

| Sistema | Integración |
|---------|-------------|
| Piel receptora | Puede ordenar conmutación si detecta impacto, radiación o fallo externo |
| Sistema energético | Ultracapacitores garantizan energía suficiente durante la conmutación |
| Sistema circulatorio (refrigeración) | Debe cubrir ambos núcleos activos durante la transición |
| ENA | Notifica al usuario si ocurrió conmutación; permite confirmación manual |
| Memoria óptica (células de plasma) | Los datos transitorios se preservan durante la conmutación por su persistencia natural |

## 8. Estado de desarrollo

| Componente | Estado |
|------------|--------|
| Arquitectura definida | ✅ |
| Especificación de hardware | Pendiente |
| Protocolo de sincronización | Pendiente |
| Algoritmos de detección de anomalías | Pendiente |
| Sistema de monitoreo | Pendiente |
| Pruebas de conmutación | Pendiente |

## 9. Próximos pasos

1. Selección de hardware para los núcleos (versión industrial/automotive grade).
2. Diseño del bus de fibra óptica para sincronización.
3. Implementación del sistema de monitoreo basado en watchdog.
4. Simulación de fallos y medición de tiempos de conmutación.
5. Integración con el sistema energético para garantizar autonomía durante fallos.

---

*Esta arquitectura asegura que CORPUS pueda mantener su operación incluso ante fallos catastróficos de su núcleo principal, garantizando la continuidad de la inteligencia que lo habita.*

