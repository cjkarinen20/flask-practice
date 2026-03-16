from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello-world.db'
app.config['SECRET_KEY'] = '96c2dda30278499a85e2eb8a0bbbbed9c84e79ad52114b44'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#---Database---
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(200), nullable = True)
    is_complete = db.Column(db.Boolean, default = False)

@app.route('/')

def hello_world():
    return 'Hello World!'

#---Dynamic-Routing---
@app.route('/user/<name>')
def user(name):
    personal = f'<h1>Hello, {name}!</h1>'
    template = '<p>Change the name in the <em> browser address bar</em> and reload the page.</p>'
    return personal + template

#---HTML-Templates---
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name =name)

@app.route('/users')
def users():
    user_names = ['Alice', 'Bob', 'Charlie']
    return render_template('users.html', names = user_names)