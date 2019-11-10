import os
# SECRET_KEY = os.urandom(16)
# print(99999)
# SECRET_KEY = 'abc'
# DEBUG = False
# ENV = 'production'

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    SECRET_KEY = 'ABC'


class ProductionConfig(Config):
    # DATABASE_URI = 'mysql://user@localhost/foo'
    # DATABASE = 'flaskr.sqlite',
    SECRET_KEY = os.urandom(16)
    DEBUG = True
    ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    # secret_key
    SECRET_KEY = 'ABC'


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'ABC'
