import time
import random

class Corpus:
    def __init__(self):
        self.energia = 100.0      # %
        self.temperatura = 36.0   # °C
        self.estabilidad = 100.0  # % (equilibrio)
        self.vivo = True

    def homeostasis(self):
        """Regula energía y temperatura automáticamente"""
        # Gasto energético natural
        self.energia -= random.uniform(0.5, 1.5)
        # Pérdida de calor
        self.temperatura -= random.uniform(0.05, 0.15)

        # Si energía baja, activa modo ahorro
        if self.energia < 20:
            print("⚠️ CORPUS: Modo ahorro energético activado")
            self.temperatura += 0.3  # menos refrigeración

        # Si temperatura baja, activa calefacción
        if self.temperatura < 35.0:
            print("🔥 CORPUS: Activando calefacción interna")
            self.temperatura += 0.5

        # Si energía es muy baja, entra en fallback
        if self.energia < 5:
            print("💀 CORPUS: Energía crítica. Entrando en modo fallback.")
            self.vivo = False

        # Limitar rangos
        self.energia = max(0, min(100, self.energia))
        self.temperatura = max(30, min(40, self.temperatura))

    def reflejo_anticaidas(self):
        """Simula un reflejo para mantener el equilibrio"""
        perturbacion = random.uniform(0, 10)
        if perturbacion > 7:
            print("🌀 CORPUS: Detecto pérdida de equilibrio. Ajustando postura.")
            self.estabilidad -= 10
            if self.estabilidad < 50:
                print("🦶 CORPUS: Dando un paso para recuperar equilibrio.")
                self.estabilidad = 80
        else:
            self.estabilidad = min(100, self.estabilidad + 5)

    def estado(self):
        print(f"🔋 Energía: {self.energia:.1f}% | 🌡️ Temp: {self.temperatura:.1f}°C | ⚖️ Estabilidad: {self.estabilidad:.1f}%")

    def ciclo(self, pasos=10):
        for i in range(pasos):
            if not self.vivo:
                print("🛑 CORPUS inactivo. Recarga necesaria.")
                break
            print(f"\n--- Ciclo {i+1} ---")
            self.homeostasis()
            self.reflejo_anticaidas()
            self.estado()
            time.sleep(1)

if __name__ == "__main__":
    print("🧠 CORPUS: Simulación de cuerpo artificial\n")
    robot = Corpus()
    robot.ciclo(pasos=10)
