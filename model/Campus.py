# Table structure for table `campus`
from importdb.db import db
class CampusModel(db.Model):
    __tablename__ = "campus"

    id_campus = db.Column(db.Integer, primary_key=True)
    ano_fundacao = db.Column(db.Date, nullable=True)
    nome = db.Column(db.String(45), nullable=False)
    
    direcao_id_direcao = db.Column(db.Integer, db.ForeignKey('direcao.id_direcao'), nullable=True)
    direcao = db.relationship('DirecaoModel', uselist=False, backref=db.backref('campus', lazy=True))

    def __repr__(self):
        return '<campus %r>' % self.nome


    
