import os
path = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Abood2004@127.0.0.1:3306/inote"
    SQLALCHEMY_DB_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECERET_KEY = "\xc0%\\QJqa\xb8\xc0\x92\x18u\x82sZ|\x9d\r(*rM\x0b\x88"