from flask import Flask
from flask import jsonify

from componentes.datos import obtener_datos

app = Flask(__name__)

@app.route('/')

def inicio():
    return "<h1>TP Back_End_Python-C24261 G19</h1>"

@app.route('/api/test')
def mostrar_datos():
    return jsonify(obtener_datos())

if __name__ == "main":
    app.run()