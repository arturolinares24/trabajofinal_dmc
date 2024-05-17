# Usar una imagen oficial de Python como imagen base
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar el contenido del directorio actual en el contenedor en /usr/src/app
COPY . .


RUN pip install --no-cache-dir -r requirements.txt

# Hacer disponible el puerto 8000 al mundo exterior a este contenedor
# Esto no publica el puerto, solo indica que el puerto está destinado a ser publicado
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Ejecutar app.py cuando se inicie el contenedor
# uvicorn se usa como servidor ASGI para ejecutar la aplicación FastAPI
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]