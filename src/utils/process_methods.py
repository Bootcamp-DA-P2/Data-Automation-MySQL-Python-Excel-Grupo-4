import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt
from src.utils.cleaning_methods import charge_path, normalize_string_columns, normalize_date_columns, delete_columns, load_clean_data

def preprocess_first_df(path):
    # Carga de datos 
    df = charge_path(path)
    
    # Normalización 
    df = normalize_date_columns(df)
    df = normalize_string_columns(df)

    # Creación de full_name
    df['full_name'] = df['first_name'] + ' ' + df['last_name']

    # Eliminación de las columnas redundantes tras la creación de columnas adicionales a pertir de ellas
    df = delete_columns(df, ['first_name', 'last_name'])

    df['district'] = df['district'].fillna(
    df.groupby(['city', 'postal_code', 'country'])['district'].transform(
        lambda x: x.mode().iloc[0] if not x.mode().empty else 'missing'
        )
    )

    load_clean_data(df, 'output/client_activity_clean.csv')

def preprocess_third_df(path):
    df = charge_path(path)
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

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
    df['season'] = df['rental_month'].apply(lambda x: 'Spring' if x in [3,4,5] else ('Summer' if x in [6,7,8] else ('Autumn' if x in [9,10,11] else 'Winter')))

    # Creación de la columna 'part_of_the_day' para indicar el tramo del día en el que se realizó el alquiler
    df['rental_hour_part_of_the_day'] = df['rental_hour'].apply(lambda x: 'Night' if x in [0,1,2,3,4,5,6] else('Morning' if x in [7,8,9,10,11,12] else 'Afternoon'))

    # Creación de la columna 'part_of_the_day' para indicar el tramo del día en el que se realizó la devolución
    df['return_hour_part_of_the_day'] = df['return_hour'].apply(lambda x: 'Night' if x in [0,1,2,3,4,5,6] else('Morning' if x in [7,8,9,10,11,12] else 'Afternoon'))

    # Creación de la columna 'payment_lag' para indicar el tiempo transcurrido entre la fecha de alquiler y la fecha de pago. Lo ideal es que sea 0,
    # pero puede haber casos en los que el pago se realice después del alquiler. Sirve para detectar posibles anomalías
    df['payment_lag'] = df['payment_date'].dt.day - df['rental_date'].dt.day

    df = delete_columns(df, ['rental_date', 'return_date'])

    load_clean_data(df, 'output/global_activity_clients_clean.csv')



def preprocess_second_df(path):
    #Carga de datos
    df = charge_path(path)

    # Normalización a tipo fecha y string
    df = normalize_date_columns(df)
    df = normalize_string_columns(df)

    # Eliminación de columnas innecesarias
    df = delete_columns(df, ['language'])

    #Exportación de datos limpios
    load_clean_data(df, 'output/catalog_film_clean.csv')
