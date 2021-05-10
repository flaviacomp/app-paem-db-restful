# resource usuario
from flask_restful import Resource, reqparse

from util.user_authentication import token_required

from model.discente import DiscenteModel
from model.curso import CursoModel

class RecrsDiscente(Resource):
    
    ENDPOINT = 'discente'
    ROUTE = '/discentes/discente'


    def __init__(self):
        # args
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('matricula', type=str, required=True, help="Para acessar o recurso, precisa enviar a matícula.")

    @token_required
    def get(self, current_user):
      args = self.__parser.parse_args(strict=True)
      matricula = args.get('matricula')
      discente = DiscenteModel.find_by_matricula(matricula)
      return discente.serialize()
    
class RecrsListaDiscente(Resource):
      ENDPOINT = 'discentes'
      ROUTE = '/discentes'

      @token_required
      def get(self, current_user):
        discentes = DiscenteModel.query_all()
        return [discente.serialize() for discente in discentes]