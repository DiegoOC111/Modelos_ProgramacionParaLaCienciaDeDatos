# Repositorio de Proyectos - Programación para Ciencia de Datos (PPCD)

Este repositorio contiene el código fuente, los notebooks de análisis y la documentación correspondiente a la Entrega 2 de la asignatura Programación para Ciencia de Datos (PPCD) impartida en Duoc UC, sede Antonio Varas. 

El repositorio agrupa tres proyectos principales enfocados en el preprocesamiento de datos, análisis exploratorio y el entrenamiento de modelos de machine learning y deep learning.

---

## Tabla de Contenidos

* [Descripción General](#descripción-general)
* [Proyectos Incluidos](#proyectos-incluidos)
  * [1. Evaluación Práctica (Prueba 2)](#1-evaluación-práctica-prueba-2)
  * [2. Trabajo de Asignatura (PPCD)](#2-trabajo-de-asignatura-ppcd)
  * [3. Pipeline de Detección de Neumonía](#3-pipeline-de-detección-de-neumonía)
* [Documentación](#documentación)
* [Tecnologías y Requisitos](#tecnologías-y-requisitos)
* [Autores](#autores)

---

## Proyectos Incluidos

Los tres proyectos están desarrollados en Jupyter Notebooks individuales para mantener el código modular y ordenado.

### 1. Evaluación Práctica (Prueba 2)
* **Archivo:** `PrograCienciaDatos_Prueba_2_Cristobal.ipynb`
* **Descripción:** Resolución de la segunda evaluación de la asignatura. Contiene ejercicios aplicados de limpieza de datos, análisis exploratorio (EDA) y la implementación de algoritmos de modelado según los requerimientos de la prueba.

### 2. Trabajo de Asignatura (PPCD)
* **Archivo:** `Trabajo_2_PPCD (2).ipynb`
* **Descripción:** Segundo trabajo práctico de la asignatura. Se enfoca en la manipulación avanzada de datasets, transformaciones de datos y aplicación de técnicas de ciencia de datos para extraer insights de valor.

### 3. Pipeline de Detección de Neumonía
* **Archivo:** `pneumonia_analysis_pipeline.ipynb`
* **Descripción:** El proyecto más robusto de la entrega. Consiste en un pipeline completo para el análisis y clasificación de imágenes médicas (radiografías de tórax) con el fin de detectar neumonía. Incluye el preprocesamiento de imágenes, división de datos (train/test/validation) y el entrenamiento de modelos predictivos.

---

## Documentación

El repositorio incluye un informe técnico detallado que respalda las decisiones tomadas en el código, enfocado principalmente en el tercer proyecto:

* **Informe Técnico modelos comparativos.pdf:** Documento que analiza y compara métricas de rendimiento (Accuracy, Precision, Recall, F1-Score) de los distintos modelos predictivos evaluados para la detección de neumonía, justificando la elección del modelo final.

---

## Tecnologías y Requisitos

Para ejecutar los notebooks de este repositorio sin problemas, asegúrate de tener instalado Python 3.x y las siguientes librerías principales:

* `jupyter` o `jupyterlab`
* `pandas` y `numpy` para manipulación de datos.
* `matplotlib` y `seaborn` para visualización.
* `scikit-learn` para algoritmos de machine learning tradicional.
* `tensorflow` / `keras` (o el framework utilizado en el pipeline de neumonía) para el procesamiento de imágenes.

Para instalar las dependencias básicas, puedes ejecutar:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
