from gql import gql
import pytest
from app.tests.pdfs.request_queries_examples import solicit_mamografia_required_data_request_string

def data_to_use(client, datetime_with_timezone_to_use, 
    patient_name='Patient Name',
    patient_cns='928976954930007',
    patient_mother_name='Patient Mother Name',
    patient_birthday=None,
    solicitation_datetime=None,
    professional_solicitor_name='Professional Name',
    nodule_lump='NAO',
    high_risk='NAOSABE',
    examinated_before='NAOSABE',
    mammogram_before='["NAO", "2020"]',
    health_unit_adress_uf='SP',
    health_unit_cnes=1234567,
    health_unit_name="Health Unit Name",
    health_unit_adress_city='Unit City',
    health_unit_city_ibge_code='1234567',
    document_chart_number='1234567895',
    protocol_number='5478546135245165',
    patient_sex='F',
    patient_surname='Patient Surname',
    patient_document_cpf='"28445400070"',
    patient_nationality='Patient Nationality',
    patient_address='Patient Adress',
    patient_address_number=123456,
    patient_address_adjunct='Patient Adress Adjunct',
    patient_address_neighborhood='Neighborhood',
    patient_address_city_ibge_code='1234567',
    patient_address_city='Patient City',
    patient_address_uf='SP',
    patient_ethnicity='["INDIGENA", "Indigena"]',
    patient_address_reference='Adress Reference',
    patient_schooling='SUPCOMPL',
    patient_address_cep='12345678',
    exam_number="4512457845",
    tracking_mammogram='JATRATADO',
    patient_phonenumber='1234567890',
    radiotherapy_before='["SIMESQ", "2020"]',
    breast_surgery_before='''{
didNot: "false",
biopsiaInsinonal: ["2020", null],
biopsiaLinfonodo: [null],
biopsiaExcisional: [null],
centraledomia: [null], 
segmentectomia: ["2021", "2010"],
dutectomia: [null],
mastectomia: [null],
mastectomiaPoupadoraPele: [null],
mastectomiaPoupadoraPeleComplexoAreolo: [null],
linfadenectomiaAxilar: [null],
reconstrucaoMamaria: [null],
mastoplastiaRedutora: [null],
indusaoImplantes: [null]
}''',
    diagnostic_mammogram='''{
    exameClinico:{
    direta: {
        papilar: true,
        descargaPapilar: ["CRISTALINA", "HEMORRAGICA"],
        nodulo: ["QSL", "QIL", "QSM", "QIM"],
        espessamento: ["QSL", "QIL", "QSM", "QIM"],
        linfonodoPalpavel: ["AXILAR", "SUPRACLAVICULAR"]
    },
    esquerda:{
        papilar: true,
        descargaPapilar: ["CRISTALINA", "HEMORRAGICA"],
        nodulo: ["QSL", "QIL", "QSM", "QIM"],
        espessamento: ["QSL", "QIL", "QSM", "QIM"],
        linfonodoPalpavel: ["AXILAR", "SUPRACLAVICULAR"]
    }
    },
    controleRadiologico:{
    direta: ["nodulo", "microca", "assimetria_focal"],
    esquerda: ["nodulo", "microca", "assimetria_focal"]
    },
    lesaoDiagnostico: {
    direta: ["nodulo", "microca", "assimetria_focal"],
    esquerda: ["nodulo", "microca", "assimetria_focal"] 
    },
    avaliacaoResposta: ["direita", "esquerda"],
    revisaoMamografiaLesao: {
    direta: ["0", "3", "4", "5"],
    esquerda: ["0", "3", "4", "5"]
    },
    controleLesao: {
    direta: ["nodulo", "microca", "assimetria_focal"],
    esquerda: ["nodulo", "microca", "assimetria_focal"]
    }
    
}'''
):

    if solicitation_datetime == None:
        solicitation_datetime = datetime_with_timezone_to_use
    if patient_birthday == None:
        patient_birthday = datetime_with_timezone_to_use
    

    patient_address = '{' + 'street: ' + f'"{patient_address}"' + ', city: ' + f'"{patient_address_city}"' + ',reference: ' + f'"{patient_address_reference}"' + 'neighborhood: ' + f'"{patient_address_neighborhood}"' +', complement: ' + f'"{patient_address_adjunct}"' + ',number: ' + f'"{patient_address_number}"'  + ', ibgeCityCode: ' + f'"{patient_address_city_ibge_code}"' + ', uf:' + f'"{patient_address_uf}"' + ', zipCode: ' + f'"{patient_address_cep}"' + '},'

    patient = '{name: ' + f'"{patient_name}"' + ', cns: ' + f'"{patient_cns}"' + ',cpf: ' + str(patient_document_cpf) + ', birthdate: ' + f'"{patient_birthday}"' + ', sex: ' + f'"{patient_sex}"' + ', motherName: ' + f'"{patient_mother_name}"' + ',weightKg:' + '123' + ', address: ' + f'{patient_address}' + 'nationality:' + f'"{patient_nationality}"' + '}'

    request_string = """
        mutation{
            generatePdf_SolicitMamografia("""

    campos_string = f"""
    patient: {patient},
    patientPhonenumber: "{patient_phonenumber}",
    patientSchooling: "{patient_schooling}",
    patientSurname: "{patient_surname}",
    mammogramBefore: {mammogram_before},
    noduleLump: "{nodule_lump}",
    highRisk: "{high_risk}",
    examinatedBefore: "{examinated_before}",
    healthUnitName: "{health_unit_name}",
    healthUnitAdressUf: "{health_unit_adress_uf}",
    healthUnitAdressCity: "{health_unit_adress_city}",
    radiotherapyBefore: {radiotherapy_before},
    breastSurgeryBefore: {breast_surgery_before},
    healthUnitCnes: {health_unit_cnes},
    protocolNumber: "{protocol_number}",
    healthUnitCityIbgeCode: "{health_unit_city_ibge_code}",
    documentChartNumber: "{document_chart_number}",
    patientEthnicity: {patient_ethnicity},
    professionalSolicitorName: "{professional_solicitor_name}",
    solicitationDatetime: "{solicitation_datetime}",
    examNumber: "{exam_number}",
    trackingMammogram: "{tracking_mammogram}",
    diagnosticMammogram: {diagnostic_mammogram}
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
    
    
def test_with_data_in_function(client, datetime_with_timezone_to_use):
    assert data_to_use(client, datetime_with_timezone_to_use) == True

def test_answer_with_all_fields(client, datetime_with_timezone_to_use):
    assert data_to_use(client, datetime_with_timezone_to_use) == True

def test_awnser_with_only_required_data(client):

    query = gql(solicit_mamografia_required_data_request_string)
    result = False 
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True 
    except:
        result = False 
    assert result == True


#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_datetime
# test wrong type
# test valid datetime


def test_valid_patient_birthday(client, datetime_with_timezone_to_use):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_birthday=datetime_with_timezone_to_use) == True

def test_valid_solicitation_datetime(client, datetime_with_timezone_to_use):
    assert data_to_use(client, datetime_with_timezone_to_use, solicitation_datetime=datetime_with_timezone_to_use) == True

##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# nodule_lump
# high_risk
# examinated_before
# patient_ethnicity
# patient_schooling
# tracking_mammogram
# test wrong type
# test not exist option
# test all options in Upper Case
# test all options in lower Case

@pytest.mark.parametrize("test_input", ['G', 1231])
def test_false_sex(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_sex=test_input) == False

@pytest.mark.parametrize("test_input", ['M', 'm', 'F', 'f'])
def test_sex(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_sex=test_input) == True

@pytest.mark.parametrize("test_input", ['SIMDIR', 'simdir', 'SIMESQ', 'simesq',
'NAO', 'nao'])
def test_nodule_lump(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, nodule_lump=test_input) == True

@pytest.mark.parametrize("test_input", ['SIM', 'sim', 'NAOSABE', 'naosabe',
'NAO', 'nao'])
def test_high_risk(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, high_risk=test_input) == True

@pytest.mark.parametrize("test_input", ['SIM', 'sim', 'NAOSABE', 'naosabe',
'NUNCA', 'nunca'])
def test_examinated_before(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, examinated_before=test_input) == True

@pytest.mark.parametrize("test_input", [
'["BRANCA", "ehinith"]',
'["branca", "ehinith"]',
'["PRETA", "ehinith"]',
'["preta", "ehinith"]',
'["PARDA", "ehinith"]',
'["parda", "ehinith"]',
'["AMARELA", "ehinith"]',
'["amarela", "ehinith"]',
'["INDIGENA", "ehinith"]',
'["indigena", "ehinith"]'
])
def test_patient_ethnicity(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_ethnicity=test_input) == True

@pytest.mark.parametrize("test_input", [
    'ANALFABETO', 
    'analfabeto',
    'FUNDINCOM',
    'fundincom',
    'FUNDCOMPL',
    'fundcompl',
    'MEDIOCOMPL',
    'mediocompl',
    'SUPCOMPL',
    'supcompl'
])
def test_patient_schooling(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_schooling=test_input) == True

@pytest.mark.parametrize("test_input", [
    'POPALVO',
    'popalvo',
    'RISCOELEVADO',
    'riscoelevado',
    'JATRATADO',
    'jatratado'
])
def test_tracking_mammogram(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, tracking_mammogram=test_input) == True


####################################################################
# TEST ADRESS VARIABLES
# health_unit_adress_uf
# health_unit_adress_city
# health_unit_city_ibge_code
# patient_address_city_ibge_code
# patient_address
# patient_address_number
# patient_address_adjunct
# patient_address_neighborhood
# patient_address_city
# patient_address_uf (already tested in option tests)
# patient_address_reference
# patient_address_cep
# test wrong type
# test empty value
# test empty space value
# invalid value
# Long value

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_address(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_address=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_address_city(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_address_city=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_health_unit_adress_city(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, health_unit_adress_city=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_address_adjunct(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_address_adjunct=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_address_neighborhood(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_address_neighborhood=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_address_reference(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_address_reference=test_input) == True

@pytest.mark.parametrize("test_input", ['AC', 'ac', 'AL', 'al', 'AP', 'ap', 'AM', 'am', 'BA', 'ba', 'CE', 'ce', 'DF', 'df', 'ES', 'es', 'GO', 'go', 'MA', 'ma', 'MS', 'ms', 'MT','mt', 'MG', 'mg', 'PA', 'pa', 'PB', 'pb', 'PE', 'pe', 'PR', 'pr', 'PI', 'pi', 'RJ', 'rj', 'RN', 'rn', 'RS', 'rs', 'RO', 'ro', 'RR', 'rr', 'SC', 'sc', 'SP', 'sp', 'SE', 'se', 'TO', 'to'])
def test_ufs(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_address_uf=test_input) == True

@pytest.mark.parametrize("test_input", ['AC', 'ac', 'AL', 'al', 'AP', 'ap', 'AM', 'am', 'BA', 'ba', 'CE', 'ce', 'DF', 'df', 'ES', 'es', 'GO', 'go', 'MA', 'ma', 'MS', 'ms', 'MT','mt', 'MG', 'mg', 'PA', 'pa', 'PB', 'pb', 'PE', 'pe', 'PR', 'pr', 'PI', 'pi', 'RJ', 'rj', 'RN', 'rn', 'RS', 'rs', 'RO', 'ro', 'RR', 'rr', 'SC', 'sc', 'SP', 'sp', 'SE', 'se', 'TO', 'to'])
def test_health_unit_adress_uf(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, health_unit_adress_uf=test_input) == True


#############################################################################
# NORMAL TEXT VARIABLES THAT CAN BE NULL
# protocol_number
# patient_nationality
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit



@pytest.mark.parametrize("test_input", ['    ', ''])
def test_protocol_number(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, protocol_number=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_nationality(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, patient_nationality=test_input) == True


#################################################################################
# TEST markable square and oneline text
# radiotherapy_before
# mammogram_before
# test wrong type
# short value
# long value  
# test not exist option
# test all options in Upper Case
# test all options in lower Case

@pytest.mark.parametrize("test_input", [
    '["SIMDIR", "2020"]',
    '["simdir", "2020"]',
    '["SIMESQ", "2020"]',
    '["simesq", "2020"]',
    '["NAO", "2020"]',
    '["nao", "2020"]',
    '["NAOSABE", "2020"]'
])
def test_radiotherapy_before(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, radiotherapy_before=test_input) == True

#############################################################################
# test diagnostic_mammogram
# test wrong type
# test wrong type in value
# short value
# long value  
# test not exist option

@pytest.mark.parametrize("test_input", [
    '''{
    exameClinico:{
        direta: {
            papilar: true,
            descargaPapilar: ["CRISTALINA", "HEMORRAGICA"],
            nodulo: ["QSL", "QIL", "QSM", "QIM", "UQLAT", "UQSUP", "UQMED", "UQINF", "RRA", "PA"],
            espessamento:["QSL", "QIL", "QSM", "QIM", "UQLAT", "UQSUP", "UQMED", "UQINF", "RRA", "PA"],
            linfonodoPalpavel:["AXILAR", "SUPRACLAVICULAR"]
            },
        esquerda:{
            papilar: true,
            descargaPapilar: ["CRISTALINA", "HEMORRAGICA"],
            nodulo: ["QSL", "QIL", "QSM", "QIM", "UQLAT", "UQSUP", "UQMED", "UQINF", "RRA", "PA"],
            espessamento:["QSL", "QIL", "QSM", "QIM", "UQLAT", "UQSUP", "UQMED", "UQINF", "RRA", "PA"],
            linfonodoPalpavel:["AXILAR", "SUPRACLAVICULAR"]
            }
        }
    }''',
    '''{
        controleRadiologico:{
        direta: ["nodulo", "microca", "assimetria_focal"],
        esquerda: ["nodulo", "microca", "assimetria_focal"]
        }
    }''',
    '''{
        lesaoDiagnostico: {
        direta: ["nodulo", "microca", "assimetria_focal"],
        esquerda: ["nodulo", "microca", "assimetria_focal"] 
        }
    }''',
    '''{
        avaliacaoResposta: ["direita", "esquerda"]
    }''',
    '''{
        revisaoMamografiaLesao: {
        direta: ["0", "3", "4", "5"],
        esquerda: ["0", "3", "4", "5"]
        }
    }''',
    '''{
        controleLesao: {
        direta: ["nodulo", "microca", "assimetria_focal"],
        esquerda: ["nodulo", "microca", "assimetria_focal"]
        }
        }'''
])
def test_diagnostic_mammogram(client, datetime_with_timezone_to_use, test_input):
    assert data_to_use(client, datetime_with_timezone_to_use, diagnostic_mammogram=test_input) == True

