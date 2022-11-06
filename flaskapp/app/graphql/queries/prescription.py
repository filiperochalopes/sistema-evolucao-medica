from datetime import datetime, timedelta
from app.graphql import query
from ariadne import convert_kwargs_to_snake_case
from app.models import Diet, Drug, NursingActivity, RestingActivity, db
from app.serializers import DrugSchema

@query.field("prescription")
@convert_kwargs_to_snake_case
def prescription(*_, patient_id:int=None, initial_datetime:str=datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d 7:00:00'), ending_datetime:str=datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')):
    '''Função que retorna as prescrições de determinado paciente'''
    return []

@query.field("restingActivities")
def resting_activity_list(*_):
    return db.session.query(RestingActivity).all()

@query.field("diets")
def diet_list(*_):
    return db.session.query(Diet).all()

@query.field("drugs")
def drug_list(*_):
    schema = DrugSchema()
    return [schema.dump(d) for d in db.session.query(Drug).all()]

@query.field("nursingActivities")
def nursing_activity_list(*_):
    return db.session.query(NursingActivity).all()

@query.field("prescriptionTypes")
def prescription_type_list(*_):
    return [
        {
            'label': 'Atividades de descanso',
            'name': 'restingActivity'
        },
        {
            'label': 'Dieta',
            'name': 'diet'
        },
        {
            'label': 'Medicação',
            'name': 'drug'
        },
        {
            'name': 'Atividades de enfermagem',
            'name': 'nursingActivity'
        },
    ]

@query.field("drugRoutes")
def drug_route_list(*_):
    return [
        'Intramuscular',
        'Inalatória por via nasal',
        'Inalatória por via oral',
        'Endovenosa',
        'Retal',
        'Traqueal',
        'Nasal',
        'Oral',
    ]