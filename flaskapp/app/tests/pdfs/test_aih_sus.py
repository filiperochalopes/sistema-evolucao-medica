from gql import gql
import pytest
from app.tests.pdfs.request_queries_examples import aih_sus_required_data_request_string


def data_to_use(client, datetime_to_use, requesting_establishment_name='Establishment Solicit Name',requesting_establishment_cnes="1234567",establishment_exec_name='Establshment Exec Name',establishment_exec_cnes="7654321",patient_name='Patient Name',patient_cns="928976954930007",patient_birthday=None,patient_sex='F',patient_mother_name='Patient Mother Name',patient_address='Patient Adress street neighobourd',patient_address_city='Patient City',patient_address_city_ibge_code='1234567', patient_address_uf='SP',patient_address_cep='12345678',main_clinical_signs_symptoms="Patient main clinical signs sysmpthoms",conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',initial_diagnosis='Patient Initial diagnosis',principal_cid_10="A00",procedure_solicited='Procedure Solicited',procedure_code='1234567890', clinic='Clinic Name', internation_carater='Internation Carater', professional_solicitor_document='{cns: "928976954930007", cpf: null, rg: null}', professional_solicitor_name='Profissional Solicit Name', solicitation_date=None, professional_authorization_name='Authorization professional name', emission_org_code='OrgCode2022', authorization_professional_document='{cns: null, cpf: "28445400070", rg: null}', authorization_date=None,hospitalization_authorization_number='1234567890',exam_results='Xray tibia broken',chart_number='1234',patient_ethnicity='Preta', patient_responsible_name='Patient Responsible Name', contacts_phonenumbers='["5286758957", "5465981345"]', secondary_cid_10='A01',cid_10_associated_causes='A02',acident_type='work_path', insurance_company_cnpj='37549670000171', insurance_company_ticket_number='123450123456', insurance_company_series='Insurn',company_cnpj='37549670000171', company_cnae=5310501, company_cbor=123456, pension_status='not_insured'):

    if patient_birthday == None:
        patient_birthday = datetime_to_use
    if solicitation_date == None:
        solicitation_date = datetime_to_use
    if authorization_date == None:
        authorization_date = datetime_to_use


    # Creating inputs
    requesting_establishment = '{name: ' + f'"{requesting_establishment_name}"' + ', cnes: ' + f'"{requesting_establishment_cnes}"' + '}'
    establishment_exec = '{name: ' + f'"{establishment_exec_name}"' + ', cnes: ' + f'"{establishment_exec_cnes}"' + '}'

    patient_address = '{' + 'street: ' + f'"{patient_address}"' + ', city: ' + f'"{patient_address_city}"' + ', ibgeCityCode: ' + f'"{patient_address_city_ibge_code}"' + ', uf:' + f'"{patient_address_uf}"' + ', zipCode: ' + f'"{patient_address_cep}"' + '},'

    patient = '{name: ' + f'"{patient_name}"' + ', cns: ' + f'"{patient_cns}"' + ', birthdate: ' + f'"{patient_birthday}"' + 'phone: ' + f'"10123456789"' + ', sex: ' + f'"{patient_sex}"' + 'ethnicity: ' + f'"{patient_ethnicity}"'+ ',weightKg:' + '123' +', motherName: ' + f'"{patient_mother_name}"' + ', address: ' + f'{patient_address}' + '}'

    request_string = """
        mutation{
            generatePdf_AihSus("""

    campos_string = f"""
    requestingEstablishment: {requesting_establishment},
    establishmentExec: {establishment_exec},
    patient: {patient},
    mainClinicalSignsSymptoms: "{main_clinical_signs_symptoms}",
    conditionsJustifyHospitalization: "{conditions_justify_hospitalization}",
    initialDiagnosis: "{initial_diagnosis}",
    principalCid10: "{principal_cid_10}",
    requestedProcedure: "{procedure_solicited}",
    procedureCode: "{procedure_code}",
    clinic: "{clinic}",
    internationCarater: "{internation_carater}",
    requestingProfessionalDocument: {professional_solicitor_document},
    requestingProfessionalName: "{professional_solicitor_name}",
    requestDate: "{solicitation_date}",
    professionalAuthorizationName: "{professional_authorization_name}",
    emissionOrgCode: "{emission_org_code}",
    authorizationProfessionalDocument: {authorization_professional_document}
    authorizationDate: "{authorization_date}",
    hospitalizationAuthorizationNumber: "{hospitalization_authorization_number}",
    examResults: "{exam_results}",
    chartNumber: "{chart_number}",
    patientResponsibleName: "{patient_responsible_name}",
    contactsPhonenumbers: {contacts_phonenumbers}
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

#Testing Aih SUS
def test_with_data_in_function(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True

def test_answer_with_all_fields(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True

def test_awnser_with_only_required_data(client):

    query = gql(aih_sus_required_data_request_string)
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

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_empty_value_patient_responsible_name(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, patient_responsible_name=test_input) == True

#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_date
# authorization_date
# test wrong type
# test valid datetime

def test_valid_patient_birthday(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, patient_birthday=datetime_to_use) == True

def test_valid_solicitation_date(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, solicitation_date=datetime_to_use) == True

def test_valid_authorization_date(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, authorization_date=datetime_to_use) == True

##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# acident_type
# pension_status
# patient_address_uf
# test wrong type
# test not exist option
# test all options in Upper Case
# test all options in lower Case

@pytest.mark.parametrize("test_input", ['G', 1231])
def test_false_sex(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, patient_sex=test_input) == False

@pytest.mark.parametrize("test_input", ['M', 'm', 'F', 'f'])
def test_sex(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, patient_sex=test_input) == True

@pytest.mark.parametrize("test_input", ['WORK', 'work', 'TRAFFIC', 'traffic', 'WORK_PATH', 'work_path'])
def test_acident_type(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, acident_type=test_input) == True

@pytest.mark.parametrize("test_input", ['WORKER', 'worker', 'EMPLOYER', 'employer', 'AUTONOMOUS', 'autonomous', 'UNEMPLOYED', 'unemployed', 'RETIRED', 'retired', 'NOT_INSURED', 'not_insured'])
def test_pension_status(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, pension_status=test_input) == True

@pytest.mark.parametrize("test_input", ['AC', 'ac', 'AL', 'al', 'AP', 'ap', 'AM', 'am', 'BA', 'ba', 'CE', 'ce', 'DF', 'df', 'ES', 'es', 'GO', 'go', 'MA', 'ma', 'MS', 'ms', 'MT','mt', 'MG', 'mg', 'PA', 'pa', 'PB', 'pb', 'PE', 'pe', 'PR', 'pr', 'PI', 'pi', 'RJ', 'rj', 'RN', 'rn', 'RS', 'rs', 'RO', 'ro', 'RR', 'rr', 'SC', 'sc', 'SP', 'sp', 'SE', 'se', 'TO', 'to'])
def test_ufs(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, patient_address_uf=test_input) == True

#################################################################################
# TEST INT VARIABLES CAN/CANNOT BE NULL
# hospitalization_authorization_number
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

def test_empty_value_chart_number(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, chart_number=None) == True

def test_empty_value_insurance_company_ticket_number(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, insurance_company_ticket_number=None) == True


##############################################################################
# TEST CNPJ VARIABLES
# insurance_company_cnpj
# company_cnpj
# test wrong type
# test invalid cnpj
# test valid cpnj

def test_validCNPJ_insurance_company_cnpj(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, insurance_company_cnpj=37549670000171) == True

def test_validCNPJ_company_cnpj(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use, company_cnpj=37549670000171) == True


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


@pytest.mark.parametrize("test_input", [None, '    ', ''])
def test_empty_value_patient_ethnicity(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, patient_ethnicity=test_input) == True

@pytest.mark.parametrize("test_input", [None, '    ', ''])
def test_empty_value_secondary_cid_10(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, secondary_cid_10=test_input) == True

@pytest.mark.parametrize("test_input", [None, '    ', ''])
def test_empty_value_cid_10_associated_causes(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, cid_10_associated_causes=test_input) == True

@pytest.mark.parametrize("test_input", [None, '    ', ''])
def test_empty_value_insurance_company_series(client, datetime_to_use, test_input):
    assert data_to_use(client, datetime_to_use, insurance_company_series=test_input) == True




