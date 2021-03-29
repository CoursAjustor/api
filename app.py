import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database.connect import DATABASE_PATH

app = Flask(__name__, static_folder="public", template_folder="views")
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_PATH
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

log = app.logger

from routes.routes import *