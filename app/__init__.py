import logging, os
from flask import Flask
from flask_appbuilder.security.mongoengine.manager import SecurityManager
from flask_appbuilder import AppBuilder
from flask_mongoengine import MongoEngine

"""
 Logging configuration
"""
class App:
    class __App:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not App.instance:
            App.instance = App.__App(arg)
            logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
            logging.getLogger().setLevel(logging.DEBUG)

            app = Flask(__name__)
            app.config.from_object('config')
            app.config['MONGODB_SETTINGS'] = {'HOST':'mongodb://careful:123456abc@ds127771.mlab.com:27771/careful','DB': 'careful'}
            db = MongoEngine(app)
            appbuilder = AppBuilder(app, security_manager_class=SecurityManager)
        else:
            App.instance.val = arg
        return app

"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""    
app = App('init')
from app import views
