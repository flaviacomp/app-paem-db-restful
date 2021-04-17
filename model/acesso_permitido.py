from database.db import db
from .solicitacao_acesso import SolicitacaoAcessoModel


class AcessoPermitidoModel(db.Model):
    __tablename__ = "acesso_permitido"

    id_acesso_permitido = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float, nullable=True)
    hora_entrada = db.Column(db.Time, nullable=True)
    hora_saida = db.Column(db.Time, nullable=True)
    
    id_solicitacao_acesso = db.Column(db.Integer, db.ForeignKey('solicitacao_acesso.id_solicitacao_acesso'), nullable=True)
    solicita_acesso = db.relationship('SolicitacaoAcessoModel', uselist=False, backref=db.backref('acesso_permitido', lazy='select', uselist=False))

    def serialize(self):
      return {
         'id_acesso_permitido':self.id_acesso_permitido,
         'temperatura':self.temperatura,
         'hora_entrada':str(self.hora_entrada),
         'hora_saida':str(self.hora_saida),
         'id_solicitacao_acesso':self.id_solicitacao_acesso
      }

    @classmethod
    def find_by_id(cls, id):
       return cls.query.filter_by(id_acesso_permitido=id).first()
   
    @classmethod
    def find_by_id_solicitacao_acesso(cls, id):
       return cls.query.filter_by(id_solicitacao_acesso=id).first()

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
        return '<acesso_permitido %r>' % self.nome
