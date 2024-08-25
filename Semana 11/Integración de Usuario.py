def menu():
    inventario = Inventario()
    inventario.cargar_de_archivo('inventario.pkl')

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad (dejar en blanco para no cambiar): ") or 0)
            precio = float(input("Nuevo precio (dejar en blanco para no cambiar): ") or 0.0)
            inventario.actualizar_producto(id, cantidad if cantidad else None, precio if precio else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            for producto in resultados:
                print(producto)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            inventario.guardar_en_archivo('inventario.pkl')

        elif opcion == '7':
            inventario.guardar_en_archivo('inventario.pkl')
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor elige de nuevo.")


if __name__ == "__main__":
    menu()
