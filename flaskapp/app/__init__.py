import json
import sys
from datetime import datetime
from app.models import User, ProfessionalCategoryEnum
from app.services.utils.auth import cpf_validator, cns_validator
from app.models import User
from app.env import InstitutionData, DatabaseSettings
from .graphql import query, type_defs, mutation
from .graphql.generate_pdf_schema import generate_pdf_type_defs
from .graphql.print_pdf_schema import print_pdf_type_defs
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from ariadne import graphql_sync, make_executable_schema
from flask_scss import Scss
from ariadne.constants import PLAYGROUND_HTML
from app.models import DrugGroupPreset, db, Cid10, Config, Diet, Drug, DrugKindEnum, FluidBalanceDescription, NursingActivity, RestingActivity, State, Allergy, Comorbidity, HighComplexityProcedure
from flask_cors import CORS
from app.serializers import ma

import os


template_dir = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'templates')
app = Flask(__name__, static_folder='reactapp/build')
app.config['SQLALCHEMY_DATABASE_URI'] = DatabaseSettings().URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.getenv('SECRET_KEY')

db.init_app(app)
ma.init_app(app)
CORS(app)


migrate = Migrate(app, db)
Scss(app, static_dir='app/static/css', asset_dir='app/assets/scss')


schema = make_executable_schema(
    [type_defs, generate_pdf_type_defs, print_pdf_type_defs], [query, mutation])


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


@app.cli.command("create_users")
def create_users():
    encrypted_password = User.generate_password('passw@rd')
    json_file = open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'users.json'))
    users = json.load(json_file)
    user_dict = {}
    for user in users:
        user_dict = {**user}
        print(f"Cadastrando usuário {user['name']}...", file=sys.stderr)
        # Verifica o preenchimento de cpf ou cns, um dos dois devem estar preenchidos
        if 'cpf' in user and not user['cpf'] and 'cns' in user and not user['cns']:
            raise Exception(
                'CPF ou CNS devem estar preenchidos, os dois campos não podem ficar em branco')
        if 'cns' in user and user['cns'] is not None:
            if cns_validator.validate(user['cns']) is False:
                raise Exception(f'Número de CNS {user["cns"]} inválido')
        if 'cpf' in user and user['cpf'] is not None:
            if cpf_validator.validate(user['cpf']) is False:
                raise Exception('Número de CPF inválido')

        user_dict['professional_category'] = ProfessionalCategoryEnum[user['professional_category']]
        user_dict['birthdate'] = datetime.strptime(
            user['birthdate'], '%Y-%m-%d')
        user_dict['password_hash'] = encrypted_password
        new_user = User(**user_dict)
        db.session.add(new_user)
        db.session.commit()


@app.cli.command("seed")
def seed():
    """Seed the database."""
    import csv

    # Cadastrando lista de Cid10
    with open(os.path.join(os.path.dirname(__file__), 'assets', 'CID-10-DATASUS.csv'), 'r', encoding='ISO-8859-1') as file:
        csvreader = csv.reader(file, dialect='excel', delimiter=';')
        next(file)
        for row in csvreader:
            cid10 = Cid10(code=row[0], description=row[4])
            db.session.add(cid10)

    # Cadastrando lista de Estados
    with open(os.path.join(os.path.dirname(__file__), 'assets', 'ESTADOS-UF.csv'), 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        next(file)
        for row in csvreader:
            state = State(ibge_code=int(row[0]), name=row[1], uf=row[2])
            db.session.add(state)

    # Cadastrando procedimentos de alta complexidade
    with open(os.path.join(os.path.dirname(__file__), 'assets', 'HIGH-COMPLEXITY-PROCEDURES.csv'), 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        next(file)
        for row in csvreader:
            procedure = HighComplexityProcedure(name=row[0], code=row[1])
            db.session.add(procedure)

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
        Drug(name='Dipirona 500mg/mL 2ml', usual_dosage='1g (1 ampola) no momento', usual_route='Intramuscular',
             comment='Dose pediátrica: (20-25mg/kg/dose), dica: Dividir o peso em kg por 20 é a quantidade em ml a sr administrada EV/IM', kind=DrugKindEnum.oth),
        Drug(name='Diclofenaco 75mg/3ml', usual_dosage='75mg (1 ampola) no momento',
             usual_route='Intramuscular', kind=DrugKindEnum.oth),
        Drug(name='Dexametasona 10mg/2,5ml', usual_dosage='10mg (1 ampola) no momento',
             usual_route='Intramuscular', kind=DrugKindEnum.oth),
        Drug(name='Nebulização 1ml de adrenalina + 5ml de SF 0,9% + 10 gotas de Ipratrópio 0,25 mg/mL', usual_dosage='Realizar inalação', usual_route='Inalatória por via nasal',
             comment='Zhang L, Sanguebsche LS. The safety of nebulization with 3 to 5 ML of adrenaline (1:1000) in children: An evidence based review. Jornal de Pediatria. 2005;81(3):193–7.  ', kind=DrugKindEnum.oth),
        Drug(name='Ceftriaxona 1g', usual_dosage='1g 12/12h', usual_route='Endovenosa',
             comment='Dose pediátrica usual: (50mg/kg/dose) 12/12h', kind=DrugKindEnum.atb),
        Drug(name='Ciprofloxacino 200mg/100ml', usual_dosage='400mg 12/12h',
             usual_route='Endovenosa', kind=DrugKindEnum.atb),
        Drug(name='Salbutamol 100mcg/jato', usual_dosage='8 puffs 4/4h se desconforto respiratório',
             usual_route='Inalatória por via oral', kind=DrugKindEnum.oth),
        Drug(name='Trombofob gel (Heparina sódica tópica)', usual_dosage='Aplicar em região de equimose sem massagear ou friccionar 6x/dia',
             usual_route='Inalatória por via oral', kind=DrugKindEnum.oth),
        Drug(name='Chá concentrado de Chamomilla', usual_dosage='Aplicar em compressa à 38°C 3x/dia em região de flebite',
             usual_route='Local/Tópica', kind=DrugKindEnum.oth, comment='Reis, P.E. et al. (2011) ‘Clinical application of Chamomilla recutita in phlebitis: Dose response curve study’, Revista Latino-Americana de Enfermagem, 19(1), pp. 03–10. doi:10.1590/s0104-11692011000100002. '),
    ]
    db.session.bulk_save_objects(drugs)
    # Adicionando algumas atividades de enfermagem iniciais
    nursing_activities = [
        NursingActivity(name='Aferir sinais vitais 6/6h'),
        NursingActivity(
            name='Monitoração multiparamétrica contínua(cardioscopia, pressão arterial, saturação de O2'),
        NursingActivity(name='Registro de balanço hídrico'),
        NursingActivity(
            name='RN: Limpeza de coto umbilical com álcool 70% a cada troca de fraldas'),
        NursingActivity(
            name='Vigiar sangramento/loquiações e registrar perdas estimadas conforme avaliação comparativa com modelos'),
    ]
    db.session.bulk_save_objects(nursing_activities)
    # Adicionando algumas atividades de descanso
    resting_activities = [
        RestingActivity(
            name='Repouso absoluto, cabeceira elevada 30°, atenção para lesões por pressão. Variar decúbito a cada 2h'),
        RestingActivity(name='Repouso relativo'),
    ]
    db.session.bulk_save_objects(resting_activities)
    # Adicionndo alguns tipos de dieta
    diets = [
        Diet(name='Dieta livre'),
        Diet(name='Dieta livre, estimular hidratação'),
        Diet(name='Dieta lactante (Evitar FODMAPs - produtos lácteos, a soja, o trigo, ovos, os crucíferos, as frutas cítricas, o café e o chocolate)'),
        Diet(name='Dieta branda, para diabéticos (sem carboidratos simples)'),
        Diet(name='Dieta branda, para hipertensos (hipossódica)'),
        Diet(name='Dieta branda, para hipertensos e diabéticos'),
        Diet(name='Dieta pastosa'),
        Diet(name='Dieta líquida'),
        Diet(name='Dieta zero')
    ]
    db.session.bulk_save_objects(diets)
    # Adicionndo algumas descrições de Balanço hídrico
    fluid_balance_descriptions = [
        FluidBalanceDescription(value='Medicação'),
        FluidBalanceDescription(value='Hidratação Venosa (Soro)'),
        FluidBalanceDescription(value='Ingesta oral (Diversos)'),
        FluidBalanceDescription(value='Diurese'),
        FluidBalanceDescription(value='Fezes'),
    ]
    db.session.bulk_save_objects(fluid_balance_descriptions)
    # Adicionando alguns presets de grupo de medicamentos
    drug_group_preset_1 = DrugGroupPreset(
        label='Sintomáticos Internamento', name='sintomaticos')
    db.session.add(drug_group_preset_1)
    drug_group_preset_1.drugs.append(
        Drug(name='Dipirona 500mg/mL 2ml', usual_dosage='1g, 6/6h se dor ou temp axilar > 37,8°C', usual_route='Endovenosa', kind=DrugKindEnum.oth))
    drug_group_preset_1.drugs.append(Drug(name='Insulina Regular 100UI/ml',
                                          usual_dosage='Aplicar conforme protocolo da unidade se HGT > 180', usual_route='Subcutânea', kind=DrugKindEnum.oth))
    drug_group_preset_1.drugs.append(
        Drug(name='Glicose 50%', usual_dosage='Administrar 20ml se HGT < 70mg/dL', usual_route='Endovenosa', kind=DrugKindEnum.oth, comment='Em pacientes não diabéticos pode-se usar 50mg/ml como medida de corte'))
    drug_group_preset_1.drugs.append(Drug(name='Oxigênio (Catéter nasal)', usual_dosage='5l/min se SpO2 < 88%', usual_route='Endovenosa',
                                          kind=DrugKindEnum.oth, comment='Metas: DPOC 88-92%, IAM >= 90%, AVC (Stroke Oxygen Study) >= 90%'))
    drug_group_preset_2 = DrugGroupPreset(
        label='Gestante', name='gestante')
    db.session.add(drug_group_preset_2)
    drug_group_preset_2.drugs.append(
        Drug(name='Ocitocina 5UI/mL', usual_dosage='10UI (2 ampolas) UI, após nascimento do bebê', usual_route='Intramuscular', kind=DrugKindEnum.oth))
    drug_group_preset_2.drugs.append(Drug(
        name='Vitamina K 10mg/ml', usual_dosage='RN: 0,1ml ao nascer', usual_route='Intramuscular', kind=DrugKindEnum.oth))
    drug_group_preset_3 = DrugGroupPreset(
        label='Infarto Agudo - IAM', name='iam')
    db.session.add(drug_group_preset_3)
    drug_group_preset_3.drugs.append(
        Drug(name='Ácido Acetilsalicílico (AAS) 100mg', usual_dosage='3 comprimidos, mastigados', usual_route='Oral', kind=DrugKindEnum.oth))
    dipirona = db.session.query(Drug).filter(
        Drug.name == 'Dipirona 500mg/mL 2ml').first()
    # todo Quando mudar para DrugPrescriptionGroup ou até mesmo PrescriptionGroup
    # dipirona_ev.route = "Endovenosa"
    # dipirona_ev.dosage = "1g (1 ampola) no momento"
    drug_group_preset_3.drugs.append(dipirona)
    drug_group_preset_3.drugs.append(Drug(name='Mononitrato Isossorbida 5mg',
                                     usual_dosage='1 comprimido a cada 5min (à critério médico)', usual_route='Sublingual', kind=DrugKindEnum.oth))
    drug_group_preset_3.drugs.append(Drug(
        name='Clopidogrel 75mg', 
        usual_dosage='4 comprimidos, dose única', 
        comment='Realizar apenas 75mg em pacientes maiores que 75mg', usual_route='Oral', kind=DrugKindEnum.oth))
    drug_group_preset_3.drugs.append(Drug(
        name='Metoprolol 50mg', usual_dosage='1 comprimido 24/24h', usual_route='Oral', kind=DrugKindEnum.oth))

    # Adicionando alergias
    allergies = [
        Allergy(value='Dipirona'),
        Allergy(value='Penicilina'),
        Allergy(value='Nega Alergia'),
        Allergy(value='Ibuprofeno (AINES)')
    ]
    db.session.bulk_save_objects(allergies)

    # Adicionando comorbidades
    comorbidities = [
        Comorbidity(value='Nega Comorbidade'),
        Comorbidity(value='Hipertensão Arterial Sistêmica (HAS)'),
        Comorbidity(value='Diabetes Mellitus tipo 2 (DM2)'),
        Comorbidity(value='Diabetes Mellitus tipo 1 (DM1)'),
        Comorbidity(value='Tabagismo'),
        Comorbidity(value='Etilismo'),
        Comorbidity(value='Asma')
    ]
    db.session.bulk_save_objects(comorbidities)

    # Enviando informações para o banco
    db.session.commit()