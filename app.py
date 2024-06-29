from flask import Flask
from flask import jsonify



app = Flask(__name__)

@app.route('/')

def inicio():
    return "<h1>TP Back_End_Python-C24261 G19</h1>"

from componentes.vistas_api import *

if __name__ == "main":
    app.run()