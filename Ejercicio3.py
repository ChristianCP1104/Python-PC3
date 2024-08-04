import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

# Crear dos objetos 
circulo1 = CIRCULO(5)
circulo2 = CIRCULO(10)

# Calcular el área 
area1 = circulo1.calcular_area()
area2 = circulo2.calcular_area()

print(f"El área del círculo con radio {circulo1.radio} es: {area1:.2f}")
print(f"El área del círculo con radio {circulo2.radio} es: {area2:.2f}")
