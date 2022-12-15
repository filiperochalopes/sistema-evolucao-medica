from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
from app.env import GRAPHQL_MUTATION_QUERY_URL
import pytest

global lenght_test
lenght_test = ''
for x in range(0, 1100):
    lenght_test += str(x)

datetime_to_use = datetime.datetime.now().strftime('%d/%m/%Y')

# Select your transport with ag graphql url endpoint
transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

def data_to_use(establishment_solitc_name='Establishment Solicit Name',
establishment_solitc_cnes=1234567,
patient_name='Patient Name',
patient_mother_name='Patient Mother Name',
patient_weight=142,
patient_height=180,
cid_10='A123',
anamnese="Anamnese",
prof_solicitor_name="Professional Solicitor Name",
solicitation_datetime=datetime_to_use,
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
def test_with_data_in_function():
    assert data_to_use() == True

def test_answer_with_all_fields():
    assert data_to_use() == True

def test_awnser_with_only_required_data():
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
def test_empty_value_establishment_solitc_name(test_input):
    assert data_to_use(establishment_solitc_name=test_input) == False

@pytest.mark.parametrize("test_input", [lenght_test[:70], lenght_test[:1]])
def test_text_establishment_solitc_name(test_input):
    assert data_to_use(establishment_solitc_name=test_input) == False

def test_wrongtype_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name=123124) == False

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_patient_name(test_input):
    assert data_to_use(patient_name=test_input) == False

@pytest.mark.parametrize("test_input", [lenght_test[:81], lenght_test[:1]])
def test_text_patient_name(test_input):
    assert data_to_use(patient_name=test_input) == False

def test_wrongtype_patient_name():    
    assert data_to_use(patient_name=123124) == False

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_patient_mother_name(test_input):
    assert data_to_use(patient_mother_name=test_input) == False

@pytest.mark.parametrize("test_input", [lenght_test[:81], lenght_test[:1]])
def test_text_patient_mother_name(test_input):
    assert data_to_use(patient_mother_name=test_input) == False

def test_wrongtype_patient_mother_name():    
    assert data_to_use(patient_mother_name=123124) == False

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_prof_solicitor_name(test_input):
    assert data_to_use(prof_solicitor_name=test_input) == False

@pytest.mark.parametrize("test_input", [lenght_test[:50], lenght_test[:1]])
def test_text_prof_solicitor_name(test_input):
    assert data_to_use(prof_solicitor_name=test_input) == False

def test_wrongtype_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=123124) == False

@pytest.mark.parametrize("test_input", ['["sim", ""]', '["sim", " "]', f'["sim", "{lenght_test[:50]}"]', 'aa'])
def test_text_capacity_attest_responsible_name(test_input):
    assert data_to_use(capacity_attest=test_input) == False

def test_wrongtype_capacity_attest_responsible_name():    
    assert data_to_use(capacity_attest=123124) == False


####################################################################
# TEST CNES 
# establishment_solitc_cnes
# wrong type
# invalid cnes

@pytest.mark.parametrize("test_input", ['adsadad', 451236548])
def test_wrongtype_invalid_establishment_solitc_cnes(test_input):
    assert data_to_use(establishment_solitc_cnes=test_input) == False



#################################################################
# TEST DATETIMES VARIABLES
# solicitation_datetime
# test wrong type
# test valid datetime

def test_wrongtype_solicitation_datetime():
    assert data_to_use(solicitation_datetime='bahabah') == False

def test_valid_solicitation_datetime():
    assert data_to_use(solicitation_datetime=datetime_to_use) == True


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

def test_wrongtype_filled_by():
    assert data_to_use(filled_by=1231) == False

@pytest.mark.parametrize("test_input", [
    '''["WTAHST", "Other name", "{'cpf':'28445400070'}"]''',
    '''["OUTRO", "", "{'cpf':'28445400070'}"]''',
    '''["OUTRO", " ", "{'cpf':'28445400070'}"]''',
    f'''["OUTRO", "{lenght_test[:3]}", "{"'cpf':'28445400070'"}"]''',
    f'''["OUTRO", "{lenght_test[:45]}", "{"'cpf':'28445400070'"}"]''',
    '''["RESPONSAVEL", 123, "{'cpf':'28445400070'}"]''',
    '''["OUTRO", 123, "{'cpf':'28445400070'}"]''',
    '''["WTAHST", "Other name", "{'cpf':'28445400070'}"]'''
    '''["OUTRO", null, "{'cpf':'28445400070'}"]''',
    ])
def test_false_filled_by(test_input):
    # All options that are not supposed to pass
    assert data_to_use(filled_by=test_input) == False

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
    f'''["MEDICO", "{lenght_test[:3]}", "{"'cpf':'28445400070'"}"]''',
    f'''["PACIENTE", "{lenght_test[:3]}", "{"'cpf':'28445400070'"}"]''',
    f'''["MAE", "{lenght_test[:3]}", "{"'cpf':'28445400070'"}"]''',
    f'''["RESPONSAVEL", "{lenght_test[:3]}", "{"'cpf':'28445400070'"}"]''',
    f'''["MEDICO", "{lenght_test[:45]}", "{"'cpf':'28445400070'"}"]''',
    f'''["PACIENTE", "{lenght_test[:45]}", "{"'cpf':'28445400070'"}"]''',
    f'''["MAE", "{lenght_test[:45]}", "{"'cpf':'28445400070'"}"]''',
    f'''["RESPONSAVEL", "{lenght_test[:45]}", "{"'cpf':'28445400070'"}"]'''
    ])
def test_true_filled_by(test_input):
    # All options that had to be success
    assert data_to_use(filled_by=test_input) == True

@pytest.mark.parametrize("test_input", [
    '["INFORMAR", null]',
    '["INFORMAR", ""]',
    '["INFORMAR", "  "]',
    f'["INFORMAR", "{lenght_test[:3]}"]',
    f'["INFORMAR", "{lenght_test[:35]}"]',
    1231,
    '["WTAHST", "Patient Ethnicity"]'
    ])
def test_false_patient_ethnicity(test_input):
    # All options that had to be success
    assert data_to_use(patient_ethnicity=test_input) == False


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
    f'["BRANCA", "{lenght_test[:3]}"]',
    f'["PRETA", "{lenght_test[:3]}"]',
    f'["PARDA", "{lenght_test[:3]}"]',
    f'["AMARELA", "{lenght_test[:3]}"]',
    f'["INDIGENA", "{lenght_test[:3]}"]',
    f'["SEMINFO", "{lenght_test[:3]}"]',
    f'["BRANCA", "{lenght_test[:35]}"]',
    f'["PRETA", "{lenght_test[:35]}"]',
    f'["PARDA", "{lenght_test[:35]}"]',
    f'["AMARELA", "{lenght_test[:35]}"]',
    f'["INDIGENA", "{lenght_test[:35]}"]',
    f'["SEMINFO", "{lenght_test[:35]}"]'
    ])
def test_true_patient_ethnicity(test_input):
    # All options that had to be success
    assert data_to_use(patient_ethnicity=test_input) == True

@pytest.mark.parametrize("test_input", [
    1231,
    '["WTAHST", "Patient Ethnicity"]',
    '["SIM", null]',
    '["SIM", " "]',
    f'["SIM", "{lenght_test[:3]}"]',
    f'["SIM", "{lenght_test[:172]}"]'
    ])
def test_false_previous_treatment(test_input):
    # All options that had to be success
    assert data_to_use(previous_treatment=test_input) == False

@pytest.mark.parametrize("test_input", [
    '["SIM", "Patient Ethnicity"]',
    '["sim", "Patient Ethnicity"]',
    '["SIM", "Patient Ethnicity"]',
    '["NAO", "Patient Ethnicity"]',
    '["NAO", null]',
    '["NAO", null]',
    '["NAO", " "]',
    f'["NAO", "{lenght_test[:3]}"]',
    f'["NAO", "{lenght_test[:170]}"]'
    ])
def test_true_previous_treatment(test_input):
    # All options that had to be success
    assert data_to_use(previous_treatment=test_input) == True


#############################################################################
# TEST BIG TEXT WITH LINE BRAKES
# anamnese
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

def test_wrong_type_anamnese():
    assert data_to_use(anamnese=131) == False

def test_empty_value_anamnese():
    assert data_to_use(anamnese='') == False

def test_empty_spaces_anamnese():
    assert data_to_use(anamnese='    ') == False

def test_shortText_anamnese():
    assert data_to_use(anamnese='abla') == False

def test_more_than_limit_anamnese():
    assert data_to_use(anamnese=lenght_test[:500]) == False


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

def test_wrong_type_diagnostic():
    assert data_to_use(diagnostic=123) == False

def test_empty_value_diagnostic():
    assert data_to_use(diagnostic='null') == True

def test_empty_spaces_diagnostic():
    assert data_to_use(diagnostic='    ') == True

def test_longValue_diagnostic():
    assert data_to_use(diagnostic=lenght_test[:86]) == False

def test_shortValue_diagnostic():
    assert data_to_use(diagnostic='aaa') == False

def test_wrong_type_patient_email():
    assert data_to_use(patient_email=123) == False

def test_empty_value_patient_email():
    assert data_to_use(patient_email=' ') == True

def test_empty_spaces_patient_email():
    assert data_to_use(patient_email='    ') == True

def test_longValue_patient_email():
    assert data_to_use(patient_email=lenght_test[:65]) == False

def test_shortValue_patient_email():
    assert data_to_use(patient_email='aaa') == False

def test_empty_value_cid_10():
    assert data_to_use(cid_10=' ') == False

def test_empty_spaces_cid_10():
    assert data_to_use(cid_10='    ') == False

def test_longValue_cid_10():
    assert data_to_use(cid_10=lenght_test[:6]) == False

def test_shortValue_cid_10():
    assert data_to_use(cid_10='aa') == False

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

def test_wrong_type_patient_weight():
    assert data_to_use(patient_weight='"asd"') == False

def test_empty_value_patient_weight():
    assert data_to_use(patient_weight='""') == False

def test_empty_spaces_patient_weight():
    assert data_to_use(patient_weight='"   "') == False

def test_longValue_patient_weight():
    assert data_to_use(patient_weight=5487) == False

def test_empty_value_patient_height():
    assert data_to_use(patient_height='""') == False

def test_empty_spaces_patient_height():
    assert data_to_use(patient_height='"  "') == False

def test_longValue_patient_height():
    assert data_to_use(patient_height=5487) == False

def test_empty_value_contacts_phonenumbers():
    assert data_to_use(contacts_phonenumbers='""') == False

def test_empty_spaces_contacts_phonenumbers():
    assert data_to_use(contacts_phonenumbers='"   "') == False

def test_longValue_contacts_phonenumbers():
    assert data_to_use(contacts_phonenumbers='["9854894846", "98641984195156"]') == False




#################################################################
# TEST DOCUMENTS CNS AND CPF
# prof_solicitor_document
# patient_document
# wrong type
# invalid cns
# invalid cpf
# wrong option

def test_wrongtype_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document='451236548554') == False

def test_invalidcns_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document='{cns:"284123312123", rg: null, cpf: null}') == False

def test_invalidccpf_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document='{cpf:"284123312123", rg: null, cns: null}') == False

def test_wrongoption_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document='{cpf:null, rg: null, cns: null}') == False

def test_wrongtype_patient_document():
    assert data_to_use(patient_document='451236548554') == False

def test_invalidcns_patient_document():
    assert data_to_use(patient_document='{cns:"284123312123", rg: null, cpf: null}') == False

def test_invalidccpf_patient_document():
    assert data_to_use(patient_document='{cpf:"284123312123", rg: null, cns: null}') == False

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

def test_wrong_type_medicines():
    assert data_to_use(medicines=123) == False

def test_wrong_type_medicines():
    assert data_to_use(medicines=123) == False

def test_wrong_type_medicine_name():
    assert data_to_use(medicines='[{medicineName:234234, quant1month:"20 comp", quant2month:"15 comp", quant3month:"5 comp"}]') == False

def test_wrong_type_quant_1_month():
    assert data_to_use(medicines='[{medicineName:"234234", quant1month:541, quant2month:"15 comp", quant3month:"5 comp"}]') == False

def test_wrong_type_quant_2_month():
    assert data_to_use(medicines='[{medicineName:"234234", quant1month:"541", quant2month:649781, quant3month:"5 comp"}]') == False

def test_wrong_type_quant_3_month():
    assert data_to_use(medicines='[{medicineName:"234234", quant1month:"541", quant2month:"64981", quant3month:234234}]') == False

def test_empty_value_medicine_name():
    assert data_to_use(medicines='[{medicineName:"", quant1month:"541", quant2month:"64981", quant3month:"234234"}]') == False

def test_empty_value_quant_1_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"", quant2month:"64981", quant3month:"234234"}]') == False

def test_empty_value_quant_2_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"", quant3month:"234234"}]') == False

def test_empty_value_quant_3_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:""}]') == False

def test_empty_spaces_medicine_name():
    assert data_to_use(medicines='[{medicineName:"   ", quant1month:"541", quant2month:"64981", quant3month:"234234"}]') == False

def test_empty_spaces_quant_1_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"      ", quant2month:"64981", quant3month:"234234"}]') == False

def test_empty_spaces_quant_2_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"     ", quant3month:"234234"}]') == False

def test_empty_spaces_quant_3_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"      "}]') == False

def test_more_than_limit_dicts():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}, {medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}, {medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}, {medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}, {medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}, {medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"asdadasd"}]') == False


def test_short_value_medicine_name():
    assert data_to_use(medicines='[{medicineName:"asd", quant1month:"541", quant2month:"64981", quant3month:"234234"}]') == False

def test_short_value_quant_1_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"", quant2month:"64981", quant3month:"234234"}]') == False

def test_short_value_quant_2_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"", quant3month:"234234"}]') == False

def test_short_value_quant_3_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:""}]') == False

def test_long_value_medicine_name():
    assert data_to_use(medicines='[{medicineName:"lenght_test", quant1month:"541", quant2month:"64981", quant3month:"234234"}]'.replace('lenght_test', lenght_test[:70])) == False

def test_long_value_quant_1_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"lenght_test", quant2month:"64981", quant3month:"234234"}]'.replace('lenght_test', lenght_test[:11])) == False

def test_long_value_quant_2_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"lenght_test", quant3month:"234234"}]'.replace('lenght_test', lenght_test[:11])) == False

def test_long_value_quant_3_month():
    assert data_to_use(medicines='[{medicineName:"1asdasdasd", quant1month:"123123", quant2month:"adasdasda", quant3month:"lenght_test"}]'.replace('lenght_test', lenght_test[:11])) == False

