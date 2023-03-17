"""
Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
• mostrar(): Muestra los datos de la persona.
• es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
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
    
def main():
    p1 = Persona()
    print(p1.get_nombre())
    p1.set_nombre("Homero")
    p1.set_apellido("Simpson")
    p1.set_edad(45)
    print(p1.mostrar())
    print(p1.es_mayor_de_edad())

    p2 = Persona("Bart", "Simpron", 12)
    print(p2.mostrar())
    print(p2.es_mayor_de_edad())

if __name__ == "__main__":
    main()