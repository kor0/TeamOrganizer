import logging
from flask import Flask
from flask_appbuilder.security.mongoengine.manager import SecurityManager
from flask_appbuilder import AppBuilder
from flask_mongoengine import MongoEngine
"""
 Logging configuration
"""
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
app.config['MONGODB_SETTINGS'] = {'HOST':'mongodb://careful:123456abc@ds127771.mlab.com:27771/careful','DB': 'careful'}
db = MongoEngine(app)
appbuilder = AppBuilder(app, security_manager_class=SecurityManager)

from app import views
