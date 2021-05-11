from flask import Flask  # Import Flask class
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy class

app = Flask(__name__)  # create Flask object

# Set the connection string to connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.105.152.18/myflaskdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # create SQLALchemy object


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, nullable=True)


@app.route('/')
def index():
    return "This is a TODO list"


@app.route('/todos')
def showtodos():
    all_todos = Todos.query.all()
    todo_sum = ""
    for todo in all_todos:
        todo_sum = todo_sum + "<br>" + todo.task + " " + str(todo.complete)
    return todo_sum


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
