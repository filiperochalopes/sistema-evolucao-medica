from gql import gql
import pytest


def data_to_use(client, document_datetime_to_use, created_at=None, patient_name='Patient Name',
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
        created_at = document_datetime_to_use

    all_evolutions = ''
    for evo in evolutions:
        all_evolutions += '{createdAt:' + f'"{evo["created_at"]}"' + ',description:' + f'"{evo["description"]}",' + 'professional:' + f'{evo["professional"]}' +'},'

    all_measures = ''
    for evo in measures:
        all_measures += '{createdAt:' + f'"{evo["created_at"]}"' + ',cardiacFrequency:' + f'{evo["cardiac_frequency"]}' + ',respiratoryFrequency:' + f'{evo["respiratory_frequency"]}' + ',sistolicBloodPressure:' + f'{evo["sistolic_blood_pressure"]}' + ',diastolicBloodPressure:' + f'{evo["diastolic_blood_pressure"]}' + ',glucose:' + f'"{evo["glucose"]}"' + ',spO2:' + f'{evo["spO2"]}' + ',celciusAxillaryTemperature:' + f'{evo["celcius_axillary_temperature"]}' + ',pain:' + f'{evo["pain"]}' + ',professional:' + f'{evo["professional"]}' +'},'

    patient = '{name: ' + f'"{patient_name}"' + ', cns: ' + '"928976954930007"' + ',weightKg:' + '123' + '}'

    request_string = """
    mutation{
	generatePdf_FolhaEvolucao("""

    campos_string = f"""
    createdAt: "{created_at}",
    patient: {patient},
    evolutions:[{all_evolutions}],
    measures: [{all_measures}],
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

#Testing Folha evolucao
def test_with_data_in_function(client, document_datetime_to_use):
    assert data_to_use(client, document_datetime_to_use) == True

##############################################################
# ERRORS IN NAMES CAMPS

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_patient_name(client, document_datetime_to_use, test_input):
    assert data_to_use(client, document_datetime_to_use, patient_name=test_input) == False

#################################################################
# TEST DATETIMES VARIABLES

def test_valid_created_at(client, document_datetime_to_use):
    assert data_to_use(client, document_datetime_to_use, created_at=document_datetime_to_use) == True

def test_invalid_created_at(client, document_datetime_to_use):
    assert data_to_use(client, document_datetime_to_use, created_at='10:10:24 - 1245') == False

##################################################################
# TEST EVOLUTIONS

@pytest.mark.parametrize("test_input", [
    [{
        'created_at': "10/10/2022 20:10",
        'description': "quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem.",
        'professional':'{name: "Professional Name",category: "m",document: "12345/BA"}'}],
    [{
        'created_at': "10/10/2022 20:10",
        'description': "quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem.",
        'professional':'{name: "Professional Name",category: "m",document: "12345/BA"}'}],
])
def test_valid_evolutions(client, document_datetime_to_use, test_input):
    assert data_to_use(client, document_datetime_to_use, evolutions=test_input) == True

@pytest.mark.parametrize("test_input", [
    [{
        'created_at': "10/10/2022",
        'description': "quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem.",
        'professional':'{name: "Professional Name",category: "m",document: "12345/BA"}'}],
    [{
        'created_at': "20:10",
        'description': "quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem.quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem.quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem.quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem.",
        'professional':'{name: "Professional Name",category: "m",document: "11331/BA"}'}],
])
def test_invalid_evolutions(client, document_datetime_to_use, test_input):
    assert data_to_use(client, document_datetime_to_use, evolutions=test_input) == False


##################################################################
# TEST MEASURES

@pytest.mark.parametrize("test_input", [
    [{
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
        },],
])
def test_valid_measures(client, document_datetime_to_use, test_input):
    assert data_to_use(client, document_datetime_to_use, measures=test_input) == True

@pytest.mark.parametrize("test_input", [
    [{
        'created_at': "10/10/2022",
        'cardiac_frequency': 54,
        'respiratory_frequency': 15,
        'sistolic_blood_pressure': 152,
        'diastolic_blood_pressure': 84,
        'glucose': "152",
        'spO2': 96,
        'celcius_axillary_temperature': 37,
        'pain': 2,
        'professional':'{name: "Professional Name",category: "m",document: "12345/BA"}'
        },],
    [{
        'created_at': "10/10/2022 20:10",
        'cardiac_frequency': '"54"',
        'respiratory_frequency': 15,
        'sistolic_blood_pressure': 152,
        'diastolic_blood_pressure': 84,
        'glucose': "152",
        'spO2': 96,
        'celcius_axillary_temperature': 37,
        'pain': 2,
        'professional':'{name: "Professional Name",category: "m",document: "12345/BA"}'
        },],
    [{
        'created_at': "20:10",
        'cardiac_frequency': 54,
        'respiratory_frequency': 15,
        'sistolic_blood_pressure': 152,
        'diastolic_blood_pressure': 84,
        'glucose': "152",
        'spO2': 96,
        'celcius_axillary_temperature': 37,
        'pain': 2,
        'professional':'{name: "Professional Name",category: "m",document: "12345/BA"}'
        },],
    [{
        'created_at': "10/10/2022 20:10",
        'cardiac_frequency': 54,
        'respiratory_frequency': 15,
        'sistolic_blood_pressure': 152,
        'diastolic_blood_pressure': 84,
        'glucose': "152",
        'spO2': 96,
        'celcius_axillary_temperature': 37,
        'pain': 2,
        'professional':'{name: 1,category: "m",document: "12345/BA"}'
        },],
    [{
        'created_at': "10/10/2022 20:10",
        'cardiac_frequency': 54,
        'respiratory_frequency': 15,
        'sistolic_blood_pressure': '"152"',
        'diastolic_blood_pressure': 84,
        'glucose': "152",
        'spO2': 96,
        'celcius_axillary_temperature': 37,
        'pain': 2,
        'professional':'{name: "Professional Name",category: "m",document: "12345/BA"}'
        },],
    [{
        'created_at': "10/10/2022 20:10",
        'cardiac_frequency': 54,
        'respiratory_frequency': 15,
        'sistolic_blood_pressure': 152,
        'diastolic_blood_pressure': 84,
        'glucose': "152",
        'spO2': 96,
        'celcius_axillary_temperature': '"37"',
        'pain': '"2"',
        'professional':'{name: "Professional Name",category: "m",document: "12345/BA"}'
        },],
])
def test_invalid_measures(client, document_datetime_to_use, test_input):
    assert data_to_use(client, document_datetime_to_use, measures=test_input) == False





