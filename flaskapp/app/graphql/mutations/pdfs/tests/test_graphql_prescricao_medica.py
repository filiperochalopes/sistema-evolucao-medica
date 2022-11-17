from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
from app.env import GRAPHQL_MUTATION_QUERY_URL

global lenght_test
lenght_test = ''
for x in range(0, 2000):
    lenght_test += str(x)

datetime_to_use = datetime.datetime.now().strftime('%d/%m/%Y')

# Select your transport with ag graphql url endpoint
transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

def data_to_use(_=None, info=None, document_datetime=datetime_to_use,
        patient_name='Pacient Name',
        prescription='{medicineName:"Dipirona 500mg", amount:"4 comprimidos", useMode:"1 comprimido, via oral, de 6/6h por 3 dias"}'):
        
        request_string = """
        mutation{
            generatePdf_PrescricaoMedica("""

        campos_string = f"""
            documentDatetime: "{document_datetime}",
            patientName: "{patient_name}",
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
def test_answer_with_all_fields():
    """Test fill ficha internamento with all data correct"""
    assert data_to_use() == True


##############################################################
# ERRORS IN NAMES CAMPS
# patient_name

def test_wrongtype_patient_name():    
    assert data_to_use(patient_name=123124) == False

def test_empty_patient_name():    
    assert data_to_use(patient_name='') == False

def test_with_space_patient_name():    
    assert data_to_use(patient_name='  ') == False

def test_long_patient_name():    
    assert data_to_use(patient_name=str(lenght_test[:36])) == False

def test_short_patient_name():    
    assert data_to_use(patient_name='11113') == False

#################################################################
# TEST DATETIMES VARIABLES
# document_datetime

def test_wrongtype_document_datetime():
    assert data_to_use(document_datetime='bahabah') == False

def test_valid_document_datetime():
    assert data_to_use(document_datetime=datetime_to_use) == True

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

def test_wrongtype_prescriptions():
    assert data_to_use(prescription=131231) == False

def test_list_with_other_types():
    assert data_to_use(prescription=154287) == False


def test_dicts_without_necessary_keys():
    query_to_test = f"""
    medicineName:"Dipirona", 
    amount: "8 comprimidos"
    """
    assert data_to_use(prescription=str('{' + query_to_test + '}')) == False

def test_dicts_with_more_than_necessary_keys():
    query_to_test = f"""
    medicineName:"Dipirona", 
    amount: "8 comprimidos", 
    useMode:"8/8 comprimidos",
    dontExiste: "uai"
    """
    assert data_to_use(prescription=str('{' + query_to_test + '}')) == False

def test_medicine_name_with_wrongtype():
    query_to_test = f"""
    medicineName:65452, 
    amount: "8 comprimidos", 
    useMode:"8/8 comprimidos"
    """
    assert data_to_use(prescription=str('{' + query_to_test + '}')) == False

def test_medicine_name_longer():
    query_to_test = f"""
    medicineName:"{lenght_test[:70]}", 
    amount: "8 comprimidos", 
    useMode:"8/8 comprimidos"
    """
    assert data_to_use(prescription=str('{' + query_to_test + '}')) == False

def test_amount_with_wrongtype():
    query_to_test = f"""
    medicineName:"sadfasdf", 
    amount:875452, 
    useMode:"8/8 comprimidos"
    """
    assert data_to_use(prescription=str('{' + query_to_test + '}')) == False

def test_amount_longer():
    query_to_test = f"""
    medicineName:"sadfasdf", 
    amount:"{lenght_test[:265]}", 
    useMode:"8/8 comprimidos"
    """
    assert data_to_use(prescription=str('{' + query_to_test + '}')) == False
    

def test_use_mode_with_wrongtype():
    query_to_test = f"""
    medicineName:"sadfasdf", 
    amount:"4 comprimidos", 
    useMode: 112313
    """
    assert data_to_use(prescription=str('{' + query_to_test + '}')) == False

def test_use_mode_longer():
    query_to_test = f"""
    medicineName:"sadfasdf", 
    amount:"4 comprimidos", 
    useMode:"{lenght_test[:265]}"
    """
    assert data_to_use(prescription=str('{' + query_to_test + '}')) == False
    












