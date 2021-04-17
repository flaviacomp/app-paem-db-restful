
from datetime import date, time
from model.solicitacao_acesso import SolicitacaoAcessoModel

from flask_restful import Resource, request

from util.user_authentication import token_required
from util.http_codes import NOT_FOUND_REQUEST, BAD_REQUEST, FORBIDDEN_REQUEST, CREATED, OK


class RecrsSolicitacaoAcesso(Resource):
    
    END_POINT = 'solicitacao_acesso'
    URL = '/solicitacoes_acessos/solicitacao_acesso'

    # @token_required
    def get(self):
        
        id = request.json['id']
        if not id:
            return {'message':'arquivo json não enviado'}, BAD_REQUEST

        solicitacaoAcesso = SolicitacaoAcessoModel.find_by_id(id)
        return solicitacaoAcesso.serialize(), OK
    
    # @token_required
    def post(self):

        solicitacao_dict = request.json
        if not solicitacao_dict:
            return {'message':'arquivo json não enviado'}, BAD_REQUEST

        day, month, year = solicitacao_dict['data'].split('-')
        solicitacao_dict['data'] = date(day=int(day), month=int(month), year=int(year))
        
        hour_inic, minute_inic, second_inic = solicitacao_dict['hora_inicio'].split(':')
        solicitacao_dict['hora_inicio'] = time(hour=int(hour_inic), minute=int(minute_inic), second=int(second_inic))

        hour_fim, minute_fim, second_fim = solicitacao_dict['hora_fim'].split(':')
        solicitacao_dict['hora_fim'] = time(hour=int(hour_fim), minute=int(minute_fim), second=int(second_fim))
        
        novaSolicitacao = SolicitacaoAcessoModel(**solicitacao_dict)
        SolicitacaoAcessoModel.save_to_db(novaSolicitacao)

        return {'message':'solicitado realizada.'}, CREATED
    
    def put(self):

        solicitacao_dict = request.json
        if not solicitacao_dict:
            return {'message':'arquivo json não enviado'}, BAD_REQUEST

        novaSolicitacao = SolicitacaoAcessoModel(**solicitacao_dict)
        SolicitacaoAcessoModel.save_to_db(novaSolicitacao)

        return {'message':'solicitado realizada.'}, CREATED


    # @token_required
    def delete(self):
        
        try:
            id = request.json['id']
        except:

            return {'message':'arquivo json não enviado'}, BAD_REQUEST

        solicitacaoAcesso = SolicitacaoAcessoModel.find_by_id(id)
        SolicitacaoAcessoModel.delete_from_db(solicitacaoAcesso)

        return {'message':f'acesso solicitado por {solicitacaoAcesso.nome} excluído'}, OK

class RecrsListaSolicitacaoAcesso(Resource):
    
    END_POINT = 'solicitacoes_acessos'
    URL = '/solicitacoes_acessos'
    
    # @token_required
    def get(self, current_user):
        return [solicitacao.serialize() for solicitacao in SolicitacaoAcessoModel.query_all()]


