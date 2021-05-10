
from datetime import date, time
from model.solicitacao_acesso import SolicitacaoAcessoModel

from flask_restful import Resource, reqparse, request

from util.user_authentication import token_required
from util.http_codes import NOT_FOUND_REQUEST, BAD_REQUEST, FORBIDDEN_REQUEST, CREATED, OK


class RecrsSolicitacaoAcesso(Resource):
    
    ENDPOINT = 'solicitacao_acesso'
    ROUTE = '/solicitacoes_acessos/solicitacao_acesso'

    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument("id_usuario", type=int, required=True, help="Precisa do argumento id_usuario na solicitação para acessar a solicitação do mesmo.")
        self.__parser.add_argument("id_solicitacao_acesso", type=int, required=True, help="Precisa do argumento id_solicitação_acesso na solicitação para acessar a solicitação do mesmo.")

    @token_required
    def get(self, current_user):
        
        args = self.__parser.parse_args(strict=True)
        id_usuario = args.get("id_usuario")

        if not id_usuario:
            return {'message':'argumento id_usuario vazio.'}, BAD_REQUEST

        solicitacaoAcesso = SolicitacaoAcessoModel.find_by_id_usuario(id_usuario)
        if not solicitacaoAcesso:
            return {'message':'solicitação para este uduário não existe'}, NOT_FOUND_REQUEST

        return solicitacaoAcesso.serialize(), OK
    
    @token_required
    def post(self, current_user):

        solicitacao_dict = request.json
        if not solicitacao_dict:
            return {'message':'arquivo json não enviado'}, BAD_REQUEST
        
        # TODO: Verify if accesses already was posted
        solicitacaoAcesso = SolicitacaoAcessoModel.find_by_id(solicitacao_dict['id_solicitacao_acesso'])
        if solicitacaoAcesso:
            return {'message':'esta solicitacão já foi reslizada.'}, BAD_REQUEST 


        # FIXME: Remove this validations data and add property in SolicitacaoAcessoModel
        day, month, year = solicitacao_dict['data'].split('-')
        solicitacao_dict['data'] = date(day=int(day), month=int(month), year=int(year))
        
        hour_inic, minute_inic, second_inic = solicitacao_dict['hora_inicio'].split(':')
        solicitacao_dict['hora_inicio'] = time(hour=int(hour_inic), minute=int(minute_inic), second=int(second_inic))

        hour_fim, minute_fim, second_fim = solicitacao_dict['hora_fim'].split(':')
        solicitacao_dict['hora_fim'] = time(hour=int(hour_fim), minute=int(minute_fim), second=int(second_fim))
        
        novaSolicitacao = SolicitacaoAcessoModel(**solicitacao_dict)
        SolicitacaoAcessoModel.save_to_db(novaSolicitacao)

        return {'message':'solicitado realizada.'}, CREATED
    
    @token_required
    def put(self, current_user):

        solicitacao_dict = request.json
        if not solicitacao_dict:
            return {'message':'arquivo json não enviado'}, BAD_REQUEST

        novaSolicitacao = SolicitacaoAcessoModel(**solicitacao_dict)

        SolicitacaoAcessoModel.save_to_db(novaSolicitacao)

        return {'message':'solicitado realizada.'}, CREATED


    @token_required
    def delete(self, current_user):
        
        try:
            args = self.__parser.parse_args()
            id_solicitacao_acesso = args.get('id_solicitacao_acesso')
        except:

            return {'message':'id_solicitacao_acesso está vazio.'}, BAD_REQUEST

        solicitacaoAcesso = SolicitacaoAcessoModel.find_by_id(id_solicitacao_acesso)

        if not solicitacaoAcesso:
            return {'message':'esta solicitacao_acesso não existe'}, NOT_FOUND_REQUEST

        SolicitacaoAcessoModel.delete_from_db(solicitacaoAcesso)

        return {'message':f'acesso solicitado por {solicitacaoAcesso.nome} excluído'}, OK

class RecrsListaSolicitacaoAcesso(Resource):
    
    ENDPOINT = 'solicitacoes_acessos'
    ROUTE = '/solicitacoes_acessos'
    
    @token_required
    def get(self, current_user):
        return [solicitacao.serialize() for solicitacao in SolicitacaoAcessoModel.query_all()]

