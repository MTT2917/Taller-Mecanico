import conectar
from dao.marca_dao import MarcaDao
from dao.modelo_dao import ModeloDao
from dao.auto_dao import AutoDao

def main():
    print("--- Inicializando Base de Datos ---")
    
    # 1. Crear conexión
    conn = conectar.crear_conexion()
    
    # 2. Instanciar los DAOs pasándoles la conexión
    marca_dao = MarcaDao(conn)
    modelo_dao = ModeloDao(conn)
    auto_dao = AutoDao(conn)
    
    # 3. Crear las tablas
    # Nota: auto_dao.crear_tabla() creará 'vehiculos' y luego 'autos'
    print("Creando tablas...")
    marca_dao.crear_tabla()
    modelo_dao.crear_tabla()
    auto_dao.crear_tabla()
    
    # 4. Validar que las tablas existan en la BD
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tablas_creadas = [fila[0] for fila in cursor.fetchall()]
    
    print("\n--- Tablas encontradas en la Base de Datos ---")
    for tabla in tablas_creadas:
        # Excluimos la tabla interna de SQLite
        if tabla != "sqlite_sequence":
            print(f"- {tabla}")
    
    print("\nProceso finalizado exitosamente.")

if __name__ == "__main__":
    main()
