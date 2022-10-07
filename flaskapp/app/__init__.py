from app.views.auth import auth as auth_blueprint
from app.views.main import main as main_blueprint
from flask_login import LoginManager
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_scss import Scss
from flask_marshmallow import Marshmallow
from ariadne.constants import PLAYGROUND_HTML
from ariadne import graphql_sync, make_executable_schema
from app.models import db
from app.models import User
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['AUTOCRUD_METADATA_ENABLED'] = True
app.secret_key = os.getenv('SECRET_KEY')

db.init_app(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)
Scss(app, static_dir='app/static/css', asset_dir='app/assets/scss')

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

from .graphql import query, type_defs, resolvers
schema = make_executable_schema(type_defs, query)

@app.route("/api/v1/graphql", methods=["GET"])
def graphql_playground():
    '''
    Create a GraphQL Playground UI for the GraphQL schema
    '''
    # Playground accepts GET requests only.
    # If you wanted to support POST you'd have to
    # change the method to POST and set the content
    # type header to application/graphql
    return PLAYGROUND_HTML

# Create a GraphQL endpoint for executing GraphQL queries


@app.route("/api/v1/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema, data, context_value={"request": request})
    status_code = 200 if success else 400
    return jsonify(result), status_code


'''
Comandos flask cli
'''

@app.cli.command("seed")
def seed():
    """Seed the database."""
    user_1 = User(username="medico", password="senha@123".encode('utf-8'))
    db.session.add(user_1)
    db.session.commit()
    print(user_1)