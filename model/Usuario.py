from importdb.db import db

class UsuarioModel(db.Model):
    __tablename__='usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(45), nullable=False)
    senha = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(45), nullable=False)
    tipo = db.Column(db.Integer, nullable=False)

    
    def __init__(self, login, senha, email, tipo):
        self.login = login
        self.senha = senha
        self.email = email
        self.tipo = tipo

    def __repr__(self):
        return '<usuario %r>' % self.login