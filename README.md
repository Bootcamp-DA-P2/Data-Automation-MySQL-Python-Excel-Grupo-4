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

## 🧠 Decisiones Tomadas
*Se ha priorizado el mantenimiento de la integridad referencial durante los JOINS.
Con los valores nulos hemos procedido a relizar una imputación a (`missing`).
En el caso de los outliers, se decidió mantenerlos ya que el dataframe solamente presentaba 4 valores outliers. Estas decisiones han sido tomadas basándonos en el conocimiento del dominio de los datos de Sakila.*

---
## 📊 Gráficas Relevantes
*Qué graficas hemos realizado*

---
**Desarrollado por:** Ana Ganfornina y Daniel Luque
**Plazo de entrega:** 1 semana
