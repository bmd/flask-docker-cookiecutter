import os
from flask import Flask
from flask_restful import Api
from models import *
from resources import *


def make_app():

    # initialize the app
    app = Flask(__name__)
    # load configs
    print 'Loading env config'
    if os.environ['APP_ENV'] == 'Prod':
        print 'Configuring as Production'
        app.config.from_object('config.Prod')
    else:
        print 'Configuring as Dev'
        app.config.from_object('config.Dev')

    # initialize flask
    print 'Initializing Flask-restful'
    api = Api(app)

    print 'Initializing database connection'
    db.init_app(app)

    return db, api, app


db, api, app = make_app()
