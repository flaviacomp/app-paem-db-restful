from importdb.db import db
class TecnicoModel(db.Model):
    __tablename__ = "tecnico"

    id_tecnico = db.Column(db.Integer, primary_key=True)
    siape = db.Column(db.String(45), unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=True)
    cargo = db.Column(db.String(45), nullable=True)
    status_covid = db.Column(db.SmallInteger, nullable=True)
    status_afastamento = db.Column(db.SmallInteger, nullable=True)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', uselist=False, backref=db.backref('tecnico', lazy=True))

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)
    curso = db.relationship('CursoModel', backref=db.backref('tecnicos', lazy=True))

    def __repr__(self):
        return '<tecnico %r>' % self.nome
