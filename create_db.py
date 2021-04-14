
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
from pandas import DataFrame, read_csv, datetime

def import_csv_db(db):

    # dateparser_campus = lambda x: datetime.strptime(x, "%d-%m-%y")
    # dateparser_curso = lambda x: datetime.strptime(x, "%d-%m-%y")
    # dateparser_docente = lambda x: datetime.strptime(x, "%d-%m-%y")
    # dateparser_tecnico = lambda x: datetime.strptime(x, "%d-%m-%y")
    # timeparser = lambda x: datetime.strptime(x, "%H:%M:%S")

    campus_dicts = read_csv('importdb\\inputs\\campus.csv', parse_dates=["ano_fundacao"], na_filter=False, sep=';', encoding='utf-8').to_dict(orient='records')
    curso_dicts = read_csv('importdb\\inputs\\curso.csv', parse_dates=["data_fundacao"], na_filter=False, sep=';', encoding='ISO-8859-1').to_dict(orient='records')
    discente_dicts = read_csv('importdb\\inputs\\discente.csv', na_filter=False, sep=';', encoding='ISO-8859-1').to_dict(orient='records')
    docente_dicts = read_csv('importdb\\inputs\\docentes.csv', parse_dates=["data_nascimento"], na_filter=False, sep=';', encoding='ISO-8859-1').to_dict(orient='records')
    recurso_campus_dicts = read_csv('importdb\\inputs\\recurso_campus.csv', parse_dates=["inicio_horario_funcionamento", "fim_horario_funcionamento"], na_filter=False, sep=';', encoding='ISO-8859-1').to_dict(orient='records')
    tecnico_dicts = read_csv('importdb\\inputs\\tecnico.csv', parse_dates=["data_nascimento"], na_filter=False, sep=';', encoding='ISO-8859-1').to_dict(orient='records')
    usuario_dicts = read_csv('importdb\\inputs\\usuario.csv', na_filter=False, sep=';', encoding='ISO-8859-1').to_dict(orient='records')

    
    # import usuario
    usuarios = list()
    for row in usuario_dicts:
        usuario = UsuarioModel(**row)
        usuarios.append(usuario)
    db.session.add_all(usuarios)
    db.session.commit()

    # import campus
    campuss = list()
    for row in campus_dicts:
        campus = CampusModel(**row)
        campuss.append(campus)
    db.session.add_all(campuss)
    db.session.commit()

    # import curso
    cursos = list()
    for row in curso_dicts:
        curso = CursoModel(**row)
        cursos.append(curso)
    db.session.add_all(cursos)
    db.session.commit()

    # import recurso_campus
    recursos_campus = list()
    for row in recurso_campus_dicts:
        recurso_campus = RecursoCampusModel(**row)
        recursos_campus.append(recurso_campus)
    db.session.add_all(recursos_campus)
    db.session.commit()

    # import discente
    discentes = list()
    for row in discente_dicts:
        discente = DiscenteModel(**row)
        discentes.append(discente)
    db.session.add_all(discentes)
    db.session.commit()

    # import docente
    docentes = list()
    for row in docente_dicts:
        docente = DocenteModel(**row)
        docentes.append(docente)
    db.session.add_all(docentes)
    db.session.commit()

    # import tecnico
    tecnicos = list()
    for row in tecnico_dicts:
        tecnico = TecnicoModel(**row)
        tecnicos.append(tecnico)
    db.session.add_all(tecnicos)
    db.session.commit()

if __name__=='__main__':
    from importdb.db import create_db, db
    from flask import Flask
    app = Flask(__name__)

    hostname = input('\nHost name. Default is localhost: ')
    username = input('\nUsername: ')
    password = input('\nPassword: ')
    
    if hostname == '':
        hostname = 'localhost'

    create_db(app, username, password, hostname)
    import_csv_db(db)
