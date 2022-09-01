import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_VAR')
    SQLALCHEMY_DB_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('API_KEY')