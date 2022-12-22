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


def data_to_use(
    patient_name='Patient Name',
    patient_cns='928976954930007',
    patient_mother_name='Patient Mother Name',
    patient_birthday=datetime_to_use,
    solicitation_datetime=datetime_to_use,
    prof_solicitor_name='Professional Name',
    nodule_lump='NAO',
    high_risk='NAOSABE',
    examinated_before='NAOSABE',
    mammogram_before='["NAO", "2020"]',
    patient_age=23,
    health_unit_adress_uf='SP',
    health_unit_cnes=1234567,
    health_unit_name="Health Unit Name",
    health_unit_adress_city='Unit City',
    health_unit_city_ibge_code='1234567',
    document_chart_number='1234567895',
    protocol_number='5478546135245165',
    patient_sex='F',
    patient_surname='Patient Surname',
    patient_document_cpf='{cns: null,rg: null,cpf: "28445400070"}',
    patient_nationality='Patient Nationality',
    patient_adress='Patient Adress',
    patient_adress_number=123456,
    patient_adress_adjunct='Patient Adress Adjunct',
    patient_adress_neighborhood='Neighborhood',
    patient_city_ibge_code='1234567',
    patient_adress_city='Patient City',
    patient_adress_uf='SP',
    patient_ethnicity='["INDIGENA", "Indigena"]',
    patient_adress_reference='Adress Reference',
    patient_schooling='SUPCOMPL',
    patient_adress_cep='12345678',
    exam_number=lenght_test[:10],
    tracking_mammogram='JATRATADO',
    patient_phonenumber='1234567890',
    radiotherapy_before='["SIMESQ", "2020"]',
    breast_surgery_before='''{
didNot: "TRUE",
biopsiaInsinonal: [null],
biopsiaLinfonodo: [null],
biopsiaExcisional: [null],
centraledomia: [null], 
segmentectomia: [null],
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

    request_string = """
        mutation{
            generatePdf_SolicitMamografia("""

    campos_string = f"""
    patientCns: "{patient_cns}",
    patientBirthday: "{patient_birthday}",
    mammogramBefore: {mammogram_before},
    patientAge: {patient_age},
    patientName: "{patient_name}",
    patientMotherName: "{patient_mother_name}",
    noduleLump: "{nodule_lump}",
    highRisk: "{high_risk}",
    examinatedBefore: "{examinated_before}",
    healthUnitName: "{health_unit_name}",
    healthUnitAdressUf: "{health_unit_adress_uf}",
    healthUnitAdressCity: "{health_unit_adress_city}",
    patientSurname: "{patient_surname}",
    patientSchooling: "{patient_schooling}",
    patientAdress: "{patient_adress}",
    patientAdressAdjunct: "{patient_adress_adjunct}",
    patientAdressNeighborhood: "{patient_adress_neighborhood}",
    patientAdressReference: "{patient_adress_reference}",
    patientAdressCity: "{patient_adress_city}",
    patientAdressCep: "{patient_adress_cep}",
    patientPhonenumber: "{patient_phonenumber}",
    radiotherapyBefore: {radiotherapy_before},
    breastSurgeryBefore: {breast_surgery_before},
    healthUnitCnes: {health_unit_cnes},
    protocolNumber: "{protocol_number}",
    patientDocumentCpf: {patient_document_cpf},
    patientAdressNumber: {patient_adress_number},
    patientAdressUf: "{patient_adress_uf}",
    healthUnitCityIbgeCode: "{health_unit_city_ibge_code}",
    documentChartNumber: "{document_chart_number}",
    patientSex: "{patient_sex}",
    patientNationality: "{patient_nationality}",
    patientCityIbgeCode: "{patient_city_ibge_code}",
    patientEthnicity: {patient_ethnicity},
    profSolicitorName: "{prof_solicitor_name}",
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


def test_with_data_in_function():
    assert data_to_use() == True

def test_answer_with_all_fields():
    assert data_to_use() == True

def test_awnser_with_only_required_data():
    request_string = """
        mutation{
            generatePdf_SolicitMamografia("""

    campos_string = """
    patientCns: "928976954930007",
    patientBirthday: "17/11/2022",
    mammogramBefore: ["NAO", "2020"],
    patientAge: 23,
    patientName: "Patient Name",
    patientMotherName: "Patient Mother Name",
    noduleLump: "NAO",
    highRisk: "NAOSABE",
    examinatedBefore: "NUNCA",
    profSolicitorName: "Professional Soliciame",
    solicitationDatetime: "10/10/2012"
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


#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_datetime
# test wrong type
# test valid datetime


def test_valid_patient_birthday():
    assert data_to_use(patient_birthday=datetime_to_use) == True

def test_valid_solicitation_datetime():
    assert data_to_use(solicitation_datetime=datetime_to_use) == True

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
def test_false_sex(test_input):
    assert data_to_use(patient_sex=test_input) == False

@pytest.mark.parametrize("test_input", ['M', 'm', 'F', 'f'])
def test_sex(test_input):
    assert data_to_use(patient_sex=test_input) == True

@pytest.mark.parametrize("test_input", ['SIMDIR', 'simdir', 'SIMESQ', 'simesq',
'NAO', 'nao'])
def test_nodule_lump(test_input):
    assert data_to_use(nodule_lump=test_input) == True

@pytest.mark.parametrize("test_input", ['SIM', 'sim', 'NAOSABE', 'naosabe',
'NAO', 'nao'])
def test_high_risk(test_input):
    assert data_to_use(high_risk=test_input) == True

@pytest.mark.parametrize("test_input", ['SIM', 'sim', 'NAOSABE', 'naosabe',
'NUNCA', 'nunca'])
def test_examinated_before(test_input):
    assert data_to_use(examinated_before=test_input) == True

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
def test_patient_ethnicity(test_input):
    assert data_to_use(patient_ethnicity=test_input) == True

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
def test_patient_schooling(test_input):
    assert data_to_use(patient_schooling=test_input) == True

@pytest.mark.parametrize("test_input", [
    'POPALVO',
    'popalvo',
    'RISCOELEVADO',
    'riscoelevado',
    'JATRATADO',
    'jatratado'
])
def test_tracking_mammogram(test_input):
    assert data_to_use(tracking_mammogram=test_input) == True


####################################################################
# TEST ADRESS VARIABLES
# health_unit_adress_uf
# health_unit_adress_city
# health_unit_city_ibge_code
# patient_city_ibge_code
# patient_adress
# patient_adress_number
# patient_adress_adjunct
# patient_adress_neighborhood
# patient_adress_city
# patient_adress_uf (already tested in option tests)
# patient_adress_reference
# patient_adress_cep
# test wrong type
# test empty value
# test empty space value
# invalid value
# Long value

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_adress(test_input):
    assert data_to_use(patient_adress=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_adress_city(test_input):
    assert data_to_use(patient_adress_city=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_health_unit_adress_city(test_input):
    assert data_to_use(health_unit_adress_city=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_adress_adjunct(test_input):
    assert data_to_use(patient_adress_adjunct=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_adress_neighborhood(test_input):
    assert data_to_use(patient_adress_neighborhood=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_adress_reference(test_input):
    assert data_to_use(patient_adress_reference=test_input) == True

@pytest.mark.parametrize("test_input", ['AC', 'ac', 'AL', 'al', 'AP', 'ap', 'AM', 'am', 'BA', 'ba', 'CE', 'ce', 'DF', 'df', 'ES', 'es', 'GO', 'go', 'MA', 'ma', 'MS', 'ms', 'MT','mt', 'MG', 'mg', 'PA', 'pa', 'PB', 'pb', 'PE', 'pe', 'PR', 'pr', 'PI', 'pi', 'RJ', 'rj', 'RN', 'rn', 'RS', 'rs', 'RO', 'ro', 'RR', 'rr', 'SC', 'sc', 'SP', 'sp', 'SE', 'se', 'TO', 'to'])
def test_ufs(test_input):
    assert data_to_use(patient_adress_uf=test_input) == True

@pytest.mark.parametrize("test_input", ['AC', 'ac', 'AL', 'al', 'AP', 'ap', 'AM', 'am', 'BA', 'ba', 'CE', 'ce', 'DF', 'df', 'ES', 'es', 'GO', 'go', 'MA', 'ma', 'MS', 'ms', 'MT','mt', 'MG', 'mg', 'PA', 'pa', 'PB', 'pb', 'PE', 'pe', 'PR', 'pr', 'PI', 'pi', 'RJ', 'rj', 'RN', 'rn', 'RS', 'rs', 'RO', 'ro', 'RR', 'rr', 'SC', 'sc', 'SP', 'sp', 'SE', 'se', 'TO', 'to'])
def test_health_unit_adress_uf(test_input):
    assert data_to_use(health_unit_adress_uf=test_input) == True


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
def test_protocol_number(test_input):
    assert data_to_use(protocol_number=test_input) == True

@pytest.mark.parametrize("test_input", ['    ', ''])
def test_patient_nationality(test_input):
    assert data_to_use(patient_nationality=test_input) == True


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
def test_radiotherapy_before(test_input):
    assert data_to_use(radiotherapy_before=test_input) == True

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
def test_diagnostic_mammogram(test_input):
    assert data_to_use(diagnostic_mammogram=test_input) == True

# def test_right_diagnostic_mammogram_exame_clinico():
#     assert data_to_use(diagnostic_mammogram=) == True

# def test_right_diagnostic_mammogram_controle_radiologico():
#     assert data_to_use(diagnostic_mammogram=) == True

# def test_right_diagnostic_mammogram_lesao_diagnostico():
#     assert data_to_use(diagnostic_mammogram=) == True

# def test_right_diagnostic_mammogram_avaliacao_resposta():
#     assert data_to_use(diagnostic_mammogram=) == True

# def test_right_diagnostic_mammogram_revisao_mamografia_lesao():
#     assert data_to_use(diagnostic_mammogram=) == True

# def test_right_diagnostic_mammogram_revisao_controle_lesao():
#     assert data_to_use(diagnostic_mammogram=) == True

