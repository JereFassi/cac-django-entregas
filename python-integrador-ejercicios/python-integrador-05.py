"""
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
"""

def get_int_iterativo():
    user_input_ok = False
    while not user_input_ok:
        try:
            user_input = int(input("Ingrese un número entero: "))
            user_input_ok = True
        except ValueError:
            print("Valor no numérico, intente nuevamente...")
        else:
            return user_input
    
def get_int_recursivo():
    try:
        user_input = int(input("Ingrese un número entero: "))
    except ValueError:
        print("Valor no numérico, intente nuevamente...")
        return get_int_recursivo()
    else:
        return user_input

def main():
    value = get_int_iterativo()
    print("Funcion iterativa - Valor ingresado: ", value)

    value = get_int_recursivo()
    print("Funcion recursiva - Valor ingresado: ", value)

if __name__ == "__main__":
    main()