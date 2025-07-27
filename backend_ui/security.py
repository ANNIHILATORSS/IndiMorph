import os
import jwt
from flask import request, jsonify
from functools import wraps

JWT_SECRET = os.environ.get('JWT_SECRET', 'changeme')


def encode_auth_token(user_id):
    return jwt.encode({'user_id': user_id}, JWT_SECRET, algorithm='HS256')

def decode_auth_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return payload['user_id']
    except Exception:
        return None

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization', None)
        if not auth or not auth.startswith('Bearer '):
            return jsonify({'error': 'Missing or invalid token'}), 401
        token = auth.split(' ')[1]
        user_id = decode_auth_token(token)
        if not user_id:
            return jsonify({'error': 'Invalid token'}), 401
        return f(*args, **kwargs)
    return decorated 