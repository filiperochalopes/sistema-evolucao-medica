from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
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
    request_string = """
        mutation{
            generatePdf_SolicitExames("""

    campos_string = """
    patientName: "Patient NAme",
    patientCns: "928976954930007",
    patientBirthday: "10/10/2021",
    patientAdress: "Patient Adress",
    solicitationReason: "Solicitation reason",
    profSolicitorName: "Professional solicitor Name",
    solicitationDatetime: "10/10/2014",
    exams: "Required exams"
    """

    final_string = """
    ){base64Pdf}
    }
    """
    all_string = request_string + campos_string + final_string
    query = gql(all_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True


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

def test_empty_prof_authorized():    
    assert data_to_use(prof_authorized_name='') == True

def test_with_space_prof_authorized():    
    assert data_to_use(prof_authorized_name='  ') == True

def test_empty_document_pacient_name():    
    assert data_to_use(document_pacient_name='') == True

def test_with_space_document_pacient_name():    
    assert data_to_use(document_pacient_name='  ') == True


#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_datetime
# autorization_datetime
# document_pacient_date
# test wrong type
# test valid datetime

def test_valid_patient_birthday():
    assert data_to_use(patient_birthday=datetime_to_use) == True

def test_valid_solicitation_datetime():
    assert data_to_use(solicitation_datetime=datetime_to_use) == True

def test_valid_autorization_datetime():
    assert data_to_use(autorization_datetime=datetime_to_use) == True

def test_valid_document_pacient_date():
    assert data_to_use(document_pacient_date=datetime_to_use) == True


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

def test_1_pages_long_exams():
    assert data_to_use(exams=lenght_test[:200]) == True

def test_2_pages_long_exams():
    assert data_to_use(exams=lenght_test[:400]) == True

def test_3_pages_long_exams():
    assert data_to_use(exams=lenght_test[:750]) == True






