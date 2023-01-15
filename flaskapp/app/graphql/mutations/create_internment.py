import datetime
from pprint import pprint
import sys

from ariadne import convert_kwargs_to_snake_case

from app.models import Address, Internment, Patient, SexEnum, db
from app.serializers import InternmentSchema
from app.graphql import mutation
from app.models import Internment
from app.services.utils.decorators import token_authorization
from app.services.utils.auth import cpf_validator, cns_validator
from app.services.utils.create_comorbities_and_allergies import create_comorbidities_and_allergies

@mutation.field('createInternment')
@convert_kwargs_to_snake_case
@token_authorization
def create_internment(_, info, hpi: str, justification: str, patient: dict, cid_10_code: str, admission_datetime:str, current_user: dict):
    print('current_user', file=sys.stderr)
    print(current_user.__dict__, file=sys.stderr)
    patient['birthdate'] = datetime.datetime.strptime(patient['birthdate'], '%Y-%m-%d')
    patient['sex'] = SexEnum[patient['sex']]
    # Verifica se já existe o paciente pelos campos únicos: `cpf`, `cns` e `rg`
    if 'cns' in patient.keys():
        # Verifica se o CNS é válido
        if cns_validator.validate(patient['cns']) is False:
            raise Exception('Número de CNS inválido')
        stored_patient = db.session.query(Patient).filter(Patient.cns != None).filter(
            Patient.cns == patient['cns']).one_or_none()
    if not stored_patient and 'cpf' in patient.keys():
        if cpf_validator.validate(patient['cpf']) is False:
            raise Exception('Número de CPF inválido')
        stored_patient = db.session.query(Patient).filter(Patient.cpf != None).filter(
            Patient.cpf == patient['cpf']).one_or_none()
    if not stored_patient and 'rg' in patient.keys():
        stored_patient = db.session.query(Patient).filter(Patient.rg != None).filter(
            Patient.rg == patient['rg']).one_or_none()

    if stored_patient:
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
    else:
        # Cria novo paciente
        comorbidities, allergies = create_comorbidities_and_allergies(input_patient=patient).values()
        del patient['comorbidities']
        del patient['allergies']
        new_address = Address(**patient['address'])
        db.session.add(new_address)
        del patient['address']
        patient_model = Patient(**patient)
        patient_model.comorbidities.extend(comorbidities)
        patient_model.allergies.extend(allergies)
        db.session.add(patient_model)
    
    db.session.commit()

    # Cria o internamento
    internment = Internment(
        admission_datetime=datetime.datetime.strptime(admission_datetime, '%Y-%m-%d %H:%M'),
        hpi=hpi,
        justification=justification,
        waiting_vacancy=False,
        regulation_code='',
        patient_id=patient_model.id,
        professional_id=current_user.id,
        cid10_code=cid_10_code
    )

    db.session.add(internment)
    db.session.commit()
    
    schema = InternmentSchema()
    return {
        **schema.dump(internment),
        'patient': patient_model
    }
