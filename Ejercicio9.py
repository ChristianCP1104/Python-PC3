# menu.py
from Ejercicio3 import CIRCULO
from Ejercicio4 import RECTANGULO, CUADRADO

def obtener_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: El valor debe ser positivo.")
        except ValueError:
            print("Error: Entrada no válida. Por favor ingresa un número.")

def calcular_area_circulo():
    radio = obtener_numero_positivo("Ingrese el radio del círculo: ")
    circulo = CIRCULO(radio)
    print(f"El área del círculo con radio {circulo.radio} es: {circulo.calcular_area():.2f}")

def calcular_area_rectangulo():
    largo = obtener_numero_positivo("Ingrese el largo del rectángulo: ")
    ancho = obtener_numero_positivo("Ingrese el ancho del rectángulo: ")
    rectangulo = RECTANGULO(largo, ancho)
    print(f"El área del rectángulo con largo {rectangulo.largo} y ancho {rectangulo.ancho} es: {rectangulo.calcular_area()}")

def calcular_area_cuadrado():
    lado = obtener_numero_positivo("Ingrese el lado del cuadrado: ")
    cuadrado = CUADRADO(lado)
    print(f"El área del cuadrado con lado {cuadrado.largo} es: {cuadrado.calcular_area()}")

def mostrar_menu():
    while True:
        print("\nMenú de Cálculo de Áreas")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Error: Opción no válida. Por favor seleccione una opción entre 1 y 4.")

if __name__ == "__main__":
    mostrar_menu()
