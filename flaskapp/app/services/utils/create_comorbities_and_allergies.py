import sys
from app.models import Allergy, Comorbidity, db

def create_comorbidities_and_allergies(input_patient: dict) -> dict:
    '''Pega o dicionário `input_patient``` para capturar os campos de alergias e comorbidades, devolvendo um diionário com esses elementos'''

    # Edita e atualiza o paciente com os novos dados atuais. Criação de Comorbidades
    comorbidities = []
    for comorbidity_name in input_patient['comorbidities']:
        # Verifica se já existe a comorbidade no banco de dados
        if len(db.session.query(Comorbidity).filter(Comorbidity.value==comorbidity_name).all()) <= 0:
            comorbidity = Comorbidity(value=comorbidity_name)
            db.session.add(comorbidity)
            comorbidities.append(comorbidity)
        else:
            comorbidities.append(db.session.query(Comorbidity).filter(Comorbidity.value==comorbidity_name).one())
    # Criação de Alergias
    allergies = []
    for allergy_name in input_patient['allergies']:
        print(allergy_name, file=sys.stderr)
        if len(db.session.query(Allergy).filter(Allergy.value==allergy_name).all()) <= 0:
            allergy = Allergy(value=allergy_name)
            db.session.add(allergy)
            allergies.append(allergy)
        else:
            allergies.append(db.session.query(Allergy).filter(Allergy.value==allergy_name).one())
    
    # TODO Verifica quais comorbidades e alergias adicionadas não existem para remover esse usuário caso input_patient traga consigo um id
    
    return {
        'comorbidities': comorbidities,
        'allergies': allergies
    }