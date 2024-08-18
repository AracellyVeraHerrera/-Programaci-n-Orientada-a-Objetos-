class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        for prod in self.productos:
            if prod.get_id_producto() == producto.get_id_producto():
                print(f"El producto con ID {producto.get_id_producto()} ya existe.")
                return
        self.productos.append(producto)
        print(f"Producto {producto.get_nombre()} añadido al inventario.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                self.productos.remove(producto)
                print(f"Producto con ID {id_producto} eliminado.")
                return
        print(f"No se encontró ningún producto con ID {id_producto}.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print(f"Producto con ID {id_producto} actualizado.")
                return
        print(f"No se encontró ningún producto con ID {id_producto}.")

    def buscar_producto(self, nombre):
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if resultados:
            for prod in resultados:
                print(prod.mostrar_info())
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto.mostrar_info())
