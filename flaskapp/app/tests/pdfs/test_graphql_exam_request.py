from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
from app.env import GRAPHQL_MUTATION_QUERY_URL
import pytest

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
def client():
    # Select your transport with ag graphql url endpoint
    transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)
    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)

def data_to_use(client, datetime_to_use, patient_name='Patient Name',patient_cns='928976954930007', patient_birthday=None,patient_adress="Patient Adress",exams="Exames tests with a text",solicitation_reason="Solicitation Reason",prof_solicitor_name="Professional Solicitor",prof_authorized_name="Professional Authorized",solicitation_datetime=None,autorization_datetime=None, document_pacient_date=None,document_pacient_name='Document pacient name'):

    if patient_birthday == None:
        patient_birthday = datetime_to_use
    if solicitation_datetime == None:
        solicitation_datetime = datetime_to_use
    if document_pacient_date == None:
        document_pacient_date = datetime_to_use
    if autorization_datetime == None:
        autorization_datetime = datetime_to_use

    request_string = """
        mutation{
            generatePdf_SolicitExames("""

    campos_string = f"""
    patientName: "{patient_name}",
    patientCns: "{patient_cns}",
    patientBirthday: "{patient_birthday}",
    patientAdress: "{patient_adress}",
    solicitationReason: "{solicitation_reason}",
    profSolicitorName: "{prof_solicitor_name}",
    solicitationDatetime: "{solicitation_datetime}",
    exams: "{exams}",
    profAuthorizedName: "{prof_authorized_name}", 
    documentPacientName: "{document_pacient_name}",
    autorizationDatetime: "{autorization_datetime}",
    documentPacientDate: "{document_pacient_date}"
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

#Testing Ficha Internamento
def test_with_data_in_function(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True

def test_answer_with_all_fields(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True

def test_awnser_with_only_required_data(client, datetime_to_use):
    request_string = """
        mutation{
            generatePdf_SolicitExames("""

    campos_string = """
    patientName: "Patient NAme",
    patientCns: "928976954930007",
    patientBirthday: "10/10/2021",
    patientAdress: "Patient Adress",
    solicitationReason: "Solicitation reason",
    profSolicitorName: "Professional solicitor Name",
    solicitationDatetime: "10/10/2014",
    exams: "Required exams"
    """

    final_string = """
    ){base64Pdf}
    }
    """
    all_string = request_string + campos_string + final_string
    query = gql(all_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True


##############################################################
# ERRORS IN NAMES CAMPS
# patientName
# prof_authorized_name
# prof_solicitor_name
# document_pacient_name
# Name empty
# Name with space
# long name
# short name
# wrong name type


@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_prof_authorized_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, prof_authorized_name=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_document_pacient_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_pacient_name=test_input) == True


#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_datetime
# autorization_datetime
# document_pacient_date
# test wrong type
# test valid datetime

def test_valid_patient_birthday(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use,patient_birthday=datetime_to_use) == True

def test_valid_solicitation_datetime(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use,solicitation_datetime=datetime_to_use) == True

def test_valid_autorization_datetime(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use,autorization_datetime=datetime_to_use) == True

def test_valid_document_pacient_date(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use,document_pacient_date=datetime_to_use) == True


#############################################################################
# TEST TEXT VARIABLES THAT CHANGE NUMBER OF PAGS
# exams
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit
# test 1 page long 
# test 2 pages long
# test 3 pages long

def test_1_pages_long_exams(client, datetime_to_use, lenght_test):
    text = lenght_test[:200]
    assert data_to_use(client, datetime_to_use,exams=text) == True

def test_2_pages_long_exams(client, datetime_to_use, lenght_test):
    text = lenght_test[:400]
    assert data_to_use(client, datetime_to_use,exams=text) == True

def test_3_pages_long_exams(client, datetime_to_use, lenght_test):
    text = lenght_test[:750]
    assert data_to_use(client, datetime_to_use,exams=text) == True






