import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database.connect import DATABASE_PATH
from app import db
from models.UserModel import User

db.create_all()

alexandre = User(firstname="Alexandre", lastname="Darthoit")

db.session.add(alexandre)
db.session.commit()