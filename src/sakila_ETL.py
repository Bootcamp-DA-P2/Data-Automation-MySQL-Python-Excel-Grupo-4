from sqlalchemy import create_engine, text
from src.config import *
import pandas as pd


BASE_PATH = "output/"
paths = ['client_activity_rental.csv', 'catalog_film.csv', 'global_activity_clients.csv']

query_sql_1 = """
                select
                    LOWER(cu.first_name) AS first_name,
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
                JOIN address ad on cu.address_id = ad.address_id
                JOIN city ci on ci.city_id = ad.city_id
                JOIN country co on ci.country_id = co.country_id
                JOIN rental re on cu.customer_id = re.customer_id
                JOIN payment pa on re.rental_id = pa.rental_id
                WHERE
                    rental_date IS NOT NULL
                    AND return_date IS NOT NULL
                    AND amount > 0
                    AND rental_date < return_date;
            """

sql_query_2 = """
                SELECT 
                    inv.inventory_id,
                    LOWER(TRIM(film.title)) AS title,
                    LOWER(TRIM(cat.name)) AS category,
                    length,
                    rating,
                    LOWER(TRIM(l.name)) AS language,
                    COUNT(DISTINCT inv.inventory_id) AS total_inventory, -- Contamos cuántas copias físicas distintas existen para esta película
                    COUNT(r.rental_id) AS total_rentals -- Contamos cuántas transacciones de alquiler existen en total
                FROM film
                JOIN film_category fcat ON fcat.film_id = film.film_id
                JOIN category cat ON fcat.category_id = cat.category_id
                JOIN language l ON l.language_id = film.language_id
                JOIN inventory inv ON film.film_id = inv.film_id
                JOIN rental r ON inv.inventory_id = r.inventory_id
                GROUP BY 
                    inv.inventory_id,
                    film.title,
                    cat.name,
                    l.name,
                    film.length,
                    film.rating;

"""

sql_query_3 = """
    select
        lower(fi.title) 'Title',
        lower(fi.description) 'Description',
        fi.release_year,
        fi.rating,
        lower(ca.name) as 'Category',
        re.rental_date,
        re.return_date,
        pa.amount,
        pa.payment_date,
        concat(lower(cu.first_name),' ',lower(cu.last_name)) as 'Full Name',
        lower(ci.city) as 'City',
        lower(co.country) as 'Country',
        DATEDIFF(re.return_date, re.rental_date) AS rental_duration
    from customer cu
        join address ad on cu.address_id = ad.address_id
        join city ci on ci.city_id = ad.city_id
        join country co on ci.country_id = co.country_id
        join rental re on cu.customer_id = re.customer_id
        join payment pa on re.rental_id = pa.rental_id
        join inventory inv on re.inventory_id = inv.inventory_id
        join film fi on inv.film_id = fi.film_id
        join film_category fic on fic.film_id = fi.film_id
        join category ca on ca.category_id = fic.category_id
    WHERE
        rental_date IS NOT NULL
        AND return_date IS NOT NULL
        AND amount > 0
        AND rental_date < return_date
    order by
        rental_date asc
    """

queries = [query_sql_1, sql_query_2, sql_query_3]

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

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        

def get_execute_queries(queries, paths):
    conection = conection_bd()
    with conection:
        for i, query in enumerate(queries):
            result = conection.execute(text(query))
            rows = result.fetchall()
            columns = result.keys()

            # 2. Create the Pandas DataFrame
            df = pd.DataFrame(rows, columns=columns)
            
            # --- 3. EXPORTAR A CSV (Paso Nuevo) ---
            df.to_csv(
                BASE_PATH + paths[i], # ruta y Nombre del archivo de salida
                index=False, # Evita escribir el índice del DataFrame en el archivo
                encoding='utf-8' # Asegura que caracteres especiales (como acentos) se guarden bien
            )

            print(f"✅ DataFrame successfully created and saved to: {BASE_PATH + paths[i]}")
