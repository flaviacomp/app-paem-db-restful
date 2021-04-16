# resource usuario
from datetime import datetime, timedelta

from flask_restful import Resource, request, output_json
import jwt

from app.user_authentication import verify_password, token_required
from app.http_codes import BAD_REQUEST, FORBIDDEN_REQUEST, NOT_FOUND_REQUEST, OK

from app import app
from model.usuario import UsuarioModel


class RecrsUsuario(Resource):
    END_POINT = 'login'
    URL = '/auth/token'

    def get(self):

        login = request.json['login']
        senha = request.json['senha']

        if not (login and senha):
            return {'massage':'login e senha vazios'}, BAD_REQUEST
        
        usuario = UsuarioModel.find_by_login(login)
        
        if not usuario:
            return {'massage':'usuário não existe'}, BAD_REQUEST

        if not verify_password(senha, usuario.senha):
            return {'massage':'senha inválida.'}, BAD_REQUEST
        
        payload = {
            "id": usuario.id_usuario,
            "exp": datetime.utcnow()+timedelta(minutes=30)
        }

        token = jwt.encode(payload, app.secret_key, algorithm='HS256')

        return {'token':token}, 

class RecrsListaUsuario(Resource):

    END_POINT = 'users'
    URL = '/auth/users'

    @token_required
    def get(self, current_user):
        myusuario = UsuarioModel.query_all()
        return [usuario.serialize() for usuario in myusuario], OK