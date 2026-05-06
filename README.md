# SQL to Python Data Pipeline Grupo 4: Sakila Analysis 📊

## 📝 Descripción del Proyecto
Este proyecto consiste en el diseño y ejecución de un pipeline de datos completo, desde la extracción y limpieza inicial en **SQL** hasta el procesamiento avanzado y análisis en **Python**. Utilizando la base de datos **Sakila**, se han generado diversos conjuntos de datos para analizar el comportamiento de clientes, el catálogo de películas y la popularidad de los actores.

El flujo de trabajo se divide en dos fases:
1.  **Fase SQL:** Extracción mediante join y limpieza básica.
2.  **Fase Python:** Limpieza en profundidad, conversión de formatos, creación de columnas adicionale, detección de valores nulos y outliers. Exportación de datos una vez han sido procesados.

---

## 🎯 Objetivos Concretos
* **Comprender** la estructura de la base de datos Sakila y conectar múltiples tablas.
* **Extraer** tres dataframes obligatorios mediante joins personalizados.
* **Aplicar** reglas de limpieza y estandarización directamente en el motor de base de datos.
* **Documentar** un proceso reproducible en un notebook que justifique cada decisión de limpieza.
* **Exportar** un dataset final limpio (CSV o Parquet) para futuras etapas de análisis.

---

## 🏗️ Fases del Desarrollo

### 1. Extracción desde SQL
Se generaron tres vistas de datos iniciales uniendo tablas específicas:
* **Dataframe 1: Actividad de clientes** (`customer`, `address`, `city`, `country`, `rental`, `payment`).
* **Dataframe 2: Catálogo de películas** (`film`, `film_category`, `category`, `language`, `inventory`).
* **Dataframe 3: Elenco y popularidad** (`film`, `actor`, `film_actor`).

### 2. Limpieza Preliminar en SQL
Para el dataset seleccionado, se ejecutaron las siguientes acciones de limpieza en SQL:
* **Estandarización:** Uso de `LOWER()` en columnas de texto.
* **Integridad:** Filtrado de importes inconsistentes (`amount > 0`), transacciones completadas en su totalidad (`rental_date IS NOT NULL AND return_date IS NOT NULL`).
* **Lógica de Negocio:** Validación de que la fecha de devolución sea posterior a la de alquiler (`rental_date < return_date`).
* **Columnas Derivadas:** Creación de métricas como `rental_duration` (usando `DATEDIFF`) o `is_long_film`.

### 3. Procesamiento y Limpieza Final en Python
En **Google Colab**, se realizó el tratamiento final de los datos:
* **Conversión de Tipos:** Ajuste de columnas a `datetime`, formatos numéricos y de cadenas.
* **Tratamiento de Nulos y Duplicados:** Análisis de impacto y eliminación según criterios de calidad.
* **Análisis de Outliers:** Detección de valores atípicos mediante técnicas estadísticas (Rango Intercuartílico / Test de Tukey).
* **Normalización Extra:** Limpieza final de cadenas y corrección de errores de entrada de datos.

---

## 🧰 Tecnologías y Librerías
* **SQL:** MySQL / MySQL Workbench / DBeaver.
* **Python:** Google Colab.
* **Librerías de Python:** `pandas`, `matplotlib`, `seaborn`.
* **GitHub:** Control de versiones y documentación.

---

## 📦 Entrega y Estructura del Repositorio
* `queries/`: Contiene el script `.sql` con la consulta final de extracción y limpieza.
* `notebooks/`: Archivo `.ipynb` con el procesamiento en Python y visualizaciones.
* `README.md`: Este documento detallando el proceso.

---

## ✅ Checklist de Limpieza (Python)
- [x] Conversión de fechas a `datetime`.
- [x] Gestión de duplicados.
- [x] Tratamiento de valores faltantes.
- [x] Normalización de cadenas (`lower`, `trim`).
- [x] Detección y tratamiento de **outliers**.
- [x] Creación de columnas derivadas.
- [x] Visualización de validación y exportación final.

---

### 🛠️ Ingeniería de Características (Feature Engineering)

Para enriquecer el análisis y permitir un estudio más detallado de los patrones de consumo, se han realizado diversas transformaciones y derivaciones de datos:

#### 👤 Información de Identidad
* **`full_name`**: Consolidación de los campos de nombre y apellido en una única variable, mejorando la legibilidad de los reportes y visualizaciones.

#### 📅 Extracción y Desglose Temporal
A partir de las columnas originales de fecha (`rental_date` y `return_date`), se han descompuesto los siguientes atributos para análisis granulares:
* **Componentes Cronológicos**: Creación de columnas específicas para **Día, Mes, Año y Hora**, tanto para el momento del alquiler como para la devolución.
* **`day_of_week_rental`**: Identificación del día de la semana (donde 1 es Lunes y 7 es Domingo).
* **`is_weekend_rental`**: Variable binaria (1/0) que clasifica si el alquiler ocurrió en fin de semana, permitiendo comparar el volumen de negocio entre días laborables y festivos.

#### 🌡️ Segmentación por Estacionalidad y Franjas Horarias
* **`season`**: Clasificación de los registros según la estación del año. 
  > **Nota de Análisis**: Tras explorar los datos, se observa que la actividad en Sakila se concentra exclusivamente entre los meses de mayo y agosto (Primavera y Verano), por lo que no se encontrarán registros de Otoño o Invierno en este dataset específico.
* **`rental_hour_part_of_the_day`** y **`return_hour_part_of_the_day`**: Categorización de las horas en tres franjas principales para identificar picos de afluencia:
  * **Mañana**: 07:00 - 12:59
  * **Tarde**: 13:00 - 23:59
  * **Noche**: 00:00 - 06:59

#### 🧹 Optimización y Limpieza de Columnas

Una vez extraída la información necesaria, se procedió a eliminar las columnas originales (`first_name`, `last_name`, `rental_date`, `return_date`) para reducir la redundancia.

## 🧠 Decisiones Tomadas

*Se ha priorizado el mantenimiento de la integridad referencial durante los JOINS.

Con los valores de la columna `district` hemos intentando realizar una imputación por la moda, haciendo una agrupación por `city`, `postal_code` y `country`. Con el resto de valores nulos hemos procedido a relizar una imputación a (`missing`).
En el caso de los outliers, se decidió mantenerlos ya que el dataframe solamente presentaba 4 valores outliers. Estas decisiones han sido tomadas basándonos en el conocimiento del dominio de los datos de Sakila.*

---

## 📊 Gráficas Relevantes
Hemos realizado 5 gráficas en la que:
1.  **Gráfica de alquileres por año:** Visualización de la tendecnia  de alquileres de película por año. Aquí no es hemos dado cuenta que solamente poseemos registros del año 2015
2.  **Gráfica alquires por hora del día:** Histograma de distribución de alquileres de película por hora del día.
3.  **Gráfica alquires por día de la semana y temporada:** Countplot de distribución de alquileres de película por día de la semana que se alquila y temporada del año.
4.  **Gráfica alquires por mes del año:** Countplor de distribución de alquileres por mes del año. Aquí nos hemos dado cuenta que solamente tenemos registros de los meses que van desde Mayo a Agosto
5.  **Gráfica usuarios con más alquileres:** Barplot de los Top 5 clientes con más alquileres.

---

**Desarrollado por:** Ana Ganfornina y Daniel Luque
**Plazo de entrega:** 1 semana
**Enlace Tablero Figma:** (https://www.figma.com/board/5GEmJWY33xlKvXMoCRfXxC/Flujo-de-datos-de-SQL-a-Python?node-id=0-1&p=f&t=vFISDLJqBQYrApjw-0)
