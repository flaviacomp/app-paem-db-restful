from database.db import db
from .campus import CampusModel
from .disciplina import DisciplinaModel
from .discente import DiscenteModel
from .docente import DocenteModel


class CursoModel(db.Model):
    __tablename__='curso'

    id_curso = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    data_fundacao = db.Column(db.Date, nullable=True)
    
    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=False)
    campus = db.relationship('CampusModel', backref=db.backref('cursos', lazy=True))
    
    docentes = db.relationship('DocenteModel', backref=db.backref('curso', lazy=True))
    
    disciplinas = db.relationship('DisciplinaModel', backref=db.backref('curso', lazy=True))

    discentes = db.relationship('DiscenteModel', backref=db.backref('curso', lazy=True))

    def __init__(self, nome, data_fundacao, campus_id_campus, id_curso=None):
        self.nome = nome
        self.data_fundacao = data_fundacao
        self.campus_id_campus = campus_id_campus
        self.id_curso = id_curso

    def __repr__(self):
        return '<curso %r>' % self.nome