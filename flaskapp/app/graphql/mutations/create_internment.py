import datetime
import sys

from sqlalchemy import or_
from ariadne import convert_kwargs_to_snake_case

from app.models import Internment, Patient, SexEnum, db
from app.serializers import InternmentSchema, PatientSchema
from app.graphql import mutation
from app.models import Internment
from app.utils.decorators import token_authorization


@mutation.field('createInternment')
@convert_kwargs_to_snake_case
@token_authorization
def create_internment(_, info, hpi: str, justification: str, patient: dict, cid_10_code: str, current_user: dict):
    print('current_user', file=sys.stderr)
    print(current_user.__dict__, file=sys.stderr)
    patient['birthday'] = datetime.datetime.strptime(patient['birthday'], '%Y-%m-%d')
    patient['sex'] = SexEnum[patient['sex']]
    patientSchema = PatientSchema()    
    print(patient, file=sys.stderr)
    print(patientSchema.dump(patient), file=sys.stderr)

    # Verifica se já existe o paciente pelos campos únicos: `cpf`, `cns` e `rg`
    if 'cns' in patient.keys():
        stored_patient = db.session.query(Patient).filter(Patient.cns != None).filter(
            Patient.cns == patient['cns']).one_or_none()
    if not stored_patient and 'cpf' in patient.keys():
        stored_patient = db.session.query(Patient).filter(Patient.cpf != None).filter(
            Patient.cpf == patient['cpf']).one_or_none()
    if not stored_patient and 'rg' in patient.keys():
        stored_patient = db.session.query(Patient).filter(Patient.rg != None).filter(
            Patient.rg == patient['rg']).one_or_none()

    if stored_patient:
        # Edita e atualiza o paciente com os novos dados atuais
        # patient.comorbities=
        # patient = None
        pass
    else:
        # Cria novo paciente
        patient = Patient(**patient)
        # patient.address
        # patient.comorbities
        # patient.allergies
    db.session.flush()

    # Cria o internamento
    internment = Internment(
        hpi=hpi,
        justification=justification,
        waiting_vacancy=False,
        regulation_code='',
        patient_id=patient.id,
        professional_id=current_user.id,
        cid10_code=cid_10_code
    )

    db.session.add(internment)
    db.session.flush()
    # db.session.commit()
    print(internment.__dict__, file=sys.stderr)
    schema = InternmentSchema()
    return {
        **schema.dump(internment),
        'patient': patient
    }
