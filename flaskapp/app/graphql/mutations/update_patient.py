from ariadne import convert_kwargs_to_snake_case

from app.graphql import mutation
from app.models import db, Patient, Address
from app.utils.decorators import token_authorization
from app.serializers import PatientSchema
from app.utils.create_comorbities_and_allergies import create_comorbidities_and_allergies

@mutation.field('updatePatient')
@convert_kwargs_to_snake_case
@token_authorization
def update_patient(_, info, id:int, patient:dict, current_user:dict):
    stored_patient = db.session.query(Patient).get(id)
    updated_address = Address(**patient['address'])
    db.session.add(updated_address)
    stored_patient.address = updated_address
    del patient['address']
    stored_patient.allergies.clear()
    stored_patient.comorbidities.clear()
    comorbidities, allergies = create_comorbidities_and_allergies(input_patient=patient).values()
    stored_patient.comorbidities.extend(comorbidities)
    stored_patient.allergies.extend(allergies)
    del patient['comorbidities']
    del patient['allergies']
    for key, value in patient.items():
        setattr(stored_patient, key, value)
    patient_model = stored_patient
    db.session.add(patient_model)
    db.session.commit()

    schema = PatientSchema()
    return schema.dump(patient_model)
