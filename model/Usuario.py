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

    def json(self):
        return {'id_usuario': self.id_usuario, 
                'login': self.login,
                'senha': self.senha,
                'email':self.email,
                'tipo':self.tipo,
                 }

    @classmethod
    def find_by_login(cls, login):
       return cls.query.filter_by(login=login).first_or_404()

    @classmethod
    def find_by_id(cls, id):
       return cls.query.filter_by(id_usuario=id).first_or_404()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<usuario %r>' % self.login