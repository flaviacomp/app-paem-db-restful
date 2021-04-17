from functools import wraps

from passlib.apps import custom_app_context

import jwt
from flask_restful import request,  current_app
from model.usuario import UsuarioModel

from .http_codes import BAD_REQUEST, UNAUTHORIZED_REQUEST, FORBIDDEN_REQUEST, OK, ACCEPTED

def verify_password(password, hashed_password):
    ''' Verify password hashed '''
    
    return custom_app_context.verify(password, hashed_password)

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        
        Bearer_token = None
        
        auth_key = 'Authorization'
        if auth_key in request.headers:
            Bearer_token = request.headers[auth_key]

        if not Bearer_token:
            return {'message':'acesso não autorizado.'}, UNAUTHORIZED_REQUEST

        if not ("Bearer" in Bearer_token):
            return {'message':'Token invalido'}, BAD_REQUEST

        try:

            token = Bearer_token.split()[1]
     
            data = jwt.decode(token, key=current_app.secret_key, algorithms='HS256')

            id_usuario = data['id']
            current_user = UsuarioModel.find_by_id(id_usuario)

        except:
            return {'message':'token invalido'}, BAD_REQUEST        
        
        return f(current_user=current_user, *args, **kwargs)
    
    return decorator

