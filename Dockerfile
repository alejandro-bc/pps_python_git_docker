# --- FASE 1: Resolución de dependencias ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Instalamos herramientas de compilación si fueran necesarias
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copiamos requirements e instalamos dependencias en una carpeta local
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# --- FASE 2: Ejecución ---
FROM python:3.11-slim

WORKDIR /app

# Copiamos las librerías instaladas desde la fase anterior
COPY --from=builder /root/.local /root/.local
# Copiamos el código de la aplicación y archivos necesarios
COPY app.py bayeta.py frases.txt ./

# Aseguramos que el PATH reconozca las librerías instaladas en la fase 1
ENV PATH=/root/.local/bin:$PATH

# Exponemos el puerto de Flask
EXPOSE 5000

# Comando para arrancar la app
CMD ["python", "app.py"]