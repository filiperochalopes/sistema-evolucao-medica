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

def test_empty_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name='') == False

def test_with_space_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name='  ') == False

def test_long_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name=lenght_test[:70]) == False

def test_short_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name='bro') == False

def test_wrongtype_establishment_solitc_name():    
    assert data_to_use(establishment_solitc_name=123124) == False

def test_empty_patient_name():    
    assert data_to_use(patient_name='') == False

def test_with_space_patient_name():    
    assert data_to_use(patient_name='  ') == False

def test_long_patient_name():    
    assert data_to_use(patient_name=lenght_test[:81]) == False

def test_short_patient_name():    
    assert data_to_use(patient_name='bro') == False

def test_wrongtype_patient_name():    
    assert data_to_use(patient_name=123124) == False

def test_empty_patient_mother_name():    
    assert data_to_use(patient_mother_name='') == False

def test_with_space_patient_mother_name():    
    assert data_to_use(patient_mother_name='  ') == False

def test_long_patient_mother_name():    
    assert data_to_use(patient_mother_name=lenght_test[:81]) == False

def test_short_patient_mother_name():    
    assert data_to_use(patient_mother_name='bro') == False

def test_wrongtype_patient_mother_name():    
    assert data_to_use(patient_mother_name=123124) == False

def test_empty_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='') == False

def test_with_space_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='  ') == False

def test_long_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=lenght_test[:50]) == False

def test_short_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='bro') == False

def test_wrongtype_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=123124) == False

def test_empty_capacity_attest_responsible_name():    
    assert data_to_use(capacity_attest=f'["sim", ""]') == False

def test_with_space_capacity_attest_responsible_name():    
    assert data_to_use(capacity_attest=f'["sim", " "]') == False

def test_long_capacity_attest_responsible_name():    
    assert data_to_use(capacity_attest=f'["sim", "{lenght_test[:50]}"]') == False

def test_short_capacity_attest_responsible_name():    
    assert data_to_use(capacity_attest='bro') == False

def test_wrongtype_capacity_attest_responsible_name():    
    assert data_to_use(capacity_attest=123124) == False


####################################################################
# TEST CNES 
# establishment_solitc_cnes
# wrong type
# invalid cnes


def test_wrongtype_establishment_solitc_cnes():
    assert data_to_use(establishment_solitc_cnes='adsadad') == False

def test_invalidcnes_establishment_solitc_cnes():
    assert data_to_use(establishment_solitc_cnes=451236548) == False


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

def test_notexistopiton_filled_by():
    assert data_to_use(filled_by='''["WTAHST", "Other name", "{'cpf':'28445400070'}"]''') == False

def test_medico_optionUpper_filled_by():
    assert data_to_use(filled_by='''["MEDICO", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_medico_optionLower_filled_by():
    assert data_to_use(filled_by='''["medico", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_paciente_optionUpper_filled_by():
    assert data_to_use(filled_by='''["PACIENTE", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_paciente_optionLower_filled_by():
    assert data_to_use(filled_by='''["paciente", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_mae_optionUpper_filled_by():
    assert data_to_use(filled_by='''["MAE", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_mae_optionLower_filled_by():
    assert data_to_use(filled_by='''["mae", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_responsavel_optionUpper_filled_by():
    assert data_to_use(filled_by='''["RESPONSAVEL", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_responsavel_optionLower_filled_by():
    assert data_to_use(filled_by='''["responsavel", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_outro_optionUpper_filled_by():
    assert data_to_use(filled_by='''["OUTRO", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_outro_optionLower_filled_by():
    assert data_to_use(filled_by='''
    ["outro", "Other name", "{'cpf':'28445400070'}"]
    ''') == True

def test_medico_with_text_filled_by():
    assert data_to_use(filled_by='''["MEDICO", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_paciente_with_text_filled_by():
    assert data_to_use(filled_by='''["PACIENTE", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_mae_with_text_filled_by():
    assert data_to_use(filled_by='''["MAE", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_responsavel_with_text_filled_by():
    assert data_to_use(filled_by='''["RESPONSAVEL", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_outro_with_text_filled_by():
    assert data_to_use(filled_by='''["OUTRO", "Other name", "{'cpf':'28445400070'}"]''') == True

def test_medico_without_text_filled_by():
    assert data_to_use(filled_by='''["MEDICO", null, "{'cpf':'28445400070'}"]''') == True

def test_paciente_without_text_filled_by():
    assert data_to_use(filled_by='''["PACIENTE", null, "{'cpf':'28445400070'}"]''') == True

def test_mae_without_text_filled_by():
    assert data_to_use(filled_by='''["MAE", null, "{'cpf':'28445400070'}"]''') == True

def test_responsavel_without_text_filled_by():
    assert data_to_use(filled_by='''["RESPONSAVEL", null, "{'cpf':'28445400070'}"]''') == True

def test_outro_without_text_filled_by():
    assert data_to_use(filled_by='''["OUTRO", null, "{'cpf':'28445400070'}"]''') == False

def test_medico_with_empty_text_filled_by():
    assert data_to_use(filled_by='''["MEDICO", "  ", "{'cpf':'28445400070'}"]''') == True

def test_paciente_with_empty_text_filled_by():
    assert data_to_use(filled_by='''["PACIENTE", "", "{'cpf':'28445400070'}"]''') == True

def test_mae_with_empty_text_filled_by():
    assert data_to_use(filled_by='''["MAE", "", "{'cpf':'28445400070'}"]''') == True

def test_responsavel_with_empty_text_filled_by():
    assert data_to_use(filled_by='''["RESPONSAVEL", "", "{'cpf':'28445400070'}"]''') == True

def test_outro_with_empty_text_filled_by():
    assert data_to_use(filled_by='''["OUTRO", "", "{'cpf':'28445400070'}"]''') == False

def test_medico_with_space_text_filled_by():
    assert data_to_use(filled_by='''["MEDICO", " ", "{'cpf':'28445400070'}"]''') == True

def test_paciente_with_space_text_filled_by():
    assert data_to_use(filled_by='''["PACIENTE", " ", "{'cpf':'28445400070'}"]''') == True

def test_mae_with_space_text_filled_by():
    assert data_to_use(filled_by='''["MAE", " ", "{'cpf':'28445400070'}"]''') == True

def test_responsavel_with_space_text_filled_by():
    assert data_to_use(filled_by='''["RESPONSAVEL", " ", "{'cpf':'28445400070'}"]''') == True

def test_outro_with_space_text_filled_by():
    assert data_to_use(filled_by='''["OUTRO", " ", "{'cpf':'28445400070'}"]''') == False

def test_medico_with_shorttext_filled_by():
    assert data_to_use(filled_by=f'''["MEDICO", "{lenght_test[:3]}", "{"'cpf':'28445400070'"}"]''') == True

def test_paciente_with_shorttext_filled_by():
    assert data_to_use(filled_by=f'''["PACIENTE", "{lenght_test[:3]}", "{"'cpf':'28445400070'"}"]''') == True

def test_mae_with_shorttext_filled_by():
    assert data_to_use(filled_by=f'''["MAE", "{lenght_test[:3]}", "{"'cpf':'28445400070'"}"]''') == True

def test_responsavel_with_shorttext_filled_by():
    assert data_to_use(filled_by=f'''["RESPONSAVEL", "{lenght_test[:3]}", "{"'cpf':'28445400070'"}"]''') == True

def test_outro_with_shorttext_filled_by():
    assert data_to_use(filled_by=f'''["OUTRO", "{lenght_test[:3]}", "{"'cpf':'28445400070'"}"]''') == False

def test_medico_with_longtext_filled_by():
    assert data_to_use(filled_by=f'''["MEDICO", "{lenght_test[:45]}", "{"'cpf':'28445400070'"}"]''') == True

def test_paciente_with_longtext_filled_by():
    assert data_to_use(filled_by=f'''["PACIENTE", "{lenght_test[:45]}", "{"'cpf':'28445400070'"}"]''') == True

def test_mae_with_longtext_filled_by():
    assert data_to_use(filled_by=f'''["MAE", "{lenght_test[:45]}", "{"'cpf':'28445400070'"}"]''') == True

def test_responsavel_with_longtext_filled_by():
    assert data_to_use(filled_by=f'''["RESPONSAVEL", "{lenght_test[:45]}", "{"'cpf':'28445400070'"}"]''') == True

def test_outro_with_longtext_filled_by():
    assert data_to_use(filled_by=f'''["OUTRO", "{lenght_test[:45]}", "{"'cpf':'28445400070'"}"]''') == False

def test_responsavel_with_wrong_type_text_filled_by():
    assert data_to_use(filled_by='''["RESPONSAVEL", 123, "{'cpf':'28445400070'}"]''') == True

def test_outro_with_wrong_type_text_filled_by():
    assert data_to_use(filled_by='''["OUTRO", 123, "{'cpf':'28445400070'}"]''') == False

def test_wrongtype_patient_ethnicity():
    assert data_to_use(patient_ethnicity=1231) == False

def test_notexistopiton_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["WTAHST", "Patient Ethnicity"]') == False

def test_branca_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["BRANCA", "Patient Ethnicity"]') == True

def test_branca_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["branca", "Patient Ethnicity"]') == True

def test_preta_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PRETA", "Patient Ethnicity"]') == True

def test_preta_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["preta", "Patient Ethnicity"]') == True

def test_parda_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PARDA", "Patient Ethnicity"]') == True

def test_parda_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["parda", "Patient Ethnicity"]') == True

def test_amarela_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["AMARELA", "Patient Ethnicity"]') == True

def test_amarela_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["amarela", "Patient Ethnicity"]') == True

def test_indigena_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["INDIGENA", "Patient Ethnicity"]') == True

def test_indigena_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["indigena", "Patient Ethnicity"]') == True

def test_seminfo_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["SEMINFO", "Patient Ethnicity"]') == True

def test_seminfo_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["seminfo", "Patient Ethnicity"]') == True

def test_branca_with_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["BRANCA", "Patient Ethnicity"]') == True

def test_preta_with_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PRETA", "Patient Ethnicity"]') == True

def test_parda_with_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PARDA", "Patient Ethnicity"]') == True

def test_amarela_with_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["AMARELA", "Patient Ethnicity"]') == True

def test_indigena_with_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["INDIGENA", "Patient Ethnicity"]') == True

def test_seminfo_with_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["SEMINFO", "Patient Ethnicity"]') == True

def test_branca_without_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["BRANCA", null]') == False

def test_preta_without_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PRETA", null]') == False

def test_parda_without_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PARDA", null]') == False

def test_amarela_without_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["AMARELA", null]') == False

def test_indigena_without_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["INDIGENA", null]') == False

def test_seminfo_without_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["SEMINFO", null]') == True

def test_branca_with_empty_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["BRANCA", ""]') == False

def test_preta_with_empty_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PRETA", ""]') == False

def test_parda_with_empty_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PARDA", ""]') == False

def test_amarela_with_empty_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["AMARELA", ""]') == False

def test_indigena_with_empty_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["INDIGENA", ""]') == False

def test_seminfo_with_empty_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["SEMINFO", ""]') == True

def test_branca_with_space_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["BRANCA", " "]') == True

def test_preta_with_space_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PRETA", "  "]') == True

def test_parda_with_space_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PARDA", "  "]') == True

def test_amarela_with_space_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["AMARELA", "  "]') == True

def test_indigena_with_space_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["INDIGENA", "  "]') == True

def test_seminfo_with_space_text_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["SEMINFO", "  "]') == True

def test_branca_with_shorttext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["BRANCA", "{lenght_test[:3]}"]') == False

def test_preta_with_shorttext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["PRETA", "{lenght_test[:3]}"]') == False

def test_parda_with_shorttext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["PARDA", "{lenght_test[:3]}"]') == False

def test_amarela_with_shorttext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["AMARELA", "{lenght_test[:3]}"]') == False

def test_indigena_with_shorttext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["INDIGENA", "{lenght_test[:3]}"]') == False

def test_seminfo_with_shorttext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["SEMINFO", "{lenght_test[:3]}"]') == True

def test_branca_with_longtext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["BRANCA", "{lenght_test[:35]}"]') == False

def test_preta_with_longtext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["PRETA", "{lenght_test[:35]}"]') == False

def test_parda_with_longtext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["PARDA", "{lenght_test[:35]}"]') == False

def test_amarela_with_longtext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["AMARELA", "{lenght_test[:35]}"]') == False

def test_indigena_with_longtext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["INDIGENA", "{lenght_test[:35]}"]') == False

def test_seminfo_with_longtext_patient_ethnicity():
    assert data_to_use(patient_ethnicity=f'["SEMINFO", "{lenght_test[:35]}"]') == True


def test_wrongtype_previous_treatment():
    assert data_to_use(previous_treatment=1231) == False

def test_notexistopiton_previous_treatment():
    assert data_to_use(previous_treatment='["WTAHST", "Patient Ethnicity"]') == False

def test_sim_optionUpper_previous_treatment():
    assert data_to_use(previous_treatment='["SIM", "Patient Ethnicity"]') == True

def test_sim_optionLower_previous_treatment():
    assert data_to_use(previous_treatment='["sim", "Patient Ethnicity"]') == True

def test_sim_with_text_previous_treatment():
    assert data_to_use(previous_treatment='["SIM", "Patient Ethnicity"]') == True

def test_nao_with_text_previous_treatment():
    assert data_to_use(previous_treatment='["NAO", "Patient Ethnicity"]') == True

def test_sim_without_text_previous_treatment():
    assert data_to_use(previous_treatment='["SIM", null]') == False

def test_nao_without_text_previous_treatment():
    assert data_to_use(previous_treatment='["NAO", null]') == True

def test_sim_with_empty_previous_treatment():
    assert data_to_use(previous_treatment='["SIM", null]') == False

def test_nao_with_empty_previous_treatment():
    assert data_to_use(previous_treatment='["NAO", null]') == True

def test_sim_with_space_text_previous_treatment():
    assert data_to_use(previous_treatment='["SIM", " "]') == False

def test_nao_with_space_text_previous_treatment():
    assert data_to_use(previous_treatment='["NAO", " "]') == True

def test_sim_with_shorttext_previous_treatment():
    assert data_to_use(previous_treatment=f'["SIM", "{lenght_test[:3]}"]') == False

def test_nao_with_shorttext_previous_treatment():
    assert data_to_use(previous_treatment=f'["NAO", "{lenght_test[:3]}"]') == True

def test_sim_with_longtext_previous_treatment():
    assert data_to_use(previous_treatment=f'["SIM", "{lenght_test[:172]}"]') == False

def test_nao_with_longtext_previous_treatment():
    assert data_to_use(previous_treatment=f'["NAO", "{lenght_test[:170]}"]') == True


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
    assert data_to_use(patient_weight='131') == False

def test_empty_value_patient_weight():
    assert data_to_use(patient_weight='') == False

def test_empty_spaces_patient_weight():
    assert data_to_use(patient_weight='    ') == False

def test_longValue_patient_weight():
    assert data_to_use(patient_weight=5487) == False


def test_empty_value_patient_height():
    assert data_to_use(patient_height='') == False

def test_empty_spaces_patient_height():
    assert data_to_use(patient_height='    ') == False

def test_longValue_patient_height():
    assert data_to_use(patient_height=5487) == False

def test_empty_value_contacts_phonenumbers():
    assert data_to_use(contacts_phonenumbers='') == False

def test_empty_spaces_contacts_phonenumbers():
    assert data_to_use(contacts_phonenumbers='    ') == False

def test_longValue_contacts_phonenumbers():
    assert data_to_use(contacts_phonenumbers=[9854894846, 98641984195156]) == False




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
    assert data_to_use(prof_solicitor_document={'CNS':284123312123}) == False

def test_invalidccpf_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document={'CPF':284123312123}) == False

def test_wrongoption_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document={'BBB':284123312123}) == False

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
    assert data_to_use(medicines=[{"medicineName":234234, "quant1month":"20 comp", "quant2month":"15 comp", "quant3month":"5 comp"}]) == False

def test_wrong_type_quant_1_month():
    assert data_to_use(medicines=[{"medicineName":'234234', "quant1month":541, "quant2month":"15 comp", "quant3month":"5 comp"}]) == False

def test_wrong_type_quant_2_month():
    assert data_to_use(medicines=[{"medicineName":'234234', "quant1month":'541', "quant2month":649781, "quant3month":"5 comp"}]) == False

def test_wrong_type_quant_3_month():
    assert data_to_use(medicines=[{"medicineName":'234234', "quant1month":'541', "quant2month":'64981', "quant3month":234234}]) == False

def test_empty_value_keys_medicines():
    assert data_to_use(medicines=[{"":'234234', "":'541', "quant2month":'64981', "":234234}]) == False

def test_empty_spaces_keys_medicines():
    assert data_to_use(medicines=[{" ":'234234', " ":'541', "quant2month":'64981', " ":234234}]) == False

def test_empty_value_medicine_name():
    assert data_to_use(medicines=[{"medicineName":'', "quant1month":'541', "quant2month":'64981', "quant3month":'234234'}]) == False

def test_empty_value_quant_1_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'', "quant2month":'64981', "quant3month":'234234'}]) == False

def test_empty_value_quant_2_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'', "quant3month":'234234'}]) == False

def test_empty_value_quant_3_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'adasdasda', "quant3month":''}]) == False

def test_empty_spaces_medicine_name():
    assert data_to_use(medicines=[{"medicineName":'   ', "quant1month":'541', "quant2month":'64981', "quant3month":'234234'}]) == False

def test_empty_spaces_quant_1_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'      ', "quant2month":'64981', "quant3month":'234234'}]) == False

def test_empty_spaces_quant_2_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'     ', "quant3month":'234234'}]) == False

def test_empty_spaces_quant_3_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'adasdasda', "quant3month":'      '}]) == False

def test_more_than_limit_dicts():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'adasdasda', "quant3month":'asdadasd'}, {"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'adasdasda', "quant3month":'asdadasd'}, {"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'adasdasda', "quant3month":'asdadasd'}, {"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'adasdasda', "quant3month":'asdadasd'}, {"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'adasdasda', "quant3month":'asdadasd'}, {"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'adasdasda', "quant3month":'asdadasd'}]) == False


def test_short_value_medicine_name():
    assert data_to_use(medicines=[{"medicineName":'asd', "quant1month":'541', "quant2month":'64981', "quant3month":'234234'}]) == False

def test_short_value_quant_1_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'', "quant2month":'64981', "quant3month":'234234'}]) == False

def test_short_value_quant_2_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'', "quant3month":'234234'}]) == False

def test_short_value_quant_3_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'adasdasda', "quant3month":''}]) == False

def test_long_value_medicine_name():
    assert data_to_use(medicines=[{"medicineName":lenght_test[:70], "quant1month":'541', "quant2month":'64981', "quant3month":'234234'}]) == False

def test_long_value_quant_1_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":lenght_test[:11], "quant2month":'64981', "quant3month":'234234'}]) == False

def test_long_value_quant_2_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":lenght_test[:11], "quant3month":'234234'}]) == False

def test_long_value_quant_3_month():
    assert data_to_use(medicines=[{"medicineName":'1asdasdasd', "quant1month":'123123', "quant2month":'adasdasda', "quant3month":lenght_test[:11]}]) == False

