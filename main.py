from app import api, app
from resources.recrs_usuario import RecrsUsuario, RecrsListaUsuario
from resources.recrs_solicitacao_acesso import RecrsSolicitacaoAcesso, RecrsListaSolicitacaoAcesso
from resources.recrs_acesso_permitido import RecrsAcessoPermitido, RecrsListaAcessoPermitido

if __name__=='__main__':
    
    api.add_resource(RecrsUsuario, RecrsUsuario.URL, endpoint=RecrsUsuario.END_POINT)
    api.add_resource(RecrsListaUsuario, RecrsListaUsuario.URL, endpoint=RecrsListaUsuario.END_POINT)
    
    api.add_resource(RecrsSolicitacaoAcesso, RecrsSolicitacaoAcesso.URL, endpoint=RecrsSolicitacaoAcesso.END_POINT)
    api.add_resource(RecrsListaSolicitacaoAcesso, RecrsListaSolicitacaoAcesso.URL, endpoint=RecrsListaSolicitacaoAcesso.END_POINT)
    
    api.add_resource(RecrsAcessoPermitido, RecrsAcessoPermitido.URL, endpoint=RecrsAcessoPermitido.END_POINT)
    api.add_resource(RecrsListaAcessoPermitido, RecrsListaAcessoPermitido.URL, endpoint=RecrsListaAcessoPermitido.END_POINT)

    app.run(debug=True)
