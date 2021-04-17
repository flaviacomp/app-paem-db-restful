from model.acesso_permitido import AcessoPermitidoModel

from datetime import date, time

from flask_restful import Resource, request

from util.user_authentication import token_required
from util.http_codes import NOT_FOUND_REQUEST, BAD_REQUEST, CREATED, OK


class RecrsAcessoPermitido(Resource):
    
    END_POINT = 'acesso_permitido'
    URL = '/acessos_permitidos/acesso_permitido'

    def get(self):
        
        try:
            id = request.json['id']
        except:

            return {'message':'arquivo json não enviado'}, BAD_REQUEST

        solicitacaoAcesso = AcessoPermitidoModel.find_by_id(id)
        
        return solicitacaoAcesso.serialize(), OK
    
    def post(self):
        
        acesso_permitido_dict = request.json
        
        if not acesso_permitido_dict:
            return {'message':'arquivo json não enviado'}, BAD_REQUEST

        hour_ent, minute_ent, second_ent = acesso_permitido_dict['hora_entrada'].split(':')
        acesso_permitido_dict['hora_entrada'] = time(hour=int(hour_ent), minute=int(minute_ent), second=int(second_ent))

        hour_sai, minute_sai, second_sai = acesso_permitido_dict['hora_saida'].split(':')
        acesso_permitido_dict['hora_saida'] = time(hour=int(hour_sai), minute=int(minute_sai), second=int(second_sai))

        novoAcessoPermitido = AcessoPermitidoModel(**acesso_permitido_dict)
        AcessoPermitidoModel.save_to_db(novoAcessoPermitido)

        return {'message':'acesso permitido foi criado.'}, CREATED
    
    def delete(self):
        
        try:
            id = request.json['id']
        except:

            return {'message':'arquivo json não enviado'}, BAD_REQUEST

        acessoPermitido = AcessoPermitidoModel.find_by_id(id)
        AcessoPermitidoModel.delete_from_db(acessoPermitido)

        return {'message':f'acesso permitido com id {acessoPermitido.id_acesso_permitido} excluído'}, OK

class RecrsListaAcessoPermitido(Resource):
    
    END_POINT = 'acessos_permitidos'
    URL = '/acessos_permitidos'
    
    def get(self):
        return [acessoPermitido.serialize() for acessoPermitido in AcessoPermitidoModel.query_all()]



