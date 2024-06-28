from flask import Flask
from flask import jsonify

from componentes.datos import obtener_datos
from componentes.modelos import Celular

app = Flask(__name__)

@app.route('/')

def inicio():
    return "<h1>TP Back_End_Python-C24261 G19</h1>"

@app.route('/api/test')
def mostrar_datos():
    return jsonify(obtener_datos())

@app.route('/api/celular', methods=['GET'])
def api_celulares():
    celulares = Celular.obtener()
    datos = [celular.__dict__ for celular in celulares]
    return jsonify(datos)

if __name__ == "main":
    app.run()