# DEBUG = True
import os

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    SECRET_KEY = 'ABC'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    SECRET_KEY = os.urandom(16)


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    # secret_key
    SECRET_KEY = 'ABC'


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'ABC'
