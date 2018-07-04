import os
from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP
basedir = os.path.abspath(os.path.dirname(__file__))

# App secret key
SECRET_KEY = '\2\1thdbfhsdfgzgdshrshhsfcretkey\1\2\e\y\y\h'

port = int(os.environ.get("PORT", 5000))
# The MongoEngine connection string.
MONGODB_SETTINGS = {
    'db': 'heroku_0dv5k10h', 
    'host': 'mongodb://heroku_0dv5k10h:9n9es8sdacme97kqt9duq59p86@ds127851.mlab.com:27851/heroku_0dv5k10h',
    'port': port
}

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

APP_NAME = "TOME"

#----------------------------------------------------
# AUTHENTICATION CONFIG
#----------------------------------------------------
# The authentication type
# AUTH_DB : Is for database (username/password()
AUTH_TYPE = AUTH_DB

#---------------------------------------------------
# Babel config for translations
#---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = 'en'
# Application default translation path
BABEL_DEFAULT_FOLDER = 'translations'
# The allowed translation for the app
LANGUAGES = {
    'en': {'flag':'gb', 'name':'English'},
    'pt': {'flag':'pt', 'name':'Portuguese'},
    'pt_BR': {'flag':'br', 'name': 'Pt Brazil'},
    'es': {'flag':'es', 'name':'Spanish'},
    'de': {'flag':'de', 'name':'German'},
    'zh': {'flag':'cn', 'name':'Chinese'},
    'ru': {'flag':'ru', 'name':'Russian'}
}

#---------------------------------------------------
# Image and file configuration
#---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload url, when using models with images
IMG_UPLOAD_URL = '/static/uploads/'
# Setup image size default is (300, 200, True)
#IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
APP_THEME = "readable.css"
