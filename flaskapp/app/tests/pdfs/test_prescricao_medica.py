from gql import gql
import pytest

global lenght_test_parametrize
lenght_test_parametrize = ''
for x in range(0, 1100):
    lenght_test_parametrize += str(x)


def data_to_use(client, datetime_to_use, document_datetime=None,
        professional_name='Professional Name', 
        professional_category='m', 
        professional_document='12345/BA',
        patient_name='Pacient Name',
        prescription='{medicineName:"Dipirona 500mg", amount:"4 comprimidos", useMode:"1 comprimido, via oral, de 6/6h por 3 dias"}'):
        
        if document_datetime == None:
            document_datetime = datetime_to_use

        patient = '{name: ' + f'"{patient_name}"' + ', cns: ' + '"928976954930007"' + ',weightKg:' + '123' + '}'

        professional = '{' + 'name:' + f'"{professional_name}"' + ',category:' + f'"{professional_category}"' + ",document:" f'"{professional_document}"' + '}'

        request_string = """
        mutation{
            generatePdf_PrescricaoMedica("""

        campos_string = f"""
            documentDatetime: "{document_datetime}",
            patient: {patient},
            professional: {professional},
            prescription: [{prescription}]
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
def test_answer_with_all_fields(client, datetime_to_use):
    """Test fill ficha internamento with all data correct"""
    assert data_to_use(client, datetime_to_use) == True


##############################################################
# ERRORS IN NAMES CAMPS
# patient_name
# professional_name



@pytest.mark.parametrize("test_input", ['    ', '','11113', 123124])
def test_patient_name(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, patient_name=test_input) == False

def test_lenght_patient_name(client, datetime_to_use, lenght_test):
    text = lenght_test[:36]
    assert data_to_use(client, datetime_to_use, patient_name=text) == False

def test_lenght_professional_name(client, datetime_to_use, lenght_test):
    text = lenght_test[:100]
    assert data_to_use(client, datetime_to_use, professional_name=text) == False

#################################################################
# TEST DATETIMES VARIABLES
# document_datetime

def test_wrongtype_document_datetime(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime='bahabah') == False

def test_valid_document_datetime(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime=datetime_to_use) == True

#################################################################
# TEST prescriptions
# test wrong type
# test list with other type
# test dicts wihtout necessary keys
# test dicts with more than necessary keys
# test medicine_name with wrong type
# test medicine_name longer
# test amount with wrong type
# test amount longer
# test use_mode with wrong type
# test use_mode longer

@pytest.mark.parametrize("test_input", [
    f"""
    medicineName:"Dipirona", 
    amount: "8 comprimidos"
    """,
    f"""
    medicineName:"Dipirona", 
    amount: "8 comprimidos", 
    useMode:"8/8 comprimidos",
    dontExiste: "uai"
    """,
    f"""
    medicineName:65452, 
    amount: "8 comprimidos", 
    useMode:"8/8 comprimidos"
    """,
    f"""
    medicineName:"{lenght_test_parametrize[:70]}", 
    amount: "8 comprimidos", 
    useMode:"8/8 comprimidos"
    """,
    f"""
    medicineName:"sadfasdf", 
    amount:875452, 
    useMode:"8/8 comprimidos"
    """,
    f"""
    medicineName:"sadfasdf", 
    amount:"{lenght_test_parametrize[:265]}", 
    useMode:"8/8 comprimidos"
    """,
    f"""
    medicineName:"sadfasdf", 
    amount:"4 comprimidos", 
    useMode: 112313
    """,
    f"""
    medicineName:"sadfasdf", 
    amount:"4 comprimidos", 
    useMode:"{lenght_test_parametrize[:265]}"
    """
])
def test_prescription(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, prescription=str('{' + test_input + '}')) == False

