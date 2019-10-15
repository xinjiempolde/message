from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)
from .views import *
from .controller import *
from . import init_database, erros
