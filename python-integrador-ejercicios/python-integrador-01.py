"""
Escribir una función que calcule el máximo común divisor entre dos números.
"""

def mcd(a,b):
    arr_divisores_a = []
    arr_divisores_comunes = []

    for i in range(1, int(a / 2) + 1):
        if ((a % i) == 0):
            arr_divisores_a.append(i)
    arr_divisores_a.append(a)

    for i in range(1, int(b / 2) + 1):
        if ((b % i) == 0):
            if arr_divisores_a.count(i):
                arr_divisores_comunes.append(i)

    return max(arr_divisores_comunes)

def maximo_comun_divisor(a, b):
    if b == 0:
        return a
    return maximo_comun_divisor(b, a % b)

def main():
    a = int(input("a: "))
    b = int(input("b: "))
    print("mcd is: " + str(mcd(a,b)))
    print("maximo comun divisor is: " + str(maximo_comun_divisor(a,b)))

if __name__ == "__main__":
    main()