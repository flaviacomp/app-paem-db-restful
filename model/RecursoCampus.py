from importdb.db import db
class RecursoCampusModel(db.Model):
    __tablename__ = "recurso_campus"

    id_recurso_campus = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    inicio_horario_funcionamento = db.Column(db.Time, nullable=True)
    fim_horario_funcionamento = db.Column(db.Time, nullable=True)
    
    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=False)
    campus = db.relationship('CampusModel', backref=db.backref('recursos_campus', lazy=True))

    def __repr__(self):
        return '<recurso_campus %r>' % self.nome