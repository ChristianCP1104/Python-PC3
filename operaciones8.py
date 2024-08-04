# operaciones Ejercicio8.py

def suma(a, b):
    try:
        # Verificamos que a y b sean números (int o float)
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Error: Tipo de dato no válido.")
        return a + b
    except ValueError as e:
        return str(e)

def resta(a, b):
    try:
        # Verificamos que a y b sean números (int o float)
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Error: Tipo de dato no válido.")
        return a - b
    except ValueError as e:
        return str(e)

def producto(a, b):
    try:
        # Verificamos que a y b sean números (int o float)
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Error: Tipo de dato no válido.")
        return a * b
    except ValueError as e:
        return str(e)

def division(a, b):
    try:
        # Verificamos que a y b sean números (int o float)
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Error: Tipo de dato no válido.")
        # Verificamos si el denominador es cero
        if b == 0:
            raise ZeroDivisionError("Error: No es posible dividir entre cero.")
        return a / b
    except ValueError as e:
        return str(e)
    except ZeroDivisionError as e:
        return str(e)
