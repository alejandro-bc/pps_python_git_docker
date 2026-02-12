from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

# Paso 4 (Línea WEB): Hola Mundo en la raíz
@app.route('/')
def hola_mundo():
    return "<h1>Hola, mundo</h1>"

# Paso 6 (Línea WEB): Endpoint que devuelve N frases en JSON
@app.route('/frotar/<int:n_frases>')
def endpoint_frotar(n_frases):
    # Llama a la función frotar de bayeta.py
    frases = frotar(n_frases)
    return jsonify({"frases": frases})

if __name__ == '__main__':
    # Paso 4 (Línea Python): Modificar el print para probar la función
    print("\n--- TEST DE FUNCIONAMIENTO (Experto en Python) ---")
    try:
        resultado_test = frotar(3)
        print(f"Resultado de frotar(3): {resultado_test}")
    except Exception as e:
        print(f"Error al probar la función frotar: {e}")
    print("--------------------------------------------------\n")

    # Ejecución del servidor en el puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)