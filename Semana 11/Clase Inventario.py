import pickle

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print(f"El producto con ID {producto.get_id()} ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print(f"Producto {producto.get_nombre()} añadido al inventario.")

    def eliminar_producto(self, id):
        if id in self.productos:
            eliminado = self.productos.pop(id)
            print(f"Producto {eliminado.get_nombre()} eliminado del inventario.")
        else:
            print(f"No se encontró un producto con ID {id}.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)
            print(f"Producto {id} actualizado.")
        else:
            print(f"No se encontró un producto con ID {id}.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if p.get_nombre() == nombre]
        return resultados

    def mostrar_todos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'wb') as file:
            pickle.dump(self.productos, file)
        print(f"Inventario guardado en {archivo}.")

    def cargar_de_archivo(self, archivo):
        try:
            with open(archivo, 'rb') as file:
                self.productos = pickle.load(file)
            print(f"Inventario cargado desde {archivo}.")
        except FileNotFoundError:
            print(f"No se encontró el archivo {archivo}.")
