from flask import Flask, render_template

app = Flask(__name__)

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