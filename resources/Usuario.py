# resource usuario
from flask_restful import Resource
from model.Usuario import UsuarioModel
class Usuario(Resource):
    def get(self, id_usuario):
      myusuario = UsuarioModel.find_by_id(id_usuario)
      return myusuario.json()
    
class ListaUsuario(Resource):
      def get(self):
        myusuario = UsuarioModel.query_all()
        return [usuario.json() for usuario in myusuario]

        