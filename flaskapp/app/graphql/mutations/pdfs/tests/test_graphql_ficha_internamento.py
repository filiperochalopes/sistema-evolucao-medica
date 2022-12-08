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
document_datetime_to_use = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

# Select your transport with ag graphql url endpoint
transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)


def data_to_use(document_datetime=document_datetime_to_use, patient_name="Patient Name",patient_cns='928976954930007',patient_birthday=datetime_to_use,patient_sex='F',patient_mother_name="Patient Mother Name",patient_document='{cpf: "28445400070",cns: null,rg: null}',patient_adress='pacient street, 43, paciten, USA',patient_phonenumber='44387694628', patient_drug_allergies='Penicillin, Aspirin, Ibuprofen, Anticonvulsants.', patient_comorbidities='Heart disease, High blood pressure, Diabetes, Cerebrovascular disease.',current_illness_history='Current illnes hsitoryaaaaaaaaaaa',initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral',doctor_name='Doctor Name',doctor_cns='928976954930007',doctor_crm='CRM/UF 123456',patient_adress_number=123456,patient_adress_neigh='Patient Neighborhood',patient_adress_city='Patient city',patient_adress_uf='sp',patient_adress_cep='12345678',patient_nationality='Brasileira',patient_estimate_weight=123,has_additional_health_insurance='SIM'):
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
def test_answer_with_all_fields():
    """Test fill ficha internamento with all data correct"""
    assert data_to_use() == True


def test_awnser_with_only_required_data():
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

def test_validrg_patient_document():
    assert data_to_use(patient_document='{cpf: null,cns: null,rg: "928976954930007"}') == True

def test_validcpf_patient_document():
    assert data_to_use(patient_document='{cpf: "28445400070",cns: null,rg: null}') == True


#################################################################
# TEST DATETIMES VARIABLES
# documentDatetime
# patient_birthday
# autorizaton_datetime
# test wrong type

def test_valid_documentDatetime():
    assert data_to_use(document_datetime=document_datetime_to_use) == True

def test_valid_patient_birthday():
    assert data_to_use(patient_birthday=datetime_to_use) == True

##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# has_additional_health_insurance
# test wrong type
# test not exist option
# test all options in Upper Case
# test all options in lower Case

def test_M_optionUpper_patient_sex():
    assert data_to_use(patient_sex='M') == True

def test_M_optionLower_patient_sex():
    assert data_to_use(patient_sex='m') == True

def test_F_optionUpper_patient_sex():
    assert data_to_use(patient_sex='F') == True

def test_F_optionLower_patient_sex():
    assert data_to_use(patient_sex='f') == True

def test_True_option_has_additional_health_insurance():
    assert data_to_use(has_additional_health_insurance='SIM') == True

def test_False_option_has_additional_health_insurance():
    assert data_to_use(has_additional_health_insurance='NAO') == True

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


def test_AC_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='AC') == True

def test_AC_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='ac') == True

def test_AL_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='AL') == True

def test_AL_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='al') == True

def test_AP_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='AP') == True

def test_AP_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='ap') == True

def test_AM_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='AM') == True

def test_AM_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='am') == True

def test_BA_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='BA') == True

def test_BA_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='ba') == True

def test_CE_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='CE') == True

def test_CE_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='ce') == True

def test_DF_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='DF') == True

def test_DF_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='df') == True

def test_ES_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='ES') == True

def test_ES_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='es') == True

def test_GO_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='GO') == True

def test_GO_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='go') == True

def test_MA_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='MA') == True

def test_MA_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='ma') == True

def test_MS_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='MS') == True

def test_MS_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='ms') == True

def test_MT_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='MT') == True

def test_MT_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='mt') == True

def test_MG_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='MG') == True

def test_MG_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='mg') == True

def test_PA_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='PA') == True

def test_PA_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='pa') == True

def test_PB_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='PB') == True

def test_PB_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='pb') == True

def test_PR_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='PR') == True

def test_PR_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='pr') == True

def test_PE_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='PE') == True

def test_PE_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='pe') == True

def test_PI_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='PI') == True

def test_PI_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='pi') == True

def test_RJ_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='RJ') == True

def test_RJ_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='rj') == True

def test_RN_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='RN') == True

def test_RN_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='rn') == True

def test_RS_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='RS') == True

def test_RS_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='rs') == True

def test_RO_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='RO') == True

def test_RO_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='ro') == True

def test_RR_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='RR') == True

def test_RR_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='rr') == True

def test_SC_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='SC') == True

def test_SC_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='sc') == True

def test_SP_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='SP') == True

def test_SP_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='sp') == True

def test_SE_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='SE') == True

def test_SE_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='se') == True

def test_TO_optionUpper_patient_adress_uf():
    assert data_to_use(patient_adress_uf='TO') == True

def test_TO_optionLower_patient_adress_uf():
    assert data_to_use(patient_adress_uf='to') == True


#################################################################################
# TEST CNS
# patient_cns
# doctor_cns
# wrong type
# valid
# invalid
# empty send

def test_valid_patient_cns():
    assert data_to_use(patient_cns='928976954930007') == True

def test_valid_doctor_cns():
    assert data_to_use(doctor_cns='928976954930007') == True

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

def test_shortValue_patient_estimate_weight():
    assert data_to_use(patient_estimate_weight=123) == True

