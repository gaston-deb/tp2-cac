from flask import jsonify

from app import app
from componentes.modelos import Productos
from componentes.modelos import Clientes

@app.route('/api/productos', methods=['GET'])
def api_productos():
    producto = Productos.obtener()
    if type(producto) != list: # si vuelve sólo uno
        producto = [producto] 

    datos = [productos.__dict__ for productos in producto]
    return jsonify(datos)

@app.route('/api/clientes', methods=['GET'])
def api_clientes():
    cliente = Clientes.obtener()
    if type(cliente) != list: # si vuelve sólo uno
        cliente = [cliente] 

    datos = [clientes.__dict__ for clientes in cliente]
    return jsonify(datos)

