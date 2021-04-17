# Table structure for table `solicita_acesso`
from database.db import db
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
    usuario = db.relationship('UsuarioModel', uselist=False, lazy='select', backref=db.backref('solicitacoes_acesso', lazy='select'))

    discente_id_discente = db.Column(db.Integer, db.ForeignKey('discente.id_discente'), nullable=True)
    discente = db.relationship('DiscenteModel', uselist=False, lazy='select', backref=db.backref('solicitacoes_acesso', lazy='dynamic'))

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
            'discente_id_discente':self.discente_id_discente
            # 'recurso_campus':self.recurso_campus.serialize(),
            # 'discente':self.discente.serialize()
        }

    @classmethod
    def find_by_nome(cls, nome):
       return cls.query.filter_by(nome=nome).first()

    @classmethod
    def find_by_id(cls, id):
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
        return '<solicita_acesso %r>' % self.id_solicitacao_acesso
