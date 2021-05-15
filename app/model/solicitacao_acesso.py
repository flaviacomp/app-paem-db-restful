# Table structure for table `solicita_acesso`
from ..database import db
from .usuario import UsuarioModel
from .discente import DiscenteModel
from .recurso_campus import RecursoCampusModel

from datetime import time, date

class SolicitacaoAcessoModel(db.Model):
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

    id_recurso_campus = db.Column(db.Integer, db.ForeignKey('recurso_campus.id_recurso_campus'), nullable=True)
    recurso_campus = db.relationship('RecursoCampusModel', uselist=False, lazy='select', backref=db.backref('solicitacoes_acesso', lazy='dynamic'))


    def serialize(self):
        return {
            'id':self.id_solicitacao_acesso,
            'para_si':self.para_si,
            'data':str(self.data),
            'hora_inicio':str(self.hora_inicio),
            'hora_fim':str(self.hora_fim),
            'status_acesso':self.status_acesso,
            'nome':self.nome,
            'fone':self.fone,
            'id_recurso_campus':self.id_recurso_campus,
            'matricula':self.discente.serialize()['matricula'],
            'nome_discente':self.discente.serialize()['nome'],
            'discente_id_discente':self.discente_id_discente,
            'recurso_campus':self.recurso_campus.serialize()
        }

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        day, month, year = data.split('-')
        self.__data = date(day=int(day), month=int(month), year=int(year))

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, hora_inicio):
        hour_inic, minute_inic, second_inic = hora_inicio.split(':')
        self.__hora_inicio = time(hour=int(hour_inic), minute=int(minute_inic), second=int(second_inic))

    @property
    def hora_fim(self):
        return self.__hora_fim

    @hora_fim.setter
    def hora_inicio(self, hora_fim):
        hour_inic, minute_inic, second_inic = hora_fim.split(':')
        self.__hora_fim = time(hour=int(hour_inic), minute=int(minute_inic), second=int(second_inic))

    @classmethod
    def find_by_nome(cls, nome):
       return cls.query.filter_by(nome=nome).first()

    @classmethod
    def find_by_id(cls, id):
       return cls.query.filter_by(id_solicitacao_acesso=id).first()

    @classmethod
    def find_by_id_usuario(cls, id_usuario):
       return cls.query.filter_by(usuario_id_usuario=id_usuario).first_or_404()

    @classmethod
    def  query_all(cls):
       return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<solicita_acesso %r>' % self.id_solicitacao_acesso
