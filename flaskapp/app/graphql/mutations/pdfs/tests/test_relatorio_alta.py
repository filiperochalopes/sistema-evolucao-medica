from .. import pdf_relatorio_de_alta
import datetime
from flask import Response

global lenghtTest
lenghtTest = ''
for x in range(0, 2200):
    lenghtTest += str(x)


def data_to_use(documentDatetime=datetime.datetime.now(), patient_name="Patient Name",patient_cns=928976954930007,patient_birthday=datetime.datetime.now(),patient_sex='F',patient_motherName="Patient Mother Name",patient_document={'CPF':28445400070},patient_adress='pacient street, 43, paciten, USA',evolution='Current illnes hsitoryaaaaaaaaaaaedqeqa',doctor_name='Doctor Name',doctor_cns=928976954930007,doctor_crm='CRM/UF 123456',orientations='Do not jump'):
    return pdf_relatorio_de_alta.fill_pdf_relatorio_alta(documentDatetime,  patient_name, patient_cns, patient_birthday, patient_sex, patient_motherName, patient_document,  patient_adress, evolution, doctor_name, doctor_cns, doctor_crm, orientations)

#Testing telatorio alta
def test_answer_with_all_fields():
    """Test relatorio alta with all data correct"""
    assert data_to_use() != type(Response())

def test_awnser_with_only_required_data():
    assert type(pdf_relatorio_de_alta.fill_pdf_relatorio_alta(documentDatetime=datetime.datetime.now(), patient_name="Patient Name",patient_cns=928976954930007,patient_birthday=datetime.datetime.now(),patient_sex='F',patient_motherName="Patient Mother Name",patient_document={'CPF':28445400070},patient_adress='pacient street, 43, paciten, USA',evolution='Current illnes hsitoryaaaaaaaaaaaedqeqa',doctor_name='Doctor Name',doctor_cns=928976954930007,doctor_crm='CRM/UF 123456') != type(Response()))


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


def test_wrongtype_patient_motherName():    
    assert data_to_use(patient_motherName=123124).status == Response(status=400).status

def test_empty_patient_motherName():    
    assert data_to_use(patient_motherName='').status == Response(status=400).status

def test_with_space_patient_motherName():    
    assert data_to_use(patient_motherName='  ').status == Response(status=400).status

def test_long_patient_motherName():    
    assert data_to_use(patient_motherName=str(lenghtTest[:71])).status == Response(status=400).status

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



####################################################################
# TEST ADRESS VARIABLES
# patient_adress

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

#############################################################################
# TEST BIG TEXT WITH LINE BRAKES
# evolution
# orientations

def test_wrong_type_evolution():
    assert data_to_use(evolution=131).status == Response(status=400).status

def test_empty_value_evolution():
    assert data_to_use(evolution='').status == Response(status=400).status

def test_empty_spaces_evolution():
    assert data_to_use(evolution='    ').status == Response(status=400).status

def test_shortText_evolution():
    assert data_to_use(evolution='ablas').status == Response(status=400).status

def test_more_than_limit_evolution():
    assert data_to_use(evolution=lenghtTest[:2150]).status == Response(status=400).status

def test_wrong_type_orientations():
    assert data_to_use(orientations=131).status == Response(status=400).status

def test_empty_value_orientations():
    assert type(data_to_use(orientations='')) != type(Response())

def test_empty_spaces_orientations():
    assert type(data_to_use(orientations='    ')) != type(Response())

def test_shortText_orientations():
    assert data_to_use(orientations='ablas').status == Response(status=400).status

def test_more_than_limit_orientations():
    assert data_to_use(orientations=lenghtTest[:850]).status == Response(status=400).status


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










