# reserva_hotel.py

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero}: Tipo {self.tipo}, Precio {self.precio}, Estado: {estado}"

class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias
        self.total = self.calcular_total()

    def calcular_total(self):
        return self.habitacion.precio * self.dias

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} en {self.habitacion.tipo} por {self.dias} días. Total: {self.total}"

# Creación de objetos
cliente1 = Cliente("Juan Pérez", "juan.perez@example.com")
habitacion1 = Habitacion(101, "Sencilla", 50)

# Realizar reserva
reserva1 = Reserva(cliente1, habitacion1, 3)
print(reserva1)