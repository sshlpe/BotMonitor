# Usa una imagen ligera de Python
FROM python:3.12-slim

# Crea directorio de trabajo
WORKDIR /app

# Copia archivos del proyecto
COPY . /app

# Crea el directorio para el volumen persistente
RUN mkdir -p /data

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone puerto por si decides agregar ping HTTP en el futuro
EXPOSE 8080

# Comando de inicio
CMD ["python", "bot.py"]