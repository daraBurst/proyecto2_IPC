from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_cors import CORS, cross_origin
from users import User
import json

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app, support_credentials=True)
Listado = []

@app.route('/')
def index():
    return redirect(url_for('home_page'))


@app.route('/v1/home')
def home_page():
    return render_template('index.html')


@app.route('/v1/signup', methods=['POST'])
def signup():
    global Listado
    username = request.json['username']
    name = request.json['name']
    password = request.json['password']
    confirm_pswrd = request.json['confirm_pswrd']
    if len(Listado) > 0:
        for usuario in Listado:
            if usuario.getUsername() == username:
                return jsonify({
                    'message': 'Failed',
                    'reason': 'El nombre de usuario ya existe.'
                    })
            else:
                if password != confirm_pswrd:
                    return jsonify({
                        'message': 'Failed',
                        'reason': 'Las contraseñas no coinciden.'
                        })
                else:
                    new_entry = User(username, name, password)
                    Listado.append(new_entry)
                    return jsonify({
                        'message': 'Success',
                        'reason': 'Se ha creado un nuevo usuario.'
                        })
    else:
        if password != confirm_pswrd:
            return jsonify({
                'message': 'Failed',
                'reason': 'Las contraseñas no coinciden.'
                })
        else:
            new_entry = User(username, name, password)
            Listado.append(new_entry)
            return jsonify({
                'message': 'Success',
                'reason': 'Se ha creado un nuevo usuario.'
                })


@app.route('/v1/users/all', methods=['GET'])
def show_all_usrs():
    global Listado
    List = []
    for usuario in Listado:
        usuarios = {
            'usuario': usuario.getUsername(),
            'nombre': usuario.getName(),
            'password': usuario.getPassword()
        }
        List.append(usuarios)
    json_response = jsonify(List)
    return(json_response)


@app.route('/v1/recover-password', methods=['GET'])
def recover_pswrd():
    global Listado
    username = request.json['username']
    for usuario in Listado:
        if usuario.getUsername() == username:
            response = usuario.getPassword()
            return jsonify(response)
        else:
            return jsonify({
                'message': 'Failed',
                'reason': 'El nombre de usuario no existe.'
                })
            



app.run()