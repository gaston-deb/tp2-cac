
from base_db.dml import Tabla
from base_db.config_db import conexion as con
from auxiliares.cifrado import encriptar


class Productos(Tabla):
    
    tabla = 'productos'
    conexion = con
    campos = ('id', 'tipo', 'marca', 'modelo', 'detalle', 'precio', 'imagen', 'estado')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)

class Clientes(Tabla):

    tabla = 'clientes'
    conexion = con
    campos = ('id', 'nombre', 'email', 'telefono', 'activo')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)