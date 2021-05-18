from .resources import AuthorizationResource
from .resources import UsuarioResource, ListaUsuarioResource
from .resources import DocenteResource, ListaDocenteResource
from .resources import DiscenteResource, ListaDiscenteResource
from .resources import TecnicoResource, ListaTecnicoResource
from .resources import DirecaoResource, ListaDirecaoResource
from .resources import CoordenacaoResource, ListaCoordenacaoResource
from .resources import CursoResource, ListaCursoResource
from .resources import DisciplinaResource, ListaDisciplinaResource
from .resources import CampusResource, ListaCampusResource
from .resources import SolicitacaoAcessoResource, ListaSolicitacaoAcessoResource
from .resources import AcessoPermitidoResource, ListaAcessoPermitidoResource
from .resources import RecursoCampusResource, ListaRecursoCampusResource

from .resources import app

from flask_restful import Api

api = Api(app)
api.prefix = '/api.paem'
