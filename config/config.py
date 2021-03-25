from .env_vars import *
DB_URI = "mysql+pymysql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = "environ.get('SECRET_KEY')"
    # FLASK_APP = environ.get('FLASK_APP')
    # FLASK_ENV = environ.get('FLASK_ENV')

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True