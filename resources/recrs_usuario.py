# resource usuario
from datetime import datetime, timedelta

from flask_restful import Resource, reqparse 
import jwt

from util.user_authentication import verify_password, token_required
from util.http_codes import BAD_REQUEST, FORBIDDEN_REQUEST, NOT_FOUND_REQUEST, OK

from app import app
from model.usuario import UsuarioModel


class RecrsUsuario(Resource):
    ENDPOINT = 'login'
    ROUTE = '/login'

    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('login', required=True, type=str, help="Parametro login não encontrado na requisição.")
        self.__parser.add_argument('senha', required=True, type=str, help="Parametro senha não encontrado na requisição.")

    def get(self):
        
        args = self.__parser.parse_args()
        login = args.get("login")
        senha = args.get("senha")

        if not (login and senha):
            return {'massage':'login e senha vazios'}, BAD_REQUEST
        
        usuario = UsuarioModel.find_by_login(login)
        
        if not usuario:
            return {'massage':'usuário não existe'}, BAD_REQUEST

        if not verify_password(senha, usuario.senha):
            return {'massage':'senha inválida.'}, BAD_REQUEST
        
        payload = {
            "id": usuario.id_usuario,
            "exp": datetime.utcnow()+timedelta(minutes=60)
        }

        token = jwt.encode(payload, app.secret_key, algorithm='HS256')

        return {'token':token}

class RecrsListaUsuario(Resource):

    ENDPOINT = 'users'
    ROUTE = '/users'

    @token_required
    def get(self, current_user):
        myusuario = UsuarioModel.query_all()
        return [usuario.serialize() for usuario in myusuario], OK