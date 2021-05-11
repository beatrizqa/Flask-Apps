# Import everything we need
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Declare Flask object

# Set the connection string to connect to a database
app.config['SQLALCHEMY_DATABASE_URI'] = '"mysql+pymysql://root:root@34.105.152.18/myflaskdb"'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # Declare SQLAlchemy object
