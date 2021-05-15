from ..model import DiscenteModel
from ..model import CursoModel
from ..util import OK, CREATED, BAD_REQUEST, NOT_FOUND_REQUEST


class DiscenteController:
    
    @classmethod
    def get(cls, matricula):

        discente = DiscenteModel.find_by_matricula(matricula)
        if not discente:
            return {"message":"Not found this discente."}, NOT_FOUND_REQUEST
      
        return discente.serialize(), OK

    @classmethod
    def post(cls, discente_dict):

        if not discente_dict:
            return {"message":"Not found body data with discente."}, BAD_REQUEST
      
        matricula = discente_dict.get("matricula")

        discente = DiscenteModel.find_by_matricula(matricula)
        if discente:
            DiscenteModel.update_by_matricula(matricula, discente_dict)
            return {"message":"Discente updated"}, OK

        print(discente_dict)
        new_discente = DiscenteModel(**discente_dict)
        new_discente.save_to_db()

        return {"message":"Discente added"}, CREATED

    @classmethod
    def put(cls, discente_dict):

        if not discente_dict:
            return {"message":"Not found body data with discente."}, BAD_REQUEST
        
        matricula = discente_dict.get("matricula")

        discente = DiscenteModel.find_by_matricula(matricula)
        if not discente:
            return {"message":"No found id_discente."}, BAD_REQUEST

        DiscenteModel.update_by_matricula(matricula, discente_dict)
        
        return {"message":"Discente updated"}, OK

    @classmethod
    def delete(cls, matricula):
        
        discente = DiscenteModel.find_by_matricula(matricula)
        
        if not discente:
            return {"message":"Can't delete, not found this discente."}, BAD_REQUEST
        
        discente.delete_from_db()

        return {"message":f"discente {discente.nome} deleted."}, OK

    @classmethod
    def list(cls):
        discentes = DiscenteModel.query_all()
        return [discente.serialize() for discente in discentes]