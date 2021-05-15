from ..database import db
from .campus import CampusModel


class RecursoCampusModel(db.Model):
    __tablename__ = "recurso_campus"

    id_recurso_campus = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    inicio_horario_funcionamento = db.Column(db.Time, nullable=True)
    fim_horario_funcionamento = db.Column(db.Time, nullable=True)
    quantidade_horas = db.Column(db.Integer, nullable=True) # nova coluna
    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=False)
    campus = db.relationship('CampusModel', backref=db.backref('recursos_campus', lazy=True))

    def serialize(self):
        return {'id_recuso_campus': self.id_recurso_campus, 
                                'nome': self.nome,
                                'capacidade': self.capacidade,
                                'descricao':self.descricao,
                                'inicio_horario_funcionamento':str(self.inicio_horario_funcionamento),
                                'fim_horario_funcionamento':str(self.fim_horario_funcionamento),
                                'campus_id_campus':self.campus_id_campus}
                               
                                
    @classmethod
    def find_by_name(cls, name):
       return cls.query.filter_by(nome=name).first_or_404()

    @classmethod
    def find_by_id(cls, id):
       return cls.query.filter_by(id_recurso_campus=id).first_or_404()

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
        return '<recurso_campus %r>' % self.nome