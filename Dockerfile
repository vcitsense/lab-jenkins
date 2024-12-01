# Usar la imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

COPY ./app /app


# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Make sure pytest is included in requirements.txt or install it directly
RUN pip install pytest
RUN pip install requests

# Exponer el puerto que usará Flask
EXPOSE 5000

# Establecer la variable de entorno
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0

# Comando para iniciar la aplicación
CMD ["flask", "run"]
