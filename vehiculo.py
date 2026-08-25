class Vehiculo:
    def __init__(self, patente: str, anio: int):
        self.patente: str = patente
        self.anio: int = anio
        self.__en_taller: bool = False
