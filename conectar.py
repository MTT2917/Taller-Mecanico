import sqlite3

def crear_conexion():
    """
    Crea y retorna una conexión a la base de datos SQLite 'taller.db'.
    Habilita el uso de Foreign Keys (claves foráneas) por defecto.
    """
    conexion = sqlite3.connect("taller.db")
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion
