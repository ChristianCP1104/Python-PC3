# main.py
from gestion import GestionBiblioteca
from libro import Libro

def obtener_input(mensaje):
    return input(mensaje).strip()

def menu():
    gestion = GestionBiblioteca()

    while True:
        print("\nMenú de Gestión de Biblioteca")
        print("1. Agregar un libro a la biblioteca")
        print("2. Listar los libros en la biblioteca")
        print("3. Buscar un libro por título")
        print("4. Buscar un libro por autor")
        print("5. Salir")

        opcion = obtener_input("Seleccione una opción (1-5): ")

        if opcion == '1':
            titulo = obtener_input("Ingrese el título del libro: ")
            autor = obtener_input("Ingrese el autor del libro: ")
            isbn = obtener_input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(libro)
            print("Libro agregado exitosamente.")

        elif opcion == '2':
            print("\nLibros en la biblioteca:")
            print(gestion.listar_libros())

        elif opcion == '3':
            titulo = obtener_input("Ingrese el título del libro que desea buscar: ")
            print("\nResultados de búsqueda por título:")
            print(gestion.buscar_por_titulo(titulo))

        elif opcion == '4':
            autor = obtener_input("Ingrese el autor del libro que desea buscar: ")
            print("\nResultados de búsqueda por autor:")
            print(gestion.buscar_por_autor(autor))

        elif opcion == '5':
            print("¡Hasta luego!")
            break

        else:
            print("Error: Opción no válida. Por favor seleccione una opción entre 1 y 5.")

if __name__ == "__main__":
    menu()
