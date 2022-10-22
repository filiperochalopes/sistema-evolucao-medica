import datetime
import sys

from ariadne import convert_kwargs_to_snake_case

from app.models import Allergy, Comorbidity, Internment, Patient, SexEnum, db
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

    def create_comobidities_allergies(input_patient, patient_model):
        # Edita e atualiza o paciente com os novos dados atuais. Criação de Comorbidades
        for comorbidity_name in input_patient.comorbidities:
            # Verifica se já existe a comorbidade no banco de dados
            patient_model.comorbities.clear()
            if len(db.session.query(Comorbidity).filter(Comorbidity.value==comorbidity_name).all()) <= 0:
                comorbidity = Comorbidity(value=comorbidity_name)
                patient_model.comorbities.append(comorbidity)
            else:
                patient_model.comorbities.append(db.session.query(Comorbidity).filter(Comorbidity.value==comorbidity_name).one())
        # Criação de Alergias
        for allergy_name in input_patient.allergies:
            patient_model.allergies.clear()
            if len(db.session.query(Allergy).filter(Allergy.value==allergy_name).all()) <= 0:
                allergy = Allergy(value=allergy_name)
                patient_model.allergies.append(allergy)
            else:
                patient_model.allergies.append(db.session.query(Allergy).filter(Allergy.value==allergy_name).one())

    if stored_patient:
        create_comobidities_allergies(input_patient=patient, patient_model=stored_patient)
        # patient = None
        pass
    else:
        # Cria novo paciente
        new_patient = Patient(**patient)
        # patient.address
        create_comobidities_allergies(input_patient=patient, patient_model=new_patient)
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
