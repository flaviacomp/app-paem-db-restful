# resource usuario
from flask_restful import Resource, reqparse, request
from ..controller import DiscenteController
from ..controller.auhorization import token_required


class DiscenteResource(Resource):
    
    ENDPOINT = 'discente'
    ROUTE = '/discentes/discente'
    
    # @token_required
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('matricula', type=str, required=True, help="You need to send query string maticula.")

        args = parser.parse_args(strict=True)

        matricula = args.get('matricula')
        
        return DiscenteController.get(matricula)

    # @token_required
    def post(self):
        discente_dict = request.json
        return DiscenteController.post(discente_dict)
      
    # @token_required
    def put(self):
        discente_dict = request.json
        return DiscenteController.put(discente_dict)

    # @token_required
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument('matricula', type=str, required=True, help="You need to send query string maticula.")

        args = parser.parse_args(strict=True)
        matricula = args.get("matricula")

        return DiscenteController.delete(matricula)


class ListaDiscenteResource(Resource):
      
      ENDPOINT = 'discentes'
      ROUTE = '/discentes'

      # @token_required
      def get(self):
          return DiscenteController.list()