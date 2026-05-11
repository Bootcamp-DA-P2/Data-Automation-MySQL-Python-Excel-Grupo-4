import pandas as pd
def preprocess_first_df(df):
    # Normalización strings
    colum_str = ['first_name', 'last_name','email','address','district','city','country']
    for column in colum_str:
        df[column] = df[column].astype("string").str.lower().str.strip() #limpiamos las columnas a minusculas y eliminando también espacios
        df[column] = df[column].str.replace(r'[^a-zA-Z0-9 @]', '',regex=True)

    #convertimos a boolean y no bool para que no transforme los nulos en True
    df['active'] = df['active'].astype('boolean')

    # Normalizar a tipo fecha
    column_date = ['rental_date','return_date', 'payment_date']
    for column in column_date:
        df[column] = pd.to_datetime(df[column])

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
    df = df.drop(columns=['first_name', 'last_name', 'rental_date', 'return_date'], axis=1) # axis = 1 == columnas

    # Tratamiento de valores nulos
    df['district'] = df['district'].fillna(
        df.groupby(['city', 'postal_code', 'country'])['district'].transform(
            lambda x: x.mode().iloc[0] if not x.mode().empty else 'missing'
        )
    )

    #Seleccionar los nombres de las columnas que son texto
    columns_str = df.select_dtypes("string").columns
    print(columns_str)

    for column in columns_str:
        df[column] = df[column].fillna("missing")

    df.to_csv('../output/sakila-client-activity-tratado.csv', index=False)