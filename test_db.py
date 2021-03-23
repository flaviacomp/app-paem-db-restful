from flask import Flask
from flask_restful import request, Api, Resource
from resources.Usuario import Usuario, ListaUsuario
from resources.RecursoCampus import RecursoCampus, ListaRecursoCampus
from resources.Discente import Discente, ListaDiscente
from importdb.db import db
app = Flask(__name__)

# Configure to use our database.
str_connection = f"mysql://root:70x7=sempre@localhost/mydbpaem"
app.config['SQLALCHEMY_DATABASE_URI'] = str_connection
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)

api = Api(app)

class Inicio(Resource):
    def get(self):
        return "PAGINA DE TESTE."

api.add_resource(Inicio, '/')

api.add_resource(ListaUsuario, '/usuarios')
api.add_resource(Usuario, '/usuarios/<int:id_usuario>')

api.add_resource(ListaDiscente, '/discentes')
api.add_resource(Discente, '/discentes/<int:id_discente>')

# api.add_resource(ListaRecursoCampus, '/recursos_campus')
# api.add_resource(RecursoCampus, '/recursos_campus/<int:id_recurso_campus>')

if __name__=='__main__':
    app.run()