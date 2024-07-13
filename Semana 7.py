class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f'Se ha creado el objeto {self.nombre}')

    def __del__(self):
        print(f'Se está destruyendo el objeto {self.nombre}')
        # Aquí podrías realizar tareas de limpieza o cierre de recursos, si es necesario


# Creación de instancias de la clase
objeto1 = MiClase('Objeto1')
objeto2 = MiClase('Objeto2')

# Simulación de eliminación de referencias
del objeto1
del objeto2
