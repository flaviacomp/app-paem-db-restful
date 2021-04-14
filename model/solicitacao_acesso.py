# Table structure for table `solicita_acesso`

from importdb.db import db
from .usuario import UsuarioModel
from .discente import DiscenteModel
from .recurso_campus import RecursoCampusModel


class SolicitacaoAcessoModel(db.Model):
    __tablename__= "solicitacao_acesso"

    id_solicitacao_acesso = db.Column(db.Integer, primary_key=True)
    para_si = db.Column(db.SmallInteger, nullable=False)
    data = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fim = db.Column(db.Time, nullable=False)
    status_acesso = db.Column(db.SmallInteger, nullable=True)
    nome = db.Column(db.String(45), nullable=False)
    fone = db.Column(db.String(45), nullable=True)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', uselist=False, backref=db.backref('solicitacao_acesso', lazy=True))

    discente_id_discente = db.Column(db.Integer, db.ForeignKey('discente.id_discente'), nullable=True)
    discente = db.relationship('DiscenteModel', uselist=False, backref=db.backref('solicitacao_acesso', lazy=True))

    recurso_campus_id_recurso_campus = db.Column(db.Integer, db.ForeignKey('recurso_campus.id_recurso_campus'), nullable=True)
    recurso_campus = db.relationship('RecursoCampusModel', uselist=False, backref=db.backref('solicitacao_acesso', lazy=True))

    def __repr__(self):
        return '<solicita_acesso %r>' % self.nome


    
