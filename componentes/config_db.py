import mysql.connector

config_dev = {
    "user": 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'backend_c24261_g19',
    
}

conexion = mysql.connector.connect(**config_dev)