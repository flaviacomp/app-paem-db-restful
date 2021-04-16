from app import api, app
from resources.recrs_usuario import RecrsUsuario, RecrsListaUsuario


if __name__=='__main__':
    
    api.add_resource(RecrsUsuario, RecrsUsuario.URL, endpoint=RecrsUsuario.END_POINT)
    api.add_resource(RecrsListaUsuario, RecrsListaUsuario.URL, endpoint=RecrsListaUsuario.END_POINT)
    
    app.run(debug=True)
