# pps_python_git_docker

## 1. Resolución de Dependencias
Asegurarse de tener el entorno virtual:
```bash
pip install -r requirements.txt

Para comprobar que funciona ejecutar:

python app.py

## Ejecución con Docker
1. Construir imagen: `docker build -t bayeta-app .`
2. Correr contenedor: `docker run -p 5000:5000 bayeta-app`