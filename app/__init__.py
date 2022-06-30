from flask import Flask
from flask_mail import Mail
from config import config

mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    mail.init_app(app)

    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    return app
