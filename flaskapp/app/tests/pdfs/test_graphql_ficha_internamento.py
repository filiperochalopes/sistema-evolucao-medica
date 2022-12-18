from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
from flask import Response
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
    return datetime.datetime.now().strftime('%d/%m/%Y')

@pytest.fixture
def document_datetime_to_use():
    """get current datetime with hours and minutes to test"""
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M')


@pytest.fixture
def client():
    # Select your transport with ag graphql url endpoint
    transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)
    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)


def data_to_use(client, datetime_to_use, document_datetime_to_use, document_datetime=None, patient_name="Patient Name",patient_cns='928976954930007',patient_birthday=None,patient_sex='F',patient_mother_name="Patient Mother Name",patient_document='{cpf: "28445400070",cns: null,rg: null}',patient_adress='pacient street, 43, paciten, USA',patient_phonenumber='44387694628', patient_drug_allergies='Penicillin, Aspirin, Ibuprofen, Anticonvulsants.', patient_comorbidities='Heart disease, High blood pressure, Diabetes, Cerebrovascular disease.',current_illness_history='Current illnes hsitoryaaaaaaaaaaa',initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral',doctor_name='Doctor Name',doctor_cns='928976954930007',doctor_crm='CRM/UF 123456',patient_adress_number=123456,patient_adress_neigh='Patient Neighborhood',patient_adress_city='Patient city',patient_adress_uf='sp',patient_adress_cep='12345678',patient_nationality='Brasileira',patient_estimate_weight=123,has_additional_health_insurance='SIM'):

    if patient_birthday == None:
        patient_birthday = datetime_to_use
    if document_datetime == None:
        document_datetime = document_datetime_to_use

    request_string = """
        mutation{
            generatePdf_FichaInternamento("""

    campos_string = f"""
    documentDatetime: "{document_datetime}",
    patientName: "{patient_name}",
    patientCns: "{patient_cns}",
    patientBirthday: "{patient_birthday}",
    patientSex: "{patient_sex}",
    patientMotherName: "{patient_mother_name}",
    patientDocument: {patient_document},
    patientAdress: "{patient_adress}",
    patientPhonenumber: "{patient_phonenumber}",
    patientDrugAllergies: "{patient_drug_allergies}",
    patientComorbidities: "{patient_comorbidities}",
    currentIllnessHistory: "{current_illness_history}",
    hasAdditionalHealthInsurance: "{has_additional_health_insurance}",
    initialDiagnosticSuspicion: "{initial_diagnostic_suspicion}",
    doctorName: "{doctor_name}",
    doctorCns: "{doctor_cns}",
    doctorCrm: "{doctor_crm}",
    patientAdressNumber: {patient_adress_number},
    patientAdressNeigh: "{patient_adress_neigh}",
    patientAdressCity: "{patient_adress_city}",
    patientAdressUf: "{patient_adress_uf}",
    patientAdressCep: "{patient_adress_cep}",
    patientNationality: "{patient_nationality}",
    patientEstimateWeight: {patient_estimate_weight}
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
def test_answer_with_all_fields(client, datetime_to_use, document_datetime_to_use):
    """Test fill ficha internamento with all data correct"""
    assert data_to_use(client, datetime_to_use, document_datetime_to_use) == True


def test_awnser_with_only_required_data(client, datetime_to_use, document_datetime_to_use):
    request_string = """
        mutation{
            generatePdf_FichaInternamento("""

    campos_string = """
    documentDatetime: "10/10/2014 10:12",
    patientName: "Patient Name",
    patientCns: "928976954930007",
    patientBirthday: "10/10/2021",
    patientSex: "M",
    patientMotherName: "Patient Mother Name",
    patientDocument: {cpf: "28445400070",cns: null,rg: null},
    patientAdress: "Patient Adress",
    patientPhonenumber: "10123456789",
    patientDrugAllergies: "Patient Drug Allergies",
    patientComorbidities: "Patient Commorbidites",
    currentIllnessHistory: "Current Illness History",
    initialDiagnosticSuspicion: "Initial Suspiction",
    doctorName: "Doctor Name",
    doctorCns: "928976954930007",
    doctorCrm: "CRM/UF 123456",
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

def test_validrg_patient_document(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_document='{cpf: null,cns: null,rg: "928976954930007"}') == True

def test_validcpf_patient_document(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_document='{cpf: "28445400070",cns: null,rg: null}') == True


#################################################################
# TEST DATETIMES VARIABLES
# documentDatetime
# patient_birthday
# autorizaton_datetime
# test wrong type

def test_valid_documentDatetime(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, document_datetime=document_datetime_to_use) == True

def test_valid_patient_birthday(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_birthday=datetime_to_use) == True

##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# has_additional_health_insurance
# test wrong type
# test not exist option
# test all options in Upper Case
# test all options in lower Case

@pytest.mark.parametrize("test_input", ['G', 1231])
def test_false_sex(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_sex=test_input) == False

@pytest.mark.parametrize("test_input", ['M', 'm', 'F', 'f'])
def test_sex(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_sex=test_input) == True

@pytest.mark.parametrize("test_input", ['SIM', 'NAO'])
def test_has_additional_health_insurance(client, datetime_to_use, document_datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, has_additional_health_insurance=test_input) == True

####################################################################
# TEST ADRESS VARIABLES
# patient_adress
# patient_adress_number
# patient_adress_neigh
# patient_adress_city
# patient_adress_uf 
# patient_adress_cep
# test wrong type
# test empty value
# test empty space value
# invalid value
# Long value

@pytest.mark.parametrize("test_input", ['AC', 'ac', 'AL', 'al', 'AP', 'ap', 'AM', 'am', 'BA', 'ba', 'CE', 'ce', 'DF', 'df', 'ES', 'es', 'GO', 'go', 'MA', 'ma', 'MS', 'ms', 'MT','mt', 'MG', 'mg', 'PA', 'pa', 'PB', 'pb', 'PE', 'pe', 'PR', 'pr', 'PI', 'pi', 'RJ', 'rj', 'RN', 'rn', 'RS', 'rs', 'RO', 'ro', 'RR', 'rr', 'SC', 'sc', 'SP', 'sp', 'SE', 'se', 'TO', 'to'])
def test_ufs(client, datetime_to_use, document_datetime_to_use,test_input):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_adress_uf=test_input) == True


#################################################################################
# TEST CNS
# patient_cns
# doctor_cns
# wrong type
# valid
# invalid
# empty send

def test_valid_patient_cns(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_cns='928976954930007') == True

def test_valid_doctor_cns(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, doctor_cns='928976954930007') == True

#################################################################################
# TEST NUMBER VARIABLES CAN/CANNOT BE NULL
# patient_phonenumber
# patient_estimate_weight
# !!!!! TESTING
# wrong type
# test empty value
# test empty space
# short value
# long value  

def test_shortValue_patient_estimate_weight(client, datetime_to_use, document_datetime_to_use):
    assert data_to_use(client, datetime_to_use, document_datetime_to_use, patient_estimate_weight=123) == True

