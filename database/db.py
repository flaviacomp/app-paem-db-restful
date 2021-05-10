# Create a default database or recreate if it exist
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from mysql import connector

# get AQLAlchemy
db = SQLAlchemy()

def connnect_db(username, password, hostname, db_name, app):
    str_connection = f"mysql://{username}:{password}@{hostname}/{db_name}"
    app.config['SQLALCHEMY_DATABASE_URI'] = str_connection
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return db

def create_db(app, server_user, server_pwd, server='localhost', db_name="mydbpaem"):
    '''
    Cria o banco de dados padrão para testes
    
    server_user: str\n
    Nome de usuário do servidor mysql.\n

    server_pwd : str
    Senha do servidor mysql.\n
    '''
    mydb = connector.connect(
        host=server,
        user=server_user,
        password=server_pwd
    )
    mycursor = mydb.cursor()

    mycursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARSET = utf8mb4;")
    # mycursor.execute(f"USE {db_name}")
    mydb.close()
    mycursor.close()

    # Configure to use our database.
    str_connection = f"mysql://{server_user}:{server_pwd}@{server}/{db_name}?charset=utf8mb4"
    app.config['SQLALCHEMY_DATABASE_URI'] = str_connection
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    
