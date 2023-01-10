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

def data_to_use(client, datetime_to_use, created_at=None, patient_name='Patient Name',
        evolutions=[{
        'created_at': "10/10/2022 20:10",
        'description': "quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem.",
        'professional':'{name: "Professional Name",category: "m",document: "12345/BA"}'}],
        measures=[{
        'created_at': "10/10/2022 20:10",
        'cardiac_frequency': 54,
        'respiratory_frequency': 15,
        'sistolic_blood_pressure': 152,
        'diastolic_blood_pressure': 84,
        'glucose': "152",
        'spO2': 96,
        'celcius_axillary_temperature': 37,
        'pain': 2,
        'professional':'{name: "Professional Name",category: "m",document: "12345/BA"}'
        },]):

    if created_at == None:
        created_at = datetime_to_use

    all_evolutions = ''
    for evo in evolutions:
        all_evolutions += '{createdAt:' + f'"{evo["created_at"]}"' + ',description:' + f'"{evo["description"]}",' + 'professional:' + f'{evo["professional"]}' +'},'

    all_measures = ''
    for evo in measures:
        all_measures += '{createdAt:' + f'"{evo["created_at"]}"' + ',cardiacFrequency:' + f'{evo["cardiac_frequency"]}' + ',respiratoryFrequency:' + f'{evo["respiratory_frequency"]}' + ',sistolicBloodPressure:' + f'{evo["sistolic_blood_pressure"]}' + ',diastolicBloodPressure:' + f'{evo["diastolic_blood_pressure"]}' + ',glucose:' + f'"{evo["glucose"]}"' + ',spO2:' + f'{evo["spO2"]}' + ',celciusAxillaryTemperature:' + f'{evo["celcius_axillary_temperature"]}' + ',pain:' + f'{evo["pain"]}' + ',professional:' + f'{evo["professional"]}' +'},'


    request_string = """
    mutation{
	generatePdf_FolhaEvolucao("""

    campos_string = f"""
    createdAt: "{created_at}",
    patientName: "{patient_name}",
    evolutions:[{all_evolutions}],
    measures: [{all_measures}],
    """

    final_string = """
    ){base64Pdf}
    }
    """
    all_string = request_string + campos_string + final_string
    
    print(all_string)
    query = gql(all_string)
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        return True
    except:
        print(all_string)
        return False

#Testing Aih SUS
def test_with_data_in_function(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True