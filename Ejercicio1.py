def get_fraction():
    while True:
        try:
            fraction = input("Ingrese una fracción (X/Y): ")
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            
            if x > y or y == 0:
                raise ValueError("X debe ser menor o igual a Y y Y no puede ser 0.")
            
            percentage = (x / y) * 100
            
            if percentage < 1:
                print("E")
            elif percentage > 99:
                print("F")
            else:
                print(f"{round(percentage)}%")
            break
        
        except ValueError:
            print("Entrada inválida. Por favor, asegúrese de que X e Y sean números enteros y que X sea menor o igual a Y y Y no sea 0.")
        except ZeroDivisionError:
            print("Y no puede ser 0. Por favor, ingrese nuevamente la fracción.")

get_fraction()
