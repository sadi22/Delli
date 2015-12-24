__author__ = 'SADI'

from flask import Flask
<<<<<<< HEAD
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
=======

app = Flask(__name__)
from app import views
>>>>>>> 484932b8c1b21138ed379c45cc31715ba76ebc13
