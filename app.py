from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "<h1>Hola, mundo</h1>"

@app.route('/frotar/<int:n_frases>')
def endpoint_frotar(n_frases):
    frases = frotar(n_frases)
    return jsonify({"frases": frases})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)