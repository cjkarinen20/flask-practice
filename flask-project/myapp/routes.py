from flask import render_template, redirect, url_for, request
from myapp import app, db
from myapp.models import Task 
from myapp.forms import TaskForm


@app.route('/hello/task', methods=['GET', 'POST'])
def task():
    form = TaskForm()
    if form.validate_on_submit(): # Submit Button Logic
        new_task = Task(
            title = form.title.data,
            description = form.description.data,
            is_complete = form.is_complete.data
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('hello_world'))
    return render_template('task.html', form = form)

@app.route('/task/list')
def display_tasks():
    tasks = Task.query.all()
    return render_template('task_list.html', tasks=tasks)

@app.route('/task/update_status/<int:task_id>', methods = ["POST"])
def update_task_status(task_id):
    task = Task.query.get_or_404(task_id)
    task.is_complete = 'is_complete' in request.form
    db.session.commit()
    return redirect(url_for('display_tasks'))

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