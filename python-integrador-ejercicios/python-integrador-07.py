"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales).
El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
• mostrar(): Muestra los datos de la cuenta.
• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""

class Persona:
    
    def __init__(self, nombre = None, apellido = None, edad = None, dni = None) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__dni = dni

    def __str__(self):
        return print(f'Nombre: {self.__nombre}, Apellido: {self.__apellido}')
    
    @property
    def get_nombre(self) -> str:
        return self.__nombre
    
    @property
    def get_apellido(self) -> str:
        return self.__apellido
    
    @property
    def get_edad(self) -> int:
        return self.__edad
    
    @property
    def get_dni(self) -> int:
        return self.__dni
    
    @get_nombre.setter
    def set_nombre(self,nombre: str):
        try:
            if nombre:
                self.__nombre = nombre
        except TypeError:
            return print(f'Persona.set_nombre(): valor no válido.')
        except:
            return print(f'Persona.set_nombre(): Ocurrió un error inesperado.')

    @get_apellido.setter
    def set_apellido(self,apellido: str):
        try:
            if apellido:
                self.__apellido = apellido
        except TypeError:
            return print(f'Persona.set_apellido(): valor no válido.')
        except:
            return print(f'Persona.set_apellido(): Ocurrió un error inesperado.')
    
    @get_edad.setter
    def set_edad(self,edad: int):
        try:
            if edad >= 0:
                self.__edad = edad
        except TypeError:
            return print(f'Persona.set_edad(): valor no válido.')
        except:
            return print(f'Persona.set_edad(): Ocurrió un error inesperado.')

    @get_dni.setter
    def set_dni(self,dni: int):
        try:
            if dni > 0:
                self.__dni = dni
        except TypeError:
            return print(f'Persona.set_dni(): valor no válido.')
        except:
            return print(f'Persona.set_dni(): Ocurrió un error inesperado.')
    
    def mostrar(self):
        return print(f'Nombre: {self.__nombre}, Apellido: {self.__apellido}, Edad: {self.__edad}, DNI: {self.__dni}')
    
    def es_mayor_de_edad(self) -> bool:
        try:
            if self.__edad > 18:
                return True
        except TypeError:
            return print(f'Persona.es_mayor_de_edad(): valor no válido.')
        except:
            return print(f'Persona.es_mayor_de_edad(): Ocurrió un error inesperado.')
        else:
            return False
        
class Cuenta:

    def __init__(self,titular: Persona = None, cantidad: float = None) -> None:
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def get_titular(self) -> Persona:
        return self.__titular
    
    @property
    def get_cantidad(self) -> float:
        return self.__cantidad
    
    @get_titular.setter
    def set_titular(self, p: Persona) -> None:
        self.__titular = p

    @get_cantidad.setter
    def set_nombre(self, cantidad: float) -> float:
        self.__cantidad = cantidad

    def ingresar(self,cantidad: float) -> float:
        try:
            self.__cantidad += cantidad
        except ValueError:
            return print(f'Cuenta.ingresar(): valor no válido.')
        except:
            return print(f'Cuenta.ingresar(): Ocurrió un error inesperado.')
        else:
            return self.__cantidad
        
    def retirar(self,cantidad: float) -> float:
        try:
            self.__cantidad -= cantidad
        except ValueError:
            return print(f'Cuenta.retirar(): valor no válido.')
        except:
            return print(f'Cuenta.retirar(): Ocurrió un error inesperado.')
        else:
            return self.__cantidad
        
    def mostrar(self) -> str:
        return print(f'{self.__titular.__str__}, Saldo: {self.__cantidad}')

def main():
    pass

if __name__ == "__main__":
    main()