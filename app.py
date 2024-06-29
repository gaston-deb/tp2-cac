from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')

def inicio():
    return render_template('principal.html')

from componentes.vistas_api import *

if __name__ == "main":
    app.run()