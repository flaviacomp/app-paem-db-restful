
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

from database import create_db, db

def dicts2db(dicts, Model):

    models = list()
    for row in dicts:
        objectModel = Model(**row)
        models.append(objectModel)
    
    db.session.add_all(models)
    db.session.commit()

def import_csv_db():

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
    dicts2db(usuario_dicts, UsuarioModel)

    # import campus
    dicts2db(campus_dicts, CampusModel)
    
    # import curso
    dicts2db(curso_dicts, CursoModel)

    # import recurso_campus
    dicts2db(recurso_campus_dicts, RecursoCampusModel)

    # import discente
    dicts2db(discente_dicts, DiscenteModel)

    # import docente
    dicts2db(docente_dicts, DocenteModel)

    # import tecnico
    dicts2db(tecnico_dicts, TecnicoModel)
    
    # import solicitacao_acesso
    dicts2db(solicitacao_acesso_dicts, SolicitacaoAcessoModel)
    
    # import acesso_permitido
    dicts2db(acesso_permitido_dicts, AcessoPermitidoModel)
    

if __name__=='__main__':
    create_db()
    import_csv_db()
