from importdb.db import db
class CursoModel(db.Model):
    __tablename__='curso'

    id_curso = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    data_fundacao = db.Column(db.Date, nullable=True)
    
    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=False)
    campus = db.relationship('CampusModel', backref=db.backref('cursos', lazy=True))
    
    docentes = db.relationship('DocenteModel', backref=db.backref('curso', lazy=True))
    
    def __repr__(self):
        return '<curso %r>' % self.nome