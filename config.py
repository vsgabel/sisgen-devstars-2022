import os

class Config:
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class Desenvolvimento(Config):
    DEBUG = True

class Teste(Config):
    DEBUG = True

class Producao(Config):
    Debug = False

config = {
    'dev': Desenvolvimento,
    'test': Teste,
    'prod': Producao,

    'default': Desenvolvimento 
}