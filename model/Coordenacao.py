from importdb.db import db
from .Curso import CursoModel
from .Docente import DocenteModel
class CoordenacaoModel(db.Model):
    __tablename__ = "coordenacao"

    id_coordenacao = db.Column(db.Integer, primary_key=True)
    data_entrada = db.Column(db.Date, nullable=True)
    hora_saida = db.Column(db.Time, nullable=True)

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=False)
    curso = db.relationship('CursoModel', uselist=False, backref=db.backref('coodenacao', lazy=True))

    docente_id_docente = db.Column(db.Integer, db.ForeignKey('docente.id_docente'), nullable=False)
    docente = db.relationship('DocenteModel', uselist=False, backref=db.backref('docente', lazy=True))

    def __repr__(self):
        return '<coordenacao %r>' % self.nome
