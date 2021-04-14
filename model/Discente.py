from importdb.db import db
from .usuario import UsuarioModel

class DiscenteModel(db.Model):
    __tablename__='discente'

    id_discente = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(45), nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    cpf = db.Column(db.String(15), nullable=True)
    entrada = db.Column(db.String(6), nullable=True)
    semestre = db.Column(db.Integer, nullable=True)
    endereco = db.Column(db.String(45), nullable=True)
    grupo_risco = db.Column(db.SmallInteger, nullable=True)
    status_covid = db.Column(db.SmallInteger, nullable=True)
    status_permissao = db.Column(db.SmallInteger, nullable=True)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', uselist=False, backref=db.backref('discente', lazy=True))

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)
    
    def __init__(self, matricula, nome, curso_id_curso, cpf=None, 
                        entrada=None, semestre=None, endereco=None, 
                        grupo_risco=None, status_covid=None, 
                        status_permissao=None, usuario_id_usuario=None):

        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.entrada = entrada
        self.semestre = semestre
        self.endereco = endereco
        self.grupo_risco = grupo_risco
        self.status_covid = status_covid
        self.status_permissao = status_permissao
        self.usuario_id_usuario = usuario_id_usuario
        self.curso_id_curso = curso_id_curso


    def json(self):
        return {'id_discente': self.id_discente, 
                                'nome': self.nome,
                                'matricula': self.matricula,
                                'cpf':self.cpf,
                                'entrada':self.entrada,
                                'semestre':self.semestre,
                                'endereco':self.endereco,
                                # 'grupo_risco':self.grupo_risco,
                                # 'status_covid':self.status_covid,
                                # 'status_permissao':self.status_permissao,
                                'usuario_id_usuario':self.usuario_id_usuario,
                                'curso_id_curso':self.curso_id_curso}
    
    @classmethod
    def find_by_name(cls, name):
       return cls.query.filter_by(nome=name).first_or_404()

    @classmethod
    def find_by_id(cls, id):
       return cls.query.filter_by(id_discente=id).first_or_404()

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
        return '<discente %r>' % self.login