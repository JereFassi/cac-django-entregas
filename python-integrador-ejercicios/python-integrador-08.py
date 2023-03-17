"""
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
• Un constructor.
• Los setters y getters para el nuevo atributo.
• En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
• Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
• El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
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
    
class CuentaJoven(Cuenta):
    
    def __init__(self, titular: Persona = None, cantidad: float = None, bonificacion: int = None) -> None:
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def get_bonificacion(self) -> int:
        return self.__bonificacion
    
    @get_bonificacion.setter
    def set_titular(self, bonificacion: int) -> None:
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        try:
            if self.__titular.es_mayor_de_edad():
                if self.__titular.get_edad() < 25:
                    return True
        except:
            return print(f'CuentaJoven.es_titular_valido(): Ocurrio un error.')
        else:
            return False
        
    def retirar(self, cantidad: float) -> float:
        try:
            if self.es_titular_valido():
                return super().retirar(cantidad)
        except:
            return print(f'CuentaJoven.retirar(): Ocurrio un error.')
    
    def mostrar(self) -> str:
        # super().mostrar()
        return print(f'Cuenta Joven. Bonificacion: {self.__bonificacion}')

def main():
    pass

if __name__ == "__main__":
    main()