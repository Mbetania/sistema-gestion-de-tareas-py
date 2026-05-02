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
        return error, resp
    db = get_db()
    tareas = db.execute('SELECT id, descripcion, completada FROM tareas WHERE usuario_id = ?', (user['id'],)).fetchall()
    tareas_html = ''
    if tareas:
        tareas_html = '<ul>' + ''.join(
            f'<li>[ID: {t["id"]}] {t["descripcion"]} - {"✔️" if t["completada"] else "❌"}</li>' for t in tareas
        ) + '</ul>'
    else:
        tareas_html = '<p>No tienes tareas registradas.</p>'
    html = f'<h1>Bienvenido/a, {user["usuario"]}! Aquí puedes gestionar tus tareas.</h1>' + tareas_html
    return (html, 200)

@tareas_bp.route('/tareas/pendientes', methods=['GET'])
def tareas_pendientes():
    user, error, resp = autenticar()
    if error:
        return error, resp
    db = get_db()
    tareas = db.execute(
        'SELECT id, descripcion FROM tareas WHERE usuario_id = ? AND completada = 0', (user['id'],)
    ).fetchall()
    return jsonify([{'id': t['id'], 'descripcion': t['descripcion']} for t in tareas]), 200

@tareas_bp.route('/tareas/todas', methods=['GET'])
def todas_las_tareas():
    user, error, resp = autenticar()
    if error:
        return error, resp
    db = get_db()
    tareas = db.execute(
        'SELECT id, descripcion, completada FROM tareas WHERE usuario_id = ?', (user['id'],)
    ).fetchall()
    return jsonify([{'id': t['id'], 'descripcion': t['descripcion'], 'completada': bool(t['completada'])} for t in tareas]), 200

@tareas_bp.route('/tareas/<int:tarea_id>', methods=['PATCH'])
def completar_tarea(tarea_id):
    user, error, resp = autenticar()
    if error:
        return error, resp
    db = get_db()
    tarea = db.execute(
        'SELECT * FROM tareas WHERE id = ? AND usuario_id = ?', (tarea_id, user['id'])
    ).fetchone()
    if not tarea:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    db.execute('UPDATE tareas SET completada = 1 WHERE id = ?', (tarea_id,))
    db.commit()
    return jsonify({'mensaje': 'Tarea marcada como completada'}), 200

@tareas_bp.route('/tareas/completar', methods=['PATCH'])
def completar_varias_tareas():
    user, error, resp = autenticar()
    if error:
        return error, resp
    data = request.get_json()
    ids = data.get('ids') if data else None
    if not ids or not isinstance(ids, list):
        return jsonify({'error': 'Se esperaba {"ids": [1, 2, 3]}'}), 400
    db = get_db()
    completadas = []
    no_encontradas = []
    for tarea_id in ids:
        tarea = db.execute(
            'SELECT id FROM tareas WHERE id = ? AND usuario_id = ?', (tarea_id, user['id'])
        ).fetchone()
        if tarea:
            db.execute('UPDATE tareas SET completada = 1 WHERE id = ?', (tarea_id,))
            completadas.append(tarea_id)
        else:
            no_encontradas.append(tarea_id)
    db.commit()
    return jsonify({'completadas': completadas, 'no_encontradas': no_encontradas}), 200

@tareas_bp.route('/tareas', methods=['POST'])
def crear_tarea():
    user, error, resp = autenticar()
    if error:
        return error, resp
    data = request.get_json()
    descripcion = data.get('descripcion')
    if not descripcion:
        return jsonify({'error': 'Falta la descripción de la tarea'}), 400
    db = get_db()
    cursor = db.execute('INSERT INTO tareas (usuario_id, descripcion) VALUES (?, ?)', (user['id'], descripcion))
    db.commit()
    return jsonify({'mensaje': 'Tarea creada correctamente', 'id': cursor.lastrowid}), 201
