from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import yaml
import os

app = Flask(__name__)
boostrap = Bootstrap(app)

settings = yaml.load(open(os.path.join(os.environ['HOME'], 'dd_configure.yaml')))
app.config['SQLALCHEMY_DATABASE_URI'] = settings['CONNECTION_STRING']
db = SQLAlchemy(app)

from app import views
