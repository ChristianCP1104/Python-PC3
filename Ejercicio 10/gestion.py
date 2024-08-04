# gestion.py
from libro import Libro

class GestionBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise TypeError("El argumento debe ser una instancia de la clase Libro.")
        self.libros.append(libro)

    def listar_libros(self):
        if not self.libros:
            return "No hay libros en la biblioteca."
        return "\n".join(str(libro) for libro in self.libros)

    def buscar_por_titulo(self, titulo):
        encontrados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        if not encontrados:
            return "No se encontraron libros con ese título."
        return "\n".join(str(libro) for libro in encontrados)

    def buscar_por_autor(self, autor):
        encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if not encontrados:
            return "No se encontraron libros de ese autor."
        return "\n".join(str(libro) for libro in encontrados)
