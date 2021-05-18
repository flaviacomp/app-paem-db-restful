# Create a default database or recreate if it exist
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from mysql import connector
import json



app = Flask(__name__)

with open('app/database/connection.json', 'r') as file:
    __conn_json = json.load(file)

# get AQLAlchemy
db = SQLAlchemy(app=app)

__str_connection = "mysql://{username}:{password}@{server}/{database}?charset=utf8mb4"

__username = __conn_json["username"]
__password = __conn_json["password"]
__server = __conn_json["server"]
__database = __conn_json["database"]

app.config['SQLALCHEMY_DATABASE_URI'] = __str_connection.format(
                                                    username=__username, 
                                                    password=__password, 
                                                    server=__server, 
                                                    database=__database
                                                )

app.config['SECRET_KEY'] = 'secrect_key'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def create_db():
    '''
    Cria o banco de dados padrão para testes
    
    server_user: str\n
    Nome de usuário do servidor mysql.\n

    server_pwd : str
    Senha do servidor mysql.\n
    '''
    mydb = connector.connect(
        host=__server,
        user=__username,
        password=__password
    )
    mycursor = mydb.cursor()

    mycursor.execute(f"DROP DATABASE IF EXISTS {__database}")
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {__database} CHARSET = utf8mb4;")
    # mycursor.execute(f"USE {db_name}")
    mydb.close()
    mycursor.close()

    # Configure to use our database.
    # str_connection = f"mysql://{er}:{server_pwd}@{server}/{db_name}?charset=utf8mb4"
    # app.config['SQLALCHEMY_DATABASE_URI'] = str_connection
    # app.config['SQLALCHEMY_ECHO'] = True
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.create_all()
    
