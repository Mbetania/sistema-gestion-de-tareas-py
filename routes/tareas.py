from flask import Blueprint, request, jsonify, g
from db import get_db
import sqlite3
from jwt_utils import verificar_token

tareas_bp = Blueprint('tareas', __name__)


# Middleware para autenticación con JWT
def autenticar():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return None, jsonify({'error': 'Token requerido'}), 401
    token = auth_header.split(' ')[1]
    usuario_id = verificar_token(token)
    if not usuario_id:
        return None, jsonify({'error': 'Token inválido o expirado'}), 401
    db = get_db()
    user = db.execute('SELECT * FROM usuarios WHERE id = ?', (usuario_id,)).fetchone()
    if not user:
        return None, jsonify({'error': 'Usuario no encontrado'}), 401
    return user, None, None

@tareas_bp.route('/tareas', methods=['GET'])
def bienvenida_tareas():
    user, error, resp = autenticar()
    if error:
        return resp, 401
    db = get_db()
    tareas = db.execute('SELECT descripcion, completada FROM tareas WHERE usuario_id = ?', (user['id'],)).fetchall()
    tareas_html = ''
    if tareas:
        tareas_html = '<ul>' + ''.join(
            f'<li>{t["descripcion"]} - {"✔️" if t["completada"] else "❌"}</li>' for t in tareas
        ) + '</ul>'
    else:
        tareas_html = '<p>No tienes tareas registradas.</p>'
    html = f'<h1>Bienvenido/a, {user["usuario"]}! Aquí puedes gestionar tus tareas.</h1>' + tareas_html
    return (html, 200)

@tareas_bp.route('/tareas', methods=['POST'])
def crear_tarea():
    user, error, resp = autenticar()
    if error:
        return resp, 401
    data = request.get_json()
    descripcion = data.get('descripcion')
    if not descripcion:
        return jsonify({'error': 'Falta la descripción de la tarea'}), 400
    db = get_db()
    db.execute('INSERT INTO tareas (usuario_id, descripcion) VALUES (?, ?)', (user['id'], descripcion))
    db.commit()
    return jsonify({'mensaje': 'Tarea creada correctamente'}), 201
