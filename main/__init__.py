# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)
moment = Moment(app)
bootstrap = Bootstrap(app)

from .views import *
from .controller import *
from . import init_database, erros
