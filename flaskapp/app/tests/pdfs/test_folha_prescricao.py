from gql import gql
import pytest


def data_to_use(client, document_datetime_to_use, created_at=None, printed_at=None, patient_name='Patient Name', prescriptions=[{'type': "Repouso",'description': "Prescription description",'route': "Endovenosa",'start_date': "10/11/2022",'ending_date': "21/11/2022"}]):

    if created_at == None:
        created_at = document_datetime_to_use
    if printed_at == None:
        printed_at = document_datetime_to_use

    all_prescriptions = ''
    for presc in prescriptions:
        all_prescriptions += '{type:' + f'"{presc["type"]}"' + ',description:' + f'"{presc["description"]}"' + ',route:' + f'"{presc["route"]}"' + ',startDate:' + f'"{presc["start_date"]}"' + ',endingDate:' + f'"{presc["ending_date"]}"' + '},'

    patient = '{name: ' + f'"{patient_name}"' + ', cns: ' + '"928976954930007"' + ',weightKg:' + '123' + '}'

    request_string = """
        mutation{
	        generatePdf_FolhaPrescricao("""

    campos_string = f"""
    createdAt: "{created_at}",
    printedAt: "{printed_at}",
    patient: {patient},
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

#Testing folha prescricao
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
    assert data_to_use(client, document_datetime_to_use, created_at='10/10/24') == False

def test_valid_printed_at(client, document_datetime_to_use):
    assert data_to_use(client, document_datetime_to_use, printed_at=document_datetime_to_use) == True

def test_invalid_printed_at(client, document_datetime_to_use):
    assert data_to_use(client, document_datetime_to_use, printed_at='10/10/24') == False

##################################################################
# TEST PRESCRIPTIONS

@pytest.mark.parametrize("test_input", [
    [{'type': "Repouso",'description': "Prescription description",'route': "Endovenosa",'start_date': "10/11/2022",'ending_date': "21/11/2022"}],
    [{'type': "Another Repouso",'description': "AAAAAAPrescription description",'route': "Endovenosa",'start_date': "10/11/2022",'ending_date': "21/11/2022"}],
    [{'type': "Another Repouso",'description': "Prescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPresc",'route': "Endovenosa",'start_date': "10/11/2022",'ending_date': "21/11/2022"}],
])
def test_valid_prescriptions(client, document_datetime_to_use, test_input):
    assert data_to_use(client, document_datetime_to_use, prescriptions=test_input) == True

