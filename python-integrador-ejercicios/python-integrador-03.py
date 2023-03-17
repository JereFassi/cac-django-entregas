"""
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
"""

def string_to_dict(s):

    word_dict = {}
    s_list = s.split()

    try:
        for c in s_list:
            if c in word_dict.keys():
                word_dict[c] += 1
            else:
                word_dict[c] = 1
    except:
        print("Ocurrio un error")

    return word_dict

def main():
    s = input("Ingrese cadena: ")
    print(string_to_dict(s))

if __name__ == "__main__":
    main()