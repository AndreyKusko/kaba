import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    debug = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # APP_SETTINGS = 'config.DevelopmentConfig'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = 'postgres://kaba_db_user:InterViewsMakeMe8annaDie@localhost:5432/kaba_db'


class ProductionConfig(Configuration):
    DEBUG = False


class StagingConfig(Configuration):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Configuration):
    DEVELOPMENT = True
    DEBUG = True



class TestingConfig(Configuration):
    TESTING = True
