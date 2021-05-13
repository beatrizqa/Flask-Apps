
from flask import Flask  # Import Flask class
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy class

# create Flask object. We make our 'app object' but it needs to know what model we are running
app = Flask(__name__)

# Set the connection string to connect to the database, name of DB in GCP
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.105.152.18:3306/myflaskdb"  # ==>>> this one is for stand alone DB

app.config['SQLALchemy_DATABASE_URI'] = "sqlite:///data.db"

# this is our db object which is going to be an object of the SQLALchemy class and all we need to pass is the app variable
db = SQLAlchemy(app)

'''below we make our table
    1. we have a class called Todos, that is going to be the name of our table 
    2. it will inherit db.model
'''


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable=False)
    complete = db.Column(db.Boolean, default=False)

# we need to create our routes


@app.route('/')  # we want the index
def index():  # this route is for the INDEX page so we call the function 'INDEX'
    return "This is a TODO list"


''' 2.1 Create routes that ADDS a new Todo with the value 'New Todo' every time'''


@app.route('/add')
def add():  # adds a new entry in the database
    # we create a new todo (new_todo1) from the 'Todos' table (line 22). All it needs is a TASK because line 24 (complete)
    new_todo = Todos(task='New Todo')
    # is default to False and the ID is automatically generated
    db.session.add(new_todo)  # need to add the new_todo1 to the DB
    db.session.commit()  # need to save (commit) the new_todo in the DB
    # you can return a message or the name of the new todo item ======>>>  return new_todo.name
    return "Add a new ToDO item"
    #


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
