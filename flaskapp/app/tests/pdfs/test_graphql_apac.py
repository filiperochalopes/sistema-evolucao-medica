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


def data_to_use(establishment_solitc_name='Establishment Solicit Name',establishment_solitc_cnes=1234567,patient_name='Patient Name',patient_cns="928976954930007",patient_sex='M',patient_birthday=datetime_to_use, patient_adress_city='Patient Adress City',main_procedure='{name: "teste procedimento",code: "hkmaug347s",quant: 1}',patient_mother_name='Patient Mother Name',patient_mother_phonenumber='5286758957', patient_responsible_name='Patient Responsible Name', patient_responsible_phonenumber='5465981345', patient_adress='Patient Adress',patient_color='Branca',patient_ethnicity='Indigena',patient_adress_uf='BA',patient_adressCEP='86425910', document_chart_number='12345',patient_adress_city_ibge_code=4528765,procedure_justification_description='Procedure Justification Description', prodedure_justification_main_cid_10='A98', prodedure_justification_sec_cid_10='A01', procedure_justification_associated_cause_cid_10='A45',procedure_justification_comments='Procedure Justification Comments',establishment_exec_name='Establishment Exec Name', establishment_exec_cnes=7654321,prof_solicitor_document='{cns: "928976954930007",cpf: null,rg: null}', prof_solicitor_name='Profissional Solicit Name',solicitation_datetime=datetime_to_use,signature_datetime=datetime_to_use,validity_period_start=datetime_to_use,validity_period_end=datetime_to_use,autorization_prof_name='Autorization Professional Name', emission_org_code='Cod121234',autorizaton_prof_document='{cns: "928976954930007",cpf: null,rg: null}', autorizaton_datetime=datetime_to_use,secondaries_procedures='[{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "segundo",code: "hkmhsa3s23",quant: 4}]'):
    request_string = """
        mutation{
            generatePdf_Apac("""

    campos_string = f"""
    establishmentSolitcName: "{establishment_solitc_name}",
    establishmentSolitcCnes: {establishment_solitc_cnes},
    patientName: "{patient_name}",
    patientCns: "{patient_cns}",
    patientSex: "{patient_sex}",
    patientBirthday: "{patient_birthday}",
    patientAdressCity: "{patient_adress_city}",
    mainProcedure: {main_procedure},
    secondariesProcedures: {secondaries_procedures},
    patientMotherName: "{patient_mother_name}",
    patientMotherPhonenumber: "{patient_mother_phonenumber}",
    patientResponsibleName: "{patient_responsible_name}",
    patientResponsiblePhonenumber: "{patient_responsible_phonenumber}",
    patientAdress: "{patient_adress}",
    patientEthnicity: "{patient_ethnicity}",
    patientColor: "{patient_color}",
    patientAdressUF: "{patient_adress_uf}",
    patientAdressCEP: "{patient_adressCEP}",
    documentChartNumber: "{document_chart_number}",
    patientAdressCityIbgeCode: "{patient_adress_city_ibge_code}",
    procedureJustificationDescription: "{procedure_justification_description}",
    procedureJustificationMainCid10: "{prodedure_justification_main_cid_10}",
    procedureJustificationSecCid10: "{prodedure_justification_sec_cid_10}",
    procedureJustificationAssociatedCauseCid10: "{procedure_justification_associated_cause_cid_10}",
    procedureJustificationComments: "{procedure_justification_comments}",
    establishmentExecName: "{establishment_exec_name}",
    establishmentExecCnes: {establishment_exec_cnes},
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
def test_with_data_in_function():
    assert data_to_use() == True

def test_answer_with_all_fields():
    assert data_to_use() == True

def test_awnser_with_only_required_data():
    request_string = """
        mutation{
            generatePdf_Apac("""

    campos_string = """
    establishmentSolitcName: "Establihsment Name",
    establishmentSolitcCnes: 1234567,
    patientName: "Patient Name",
    patientCns: "928976954930007",
    patientSex: "M",
    patientBirthday: "22/10/2022",
    patientAdressCity: "Patient",
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
def test_empty_value_patient_mother_name(test_input):
    assert data_to_use(patient_mother_name=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_establishment_exec_name(test_input):
    assert data_to_use(establishment_exec_name=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_prof_solicitor_name(test_input):
    assert data_to_use(prof_solicitor_name=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_autorization_prof_name(test_input):
    assert data_to_use(autorization_prof_name=test_input) == True



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

def test_valid_patient_birthday():
    assert data_to_use(patient_birthday=datetime_to_use) == True

def test_valid_solicitation_datetime():
    assert data_to_use(solicitation_datetime=datetime_to_use) == True

def test_valid_autorizaton_datetime():
    assert data_to_use(autorizaton_datetime=datetime_to_use) == True

def test_valid_signature_datetime():
    assert data_to_use(signature_datetime=datetime_to_use) == True

def test_valid_validity_period_start():
    assert data_to_use(validity_period_start=datetime_to_use) == True

def test_valid_validity_period_end ():
    assert data_to_use(validity_period_end =datetime_to_use) == True




##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# patient_adress_uf
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


####################################################################
# TEST ADRESS VARIABLES
# patient_adress
# patient_adress_city
# patient_adress_city_ibge_code
# patient_adress_uf (already tested in option tests)
# patient_adressCEP
# test wrong type
# test empty value
# test empty space value
# invalid value
# Long value

def test_empty_value_patient_adress():
    assert data_to_use(patient_adress='') == True

def test_empty_space_patient_adress():
    assert data_to_use(patient_adress='  ') == True

#############################################################################
# TEST BIG TEXT WITH LINE BRAKES
# procedure_justification_comments
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

def test_empty_value_procedure_justification_comments():
    assert data_to_use(procedure_justification_comments='') == True

def test_empty_spaces_procedure_justification_comments():
    assert data_to_use(procedure_justification_comments='    ') == True


##############################################################################
# TEST MAIN PROCEDURES

def test_right_main_procedure():
    assert data_to_use(main_procedure='{name: "teste procedimento",code: "hkmaug347s",quant: 1}') == True

def test_one_secondary_procedure():
    assert data_to_use(secondaries_procedures='{name: "teste procedimento",code: "hkmaug347s",quant: 1}') == True

def test_5_secondary_procedure():
    assert data_to_use(secondaries_procedures='[{name: "teste procedimento",code: "hkmaug347s",quant: 1}, {name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1}]') == True

def test_more_than_5_secondary_procedure():
    assert data_to_use(secondaries_procedures='[{name: "teste procedimento",code: "hkmaug347s",quant: 1}, {name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1},{name: "teste procedimento",code: "hkmaug347s",quant: 1}]') == False


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

def test_empty_value_patient_ethnicity():
    assert data_to_use(patient_ethnicity=None) == True

def test_empty_spaces_patient_ethnicity():
    assert data_to_use(patient_ethnicity='    ') == True

def test_empty_value_patient_color():
    assert data_to_use(patient_color=None) == True

def test_empty_spaces_patient_color():
    assert data_to_use(patient_color='    ') == True

def test_empty_value_prodedure_justification_main_cid_10():
    assert data_to_use(prodedure_justification_main_cid_10=None) == True

def test_empty_spaces_prodedure_justification_main_cid_10():
    assert data_to_use(prodedure_justification_main_cid_10='    ') == True

def test_empty_value_prodedure_justification_sec_cid_10():
    assert data_to_use(prodedure_justification_sec_cid_10=None) == True

def test_empty_spaces_prodedure_justification_sec_cid_10():
    assert data_to_use(prodedure_justification_sec_cid_10='    ') == True

def test_empty_value_procedure_justification_associated_cause_cid_10():
    assert data_to_use(procedure_justification_associated_cause_cid_10 =None) == True

def test_empty_spaces_procedure_justification_associated_cause_cid_10():
    assert data_to_use(procedure_justification_associated_cause_cid_10 ='    ') == True

def test_empty_value_emission_org_code():
    assert data_to_use(emission_org_code =None) == True

def test_empty_spaces_emission_org_code():
    assert data_to_use(emission_org_code ='    ') == True
