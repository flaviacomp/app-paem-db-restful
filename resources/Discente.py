# resource usuario
from flask_restful import Resource
from model.Discente import DiscenteModel
class Discente(Resource):
    def get(self, id_discente):
      mydiscente = DiscenteModel.find_by_id(id_discente)
      return mydiscente.json()
    
class ListaDiscente(Resource):
      def get(self):
        mydiscentes = DiscenteModel.query_all()
        return [discente.json() for discente in mydiscentes]