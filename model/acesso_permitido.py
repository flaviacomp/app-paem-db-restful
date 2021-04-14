from importdb.db import db
from .solicitacao_acesso import SolicitacaoAcessoModel


class AcessoPermitidoModel(db.Model):
    __tablename__ = "acesso_permitido"

    id_acesso_permitido = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float, nullable=True)
    hora_entrada = db.Column(db.Time, nullable=True)
    hora_saida = db.Column(db.Time, nullable=True)
    
    solicita_acesso_id_solicita_acesso = db.Column(db.Integer, db.ForeignKey('solicitacao_acesso.id_solicitacao_acesso'), nullable=True)
    solicita_acesso = db.relationship('SolicitacaoAcessoModel', backref=db.backref('acessos_permitido', lazy=True))

    def __repr__(self):
        return '<acesso_permitido %r>' % self.nome
