# we import the SQLAlchemy object db and the Users class defined in app.py.
from app import db, Users

# The two functions db.drop_all() and db.create_all() delete all tables then create all tables defined for our db object.
db.drop_all()
db.create_all()

# Extra: this section populates the table with an example entry
testuser = Users(first_name='Grooty', last_name='Toot')
db.session.add(testuser)
db.session.commit()
