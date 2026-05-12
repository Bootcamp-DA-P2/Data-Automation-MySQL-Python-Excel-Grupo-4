import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt
from cleaning_methods import *


from cleaning_methods import normalize_string_columns, normalize_date_columns, delete_columns, load_clean_data

def preprocess_first_df(df):
    # Normalización strings
    # Normalización a tipo fecha y string
    df= normalize_date_columns(df)
    df= normalize_string_columns(df)

    # Creación de la columna full_name uniendo el fist_name y el last_name
    df['full_name'] = df['first_name'] + ' ' + df['last_name']

    # Creación de columnas adicionales a partir de las fechas
    df['rental_day'] = df['rental_date'].dt.day
    df['rental_month'] = df['rental_date'].dt.month
    df['rental_year'] = df['rental_date'].dt.year
    df['rental_hour'] = df['rental_date'].dt.hour
    df['return_day'] = df['return_date'].dt.day
    df['return_month'] = df['return_date'].dt.month
    df['return_year'] = df['return_date'].dt.year
    df['return_hour'] = df['return_date'].dt.hour

    # Creación de la columna 'day_of_week_rental' para indicar el día de la semana en el que se realizó el alquiler
    df['day_of_week_rental'] = df['rental_date'].dt.dayofweek + 1

    # Creación de columna 'is_weekend_rental' para indicar si el alquiler se realizó en fin de semana (1) o no (0)
    df['is_weekend_rental'] = df['day_of_week_rental'].apply(lambda x: 1 if x in [6, 7] else 0)

    # Creación de la columna 'season' para indicar la estación del año en el que se realizó el alquiler
    df['season'] = df['rental_month'].apply(lambda x: 'Primavera' if x in [3,4,5] else ('Verano' if x in [6,7,8] else ('Otoño' if x in [9,10,11] else 'Invierno')))

    # Creación de la columna 'part_of_the_day' para indicar el tramo del día en el que se realizó el alquiler
    df['rental_hour_part_of_the_day'] = df['rental_hour'].apply(lambda x: 'Noche' if x in [0,1,2,3,4,5,6] else('Mañana' if x in [7,8,9,10,11,12] else 'Tarde'))

    # Creación de la columna 'part_of_the_day' para indicar el tramo del día en el que se realizó la devolución
    df['return_hour_part_of_the_day'] = df['return_hour'].apply(lambda x: 'Noche' if x in [0,1,2,3,4,5,6] else('Mañana' if x in [7,8,9,10,11,12] else 'Tarde'))

    # Eliminación de las columnas redundantes tras la creación de columnas adicionales a pertir de ellas
    df = delete_columns(df, ['first_name', 'last_name', 'rental_date', 'return_date'])

    # Tratamiento de valores nulos
    df['district'] = df['district'].fillna(
    df.groupby(['city', 'postal_code', 'country'])['district'].transform(
        lambda x: x.mode().iloc[0] if not x.mode().empty else 'missing'
    )
)

    #Seleccionar los nombres de las columnas que son texto
    columns_str = df.select_dtypes("string").columns

    for column in columns_str:
        df[column] = df[column].fillna("missing")

    # Exportación de los datos procesados
    load_clean_data(df, '../output/client-activity-clean.csv')


def preprocess_third_df(df):
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

    # Normalización a tipo fecha y string
    df = normalize_date_columns(df)
    df = normalize_string_columns(df)

    # Creación de columnas adicionales a partir de las fechas
    df['rental_day'] = df['rental_date'].dt.day
    df['rental_month'] = df['rental_date'].dt.month
    df['rental_year'] = df['rental_date'].dt.year
    df['rental_hour'] = df['rental_date'].dt.hour
    df['return_day'] = df['return_date'].dt.day
    df['return_month'] = df['return_date'].dt.month
    df['return_year'] = df['return_date'].dt.year
    df['return_hour'] = df['return_date'].dt.hour

    # Creación de la columna 'day_of_week_rental' para indicar el día de la semana en el que se realizó el alquiler
    df['day_of_week_rental'] = df['rental_date'].dt.dayofweek + 1

    # Creación de columna 'is_weekend_rental' para indicar si el alquiler se realizó en fin de semana (1) o no (0)
    df['is_weekend_rental'] = df['day_of_week_rental'].apply(lambda x: 1 if x in [6, 7] else 0)

    # Creación de la columna 'season' para indicar la estación del año en el que se realizó el alquiler
    df['season'] = df['rental_month'].apply(lambda x: 'spring' if x in [3,4,5] else ('summer' if x in [6,7,8] else ('autumn' if x in [9,10,11] else 'winter')))

    # Creación de la columna 'part_of_the_day' para indicar el tramo del día en el que se realizó el alquiler
    df['rental_hour_part_of_the_day'] = df['rental_hour'].apply(lambda x: 'night' if x in [0,1,2,3,4,5,6] else('morning' if x in [7,8,9,10,11,12] else 'afternoon'))

    # Creación de la columna 'part_of_the_day' para indicar el tramo del día en el que se realizó la devolución
    df['return_hour_part_of_the_day'] = df['return_hour'].apply(lambda x: 'night' if x in [0,1,2,3,4,5,6] else('morning' if x in [7,8,9,10,11,12] else 'afternoon'))

    # Creación de la columna 'payment_lag' para indicar el tiempo transcurrido entre la fecha de alquiler y la fecha de pago. Lo ideal es que sea 0,
    # pero puede haber casos en los que el pago se realice después del alquiler. Sirve para detectar posibles anomalías
    df['payment_lag'] = df['payment_date'].dt.day - df['rental_date'].dt.day

    # Creación de la columna 'film_age' para indicar la antigüedad de la película desde su año de lanzamiento.
    df['film_age'] = dt.now().year - df['release_year']

    # Creación de la columna 'is_adult_content' para indicar si la película es para adultos o no, basándonos en su clasificación por edades
    df['is_adult_content'] = df['rating'].apply(lambda x: 1 if x in ['R', 'NC-17'] else 0)

    # Eliminación de las columnas redundantes tras la creación de columnas adicionales a pertir de ellas
    df = delete_columns(df, ['release_year', 'rental_date', 'return_date'])

    # Exportación de los datos procesados
    load_clean_data(df, '../output/global_activity_clients_clean.csv')
    load_clean_data(df, '../output/client-activity-clean.csv')



def preprocess_second_df(path):
    #Carga de datos
    df_original = charge_path(path)
    df = df_original.copy()

    # Normalización a tipo fecha y string
    normalize_date_columns(df)
    normalize_string_columns(df)

    # Eliminación de columnas innecesarias
    delete_columns(df, ['language'])

    #Identificación de nulos
    identify_nulls(df)

    #Identificación de otulaiers
    columns_numeric = df.select_dtypes("number").columns
    columns_categorical = df.select_dtypes("object").columns

    identify_outliers(df, columns_numeric, columns_categorical)

    #Exportación de datos limpios
    load_clean_data(df, '../output/catalog_film_clean.csv')
