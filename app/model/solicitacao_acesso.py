# Table structure for table `solicita_acesso`
from ..database import db
from .base_model import BaseModel
from .usuario import UsuarioModel
from .discente import DiscenteModel
from .recurso_campus import RecursoCampusModel

from datetime import time, date

class SolicitacaoAcessoModel(BaseModel, db.Model):
      __tablename__= "solicitacao_acesso"
          

      id_solicitacao_acesso = db.Column(db.Integer, primary_key=True)
      para_si = db.Column(db.SmallInteger, nullable=False)
      __data = db.Column('data', db.Date, nullable=False)
      __hora_inicio = db.Column('hora_inicio', db.Time, nullable=False)
      __hora_fim = db.Column('hora_fim', db.Time, nullable=False)
      status_acesso = db.Column(db.SmallInteger, nullable=True)
      nome = db.Column(db.String(45), nullable=False)
      fone = db.Column(db.String(45), nullable=True)

      usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
      usuario = db.relationship('UsuarioModel', uselist=False, lazy='select', backref=db.backref('solicitacoes_acesso', lazy='select'))

      discente_id_discente = db.Column(db.Integer, db.ForeignKey('discente.id_discente'), nullable=True)
      discente = db.relationship('DiscenteModel', uselist=False, lazy='select', backref=db.backref('solicitacoes_acesso', lazy='dynamic'))

      # TODO: add visitante.

      recurso_campus_id_recurso_campus = db.Column(db.Integer, db.ForeignKey('recurso_campus.id_recurso_campus'), nullable=True)
      recurso_campus = db.relationship('RecursoCampusModel', uselist=False, lazy='select', backref=db.backref('solicitacoes_acesso', lazy='dynamic'))
      
      def __init__(self, 
                   para_si,
                   data,
                   hora_inicio,
                   hora_fim,
                   status_acesso,
                   nome,
                   fone,
                   usuario_id_usuario,
                   discente_id_discente,
                   recurso_campus_id_recurso_campus,
                   id_solicitacao_acesso=None
                                                ):

          self.id_solicitacao_acesso = id_solicitacao_acesso
          self.para_si = para_si
          self.data = data
          self.hora_inicio = hora_inicio
          self.hora_fim = hora_fim
          self.status_acesso = status_acesso
          self.nome = nome
          self.fone = fone
          self.usuario_id_usuario = usuario_id_usuario
          self.discente_id_discente = discente_id_discente
          self.recurso_campus_id_recurso_campus = recurso_campus_id_recurso_campus

      @property
      def data(self):
        return str(self.__data)

      @data.setter
      def data(self, data):
          if isinstance(data, str):
              day, month, year = data.split('-')
              data = date(day=int(day), month=int(month), year=int(year))

          self.__data = data

      @property
      def hora_inicio(self):
          return str(self.__hora_inicio)

      @hora_inicio.setter
      def hora_inicio(self, hora_inicio):
          if isinstance(hora_inicio, str):
              hour_inic, minute_inic, second_inic = hora_inicio.split(':')
              hora_inicio = time(hour=int(hour_inic), minute=int(minute_inic), second=int(second_inic))
        
          self.__hora_inicio = hora_inicio

      @property
      def hora_fim(self):
          return str(self.__hora_fim)
 
      @hora_fim.setter
      def hora_fim(self, hora_fim):
          if isinstance(hora_fim, str):
              hour_inic, minute_inic, second_inic = hora_fim.split(':')
              hora_fim = time(hour=int(hour_inic), minute=int(minute_inic), second=int(second_inic))
            
          self.__hora_fim = hora_fim

      def serialize(self):
          return {
              'id':self.id_solicitacao_acesso,
              'para_si':self.para_si,
              'data':self.data,
              'hora_inicio':self.hora_inicio,
              'hora_fim':self.hora_fim,
              'status_acesso':self.status_acesso,
              'nome':self.nome,
              'fone':self.fone,
              'matricula':self.discente.serialize()['matricula'],
              'nome_discente':self.discente.serialize()['nome'],
              'discente_id_discente':self.discente_id_discente,
              'recurso_campus_id_recurso_campus':self.recurso_campus_id_recurso_campus,
              'recurso_campus':self.recurso_campus.serialize()
          }

      @classmethod
      def find_by_id_discente(cls, id_discente):
        solicitacao_acesso = cls.query.filter_by(discente_id_discente=id_discente).first_or_404("Not found this resource.")
        return solicitacao_acesso.serialize()

      def __repr__(self):
          return '<solicita_acesso %r>' % self.id_solicitacao_acesso
