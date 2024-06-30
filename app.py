from flask import Flask, render_template, jsonify
import requests

#PARA LOS CARACTERES ESPECIALES
from flask_cors import CORS


app = Flask(__name__)
app.json.ensure_ascii = False

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')

def inicio():
    j_prod = requests.get('http://localhost:5000/api/productos')
    productos = j_prod.json()
    j_cli = requests.get('http://localhost:5000/api/clientes')
    clientes = j_cli.json()

    return render_template('principal.html', productos=productos, clientes=clientes)

from componentes.vistas_api import *

if __name__ == "main":
    app.run()