from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_cors import CORS, cross_origin
from users import User
import json

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app, support_credentials=True)
Listado = []


Admin = User('Admin', 'Usuario Maestro', 'Admin')
Listado.append(Admin)


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
    username_exists = False

    for usuario in Listado:
        if username == usuario.getUsername():
            username_exists = True
            break
    if username_exists:
        return jsonify({
            'message': 'The username already exists',
            'status': 400
        })
    else:
        if password != confirm_pswrd:
            return jsonify({
                'message': 'The password does not match',
                'status': 400
                })
        else:
            new_entry = User(username, name, password)
            Listado.append(new_entry)
            return jsonify({
                'message': 'The user has been created',
                'status': 200
                })

'''
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
'''

@app.route('/v1/signin', methods=['POST'])
def Login():
    global Listado
    username = request.json['username']
    password = request.json['password']
    for usuario in Listado:
        if usuario.getUsername() == username and usuario.getPassword() == password:
            Dato = {
                'message': 'Success',
                'username': usuario.getUsername(),
                'status': 200
                }
            break
        else:
            Dato = {
                'message': 'The credencials are not valid',
                'username': '',
                'status': 400
            }
    respuesta = jsonify(Dato)
    return(respuesta)


@app.route('/v1/dashboard/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/v1/dashboard/user/')
def dashboard_user():
    return render_template('user.html')


@app.route('/v1/users/<string:username>', methods=['GET'])
def show_user(username):
    global Listado
    List = []
    for User in Listado:
        if User.getUsername() == username: 
            usuarios = {
                'username': User.getUsername(),
                'name': User.getName(),
                'password': User.getPassword()
                }
        List.append(usuarios)
    json_response = jsonify(List)
    return(json_response)


@app.route('/v1/users/all', methods=['GET'])
def show_all_usrs():
    global Listado
    List = []
    for usuario in Listado:
        usuarios = {
            'username': usuario.getUsername(),
            'name': usuario.getName(),
            'password': usuario.getPassword()
        }
        List.append(usuarios)
    json_response = jsonify(List)
    return(json_response)


@app.route('/v1/recover-password')
def recover_pswrd_page():
    return render_template('reset-pswrd.html')


@app.route('/v1/recover-password/<string:username>', methods=['GET'])
def recover_pswrd(username):
    global Listado
    for User in Listado:
        if User.getUsername() == username:
            Dato = {
                'message': User.getPassword(),
                'status': 200
            }
            break
        else:
            Dato = {
                'message': 'The username does not exist',
                'status': 400
            }
    respuesta = jsonify(Dato)
    return(respuesta)


@app.route('/v1/delete/<string:username>', methods=['DELETE'])
def remove_usr(username):
    global Listado
    for i in range(len(Listado)):
        if username == Listado[i].getUsername():
            del Listado[i]
            Dato = {
                'message': 'The user has been deleted',
                'status': 200
            }
            break
        else:
            Dato = {
                'message': 'The username does not exist',
                'status': 400
            }
    respuesta = jsonify(Dato)
    return(respuesta)     


@app.route('/v1/general')
def general():
    return render_template('contact-about.html')

app.run(threaded=True, port=5000)
