# 📊 Automatización MySQL → Python → Excel (Sakila Analysis) Grupo 4

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

<img width="1334" height="701" alt="Captura de pantalla 2026-05-13 a las 19 01 29" src="https://github.com/user-attachments/assets/e65e869c-8654-4dbc-84c9-555d29878ff5" />


## 📝 Descripción
Este proyecto implementa un **enfoque híbrido** para el análisis de datos: utiliza la potencia de **Python** para la extracción, limpieza y pre-procesamiento de datos desde una base de datos **MySQL**, y la flexibilidad de **Excel** para el diseño creativo de dashboards.

El flujo garantiza que los datos se mantengan actualizados automáticamente en archivos CSV intermedios, permitiendo que el usuario se enfoque exclusivamente en la visualización y el storytelling dentro de Excel.

## 🎯 Objetivos
*   **Extracción Automática:** Conectar Python con MySQL para obtener datos en tiempo real.
*   **Procesamiento de Datasets:** Generar al menos 3 archivos CSV pre-procesados y listos para el análisis.
*   **Flujo Simplificado:** Crear un pipeline donde Python actúa como el motor de datos y Excel como la interfaz de usuario.
*   **Mantenimiento:** Documentar una estructura de código modular y fácil de escalar.

## 🗄️ Base de Datos
Por defecto, el proyecto utiliza la base de datos **Sakila**, la cual simula el ecosistema de una tienda de alquiler de películas (clientes, inventario, pagos y geografía).

> **Nota:** El sistema es flexible y permite ser adaptado a cualquier otra base de datos relacional cambiando las consultas SQL en el script principal. También presentamos diferentes métodos con la lógica necesaria integrada.

### Áreas de Análisis:
1.  **Clientes:** Comportamiento y patrones de consumo.
2.  **Peliculas:** Información de peliculas.
3.  **Relación Clientes - Pelicula:** Tabla de unión de tablas externas clientes y peliculas.

## 🧰 Tecnologías y Librerías
*   **Lenguaje:** Python
*   **Base de Datos:** MySQL
*   **Librerías Clave:**
    *   `pandas`: Manipulación de DataFrames y exportación a CSV.
    *   `sqlalchemy` & `mysql-connector-python`: Gestión de conexiones y queries.
    *   `python-dotenv`: Seguridad en el manejo de credenciales.
    *   `scikit-learn`: Creación de gráficas.
*   **Visualización:** Microsoft Excel (Power Pivot, Tablas dinámicas y Dashboards).
*   **Control de Versiones:** Git & GitHub.

**Desarrollado por:** Ana Ganfornina y Daniel Luque

**Plazo de entrega:** 1 semana

[Enlace Tablero Figma] (https://www.figma.com/board/5GEmJWY33xlKvXMoCRfXxC/Flujo-de-datos-de-SQL-a-Python?node-id=0-1&p=f&t=vFISDLJqBQYrApjw-0)
