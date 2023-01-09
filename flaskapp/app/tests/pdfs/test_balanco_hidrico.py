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


def data_to_use(client, datetime_to_use, created_at=None, patient_name='Patient Name', patient_weight=52, fluid_balances=[{'created_at': "20/12/2022 10:35",'value': -600,'description': "diurese"}]):

    if created_at == None:
        created_at = datetime_to_use

    all_balance = ''
    for balance in fluid_balances:
        all_balance += '{createdAt:' + f'"{balance["created_at"]}"' + ',value:' + f'{balance["value"]}' + ',description:' + f'"{balance["description"]}"' + '},'

    request_string = """
    mutation{
        generatePdf_BalancoHidrico("""

    campos_string = f"""
    createdAt: "{created_at}",
    patientName: "{patient_name}",
    patientWeight: {patient_weight},
    fluidBalance:[{all_balance}]
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