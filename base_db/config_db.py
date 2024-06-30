import mysql.connector

config_dev = {
    "user": 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'backend_c24261_g19',
    
}

config_prod = {
    "user": "gastondeb",
    "password": "Ingreso01",
    "host": "gastondeb.mysql.pythonanywhere-services.com",
    "database": "gastondeb$tp2-cac",
}

conexion = mysql.connector.connect(**config)