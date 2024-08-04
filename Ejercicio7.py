import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.y == 0 and self.x != 0:
            return "Sobre el eje X"
        else:
            return "En el origen"

    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

class Rectangulo:
    def __init__(self, punto1=None, punto2=None):
        if punto1 is None:
            punto1 = Punto()
        if punto2 is None:
            punto2 = Punto()
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()

# Crear objetos de tipo Punto
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Imprimir puntos por pantalla
print(f"Punto A: {A}")
print(f"Punto B: {B}")
print(f"Punto C: {C}")
print(f"Punto D: {D}")

# Consultar a qué cuadrante pertenecen los puntos A, C y D
print(f"Cuadrante de A: {A.cuadrante()}")
print(f"Cuadrante de C: {C.cuadrante()}")
print(f"Cuadrante de D: {D.cuadrante()}")

# Consultar los vectores AB y BA
vector_AB = A.vector(B)
vector_BA = B.vector(A)
print(f"Vector AB: {vector_AB}")
print(f"Vector BA: {vector_BA}")

# Consultar la distancia entre los puntos A y B, y B y A
distancia_AB = A.distancia(B)
distancia_BA = B.distancia(A)
print(f"Distancia entre A y B: {distancia_AB:.2f}")
print(f"Distancia entre B y A: {distancia_BA:.2f}")

# Determinar cuál de los puntos A, B o C se encuentra más lejos del origen
distancia_A_origen = A.distancia(D)
distancia_B_origen = B.distancia(D)
distancia_C_origen = C.distancia(D)

distancias = {'A': distancia_A_origen, 'B': distancia_B_origen, 'C': distancia_C_origen}
punto_mas_lejos = max(distancias, key=distancias.get)
print(f"El punto más lejos del origen es: {punto_mas_lejos}")

# Crear un rectángulo utilizando los puntos A y B
rect = Rectangulo(A, B)

# Consultar la base, altura y área del rectángulo
print(f"Base del rectángulo: {rect.base()}")
print(f"Altura del rectángulo: {rect.altura()}")
print(f"Área del rectángulo: {rect.area()}")
