def obtener_calificaciones():
    while True:
        entrada = input("Ingrese una lista de calificaciones separadas por comas: ")
        calificaciones = entrada.split(',')
        calificaciones_enteros = []

        try:
            for calificacion in calificaciones:
                calificacion = calificacion.strip()  # Eliminar espacios en blanco alrededor de cada calificación
                calificacion_entero = int(calificacion)  # Convertir la calificación a entero
                calificaciones_enteros.append(calificacion_entero)

            print("Calificaciones convertidas a enteros:", calificaciones_enteros)
            break

        except ValueError:
            print("Error: Todos los valores deben ser números enteros. Por favor, inténtelo de nuevo.")
            
obtener_calificaciones()
