from ..model import SolicitacaoAcessoModel
from .base_controller import BaseController

class SolicitacaoAcessoController(BaseController):
    
    @classmethod
    def get(self, id):
        return super().get_by_id(id, SolicitacaoAcessoModel)

    @classmethod
    def post(self, body):
        return super().post(body, SolicitacaoAcessoModel)

    @classmethod
    def put(self, body):
        return super().put(body, SolicitacaoAcessoModel)

    @classmethod
    def delete(self, id):
        return super().delete(id, SolicitacaoAcessoModel)

    @classmethod
    def get_list(self):
        return super().get_list(SolicitacaoAcessoModel)