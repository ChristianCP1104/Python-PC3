class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = None

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas is not None:
            print(f"Notas: {self.notas}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        self.notas = notas

# Crear un objeto de tipo Alumno
alumno1 = Alumno("Nataly Bejarano", "C332001")

# Asignar la edad y las notas al Alumno
alumno1.setAge(24)
alumno1.setNota([20, 19, 34])

# Mostrar la información del estudiante
alumno1.display()
