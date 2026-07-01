FROM python:3.11-slim

# Evitar que Python escriba archivos .pyc en el disco y asegurar salida de logs inmediata
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema necesarias para procesamiento de imágenes si aplica
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Asegurar la presencia de librerías para la interfaz web de la API
RUN pip install --no-cache-dir fastapi uvicorn python-multipart

# Copiar la estructura completa del proyecto al contenedor
COPY . .

# Exponer el puerto asignado para el servicio web
EXPOSE 8000

# Comando por defecto para iniciar la API con Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]