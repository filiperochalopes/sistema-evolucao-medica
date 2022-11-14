from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
from flask import Response
from app.env import GRAPHQL_MUTATION_QUERY_URL

global lenght_test
lenght_test = ''
for x in range(0, 2200):
    lenght_test += str(x)

datetime_to_use = datetime.datetime.now().strftime('%d/%m/%Y')
document_datetime_to_use = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

# Select your transport with ag graphql url endpoint
transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

def data_to_use(document_datetime=document_datetime_to_use, patient_name="Patient Name",patient_cns='928976954930007',patient_birthday=datetime_to_use,patient_sex='F',patient_mother_name="Patient Mother Name",patient_document='{cpf: "28445400070", rg: null, cns: null}',patient_adress='pacient street, 43, paciten, USA',evolution='Current illnes hsitoryaaaaaaaaaaaedqeqa',doctor_name='Doctor Name',doctor_cns='928976954930007',doctor_crm='CRM/UF 123456',orientations='Do not jump'):

    request_string = """
        mutation{
            generatePdf_RelatorioAlta("""

    campos_string = f"""
        documentDatetime: "{document_datetime}",
        patientName: "{patient_name}",
        patientCns: "{patient_cns}",
        patientBirthday: "{patient_birthday}",            
        patientSex: "{patient_sex}",            
        patientMotherName: "{patient_mother_name}",            
        patientDocument: {patient_document},  
        patientAdress: "{patient_adress}",
        doctorName: "{doctor_name}",
        doctorCns: "{doctor_cns}",
        doctorCrm: "{doctor_crm}",
        evolution: "{evolution}",
        orientations: "{orientations}",
    """

    final_string = """
    ){base64Pdf}
    }
    """

    all_string = request_string + campos_string + final_string
    query = gql(all_string)
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        return True
    except:
        return False 

#Testing telatorio alta
def test_answer_with_all_fields():
    """Test relatorio alta with all data correct"""
    assert data_to_use() == True

def test_awnser_with_only_required_data():
    result = False
    document_test = '{cpf: "28445400070", rg: null, cns: null}'
    
    request_string = """
        mutation{
            generatePdf_RelatorioAlta("""


    campos_string = f"""
        documentDatetime: "{document_datetime_to_use}",
        patientName: "Patient Name",
        patientCns: "928976954930007",
        patientBirthday: "{datetime_to_use}",
        patientSex: "F",
        patientMotherName: "Patient Mother Name",
        patientDocument: {document_test},
        patientAdress: "pacient street, 43, paciten, USA",
        evolution: "Current illnes hsitoryaaaaaaaaaaaedqeqa",
        doctorName: "Doctor Name",
        doctorCns: "928976954930007",
        doctorCrm: "CRM/UF 123456"
    """

    final_string = """
    ){base64Pdf}
    }
    """

    all_string = request_string + campos_string + final_string
    query = gql(all_string)
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    assert result == True


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
    assert data_to_use(patient_mother_name=123124) == False

def test_empty_patient_mother_name():    
    assert data_to_use(patient_mother_name='') == False

def test_with_space_patient_mother_name():    
    assert data_to_use(patient_mother_name='  ') == False

def test_long_patient_mother_name():    
    assert data_to_use(patient_mother_name=str(lenght_test[:71])) == False

def test_short_patient_mother_name():    
    assert data_to_use(patient_mother_name='11113') == False

def test_wrongtype_doctor_name():    
    assert data_to_use(doctor_name=123124) == False

def test_empty_doctor_name():    
    assert data_to_use(doctor_name='') == False

def test_with_space_doctor_name():    
    assert data_to_use(doctor_name='  ') == False

def test_long_doctor_name():    
    assert data_to_use(doctor_name=str(lenght_test[:52])) == False

def test_short_doctor_name():    
    assert data_to_use(doctor_name='11113') == False


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
    assert data_to_use(patient_document='451236548554') == False

def test_invalidrg_patient_document():
    assert data_to_use(patient_document='{cpf: null, rg: "28123", cns: null}') == False

def test_validrg_patient_document():
    assert data_to_use(patient_document='{cpf: null, rg: "928976954930007", cns: null}') == True

def test_invalidccpf_patient_document():
    assert data_to_use(patient_document='{cpf: "284123312123", rg: null, cns: null}') == False

def test_validcpf_patient_document():
    assert data_to_use(patient_document='{cpf: "43423412399", rg: null, cns: null}') == True

def test_wrongoption_patient_document():
    assert data_to_use(patient_document='{BBB: "284123312123", rg: null, cns: null}') == False

#################################################################
# TEST DATETIMES VARIABLES
# document_datetime
# patient_birthday
# autorizaton_datetime
# test wrong type

def test_wrongtype_document_datetime():
    assert data_to_use(document_datetime='bahabah') == False

def test_valid_document_datetime():
    assert data_to_use(document_datetime=document_datetime_to_use) == True

def test_wrongtype_patient_birthday():
    assert data_to_use(patient_birthday='bahabah') == False

def test_valid_patient_birthday():
    assert data_to_use(patient_birthday=datetime_to_use) == True


##################################################################
# TEST MARKABLE OPTIONS
# patient_sex

def test_wrongtype_patient_sex():
    assert data_to_use(patient_sex=1231) == False

def test_notexistopiton_patient_sex():
    assert data_to_use(patient_sex='G') == False

def test_M_optionUpper_patient_sex():
    assert data_to_use(patient_sex='M') == True

def test_M_optionLower_patient_sex():
    assert data_to_use(patient_sex='m') == True

def test_F_optionUpper_patient_sex():
    assert data_to_use(patient_sex='F') == True

def test_F_optionLower_patient_sex():
    assert data_to_use(patient_sex='f') == True



####################################################################
# TEST ADRESS VARIABLES
# patient_adress

def test_empty_value_patient_adress():
    assert data_to_use(patient_adress='') == False

def test_empty_space_patient_adress():
    assert data_to_use(patient_adress='   ') == False

def test_invalid_value_patient_adress():
    assert data_to_use(patient_adress='111') == False

def test_long_value_patient_adress():
    assert data_to_use(patient_adress=str(lenght_test[:65])) == False

#############################################################################
# TEST BIG TEXT WITH LINE BRAKES
# evolution
# orientations

def test_wrong_type_evolution():
    assert data_to_use(evolution=131) == False

def test_empty_value_evolution():
    assert data_to_use(evolution='') == False

def test_empty_spaces_evolution():
    assert data_to_use(evolution='    ') == False

def test_shortText_evolution():
    assert data_to_use(evolution='ablas') == False

def test_more_than_limit_evolution():
    assert data_to_use(evolution=lenght_test[:2150]) == False

def test_wrong_type_orientations():
    assert data_to_use(orientations=131) == False

def test_empty_value_orientations():
    assert data_to_use(orientations='') == True

def test_empty_spaces_orientations():
    assert data_to_use(orientations='    ') == True

def test_shortText_orientations():
    assert data_to_use(orientations='ablas') == False

def test_more_than_limit_orientations():
    assert data_to_use(orientations=lenght_test[:850]) == False


#################################################################################
# TEST CNS
# patient_cns
# doctor_cns
# wrong type
# valid
# invalid
# empty send

def test_wrongtype_patient_cns():
    assert data_to_use(patient_cns='13123') == False

def test_valid_patient_cns():
    assert data_to_use(patient_cns="928976954930007") == True

def test_invalid_patient_cns():
    assert data_to_use(patient_cns="928976546250007") == False

def test_empty_patient_cns():
    assert data_to_use(patient_cns='null') == False

def test_wrongtype_doctor_cns():
    assert data_to_use(doctor_cns='13123') == False

def test_valid_doctor_cns():
    assert data_to_use(doctor_cns="928976954930007") == True

def test_invalid_doctor_cns():
    assert data_to_use(doctor_cns="928976546250007") == False

def test_empty_doctor_cns():
    assert data_to_use(doctor_cns='null') == False











