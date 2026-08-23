class Vehiculo:
    def __init__(self, marca: str, modelo: str, año: int):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    @property
    def marca(self) -> str:
        return self._marca

    @property
    def modelo(self) -> str:
        return self._modelo

    @property
    def año(self) -> int:
        return self._año

    def obtener_informacion(self) -> str:
        """Retorna la información básica del vehículo."""
        return f"{self.marca} {self.modelo} (Año: {self.año})"

    def __str__(self) -> str:
        return self.obtener_informacion()
