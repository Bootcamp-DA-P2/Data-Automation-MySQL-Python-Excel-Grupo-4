import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#charge the path
def charge_path(path):
    df = pd.read_csv(path)
    return df

def show_head(df, top_n=10):
    return df.head(top_n)

def show_info(df):
    return df.info()

def first_visualizer(df):

    # Visualización del tamaño del dataframe
    num_columnas = df.shape[1]
    num_filas = df.shape[0]

    #Duplicados
    num_duplicados = df.duplicated().sum()

    # Suma de valores nulos por columna
    null_values = df.isnull().sum().sum()

    # Porcentaje de valores nulos por columna
    df_porcentaje_nulos_columna = (df.isnull().sum() * 100 / len(df),2)


    # Estadísticas descriptivas para columnas categóricas
    df_describe_numeric = df.describe()
    # Estadísticas descriptivas para columnas categóricas
    df_describe_categorical = df.describe(include='object')

    return num_columnas, num_filas, num_duplicados, null_values, df_porcentaje_nulos_columna, df_describe_numeric, df_describe_categorical

def normalize_string_columns(df):
    """
    Normalización de las columnas de tipo string: convertir a minúsculas, eliminar espacios y caracteres especiales.
    """
    columns_str = df.select_dtypes("object").columns

    for column in columns_str:
        df[column] = df[column].astype("string").str.lower().str.strip()
        df[column] = df[column].str.replace(r'[^a-zA-Z0-9 @]', '', regex=True)

    return df

def normalize_date_columns(df):
    """
    Normalización de las columnas de tipo fecha: convertir a formato datetime."""
    
    column_date = df.filter(like='date').columns
    for column in column_date:
        df[column] = pd.to_datetime(df[column])
    return df

def delete_columns(df, columns_to_delete):
    """
    Eliminar columnas específicas del dataframe.
    """
    df = df.drop(columns=columns_to_delete, axis=1)
    return df


def identify_nulls(df):
    """
    Identificar valores nulos en el dataframe.
    """
    print("--------------------------------")
    nuls = df.isnull().sum().sum()

    if nuls == 0:
        print("En este caso no se encuentran valores nulos por lo que no se procede a eliminar filas.")
    else:
        print(f"Se encontraron {nuls} valores nulos.")


def identify_outliers(df, variables_numericas, variables_categoricas):
    """
    Identificación de valores atípicos en columnas numéricas utilizando el método del rango intercuartílico (IQR).
    number_columns: array de columnas numéricas
    categorical_columns: array de columnas categóricas
    """
    for col in variables_numericas:
        plt.figure(figsize=(8,4))
        sns.histplot(df[col], kde=True)
        plt.title(f'Histograma de {col}')
        plt.xlabel(col)
        plt.ylabel('Frecuencia')
        plt.show()

        plt.figure(figsize=(8,4))
        sns.boxplot(x=df[col], orient='horizontal')
        plt.title(f'Boxplot de {col}')
        plt.xlabel(col)
        plt.show()
    
    for col in variables_categoricas:
        plt.figure(figsize=(8,4))
        sns.countplot(x=df[col])
        plt.title(f'Conteo de {col}')
        plt.xlabel(col)
        plt.ylabel('Frecuencia')
        plt.xticks(rotation=45)
        plt.show()

def load_clean_data(df, path):
    df.to_csv(path, index=False)
