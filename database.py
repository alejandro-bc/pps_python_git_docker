from pymongo import MongoClient
import random

def conectar_db():
    # Usamos 'mongo-db' como host porque así se llama el contenedor en la red
    client = MongoClient('mongodb://mongo-db:27017/')
    db = client['bayeta_db']
    return db['frases']

def inicializar_db(coleccion):
    # Solo insertamos si está vacía
    if coleccion.count_documents({}) == 0:
        with open("frases.txt", "r", encoding="utf-8") as f:
            frases = [{"texto": linea.strip()} for linea in f if linea.strip()]
        if frases:
            coleccion.insert_many(frases)
            print("Base de datos inicializada con frases.txt")

def obtener_frases_random(coleccion, n=1):
    # Usamos el operador $sample de Mongo para obtener frases aleatorias
    pipeline = [{"$sample": {"size": n}}]
    cursor = coleccion.aggregate(pipeline)
    return [doc['texto'] for doc in cursor]