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
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

@pytest.fixture
def client():
    # Select your transport with ag graphql url endpoint
    transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)
    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)


def data_to_use(client, datetime_to_use, created_at=None, printed_at=None, patient_name='Patient Name', prescriptions=[{'type': "Repouso",'description': "Prescription description",'route': "Endovenosa",'start_date': "10/11/2022",'ending_date': "21/11/2022"}]):

    if created_at == None:
        created_at = datetime_to_use
    if printed_at == None:
        printed_at = datetime_to_use

    all_prescriptions = ''
    for presc in prescriptions:
        all_prescriptions += '{type:' + f'"{presc["type"]}"' + ',description:' + f'"{presc["description"]}"' + ',route:' + f'"{presc["route"]}"' + ',startDate:' + f'"{presc["start_date"]}"' + ',endingDate:' + f'"{presc["ending_date"]}"' + '},'


    request_string = """
        mutation{
	        generatePdf_FolhaPrescricao("""

    campos_string = f"""
    createdAt: "{created_at}",
    printedAt: "{printed_at}",
    patientName: "{patient_name}",
    prescriptions: [{all_prescriptions}]
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

#Testing Aih SUS
def test_with_data_in_function(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True


##############################################################
# ERRORS IN NAMES CAMPS

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_patient_name(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, patient_name=test_input) == False

#################################################################
# TEST DATETIMES VARIABLES

def test_valid_created_at(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, created_at=datetime_to_use) == True

def test_invalid_created_at(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, created_at='10/10/24') == False

def test_valid_printed_at(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, printed_at=datetime_to_use) == True

def test_invalid_printed_at(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, printed_at='10/10/24') == False

##################################################################
# TEST PRESCRIPTIONS

@pytest.mark.parametrize("test_input", [
    [{'type': "Repouso",'description': "Prescription description",'route': "Endovenosa",'start_date': "10/11/2022",'ending_date': "21/11/2022"}],
    [{'type': "Another Repouso",'description': "AAAAAAPrescription description",'route': "Endovenosa",'start_date': "10/11/2022",'ending_date': "21/11/2022"}],
    [{'type': "Another Repouso",'description': "Prescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPresc",'route': "Endovenosa",'start_date': "10/11/2022",'ending_date': "21/11/2022"}],
])
def test_valid_prescriptions(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, prescriptions=test_input) == True

