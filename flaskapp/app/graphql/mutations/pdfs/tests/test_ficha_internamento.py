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
    assert type(pdf_ficha_internamento.fill_pdf_ficha_internamento(documentDatetime=datetime.datetime.now(), 
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
        ddocumentDatetime=datetime.datetime.now(), 
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


if __name__ == "__main__":
    pdf_ficha_internamento.fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="iashubfiuyasgfuygasfgasygifuygsayfiasuygfyagsfiuygsydgfaiuyfyausfgiuasgfyagsfiuasgyfiuasygfvisuyagfiuyasfguyagfiuysagfiuyagfiuyg",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CPF':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        )