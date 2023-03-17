"""
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
Escribir otra función que reciba el diccionario generado con la función anterior y devuelva
una tupla con la palabra más repetida y su frecuencia.
"""

def higher_frequency(d):
    higher = 0
    key = ''
    for k in d:
        d_value = d[k]
        if d_value > higher:
            higher = d_value
            key = k

    return (key, d[key])

def string_to_dict(s):

    _dict = {}
    s_list = s.split()

    try:
        for c in s_list:
            if c in _dict.keys():
                _dict[c] += 1
            else:
                _dict[c] = 1
    except:
        print("Ocurrio un error")

    return _dict

def main():
    s = input("Ingrese cadena: ")
    s_dict = string_to_dict(s)
    print(type(s_dict))
    print(s_dict)
    s_tuple = higher_frequency(s_dict)
    print(type(s_tuple))
    print(s_tuple)

if __name__ == "__main__":
    main()