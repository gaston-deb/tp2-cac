from flask import render_template
from flask import request
from flask import render_template
from app import app
from componentes.modelos import Productos
from componentes.modelos import Clientes

@app.route('/')
def inicio():
    return render_template('principal.html')

# Ruta Productos
@app.route('/productos')
def productos():
    productos = Productos.obtener()
    return render_template('productos.html', productos=productos)

# Ruta Clientes
@app.route('/clientes')
def clientes():
    clientes = Clientes.obtener()
    return render_template('clientes.html', clientes=clientes)

# ---------------------------------------------------
# Ruta productos/agregar
@app.route('/productos/agregar')
def agregarProducto():
    return render_template('agregar_productos.html')

# Ruta productos/altaProducto - Envía a la BBDD el nuevo producto
@app.route('/productos/altaProducto', methods=['POST'])
def alta_productos():
    # datos = request.form
    # producto = Productos()
    # mensaje = producto.guardar_db(datos)
    datos = request.form.to_dict()
    
    # Convertir el campo 'precio' a float
    if 'precio' in datos:
        try:
            datos['precio'] = float(datos['precio'])
        except ValueError:
            return "Error: El precio debe ser un número válido."
    
    producto = Productos()
    mensaje = producto.guardar_db(datos)
    return f"<div style='width:80%; margin-top:40px; padding: 30px; text-align: center; background-color: #8CFDB4;'><h1>Agregar Producto</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/productos'>Regresar a la página anterior 👆</a></h2><p></p><h2><a href='/'>Regresar a la página principal 👉</a></h2>"
    

# Ruta productos/editar
@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def modificar_producto(id):
    campos = Productos.obtener("id",id)
    return render_template('modificar_productos.html', campos=campos)

# Ruta productos/eliminar
@app.route('/productos/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_producto(id):
    mensaje = Productos.eliminar(id)
    return f"<div style='width:80%; margin-top:40px; padding: 30px; text-align: center; background-color: #8CFDB4;'><h1>El producto tratado tenía el id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3>    <hr><h2><a href='/productos'>Regresar a la página anterior 👆</a></h2><p></p><h2><a href='/'>Regresar a la página principal 👉</a></h2>"

# Ruta para guardar cambios de productos editados o agregados
@app.route('/productos/guardarProducto/<int:id>', methods=['POST'])
def guardarProducto(id):
    datos = request.form
    mensaje = Productos.actualizar(id, datos)
    return f"<div style='width:80%; margin-top:40px; padding: 30px; text-align: center; background-color: #8CFDB4;'><h1>Producto a modificar con id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/productos'>Regresar a la página anterior 👆</a></h2><p></p><h2><a href='/'>Regresar a la página principal 👉</a></h2>"


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
    cliente = Clientes()
    mensaje = cliente.guardar_db(data)
    return f"<div style='width:80%; margin-top:40px; padding: 30px; text-align: center; background-color: #8CFDB4;'><h1>Agregar Cliente</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/clientes'>Regresar a la página anterior 👆</a></h2><p></p><h2><a href='/'>Regresar a la página principal 👉</a></h2>"
    

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
    return f"<div style='width:80%; margin-top:40px; padding: 30px; text-align: center; background-color: #8CFDB4;'><h1>Cliente a modificar con id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/clientes'>Regresar a la página anterior 👆</a></h2><p></p><h2><a href='/'>Regresar a la página principal 👉</a></h2>"

# Ruta clientes/eliminar
@app.route('/clientes/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_cliente(id):
    mensaje = Clientes.eliminar(id)
    return f"<div style='width:80%; margin-top:40px; padding: 30px; text-align: center; background-color: #8CFDB4;'><h1>El cliente tratado tenía el id Nº {id}</h1><hr><h3>Estado: {mensaje}</h3><hr><h2><a href='/clientes'>Regresar a la página anterior 👆</a></h2><p></p><h2><a href='/'>Regresar a la página principal 👉</a></h2>"
    #return redirect(url_for('inicio'))