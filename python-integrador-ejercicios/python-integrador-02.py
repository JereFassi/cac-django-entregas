"""
Escribir una función que calcule el mínimo común múltiplo entre dos números.
"""

def minimo_comun_multiplo(a,b):
    return (a * b) / maximo_comun_divisor(a, b)

def maximo_comun_divisor(a, b):
    if b == 0:
        return a
    return maximo_comun_divisor(b, a % b)

def main():
    a = int(input("a: "))
    b = int(input("b: "))
    print("maximo comun divisor es: " + str(maximo_comun_divisor(a,b)))
    print("minimo comun multiplo es: " + str(int(minimo_comun_multiplo(a,b))))

if __name__ == "__main__":
    main()