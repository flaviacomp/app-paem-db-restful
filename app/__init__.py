from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:70x7=sempre@localhost/mydbpaem" #"mysql://{server_user}:{server_pwd}@{server}/{db_name}"
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)

api = Api(app)


