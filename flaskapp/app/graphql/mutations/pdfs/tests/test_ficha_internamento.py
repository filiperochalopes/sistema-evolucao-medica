#from ..pdf_ficha_internamento import fill_pdf_ficha_internamento
from .. import pdf_ficha_internamento
import datetime
from flask import Response


def data_to_use(documentDatetime=datetime.datetime.now(), patient_name="Patient Name",patient_cns=928976954930007,patient_birthday=datetime.datetime.now(),patient_sex='F',patient_motherName="Patient Mother Name",patient_document={'CPF':28445400070},patient_adress='pacient street, 43, paciten, USA',patient_phonenumber=44387694628, patient_drug_allergies=['Penicillin', 'Aspirin', 'Ibuprofen', 'Anticonvulsants'], patient_comorbidities=['Heart disease', 'High blood pressure', 'Diabetes', 'Cerebrovascular disease'],current_illness_history='Current illnes hsitoryaaaaaaaaaaa',initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',doctor_name='Doctor Name',doctor_cns=928976954930007,doctor_crm='CRM/UF 123456',patient_adressNumber=123456,patient_adressNeigh='Patient Neighborhood',patient_adressCity='Patient city',patient_adressUF='sp',patient_adressCEP=12345678,patient_nationality='Brasileira',patient_estimateWeight=123.32,has_additional_healthInsurance=False):
    return pdf_ficha_internamento.fill_pdf_ficha_internamento(documentDatetime,patient_name, patient_cns, patient_birthday, patient_sex,  patient_motherName, patient_document, patient_adress, patient_phonenumber, patient_drug_allergies, patient_comorbidities, current_illness_history,initial_diagnostic_suspicion, doctor_name, doctor_cns, doctor_crm,patient_adressNumber, patient_adressNeigh, patient_adressCity, patient_adressUF, patient_adressCEP, patient_nationality, patient_estimateWeight, has_additional_healthInsurance)


#Testing Ficha Internamento
def test_answer_with_all_fields():
    """Test fill ficha internamento with all data correct"""
    assert data_to_use() != type(Response())


def test_awnser_with_only_required_data():
    assert type(pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CPF':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_drug_allergies=['Penicillin', 'Aspirin', 'Ibuprofen', 'Anticonvulsants'],
        patient_comorbidities=['Heart disease', 'High blood pressure', 'Diabetes', 'Cerebrovascular disease'],
        current_illness_history='Current illnes hsitoryaaaaaaaaaaa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456'
        )) != type(Response())

##############################################################
# ERRORS IN NAMES CAMPS
# patient_name
# patient_motherName
# doctor_name
# !!!!!!! TESTING !!!!!!!
# Name empty
# Name with space
# long name
# short name
# wrong name type

global lenghtTest
lenghtTest = ''
for x in range(0, 1100):
    lenghtTest += str(x)

def test_wrongtype_patient_name():    
    assert data_to_use(patient_name=123124).status == Response(status=400).status

def test_empty_patient_name():    
    assert data_to_use(patient_name='').status == Response(status=400).status

def test_with_space_patient_name():    
    assert data_to_use(patient_name='  ').status == Response(status=400).status

def test_long_patient_name():    
    assert data_to_use(patient_name=str(lenghtTest[:70])).status == Response(status=400).status

def test_short_patient_name():    
    assert data_to_use(patient_name='11113').status == Response(status=400).status

def test_wrongtype_patient_motherName():    
    assert data_to_use(patient_motherName=123124).status == Response(status=400).status

def test_empty_patient_motherName():    
    assert data_to_use(patient_motherName='').status == Response(status=400).status

def test_with_space_patient_motherName():    
    assert data_to_use(patient_motherName='  ').status == Response(status=400).status

def test_long_patient_motherName():    
    assert data_to_use(patient_motherName=str(lenghtTest[:70])).status == Response(status=400).status

def test_short_patient_motherName():    
    assert data_to_use(patient_motherName='11113').status == Response(status=400).status

def test_wrongtype_doctor_name():    
    assert data_to_use(doctor_name=123124).status == Response(status=400).status

def test_empty_doctor_name():    
    assert data_to_use(doctor_name='').status == Response(status=400).status

def test_with_space_doctor_name():    
    assert data_to_use(doctor_name='  ').status == Response(status=400).status

def test_long_doctor_name():    
    assert data_to_use(doctor_name=str(lenghtTest[:70])).status == Response(status=400).status

def test_short_doctor_name():    
    assert data_to_use(doctor_name='11113').status == Response(status=400).status
