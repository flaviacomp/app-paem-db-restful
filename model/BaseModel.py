
# Model class base of tables
# from importdb.db import db

# class BaseModel(db.Model):


#     @classmethod
#     def find_by_name(cls, name):
#        return cls.query.filter_by(nome=name).first_or_404()

#     def save_to_db(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete_from_db(self):
#         db.session.delete(self)
#         db.session.commit()