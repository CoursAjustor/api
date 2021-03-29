from app import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  firstname = db.Column(db.String, unique=True, nullable=False)
  lastname = db.Column(db.String, unique=True, nullable=False)