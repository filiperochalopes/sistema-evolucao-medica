from app.routes.auth import auth as auth_blueprint
from app.routes.main import main as main_blueprint
from flask_autocrud import AutoCrud
from flask_login import LoginManager
from flask import Flask
from flask_migrate import Migrate
from flask_scss import Scss
from app.models import db
from app.models import User
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['AUTOCRUD_METADATA_ENABLED'] = True
app.secret_key = os.getenv('SECRET_KEY')

db.init_app(app)


# AutoCrud(app, db)
migrate = Migrate(app, db)
Scss(app, static_dir='app/static/css', asset_dir='app/assets/scss')

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

@app.cli.command("seed")
def seed():
    """Seed the database."""
    user_1 = User(username="medico", password="senha@123".encode('utf-8'))
    db.session.add(user_1)
    db.session.commit()
    print(user_1)