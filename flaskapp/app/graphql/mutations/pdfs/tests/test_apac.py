from pdfs import pdf_apac
import datetime
from flask import Response

global lenght_test
lenght_test = ''
for x in range(0, 1100):
    lenght_test += str(x)

def data_to_use(establishment_solitc_name='Establishment Solicit Name',establishment_solitc_cnes=1234567,patient_name='Patient Name',patient_cns=928976954930007,patient_sex='M',patient_birthday=datetime.datetime.now(), patient_adress_city='Patient Adress City',main_procedure_name='Main procedure Name',main_procedure_code='1234567890',main_procedure_quant=4,patient_mother_name='Patient Mother Name',       patient_mother_phonenumber=5286758957, patient_responsible_name='Patient Responsible Name', patient_responsible_phonenumber=5465981345, patient_adress='Patient Adress',patient_color='Branca',patient_ethnicity='Indigena',patient_adressUF='BA',patient_adressCEP=86425910, document_chart_number=12345,patient_adress_city_IBGEcode=4528765,procedure_justification_description='Procedure Justification Description', prodedure_justification_main_cid10='A98', prodedure_justification_sec_cid10='A01', procedure_justification_associated_cause_cid10='A45',procedure_justification_comments='Procedure Justification Comments',establishment_exec_name='Establishment Exec Name', establishment_exec_cnes=7654321,prof_solicitor_document={'CPF':28445400070}, prof_solicitor_name='Profissional Solicit Name',solicitation_datetime=datetime.datetime.now(),signature_datetime=datetime.datetime.now(),validity_period_start=datetime.datetime.now(),validity_period_end=datetime.datetime.now(),autorization_prof_name='Autorization Professional Name', emission_org_code='Cod121234',autorizaton_prof_document={'CPF':28445400070}, autorizaton_datetime=datetime.datetime.now(),secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]):
    return pdf_apac.fill_pdf_apac(establishment_solitc_name, establishment_solitc_cnes, patient_name, patient_cns, patient_sex, patient_birthday, patient_adress_city, main_procedure_name, main_procedure_code, main_procedure_quant, patient_mother_name, patient_mother_phonenumber, patient_responsible_name, patient_responsible_phonenumber, patient_adress, patient_ethnicity, patient_color, patient_adressUF, patient_adressCEP, document_chart_number, patient_adress_city_IBGEcode, procedure_justification_description, prodedure_justification_main_cid10, prodedure_justification_sec_cid10, procedure_justification_associated_cause_cid10, procedure_justification_comments, establishment_exec_name, establishment_exec_cnes,prof_solicitor_document, prof_solicitor_name, solicitation_datetime, autorization_prof_name, emission_org_code, autorizaton_prof_document, autorizaton_datetime, signature_datetime, validity_period_start, validity_period_end, secondaries_procedures)

#Testing APAC
def test_with_data_in_function():
    assert type(data_to_use()) != type(Response())

def test_answer_with_all_fields():
    assert type(data_to_use()) != type(Response())

def test_awnser_with_only_required_data():
    assert type(pdf_apac.fill_pdf_apac(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        patient_name='Patient Name',
        patient_cns=928976954930007,
        patient_sex='M',
        patient_birthday=datetime.datetime.now(),
        patient_adress_city='Patient Adress City',
        main_procedure_name='Main procedure Name',
        main_procedure_code='1234567890',
        main_procedure_quant=4
        )) != type(Response())

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
    assert data_to_use(establishment_solitc_name=lenght_test[:84]).status == Response(status=400).status

def test_short_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name='bro').status == Response(status=400).status

def test_wrongtype_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name=123124).status == Response(status=400).status

def test_empty_patient_name():    
    assert data_to_use(patient_name='').status == Response(status=400).status

def test_with_space_patient_name():    
    assert data_to_use(patient_name='  ').status == Response(status=400).status

def test_long_patient_name():    
    assert data_to_use(patient_name=lenght_test[:70]).status == Response(status=400).status

def test_short_patient_name():    
    assert data_to_use(patient_name='bro').status == Response(status=400).status

def test_wrongtype_patient_name():    
    assert data_to_use(patient_name=123124).status == Response(status=400).status

def test_empty_patient_mother_name():    
    assert type(data_to_use(patient_mother_name='')) != type(Response())

def test_with_space_patient_mother_name():    
    assert type(data_to_use(patient_mother_name='  ')) != type(Response())

def test_long_patient_mother_name():    
    assert data_to_use(patient_mother_name=lenght_test[:70]).status == Response(status=400).status

def test_short_patient_mother_name():    
    assert data_to_use(patient_mother_name='bro').status == Response(status=400).status

def test_wrongtype_patient_mother_name():    
    assert data_to_use(patient_mother_name=123124).status == Response(status=400).status

def test_empty_patient_responsible_name():    
    assert type(data_to_use(patient_responsible_name='')) != type(Response())

def test_with_space_patient_responsible_name():    
    assert type(data_to_use(patient_responsible_name='  ')) != type(Response())

def test_long_patient_responsible_name():    
    assert data_to_use(patient_responsible_name=lenght_test[:70]).status == Response(status=400).status

def test_short_patient_responsible_name():    
    assert data_to_use(patient_responsible_name='bro').status == Response(status=400).status

def test_wrongtype_patient_responsible_name():    
    assert data_to_use(patient_responsible_name=123124).status == Response(status=400).status

def test_empty_establishment_exec_name():    
    assert type(data_to_use(establishment_exec_name='')) != type(Response())

def test_with_space_establishment_exec_name():    
    assert type(data_to_use(establishment_exec_name='  ')) != type(Response())

def test_long_establishment_exec_name():    
    assert data_to_use(establishment_exec_name=lenght_test[:75]).status == Response(status=400).status

def test_short_establishment_exec_name():    
    assert data_to_use(establishment_exec_name='bro').status == Response(status=400).status

def test_wrongtype_establishment_exec_name():    
    assert data_to_use(establishment_exec_name=123124).status == Response(status=400).status

def test_empty_prof_solicitor_name():    
    assert type(data_to_use(prof_solicitor_name='')) != type(Response())

def test_with_space_prof_solicitor_name():    
    assert type(data_to_use(prof_solicitor_name='  ')) != type(Response())

def test_long_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=lenght_test[:50]).status == Response(status=400).status

def test_short_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='bro').status == Response(status=400).status

def test_wrongtype_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=123124).status == Response(status=400).status

def test_empty_autorization_prof_name():    
    assert type(data_to_use(autorization_prof_name='')) != type(Response())

def test_with_space_autorization_prof_name():    
    assert type(data_to_use(autorization_prof_name='  ')) != type(Response())

def test_long_autorization_prof_name():    
    assert data_to_use(autorization_prof_name=lenght_test[:50]).status == Response(status=400).status

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
# signature_datetime
# validity_period_end 
# validity_period_start
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

def test_wrongtype_validity_period_start():
    assert data_to_use(validity_period_start='bahabah').status == Response(status=400).status

def test_valid_validity_period_start():
    assert type(data_to_use(validity_period_start=datetime.datetime.now())) != type(Response())

def test_wrongtype_validity_period_end ():
    assert data_to_use(validity_period_end ='bahabah').status == Response(status=400).status

def test_valid_validity_period_end ():
    assert type(data_to_use(validity_period_end =datetime.datetime.now())) != type(Response())




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
    assert data_to_use(patient_adress=lenght_test[:100]).status == Response(status=400).status

def test_wrongtype_patient_adress_city():
    assert data_to_use(patient_adress_city=1212312).status == Response(status=400).status

def test_empty_value_patient_adress_city():
    assert data_to_use(patient_adress_city='').status == Response(status=400).status

def test_empty_space_patient_adress_city():
    assert data_to_use(patient_adress_city='  ').status == Response(status=400).status

def test_invalid_value_patient_adress_city():
    assert data_to_use(patient_adress_city='111').status == Response(status=400).status

def test_long_value_patient_adress_city():
    assert data_to_use(patient_adress_city=lenght_test[:60]).status == Response(status=400).status

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


#############################################################################
# TEST BIG TEXT WITH LINE BRAKES
# procedure_justification_comments
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

def test_wrong_type_procedure_justification_comments():
    assert data_to_use(procedure_justification_comments=131).status == Response(status=400).status

def test_empty_value_procedure_justification_comments():
    assert type(data_to_use(procedure_justification_comments='')) != type(Response())

def test_empty_spaces_procedure_justification_comments():
    assert type(data_to_use(procedure_justification_comments='    ')) != type(Response())

def test_shortText_procedure_justification_comments():
    assert data_to_use(procedure_justification_comments='abla').status == Response(status=400).status

def test_more_than_limit_procedure_justification_comments():
    assert data_to_use(procedure_justification_comments=lenght_test[:800]).status == Response(status=400).status

#############################################################################
# NORMAL TEXT VARIABLES THAT CANNOT BE NULL
# main_procedure_name
# main_procedure_code
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

def test_wrong_type_main_procedure_name():
    assert data_to_use(main_procedure_name=131).status == Response(status=400).status

def test_empty_value_main_procedure_name():
    assert data_to_use(main_procedure_name='').status == Response(status=400).status

def test_empty_spaces_main_procedure_name():
    assert data_to_use(main_procedure_name='    ').status == Response(status=400).status

def test_shortText_main_procedure_name():
    assert data_to_use(main_procedure_name='abla').status == Response(status=400).status

def test_more_than_limit_main_procedure_name():
    assert data_to_use(main_procedure_name=lenght_test[:55]).status == Response(status=400).status

def test_wrong_type_main_procedure_code():
    assert data_to_use(main_procedure_code=131).status == Response(status=400).status

def test_empty_value_main_procedure_code():
    assert data_to_use(main_procedure_code='').status == Response(status=400).status

def test_empty_spaces_main_procedure_code():
    assert data_to_use(main_procedure_code='    ').status == Response(status=400).status

def test_shortText_main_procedure_code():
    assert data_to_use(main_procedure_code='abla').status == Response(status=400).status

def test_more_than_limit_main_procedure_code():
    assert data_to_use(main_procedure_code=lenght_test[:11]).status == Response(status=400).status



#################################################################################
# TEST INT VARIABLES CAN/CANNOT BE NULL
# main_procedure_quant
# patient_mother_phonenumber
# patient_responsible_phonenumber
# document_chart_number
# !!!!! TESTING
# wrong type
# test empty value
# test empty space
# short value
# long value  

def test_wrong_type_main_procedure_quant():
    assert data_to_use(main_procedure_quant='131').status == Response(status=400).status

def test_empty_value_main_procedure_quant():
    assert data_to_use(main_procedure_quant='').status == Response(status=400).status

def test_empty_spaces_main_procedure_quant():
    assert data_to_use(main_procedure_quant='    ').status == Response(status=400).status

def test_longValue_main_procedure_quant():
    assert data_to_use(main_procedure_quant=int(lenght_test[:10])).status == Response(status=400).status

def test_wrong_type_patient_mother_phonenumber():
    assert data_to_use(patient_mother_phonenumber='131').status == Response(status=400).status

def test_empty_value_patient_mother_phonenumber():
    assert data_to_use(patient_mother_phonenumber='').status == Response(status=400).status

def test_empty_spaces_patient_mother_phonenumber():
    assert data_to_use(patient_mother_phonenumber='    ').status == Response(status=400).status

def test_longValue_patient_mother_phonenumber():
    assert data_to_use(patient_mother_phonenumber=int(lenght_test[:14])).status == Response(status=400).status

def test_wrong_type_patient_responsible_phonenumber():
    assert data_to_use(patient_responsible_phonenumber='131').status == Response(status=400).status

def test_empty_value_patient_responsible_phonenumber():
    assert data_to_use(patient_responsible_phonenumber='').status == Response(status=400).status

def test_empty_spaces_patient_responsible_phonenumber():
    assert data_to_use(patient_responsible_phonenumber='    ').status == Response(status=400).status

def test_longValue_patient_responsible_phonenumber():
    assert data_to_use(patient_responsible_phonenumber=int(lenght_test[:14])).status == Response(status=400).status

def test_wrong_type_document_chart_number():
    assert data_to_use(document_chart_number='131').status == Response(status=400).status

def test_empty_value_document_chart_number():
    assert data_to_use(document_chart_number='').status == Response(status=400).status

def test_empty_spaces_document_chart_number():
    assert data_to_use(document_chart_number='    ').status == Response(status=400).status

def test_longValue_document_chart_number():
    assert data_to_use(document_chart_number=int(lenght_test[:16])).status == Response(status=400).status



##############################################################################
# TEST STRING THAT CAN BE NULL
# patient_ethnicity
# patient_color
# prodedure_justification_main_cid10
# prodedure_justification_sec_cid10
# procedure_justification_associated_cause_cid10
# emission_org_code
# test wront type
# test empty value
# test empty spaces
# test long values
# test short values

def test_wrong_type_patient_ethnicity():
    assert data_to_use(patient_ethnicity=123).status == Response(status=400).status

def test_empty_value_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=None)) != type(Response())

def test_empty_spaces_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity='    ')) != type(Response())

def test_longValue_patient_ethnicity():
    assert data_to_use(patient_ethnicity=lenght_test[:20]).status == Response(status=400).status

def test_shortValue_patient_ethnicity():
    assert data_to_use(patient_ethnicity='aaa').status == Response(status=400).status

def test_wrong_type_patient_color():
    assert data_to_use(patient_color=123).status == Response(status=400).status

def test_empty_value_patient_color():
    assert type(data_to_use(patient_color=None)) != type(Response())

def test_empty_spaces_patient_color():
    assert type(data_to_use(patient_color='    ')) != type(Response())

def test_longValue_patient_color():
    assert data_to_use(patient_color=lenght_test[:15]).status == Response(status=400).status

def test_shortValue_patient_color():
    assert data_to_use(patient_color='aaa').status == Response(status=400).status

def test_wrong_type_prodedure_justification_main_cid10():
    assert data_to_use(prodedure_justification_main_cid10=123).status == Response(status=400).status

def test_empty_value_prodedure_justification_main_cid10():
    assert type(data_to_use(prodedure_justification_main_cid10=None)) != type(Response())

def test_empty_spaces_prodedure_justification_main_cid10():
    assert type(data_to_use(prodedure_justification_main_cid10='    ')) != type(Response())

def test_longValue_prodedure_justification_main_cid10():
    assert data_to_use(prodedure_justification_main_cid10=lenght_test[:6]).status == Response(status=400).status

def test_shortValue_prodedure_justification_main_cid10():
    assert data_to_use(prodedure_justification_main_cid10='aa').status == Response(status=400).status

def test_wrong_type_prodedure_justification_sec_cid10():
    assert data_to_use(prodedure_justification_sec_cid10=123).status == Response(status=400).status

def test_empty_value_prodedure_justification_sec_cid10():
    assert type(data_to_use(prodedure_justification_sec_cid10=None)) != type(Response())

def test_empty_spaces_prodedure_justification_sec_cid10():
    assert type(data_to_use(prodedure_justification_sec_cid10='    ')) != type(Response())

def test_longValue_prodedure_justification_sec_cid10():
    assert data_to_use(prodedure_justification_sec_cid10=lenght_test[:6]).status == Response(status=400).status

def test_shortValue_prodedure_justification_sec_cid10():
    assert data_to_use(prodedure_justification_sec_cid10='aa').status == Response(status=400).status

def test_wrong_type_procedure_justification_associated_cause_cid10():
    assert data_to_use(procedure_justification_associated_cause_cid10 =123).status == Response(status=400).status

def test_empty_value_procedure_justification_associated_cause_cid10():
    assert type(data_to_use(procedure_justification_associated_cause_cid10 =None)) != type(Response())

def test_empty_spaces_procedure_justification_associated_cause_cid10():
    assert type(data_to_use(procedure_justification_associated_cause_cid10 ='    ')) != type(Response())

def test_longValue_procedure_justification_associated_cause_cid10():
    assert data_to_use(procedure_justification_associated_cause_cid10 =lenght_test[:6]).status == Response(status=400).status

def test_shortValue_procedure_justification_associated_cause_cid10():
    assert data_to_use(procedure_justification_associated_cause_cid10 ='aa').status == Response(status=400).status

def test_wrong_type_emission_org_code():
    assert data_to_use(emission_org_code =123).status == Response(status=400).status

def test_empty_value_emission_org_code():
    assert type(data_to_use(emission_org_code =None)) != type(Response())

def test_empty_spaces_emission_org_code():
    assert type(data_to_use(emission_org_code ='    ')) != type(Response())

def test_longValue_emission_org_code():
    assert data_to_use(emission_org_code =lenght_test[:20]).status == Response(status=400).status

def test_shortValue_emission_org_code():
    assert data_to_use(emission_org_code ='a').status == Response(status=400).status

# TEST secondaries_procedures
# test wront type
# test wront type procedure_code
# test wront type procedure_name
# test wront type quant
# test empty value in keys
# test empty spaces in keys
# test empty value in procedure_code
# test empty value in procedure_name
# test empty value in quant
# test empty spaces in procedure_code
# test empty spaces in procedure_name
# test empty spaces in quant
# test more than limit dicts
# test long values in procedure_code
# test long values in procedure_name
# test long values in quant
# test short values in procedure_code
# test short values in procedure_name
# test short values in quant


def test_wrong_type_secondaries_procedures():
    assert data_to_use(secondaries_procedures=123).status == Response(status=400).status

def test_wrong_type_secondaries_procedures():
    assert data_to_use(secondaries_procedures=123).status == Response(status=400).status

def test_wrong_type_procedure_name_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":1313, "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_wrong_type_procedure_code_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":58, "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_wrong_type_quant_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":58, "quant":'5'}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status


def test_empty_value_keys_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"":"Procedure Name", "procedure_code":"cod4521578", "quant":5}, {"":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_empty_spaces_keys_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{" ":"Procedure Name", "procedure_code":"cod4521578", "quant":5}, {"  ":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_empty_value_procedure_code_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":"", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_empty_value_procedure_name_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"", "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_empty_value_quant_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"", "procedure_code":"cod4521578", "quant":""}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_empty_spaces_quant_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"", "procedure_code":"cod4521578", "quant":"  "}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_empty_spaces_procedure_name_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"  ", "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_empty_spaces_procedure_code_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":" ", "quant":1}]).status == Response(status=400).status

def test_more_than_limit_dict_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1},{"procedure_name":"Procedure Name", "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}, {"procedure_name":"Procedure Name", "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_long_values_procedure_code_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":lenght_test[:13], "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_long_values_procedure_name_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":lenght_test[:60], "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_long_values_quant_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":"cod4521578", "quant":int(lenght_test[:10])}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_short_values_quant_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":"cod4521578", "quant":0}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_short_values_procedure_name_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"Name", "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status

def test_short_values_procedure_code_secondaries_procedures():
    assert data_to_use(secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":"123as", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]).status == Response(status=400).status








