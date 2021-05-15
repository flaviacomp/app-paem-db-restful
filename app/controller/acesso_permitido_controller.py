from ..model import AcessoPermitidoModel
from .base_controller import BaseController

class AcessoPermitidoController(BaseController):
    
    @classmethod
    def get(self, id):
        super().get_by_id(id, AcessoPermitidoModel)

    @classmethod
    def post(self, body):
        super().post(body, AcessoPermitidoModel)

    @classmethod
    def put(self, body):
        super().put(body, AcessoPermitidoModel)

    @classmethod
    def delete(self, id):
        super().delete(id,AcessoPermitidoModel)
    
    @classmethod
    def get_list(self):
        super().get_list(AcessoPermitidoModel)