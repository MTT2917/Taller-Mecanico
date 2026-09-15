from dao.dao import Dao

class ModeloDao(Dao):
    """
    Data Access Object para la entidad Modelo.
    Hereda de la clase base Dao para utilizar la conexión y el cursor.
    """
    
    def crear_tabla(self):
        """
        Crea la tabla 'modelos' en la base de datos si no existe.
        La tabla contiene:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - nombre: TEXT NOT NULL
        - marca_id: INTEGER NOT NULL (Clave Foránea hacia marcas.id)
        """
        sql = """
        CREATE TABLE IF NOT EXISTS modelos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            marca_id INTEGER NOT NULL,
            FOREIGN KEY (marca_id) REFERENCES marcas (id)
        )
        """
        self.cursor.execute(sql)
        self.conexion.commit()
