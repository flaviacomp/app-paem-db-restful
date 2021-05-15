from .usuario import UsuarioModel
from .discente import DiscenteModel
from .docente import DocenteModel
from .tecnico import TecnicoModel
from .portaria import PortariaModel
from .coordenacao import CoordenacaoModel
from .curso import CursoModel
from .campus import CampusModel
from .solicitacao_acesso import SolicitacaoAcessoModel
from .acesso_permitido import AcessoPermitidoModel
from .recurso_campus import RecursoCampusModel
from .reserva_recurso_servidores import ReservaRecursoServidoresModel
from .direcao import DirecaoModel

from flask_restful import Api
from flask_restful import Resource
from flask_restful import request
from flask_restful import reqparse

from ..database import app

api = Api(app)




