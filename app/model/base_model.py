
# Model class base of tables
from ..database import db

# class to work on object model properties
class BaseModel():
    
    @classmethod
    def find_by_id(cls, id):
       return cls.query.get(id)
    
    @classmethod
    def query_all(cls):
       return cls.query.all()
    
    @classmethod
    def update_by_id(cls, id, dict):
        model = cls.query.get(id)
        for key, value in dict.items():
            if hasattr(model, key):
                setattr(model, key, value)
        cls.save()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def save_all(values):
        db.session.add_all()
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def save(cls):
        db.session.commit()

# class to working on person atributes 
class PessoaModel(BaseModel):

    @classmethod
    def find_by_name(cls, nome):
       return cls.query.filter_by(nome=nome).first()

    @classmethod
    def update_by_name(cls, nome, dict):
       cls.query.filter_by(nome=nome).update(dict)
       cls.save()