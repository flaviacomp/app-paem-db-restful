# resource usuario
from flask_restful import Resource
from model.RecursoCampus import RecursoCampusModel
class RecursoCampus(Resource):
    def get(self, id_recurso_campus):
      myrecurso = RecursoCampusModel.find_by_id(id_recurso_campus)
      return myrecurso.json()
    
class ListaRecursoCampus(Resource):
      def get(self):
        myrecursos = RecursoCampusModel.query_all()
        return [recurso.json() for recurso in myrecursos]