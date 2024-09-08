class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self._titulo_autor = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self):
        return self._titulo_autor[0]

    @property
    def autor(self):
        return self._titulo_autor[1]

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}, Categoría: {self.categoria})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de objetos Libro

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.ids_usuarios = set()  # Conjunto para asegurarse de que los IDs sean únicos

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print(f"El ID de usuario {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            del self.libros[isbn]  # Eliminar el libro de la colección disponible
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print(f"No se pudo prestar el libro. Verifique el ID de usuario y el ISBN.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    self.libros[isbn] = libro
                    usuario.devolver_libro(isbn)
                    print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                    return
            print(f"El usuario no tiene prestado un libro con ISBN {isbn}.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo and titulo.lower() in libro.titulo.lower()) or \
                    (autor and autor.lower() in libro.autor.lower()) or \
                    (categoria and categoria.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return []


# Ejemplo de uso

# Crear algunos libros
libro1 = Libro("1984", "George Orwell", "Ficción", "123456789")
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", "Infantil", "987654321")

# Crear usuarios
usuario1 = Usuario("Alice", "U001")
usuario2 = Usuario("Bob", "U002")

# Crear la biblioteca
biblioteca = Biblioteca()

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("U001", "123456789")
biblioteca.devolver_libro("U001", "123456789")

# Buscar libros
resultados = biblioteca.buscar_libro(titulo="1984")
for libro in resultados:
    print(libro)

# Listar libros prestados
prestados = biblioteca.listar_libros_prestados("U001")
for libro in prestados:
    print(libro)