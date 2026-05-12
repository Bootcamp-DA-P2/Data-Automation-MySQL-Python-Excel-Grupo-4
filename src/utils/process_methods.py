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

    # Tratamiento de valores nulos (Mantenemos tu lógica de distrito)
    df['district'] = df['district'].fillna(
        df.groupby(['city', 'postal_code', 'country'])['district'].transform(
            lambda x: x.mode().iloc[0] if not x.mode().empty else 'missing'
        )
    )

    # Columnas de texto a 'missing'
    columns_str = df.select_dtypes("string").columns
    for column in columns_str:
        df[column] = df[column].fillna("missing")

    # Eliminación de columnas redundantes (SOLO las que existen en esta tabla)
    df = delete_columns(df, ['first_name', 'last_name'])

    load_clean_data(df, 'output/client-activity-clean.csv')

def preprocess_third_df(path):
    df = charge_path(path)
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

    df = normalize_date_columns(df)
    df = normalize_string_columns(df)

    # Verificación de seguridad
    if 'rental_date' in df.columns:
        # Lógica temporal (Día, Mes, Año, Hora)
        df['rental_day'] = df['rental_date'].dt.day
        df['rental_month'] = df['rental_date'].dt.month
        df['rental_year'] = df['rental_date'].dt.year
        df['rental_hour'] = df['rental_date'].dt.hour
        
        # Estaciones y Tramos (Mantenemos tu lógica original)
        df['season'] = df['rental_month'].apply(lambda x: 'spring' if x in [3,4,5] else ('summer' if x in [6,7,8] else ('autumn' if x in [9,10,11] else 'winter')))
        df['rental_hour_part_of_the_day'] = df['rental_hour'].apply(lambda x: 'night' if x in [0,1,2,3,4,5,6] else('morning' if x in [7,8,9,10,11,12] else 'afternoon'))

    # Cálculo de lag de pago (Corregido para evitar errores de fin de mes)
    if 'payment_date' in df.columns and 'rental_date' in df.columns:
        df['payment_lag'] = (df['payment_date'] - df['rental_date']).dt.days

    # Eliminación final de columnas de fecha originales
    df = delete_columns(df, ['rental_date', 'return_date', 'payment_date'])

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
