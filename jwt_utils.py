import jwt
import datetime

SECRET_KEY = 'supersecreto'  # Cambia esto en producción

# Generar token JWT

def generar_token(usuario_id):
    payload = {
        'usuario_id': usuario_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

# Verificar token JWT

def verificar_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['usuario_id']
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None
