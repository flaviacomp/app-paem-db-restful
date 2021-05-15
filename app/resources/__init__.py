from ..model import api
api.prefix = '/api.paem'

from .usuario_resource import UsuarioResource, ListaUsuarioResource, AuthorizationToken
from .docente_resource import DocenteResource, ListaDocenteResource
from .discente_resource import DiscenteResource, ListaDiscenteResource
from .tecnico_resource import TecnicoResource, ListaTecnicoResource
from .direcao_resource import DirecaoResource, ListaDirecaoResource
from .coordenacao_resource import CoordenacaoResource, ListaCoordenacaoResource
from .curso_resource import CursoResource, ListaCursoResource
from .disciplina_resource import DisciplinaResource, ListaDisciplinaResource
from .campus_resource import CampusResource, ListaCampusResource
from .solicitacao_acesso_resource import SolicitacaoAcessoResource, ListaSolicitacaoAcessoResource
from .acesso_permitido_resource import AcessoPermitidoResource, ListaAcessoPermitidoResource
from .recurso_campus_resource import RecursoCampusResource, ListaRecursoCampusResource
