from flask import Flask, render_template, jsonify
import requests

#PARA LOS CARACTERES ESPECIALES
from flask_cors import CORS

app = Flask(__name__)
app.json.ensure_ascii = False

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def inicio():
    return render_template('principal.html')

from componentes.vistas_api import *

if __name__ == "main":
    app.run()