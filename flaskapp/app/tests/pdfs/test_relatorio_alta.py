from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
from app.env import GRAPHQL_MUTATION_QUERY_URL
import pytest

# Variable to parametrize 
global lenght_test_parametrize
lenght_test_parametrize = ''
for x in range(0, 1100):
    lenght_test_parametrize += str(x)

@pytest.fixture
def lenght_test():
    """generate a string with data with charactes to test lenght"""
    lenght_test = ''
    for x in range(0, 1100):
        lenght_test += str(x)
    return lenght_test

@pytest.fixture
def datetime_to_use():
    """get current datetime to test"""
    return datetime.datetime.now().strftime('%d/%m/%Y')

@pytest.fixture
def document_datetime_to_use():
    """get current datetime with hours and minutes to test"""
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

@pytest.fixture
def client():
    # Select your transport with ag graphql url endpoint
    transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)
    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)

def data_to_use(client, datetime_to_use, document_datetime_to_use, document_datetime=None, patient_name="Patient Name",patient_cns='928976954930007',patient_birthday=None,patient_sex='F',patient_mother_name="Patient Mother Name",patient_cpf='"28445400070"', patient_rg='null',patient_address='pacient street, 43, paciten, USA',evolution='Current illnes hsitoryaaaaaaaaaaaedqeqa',doctor_name='Doctor Name',doctor_cns='928976954930007',doctor_crm='CRM/UF 123456',orientations='Do not jump'):

    if document_datetime == None:
        document_datetime = document_datetime_to_use
    if patient_birthday == None:
        patient_birthday = datetime_to_use


    patient_address = '{' + 'street: ' + f'"{patient_address}"' + ', city: ' + f'"City"' + ', uf:' + f'"SP"' + ', neighborhood: ' + '"Neigh"' + ', number: ' + '"1"' + '},'

    patient = '{name: ' + f'"{patient_name}"' + ', cns: ' + f'"{patient_cns}"' + ', birthdate: ' + f'"{patient_birthday}"' + ', cpf: ' + str(patient_cpf) + ', rg: ' + f'"{patient_rg}"' + ', sex: ' + f'"{patient_sex}"' + ', motherName: ' + f'"{patient_mother_name}"' + ', address: ' + f'{patient_address}' + '}'

    request_string = """
        mutation{
            generatePdf_RelatorioAlta("""

    campos_string = f"""
        documentDatetime: "{document_datetime}",
        patient: {patient},
        doctorName: "{doctor_name}",
        doctorCns: "{doctor_cns}",
        doctorCrm: "{doctor_crm}",
        evolution: "{evolution}",
        orientations: "{orientations}"
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
def test_answer_with_all_fields(client, datetime_to_use, document_datetime_to_use):
    """Test relatorio alta with all data correct"""
    assert data_to_use(client, datetime_to_use, document_datetime_to_use) == True

def test_awnser_with_only_required_data(client, datetime_to_use, document_datetime_to_use):
    result = False
    
    request_string = """
        mutation{
            generatePdf_RelatorioAlta("""


    campos_string = """
        documentDatetime: "17/11/2022 03:23",
        patient: {
            name:"Patient Namme",
            cns: "928976954930007",
            birthdate: "17/11/2022",
            sex: "F",
            motherName: "Patient Mother Name",
            cpf: "28445400070",
            rg: null,
            address: {
                street: "pacient street",
                city: "City",
                neighborhood: "neighborhood",
                number: "41",
                uf: "SP"
            }
        }
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

@pytest.mark.parametrize("test_input", ['    ', '', lenght_test_parametrize[:71], '11113', 123124])
def test_patient_mother_name(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_mother_name=test_input) == False

@pytest.mark.parametrize("test_input", ['    ', '', lenght_test_parametrize[:52], '11113', 123124])
def test_doctor_name(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, doctor_name=test_input) == False


#################################################################
#TEST DOCUMENTS RG AND CPF
# patient_document
# wrong type
# invalid rg
# valido rg
# invalid cpf
# valid cpf
# wrong option


@pytest.mark.parametrize("test_input", [
    '"451236548554"',
    '"284123312123"',
    '"284123312123"'
])
def test_false_patient_cpf(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_cpf=test_input) == False

@pytest.mark.parametrize("test_input", [
    '"43423412399"'
])
def test_true_patient_cpf(client, datetime_to_use, document_datetime_to_use, test_input):
    # Until this time, cns is as 
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_cpf=test_input) == True

@pytest.mark.parametrize("test_input", [
    '1964895912341948',
    '52541675346',
    'asdyugaudygay'
])
def test_false_patient_cns(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_cns=test_input) == False

@pytest.mark.parametrize("test_input", [
    '928976954930007'
])
def test_true_patient_cns(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_cns=test_input) == True

@pytest.mark.parametrize("test_input", [
    "sdfsf2",
    "28123",
    "284123312123123421",
    "sdffsd2323425sdf"
])
def test_false_patient_rg(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_rg=test_input, patient_cpf='null') == False

@pytest.mark.parametrize("test_input", [
    "928976954930007"
])
def test_true_patient_rg(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_rg=test_input, patient_cpf='null') == True

#################################################################
# TEST DATETIMES VARIABLES
# document_datetime
# patient_birthday
# autorizaton_datetime
# test wrong type

def test_wrongtype_document_datetime(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, document_datetime='bahabah') == False

def test_valid_document_datetime(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, document_datetime=document_datetime_to_use) == True

def test_wrongtype_patient_birthday(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_birthday='bahabah') == False

def test_valid_patient_birthday(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_birthday=datetime_to_use) == True


##################################################################
# TEST MARKABLE OPTIONS
# patient_sex

@pytest.mark.parametrize("test_input", ['G', 1231])
def test_false_sex(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_sex=test_input) == False

@pytest.mark.parametrize("test_input", ['M', 'm', 'F', 'f'])
def test_sex(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_sex=test_input) == True



####################################################################
# TEST ADRESS VARIABLES
# patient_address

@pytest.mark.parametrize("test_input", [lenght_test_parametrize[:65]])
def test_patient_address(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_address=test_input) == False


#############################################################################
# TEST BIG TEXT WITH LINE BRAKES
# evolution
# orientations

@pytest.mark.parametrize("test_input", ['', '    ', 111, 'aaaa', lenght_test_parametrize[:2150]])
def test_evolution(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, evolution=test_input) == False

@pytest.mark.parametrize("test_input", [111, 'aaaa', lenght_test_parametrize[:850]])
def test_false_orientations(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, orientations=test_input) == False

@pytest.mark.parametrize("test_input", ['', '    '])
def test_true_orientations(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, orientations=test_input) == True

#################################################################################
# TEST CNS
# patient_cns
# doctor_cns
# wrong type
# valid
# invalid
# empty send

@pytest.mark.parametrize("test_input", ['13123', '928976546250007', 'null'])
def test_false_patient_cns(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_cns=test_input) == False

def test_valid_patient_cns(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_cns="928976954930007") == True


@pytest.mark.parametrize("test_input", ['13123', '928976546250007', 'null'])
def test_false_doctor_cns(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, doctor_cns=test_input) == False

def test_valid_doctor_cns(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, doctor_cns="928976954930007") == True

