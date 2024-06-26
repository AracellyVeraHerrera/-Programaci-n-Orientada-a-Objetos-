# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Clase derivada Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)
        self.__numero_puertas = numero_puertas  # Atributo encapsulado

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Número de puertas: {self.__numero_puertas}"

    def get_numero_puertas(self):
        return self.__numero_puertas

    def set_numero_puertas(self, numero_puertas):
        self.__numero_puertas = numero_puertas

# Clase derivada Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Tipo: {self.tipo}"

if __name__ == "__main__":
    # Creación de instancias
    coche = Coche("Toyota", "Corolla", 4)
    moto = Moto("Yamaha", "MT-07", "Deportiva")

    # Uso de los métodos de las clases
    print(coche.mostrar_informacion())
    print("Número de puertas del coche:", coche.get_numero_puertas())

    print(moto.mostrar_informacion())
