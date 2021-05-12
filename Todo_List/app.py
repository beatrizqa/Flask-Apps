
from flask import Flask  # Import Flask class
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy class

app = Flask(__name__)  # create Flask object

# Set the connection string to connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.105.152.18/myflaskdb"

db = SQLAlchemy(app)  # create SQLALchemy object


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, default=False)


@app.route('/')
def index():
    return "This is a TODO list"


@app.route('/add')
def add():
    # a new entry in the database
    new_todo1 = Todos(task='Take out the bins', complete=True)
    db.session.add(new_todo1)
    db.session.commit()
    return "Add a new ToDO item"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
