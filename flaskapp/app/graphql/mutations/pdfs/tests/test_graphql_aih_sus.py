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

def data_to_use(establishment_solitc_name='Establishment Solicit Name',establishment_solitc_cnes=1234567,establishment_exec_name='Establshment Exec Name',establishment_exec_cnes=7654321,patient_name='Patient Name',patient_cns="928976954930007",patient_birthday=datetime_to_use,patient_sex='F',patient_mother_name='Patient Mother Name',patient_adress='Patient Adress street neighobourd',patient_adress_city='Patient City',patient_adress_city_ibge_code='1234567', patient_adress_uf='SP',patient_adress_cep='12345678',main_clinical_signs_symptoms="Patient main clinical signs sysmpthoms",conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',initial_diagnostic='Patient Initial Diagnostic',principal_cid_10="A00",procedure_solicited='Procedure Solicited',procedure_code='1234567890', clinic='Clinic Name', internation_carater='Internation Carater', prof_solicitor_document='{cns: "928976954930007", cpf: null, rg: null}',
prof_solicitor_name='Profissional Solicit Name', solicitation_datetime=datetime_to_use, prof_autorization_name='Autorization professional name', emission_org_code='OrgCode2022', autorizaton_prof_document='{cns: null, cpf: "28445400070", rg: null}', autorizaton_datetime=datetime_to_use,hospitalization_autorization_number='1234567890',exam_results='Xray tibia broken',chart_number='1234',patient_ethnicity='Preta', patient_responsible_name='Patient Responsible Name', patient_mother_phonenumber='5613248546', patient_responsible_phonenumber='8564721598', secondary_cid_10='A01',cid_10_associated_causes='A02',acident_type='work_path', insurance_company_cnpj='37549670000171', insurance_company_ticket_number='123450123456', insurance_company_series='Insurn',company_cnpj='37549670000171', company_cnae=5310501, company_cbor=123456, pension_status='not_insured'):

    request_string = """
        mutation{
            generatePdf_AihSus("""

    campos_string = f"""
    establishmentSolitcName: "{establishment_solitc_name}",
    establishmentSolitcCnes: {establishment_solitc_cnes},
    establishmentExecName: "{establishment_exec_name}",
    establishmentExecCnes: {establishment_exec_cnes},
    patientName: "{patient_name}",
    patientCns: "{patient_cns}",
    patientBirthday: "{patient_birthday}",
    patientSex: "{patient_sex}",
    patientMotherName: "{patient_mother_name}",
    patientAdress: "{patient_adress}",
    patientAdressCity: "{patient_adress_city}",
    patientAdressCityIbgeCode: "{patient_adress_city_ibge_code}",
    patientAdressUF: "{patient_adress_uf}",
    patientAdressCEP: "{patient_adress_cep}",
    mainClinicalSignsSymptoms: "{main_clinical_signs_symptoms}",
    conditionsJustifyHospitalization: "{conditions_justify_hospitalization}",
    initialDiagnostic: "{initial_diagnostic}",
    principalCid10: "{principal_cid_10}",
    procedureSolicited: "{procedure_solicited}",
    procedureCode: "{procedure_code}",
    clinic: "{clinic}",
    internationCarater: "{internation_carater}",
    profSolicitorDocument: {prof_solicitor_document},
    profSolicitorName: "{prof_solicitor_name}",
    solicitationDatetime: "{solicitation_datetime}",
    profAutorizationName: "{prof_autorization_name}",
    emissionOrgCode: "{emission_org_code}",
    autorizatonProfDocument: {autorizaton_prof_document}
    autorizatonDatetime: "{autorizaton_datetime}",
    hospitalizationAutorizationNumber: "{hospitalization_autorization_number}",
    examResults: "{exam_results}",
    chartNumber: "{chart_number}",
    patientEthnicity: "{patient_ethnicity}",
    patientResponsibleName: "{patient_responsible_name}",
    patientMotherPhonenumber: "{patient_mother_phonenumber}",
    patientResponsiblePhonenumber: "{patient_responsible_phonenumber}",
    secondaryCid10: "{secondary_cid_10}",
    cid10AssociatedCauses: "{cid_10_associated_causes}",
    acidentType: "{acident_type}",
    insuranceCompanyCnpj: "{insurance_company_cnpj}",
    insuranceCompanyTicketNumber: "{insurance_company_ticket_number}",
    insuranceCompanySeries: "{insurance_company_series}",
    companyCnpj: "{company_cnpj}",
    companyCnae: {company_cnae},
    companyCbor: {company_cbor},
    pensionStatus: "{pension_status}"
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

#Testing Aih SU
def test_with_data_in_function():
    assert data_to_use() == True

def test_answer_with_all_fields():
    assert data_to_use() == True

def test_awnser_with_only_required_data():
    request_string = """
        mutation{
            generatePdf_AihSus("""

    campos_string = """
    establishmentSolitcName: "Establishment Solicit Name",
    establishmentSolitcCnes: 1234567,
    establishmentExecName: "Establshment Exec Name",
    establishmentExecCnes: 7654321,
    patientName: "Patient Name",
    patientCns: "928976954930007",
    patientBirthday: "10/10/2010",
    patientSex: "M",
    patientMotherName: "Patient Mother Name",
    patientAdress: "Patient Adress street neighobourd",
    patientAdressCity: "Patient City",
    patientAdressCityIbgeCode: "1234567",
    patientAdressUF: "SP",
    patientAdressCEP: "12345678"
    mainClinicalSignsSymptoms: "Patient main clinical signs sysmpthoms",
    conditionsJustifyHospitalization: "'Patient Conditions justify hiospitalizaiton",
    initialDiagnostic: "Patient Initial Diagnostic",
    principalCid10: "A00",
    procedureSolicited: "Procedure Solicited",
    procedureCode: "1234567890",
    clinic: "'Clinic Name",
    internationCarater: "Internation Carater",
    profSolicitorDocument: {cns: "928976954930007", cpf: null, rg: null},
    profSolicitorName: "Profissional Solicit Name",
    solicitationDatetime: "10/10/2021",
    profAutorizationName: "Autorization professional name",
    emissionOrgCode: "OrgCode2022",
    autorizatonProfDocument: {cns: null, cpf: "28445400070", rg: null},
    autorizatonDatetime: "17/01/2008",
    hospitalizationAutorizationNumber: "1234567890",
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

def test_empty_patient_responsible_name():    
    assert data_to_use(patient_responsible_name='') == True

def test_with_space_patient_responsible_name():    
    assert data_to_use(patient_responsible_name='  ') == True


#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_datetime
# autorizaton_datetime
# test wrong type
# test valid datetime

def test_valid_patient_birthday():
    assert data_to_use(patient_birthday=datetime_to_use) == True

def test_valid_solicitation_datetime():
    assert data_to_use(solicitation_datetime=datetime_to_use) == True

def test_valid_autorizaton_datetime():
    assert data_to_use(autorizaton_datetime=datetime_to_use) == True

##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# acident_type
# pension_status
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

def test_work_option_acident_type():
    assert data_to_use(acident_type='work') == True

def test_work_optionUpper_acident_type():
    assert data_to_use(acident_type='WORK') == True

def test_work_optionLower_acident_type():
    assert data_to_use(acident_type='work') == True

def test_traffic_option_acident_type():
    assert data_to_use(acident_type='traffic') == True

def test_traffic_optionUpper_acident_type():
    assert data_to_use(acident_type='TRAFFIC') == True

def test_traffic_optionLower_acident_type():
    assert data_to_use(acident_type='traffic') == True

def test_work_path_option_acident_type():
    assert data_to_use(acident_type='work_path') == True

def test_work_path_optionUpper_acident_type():
    assert data_to_use(acident_type='WORK_PATH') == True

def test_work_path_optionLower_acident_type():
    assert data_to_use(acident_type='work_path') == True

def test_worker_option_pension_status():
    assert data_to_use(pension_status='worker') == True

def test_worker_optionUpper_pension_status():
    assert data_to_use(pension_status='WORKER') == True

def test_worker_optionLower_pension_status():
    assert data_to_use(pension_status='worker') == True

def test_employer_option_pension_status():
    assert data_to_use(pension_status='employer') == True

def test_employer_optionUpper_pension_status():
    assert data_to_use(pension_status='EMPLOYER') == True

def test_employer_optionLower_pension_status():
    assert data_to_use(pension_status='employer') == True

def test_autonomous_option_pension_status():
    assert data_to_use(pension_status='autonomous') == True

def test_autonomous_optionUpper_pension_status():
    assert data_to_use(pension_status='AUTONOMOUS') == True

def test_autonomous_optionLower_pension_status():
    assert data_to_use(pension_status='autonomous') == True

def test_unemployed_option_pension_status():
    assert data_to_use(pension_status='unemployed') == True

def test_unemployed_optionUpper_pension_status():
    assert data_to_use(pension_status='UNEMPLOYED') == True

def test_unemployed_optionLower_pension_status():
    assert data_to_use(pension_status='unemployed') == True

def test_retired_option_pension_status():
    assert data_to_use(pension_status='retired') == True

def test_retired_optionUpper_pension_status():
    assert data_to_use(pension_status='RETIRED') == True

def test_retired_optionLower_pension_status():
    assert data_to_use(pension_status='retired') == True

def test_not_insured_option_pension_status():
    assert data_to_use(pension_status='not_insured') == True

def test_not_insured_optionUpper_pension_status():
    assert data_to_use(pension_status='NOT_INSURED') == True

def test_not_insured_optionLower_pension_status():
    assert data_to_use(pension_status='not_insured') == True

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
# TEST INT VARIABLES CAN/CANNOT BE NULL
# hospitalization_autorization_number
# chart_number
# patient_mother_phonenumber
# patient_responsible_phonenumber
# insurance_company_ticket_number
# company_cnae
# company_cbor
# !!!!! TESTING
# wrong type
# test empty value
# test empty space
# short value
# long value  

def test_empty_value_chart_number():
    assert data_to_use(chart_number=None) == True

def test_empty_value_insurance_company_ticket_number():
    assert data_to_use(insurance_company_ticket_number=None) == True


##############################################################################
# TEST CNPJ VARIABLES
# insurance_company_cnpj
# company_cnpj
# test wrong type
# test invalid cnpj
# test valid cpnj

def test_validCNPJ_insurance_company_cnpj():
    assert data_to_use(insurance_company_cnpj=37549670000171) == True

def test_validCNPJ_company_cnpj():
    assert data_to_use(company_cnpj=37549670000171) == True


##############################################################################
# TEST STRING THAT CAN BE NULL
# patient_ethnicity
# patient_responsible_name
# secondary_cid_10
# cid_10_associated_causes
# insurance_company_series
# test wront type
# test empty value
# test empty spaces
# test long values
# test short values

def test_empty_value_patient_ethnicity():
    assert data_to_use(patient_ethnicity=None) == True

def test_empty_spaces_patient_ethnicity():
    assert data_to_use(patient_ethnicity='    ') == True

def test_empty_spaces_patient_responsible_name():
    assert data_to_use(patient_responsible_name='    ') == True

def test_empty_value_secondary_cid_10():
    assert data_to_use(secondary_cid_10=None) == True

def test_empty_spaces_secondary_cid_10():
    assert data_to_use(secondary_cid_10='    ') == True

def test_empty_value_cid_10_associated_causes():
    assert data_to_use(cid_10_associated_causes=None) == True

def test_empty_spaces_cid_10_associated_causes():
    assert data_to_use(cid_10_associated_causes='    ') == True

def test_empty_value_insurance_company_series():
    assert data_to_use(insurance_company_series=None) == True

def test_empty_spaces_insurance_company_series():
    assert data_to_use(insurance_company_series='    ') == True


