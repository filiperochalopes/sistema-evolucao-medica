from app.env import InstitutionData
from .graphql import query, type_defs, mutation
from flask import Flask, request, jsonify, send_from_directory
from flask_migrate import Migrate
from ariadne import graphql_sync, make_executable_schema
from flask_scss import Scss
from ariadne.constants import PLAYGROUND_HTML
from app.models import Cid10, Config, Drug, DrugKindEnum, db
from flask_cors import CORS
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
CORS(app)

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
    import csv

    # cadastrando lista de Cid10
    with open(os.path.join(os.path.dirname(__file__), 'assets', 'CID-10-DATASUS.csv'), 'r', encoding='ISO-8859-1') as file:
        csvreader = csv.reader(file, dialect='excel', delimiter=';')
        for row in csvreader:
            cid10 = Cid10(code=row[0], description=row[4])
            db.session.add(cid10)

    # Adicionando configurações das instituições
    configs = [
        Config(key='institution_name',
               value=InstitutionData.NAME[0]),
        Config(key='institution_cnes', value=InstitutionData.CNES[0]),
        Config(key='institution_director', value=InstitutionData.DIRECTOR[0]),
        Config(key='institution_cnpj', value=InstitutionData.CNPJ[0]),
    ]
    db.session.bulk_save_objects(configs)

    # Adicionando algumas medicações iniciais
    drugs = [
        Drug(name='Dipirona 500mg/mL 2ml', usual_dosage='1g (1 ampola) no momento', usual_route='Intramuscular', comment='Dose pediátrica: (20-25mg/kg/dose), dica: Dividir o peso em kg por 20 é a quantidade em ml a sr administrada EV/IM', kind=DrugKindEnum.oth),
        Drug(name='Diclofenaco 25mg/ml 3m', usual_dosage='75mg (1 ampola) no momento', usual_route='Intramuscular', kind=DrugKindEnum.oth),
        Drug(name='Dexametasona 4mg/2,5ml', usual_dosage='10mg (1 ampola) no momento', usual_route='Intramuscular', kind=DrugKindEnum.oth),
        Drug(name='Nebulização 1ml de adrenalina + 5ml de SF 0,9% + 10 gotas de Ipratrópio 0,25 mg/mL', usual_dosage='1g (1 ampola) no momento', usual_route='Inalatória por via nasal', comment='Zhang L, Sanguebsche LS. The safety of nebulization with 3 to 5 ML of adrenaline (1:1000) in children: An evidence based review. Jornal de Pediatria. 2005;81(3):193–7.  ', kind=DrugKindEnum.oth),
        Drug(name='Ceftriaxona 1g', usual_dosage='1g 12/12h', usual_route='Endovenoso', comment='Dose pediátrica usual: (50mg/kg/dose) 12/12h', kind=DrugKindEnum.atb),
    ]
    db.session.bulk_save_objects(drugs)
    # Adicionando algumas atividades de enfermagem iniciais
    # Adicionando algumas atividades de descanso
    # Adicionndo alguns tipos de dieta
    # Adicionndo algumas descrições de Balanço hídrico
    
    # Enviando informações para o banco
    db.session.commit()
