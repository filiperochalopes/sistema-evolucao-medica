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


#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_datetime
# autorizaton_datetime
# signature_datetime,
# test wrong type
# test valid datetime

def test_wrongtype_patient_birthday():
    assert data_to_use(patient_birthday='bahabah').status == Response(status=400).status

def test_valid_patient_birthday():
    assert type(data_to_use(patient_birthday=datetime.datetime.now())) != type(Response())

def test_wrongtype_solicitation_datetime():
    assert data_to_use(solicitation_datetime='bahabah').status == Response(status=400).status

def test_valid_solicitation_datetime():
    assert type(data_to_use(solicitation_datetime=datetime.datetime.now())) != type(Response())

def test_wrongtype_autorizaton_datetime():
    assert data_to_use(autorizaton_datetime='bahabah').status == Response(status=400).status

def test_valid_autorizaton_datetime():
    assert type(data_to_use(autorizaton_datetime=datetime.datetime.now())) != type(Response())

def test_wrongtype_signature_datetime():
    assert data_to_use(signature_datetime='bahabah').status == Response(status=400).status

def test_valid_signature_datetime():
    assert type(data_to_use(signature_datetime=datetime.datetime.now())) != type(Response())

##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# patient_adressUF
# test wrong type
# test not exist option
# test all options in Upper Case
# test all options in lower Case

def test_wrongtype_patient_sex():
    assert data_to_use(patient_sex=1231).status == Response(status=400).status

def test_notexistopiton_patient_sex():
    assert data_to_use(patient_sex='G').status == Response(status=400).status

def test_M_optionUpper_patient_sex():
    assert type(data_to_use(patient_sex='M')) != type(Response())

def test_M_optionLower_patient_sex():
    assert type(data_to_use(patient_sex='m')) != type(Response())

def test_F_optionUpper_patient_sex():
    assert type(data_to_use(patient_sex='F')) != type(Response())

def test_F_optionLower_patient_sex():
    assert type(data_to_use(patient_sex='f')) != type(Response())

def test_wrongtype_patient_adressUF():
    assert data_to_use(patient_adressUF=1231).status == Response(status=400).status

def test_notexistopiton_patient_adressUF():
    assert data_to_use(patient_adressUF='AUYD').status == Response(status=400).status

def test_AC_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='AC')) != type(Response())

def test_AC_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ac')) != type(Response())

def test_AL_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='AL')) != type(Response())

def test_AL_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='al')) != type(Response())

def test_AP_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='AP')) != type(Response())

def test_AP_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ap')) != type(Response())

def test_AM_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='AM')) != type(Response())

def test_AM_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='am')) != type(Response())

def test_BA_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='BA')) != type(Response())

def test_BA_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ba')) != type(Response())

def test_CE_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='CE')) != type(Response())

def test_CE_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ce')) != type(Response())

def test_DF_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='DF')) != type(Response())

def test_DF_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='df')) != type(Response())

def test_ES_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ES')) != type(Response())

def test_ES_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='es')) != type(Response())

def test_GO_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='GO')) != type(Response())

def test_GO_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='go')) != type(Response())

def test_MA_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='MA')) != type(Response())

def test_MA_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ma')) != type(Response())

def test_MS_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='MS')) != type(Response())

def test_MS_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ms')) != type(Response())

def test_MT_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='MT')) != type(Response())

def test_MT_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='mt')) != type(Response())

def test_MG_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='MG')) != type(Response())

def test_MG_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='mg')) != type(Response())

def test_PA_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='PA')) != type(Response())

def test_PA_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='pa')) != type(Response())

def test_PB_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='PB')) != type(Response())

def test_PB_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='pb')) != type(Response())

def test_PR_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='PR')) != type(Response())

def test_PR_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='pr')) != type(Response())

def test_PE_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='PE')) != type(Response())

def test_PE_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='pe')) != type(Response())

def test_PI_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='PI')) != type(Response())

def test_PI_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='pi')) != type(Response())

def test_RJ_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='RJ')) != type(Response())

def test_RJ_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='rj')) != type(Response())

def test_RN_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='RN')) != type(Response())

def test_RN_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='rn')) != type(Response())

def test_RS_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='RS')) != type(Response())

def test_RS_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='rs')) != type(Response())

def test_RO_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='RO')) != type(Response())

def test_RO_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ro')) != type(Response())

def test_RR_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='RR')) != type(Response())

def test_RR_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='rr')) != type(Response())

def test_SC_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='SC')) != type(Response())

def test_SC_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='sc')) != type(Response())

def test_SP_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='SP')) != type(Response())

def test_SP_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='sp')) != type(Response())

def test_SE_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='SE')) != type(Response())

def test_SE_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='se')) != type(Response())

def test_TO_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='TO')) != type(Response())

def test_TO_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='to')) != type(Response())


####################################################################
# TEST ADRESS VARIABLES
# patient_adress
# patient_adress_city
# patient_adress_city_IBGEcode
# patient_adressUF (already tested in option tests)
# patient_adressCEP
# test wrong type
# test empty value
# test empty space value
# invalid value
# Long value

def test_wrongtype_patient_adress():
    assert data_to_use(patient_adress=1212312).status == Response(status=400).status

def test_empty_value_patient_adress():
    assert type(data_to_use(patient_adress='')) != type(Response())

def test_empty_space_patient_adress():
    assert type(data_to_use(patient_adress='  ')) != type(Response())

def test_invalid_value_patient_adress():
    assert data_to_use(patient_adress='111').status == Response(status=400).status

def test_long_value_patient_adress():
    assert data_to_use(patient_adress=lenghtTest[:100]).status == Response(status=400).status

def test_wrongtype_patient_adress_city():
    assert data_to_use(patient_adress_city=1212312).status == Response(status=400).status

def test_empty_value_patient_adress_city():
    assert data_to_use(patient_adress_city='').status == Response(status=400).status

def test_empty_space_patient_adress_city():
    assert data_to_use(patient_adress_city='  ').status == Response(status=400).status

def test_invalid_value_patient_adress_city():
    assert data_to_use(patient_adress_city='111').status == Response(status=400).status

def test_long_value_patient_adress_city():
    assert data_to_use(patient_adress_city=lenghtTest[:60]).status == Response(status=400).status

def test_wrongtype_patient_adress_city_IBGEcode():
    assert data_to_use(patient_adress_city_IBGEcode='1212312').status == Response(status=400).status

def test_empty_value_patient_adress_city_IBGEcode():
    assert data_to_use(patient_adress_city_IBGEcode='').status == Response(status=400).status

def test_empty_space_patient_adress_city_IBGEcode():
    assert data_to_use(patient_adress_city_IBGEcode='  ').status == Response(status=400).status

def test_invalid_value_patient_adress_city_IBGEcode():
    assert data_to_use(patient_adress_city_IBGEcode=2411).status == Response(status=400).status

def test_long_value_patient_adress_city_IBGEcode():
    assert data_to_use(patient_adress_city_IBGEcode=52352352352352352352352352352).status == Response(status=400).status

def test_wrongtype_patient_adressCEP():
    assert data_to_use(patient_adressCEP='1212312').status == Response(status=400).status

def test_empty_value_patient_adressCEP():
    assert data_to_use(patient_adressCEP='').status == Response(status=400).status

def test_empty_space_patient_adressCEP():
    assert data_to_use(patient_adressCEP='  ').status == Response(status=400).status

def test_invalid_value_patient_adressCEP():
    assert data_to_use(patient_adressCEP=2411).status == Response(status=400).status

def test_long_value_patient_adressCEP():
    assert data_to_use(patient_adressCEP=52352352352352352352352352352).status == Response(status=400).status


























