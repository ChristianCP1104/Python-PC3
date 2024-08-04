# calculos.py

import operaciones8

def main():
    # Pruebas de las funciones
    print("Suma:")
    print(operaciones8.suma(10, 5))          # Debería imprimir 15
    print(operaciones8.suma(10, "5"))        # Debería imprimir "Error: Tipo de dato no válido."

    print("\nResta:")
    print(operaciones8.resta(10, 5))         # Debería imprimir 5
    print(operaciones8.resta(10, "5"))       # Debería imprimir "Error: Tipo de dato no válido."

    print("\nProducto:")
    print(operaciones8.producto(10, 5))      # Debería imprimir 50
    print(operaciones8.producto(10, "5"))    # Debería imprimir "Error: Tipo de dato no válido."

    print("\nDivisión:")
    print(operaciones8.division(10, 2))      # Debería imprimir 5.0
    print(operaciones8.division(10, 0))      # Debería imprimir "Error: No es posible dividir entre cero."
    print(operaciones8.division(10, "2"))    # Debería imprimir "Error: Tipo de dato no válido."

if __name__ == "__main__":
    main()