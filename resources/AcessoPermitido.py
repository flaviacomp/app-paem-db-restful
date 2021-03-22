from db import db
class AcessoPermitidoModel(db.Model):
    __tabename__ = "acesso_permitido"

    id_acesso_permitido = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float, nullable=True)
    hora_entrada = db.Column(db.Time, nullable=True)
    hora_saida = db.Column(db.Time, nullable=True)
    
    solicita_acesso_id_solicita_acesso = db.Column(db.Integer, db.ForeignKey('solicita_acesso.id_solicita_acesso'), nullable=True)
    solicita_acesso = db.relationship('SolicitaAcessoModel', backref=db.backref('solicita_acessos', lazy=True))

    def __repr__(self):
        return '<acesso_permitido %r>' % self.nome
