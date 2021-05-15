# resource usuario
from ..controller import UsuarioController
from ..controller.auhorization import token_required
from ..util import BAD_REQUEST, FORBIDDEN_REQUEST, NOT_FOUND_REQUEST, OK
from flask_restful import Resource, reqparse, request
from ..controller import UsuarioController

class UsuarioResource(Resource):
    ENDPOINT = 'usuario'
    ROUTE = '/usuario'

    # @token_required
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id_usuario', type=str, required=True, help="You need to send query string id_usuario.")

        args = parser.parse_args(strict=True)
        id_usuario = args.get('id_usuario')
        
        return UsuarioController.get(id_usuario)

    # @token_required
    def post(self):
        body = request.json
        return UsuarioController.post(body)
      
    # @token_required
    def put(self):
        body = request.json
        return UsuarioController.put(body)

    # @token_required
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id_usuario', type=str, required=True, help="You need to send query string id_usuario.")

        args = parser.parse_args(strict=True)
        id_usuario = args.get('id_usuario')

        return UsuarioController.delete(id_usuario)

class AuthorizationToken(Resource):
    
    ENDPOINT = 'login'
    ROUTE = '/login'
    
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('login', required=True, type=str, help="Parametro login não encontrado na requisição.")
        self.__parser.add_argument('senha', required=True, type=str, help="Parametro senha não encontrado na requisição.")
        self.__parser.add_argument('cpf', type=str, help="Parametro cpf não encontrado na requisição.")

    def get(self):
        
        args = self.__parser.parse_args()
        login = args.get("login")
        senha = args.get("senha")

        return UsuarioController.get_token(login, senha)

class ListaUsuarioResource(Resource):

    ENDPOINT = 'users'
    ROUTE = '/users'

    # @token_required
    def get(self):
        return UsuarioController.get_list()