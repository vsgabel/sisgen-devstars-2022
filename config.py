import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if "postgre://" in SQLALCHEMY_DATABASE_URI:
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgre://", "postgresql://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SSL_REDIRECT = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

    @staticmethod
    def init_app(app):
        import logging
        from logging import FileHandler

        handler = FileHandler("log.log", 'a')
        handler.setLevel(logging.INFO)

        app.logger.addHandler(handler)

class HerokuConfig(ProductionConfig):
    SSL_REDIRECT = True if os.getenv("DYNO") else False

    @staticmethod
    def init_app(app):
        ProductionConfig.init_app(app)

        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)
    

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig 
}