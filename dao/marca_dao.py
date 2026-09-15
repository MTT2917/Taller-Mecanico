from dao.dao import Dao

class MarcaDao(Dao):
    """
    Data Access Object para la entidad Marca.
    Hereda de la clase base Dao para utilizar la conexión y el cursor.
    """
    
    def crear_tabla(self):
        """
        Crea la tabla 'marcas' en la base de datos si no existe.
        La tabla contiene:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - nombre: TEXT NOT NULL
        """
        sql = """
        CREATE TABLE IF NOT EXISTS marcas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
        """
        self.cursor.execute(sql)
        self.conexion.commit()
