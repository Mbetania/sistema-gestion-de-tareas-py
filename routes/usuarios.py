from flask import Blueprint, request, jsonify
from db import get_db
from utils import hash_password, verify_password
from jwt_utils import generar_token
import sqlite3

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    usuario = data.get('usuario')
    password = data.get('password')
    if not usuario or not password:
        return jsonify({'error': 'Faltan datos'}), 400
    db = get_db()
    try:
        hash_pass = hash_password(password)
        db.execute('INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)', (usuario, hash_pass))
        db.commit()
        return jsonify({'mensaje': 'Usuario registrado correctamente'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El usuario ya existe'}), 409


# Endpoint para login de usuarios
@usuarios_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    password = data.get('password')
    if not usuario or not password:
        return jsonify({'error': 'Faltan datos'}), 400
    db = get_db()
    user = db.execute('SELECT * FROM usuarios WHERE usuario = ?', (usuario,)).fetchone()
    if user and verify_password(password, user['contrasena']):
        token = generar_token(user['id'])
        return jsonify({'mensaje': 'Login exitoso', 'token': token}), 200
    else:
        return jsonify({'error': 'Credenciales inválidas'}), 401
