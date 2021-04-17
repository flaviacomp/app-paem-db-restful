
# import models to create tables
from model.usuario import UsuarioModel
from model.curso import CursoModel
from model.campus import CampusModel
from model.docente import DocenteModel
from model.direcao import DirecaoModel
from model.coordenacao import CoordenacaoModel
from model.recurso_campus import RecursoCampusModel
from model.solicitacao_acesso import SolicitacaoAcessoModel
from model.acesso_permitido import AcessoPermitidoModel
from model.discente import DiscenteModel
from model.disciplina import DisciplinaModel
from model.portaria import PortariaModel
from model.tecnico import TecnicoModel

# libs
from datetime import time, date
from pandas import DataFrame, read_csv

def dicts2db(dicts, Model, db):

    models = list()
    for row in dicts:
        objectModel = Model(**row)
        models.append(objectModel)
    
    db.session.add_all(models)
    db.session.commit()

def import_csv_db(db):

    campus_dicts = read_csv('database\\inputs\\campus.csv', parse_dates=["ano_fundacao"], na_filter=False, sep=';', encoding='utf-8').to_dict(orient='records')
    curso_dicts = read_csv('database\\inputs\\curso.csv', parse_dates=["data_fundacao"], na_filter=False, sep=';', encoding='ISO-8859-1').to_dict(orient='records')
    discente_dicts = read_csv('database\\inputs\\discentes.csv', na_filter=False, sep=';', encoding='ISO-8859-1').to_dict(orient='records')
    docente_dicts = read_csv('database\\inputs\\docentes.csv', parse_dates=["data_nascimento"], na_filter=False, sep=';', encoding='ISO-8859-1').to_dict(orient='records')
    recurso_campus_dicts = read_csv('database\\inputs\\recurso_campus.csv', parse_dates=["inicio_horario_funcionamento", "fim_horario_funcionamento"], na_filter=False, sep=';', encoding='utf-8').to_dict(orient='records')
    tecnico_dicts = read_csv('database\\inputs\\tecnico.csv', parse_dates=["data_nascimento"], na_filter=False, sep=';', encoding='ISO-8859-1').to_dict(orient='records')
    usuario_dicts = read_csv('database\\inputs\\usuario.csv', na_filter=False, sep=';', encoding='utf-8').to_dict(orient='records')
    solicitacao_acesso_dicts = read_csv('database\\inputs\\solicitacao_acesso.csv', parse_dates=["data", "hora_inicio", "hora_fim"], na_filter=False, sep=';', encoding='utf-8').to_dict(orient='records')
    acesso_permitido_dicts = read_csv('database\\inputs\\acesso_permitido.csv', parse_dates=["hora_entrada", "hora_saida"], na_filter=False, sep=';', encoding='utf-8').to_dict(orient='records')
    
    # import usuario
    dicts2db(usuario_dicts, UsuarioModel, db)

    # import campus
    dicts2db(campus_dicts, CampusModel, db)
    
    # import curso
    dicts2db(curso_dicts, CursoModel, db)

    # import recurso_campus
    dicts2db(recurso_campus_dicts, RecursoCampusModel, db)

    # import discente
    dicts2db(discente_dicts, DiscenteModel, db)

    # import docente
    dicts2db(docente_dicts, DocenteModel, db)

    # import tecnico
    dicts2db(tecnico_dicts, TecnicoModel, db)
    
    # import solicitacao_acesso
    dicts2db(solicitacao_acesso_dicts, SolicitacaoAcessoModel, db)
    
    # import acesso_permitido
    dicts2db(acesso_permitido_dicts, AcessoPermitidoModel, db)
    

if __name__=='__main__':
    from getpass import getpass
    from database.db import create_db, db
    from flask import Flask

    app = Flask(__name__)

    hostname = input('\nHost name. Default is localhost: ')
    username = input('\nUsername. Default user is root: ')
    password = getpass('\nPassword: ')
    
    if hostname == '':
        hostname = 'localhost'
    if username == '':
        username = 'root'

    create_db(app, username, password, hostname)
    import_csv_db(db)
