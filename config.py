import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_VAR')
    SQLALCHEMY_DB_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "\xc0%\\QJqa\xb8\xc0\x92\x18u\x82sZ|\x9d\r(*rM\x0b\x88"