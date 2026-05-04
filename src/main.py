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
            result = connection.execute(text("SELECT * FROM sakila;"))
            print(result.fetchone())

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        

def get_data_list_from_join_activity_clients():
    """Obtener datos de la unión de tablas birds, locations y species"""
    connection = conection_bd()
    with connection:
        join_query_sql = """
                            select
                                LOWER(cu.first_name) AS firt_name,
                                LOWER(cu.last_name) AS last_name,
                                LOWER(cu.email) AS email,
                                cu.active,
                                LOWER(ad.address) AS address,
                                LOWER(ad.district) AS district,
                                ad.postal_code, 
                                ad.phone,
                                LOWER(ci.city) AS city,
                                LOWER(co.country) AS country,
                                re.rental_date,
                                re.return_date,
                                pa.amount,
                                pa.payment_date,
                                DATEDIFF(re.return_date, re.rental_date) AS rental_duration
                            from customer cu
                            JOIN 
                                address ad on cu.address_id = ad.address_id
                            JOIN 
                                city ci on ci.city_id = ad.city_id
                            JOIN 
                                country co on ci.country_id = co.country_id
                            JOIN 
                                rental re on cu.customer_id = re.customer_id
                            JOIN 
                                payment pa on re.rental_id = pa.rental_id
                            WHERE
                                rental_date IS NOT NULL
                                AND return_date IS NOT NULL
                                AND amount > 0
                                AND rental_date < return_date;
                            """
    
        result = connection.execute(text(join_query_sql))
        rows = result.fetchall()
        columns = result.keys()

            # 2. Create the Pandas DataFrame
        df = pd.DataFrame(rows, columns=columns)
            
            # --- 3. EXPORTAR A CSV (Paso Nuevo) ---
        df.to_csv(
                "data/sakila.csv", # ruta y Nombre del archivo de salida
                index=False, # Evita escribir el índice del DataFrame en el archivo
                encoding='utf-8' # Asegura que caracteres especiales (como acentos) se guarden bien
        )

        print(f"✅ DataFrame successfully created and saved to: {'data/sakila.csv'}")

        return df
        
if __name__ == "__main__":
    test_connection()
    get_data_list_from_join_activity_clients()