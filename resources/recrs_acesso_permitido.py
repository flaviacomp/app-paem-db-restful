from model.acesso_permitido import AcessoPermitidoModel

from datetime import date, time

from flask_restful import Resource, reqparse, request

from util.user_authentication import token_required
from util.http_codes import NOT_FOUND_REQUEST, BAD_REQUEST, CREATED, OK


class RecrsAcessoPermitido(Resource):
    
    ENDPOINT = 'acesso_permitido'
    ROUTE = '/acessos_permitidos/acesso_permitido'

    def __init__(self):

        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument("id_acesso_permitido")
        
    @token_required
    def get(self, current_user):

        args = self.__parser.parse_args()

        id_acesso_permitido = args.get("id_acesso_permitido")

        if not id_acesso_permitido:
            return {'message':'id_acesso_permitido está vazio.'}, BAD_REQUEST

        acessoPermitido = AcessoPermitidoModel.find_by_id(id_acesso_permitido)

        if not acessoPermitido:
            return {'message':'esta solicitacao_acesso não existe'}, NOT_FOUND_REQUEST
        
        return acessoPermitido.serialize(), OK
    
    @token_required
    def post(self, current_user):
        
        acesso_permitido_dict = request.json
        
        if not acesso_permitido_dict:
            return {'message':'arquivo json não enviado'}, BAD_REQUEST
        
        # TODO: Verify if acesso_permitido already was posted
        acessoPermitido = AcessoPermitidoModel.find_by_id(acesso_permitido_dict['id_acesso_permitido'])
        if acessoPermitido:
            return {'message':'esta acesso_permitido já foi reslizado.'}, BAD_REQUEST 


        # FIXME: Remove this validations data and add property in AcessoPermitidoModel
        hour_ent, minute_ent, second_ent = acesso_permitido_dict['hora_entrada'].split(':')
        acesso_permitido_dict['hora_entrada'] = time(hour=int(hour_ent), minute=int(minute_ent), second=int(second_ent))

        hour_sai, minute_sai, second_sai = acesso_permitido_dict['hora_saida'].split(':')
        acesso_permitido_dict['hora_saida'] = time(hour=int(hour_sai), minute=int(minute_sai), second=int(second_sai))

        novoAcessoPermitido = AcessoPermitidoModel(**acesso_permitido_dict)
        AcessoPermitidoModel.save_to_db(novoAcessoPermitido)

        return {'message':'acesso permitido foi criado.'}, CREATED
    
    @token_required
    def delete(self, current_user):
        
        args = self.__parser.parse_args()

        id_acesso_permitido = args.get("id_acesso_permitido")
    
        if not id_acesso_permitido:
           return {'message':'id_acesso_permitido está vazio.'}, BAD_REQUEST

        acessoPermitido = AcessoPermitidoModel.find_by_id(id_acesso_permitido)

        if not acessoPermitido:
            return {'message':'esta acesso_permitido não existe'}, NOT_FOUND_REQUEST

        AcessoPermitidoModel.delete_from_db(acessoPermitido)

        return {'message':f'acesso permitido com id {acessoPermitido.id_acesso_permitido} excluído'}, OK

class RecrsListaAcessoPermitido(Resource):
    
    ENDPOINT = 'acessos_permitidos'
    ROUTE = '/acessos_permitidos'
    
    @token_required
    def get(self, current_user):
        return [acessoPermitido.serialize() for acessoPermitido in AcessoPermitidoModel.query_all()]



