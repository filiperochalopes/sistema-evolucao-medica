#from ..pdf_ficha_internamento import fill_pdf_ficha_internamento
from .. import pdf_ficha_internamento
import datetime
from flask import Response

global lenghtTest
lenghtTest = ''
for x in range(0, 2000):
    lenghtTest += str(x)


def data_to_use(documentDatetime=datetime.datetime.now(), patient_name="Patient Name",patient_cns=928976954930007,patient_birthday=datetime.datetime.now(),patient_sex='F',patient_motherName="Patient Mother Name",patient_document={'CPF':28445400070},patient_adress='pacient street, 43, paciten, USA',patient_phonenumber=44387694628, patient_drug_allergies='Penicillin, Aspirin, Ibuprofen, Anticonvulsants.', patient_comorbidities='Heart disease, High blood pressure, Diabetes, Cerebrovascular disease.',current_illness_history='Current illnes hsitoryaaaaaaaaaaa',initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',doctor_name='Doctor Name',doctor_cns=928976954930007,doctor_crm='CRM/UF 123456',patient_adressNumber=123456,patient_adressNeigh='Patient Neighborhood',patient_adressCity='Patient city',patient_adressUF='sp',patient_adressCEP=12345678,patient_nationality='Brasileira',patient_estimateWeight=123.32,has_additional_healthInsurance=False):
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
        patient_drug_allergies='Penicillin, Aspirin, Ibuprofen, Anticonvulsants.',
        patient_comorbidities='Heart disease, High blood pressure, Diabetes, Cerebrovascular disease.',
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
    assert data_to_use(doctor_name=str(lenghtTest[:52])).status == Response(status=400).status

def test_short_doctor_name():    
    assert data_to_use(doctor_name='11113').status == Response(status=400).status


#################################################################
#TEST DOCUMENTS RG AND CPF
# patient_document
# wrong type
# invalid rg
# valido rg
# invalid cpf
# valid cpf
# wrong option

def test_wrongtype_patient_document():
    assert data_to_use(patient_document='451236548554').status == Response(status=400).status

def test_invalidrg_patient_document():
    assert data_to_use(patient_document={'RG':28123}).status == Response(status=400).status

def test_validrg_patient_document():
    assert data_to_use(patient_document={'RG':928976954930007}) != type(Response())

def test_invalidccpf_patient_document():
    assert data_to_use(patient_document={'CPF':284123312123}).status == Response(status=400).status

def test_validcpf_patient_document():
    assert data_to_use(patient_document={'CPF':43423412399}) != type(Response())

def test_wrongoption_patient_document():
    assert data_to_use(patient_document={'BBB':284123312123}).status == Response(status=400).status

#################################################################
# TEST DATETIMES VARIABLES
# documentDatetime
# patient_birthday
# autorizaton_datetime
# test wrong type

def test_wrongtype_documentDatetime():
    assert data_to_use(documentDatetime='bahabah').status == Response(status=400).status

def test_valid_documentDatetime():
    assert type(data_to_use(documentDatetime=datetime.datetime.now())) != type(Response())


def test_wrongtype_patient_birthday():
    assert data_to_use(patient_birthday='bahabah').status == Response(status=400).status

def test_valid_patient_birthday():
    assert type(data_to_use(patient_birthday=datetime.datetime.now())) != type(Response())

##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# has_additional_healthInsurance
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

def test_wrongtype_has_additional_healthInsurance():
    assert data_to_use(has_additional_healthInsurance=1231).status == Response(status=400).status

def test_notexistopiton_has_additional_healthInsurance():
    assert data_to_use(has_additional_healthInsurance='23').status == Response(status=400).status

def test_True_option_has_additional_healthInsurance():
    assert type(data_to_use(has_additional_healthInsurance=True)) != type(Response())

def test_False_option_has_additional_healthInsurance():
    assert type(data_to_use(has_additional_healthInsurance=False)) != type(Response())

####################################################################
# TEST ADRESS VARIABLES
# patient_adress
# patient_adressNumber
# patient_adressNeigh
# patient_adressCity
# patient_adressUF 
# patient_adressCEP
# test wrong type
# test empty value
# test empty space value
# invalid value
# Long value

def test_wrongtype_patient_adress():
    assert data_to_use(patient_adress=1212312).status == Response(status=400).status

def test_empty_value_patient_adress():
    assert data_to_use(patient_adress='').status == Response(status=400).status

def test_empty_space_patient_adress():
    assert data_to_use(patient_adress='   ').status == Response(status=400).status

def test_invalid_value_patient_adress():
    assert data_to_use(patient_adress='111').status == Response(status=400).status

def test_long_value_patient_adress():
    assert data_to_use(patient_adress=str(lenghtTest[:65])).status == Response(status=400).status

def test_wrongtype_patient_adressNumber():
    assert data_to_use(patient_adressNumber='1212312').status == Response(status=400).status

def test_empty_value_patient_adressNumber():
    assert type(data_to_use(patient_adressNumber=None)) != type(Response())

def test_empty_space_patient_adressNumber():
    assert data_to_use(patient_adressNumber='   ').status == Response(status=400).status

def test_invalid_value_patient_adressNumber():
    assert data_to_use(patient_adressNumber='123').status == Response(status=400).status

def test_long_value_patient_adressNumber():
    assert data_to_use(patient_adressNumber=1234567).status == Response(status=400).status

def test_wrongtype_patient_adressNeigh():
    assert data_to_use(patient_adressNeigh=1212).status == Response(status=400).status

def test_empty_value_patient_adressNeigh():
    assert type(data_to_use(patient_adressNeigh=None)) != type(Response())

def test_empty_space_patient_adressNeigh():
    assert type(data_to_use(patient_adressNeigh='   ')) != type(Response())

def test_invalid_value_patient_adressNeigh():
    assert data_to_use(patient_adressNeigh='123').status == Response(status=400).status

def test_long_value_patient_adressNeigh():
    assert data_to_use(patient_adressNeigh=str(lenghtTest[:30])).status == Response(status=400).status

def test_wrongtype_patient_adressCity():
    assert data_to_use(patient_adressCity=1212).status == Response(status=400).status

def test_empty_value_patient_adressCity():
    assert type(data_to_use(patient_adressCity=None)) != type(Response())

def test_empty_space_patient_adressCity():
    assert type(data_to_use(patient_adressCity='   ')) != type(Response())

def test_invalid_value_patient_adressCity():
    assert data_to_use(patient_adressCity='123').status == Response(status=400).status

def test_long_value_patient_adressCity():
    assert data_to_use(patient_adressCity=str(lenghtTest[:34])).status == Response(status=400).status

def test_wrongtype_patient_adressCEP():
    assert data_to_use(patient_adressCEP='1212').status == Response(status=400).status

def test_empty_value_patient_adressCEP():
    assert type(data_to_use(patient_adressCEP=None)) != type(Response())

def test_empty_space_patient_adressCEP():
    assert data_to_use(patient_adressCEP='   ').status == Response(status=400).status

def test_invalid_value_patient_adressCEP():
    assert data_to_use(patient_adressCEP=1231).status == Response(status=400).status

def test_long_value_patient_adressCEP():
    assert data_to_use(patient_adressCEP=lenghtTest[:10]).status == Response(status=400).status

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


#############################################################################
# TEST BIG TEXT WITH LINE BRAKES
# current_illness_history
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

def test_wrong_type_current_illness_history():
    assert data_to_use(current_illness_history=131).status == Response(status=400).status

def test_empty_value_current_illness_history():
    assert data_to_use(current_illness_history='').status == Response(status=400).status

def test_empty_spaces_current_illness_history():
    assert data_to_use(current_illness_history='    ').status == Response(status=400).status

def test_shortText_current_illness_history():
    assert data_to_use(current_illness_history='ablas').status == Response(status=400).status

def test_more_than_limit_current_illness_history():
    assert data_to_use(current_illness_history=lenghtTest[:1690]).status == Response(status=400).status

#############################################################################
# NORMAL TEXT VARIABLES THAT CANNOT/can BE NULL
# patient_drug_allergies
# patient_comorbidities
# initial_diagnostic_suspicion
# doctor_crm 
# patient_nationality (can be null)
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

def test_wrong_type_patient_drug_allergies():
    assert data_to_use(patient_drug_allergies=131).status == Response(status=400).status

def test_empty_value_patient_drug_allergies():
    assert data_to_use(patient_drug_allergies='').status == Response(status=400).status

def test_empty_spaces_patient_drug_allergies():
    assert data_to_use(patient_drug_allergies='    ').status == Response(status=400).status

def test_shortText_patient_drug_allergies():
    assert data_to_use(patient_drug_allergies='abla').status == Response(status=400).status

def test_more_than_limit_patient_drug_allergies():
    assert data_to_use(patient_drug_allergies=lenghtTest[:110]).status == Response(status=400).status

def test_wrong_type_patient_comorbidities():
    assert data_to_use(patient_comorbidities=131).status == Response(status=400).status

def test_empty_value_patient_comorbidities():
    assert data_to_use(patient_comorbidities='').status == Response(status=400).status

def test_empty_spaces_patient_comorbidities():
    assert data_to_use(patient_comorbidities='    ').status == Response(status=400).status

def test_shortText_patient_comorbidities():
    assert data_to_use(patient_comorbidities='abla').status == Response(status=400).status

def test_more_than_limit_patient_comorbidities():
    assert data_to_use(patient_comorbidities=lenghtTest[:110]).status == Response(status=400).status

def test_wrong_type_initial_diagnostic_suspicion():
    assert data_to_use(initial_diagnostic_suspicion=131).status == Response(status=400).status

def test_empty_value_initial_diagnostic_suspicion():
    assert data_to_use(initial_diagnostic_suspicion='').status == Response(status=400).status

def test_empty_spaces_initial_diagnostic_suspicion():
    assert data_to_use(initial_diagnostic_suspicion='    ').status == Response(status=400).status

def test_shortText_initial_diagnostic_suspicion():
    assert data_to_use(initial_diagnostic_suspicion='abla').status == Response(status=400).status

def test_more_than_limit_initial_diagnostic_suspicion():
    assert data_to_use(initial_diagnostic_suspicion=lenghtTest[:110]).status == Response(status=400).status

def test_wrong_type_doctor_crm():
    assert data_to_use(doctor_crm=131).status == Response(status=400).status

def test_empty_value_doctor_crm():
    assert data_to_use(doctor_crm='').status == Response(status=400).status

def test_empty_spaces_doctor_crm():
    assert data_to_use(doctor_crm='    ').status == Response(status=400).status

def test_shortText_doctor_crm():
    assert data_to_use(doctor_crm='abla').status == Response(status=400).status

def test_more_than_limit_doctor_crm():
    assert data_to_use(doctor_crm=lenghtTest[:14]).status == Response(status=400).status

def test_wrong_type_patient_nationality():
    assert data_to_use(patient_nationality=131).status == Response(status=400).status

def test_empty_value_patient_nationality():
    assert type(data_to_use(patient_nationality='')) != type(Response())

def test_empty_spaces_patient_nationality():
    assert type(data_to_use(patient_nationality='    ')) != type(Response())

def test_shortText_patient_nationality():
    assert type(data_to_use(patient_nationality='abla123')) != type(Response())

def test_more_than_limit_patient_nationality():
    assert data_to_use(patient_nationality=lenghtTest[:25]).status == Response(status=400).status

#################################################################################
# TEST CNS
# patient_cns
# doctor_cns
# wrong type
# valid
# invalid
# empty send

def test_wrongtype_patient_cns():
    assert data_to_use(patient_cns='13123').status == Response(status=400).status

def test_valid_patient_cns():
    assert type(data_to_use(patient_cns=928976954930007)) != type(Response())

def test_invalid_patient_cns():
    assert data_to_use(patient_cns=928976546250007).status == Response(status=400).status

def test_empty_patient_cns():
    assert data_to_use(patient_cns=None).status == Response(status=400).status

def test_wrongtype_doctor_cns():
    assert data_to_use(doctor_cns='13123').status == Response(status=400).status

def test_valid_doctor_cns():
    assert type(data_to_use(doctor_cns=928976954930007)) != type(Response())

def test_invalid_doctor_cns():
    assert data_to_use(doctor_cns=928976546250007).status == Response(status=400).status

def test_empty_doctor_cns():
    assert data_to_use(doctor_cns=None).status == Response(status=400).status


#################################################################################
# TEST NUMBER VARIABLES CAN/CANNOT BE NULL
# patient_phonenumber
# patient_estimateWeight
# !!!!! TESTING
# wrong type
# test empty value
# test empty space
# short value
# long value  

def test_wrong_type_patient_phonenumber():
    assert data_to_use(patient_phonenumber='131').status == Response(status=400).status

def test_empty_value_patient_phonenumber():
    assert data_to_use(patient_phonenumber=None).status == Response(status=400).status

def test_empty_spaces_patient_phonenumber():
    assert data_to_use(patient_phonenumber='    ').status == Response(status=400).status

def test_longValue_patient_phonenumber():
    assert data_to_use(patient_phonenumber=int(lenghtTest[:14])).status == Response(status=400).status

def test_shortValue_patient_phonenumber():
    assert data_to_use(patient_phonenumber=1234567).status == Response(status=400).status

def test_wrong_type_patient_estimateWeight():
    assert data_to_use(patient_estimateWeight='131').status == Response(status=400).status

def test_empty_value_patient_estimateWeight():
    assert type(data_to_use(patient_estimateWeight=None)) != type(Response())

def test_empty_spaces_patient_estimateWeight():
    assert data_to_use(patient_estimateWeight='    ').status == Response(status=400).status

def test_longValue_patient_estimateWeight():
    assert data_to_use(patient_estimateWeight=float(lenghtTest[:8])).status == Response(status=400).status

def test_shortValue_patient_estimateWeight():
    assert type(data_to_use(patient_estimateWeight=123)) != type(Response())


































