from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
from flask import Response
from app.env import GRAPHQL_MUTATION_QUERY_URL

global lenght_test
lenght_test = ''
for x in range(0, 1100):
    lenght_test += str(x)

datetime_to_use = datetime.datetime.now().strftime('%d/%m/%Y')

# Select your transport with ag graphql url endpoint
transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

def data_to_use(patient_name='Patient Name',patient_cns='928976954930007', patient_birthday=datetime_to_use,patient_adress="Patient Adress",exams=lenght_test[:800],solicitation_reason="Solicitation Reason",prof_solicitor_name="Professional Solicitor",prof_authorized_name="Professional Authorized",solicitation_datetime=datetime_to_use,autorization_datetime=datetime_to_use, document_pacient_date=datetime_to_use,document_pacient_name='Document pacient name'):
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
def test_with_data_in_function():
    assert data_to_use() == True

def test_answer_with_all_fields():
    assert data_to_use() == True

def test_awnser_with_only_required_data():
    assert type(pdf_exam_request.fill_pdf_exam_request(
        patient_name='Patient Name', 
        patient_cns=928976954930007, 
        patient_birthday=datetime_to_use, 
        patient_adress="Patient Adress", 
        exams=lenght_test[:800],
        solicitation_datetime=datetime_to_use,
        solicitation_reason="Solicitation Reason", 
        prof_solicitor_name="Professional Solicitor"
    )) != type(Response())

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

def test_empty_patientName():    
    assert data_to_use(patient_name='').status == Response(status=400).status

def test_with_space_patientName():    
    assert data_to_use(patient_name='  ').status == Response(status=400).status

def test_long_patientName():    
    assert data_to_use(patient_name=lenght_test[:84]).status == Response(status=400).status

def test_short_patientName():    
    assert data_to_use(patient_name='bro').status == Response(status=400).status

def test_wrongtype_patientName():    
    assert data_to_use(patient_name=123124).status == Response(status=400).status

def test_empty_prof_authorized():    
    assert type(data_to_use(prof_authorized_name='')) != type(Response())

def test_with_space_prof_authorized():    
    assert type(data_to_use(prof_authorized_name='  ')) != type(Response())

def test_long_prof_authorized():    
    assert data_to_use(prof_authorized_name=lenght_test[:32]).status == Response(status=400).status

def test_short_prof_authorized():    
    assert data_to_use(prof_authorized_name='bro').status == Response(status=400).status

def test_wrongtype_prof_authorized():    
    assert data_to_use(prof_authorized_name=123124).status == Response(status=400).status

def test_empty_prof_solicitor():    
    assert data_to_use(prof_solicitor_name='').status == Response(status=400).status

def test_with_space_prof_solicitor():    
    assert data_to_use(prof_solicitor_name='  ').status == Response(status=400).status

def test_long_prof_solicitor():    
    assert data_to_use(prof_solicitor_name=lenght_test[:32]).status == Response(status=400).status

def test_short_prof_solicitor():    
    assert data_to_use(prof_solicitor_name='bro').status == Response(status=400).status

def test_wrongtype_prof_solicitor():    
    assert data_to_use(prof_solicitor_name=123124).status == Response(status=400).status

def test_empty_document_pacient_name():    
    assert type(data_to_use(document_pacient_name='')) != type(Response())

def test_with_space_document_pacient_name():    
    assert type(data_to_use(document_pacient_name='  ')) != type(Response())

def test_long_document_pacient_name():    
    assert data_to_use(document_pacient_name=lenght_test[:50]).status == Response(status=400).status

def test_short_document_pacient_name():    
    assert data_to_use(document_pacient_name='bro').status == Response(status=400).status

def test_wrongtype_document_pacient_name():    
    assert data_to_use(document_pacient_name=123124).status == Response(status=400).status

####################################################################
# TEST CNES 
# patient_cns
# empty
# wrong type
# invalid cnes

def test_empty_patient_cns():
    assert data_to_use(patient_cns='').status == Response(status=400).status

def test_wrongtype_patient_cns():
    assert data_to_use(patient_cns='adsadad').status == Response(status=400).status

def test_invalidcnes_patient_cns():
    assert data_to_use(patient_cns=451236548).status == Response(status=400).status



#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_datetime
# autorization_datetime
# document_pacient_date
# test wrong type
# test valid datetime

def test_wrongtype_patient_birthday():
    assert data_to_use(patient_birthday='bahabah').status == Response(status=400).status

def test_valid_patient_birthday():
    assert type(data_to_use(patient_birthday=datetime_to_use)) != type(Response())

def test_wrongtype_solicitation_datetime():
    assert data_to_use(solicitation_datetime='bahabah').status == Response(status=400).status

def test_valid_solicitation_datetime():
    assert type(data_to_use(solicitation_datetime=datetime_to_use)) != type(Response())

def test_wrongtype_autorization_datetime():
    assert data_to_use(autorization_datetime='bahabah').status == Response(status=400).status

def test_valid_autorization_datetime():
    assert type(data_to_use(autorization_datetime=datetime_to_use)) != type(Response())

def test_wrongtype_document_pacient_date():
    assert data_to_use(document_pacient_date='bahabah').status == Response(status=400).status

def test_valid_document_pacient_date():
    assert type(data_to_use(document_pacient_date=datetime_to_use)) != type(Response())


####################################################################
# TEST ADRESS VARIABLES
# patient_adress
# test wrong type
# test empty value
# test empty space value
# invalid value
# Long value

def test_wrongtype_patient_adress():
    assert data_to_use(patient_adress=1212312).status == Response(status=400).status

def test_empty_value_patient_adress():
    assert data_to_use(patient_adress='').status == Response(status=400).status

def test_empty_space_patient_adress():
    assert data_to_use(patient_adress='  ').status == Response(status=400).status

def test_invalid_value_patient_adress():
    assert data_to_use(patient_adress='111').status == Response(status=400).status

def test_long_value_patient_adress():
    assert data_to_use(patient_adress=lenght_test[:220]).status == Response(status=400).status


#############################################################################
# NORMAL TEXT VARIABLES THAT CANNOT BE NULL
# solicitation_reason
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit


def test_wrong_type_solicitation_reason():
    assert data_to_use(solicitation_reason=131).status == Response(status=400).status

def test_empty_value_solicitation_reason():
    assert data_to_use(solicitation_reason='').status == Response(status=400).status

def test_empty_spaces_solicitation_reason():
    assert data_to_use(solicitation_reason='    ').status == Response(status=400).status

def test_shortText_solicitation_reason():
    assert data_to_use(solicitation_reason='abla').status == Response(status=400).status

def test_more_than_limit_solicitation_reason():
    assert data_to_use(solicitation_reason=lenght_test[:220]).status == Response(status=400).status


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

def test_wrong_type_exams():
    assert data_to_use(exams=131).status == Response(status=400).status

def test_empty_value_exams():
    assert data_to_use(exams='').status == Response(status=400).status

def test_empty_spaces_exams():
    assert data_to_use(exams='    ').status == Response(status=400).status

def test_shortText_exams():
    assert data_to_use(exams='abla').status == Response(status=400).status

def test_more_than_limit_exams():
    assert data_to_use(exams=lenght_test[:980]).status == Response(status=400).status

def test_1_pages_long_exams():
    assert type(data_to_use(exams=lenght_test[:200])) != type(Response())

def test_2_pages_long_exams():
    assert type(data_to_use(exams=lenght_test[:400])) != type(Response())

def test_3_pages_long_exams():
    assert type(data_to_use(exams=lenght_test[:750])) != type(Response())






