from ..controller import AcessoPermitidoController
from ..controller.auhorization import token_required
from ..util import NOT_FOUND_REQUEST, BAD_REQUEST, CREATED, OK

from flask_restful import Resource, request, reqparse
from datetime import time

class AcessoPermitidoResource(Resource):
    
    ENDPOINT = 'acesso_permitido'
    ROUTE = '/acessos_permitidos/acesso_permitido'
        
    # @token_required
    def get(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument("id_acesso_permitido")

        args = self.__parser.parse_args()
        id_acesso_permitido = args.get("id_acesso_permitido")
        
        return AcessoPermitidoController.get(id_acesso_permitido)
    
    # @token_required
    def post(self, body):
        return AcessoPermitidoController.post(body)
    
    def put(self):
        body = request.json
        return AcessoPermitidoController.put()
    
    # @token_required
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id_acesso_permitido")

        args = self.__parser.parse_args()
        id_acesso_permitido = args.get("id_acesso_permitido")
        
        return AcessoPermitidoController.delete(id_acesso_permitido)
       

class ListaAcessoPermitidoResource(Resource):
    
    ENDPOINT = 'acessos_permitidos'
    ROUTE = '/acessos_permitidos'
    
    # @token_required
    def get(self):
        return AcessoPermitidoController.get_list()



