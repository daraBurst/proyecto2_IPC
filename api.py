from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin
from users import User
import json

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app, support_credentials=True)
Listado = []

@app.route('/v1/home')
def home_page():
    return render_template('index.html')

@app.route('/signup', methods=['GET'])
def signup():
    global Listado
    List = []
    for usuario in Listado:
        new_entry = {
            'usuario': usuario.getUsername(),
            'nombre': usuario.getName(),
            'password': usuario.getPassword()
        }
        List.append(new_entry)
    json_response = jsonify(List)
    return(json_response)

app.run()