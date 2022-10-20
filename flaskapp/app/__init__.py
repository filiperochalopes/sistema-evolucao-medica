from .graphql import query, type_defs, mutation
from flask import Flask, request, jsonify, send_from_directory
from flask_migrate import Migrate
from ariadne import graphql_sync, make_executable_schema
from flask_scss import Scss
from ariadne.constants import PLAYGROUND_HTML
from app.models import Config, db
from app.models import User
from app.serializers import ma
from flask import Blueprint, render_template

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['AUTOCRUD_METADATA_ENABLED'] = True
app.secret_key = os.getenv('SECRET_KEY')

db.init_app(app)
ma.init_app(app)



# AutoCrud(app, db)
migrate = Migrate(app, db)
Scss(app, static_dir='app/static/css', asset_dir='app/assets/scss')


main = Blueprint('main', __name__)


@app.route('/templates/reactapp/build/<path:path>')
def send_report(path):
    return send_from_directory('templates/reactapp/build', path)


@main.route('/<path:path>')
def index(path):
    return render_template('reactapp/build/index.html')


schema = make_executable_schema(type_defs, [query, mutation])


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


app.register_blueprint(main)

'''
Comandos flask cli
'''


@app.cli.command("seed")
def seed():
    """Seed the database."""

    # Adicionando configurações das instituições
    configs = [
        Config(key='insitution_name',
               value='Hospital Maternidade Luís Eduardo Magalhães'),
        Config(key='insitution_cnes', value='2602202')
    ]
    db.session.bulk_save_objects(configs)

    # Adicionando usuário para testes
    user_test = User(username="medico", password="senha@123".encode('utf-8'))
    db.session.add(user_test)

    # Enviando informações para o banco
    db.session.commit()
