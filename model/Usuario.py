from importdb.db import db
from bcrypt import hashpw, checkpw, gensalt


class UsuarioModel(db.Model):
    __tablename__='usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(45), nullable=False)
    _senha = db.Column('senha', db.Text, nullable=False)
    email = db.Column(db.String(45), nullable=False)
    tipo = db.Column(db.Integer, nullable=False)

    
    def __init__(self, login, senha, email, tipo):
        self.login = login
        self.email = email
        self.tipo = tipo
        self.senha = senha

    @property
    def senha(self, password):
        return self._senha

    @senha.setter
    def senha(self, password):
        self._senha = hashpw(password.encode('utf-8'), gensalt())
    
    def verify_passord(self, password):
        return checkpw(password, self._senha)

    def serialize(self):
        return {'id_usuario': self.id_usuario, 
                'login': self.login,
                'email':self.email,
                'tipo':self.tipo,
        }

    @classmethod
    def find_by_login(cls, login):
       return cls.query.filter_by(login=login).first()

    @classmethod
    def find_by_id(cls, id):
       return cls.query.filter_by(id_usuario=id).first()

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
        return '<usuario %r>' % self.login