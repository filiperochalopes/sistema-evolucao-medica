from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
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
def client():
    # Select your transport with ag graphql url endpoint
    transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)
    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)


def data_to_use(client, datetime_to_use, establishment_solitc_name='Establishment Solicit Name',establishment_solitc_cnes=1234567,patient_name='Patient Name',patient_cns="928976954930007",patient_sex='M',patient_birthday=None, patient_address_city='Patient Adress City',main_procedure='{name: "teste procedimento",code: "hkmaug347s",quant: 1}',patient_mother_name='Patient Mother Name',patient_mother_phonenumber='5286758957', patient_responsible_name='Patient Responsible Name', patient_responsible_phonenumber='5465981345', patient_address='Patient Adress',patient_color='Branca',patient_ethnicity='Indigena',patient_address_uf='BA',patient_address_cep='86425910', document_chart_number='12345',patient_address_city_ibge_code=4528765,procedure_justification_description='Procedure Justification Description', prodedure_justification_main_cid_10='A98', prodedure_justification_sec_cid_10='A01', procedure_justification_associated_cause_cid_10='A45',procedure_justification_comments='Procedure Justification Comments',establishment_exec_name='Establishment Exec Name', establishment_exec_cnes=7654321,prof_solicitor_document='{cns: "928976954930007",cpf: null,rg: null}', prof_solicitor_name='Profissional Solicit Name',solicitation_datetime=None,signature_datetime=None,validity_period_start=None,validity_period_end=None,autorization_prof_name='Autorization Professional Name', emission_org_code='Cod121234',autorizaton_prof_document='{cns: "928976954930007",cpf: null,rg: null}', autorizaton_datetime=None,secondaries_procedures='[{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "segundo",code: "hkmhsa3s23",quant: 4}]'):

    if patient_birthday == None:
        patient_birthday = datetime_to_use
    if solicitation_datetime == None:
        solicitation_datetime = datetime_to_use
    if validity_period_start == None:
        validity_period_start = datetime_to_use
    if validity_period_end == None:
        validity_period_end = datetime_to_use
    if signature_datetime == None:
        signature_datetime = datetime_to_use
    if autorizaton_datetime == None:
        autorizaton_datetime = datetime_to_use


    # Creating inputs
    establishment_solitc = '{name: ' + f'"{establishment_solitc_name}"' + ', cnes: ' + f'"{establishment_solitc_cnes}"' + '}'
    establishment_exec = '{name: ' + f'"{establishment_exec_name}"' + ', cnes: ' + f'"{establishment_exec_cnes}"' + '}'

    patient_address = '{' + 'street: ' + f'"{patient_address}"' + ', city: ' + f'"{patient_address_city}"' + ', ibgeCityCode: ' + f'"{patient_address_city_ibge_code}"' + ', uf:' + f'"{patient_address_uf}"' + ', zipCode: ' + f'"{patient_address_cep}"' + '},'

    patient = '{name: ' + f'"{patient_name}"' + ', cns: ' + f'"{patient_cns}"' + ', birthdate: ' + f'"{patient_birthday}"' + ', sex: ' + f'"{patient_sex}"' + 'ethnicity: ' + f'"{patient_ethnicity}"' + ', motherName: ' + f'"{patient_mother_name}"' + ', address: ' + f'{patient_address}' + '}'

    request_string = """
        mutation{
            generatePdf_Apac("""

    campos_string = f"""
    establishmentSolitc: {establishment_solitc},
    patient: {patient}
    mainProcedure: {main_procedure},
    secondariesProcedures: {secondaries_procedures},
    patientMotherPhonenumber: "{patient_mother_phonenumber}",
    patientResponsibleName: "{patient_responsible_name}",
    patientResponsiblePhonenumber: "{patient_responsible_phonenumber}",
    patientColor: "{patient_color}",
    documentChartNumber: "{document_chart_number}",
    procedureJustificationDescription: "{procedure_justification_description}",
    procedureJustificationMainCid10: "{prodedure_justification_main_cid_10}",
    procedureJustificationSecCid10: "{prodedure_justification_sec_cid_10}",
    procedureJustificationAssociatedCauseCid10: "{procedure_justification_associated_cause_cid_10}",
    procedureJustificationComments: "{procedure_justification_comments}",
    establishmentExec: {establishment_exec},
    profSolicitorDocument: {prof_solicitor_document},
    profSolicitorName: "{prof_solicitor_name}",
    solicitationDatetime: "{solicitation_datetime}",
    profAutorizationName: "{autorization_prof_name}",
    emissionOrgCode: "{emission_org_code}",
    autorizatonProfDocument: {autorizaton_prof_document},
    autorizatonDatetime: "{autorizaton_datetime}",
    signatureDatetime: "{signature_datetime}",
    validityPeriodStart: "{validity_period_start}",
    validityPeriodEnd: "{validity_period_end}"
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

#Testing APAC
def test_with_data_in_function(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True

def test_answer_with_all_fields(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True

def test_awnser_with_only_required_data(client):
    request_string = """
        mutation{
            generatePdf_Apac("""

    campos_string = """
    establishmentSolitc: {
        name: "Establishmente Solict Name",
        cnes: "1234567"
    },
    establishmentExec: {
        name:"Establishment exec Name",
        cnes: "1234567"
    },
    patient: {
        name: "Patient Patient Name",
        cns: "928976954930007",
        birthdate: "10/10/2022",
        sex: "M",
        address: {
            city: "Jau",
            ibgeCityCode: "1234567",
            uf: "SP",
        }
    },
    mainProcedure: {name: "teste procedimento",code: "hkmaug347s",quant: 1}
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
# establishment_solitc_name
# patient_name
# patient_mother_name
# patient_responsible_name
# establishment_exec_name
# prof_solicitor_name
# autorization_prof_name
# !!!!!!! TESTING !!!!!!!
# Name empty
# Name with space
# long name
# short name
# wrong name type


@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_patient_mother_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, patient_mother_name=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_establishment_exec_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, establishment_exec_name=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_prof_solicitor_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, prof_solicitor_name=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_autorization_prof_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, autorization_prof_name=test_input) == True



#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_datetime
# autorizaton_datetime
# signature_datetime
# validity_period_end 
# validity_period_start
# test wrong type
# test valid datetime

def test_valid_patient_birthday(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, patient_birthday=datetime_to_use) == True

def test_valid_solicitation_datetime(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, solicitation_datetime=datetime_to_use) == True

def test_valid_autorizaton_datetime(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, autorizaton_datetime=datetime_to_use) == True

def test_valid_signature_datetime(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, signature_datetime=datetime_to_use) == True

def test_valid_validity_period_start(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, validity_period_start=datetime_to_use) == True

def test_valid_validity_period_end (client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, validity_period_end =datetime_to_use) == True




##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# patient_address_uf
# test wrong type
# test not exist option
# test all options in Upper Case
# test all options in lower Case

@pytest.mark.parametrize("test_input", ['G', 1231])
def test_false_sex(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, patient_sex=test_input) == False

@pytest.mark.parametrize("test_input", ['M', 'm', 'F', 'f'])
def test_sex(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, patient_sex=test_input) == True

@pytest.mark.parametrize("test_input", ['AC', 'ac', 'AL', 'al', 'AP', 'ap', 'AM', 'am', 'BA', 'ba', 'CE', 'ce', 'DF', 'df', 'ES', 'es', 'GO', 'go', 'MA', 'ma', 'MS', 'ms', 'MT','mt', 'MG', 'mg', 'PA', 'pa', 'PB', 'pb', 'PE', 'pe', 'PR', 'pr', 'PI', 'pi', 'RJ', 'rj', 'RN', 'rn', 'RS', 'rs', 'RO', 'ro', 'RR', 'rr', 'SC', 'sc', 'SP', 'sp', 'SE', 'se', 'TO', 'to'])
def test_ufs(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, patient_address_uf=test_input) == True


####################################################################
# TEST ADRESS VARIABLES
# patient_address
# patient_address_city
# patient_address_city_ibge_code
# patient_address_uf (already tested in option tests)
# patient_address_cep
# test wrong type
# test empty value
# test empty space value
# invalid value
# Long value

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_patient_address(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, patient_address=test_input) == True


#############################################################################
# TEST BIG TEXT WITH LINE BRAKES
# procedure_justification_comments
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit


@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_procedure_justification_comments(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, procedure_justification_comments=test_input) == True

@pytest.mark.parametrize("test_input", [1, 1090])
def test_text_lenght_procedure_justification_comments(test_input, client, datetime_to_use, lenght_test):
    text = lenght_test[:test_input]
    assert data_to_use(client, datetime_to_use, procedure_justification_comments=text) == False



##############################################################################
# TEST MAIN PROCEDURES

def test_right_main_procedure(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, main_procedure='{name: "teste procedimento",code: "hkmaug347s",quant: 1}') == True

def test_one_secondary_procedure(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, secondaries_procedures='{name: "teste procedimento",code: "hkmaug347s",quant: 1}') == True

def test_5_secondary_procedure(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, secondaries_procedures='[{name: "teste procedimento",code: "hkmaug347s",quant: 1}, {name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1}]') == True

def test_more_than_5_secondary_procedure(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, secondaries_procedures='[{name: "teste procedimento",code: "hkmaug347s",quant: 1}, {name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1}]') == False


##############################################################################
# TEST STRING THAT CAN BE NULL
# patient_ethnicity
# patient_color
# prodedure_justification_main_cid_10
# prodedure_justification_sec_cid_10
# procedure_justification_associated_cause_cid_10
# emission_org_code
# test wront type
# test empty value
# test empty spaces
# test long values
# test short values

@pytest.mark.parametrize("test_input", [None, '    ', ''])
def test_empty_value_patient_ethnicity(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, patient_ethnicity=test_input) == True

@pytest.mark.parametrize("test_input", [None, '    ', ''])
def test_empty_value_patient_color(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, patient_color=test_input) == True

@pytest.mark.parametrize("test_input", [None, '    ', ''])
def test_empty_value_prodedure_justification_main_cid_10(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, prodedure_justification_main_cid_10=test_input) == True

@pytest.mark.parametrize("test_input", [None, '    ', ''])
def test_empty_value_prodedure_justification_sec_cid_10(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, prodedure_justification_sec_cid_10=test_input) == True

@pytest.mark.parametrize("test_input", [None, '    ', ''])
def test_empty_value_procedure_justification_associated_cause_cid_10(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, procedure_justification_associated_cause_cid_10=test_input) == True

@pytest.mark.parametrize("test_input", [None, '    ', ''])
def test_empty_value_emission_org_code(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, emission_org_code=test_input) == True
