from flask import jsonify, request, redirect, url_for, render_template
#from flask import request

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

#-----------------------------------------------------

# Ruta productos/agregar

# Ruta productos/editar
@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def modificar_producto(id):
    campos = Productos.obtener("id",id)
    return render_template('modificar_productos.html', campos=campos)

# Ruta productos/eliminar
@app.route('/productos/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_producto(id):
    mensaje = Productos.eliminar(id)
    return f"<div style='width:100%; text-align: center;'><h1>El producto tratado tenía el id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/'>Regrese a la página principal 👉</a></h2>"

# Ruta para guardar cambios de productos editados o agregados
@app.route('/productos/guardarProducto/<int:id>', methods=['POST'])
def guardarProducto(id):
    datos = request.form
    mensaje = Productos.actualizar(id, datos)
    return f"<div style='width:100%; text-align: center;'><h1>Producto a modificar con id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/'>Regrese a la página principal 👉</a></h2>"


#-----------------------------------------------------

# Ruta clientes/agregar
@app.route('/clientes/agregar', methods=['POST'])
def agregar_clientes():
    cliente = Clientes.obtener()
    if type(cliente) != list: # si vuelve sólo uno
        cliente = [cliente] 

    datos = [clientes.__dict__ for clientes in cliente]
    return jsonify(datos)

# Ruta clientes/editar/

# Ruta clientes/eliminar
@app.route('/clientes/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_cliente(id):
    mensaje = Clientes.eliminar(id)
    return f"<div style='width:100%; text-align: center;'><h1>El cliente tratado tenía el id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/'>Regrese a la página principal 👉</a></h2>"
    #return redirect(url_for('inicio'))
