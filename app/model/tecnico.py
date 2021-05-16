from ..database import db
from .usuario import UsuarioModel
from .campus import CampusModel
from .base_model import BaseModel
from datetime import date


class TecnicoModel(BaseModel, db.Model):
    __tablename__ = "tecnico"

    id_tecnico = db.Column(db.Integer, primary_key=True)
    siape = db.Column(db.String(45), unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    __data_nascimento = db.Column('data_nascimento', db.Date, nullable=True)
    cargo = db.Column(db.String(45), nullable=True)
    status_covid = db.Column(db.SmallInteger, nullable=True)
    status_afastamento = db.Column(db.SmallInteger, nullable=True)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', lazy='select', uselist=False, backref=db.backref('tecnico', lazy='select'))

    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=True)
    campus = db.relationship('CampusModel', lazy='select', backref=db.backref('tecnicos', lazy='select'))

    def __init__(self, siape, 
                        nome, 
                        data_nascimento, 
                        cargo,
                        status_covid=None, 
                        status_afastamento=None, 
                        usuario_id_usuario=None, 
                        campus_id_campus=None
                        ):
                        
        self.siape = siape
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cargo = cargo
        self.status_covid = status_covid
        self.status_afastamento = status_afastamento
        self.curso_id_curso = campus_id_campus
        self.usuario_id_usuario = usuario_id_usuario

    @property
    def data_nascimento(self):
        return str(self.__data_nascimento)

    @data_nascimento.setter
    def data_nascimento(self, data):
          if isinstance(data, str):
              day, month, year = data.split('-')
              data = date(day=int(day), month=int(month), year=int(year))

          self.__data_nascimento = data

    def serialize(self):
        return {
            'id_tecnico':self.id_tecnico,
            'siape':self.siape, 
            'nome':self.nome, 
            'data_nascimento':self.data_nascimento, 
            "cargo":self.cargo,
            'status_covid':self.status_covid, 
            'status_afastamento':self.status_afastamento, 
            'usuario_id_usuario':self.usuario_id_usuario, 
            'campus_id_campus':self.campus_id_campus
        }
    
    def __repr__(self):
        return '<tecnico %r>' % self.nome
