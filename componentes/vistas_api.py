from flask import jsonify
#from flask import request

from app import app
from componentes.modelos import Celular
from componentes.modelos import Accesorio

@app.route('/api/celular', methods=['GET'])
def api_celulares():
    celulares = Celular.obtener()
    if type(celulares) != list: # si vuelve sólo uno
        celulares = [celulares] 

    datos = [celular.__dict__ for celular in celulares]
    return jsonify(datos)

@app.route('/api/accesorio', methods=['GET'])
def api_accesorios():
    accesorios = Accesorio.obtener()
    if type(accesorios) != list: # si vuelve sólo uno
        accesorios = [accesorios] 

    datos = [accesorio.__dict__ for accesorio in accesorios]
    return jsonify(datos)