# Clases que corresponden a entidades en la BBDD
from base_db.dml import Tabla
from base_db.config_db import conexion as con
from auxiliares.cifrado import encriptar

#class Nivel(Tabla):
#    tabla = 'nivel'
#    campos = ('id', 'nivel')
#    conexion = con
    
#    def __init__(self, valores):
#        super().crear(valores)
        
#class Docente(Tabla):
#    tabla = 'docente'
#    campos = ('id', 'nombre', 'apellido', 'cuit')
#    conexion = con
    
#    def __init__(self, valores):
#        super().crear(valores)

# copiado de la clase docente
class Celular(Tabla):
    
    tabla = 'celular'
    conexion = con
    campos = ('id', 'modelo', 'pantalla', 'precio')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)