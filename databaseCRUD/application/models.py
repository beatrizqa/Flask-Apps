from application import db  # we need this to create our models

''' This fime just stores our models, our tables'''


class Games(db.Model):  # this creates the 'Games' table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
