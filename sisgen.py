import os
from app import create_app, db
from flask_migrate import Migrate
from app.models import * 

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()