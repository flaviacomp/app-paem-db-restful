
from app import api
from app import UsuarioResource, ListaUsuarioResource, AuthorizationToken
from app import DocenteResource, ListaDocenteResource
from app import DiscenteResource, ListaDiscenteResource
from app import TecnicoResource, ListaTecnicoResource
from app import DirecaoResource, ListaDirecaoResource
from app import CoordenacaoResource, ListaCoordenacaoResource
from app import CursoResource, ListaCursoResource
from app import DisciplinaResource, ListaDisciplinaResource
from app import CampusResource, ListaCampusResource
from app import SolicitacaoAcessoResource, ListaSolicitacaoAcessoResource
from app import AcessoPermitidoResource, ListaAcessoPermitidoResource
from app import RecursoCampusResource, ListaRecursoCampusResource

from getpass import getpass



def adicionar_recurso(Recurso):
    api.add_resource(Recurso, Recurso.ROUTE, endpoint=Recurso.ENDPOINT)

if __name__=='__main__':

    # Login and get token
    adicionar_recurso(AuthorizationToken)
    adicionar_recurso(UsuarioResource)
    adicionar_recurso(ListaUsuarioResource)

    adicionar_recurso(SolicitacaoAcessoResource)
    adicionar_recurso(ListaSolicitacaoAcessoResource)

    adicionar_recurso(AcessoPermitidoResource)
    adicionar_recurso(ListaAcessoPermitidoResource)

    adicionar_recurso(DiscenteResource)
    adicionar_recurso(ListaDiscenteResource)
    

    api.app.run(debug=True)
