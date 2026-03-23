import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello-world.db'
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from myapp import routes, models