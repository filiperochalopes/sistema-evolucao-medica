from gql import gql
import pytest
from app.tests.pdfs.request_queries_examples import exam_request_required_data_request_string

def data_to_use(client, datetime_to_use, patient_name='Patient Name',patient_cns='928976954930007', patient_birthday=None,patient_address="Patient Adress",exams="Exames tests with a text",solicitation_reason="Solicitation Reason",requesting_professional_name="Professional Solicitor",professional_authorized_name="Professional Authorized",solicitation_date=None,authorization_date=None, document_pacient_date=None,document_pacient_name='Document pacient name'):

    if patient_birthday == None:
        patient_birthday = datetime_to_use
    if solicitation_date == None:
        solicitation_date = datetime_to_use
    if document_pacient_date == None:
        document_pacient_date = datetime_to_use
    if authorization_date == None:
        authorization_date = datetime_to_use

    patient_address = '{' + 'street: ' + f'"{patient_address}"' + ', uf:' + '"SP"' + ', city: ' + '"City"' + '},'

    patient = '{name: ' + f'"{patient_name}"' + ', cns: ' + f'"{patient_cns}"' + ', birthdate: ' + f'"{patient_birthday}"' + ',weightKg:' + '123' + ', address: ' + f'{patient_address}' + '}'

    request_string = """
        mutation{
            generatePdf_SolicitExames("""

    campos_string = f"""
    patient: {patient},
    solicitationReason: "{solicitation_reason}",
    requestingProfessionalName: "{requesting_professional_name}",
    solicitationDate: "{solicitation_date}",
    exams: "{exams}",
    professionalAuthorizedName: "{professional_authorized_name}", 
    documentPacientName: "{document_pacient_name}",
    authorizationDate: "{authorization_date}",
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
def test_with_data_in_function(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True

def test_answer_with_all_fields(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True

def test_awnser_with_only_required_data(client, datetime_to_use):
    
    query = gql(exam_request_required_data_request_string)
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
# professional_authorized_name
# requesting_professional_name
# document_pacient_name
# Name empty
# Name with space
# long name
# short name
# wrong name type


@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_professional_authorized_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, professional_authorized_name=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_document_pacient_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_pacient_name=test_input) == True


#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_date
# authorization_date
# document_pacient_date
# test wrong type
# test valid datetime

def test_valid_patient_birthday(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use,patient_birthday=datetime_to_use) == True

def test_valid_solicitation_date(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use,solicitation_date=datetime_to_use) == True

def test_valid_authorization_date(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use,authorization_date=datetime_to_use) == True

def test_valid_document_pacient_date(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use,document_pacient_date=datetime_to_use) == True


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

def test_1_pages_long_exams(client, datetime_to_use, lenght_test):
    text = lenght_test[:200]
    assert data_to_use(client, datetime_to_use,exams=text) == True

def test_2_pages_long_exams(client, datetime_to_use, lenght_test):
    text = lenght_test[:400]
    assert data_to_use(client, datetime_to_use,exams=text) == True

def test_3_pages_long_exams(client, datetime_to_use, lenght_test):
    text = lenght_test[:750]
    assert data_to_use(client, datetime_to_use,exams=text) == True






