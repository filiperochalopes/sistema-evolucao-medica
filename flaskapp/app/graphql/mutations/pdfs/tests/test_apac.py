from .. import pdf_apac
import datetime
from flask import Response

global lenghtTest
lenghtTest = ''
for x in range(0, 1100):
    lenghtTest += str(x)

def data_to_use(establishment_solitc_name='Establishment Solicit Name',establishment_solitc_cnes=1234567,patient_name='Patient Name',patient_cns=928976954930007,patient_sex='M',patient_birthday=datetime.datetime.now(), patient_adress_city='Patient Adress City',main_procedure_name='Main procedure Name',main_procedure_code='1234567890',main_procedure_quant=4,patient_mother_name='Patient Mother Name',       patient_mother_phonenumber=5286758957, patient_responsible_name='Patient Responsible Name', patient_responsible_phonenumber=5465981345, patient_adress='Patient Adress',patient_color='Branca',patient_ethnicity='Indigena',patient_adressUF='BA',patient_adressCEP=86425910, document_chart_number=12345,patient_adress_city_IBGEcode=4528765,procedure_justification_description='Procedure Justification Description', prodedure_justification_main_cid10='A98', prodedure_justification_sec_cid10='A01', procedure_justification_associated_cause_cid10='A45',procedure_justification_comments='Procedure Justification Comments',establishment_exec_name='Establishment Exec Name', establishment_exec_cnes=7654321,prof_solicitor_document={'CPF':28445400070}, prof_solicitor_name='Profissional Solicit Name',solicitation_datetime=datetime.datetime.now(),signature_datetime=datetime.datetime.now(),validity_period_start=datetime.datetime.now(),validity_period_end=datetime.datetime.now(),autorization_prof_name='Autorization Professional Name', emission_org_code='Cod121234',autorizaton_prof_document={'CPF':28445400070}, autorizaton_datetime=datetime.datetime.now(),secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]):
    return pdf_apac.fill_pdf_apac(establishment_solitc_name, establishment_solitc_cnes, patient_name, patient_cns, patient_sex, patient_birthday, patient_adress_city, main_procedure_name, main_procedure_code, main_procedure_quant, patient_mother_name, patient_mother_phonenumber, patient_responsible_name, patient_responsible_phonenumber, patient_adress, patient_ethnicity, patient_color, patient_adressUF, patient_adressCEP, document_chart_number, patient_adress_city_IBGEcode, procedure_justification_description, prodedure_justification_main_cid10, prodedure_justification_sec_cid10, procedure_justification_associated_cause_cid10, procedure_justification_comments, establishment_exec_name, establishment_exec_cnes,prof_solicitor_document, prof_solicitor_name, solicitation_datetime, autorization_prof_name, emission_org_code, autorizaton_prof_document, autorizaton_datetime, signature_datetime, validity_period_start, validity_period_end, secondaries_procedures)

#Testing APAC
def test_with_data_in_function():
    assert type(data_to_use()) != type(Response())

def test_answer_with_all_fields():
    assert type(data_to_use()) != type(Response())

def test_awnser_with_only_required_data():
    assert type(pdf_apac.fill_pdf_apac(establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        patient_name='Patient Name',
        patient_cns=928976954930007,
        patient_sex='M',
        patient_birthday=datetime.datetime.now(),
        patient_adress_city='Patient Adress City',
        main_procedure_name='Main procedure Name',
        main_procedure_code='1234567890',
        main_procedure_quant=4
        ))

##############################################################
# ERRORS IN NAMES CAMPS
# establishment_solitc_name
# patient_name
# patient_mother_name
# patient_responsible_name
# establishment_exec_name
# prof_solicitor_name
# autorization_prof_name
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
    assert data_to_use(establishment_solitc_name=lenghtTest[:84]).status == Response(status=400).status

def test_short_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name='bro').status == Response(status=400).status

def test_wrongtype_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name=123124).status == Response(status=400).status

def test_empty_patient_name():    
    assert data_to_use(patient_name='').status == Response(status=400).status

def test_with_space_patient_name():    
    assert data_to_use(patient_name='  ').status == Response(status=400).status

def test_long_patient_name():    
    assert data_to_use(patient_name=lenghtTest[:70]).status == Response(status=400).status

def test_short_patient_name():    
    assert data_to_use(patient_name='bro').status == Response(status=400).status

def test_wrongtype_patient_name():    
    assert data_to_use(patient_name=123124).status == Response(status=400).status

def test_empty_patient_mother_name():    
    assert type(data_to_use(patient_mother_name='')) != type(Response())

def test_with_space_patient_mother_name():    
    assert type(data_to_use(patient_mother_name='  ')) != type(Response())

def test_long_patient_mother_name():    
    assert data_to_use(patient_mother_name=lenghtTest[:70]).status == Response(status=400).status

def test_short_patient_mother_name():    
    assert data_to_use(patient_mother_name='bro').status == Response(status=400).status

def test_wrongtype_patient_mother_name():    
    assert data_to_use(patient_mother_name=123124).status == Response(status=400).status

def test_empty_patient_responsible_name():    
    assert type(data_to_use(patient_responsible_name='')) != type(Response())

def test_with_space_patient_responsible_name():    
    assert type(data_to_use(patient_responsible_name='  ')) != type(Response())

def test_long_patient_responsible_name():    
    assert data_to_use(patient_responsible_name=lenghtTest[:70]).status == Response(status=400).status

def test_short_patient_responsible_name():    
    assert data_to_use(patient_responsible_name='bro').status == Response(status=400).status

def test_wrongtype_patient_responsible_name():    
    assert data_to_use(patient_responsible_name=123124).status == Response(status=400).status

def test_empty_establishment_exec_name():    
    assert type(data_to_use(establishment_exec_name='')) != type(Response())

def test_with_space_establishment_exec_name():    
    assert type(data_to_use(establishment_exec_name='  ')) != type(Response())

def test_long_establishment_exec_name():    
    assert data_to_use(establishment_exec_name=lenghtTest[:75]).status == Response(status=400).status

def test_short_establishment_exec_name():    
    assert data_to_use(establishment_exec_name='bro').status == Response(status=400).status

def test_wrongtype_establishment_exec_name():    
    assert data_to_use(establishment_exec_name=123124).status == Response(status=400).status

def test_empty_prof_solicitor_name():    
    assert type(data_to_use(prof_solicitor_name='')) != type(Response())

def test_with_space_prof_solicitor_name():    
    assert type(data_to_use(prof_solicitor_name='  ')) != type(Response())

def test_long_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=lenghtTest[:50]).status == Response(status=400).status

def test_short_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='bro').status == Response(status=400).status

def test_wrongtype_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=123124).status == Response(status=400).status

def test_empty_autorization_prof_name():    
    assert type(data_to_use(autorization_prof_name='')) != type(Response())

def test_with_space_autorization_prof_name():    
    assert type(data_to_use(autorization_prof_name='  ')) != type(Response())

def test_long_autorization_prof_name():    
    assert data_to_use(autorization_prof_name=lenghtTest[:50]).status == Response(status=400).status

def test_short_autorization_prof_name():    
    assert data_to_use(autorization_prof_name='bro').status == Response(status=400).status

def test_wrongtype_autorization_prof_name():    
    assert data_to_use(autorization_prof_name=123124).status == Response(status=400).status


####################################################################
# TEST CNES 
# establishment_solitc_cnes
# establishment_exec_cnes
# empty
# wrong type
# invalid cnes

def test_empty_establishment_solitc_cnes():
    assert data_to_use(establishment_solitc_cnes='').status == Response(status=400).status

def test_wrongtype_establishment_solitc_cnes():
    assert data_to_use(establishment_solitc_cnes='adsadad').status == Response(status=400).status

def test_invalidcnes_establishment_solitc_cnes():
    assert data_to_use(establishment_solitc_cnes=451236548).status == Response(status=400).status

def test_empty_establishment_exec_cnes():
    assert data_to_use(establishment_exec_cnes='').status == Response(status=400).status

def test_wrongtype_establishment_exec_cnes():
    assert data_to_use(establishment_exec_cnes='adsadad').status == Response(status=400).status

def test_invalidcnes_establishment_exec_cnes():
    assert data_to_use(establishment_exec_cnes=451236548).status == Response(status=400).status


#################################################################
# TEST DOCUMENTS CNS AND CPF
# patient_cns
# prof_solicitor_document
# autorizaton_prof_document
# wrong type
# invalid cns
# invalid cpf
# wrong option

def test_wrongtype_patient_cns():
    assert data_to_use(patient_cns='451236548').status == Response(status=400).status

def test_invalid_patient_cns():
    assert data_to_use(patient_cns=451236548554).status == Response(status=400).status

def test_wrongtype_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document='451236548554').status == Response(status=400).status

def test_invalidcns_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document={'CNS':284123312123}).status == Response(status=400).status

def test_invalidccpf_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document={'CPF':284123312123}).status == Response(status=400).status

def test_wrongoption_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document={'BBB':284123312123}).status == Response(status=400).status

def test_wrongtype_autorizaton_prof_document():
    assert data_to_use(autorizaton_prof_document='451236548554').status == Response(status=400).status

def test_invalidcns_autorizaton_prof_document():
    assert data_to_use(autorizaton_prof_document={'CNS':284123312123}).status == Response(status=400).status

def test_invalidccpf_autorizaton_prof_document():
    assert data_to_use(autorizaton_prof_document={'CPF':284123312123}).status == Response(status=400).status

def test_wrongoption_autorizaton_prof_document():
    assert data_to_use(autorizaton_prof_document={'BBB':284123312123}).status == Response(status=400).status




