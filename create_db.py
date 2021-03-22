from model.Usuario import UsuarioModel
from model.Curso import CursoModel
from model.Campus import CampusModel
from model.Docente import DocenteModel
from model.Direcao import DirecaoModel
from model.Coordenacao import CoordenacaoModel
from model.RecursoCampus import RecursoCampusModel
from model.SolicitacaoAcesso import SolicitacaoAcessoModel
from model.AcessoPermitido import AcessoPermitidoModel
from model.Discente import DiscenteModel
from model.Disciplina import DisciplinaModel
from model.Portaria import PortariaModel
from model.Tecnico import TecnicoModel



if __name__=='__main__':
    
    from importdb.db import create_db
    from flask import Flask
    app = Flask(__name__)
    create_db(app, 'root', '70x7=sempre')

