from flask import Flask,render_template,request,redirect,url_for
import config
from exts import db
from models import Todo

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    todos=Todo.query.order_by('-create_time').all()
    return render_template('index.html',todos=todos)


@app.route('/add/',methods=['POST'])
def add():
    content=request.form.get('content')
    todo=Todo(content=content)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/done/<todo_id>')
def done(todo_id):
    todo=Todo.query.filter(Todo.id==todo_id).first()
    todo.status=1
    db.session.commit()
    context={
        'todos':Todo.query.order_by('-create_time').all()
    }
    return render_template('index.html',**context)
    # todos = Todo.query.order_by('-create_time').all()
    # return render_template('base.html', todos=todos)

@app.route('/undone/<todo_id>')
def undone(todo_id):
    todo=Todo.query.filter(Todo.id==todo_id).first()
    todo.status=0
    db.session.commit()
    context={
        'todos':Todo.query.order_by('-create_time').all()
    }
    return render_template('index.html',**context)

@app.route('/delete/<todo_id>')
def delete(todo_id):
    todo=Todo.query.filter(Todo.id==todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    context={
        'todos':Todo.query.order_by('-create_time').all()
    }
    return render_template('index.html',**context)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run()