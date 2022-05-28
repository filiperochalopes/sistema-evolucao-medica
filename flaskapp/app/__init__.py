from flask_login import LoginManager
from app.routes.auth import auth as auth_blueprint
from app.routes.main import main as main_blueprint
from flask import Flask
from flask_migrate import Migrate
from flask_scss import Scss
from flask_bcrypt import Bcrypt
from app.models import db
from app.models import User


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite3.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)
Scss(app, static_dir='app/static/css', asset_dir='app/assets/scss')

app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.cli.command("seed")
def seed():
    """Seed the database."""
    user_1 = User(username="medico", password="senha@123")
    db.session.add(user_1)
    db.session.commit()
    print(user_1)
