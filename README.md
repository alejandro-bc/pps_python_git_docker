# La Bayeta de la Fortuna - v5.0 (Final Release)

Esta aplicación es un microservicio basado en Python que ofrece frases
de fortuna aleatorias. Ha evolucionado desde un script simple hasta una
arquitectura profesional orquestada con Docker Compose y persistencia en
MongoDB.

------------------------------------------------------------------------

## Guía de Inicio Rápido (Instrucciones de Despliegue)

Para desplegar la aplicación completa (Base de datos + Aplicación Web)
siguiendo los estándares de este proyecto, asegúrate de tener instalado
Docker y Docker Compose, y ejecuta:

### 1. Clonar el repositorio e instalar

``` bash
git clone <url-del-repositorio>
cd pps_python_git_docker
```

### 2. Levantar el ecosistema

``` bash
docker compose up -d
```

### 3. Acceso

La aplicación estará disponible en:

    http://localhost:5000/frotar/<numero_de_frases>

Ejemplo:

    http://localhost:5000/frotar/2

------------------------------------------------------------------------

## Evolución del Proyecto y Hitos Alcanzados

A continuación se detallan los pasos realizados para garantizar la
consistencia entre entornos y la escalabilidad del sistema:

### 1. Dockerización Multifase (v2.0)

Se ha implementado un Dockerfile multifase para optimizar el peso de la
imagen final:

-   **Fase de construcción**: Basada en `python:3.11-slim`, resuelve
    dependencias e instala paquetes de compilación.
-   **Fase de ejecución**: Copia únicamente las librerías necesarias y
    el código fuente, manteniendo un entorno ligero y seguro.
-   Se incluye un archivo `.dockerignore` para evitar la inclusión de
    entornos virtuales (`venv`), carpetas de Git y archivos de
    configuración local.

------------------------------------------------------------------------

### 2. Integración de MongoDB (v3.0)

Sustitución del archivo de texto local por una base de datos NoSQL:

-   **Módulo `database.py`**: Gestiona la conexión con el motor de base
    de datos.
-   **Inicialización automática**: El sistema detecta si la base de
    datos está vacía y la puebla automáticamente con las frases de
    `frases.txt`.
-   **Consultas eficientes**: Uso del operador `$sample` de MongoDB para
    obtener frases aleatorias directamente desde el motor.

------------------------------------------------------------------------

### 3. Orquestación con Docker Compose (v4.0)

Migración de comandos manuales de Docker a un orquestador:

-   Definición de servicios `bayeta-web` y `mongo-db`.
-   Creación de una red aislada (`bayeta-network`) para la comunicación
    entre contenedores.
-   Configuración de dependencias (`depends_on`) para asegurar que la
    base de datos esté lista antes que la aplicación.

------------------------------------------------------------------------

### 4. Persistencia mediante Volúmenes (v5.0)

Para evitar la pérdida de datos al reiniciar contenedores:

-   Se ha mapeado un volumen nombrado (`mongo-data`) a la ruta interna
    `/data/db` de MongoDB.
-   Los datos ahora persisten en el host, permitiendo realizar
    actualizaciones del servicio sin perder la información almacenada.

------------------------------------------------------------------------

## Comandos Útiles para la Corrección

``` bash
docker compose ps
docker logs -f bayeta-web
docker compose down && docker compose up -d
docker volume inspect pps_python_git_docker_mongo-data
```

------------------------------------------------------------------------

## Estructura Final del Proyecto

-   `app.py`: API Flask (Endpoint principal).
-   `bayeta.py`: Lógica de negocio.
-   `database.py`: CRUD y conexión a MongoDB.
-   `docker-compose.yml`: Configuración de la orquestación.
-   `Dockerfile`: Receta de construcción de la imagen.
-   `requirements.txt`: Dependencias (Flask, pymongo).
