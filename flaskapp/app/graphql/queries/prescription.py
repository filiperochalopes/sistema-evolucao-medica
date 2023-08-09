from datetime import datetime, timedelta
from app.graphql import query
from ariadne import convert_kwargs_to_snake_case
from app.models import Diet, Drug, DrugGroupPreset, NursingActivity, RestingActivity, db
from app.serializers import DrugGroupPresetSchema, DrugSchema

@query.field("prescription")
@convert_kwargs_to_snake_case
def prescription(*_, patient_id:int=None, initial_datetime:str=datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%dT7:00:00'), ending_datetime:str=datetime.strftime(datetime.now(), '%Y-%m-%dT%H:%M:%S')):
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
    schema = DrugSchema(many=True)
    return schema.dump(db.session.query(Drug).all())

@query.field("nursingActivities")
def nursing_activity_list(*_):
    return db.session.query(NursingActivity).all()

@query.field("drugPresets")
def drug_group_preset_list(*_):
    schema = DrugGroupPresetSchema(many=True)
    return schema.dump(db.session.query(DrugGroupPreset).all())

@query.field("prescriptionTypes")
def prescription_type_list(*_):
    return [
        {
            'label': 'Atividades de descanso',
            'name': 'restingActivity',
            'querySeed': 'restingActivities'
        },
        {
            'label': 'Dieta',
            'name': 'diet',
            'querySeed': 'diets'
        },
        {
            'label': 'Medicação',
            'name': 'drug',
            'querySeed': 'drugs'
        },
        {
            'label': 'Atividades de enfermagem',
            'name': 'nursingActivity',
            'querySeed': 'nursingActivities'
        },
    ]

@query.field("drugRoutes")
def drug_route_list(*_):
    return [
        'Intramuscular',
        'Inalatória por via nasal',
        'Inalatória por via oral',
        'Subcutânea',
        'Sublingual',
        'Endovenosa',
        'Retal',
        'Local/Tópica',
        'Traqueal',
        'Nasal',
        'Oral',
    ]