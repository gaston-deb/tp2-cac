from flask import jsonify, request, redirect, url_for, render_template
from werkzeug.datastructures import ImmutableMultiDict
import requests

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
# Ruta Productos
@app.route('/productos')
def productos():
    j_prod = requests.get('http://localhost:5000/api/productos')
    productos = j_prod.json()    
    return render_template('productos.html', productos=productos)

# Ruta Clientes
@app.route('/clientes')
def clientes():
    j_prod = requests.get('http://localhost:5000/api/clientes')
    clientes = j_prod.json()    
    return render_template('clientes.html', clientes=clientes)

# ---------------------------------------------------
# Ruta productos/agregar
@app.route('/productos/agregar')
def agregarProducto():
    return render_template('agregar_productos.html')

# Ruta productos/altaProducto - Envía a la BBDD el nuevo producto
@app.route('/productos/altaProducto', methods=['POST'])
def alta_productos(datos):
    datos = request.form
    #Productos.agregar()
    return jsonify(datos)

# Ruta productos/editar
@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def modificar_producto(id):
    campos = Productos.obtener("id",id)
    return render_template('modificar_productos.html', campos=campos)

# Ruta productos/eliminar
@app.route('/productos/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_producto(id):
    mensaje = Productos.eliminar(id)
    return f"<div style='width:100%; text-align: center;'><h1>El producto tratado tenía el id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3>    <hr><h2><a href='/productos'>Regresar a la página anterior 👆</a></h2><p></p><h2><a href='/'>Regresar a la página principal 👉</a></h2>"

# Ruta para guardar cambios de productos editados o agregados
@app.route('/productos/guardarProducto/<int:id>', methods=['POST'])
def guardarProducto(id):
    datos = request.form
    mensaje = Productos.actualizar(id, datos)
    return f"<div style='width:100%; text-align: center;'><h1>Producto a modificar con id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/'>Regrese a la página principal 👉</a></h2>"


#-----------------------------------------------------

# Ruta clientes/agregar
@app.route('/clientes/agregar')
def agregarCliente():
    return render_template('agregar_clientes.html')

# Ruta clientes/alta  - Envía a la BBDD el nuevo cliente
@app.route('/clientes/altaCliente', methods=['POST'])
def alta_clientes():
    datos = request.form
    datosB = datos
    # Convertir a lista de tuplas modificable
    datos_modificables = [(key, value) for key, value in datosB.items()]
    # Agregar campo "activo" con valor específico (ejemplo)
    if len(datos_modificables) < 4:
        datos_modificables.append(('activo', 0))  # Aquí agregamos 'activo' con valor 0 ya que no existía el valor en el POST
    else:
        # Eliminar el último elemento de la lista que se carga como "1"
        datos_modificables.append(('activo', 1)) # Y lo incluimos como 1
    data = dict(datos_modificables)
    mensaje = Clientes.guardar_db(data)
    return f"<div style='width:100%; text-align: center;'><h1>Cliente a modificar con id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/clientes'>Regresar a la página anterior 👆</a></h2><p></p><h2><a href='/'>Regresar a la página principal 👉</a></h2>"
    

# Ruta clientes/editar/
@app.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
def modificar_cliente(id):
    campos = Clientes.obtener("id",id)
    return render_template('modificar_clientes.html', campos=campos)

# Ruta para guardar cambios de clientes editados o agregados
@app.route('/clientes/guardarCliente/<int:id>', methods=['POST'])
def guardarCliente(id):
    datos_formulario = request.form
    datos_inmutables = datos_formulario
    # Convertir a lista de tuplas modificable
    datos_modificables = [(key, value) for key, value in datos_inmutables.items()]
    # Agregar campo "activo" con valor específico (ejemplo)
    activo = 1 if datos_formulario.get('activo') == 'on' else 0
    if len(datos_modificables) == 4:
        # Eliminar el último elemento de la lista
        datos_modificables.pop()
    datos_modificables.append(('activo', activo))  # Aquí agregamos 'activo' con valor 1
    datos = dict(datos_modificables)
    mensaje = Clientes.actualizar(id, datos)
    return f"<div style='width:100%; text-align: center;'><h1>Cliente a modificar con id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/clientes'>Regresar a la página anterior 👆</a></h2><p></p><h2><a href='/'>Regresar a la página principal 👉</a></h2>"

# Ruta clientes/eliminar
@app.route('/clientes/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_cliente(id):
    mensaje = Clientes.eliminar(id)
    return f"<div style='width:100%; text-align: center;'><h1>El cliente tratado tenía el id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/'>Regrese a la página principal 👉</a></h2>"
    #return redirect(url_for('inicio'))
