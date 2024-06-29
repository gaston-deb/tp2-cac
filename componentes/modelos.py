
from base_db.dml import Tabla
from base_db.config_db import conexion as con
from auxiliares.cifrado import encriptar


class Celular(Tabla):
    
    tabla = 'celular'
    conexion = con
    campos = ('id', 'modelo', 'img_url', 'precio')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)

class Accesorio(Tabla):

    tabla = 'accesorio'
    conexion = con
    campos = ('id', 'modelo', 'img_url', 'precio')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)