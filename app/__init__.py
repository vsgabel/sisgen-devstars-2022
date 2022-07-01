from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config

mail = Mail()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    mail.init_app(app)

    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    return app
