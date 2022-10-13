#from ..pdf_ficha_internamento import fill_pdf_ficha_internamento
from .. import pdf_ficha_internamento
import datetime
from flask import Response


#Testing Ficha Internamento
def test_answer_with_all_fields():
    """Test fill ficha internamento with all data correct"""
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        )) != type(Response())


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

def test_answer_without_patient_adressNumber():
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
        doctor_crm='CRM/UF 123456',
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        )) != type(Response())


def test_answer_without_patient_adressNeigh():
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        )) != type(Response())

def test_answer_without_patient_adressCity():
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        )) != type(Response())

def test_answer_without_patient_adressUF():
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        )) != type(Response())


def test_answer_without_patient_adressCEP():
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        )) != type(Response())


def test_answer_without_patient_nationality():
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        )) != type(Response())


def test_answer_without_patient_estimateWeight():
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        has_additional_healthInsurance=False
        )) != type(Response())


def test_answer_without_has_additional_healthInsurance():
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        )) != type(Response())


def test_name_longer():
    """Test if can put a name with more than 60 character"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="iashubfiuyasgfuygasfgasygifuygsayfiasuygfyagsfiuygsydgfaiuyfyausfgiuasgfyagsfiuasgyfiuasygfvisuyagfiuyasfguyagfiuysagfiuyagfiuyg",
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status
        


def test_empty_name():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="",
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status


def test_with_space_name():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="         ",
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status


def test_wrong_documentdatetimeType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime='ad',
        patient_name="",
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status
    
def test_wrong_birthdaydatetimeType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday="aooads",
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_patientnametype():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name=13134,
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_sexType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex=1,
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_sexOption():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='G',
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_sexOptionExtend():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='Female',
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status


def test_wrong_pateintmothernameType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName=13134,
        patient_document={'CPF':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_drug_allergies=['Penicillin', 'Aspirin', 'Ibuprofen', 'Anticonvulsants'],
        patient_comorbidities=['Heart disease', 'High blood pressure', 'Diabetes', 'Cerebrovascular disease'],
        current_illness_history='Current illnes hsitoryaaaaaaaaaaa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status


def test_wrong_document_type():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document='caasdad',
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_drug_allergies=['Penicillin', 'Aspirin', 'Ibuprofen', 'Anticonvulsants'],
        patient_comorbidities=['Heart disease', 'High blood pressure', 'Diabetes', 'Cerebrovascular disease'],
        current_illness_history='Current illnes hsitoryaaaaaaaaaaa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_invalid_document_option():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CNS':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_drug_allergies=['Penicillin', 'Aspirin', 'Ibuprofen', 'Anticonvulsants'],
        patient_comorbidities=['Heart disease', 'High blood pressure', 'Diabetes', 'Cerebrovascular disease'],
        current_illness_history='Current illnes hsitoryaaaaaaaaaaa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_invalid_CPF():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CPF':234781568345},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_drug_allergies=['Penicillin', 'Aspirin', 'Ibuprofen', 'Anticonvulsants'],
        patient_comorbidities=['Heart disease', 'High blood pressure', 'Diabetes', 'Cerebrovascular disease'],
        current_illness_history='Current illnes hsitoryaaaaaaaaaaa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_invalidRG():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'RG':6848944314894847158},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_drug_allergies=['Penicillin', 'Aspirin', 'Ibuprofen', 'Anticonvulsants'],
        patient_comorbidities=['Heart disease', 'High blood pressure', 'Diabetes', 'Cerebrovascular disease'],
        current_illness_history='Current illnes hsitoryaaaaaaaaaaa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status


def test_wrong_patientadressType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CPF':28445400070},
        patient_adress=123124125,
        patient_phonenumber=44387694628,
        patient_drug_allergies=['Penicillin', 'Aspirin', 'Ibuprofen', 'Anticonvulsants'],
        patient_comorbidities=['Heart disease', 'High blood pressure', 'Diabetes', 'Cerebrovascular disease'],
        current_illness_history='Current illnes hsitoryaaaaaaaaaaa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status


def test_wrong_patientPhonenumberType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CPF':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber='44387694628',
        patient_drug_allergies=['Penicillin', 'Aspirin', 'Ibuprofen', 'Anticonvulsants'],
        patient_comorbidities=['Heart disease', 'High blood pressure', 'Diabetes', 'Cerebrovascular disease'],
        current_illness_history='Current illnes hsitoryaaaaaaaaaaa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_patientdrugallergies():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CPF':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_drug_allergies='wiorng that is be a list',
        patient_comorbidities=['Heart disease', 'High blood pressure', 'Diabetes', 'Cerebrovascular disease'],
        current_illness_history='Current illnes hsitoryaaaaaaaaaaa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_patientcommobidiesType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        patient_comorbidities='worng commorbidies has to be list',
        current_illness_history='Current illnes hsitoryaaaaaaaaaaa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_currentillineshistory():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        current_illness_history=['Current illnes hsitoryaaaaaaaaaaa'],
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status


def test_wrong_initialdiagnosticsuspicionType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        initial_diagnostic_suspicion=['Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.'],
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status


def test_wrong_doctornameType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_name=131241245,
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_doctorcnsType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_cns='928976954930007',
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_invalid_doctorcns():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_cns=456489489156897,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_invalid_patient_cns():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=123124124554,
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_doctorCRMType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_crm=54978151,
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_invalid_CRM():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_crm='CRM/UF 1213123423456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_patienAdressnumberType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber='123456',
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_patientNeighbouType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh=131412455,
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status


def test_wrong_patientadresscityType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity=4185998489,
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status


def test_wrong_adressCEPtype():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP='12345678',
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_invalid_patient_adressCEP():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12123345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_tolong_patient_nationality():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira12312kl389126t341624rt86712f4671fgvyiasubgdiyg1y6gbayiugdiyagfygaiuydfgasf',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_empty_patient_nationality():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        ) != type(Response())

def test_wrong_patientEstimateWirghtType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight='1414',
        has_additional_healthInsurance=False
        ).status == Response(status=400).status

def test_wrong_has_addidional_unsuranceType():
    """Test fill ficha internamento with all data correct"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(
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
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance='False'
        ).status == Response(status=400).status

