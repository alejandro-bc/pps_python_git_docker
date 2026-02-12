# --- FASE 1: Resolución de dependencias ---
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
# Instalamos dependencias
RUN pip install --user --no-cache-dir -r requirements.txt


# --- FASE 2: Ejecución ---
FROM python:3.11-slim

WORKDIR /app

# Traemos las dependencias de la fase anterior
COPY --from=builder /root/.local /root/.local

# CAMBIO AQUÍ: Copiamos TODOS los archivos .py y el .txt necesarios
# Es mejor listar los archivos o usar un patrón para no olvidar ninguno
COPY app.py bayeta.py database.py frases.txt ./

# Aseguramos que el PATH reconozca las librerías (como pymongo)
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "app.py"]