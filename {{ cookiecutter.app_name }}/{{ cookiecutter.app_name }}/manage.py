from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from {{ cookiecutter.app_name }} import app
from {{ cookiecutter.app_name }}.models import *


manager = Manager(app)

@manager.command
def create_db():

    with app.app_context():
        db.init_app(app)

        print "Dropping database tables"
        db.drop_all()

        print "Recreating database tables"
        db.create_all()


@manager.command
def seed_db():

    with app.app_context():
        db.init_app(app)
        print 'No data to seed'


@manager.command
def start():
    app.run('0.0.0.0', debug=True)


if __name__ == "__main__":
    manager.run()
