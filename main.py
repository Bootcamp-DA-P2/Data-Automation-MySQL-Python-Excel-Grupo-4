from src.sakila_ETL import get_execute_queries, queries, paths
from src.utils.process_methods import preprocess_first_df, preprocess_second_df, preprocess_third_df
if __name__ == "__main__":
    try:
        get_execute_queries(queries, paths)
        print('Queries ejecutadas exitosamente')

        preprocess_first_df('output/client_activity_rental.csv')
        preprocess_second_df('output/catalog_film.csv')
        preprocess_third_df('output/global_activity_clients.csv')
        print('Dataframes procesados exitosamente')
    except Exception as e:
        print(f'Error en el pipeline: {e}')

