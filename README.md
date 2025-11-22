# TFM - Análisis de Tráfico Celular

Este repositorio contiene el código y los análisis para el Trabajo de Fin de Máster (TFM) sobre dinámicas de tráfico de telecomunicaciones. El proyecto analiza grandes volúmenes de datos de SMS, llamadas e Internet en la ciudad de Milán, explorando tanto patrones temporales como su distribución espacial.

## 📂 Contenido del Repositorio

*   **`analysis.ipynb`**: Notebook principal de Jupyter. Contiene todo el flujo de trabajo:
    *   Carga eficiente de datos masivos usando `Dask`.
    *   Análisis temporal: Evolución del tráfico por semana (Lunes-Domingo).
    *   Análisis espacial: Mapa de calor (Heatmap) de la distribución del tráfico en la cuadrícula urbana (100x100).
*   **`requirements.txt`**: Lista de dependencias necesarias para ejecutar el proyecto.
*   **`.gitignore`**: Configuración para excluir archivos de datos grandes y temporales.

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu ordenador local:

### 1. Clonar el Repositorio

Abre tu terminal y ejecuta:

```bash
git clone https://github.com/jorgenchu/TFM.git
cd TFM
```

### 2. Requisitos Previos

Necesitas tener instalado **Python 3.8** o superior.

### 3. Instalar Dependencias

Instala las librerías necesarias (Pandas, Dask, Matplotlib, etc.) ejecutando:

```bash
pip install -r requirements.txt
```

## ▶️ Uso

1.  Asegúrate de tener los archivos de datos (`data1.csv`, `data2.csv`) en las carpetas correspondientes dentro del directorio del proyecto (o ajusta las rutas en el notebook).
2.  Inicia Jupyter Notebook:

```bash
jupyter notebook
```

3.  Abre el archivo `analysis.ipynb` y ejecuta las celdas secuencialmente.

## 📊 Visualizaciones Clave

El notebook genera:
*   Gráficas de series temporales mostrando los picos de actividad diaria y semanal.
*   Un **Mapa de Calor (Spatial Distribution)** que visualiza la concentración de tráfico en el centro de la ciudad frente a la periferia.

## 🛠️ Tecnologías Utilizadas

*   **Python**: Lenguaje principal.
*   **Dask**: Para el procesamiento paralelo de grandes conjuntos de datos (Big Data).
*   **Pandas**: Manipulación y análisis de datos.
*   **Matplotlib**: Generación de gráficos y visualizaciones.
