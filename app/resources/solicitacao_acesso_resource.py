from ..util import NOT_FOUND_REQUEST, BAD_REQUEST, FORBIDDEN_REQUEST, CREATED, OK
from ..controller import SolicitacaoAcessoController
from ..controller.auhorization import token_required

from flask_restful import Resource, reqparse, request

class SolicitacaoAcessoResource(Resource):
    
    ENDPOINT = 'solicitacaos_acessos'
    ROUTE = '/solicitacoes_acessos/solicitacao_acesso'

    # @token_required
    def get(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument("id_discente", type=int, help="Required query string integer id_discente.")
        parser.add_argument("id_solicitacao_acesso", type=int, help="Required query string integer id_solicitacao_acesso.")
        
        args = parser.parse_args(strict=True)
        id_solicitacao_acesso = args.get("id_solicitacao_acesso")
        id_discente = args.get("id_discente")

        if id_discente:
            return SolicitacaoAcessoController.get_id_discente(id_discente)

        if id_solicitacao_acesso:
            return SolicitacaoAcessoController.get(id_solicitacao_acesso)    

        return {"message":"Required query string id_solicitacao_acesso or id_discente."}, BAD_REQUEST

    # @token_required
    def post(self):
        body = request.json
        return SolicitacaoAcessoController.post(body)
            
    # @token_required
    def put(self):
        body = request.json
        return SolicitacaoAcessoController.put(body)

    # @token_required
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument("id_solicitacao_acesso", type=int, required=True, help="Precisa do argumento id_solicitação_acesso na solicitação para acessar a solicitação do mesmo.")
        
        args = parser.parse_args()
        id_solicitacao_acesso = args.get('id_solicitacao_acesso')
        
        return SolicitacaoAcessoController.delete(id_solicitacao_acesso)

class ListaSolicitacaoAcessoResource(Resource):
    
    ENDPOINT = 'solicitacoes_acesso'
    ROUTE = '/solicitacoes_acessos'
    
    # @token_required
    def get(self):
        return SolicitacaoAcessoController.get_list()

