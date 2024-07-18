import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def agregar_script(opciones):
    nombre_script = input("Ingrese el nombre del nuevo script (con la ruta relativa desde la base): ")
    clave_opcion = str(len(opciones) + 1)
    opciones[clave_opcion] = nombre_script
    print(f"Script agregado con éxito: {clave_opcion} - {nombre_script}")


def eliminar_script(opciones):
    clave_opcion = input("Ingrese el número del script que desea eliminar: ")
    if clave_opcion in opciones:
        del opciones[clave_opcion]
        print("Script eliminado con éxito.")
    else:
        print("Opción no válida.")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        # Agrega aquí el resto de las rutas de los scripts
        '2': 'Unidad 2/2.1. Mas Tecnicas/2.1-1. Otro Ejemplo.py'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")
        print("A - Agregar nuevo script")
        print("E - Eliminar un script")

        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        elif eleccion == 'A':
            agregar_script(opciones)
        elif eleccion == 'E':
            eliminar_script(opciones)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()