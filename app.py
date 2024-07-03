from flask import Flask

#PARA LOS CARACTERES ESPECIALES
from flask_cors import CORS

app = Flask(__name__)
app.json.ensure_ascii = False


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from componentes.vistas_web import *
from componentes.vistas_api import *

if __name__ == "main":
    app.run()