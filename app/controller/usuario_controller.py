from .auhorization import verify_password
from ..model import UsuarioModel, app
from ..util import BAD_REQUEST, OK
from .base_controller import BaseController

from datetime import timedelta, datetime
import jwt

class UsuarioController(BaseController):

    @classmethod
    def get_token(cls, login, senha):
        
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

    @classmethod
    def get(cls, id):
        return super().get_by_id(id, UsuarioModel)

    @classmethod
    def post(self, body):
        return super().post(body, UsuarioModel)

    @classmethod
    def put(self, body):
        return super().put(body)
    
    @classmethod
    def delete(self, id):
        return super().delete(id, UsuarioModel)
    
    @classmethod
    def get_list(cls):
        return super().list_get(UsuarioModel)