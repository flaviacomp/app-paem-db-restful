from flask import Flask
from flask_restful import request, Api
from resources.Usuario import Usuario
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

api.add_resource(Usuario, '/<int:id_usuario>')

if __name__=='__main__':
    app.run()