class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

# Crear los objetos (RECTANGULO y CUADRADO)
rectangulo = RECTANGULO(10, 5)
cuadrado = CUADRADO(4)

# Calcular el área del rectángulo y del cuadrado
area_rectangulo = rectangulo.calcular_area()
area_cuadrado = cuadrado.calcular_area()

print(f"El área del rectángulo con largo {rectangulo.largo} y ancho {rectangulo.ancho} es: {area_rectangulo}")
print(f"El área del cuadrado con lado {cuadrado.largo} es: {area_cuadrado}")
