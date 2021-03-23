# Table structure for table `solicita_acesso`

from importdb.db import db
from .Usuario import UsuarioModel
class ReservaRecursoCampusModel(db.Model):
    __tablename__= "reserva_recurso_servidores"

    id_reserva_recurso_servidores = db.Column(db.Integer, primary_key=True)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_final = db.Column(db.Time, nullable=False)
    descricao = db.Column(db.SmallInteger, nullable=True)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuarios = db.relationship('UsuarioModel',, uselist=False, backref=db.backref('reserva_recurso_servidores', lazy=True))

    def __repr__(self):
        return '<reserva_recurso_campus %r>' % self.nome


    
