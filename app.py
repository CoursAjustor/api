import os
from flask import Flask

app = Flask(__name__, static_folder="public", template_folder="views")

log = app.logger

from routes.routes import *