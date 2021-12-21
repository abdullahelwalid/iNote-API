import os
path = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(path, 'database.db')
    SQLALCHEMY_DB_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False