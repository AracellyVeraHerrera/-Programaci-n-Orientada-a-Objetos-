class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura para el día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Función principal
def main():
    print("Programa para calcular el promedio semanal del clima.")
    clima_diario = ClimaDiario()
    clima_diario.ingresar_temperaturas()
    promedio = clima_diario.calcular_promedio_semanal()
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
