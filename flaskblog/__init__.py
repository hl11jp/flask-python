from flask import (Flask)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '922b07ca5a25ceafa1052b56d82482ed'
db = SQLAlchemy(app)

from flaskblog import routes