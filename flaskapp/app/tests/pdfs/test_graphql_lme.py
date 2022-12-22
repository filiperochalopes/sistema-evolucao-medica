from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
from app.env import GRAPHQL_MUTATION_QUERY_URL
import pytest

# Variable to parametrize 
global lenght_test_parametrize
lenght_test_parametrize = ''
for x in range(0, 1100):
    lenght_test_parametrize += str(x)

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

def data_to_use(client, datetime_to_use, establishment_solitc_name='Establishment Solicit Name',
establishment_solitc_cnes=1234567,
patient_name='Patient Name',
patient_mother_name='Patient Mother Name',
patient_weight=142,
patient_height=180,
cid_10='A123',
anamnese="Anamnese",
prof_solicitor_name="Professional Solicitor Name",
solicitation_datetime=None,
prof_solicitor_document='{cpf:"28445400070"}',
capacity_attest='["nao", "Responsible Name"]',
filled_by='''["MEDICO", "Other name", "{'cpf':'28445400070'}"]''',
patient_ethnicity='["SEMINFO", "Patient Ethnicity"]',
previous_treatment='["SIM", "Previout Theatment"]',
diagnostic='Diagnostic',
patient_document='{cns: "928976954930007", rg: null, cpf: null}',
patient_email="patietemail@gmail.com",
contacts_phonenumbers='["1254875652", "4578456598"]',
medicines='[{medicineName: "nome do Medicamneto", quant1month:"20 comp",        quant2month: "15 comp", quant3month: "5 comp"},{medicineName: "nome do Medicamneto", quant1month:"20 comp", quant2month: "15 comp", quant3month: "5 comp"}]'
    ):

    if solicitation_datetime == None:
        solicitation_datetime = datetime_to_use

    request_string = """
        mutation{
            generatePdf_Lme("""

    campos_string = f"""
        establishmentSolitcName: "{establishment_solitc_name}",
        establishmentSolitcCnes: {establishment_solitc_cnes},
        patientName: "{patient_name}",
        patientMotherName: "{patient_mother_name}",
        patientWeight: {patient_weight},
        patientHeight: {patient_height},
        cid10: "{cid_10}",
        anamnese: "{anamnese}",
        profSolicitorName: "{prof_solicitor_name}",
        solicitationDatetime: "{solicitation_datetime}",
        profSolicitorDocument: {prof_solicitor_document},
        capacityAttest: {capacity_attest},
        filledBy: {filled_by},
        patientEthnicity: {patient_ethnicity},
        previousTreatment: {previous_treatment},
        diagnostic: "{diagnostic}",
        patientDocument: {patient_document},
        patientEmail: "{patient_email}",
        contactsPhonenumbers: {contacts_phonenumbers},
        medicines: {medicines}
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
    result = False
    request_string = """
        mutation{
            generatePdf_Lme("""

    campos_string = """
        establishmentSolitcName: "Establishment",
        establishmentSolitcCnes: 1234567,
        patientName: "Patient Name",
        patientMotherName: "Patient Mother Name",
        patientWeight: 180,
        patientHeight: 140,
        cid10: "A123",
        anamnese: "Anamnese",
        profSolicitorName: "Professional Solic Name",
        solicitationDatetime: "12/10/2022",
        profSolicitorDocument: {cpf:"28445400070"},
        capacityAttest: ["nao", "Responsible Name"],
        filledBy: ["MEDICO", "Other name", "{'cpf':'28445400070'}"],
        patientEthnicity: ["SEMINFO", "Patient Ethnicity"],
        previousTreatment: ["SIM", "Previout Theatment"]
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
        result = True
    except:
        result = False 
    assert result == True
    


##############################################################
# ERRORS IN NAMES CAMPS
# establishment_solitc_name
# patient_name
# patient_mother_name
# cappacity attest [patient_responsible_name]
# prof_solicitor_name
# !!!!!!! TESTING !!!!!!!
# Name empty
# Name with space
# long name
# short name
# wrong name type


@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_establishment_solitc_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, establishment_solitc_name=test_input) == False

@pytest.mark.parametrize("test_input", [70, 1])
def test_text_establishment_solitc_name(test_input, client, datetime_to_use, lenght_test):
    text = lenght_test[:test_input]
    assert data_to_use(client, datetime_to_use, establishment_solitc_name=text) == False

def test_wrongtype_establishment_solitc_name(client, datetime_to_use):    
    assert data_to_use(client, datetime_to_use, establishment_solitc_name=123124) == False

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_patient_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, patient_name=test_input) == False

@pytest.mark.parametrize("test_input", [81, 1])
def test_text_patient_name(test_input, client, datetime_to_use, lenght_test):
    text = lenght_test[:test_input]
    assert data_to_use(client, datetime_to_use, patient_name=text) == False

def test_wrongtype_patient_name(client, datetime_to_use):    
    assert data_to_use(client, datetime_to_use, patient_name=123124) == False

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_patient_mother_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, patient_mother_name=test_input) == False

@pytest.mark.parametrize("test_input", [81,1])
def test_text_patient_mother_name(test_input, client, datetime_to_use, lenght_test):
    text = lenght_test[:test_input]
    assert data_to_use(client, datetime_to_use, patient_mother_name=text) == False

def test_wrongtype_patient_mother_name(client, datetime_to_use):    
    assert data_to_use(client, datetime_to_use, patient_mother_name=123124) == False

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_prof_solicitor_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, prof_solicitor_name=test_input) == False

@pytest.mark.parametrize("test_input", [50, 1])
def test_text_prof_solicitor_name(test_input, client, datetime_to_use, lenght_test):
    text = lenght_test[:test_input]
    assert data_to_use(client, datetime_to_use, prof_solicitor_name=text) == False

def test_wrongtype_prof_solicitor_name(client, datetime_to_use):    
    assert data_to_use(client, datetime_to_use, prof_solicitor_name=123124) == False

@pytest.mark.parametrize("test_input", ['["sim", ""]', '["sim", " "]', f'["sim", "{lenght_test_parametrize[:50]}"]', 'aa'])
def test_text_capacity_attest_responsible_name(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, capacity_attest=test_input) == False


def test_wrongtype_capacity_attest_responsible_name(client, datetime_to_use):    
    assert data_to_use(client, datetime_to_use, capacity_attest=123124) == False


####################################################################
# TEST CNES 
# establishment_solitc_cnes
# wrong type
# invalid cnes

@pytest.mark.parametrize("test_input", ['adsadad', 451236548])
def test_wrongtype_invalid_establishment_solitc_cnes(test_input, client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, establishment_solitc_cnes=test_input) == False



#################################################################
# TEST DATETIMES VARIABLES
# solicitation_datetime
# test wrong type
# test valid datetime

def test_wrongtype_solicitation_datetime(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, solicitation_datetime='bahabah') == False

def test_valid_solicitation_datetime(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, solicitation_datetime=datetime_to_use) == True


##################################################################
# TEST MARKABLE OPTIONS WITH TEXT
# filled_by
# patient_ethnicity
# previous_treatment
# test not exist option
# test all options in Upper Case
# test all options in lower Case
# test text without correct option
# test text with correct option
# test text empty
# test text with space
# test long text
# test short text
# test wrong text type 

def test_wrongtype_filled_by(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, filled_by=1231) == False

@pytest.mark.parametrize("test_input", [
    '''["WTAHST", "Other name", "{'cpf':'28445400070'}"]''',
    '''["OUTRO", "", "{'cpf':'28445400070'}"]''',
    '''["OUTRO", " ", "{'cpf':'28445400070'}"]''',
    f'''["OUTRO", "{lenght_test_parametrize[:3]}", "{"'cpf':'28445400070'"}"]''',
    f'''["OUTRO", "{lenght_test_parametrize[:45]}", "{"'cpf':'28445400070'"}"]''',
    '''["RESPONSAVEL", 123, "{'cpf':'28445400070'}"]''',
    '''["OUTRO", 123, "{'cpf':'28445400070'}"]''',
    '''["WTAHST", "Other name", "{'cpf':'28445400070'}"]''',
    '''["OUTRO", null, "{'cpf':'28445400070'}"]''',
    ])
def test_false_filled_by(test_input, client, datetime_to_use):
    # All options that are not supposed to pass
    assert data_to_use(client, datetime_to_use, filled_by=test_input) == False

@pytest.mark.parametrize("test_input", [
    '''["MEDICO", "Other name", "{'cpf':'28445400070'}"]''',
    '''["medico", "Other name", "{'cpf':'28445400070'}"]''',
    '''["PACIENTE", "Other name", "{'cpf':'28445400070'}"]''',
    '''["paciente", "Other name", "{'cpf':'28445400070'}"]''',
    '''["MAE", "Other name", "{'cpf':'28445400070'}"]''',
    '''["mae", "Other name", "{'cpf':'28445400070'}"]''',
    '''["RESPONSAVEL", "Other name", "{'cpf':'28445400070'}"]''',
    '''["responsavel", "Other name", "{'cpf':'28445400070'}"]''',
    '''["OUTRO", "Other name", "{'cpf':'28445400070'}"]''',
    '''["outro", "Other name", "{'cpf':'28445400070'}"]''',
    '''["MEDICO", "Other name", "{'cpf':'28445400070'}"]''',
    '''["MAE", "Other name", "{'cpf':'28445400070'}"]''',
    '''["MEDICO", null, "{'cpf':'28445400070'}"]''',
    '''["PACIENTE", null, "{'cpf':'28445400070'}"]''',
    '''["MAE", null, "{'cpf':'28445400070'}"]''',
    '''["RESPONSAVEL", null, "{'cpf':'28445400070'}"]''',
    '''["MEDICO", "  ", "{'cpf':'28445400070'}"]''',
    '''["PACIENTE", "", "{'cpf':'28445400070'}"]''',
    '''["MAE", "", "{'cpf':'28445400070'}"]''',
    '''["RESPONSAVEL", "", "{'cpf':'28445400070'}"]''',
    '''["MEDICO", " ", "{'cpf':'28445400070'}"]''',
    '''["PACIENTE", " ", "{'cpf':'28445400070'}"]''',
    '''["MAE", " ", "{'cpf':'28445400070'}"]''',
    '''["RESPONSAVEL", " ", "{'cpf':'28445400070'}"]''',
    f'''["MEDICO", "{lenght_test_parametrize[:3]}", "{"'cpf':'28445400070'"}"]''',
    f'''["PACIENTE", "{lenght_test_parametrize[:3]}", "{"'cpf':'28445400070'"}"]''',
    f'''["MAE", "{lenght_test_parametrize[:3]}", "{"'cpf':'28445400070'"}"]''',
    f'''["RESPONSAVEL", "{lenght_test_parametrize[:3]}", "{"'cpf':'28445400070'"}"]''',
    f'''["MEDICO", "{lenght_test_parametrize[:45]}", "{"'cpf':'28445400070'"}"]''',
    f'''["PACIENTE", "{lenght_test_parametrize[:45]}", "{"'cpf':'28445400070'"}"]''',
    f'''["MAE", "{lenght_test_parametrize[:45]}", "{"'cpf':'28445400070'"}"]''',
    f'''["RESPONSAVEL", "{lenght_test_parametrize[:45]}", "{"'cpf':'28445400070'"}"]'''
    ])
def test_true_filled_by(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, filled_by=test_input) == True

@pytest.mark.parametrize("test_input", [
    '["INFORMAR", null]',
    '["INFORMAR", ""]',
    '["INFORMAR", "  "]',
    f'["INFORMAR", "{lenght_test_parametrize[:3]}"]',
    f'["INFORMAR", "{lenght_test_parametrize[:35]}"]',
    1231,
    '["WTAHST", "Patient Ethnicity"]'
    ])
def test_false_patient_ethnicity(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, patient_ethnicity=test_input) == False


@pytest.mark.parametrize("test_input", [
    '["BRANCA", "Patient Ethnicity"]',
    '["branca", "Patient Ethnicity"]',
    '["PRETA", "Patient Ethnicity"]',
    '["preta", "Patient Ethnicity"]',
    '["PARDA", "Patient Ethnicity"]',
    '["parda", "Patient Ethnicity"]',
    '["AMARELA", "Patient Ethnicity"]',
    '["amarela", "Patient Ethnicity"]',
    '["INDIGENA", "Patient Ethnicity"]',
    '["indigena", "Patient Ethnicity"]',
    '["SEMINFO", "Patient Ethnicity"]',
    '["seminfo", "Patient Ethnicity"]',
    '["INFORMAR", "Patient Ethnicity"]',
    '["INFORMAR", "Patient Ethnicity"]',
    '["BRANCA", "Patient Ethnicity"]',
    '["PRETA", "Patient Ethnicity"]',
    '["PARDA", "Patient Ethnicity"]',
    '["AMARELA", "Patient Ethnicity"]',
    '["INDIGENA", "Patient Ethnicity"]',
    '["SEMINFO", "Patient Ethnicity"]',
    '["INFORMAR", "Patient Ethnicity"]',
    '["BRANCA", null]',
    '["PRETA", null]',
    '["PARDA", null]',
    '["AMARELA", null]',
    '["INDIGENA", null]',
    '["SEMINFO", null]',
    '["BRANCA", ""]',
    '["PRETA", ""]',
    '["PARDA", ""]',
    '["AMARELA", ""]',
    '["INDIGENA", ""]',
    '["SEMINFO", ""]',
    '["BRANCA", " "]',
    '["PRETA", "  "]',
    '["PARDA", "  "]',
    '["AMARELA", "  "]',
    '["INDIGENA", "  "]',
    '["SEMINFO", "  "]',
    f'["BRANCA", "{lenght_test_parametrize[:3]}"]',
    f'["PRETA", "{lenght_test_parametrize[:3]}"]',
    f'["PARDA", "{lenght_test_parametrize[:3]}"]',
    f'["AMARELA", "{lenght_test_parametrize[:3]}"]',
    f'["INDIGENA", "{lenght_test_parametrize[:3]}"]',
    f'["SEMINFO", "{lenght_test_parametrize[:3]}"]',
    f'["BRANCA", "{lenght_test_parametrize[:35]}"]',
    f'["PRETA", "{lenght_test_parametrize[:35]}"]',
    f'["PARDA", "{lenght_test_parametrize[:35]}"]',
    f'["AMARELA", "{lenght_test_parametrize[:35]}"]',
    f'["INDIGENA", "{lenght_test_parametrize[:35]}"]',
    f'["SEMINFO", "{lenght_test_parametrize[:35]}"]'
    ])
def test_true_patient_ethnicity(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, patient_ethnicity=test_input) == True

@pytest.mark.parametrize("test_input", [
    1231,
    '["WTAHST", "Patient Ethnicity"]',
    '["SIM", null]',
    '["SIM", " "]',
    f'["SIM", "{lenght_test_parametrize[:3]}"]',
    f'["SIM", "{lenght_test_parametrize[:172]}"]'
    ])
def test_false_previous_treatment(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, previous_treatment=test_input) == False

@pytest.mark.parametrize("test_input", [
    '["SIM", "Patient Ethnicity"]',
    '["sim", "Patient Ethnicity"]',
    '["SIM", "Patient Ethnicity"]',
    '["NAO", "Patient Ethnicity"]',
    '["NAO", null]',
    '["NAO", null]',
    '["NAO", " "]',
    f'["NAO", "{lenght_test_parametrize[:3]}"]',
    f'["NAO", "{lenght_test_parametrize[:170]}"]'
    ])
def test_true_previous_treatment(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, previous_treatment=test_input) == True


#############################################################################
# TEST BIG TEXT WITH LINE BRAKES
# anamnese
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

@pytest.mark.parametrize("test_input", [131, '', '   ', 'vlza', lenght_test_parametrize[:500]])
def test_anamnese(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, anamnese=test_input) == False

#############################################################################
# TEST STRING THAT CAN/CANNOT BE NULL
# diagnostic
# patient_email
# cid_10
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

@pytest.mark.parametrize("test_input", [123, 'aaa', lenght_test_parametrize[:86]])
def test_false_diagnostic(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, diagnostic=test_input) == False

@pytest.mark.parametrize("test_input", ['null' , '', '   '])
def test_true_diagnostic(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, diagnostic=test_input) == True

@pytest.mark.parametrize("test_input", [123, 'aaa', lenght_test_parametrize[:65]])
def test_false_patient_email(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, patient_email=test_input) == False

@pytest.mark.parametrize("test_input", ['', '   '])
def test_true_patient_email(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, patient_email=test_input) == True


@pytest.mark.parametrize("test_input", ['', '   ', 'aa', lenght_test_parametrize[:6]])
def test_cid_10(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, cid_10=test_input) == False

#################################################################################
# TEST INT VARIABLES CAN/CANNOT BE NULL
# patient_weight
# patient_height
# contacts_phonenumbers
# !!!!! TESTING
# wrong type
# test empty value
# test empty space
# short value
# long value  

@pytest.mark.parametrize("test_input", ['""', '"   "', 5875, '"ada"'])
def test_patient_weight(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, patient_weight=test_input) == False

@pytest.mark.parametrize("test_input", ['""', '"   "', 5875, '"ada"'])
def test_patient_height(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, patient_height=test_input) == False

@pytest.mark.parametrize("test_input", ['""', '"   "', '["9854894846", "98641984195156"]'])
def test_contacts_phonenumbers(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, contacts_phonenumbers=test_input) == False

#################################################################
# TEST DOCUMENTS CNS AND CPF
# prof_solicitor_document
# patient_document
# wrong type
# invalid cns
# invalid cpf
# wrong option


@pytest.mark.parametrize("test_input", [
    '451236548554',
    '{cns:"284123312123", rg: null, cpf: null}',
    '{cpf:"284123312123", rg: null, cns: null}',
    '{cpf:null, rg: null, cns: null}'
])
def test_prof_solicitor_document(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, prof_solicitor_document=test_input) == False

@pytest.mark.parametrize("test_input", [
    '451236548554',
    '{cns:"284123312123", rg: null, cpf: null}',
    '{cpf:"284123312123", rg: null, cns: null}',
    '{cpf:null, rg: null, cns: null}'
])
def test_patient_document(test_input, client, datetime_to_use):
    # All options that had to be success
    assert data_to_use(client, datetime_to_use, patient_document=test_input) == False


# TEST medicines
# test wront type
# test wront type medicine_name
# test wront type quant1month
# test wront type quant2month
# test wront type quant3month
# test empty value in keys
# test empty spaces in keys
# test empty value in medicineName
# test empty value in quant1month
# test empty value in quant2month
# test empty value in quant3month
# test empty spaces in medicineName
# test empty spaces in quant1month
# test empty spaces in quant2month
# test empty spaces in quant3month
# test more than limit dicts
# test long values in medicineName
# test long values in quant1month
# test long values in quant2month
# test long values in quant3month
# test short values in medicineName
# test short values in quant1month
# test short values in quant2month
# test short values in quant3month

def test_wrong_type_medicines(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines=123) == False

def test_wrong_type_medicine_name(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:234234, quant1month:"20 comp", quant2month:"15 comp", quant3month:"5 comp"}]') == False

def test_wrong_type_quant_1_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"234234", quant1month:541, quant2month:"15 comp", quant3month:"5 comp"}]') == False

def test_wrong_type_quant_2_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"234234", quant1month:"541", quant2month:649781, quant3month:"5 comp"}]') == False

def test_wrong_type_quant_3_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"234234", quant1month:"541", quant2month:"64981", quant3month:234234}]') == False

def test_empty_value_medicine_name(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"", quant1month:"541", quant2month:"64981", quant3month:"234234"}]') == False

def test_empty_value_quant_1_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"", quant2month:"64981", quant3month:"234234"}]') == False

def test_empty_value_quant_2_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"", quant3month:"234234"}]') == False

def test_empty_value_quant_3_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:""}]') == False

def test_empty_spaces_medicine_name(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"   ", quant1month:"541", quant2month:"64981", quant3month:"234234"}]') == False

def test_empty_spaces_quant_1_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"      ", quant2month:"64981", quant3month:"234234"}]') == False

def test_empty_spaces_quant_2_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"     ", quant3month:"234234"}]') == False

def test_empty_spaces_quant_3_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"      "}]') == False

def test_more_than_limit_dicts(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}, {medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}, {medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}, {medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}, {medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}, {medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}]') == False


def test_short_value_medicine_name(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"asd", quant1month:"541", quant2month:"64981", quant3month:"234234"}]') == False

def test_short_value_quant_1_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"", quant2month:"64981", quant3month:"234234"}]') == False

def test_short_value_quant_2_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"", quant3month:"234234"}]') == False

def test_short_value_quant_3_month(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:""}]') == False

def test_long_value_medicine_name(client, datetime_to_use, lenght_test):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"lenght_test", quant1month:"541", quant2month:"64981", quant3month:"234234"}]'.replace('lenght_test', lenght_test[:70])) == False

def test_long_value_quant_1_month(client, datetime_to_use, lenght_test):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"lenght_test", quant2month:"64981", quant3month:"234234"}]'.replace('lenght_test', lenght_test[:11])) == False

def test_long_value_quant_2_month(client, datetime_to_use, lenght_test):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"lenght_test", quant3month:"234234"}]'.replace('lenght_test', lenght_test[:11])) == False

def test_long_value_quant_3_month(client, datetime_to_use, lenght_test):
    assert data_to_use(client, datetime_to_use, medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"lenght_test"}]'.replace('lenght_test', lenght_test[:11])) == False

