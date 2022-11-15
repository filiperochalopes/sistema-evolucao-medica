from datetime import datetime
import sys

from ariadne import convert_kwargs_to_snake_case

from app.serializers import PrescriptionSchema, EvolutionSchema
from app.graphql import mutation
from app.models import db, Internment, Evolution, RestingActivity, Diet, Drug, DrugKindEnum, DrugPrescription, Prescription, NursingActivity, Pending
from app.utils.decorators import token_authorization

@mutation.field('createPrescription')
@convert_kwargs_to_snake_case
@token_authorization
def create_prescription(_, info, internment_id:int, text:str, prescription:dict, pendings:str, cid_10_code: str, current_user: dict):
    # Determinando internamento
    internment = db.session.query(Internment).get(internment_id)
    # Determinando profissional que está registrando
    professional = current_user

    # Cria a prescrição
    prescription_model = Prescription(created_at=datetime.now())
    db.session.add(prescription_model)
    db.session.flush()
    # Cria ou seleciona a atividade de descanso
    try:
        resting_activity = db.session.query(RestingActivity).filter(RestingActivity.name == prescription['resting_activity']).one()
    except Exception:
        resting_activity = RestingActivity(name=prescription['resting_activity'])
        db.session.add(resting_activity)
        db.session.flush()    

    prescription_model.resting_activity = resting_activity

    # Cria ou seleciona a dieta
    try:
        diet = db.session.query(Diet).filter(Diet.name == prescription['diet']).one()
    except Exception:
        diet = Diet(name=prescription['diet'])
        db.session.add(diet)
        db.session.flush()    

    prescription_model.diet = diet
    
    # Cria as prescrições de medicações e as drugs, se necessário
    drug_prescriptions_raw = prescription['drugs']
    for drug_prescription in drug_prescriptions_raw:
        # Seleciona ou cria a medicação utilizada
        try:
            drug = db.session.query(Drug).filter(Drug.name == drug_prescription['drug_name']).filter(Drug.usual_route == drug_prescription['route']).one()
        except Exception:
            drug = Drug(name=drug_prescription['drug_name'], usual_dosage=drug_prescription['dosage'], usual_route=drug_prescription['route'], kind=DrugKindEnum[drug_prescription['drug_kind']])
            db.session.add(drug)
            db.session.flush()
        timestamp = {}
        if drug.kind == DrugKindEnum.atb:
            try:
                timestamp = {
                    'initial_date': datetime.strptime(drug_prescription['initial_date'], '%Y-%m-%d %H:%M:%S'),
                    'ending_date': datetime.strptime(drug_prescription['ending_date'], '%Y-%m-%d %H:%M:%S'),
                }
            except Exception as e:
                raise Exception(f'É obrigatório colocar a data inicial e de previsão de término em uso de antibióticos, {e}')
        drug_prescription = DrugPrescription(drug_id=drug.id, dosage=drug_prescription['dosage'], route=drug_prescription['route'], prescription_id=prescription_model.id, **timestamp)
        db.session.add(drug_prescription)    
        db.session.flush()    
        prescription_model.drug_prescriptions.append(drug_prescription)

    # Cria ou seleciona as atividades de enfermagem
    for nursing_activity_name in prescription['nursing_activities']:
        try:
            nursing_activity = db.session.query(NursingActivity).filter(NursingActivity.name == nursing_activity_name).one()
        except Exception:
            nursing_activity = NursingActivity(name=nursing_activity_name)
            db.session.add(nursing_activity)
            db.session.flush()    
        prescription_model.nursing_activities.append(nursing_activity)
    
    db.session.commit()    
    schema = PrescriptionSchema()

    return schema.dump(prescription_model)
