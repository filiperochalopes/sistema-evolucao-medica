from app.views.api import auth as api_blueprint
from app.views.main import main as main_blueprint
from flask import Flask
from flask_migrate import Migrate
from flask_scss import Scss
from app.models import db
from app.models import User
from flask import Blueprint, render_template

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


main = Blueprint('main', __name__)

@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def index(path):
    return render_template('index.html')

app.register_blueprint(api_blueprint)
app.register_blueprint(main_blueprint)

@app.cli.command("seed")
def seed():
    """Seed the database."""
    user_1 = User(username="medico", password="senha@123".encode('utf-8'))
    db.session.add(user_1)
    db.session.commit()
    print(user_1)