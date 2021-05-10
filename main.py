from app import api, app
from resources.recrs_usuario import RecrsUsuario, RecrsListaUsuario
from resources.recrs_solicitacao_acesso import RecrsSolicitacaoAcesso, RecrsListaSolicitacaoAcesso
from resources.recrs_acesso_permitido import RecrsAcessoPermitido, RecrsListaAcessoPermitido
from resources.recrs_discente import RecrsDiscente, RecrsListaDiscente

def adicionar_recurso(Recurso):
    api.add_resource(Recurso, Recurso.ROUTE, endpoint=Recurso.ENDPOINT)

if __name__=='__main__':
    
    # Login and get token
    adicionar_recurso(RecrsUsuario)
    adicionar_recurso(RecrsListaUsuario)

    adicionar_recurso(RecrsSolicitacaoAcesso)
    adicionar_recurso(RecrsListaSolicitacaoAcesso)

    adicionar_recurso(RecrsAcessoPermitido)
    adicionar_recurso(RecrsListaAcessoPermitido)

    adicionar_recurso(RecrsDiscente)
    adicionar_recurso(RecrsListaDiscente)
    

    app.run(debug=True)
