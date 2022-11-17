from app.graphql.mutations.pdfs import pdf_ficha_internamento
import datetime
from flask import Response

global lenght_test
lenght_test = ''
for x in range(0, 2000):
    lenght_test += str(x)

datetime_to_use = datetime.datetime.now()

def data_to_use(document_datetime=datetime_to_use, patient_name="Patient Name",patient_cns=928976954930007,patient_birthday=datetime_to_use,patient_sex='F',patient_mother_name="Patient Mother Name",patient_document={'CPF':28445400070},patient_adress='pacient street, 43, paciten, USA',patient_phonenumber=44387694628, patient_drug_allergies='Penicillin, Aspirin, Ibuprofen, Anticonvulsants.', patient_comorbidities='Heart disease, High blood pressure, Diabetes, Cerebrovascular disease.',current_illness_history='Current illnes hsitoryaaaaaaaaaaa',initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral',doctor_name='Doctor Name',doctor_cns=928976954930007,doctor_crm='CRM/UF 123456',patient_adress_number=123456,patient_adress_neigh='Patient Neighborhood',patient_adress_city='Patient city',patient_adress_uf='sp',patient_adress_cep=12345678,patient_nationality='Brasileira',patient_estimate_weight=123,has_additional_health_insurance=False):
    return pdf_ficha_internamento.fill_pdf_ficha_internamento(document_datetime,patient_name, patient_cns, patient_birthday, patient_sex,  patient_mother_name, patient_document, patient_adress, patient_phonenumber, patient_drug_allergies, patient_comorbidities, current_illness_history,initial_diagnostic_suspicion, doctor_name, doctor_cns, doctor_crm,patient_adress_number, patient_adress_neigh, patient_adress_city, patient_adress_uf, patient_adress_cep, patient_nationality, patient_estimate_weight, has_additional_health_insurance)


#Testing Ficha Internamento
def test_answer_with_all_fields():
    """Test fill ficha internamento with all data correct"""
    assert data_to_use() != type(Response())


def test_awnser_with_only_required_data():
    assert type(pdf_ficha_internamento.fill_pdf_ficha_internamento(
        document_datetime=datetime_to_use, 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime_to_use,
        patient_sex='F',
        patient_mother_name="Patient Mother Name",
        patient_document={'CPF':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_drug_allergies='Penicillin, Aspirin, Ibuprofen, Anticonvulsants.',
        patient_comorbidities='Heart disease, High blood pressure, Diabetes, Cerebrovascular disease.',
        current_illness_history='Current illnes hsitoryaaaaaaaaaaa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456'
        )) != type(Response())

##############################################################
# ERRORS IN NAMES CAMPS
# patient_name
# patient_mother_name
# doctor_name
# !!!!!!! TESTING !!!!!!!
# Name empty
# Name with space
# long name
# short name
# wrong name type



def test_wrongtype_patient_mother_name():    
    assert data_to_use(patient_mother_name=123124).status == Response(status=400).status

def test_empty_patient_mother_name():    
    assert data_to_use(patient_mother_name='').status == Response(status=400).status

def test_with_space_patient_mother_name():    
    assert data_to_use(patient_mother_name='  ').status == Response(status=400).status

def test_long_patient_mother_name():    
    assert data_to_use(patient_mother_name=str(lenght_test[:71])).status == Response(status=400).status

def test_short_patient_mother_name():    
    assert data_to_use(patient_mother_name='11113').status == Response(status=400).status

def test_wrongtype_doctor_name():    
    assert data_to_use(doctor_name=123124).status == Response(status=400).status

def test_empty_doctor_name():    
    assert data_to_use(doctor_name='').status == Response(status=400).status

def test_with_space_doctor_name():    
    assert data_to_use(doctor_name='  ').status == Response(status=400).status

def test_long_doctor_name():    
    assert data_to_use(doctor_name=str(lenght_test[:52])).status == Response(status=400).status

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
    assert data_to_use(document_datetime='bahabah').status == Response(status=400).status

def test_valid_documentDatetime():
    assert type(data_to_use(document_datetime=datetime_to_use)) != type(Response())


def test_wrongtype_patient_birthday():
    assert data_to_use(patient_birthday='bahabah').status == Response(status=400).status

def test_valid_patient_birthday():
    assert type(data_to_use(patient_birthday=datetime_to_use)) != type(Response())

##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# has_additional_health_insurance
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

def test_wrongtype_has_additional_health_insurance():
    assert data_to_use(has_additional_health_insurance=1231).status == Response(status=400).status

def test_notexistopiton_has_additional_health_insurance():
    assert data_to_use(has_additional_health_insurance='23').status == Response(status=400).status

def test_True_option_has_additional_health_insurance():
    assert type(data_to_use(has_additional_health_insurance=True)) != type(Response())

def test_False_option_has_additional_health_insurance():
    assert type(data_to_use(has_additional_health_insurance=False)) != type(Response())

####################################################################
# TEST ADRESS VARIABLES
# patient_adress
# patient_adress_number
# patient_adress_neigh
# patient_adress_city
# patient_adress_uf 
# patient_adress_cep
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
    assert data_to_use(patient_adress=str(lenght_test[:65])).status == Response(status=400).status

def test_wrongtype_patient_adress_number():
    assert data_to_use(patient_adress_number='1212312').status == Response(status=400).status

def test_empty_value_patient_adress_number():
    assert type(data_to_use(patient_adress_number=None)) != type(Response())

def test_empty_space_patient_adress_number():
    assert data_to_use(patient_adress_number='   ').status == Response(status=400).status

def test_invalid_value_patient_adress_number():
    assert data_to_use(patient_adress_number='123').status == Response(status=400).status

def test_long_value_patient_adress_number():
    assert data_to_use(patient_adress_number=1234567).status == Response(status=400).status

def test_wrongtype_patient_adress_neigh():
    assert data_to_use(patient_adress_neigh=1212).status == Response(status=400).status

def test_empty_value_patient_adress_neigh():
    assert type(data_to_use(patient_adress_neigh=None)) != type(Response())

def test_empty_space_patient_adress_neigh():
    assert type(data_to_use(patient_adress_neigh='   ')) != type(Response())

def test_invalid_value_patient_adress_neigh():
    assert data_to_use(patient_adress_neigh='123').status == Response(status=400).status

def test_long_value_patient_adress_neigh():
    assert data_to_use(patient_adress_neigh=str(lenght_test[:33])).status == Response(status=400).status

def test_wrongtype_patient_adress_city():
    assert data_to_use(patient_adress_city=1212).status == Response(status=400).status

def test_empty_value_patient_adress_city():
    assert type(data_to_use(patient_adress_city=None)) != type(Response())

def test_empty_space_patient_adress_city():
    assert type(data_to_use(patient_adress_city='   ')) != type(Response())

def test_invalid_value_patient_adress_city():
    assert data_to_use(patient_adress_city='123').status == Response(status=400).status

def test_long_value_patient_adress_city():
    assert data_to_use(patient_adress_city=str(lenght_test[:36])).status == Response(status=400).status

def test_wrongtype_patient_adress_cep():
    assert data_to_use(patient_adress_cep='1212').status == Response(status=400).status

def test_empty_value_patient_adress_cep():
    assert type(data_to_use(patient_adress_cep=None)) != type(Response())

def test_empty_space_patient_adress_cep():
    assert data_to_use(patient_adress_cep='   ').status == Response(status=400).status

def test_invalid_value_patient_adress_cep():
    assert data_to_use(patient_adress_cep=1231).status == Response(status=400).status

def test_long_value_patient_adress_cep():
    assert data_to_use(patient_adress_cep=lenght_test[:10]).status == Response(status=400).status

def test_wrongtype_patient_adress_uf():
    assert data_to_use(patient_adress_uf=1231).status == Response(status=400).status

def test_notexistopiton_patient_adress_uf():
    assert data_to_use(patient_adress_uf='AUYD').status == Response(status=400).status

def test_AC_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AC')) != type(Response())

def test_AC_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ac')) != type(Response())

def test_AL_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AL')) != type(Response())

def test_AL_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='al')) != type(Response())

def test_AP_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AP')) != type(Response())

def test_AP_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ap')) != type(Response())

def test_AM_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AM')) != type(Response())

def test_AM_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='am')) != type(Response())

def test_BA_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='BA')) != type(Response())

def test_BA_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ba')) != type(Response())

def test_CE_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='CE')) != type(Response())

def test_CE_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ce')) != type(Response())

def test_DF_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='DF')) != type(Response())

def test_DF_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='df')) != type(Response())

def test_ES_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ES')) != type(Response())

def test_ES_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='es')) != type(Response())

def test_GO_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='GO')) != type(Response())

def test_GO_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='go')) != type(Response())

def test_MA_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MA')) != type(Response())

def test_MA_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ma')) != type(Response())

def test_MS_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MS')) != type(Response())

def test_MS_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ms')) != type(Response())

def test_MT_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MT')) != type(Response())

def test_MT_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='mt')) != type(Response())

def test_MG_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MG')) != type(Response())

def test_MG_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='mg')) != type(Response())

def test_PA_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PA')) != type(Response())

def test_PA_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pa')) != type(Response())

def test_PB_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PB')) != type(Response())

def test_PB_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pb')) != type(Response())

def test_PR_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PR')) != type(Response())

def test_PR_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pr')) != type(Response())

def test_PE_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PE')) != type(Response())

def test_PE_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pe')) != type(Response())

def test_PI_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PI')) != type(Response())

def test_PI_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pi')) != type(Response())

def test_RJ_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RJ')) != type(Response())

def test_RJ_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rj')) != type(Response())

def test_RN_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RN')) != type(Response())

def test_RN_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rn')) != type(Response())

def test_RS_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RS')) != type(Response())

def test_RS_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rs')) != type(Response())

def test_RO_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RO')) != type(Response())

def test_RO_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ro')) != type(Response())

def test_RR_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RR')) != type(Response())

def test_RR_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rr')) != type(Response())

def test_SC_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='SC')) != type(Response())

def test_SC_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='sc')) != type(Response())

def test_SP_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='SP')) != type(Response())

def test_SP_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='sp')) != type(Response())

def test_SE_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='SE')) != type(Response())

def test_SE_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='se')) != type(Response())

def test_TO_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='TO')) != type(Response())

def test_TO_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='to')) != type(Response())


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
    assert data_to_use(current_illness_history=lenght_test[:1610]).status == Response(status=400).status

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
    assert data_to_use(patient_drug_allergies=lenght_test[:110]).status == Response(status=400).status

def test_wrong_type_patient_comorbidities():
    assert data_to_use(patient_comorbidities=131).status == Response(status=400).status

def test_empty_value_patient_comorbidities():
    assert data_to_use(patient_comorbidities='').status == Response(status=400).status

def test_empty_spaces_patient_comorbidities():
    assert data_to_use(patient_comorbidities='    ').status == Response(status=400).status

def test_shortText_patient_comorbidities():
    assert data_to_use(patient_comorbidities='abla').status == Response(status=400).status

def test_more_than_limit_patient_comorbidities():
    assert data_to_use(patient_comorbidities=lenght_test[:110]).status == Response(status=400).status

def test_wrong_type_initial_diagnostic_suspicion():
    assert data_to_use(initial_diagnostic_suspicion=131).status == Response(status=400).status

def test_empty_value_initial_diagnostic_suspicion():
    assert data_to_use(initial_diagnostic_suspicion='').status == Response(status=400).status

def test_empty_spaces_initial_diagnostic_suspicion():
    assert data_to_use(initial_diagnostic_suspicion='    ').status == Response(status=400).status

def test_shortText_initial_diagnostic_suspicion():
    assert data_to_use(initial_diagnostic_suspicion='abla').status == Response(status=400).status

def test_more_than_limit_initial_diagnostic_suspicion():
    assert data_to_use(initial_diagnostic_suspicion=lenght_test[:110]).status == Response(status=400).status

def test_wrong_type_doctor_crm():
    assert data_to_use(doctor_crm=131).status == Response(status=400).status

def test_empty_value_doctor_crm():
    assert data_to_use(doctor_crm='').status == Response(status=400).status

def test_empty_spaces_doctor_crm():
    assert data_to_use(doctor_crm='    ').status == Response(status=400).status

def test_shortText_doctor_crm():
    assert data_to_use(doctor_crm='abla').status == Response(status=400).status

def test_more_than_limit_doctor_crm():
    assert data_to_use(doctor_crm=lenght_test[:14]).status == Response(status=400).status

def test_wrong_type_patient_nationality():
    assert data_to_use(patient_nationality=131).status == Response(status=400).status

def test_empty_value_patient_nationality():
    assert type(data_to_use(patient_nationality='')) != type(Response())

def test_empty_spaces_patient_nationality():
    assert type(data_to_use(patient_nationality='    ')) != type(Response())

def test_shortText_patient_nationality():
    assert data_to_use(patient_nationality='ab').status == Response(status=400).status

def test_more_than_limit_patient_nationality():
    assert data_to_use(patient_nationality=lenght_test[:27]).status == Response(status=400).status

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
# patient_estimate_weight
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
    assert data_to_use(patient_phonenumber=int(lenght_test[:14])).status == Response(status=400).status

def test_shortValue_patient_phonenumber():
    assert data_to_use(patient_phonenumber=1234567).status == Response(status=400).status

def test_wrong_type_patient_estimate_weight():
    assert data_to_use(patient_estimate_weight='131').status == Response(status=400).status

def test_empty_value_patient_estimate_weight():
    assert type(data_to_use(patient_estimate_weight=None)) != type(Response())

def test_empty_spaces_patient_estimate_weight():
    assert data_to_use(patient_estimate_weight='    ').status == Response(status=400).status

def test_longValue_patient_estimate_weight():
    assert data_to_use(patient_estimate_weight=float(lenght_test[:8])).status == Response(status=400).status

def test_shortValue_patient_estimate_weight():
    assert type(data_to_use(patient_estimate_weight=123)) != type(Response())

