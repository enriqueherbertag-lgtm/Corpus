"""
Simulación de flujo energético de CORPUS en Gazebo
Modelo de consumo según modo de operación
"""

import matplotlib.pyplot as plt
import numpy as np

# Parámetros
battery_capacity = 7200  # Wh
ultracap_capacity = 500  # Wh

# Consumo por modo (W)
modes = {
    "reposo": 15,
    "familia": 75,
    "exploracion": 40,
    "proteccion": 150
}

# Captura ambiental (W)
ambient_capture = {
    "rf": 0.5,
    "termica": 1.0,
    "total": 1.5
}

# Simulación de 30 días en modo reposo
days = 30
hours = days * 24
time = np.arange(0, hours, 1)

# Escenario: 20 días reposo, 5 días familia, 3 días exploración, 2 días protección
scenario = [modes["reposo"]] * (20*24) + [modes["familia"]] * (5*24) + [modes["exploracion"]] * (3*24) + [modes["proteccion"]] * (2*24)
scenario = scenario[:hours]  # Asegurar longitud

# Energía consumida
energy_consumed = np.cumsum(scenario) / 1000  # kWh

# Energía capturada (constante)
energy_captured = np.cumsum([ambient_capture["total"]] * hours) / 1000  # kWh

# Energía restante en batería
battery_initial = battery_capacity / 1000  # kWh
battery_remaining = battery_initial - (energy_consumed - energy_captured)
battery_remaining = np.maximum(battery_remaining, 0)

# Gráfico
plt.figure(figsize=(12, 6))
plt.plot(time / 24, battery_remaining, label="Energía restante (kWh)", color="blue")
plt.axhline(y=0, color="red", linestyle="--", label="Límite crítico")
plt.xlabel("Días")
plt.ylabel("Energía (kWh)")
plt.title("Simulación de consumo energético - CORPUS")
plt.legend()
plt.grid(True)
plt.savefig("energy_simulation.png", dpi=150)
plt.show()

print(f"Energía inicial: {battery_initial} kWh")
print(f"Energía total consumida: {energy_consumed[-1]:.1f} kWh")
print(f"Energía capturada: {energy_captured[-1]:.1f} kWh")
print(f"Energía restante: {battery_remaining[-1]:.1f} kWh")
