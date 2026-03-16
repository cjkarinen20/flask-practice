from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello-world.db'
app.config['SECRET_KEY'] = '96c2dda30278499a85e2eb8a0bbbbed9c84e79ad52114b44'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from myapp import routes, models