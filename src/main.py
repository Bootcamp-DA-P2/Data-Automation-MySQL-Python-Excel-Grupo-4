from sqlalchemy import create_engine, text
from config import *
import pandas as pd



# Create a database connection
def conection_bd():
    """Crear conexión a la base de datos"""
    # 1. Construir la URL de conexión completa
    url_db = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    # 2. Crear el objeto 'motor' (engine) usando la URL
    engine = create_engine(url_db)
    return engine.connect()


def test_connection():
    """Probar la conexión a la base de datos"""
    connection = conection_bd()
    try:
        with connection:
            print("Conexión exitosa a la base de datos.")
            result = connection.execute(text("SELECT * FROM birds;"))
            print(result.fetchone())

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        

def get_data_list_from_join():
    """Obtener datos de la unión de tablas birds, locations y species"""
    connection = conection_bd()
    with connection:
        join_query_sql = """ 
                            SELECT
                                sightings.date,
                                sightings.count,
                                birds.common_name AS species,
                                parks.name AS park,
                                parks.district AS district
                            FROM
                                sightings
                            JOIN
                                birds ON sightings.bird_id = birds.id
                            JOIN
                                parks ON sightings.park_id = parks.id;"""
    
        result = connection.execute(text(join_query_sql))
        rows = result.fetchall()
        columns = result.keys()

            # 2. Create the Pandas DataFrame
        df = pd.DataFrame(rows, columns=columns)
            
            # --- 3. EXPORTAR A CSV (Paso Nuevo) ---
        df.to_csv(
                "data/madrid_bird_sightings.csv", # ruta y Nombre del archivo de salida
                index=False, # Evita escribir el índice del DataFrame en el archivo
                encoding='utf-8' # Asegura que caracteres especiales (como acentos) se guarden bien
        )

        print(f"✅ DataFrame successfully created and saved to: {'data/madrid_bird_sightings.csv'}")

        return df
        
if __name__ == "__main__":
    test_connection()
    get_data_list_from_join()