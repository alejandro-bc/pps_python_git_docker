from database import conectar_db, inicializar_db, obtener_frases_random

# Conectamos e inicializamos al importar
coleccion = conectar_db()
inicializar_db(coleccion)

def frotar(n_frases: int = 1) -> list:
    try:
        return obtener_frases_random(coleccion, n_frases)
    except Exception as e:
        return [f"Error en la BBDD: {e}"]