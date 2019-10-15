from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/test.db'
db = SQLAlchemy(app)
from .views import *
from .controller import *
from . import init_database
