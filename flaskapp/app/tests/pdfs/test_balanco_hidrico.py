from gql import gql
import pytest


def data_to_use(client, datetime_to_use, patient_name='Patient Name', patient_weight=52, fluid_balances=[{'created_at': "2023-02-08T01:17:20.624559",'volumeMl': -600,'description': "diurese"}]):


    all_balance = ''
    for balance in fluid_balances:
        all_balance += '{createdAt:' + f'"{balance["created_at"]}"' + ',volumeMl:' + f'{balance["volumeMl"]}' + ',description:' + f'"{balance["description"]}"' + '},'
    
        patient = '{name: ' + f'"{patient_name}"' + ', cns: ' + '"928976954930007"' + ',weightKg:' + f'{patient_weight}' + '}'


    request_string = """
    mutation{
        generatePdf_BalancoHidrico("""

    campos_string = f"""
    patient: {patient}
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
        print(all_string)
        return False

#Testing balanco hidrico
def test_with_data_in_function(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True

def test_answer_with_all_fields(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True

##############################################################
# ERRORS IN NAMES CAMPS

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_patient_name(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, patient_name=test_input) == False


#################################################################
# TEST WEIGHT

@pytest.mark.parametrize("test_input", [10, 1, 5, 50, 120])
def test_valid_patient_weight(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, patient_weight=test_input) == True



##################################################################
# TEST FLUID BALANCES

@pytest.mark.parametrize("test_input", [
    [{'created_at': "2023-02-08T01:17:20.624559",'volumeMl': -600,'description': "diurese"}],
    [{'created_at': "2023-02-08T01:17:20.624559",'volumeMl': 600,'description': "diurese"}],
])
def test_valid_fluid_balance(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, fluid_balances=test_input) == True


@pytest.mark.parametrize("test_input", [
    [{'created_at': "20/12/2022",'volumeMl': -600,'description': "diurese"}],
    [{'created_at': "20/12/2022 10:35",'volumeMl': 600,'description': "diuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediuresediurese"}],
    [{'created_at': "20/12/2022 10:35",'volumeMl': -0.45,'description': "diurese"}],
])
def test_invalid_fluid_balance(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, fluid_balances=test_input) == False
