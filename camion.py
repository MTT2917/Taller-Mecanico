from vehiculo import Vehiculo # Importa la clase Vehiculo desde el archivo vehiculo.py


class Camion(Vehiculo): # Define la clase Camion que hereda de la clase padre Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_carga: int): # Constructor que recibe patente, año y capacidad de carga en kilos
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo para inicializar patente y año
        self.__capacidad_carga: int = capacidad_carga # Guarda la capacidad de carga recibida como un atributo privado
