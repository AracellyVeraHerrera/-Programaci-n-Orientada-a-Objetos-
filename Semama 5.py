# calculo_area_circulo.py
# Este programa calcula el área de un círculo dado su radio.

import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Args:
    radio (float): El radio del círculo.

    Returns:
    float: El área del círculo.
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * radio ** 2

def main():
    """
    Función principal del programa.
    """
    try:
        radio = float(input("Introduce el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} es {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()