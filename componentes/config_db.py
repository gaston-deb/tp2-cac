from flask import Flask

app = Flask(__name__)

def inicio():
    return "TP Back_End_Python-C24261 G19"

if __name__ == "main":
    app.run()