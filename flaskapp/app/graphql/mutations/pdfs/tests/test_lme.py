from pdfs import pdf_lme
import datetime
from flask import Response

global lenght_test
lenght_test = ''
for x in range(0, 1100):
    lenght_test += str(x)


def data_to_use(establishment_solitc_name='Establishment Solicit Name',
establishment_solitc_cnes=1234567,
patient_name='Patient Name',
patient_mother_name='Patient Mother Name',
patient_weight=142,
patient_height=180,
cid10='A123',
anamnese="Anamnese",
prof_solicitor_name="Professional Solicitor Name",
solicitation_datetime=datetime.datetime.now(),
prof_solicitor_document={'CPF':28445400070},
capacity_attest=['nao', 'Responsible Name'],
filled_by=['MEDICO', 'Other name', {'CPF':28445400070}],
patient_ethnicity=['SEMINFO', 'Patient Ethnicity'],
previous_treatment=['SIM', 'Previout Theatment'],
diagnostic='Diagnostic',
patient_document={'CNS':928976954930007},
patient_email='patietemail@gmail.com',
contacts_phonenumbers=[1254875652, 4578456598],
medicines=[{"medicine_name":lenght_test[:60], "quant_1month":"20 comp", "quant_2month":"15 comp", "quant_3month":"5 comp"}, {"medicine_name":lenght_test[:60], "quant_1month":"20 comp", "quant_2month":"15 comp", "quant_3month":"5 comp"}, {"medicine_name":lenght_test[:60], "quant_1month":"20 comp", "quant_2month":"15 comp", "quant_3month":"5 comp"}, {"medicine_name":lenght_test[:60], "quant_1month":"20 comp", "quant_2month":"15 comp", "quant_3month":"5 comp"}, {"medicine_name":lenght_test[:60], "quant_1month":"20 comp", "quant_2month":"15 comp", "quant_3month":"5 comp"}]
    ):
    return pdf_lme.fill_pdf_lme(establishment_solitc_name,establishment_solitc_cnes,patient_name,patient_mother_name,patient_weight,patient_height,cid10,anamnese,prof_solicitor_name,solicitation_datetime,prof_solicitor_document,capacity_attest,filled_by,patient_ethnicity,previous_treatment,diagnostic,patient_document,patient_email,contacts_phonenumbers,medicines)


#Testing APAC
def test_with_data_in_function():
    assert type(data_to_use()) != type(Response())

def test_answer_with_all_fields():
    assert type(data_to_use()) != type(Response())

def test_awnser_with_only_required_data():
    assert type(pdf_lme.fill_pdf_lme(
        establishment_solitc_name='Establishment Solicit Name',
establishment_solitc_cnes=1234567,
patient_name='Patient Name',
patient_mother_name='Patient Mother Name',
patient_weight=142,
patient_height=180,
cid10='A123',
anamnese="Anamnese",
prof_solicitor_name="Professional Solicitor Name",
solicitation_datetime=datetime.datetime.now(),
prof_solicitor_document={'CPF':28445400070},
capacity_attest=['nao', 'Responsible Name'],
filled_by=['MEDICO', 'Other name', {'CPF':28445400070}],
patient_ethnicity=['SEMINFO', 'Patient Ethnicity'],
previous_treatment=['SIM', 'Previout Theatment'])) != type(Response())


##############################################################
# ERRORS IN NAMES CAMPS
# establishment_solitc_name
# patient_name
# patient_mother_name
# cappacity attest [patient_responsible_name]
# prof_solicitor_name
# !!!!!!! TESTING !!!!!!!
# Name empty
# Name with space
# long name
# short name
# wrong name type

def test_empty_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name='').status == Response(status=400).status

def test_with_space_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name='  ').status == Response(status=400).status

def test_long_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name=lenght_test[:70]).status == Response(status=400).status

def test_short_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name='bro').status == Response(status=400).status

def test_wrongtype_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name=123124).status == Response(status=400).status

def test_empty_patient_name():    
    assert data_to_use(patient_name='').status == Response(status=400).status

def test_with_space_patient_name():    
    assert data_to_use(patient_name='  ').status == Response(status=400).status

def test_long_patient_name():    
    assert data_to_use(patient_name=lenght_test[:81]).status == Response(status=400).status

def test_short_patient_name():    
    assert data_to_use(patient_name='bro').status == Response(status=400).status

def test_wrongtype_patient_name():    
    assert data_to_use(patient_name=123124).status == Response(status=400).status

def test_empty_patient_mother_name():    
    assert data_to_use(patient_mother_name='').status == Response(status=400).status

def test_with_space_patient_mother_name():    
    assert data_to_use(patient_mother_name='  ').status == Response(status=400).status

def test_long_patient_mother_name():    
    assert data_to_use(patient_mother_name=lenght_test[:81]).status == Response(status=400).status

def test_short_patient_mother_name():    
    assert data_to_use(patient_mother_name='bro').status == Response(status=400).status

def test_wrongtype_patient_mother_name():    
    assert data_to_use(patient_mother_name=123124).status == Response(status=400).status

def test_empty_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='').status == Response(status=400).status

def test_with_space_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='  ').status == Response(status=400).status

def test_long_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=lenght_test[:50]).status == Response(status=400).status

def test_short_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='bro').status == Response(status=400).status

def test_wrongtype_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=123124).status == Response(status=400).status

def test_empty_capacity_attest_responsible_name():    
    assert data_to_use(capacity_attest='').status == Response(status=400).status

def test_with_space_capacity_attest_responsible_name():    
    assert data_to_use(capacity_attest='  ').status == Response(status=400).status

def test_long_capacity_attest_responsible_name():    
    assert data_to_use(capacity_attest=['sim', lenght_test[:50]]).status == Response(status=400).status

def test_short_capacity_attest_responsible_name():    
    assert data_to_use(capacity_attest='bro').status == Response(status=400).status

def test_wrongtype_capacity_attest_responsible_name():    
    assert data_to_use(capacity_attest=123124).status == Response(status=400).status


####################################################################
# TEST CNES 
# establishment_solitc_cnes
# empty
# wrong type
# invalid cnes

def test_empty_establishment_solitc_cnes():
    assert data_to_use(establishment_solitc_cnes='').status == Response(status=400).status

def test_wrongtype_establishment_solitc_cnes():
    assert data_to_use(establishment_solitc_cnes='adsadad').status == Response(status=400).status

def test_invalidcnes_establishment_solitc_cnes():
    assert data_to_use(establishment_solitc_cnes=451236548).status == Response(status=400).status













