from ..model import Resource, reqparse, request
from ..util import NOT_FOUND_REQUEST, BAD_REQUEST, FORBIDDEN_REQUEST, CREATED, OK
from ..controller import SolicitacaoAcessoController
from ..controller.auhorization import token_required


class SolicitacaoAcessoResource(Resource):
    
    ENDPOINT = 'solicitacao_acesso'
    ROUTE = '/solicitacoes_acessos/solicitacao_acesso'

    # @token_required
    def get(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument("id_usuario", type=int, required=True, help="Precisa do argumento id_usuario na solicitação para acessar a solicitação do mesmo.")

        args = self.__parser.parse_args(strict=True)
        id_usuario = args.get("id_usuario")

        return SolicitacaoAcessoController.get(id_usuario)

    # @token_required
    def post(self):
        body = request.json
        return SolicitacaoAcessoController.post(body)
            
    # @token_required
    def put(self):
        body = request.json
        return SolicitacaoAcessoController.put(body)

    # @token_required
    def delete(self, current_user):

        parser = reqparse.RequestParser()
        parser.add_argument("id_solicitacao_acesso", type=int, required=True, help="Precisa do argumento id_solicitação_acesso na solicitação para acessar a solicitação do mesmo.")
        
        args = self.__parser.parse_args()
        id_solicitacao_acesso = args.get('id_solicitacao_acesso')
        
        return SolicitacaoAcessoController.delete(id_solicitacao_acesso)

class ListaSolicitacaoAcessoResource(Resource):
    
    ENDPOINT = 'solicitacoes_acessos'
    ROUTE = '/solicitacoes_acessos'
    
    # @token_required
    def get(self, current_user):
        return SolicitacaoAcessoController.get_list()

