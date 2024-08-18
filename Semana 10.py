import os


class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def añadir_producto(self, nombre, cantidad, precio):
        if nombre in self.productos:
            print("El producto ya existe.")
            return
        self.productos[nombre] = Producto(nombre, cantidad, precio)
        self.guardar_en_archivo()
        print(f"Producto '{nombre}' añadido correctamente.")

    def actualizar_producto(self, nombre, cantidad, precio):
        if nombre not in self.productos:
            print("El producto no existe.")
            return
        self.productos[nombre].cantidad = cantidad
        self.productos[nombre].precio = precio
        self.guardar_en_archivo()
        print(f"Producto '{nombre}' actualizado correctamente.")

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_en_archivo()
            print(f"Producto '{nombre}' eliminado correctamente.")
        else:
            print("El producto no existe.")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(str(producto) + "\n")
        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar en archivo: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado, creando nuevo archivo.")
            return

        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[nombre] = Producto(nombre, int(cantidad), float(precio))
        except FileNotFoundError:
            print("Error: Archivo de inventario no encontrado.")
        except PermissionError:
            print("Error: No se tiene permiso para leer el archivo.")
        except Exception as e:
            print(f"Error al cargar desde archivo: {e}")


# Ejemplo de uso
inventario = Inventario()
inventario.añadir_producto("Manzanas", 100, 0.5)
inventario.actualizar_producto("Manzanas", 150, 0.45)
inventario.eliminar_producto("Manzanas")
