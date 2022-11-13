from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime

global lenght_test
lenght_test = ''
for x in range(0, 2000):
    lenght_test += str(x)

datetime_to_use = datetime.datetime.now().strftime('%d/%m/%Y')

# Select your transport with ag graphql url endpoint
transport = AIOHTTPTransport(url="http://localhost:5000/api/v1/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

def data_to_use(_=None, info=None, document_datetime=datetime_to_use,
        patient_name='Pacient Name',
        prescription='{medicineName:"Dipirona 500mg", amount:"4 comprimidos", useMode:"1 comprimido, via oral, de 6/6h por 3 dias"}'):
        
        request_string = """
        mutation{
            generatePdf_PrecricaoMedica("""

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
        return client.execute(query)

#Testing Ficha Internamento
def test_answer_with_all_fields():
    """Test fill ficha internamento with all data correct"""
    assert type(data_to_use()) != type(Exception())


##############################################################
# ERRORS IN NAMES CAMPS
# patient_name

def test_wrongtype_patient_name():    
    assert type(data_to_use(patient_name=123124)) == type(Exception())

def test_empty_patient_name():    
    assert type(data_to_use(patient_name='')) == type(Exception())

def test_with_space_patient_name():    
    assert type(data_to_use(patient_name='  ')) == type(Exception())

def test_long_patient_name():    
    assert type(data_to_use(patient_name=str(lenght_test[:36]))) == type(Exception())

def test_short_patient_name():    
    assert type(data_to_use(patient_name='11113')) == type(Exception())

#################################################################
# TEST DATETIMES VARIABLES
# document_datetime

def test_wrongtype_document_datetime():
    assert type(data_to_use(document_datetime='bahabah')) == type(Exception())

def test_valid_document_datetime():
    assert type(data_to_use(document_datetime=datetime_to_use)) != type(Exception())

#################################################################
# TEST prescriptions
# test wrong type
# test list with other type
# test dicts wihtout necessary keys
# test dicts with more than necessary keys
# test message_name with wrong type
# test message_name longer
# test amount with wrong type
# test amount longer
# test use_mode with wrong type
# test use_mode longer

def test_wrongtype_prescriptions():
    assert type(data_to_use(prescription=131231)) == type(Exception())

def test_list_with_other_types():
    assert type(data_to_use(prescription=['bahabah', 12313])) == type(Exception())

def test_list_with_other_types():
    assert type(data_to_use(prescription=['bahabah', 12313])) == type(Exception())

def test_dicts_without_necessary_keys():
    assert type(data_to_use(prescription="{'medicine_name':'Dipirona 500mg', 'amount':'4 comprimidos'}")) == type(Exception())

def test_dicts_with_more_than_necessary_keys():
    assert type(data_to_use(prescription="{'medicine_name':'Dipirona 500mg', 'amount':'4 comprimidos', 'use_mode':'1 comprimido, via oral, de 6/6h por 3 dias', 'dontExiste':'aidsuad'}")) == type(Exception())

def test_message_name_with_wrongtype():
    assert type(data_to_use(prescription="{'medicine_name':123123123, 'amount':'4 comprimidos', 'use_mode':'1 comprimido, via oral, de 6/6h por 3 dias'}")) == type(Exception())

def test_message_name_longer():
    assert type(data_to_use(prescription=[{"medicine_name":lenght_test[:70], "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}])) == type(Exception())

def test_amount_with_wrongtype():
    assert type(data_to_use(prescription=[{"medicine_name":'123123123', "amount":1213, "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}])) == type(Exception())

def test_amount_longer():
    assert type(data_to_use(prescription=[{"medicine_name":"sadfasdf", "amount":lenght_test[:70], "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}])) == type(Exception())

def test_use_mode_with_wrongtype():
        assert type(data_to_use(prescription=[{"medicine_name":'123123123', "amount":"4 comprimidos", "use_mode":12312313}])) == type(Exception())

def test_use_mode_longer():
    assert type(data_to_use(prescription=[{'medicine_name':'sadfasdf', 'amount':'4 comprimidos', 'use_mode':lenght_test[:265]}])) == type(Exception())
    












