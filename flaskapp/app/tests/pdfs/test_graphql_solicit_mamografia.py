from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
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

def test_M_optionUpper_patient_sex():
    assert data_to_use(patient_sex='M') == True

def test_M_optionLower_patient_sex():
    assert data_to_use(patient_sex='m') == True

def test_F_optionUpper_patient_sex():
    assert data_to_use(patient_sex='F') == True

def test_F_optionLower_patient_sex():
    assert data_to_use(patient_sex='f') == True

def test_SIMDIR_optionUpper_nodule_lump():
    assert data_to_use(nodule_lump='SIMDIR') == True

def test_SIMDIR_optionLower_nodule_lump():
    assert data_to_use(nodule_lump='simdir') == True

def test_SIMESQ_optionUpper_nodule_lump():
    assert data_to_use(nodule_lump='SIMESQ') == True

def test_SIMESQ_optionLower_nodule_lump():
    assert data_to_use(nodule_lump='simesq') == True

def test_NAO_optionUpper_nodule_lump():
    assert data_to_use(nodule_lump='NAO') == True

def test_NAO_optionLower_nodule_lump():
    assert data_to_use(nodule_lump='nao') == True

def test_SIM_optionUpper_high_risk():
    assert data_to_use(high_risk='SIM') == True

def test_SIM_optionLower_high_risk():
    assert data_to_use(high_risk='sim') == True

def test_NAOSABE_optionUpper_high_risk():
    assert data_to_use(high_risk='NAOSABE') == True

def test_NAOSABE_optionLower_high_risk():
    assert data_to_use(high_risk='naosabe') == True

def test_NAO_optionUpper_high_risk():
    assert data_to_use(high_risk='NAO') == True

def test_NAO_optionLower_high_risk():
    assert data_to_use(high_risk='nao') == True

def test_SIM_optionUpper_examinated_before():
    assert data_to_use(examinated_before='SIM') == True

def test_SIM_optionLower_examinated_before():
    assert data_to_use(examinated_before='sim') == True

def test_NUNCA_optionUpper_examinated_before():
    assert data_to_use(examinated_before='NUNCA') == True

def test_NUNCA_optionLower_examinated_before():
    assert data_to_use(examinated_before='nunca') == True

def test_NAOSABE_optionUpper_examinated_before():
    assert data_to_use(examinated_before='NAOSABE') == True

def test_NAOSABE_optionLower_examinated_before():
    assert data_to_use(examinated_before='naosabe') == True

def test_BRANCA_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity=['BRANCA', 'ehinith']) == True

def test_BRANCA_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity=['branca', 'ehinith']) == True

def test_PRETA_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity=['PRETA', 'ehinith']) == True

def test_PRETA_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity=['preta', 'ehinith']) == True

def test_PARDA_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity=['PARDA', 'ehinith']) == True

def test_PARDA_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity=['parda', 'ehinith']) == True

def test_AMARELA_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity=['AMARELA', 'ehinith']) == True

def test_AMARELA_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity=['amarela', 'ehinith']) == True

def test_INDIGENA_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity=['INDIGENA', 'ehinith']) == True

def test_INDIGENA_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity=['indigena', 'ehinith']) == True

def test_ANALFABETO_optionUpper_patient_schooling():
    assert data_to_use(patient_schooling='ANALFABETO') == True

def test_ANALFABETO_optionLower_patient_schooling():
    assert data_to_use(patient_schooling='analfabeto') == True

def test_FUNDINCOM_optionUpper_patient_schooling():
    assert data_to_use(patient_schooling='FUNDINCOM') == True

def test_FUNDINCOM_optionLower_patient_schooling():
    assert data_to_use(patient_schooling='fundincom') == True

def test_FUNDCOMPL_optionUpper_patient_schooling():
    assert data_to_use(patient_schooling='FUNDCOMPL') == True

def test_FUNDCOMPL_optionLower_patient_schooling():
    assert data_to_use(patient_schooling='fundcompl') == True

def test_MEDIOCOMPL_optionUpper_patient_schooling():
    assert data_to_use(patient_schooling='MEDIOCOMPL') == True

def test_MEDIOCOMPL_optionLower_patient_schooling():
    assert data_to_use(patient_schooling='mediocompl') == True

def test_SUPCOMPL_optionUpper_patient_schooling():
    assert data_to_use(patient_schooling='SUPCOMPL') == True

def test_SUPCOMPL_optionLower_patient_schooling():
    assert data_to_use(patient_schooling='supcompl') == True

def test_POPALVO_optionUpper_tracking_mammogram():
    assert data_to_use(tracking_mammogram='POPALVO') == True

def test_POPALVO_optionLower_tracking_mammogram():
    assert data_to_use(tracking_mammogram='popalvo') == True

def test_RISCOELEVADO_optionUpper_tracking_mammogram():
    assert data_to_use(tracking_mammogram='RISCOELEVADO') == True

def test_RISCOELEVADO_optionLower_tracking_mammogram():
    assert data_to_use(tracking_mammogram='riscoelevado') == True

def test_JATRATADO_optionUpper_tracking_mammogram():
    assert data_to_use(tracking_mammogram='JATRATADO') == True

def test_JATRATADO_optionLower_tracking_mammogram():
    assert data_to_use(tracking_mammogram='jatratado') == True


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

def test_empty_value_patient_adress():
    assert data_to_use(patient_adress='') == True

def test_empty_space_patient_adress():
    assert data_to_use(patient_adress='  ') == True

def test_empty_value_patient_adress_city():
    assert data_to_use(patient_adress_city='') == True

def test_empty_space_patient_adress_city():
    assert data_to_use(patient_adress_city='  ') == True

def test_empty_value_health_unit_adress_city():
    assert data_to_use(health_unit_adress_city='') == True

def test_empty_space_health_unit_adress_city():
    assert data_to_use(health_unit_adress_city='  ') == True

def test_empty_value_patient_adress_adjunct():
    assert data_to_use(patient_adress_adjunct='') == True

def test_empty_space_patient_adress_adjunct():
    assert data_to_use(patient_adress_adjunct='  ') == True

def test_empty_value_patient_adress_neighborhood():
    assert data_to_use(patient_adress_neighborhood='') == True

def test_empty_space_patient_adress_neighborhood():
    assert data_to_use(patient_adress_neighborhood='  ') == True

def test_empty_value_patient_adress_reference():
    assert data_to_use(patient_adress_reference='') == True

def test_empty_space_patient_adress_reference():
    assert data_to_use(patient_adress_reference='  ') == True

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

def test_AC_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='AC') == True

def test_AC_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='ac') == True

def test_AL_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='AL') == True

def test_AL_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='al') == True

def test_AP_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='AP') == True

def test_AP_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='ap') == True

def test_AM_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='AM') == True

def test_AM_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='am') == True

def test_BA_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='BA') == True

def test_BA_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='ba') == True

def test_CE_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='CE') == True

def test_CE_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='ce') == True

def test_DF_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='DF') == True

def test_DF_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='df') == True

def test_ES_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='ES') == True

def test_ES_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='es') == True

def test_GO_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='GO') == True

def test_GO_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='go') == True

def test_MA_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='MA') == True

def test_MA_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='ma') == True

def test_MS_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='MS') == True

def test_MS_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='ms') == True

def test_MT_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='MT') == True

def test_MT_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='mt') == True

def test_MG_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='MG') == True

def test_MG_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='mg') == True

def test_PA_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='PA') == True

def test_PA_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='pa') == True

def test_PB_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='PB') == True

def test_PB_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='pb') == True

def test_PR_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='PR') == True

def test_PR_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='pr') == True

def test_PE_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='PE') == True

def test_PE_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='pe') == True

def test_PI_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='PI') == True

def test_PI_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='pi') == True

def test_RJ_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='RJ') == True

def test_RJ_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='rj') == True

def test_RN_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='RN') == True

def test_RN_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='rn') == True

def test_RS_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='RS') == True

def test_RS_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='rs') == True

def test_RO_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='RO') == True

def test_RO_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='ro') == True

def test_RR_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='RR') == True

def test_RR_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='rr') == True

def test_SC_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='SC') == True

def test_SC_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='sc') == True

def test_SP_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='SP') == True

def test_SP_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='sp') == True

def test_SE_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='SE') == True

def test_SE_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='se') == True

def test_TO_optionUpper_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='TO') == True

def test_TO_optionLower_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='to') == True


#############################################################################
# NORMAL TEXT VARIABLES THAT CAN BE NULL
# protocol_number
# patient_nationality
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

def test_empty_value_protocol_number():
    assert data_to_use(protocol_number='') == True

def test_empty_spaces_protocol_number():
    assert data_to_use(protocol_number='    ') == True

def test_empty_value_patient_nationality():
    assert data_to_use(patient_nationality='') == True

def test_empty_spaces_patient_nationality():
    assert data_to_use(patient_nationality='    ') == True


#################################################################################
# TEST markable square and oneline text
# radiotherapy_before
# patient_ethnicity
# mammogram_before
# test wrong type
# short value
# long value  
# test not exist option
# test all options in Upper Case
# test all options in lower Case

def test_BRANCA_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["BRANCA", "ehinith"]') == True

def test_BRANCA_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["branca", "ehinith"]') == True

def test_PRETA_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PRETA", "ehinith"]') == True

def test_PRETA_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["preta", "ehinith"]') == True

def test_PARDA_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["PARDA", "ehinith"]') == True

def test_PARDA_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["parda", "ehinith"]') == True

def test_AMARELA_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["AMARELA", "ehinith"]') == True

def test_AMARELA_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["amarela", "ehinith"]') == True

def test_INDIGENA_optionUpper_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["INDIGENA", "ehinith"]') == True

def test_INDIGENA_optionLower_patient_ethnicity():
    assert data_to_use(patient_ethnicity='["indigena", "ehinith"]') == True

def test_SIMDIR_optionUpper_radiotherapy_before():
    assert data_to_use(radiotherapy_before='["SIMDIR", "2020"]') == True

def test_SIMDIR_optionLower_radiotherapy_before():
    assert data_to_use(radiotherapy_before='["simdir", "2020"]') == True

def test_SIMESQ_optionUpper_radiotherapy_before():
    assert data_to_use(radiotherapy_before='["SIMESQ", "2020"]') == True

def test_SIMESQ_optionLower_radiotherapy_before():
    assert data_to_use(radiotherapy_before='["simesq", "2020"]') == True

def test_NAO_optionUpper_radiotherapy_before():
    assert data_to_use(radiotherapy_before='["NAO", "2020"]') == True

def test_NAO_optionLower_radiotherapy_before():
    assert data_to_use(radiotherapy_before='["nao", "2020"]') == True

def test_NAOSABE_optionUpper_radiotherapy_before():
    assert data_to_use(radiotherapy_before='["NAOSABE", "2020"]') == True

def test_NAOSABE_optionLower_radiotherapy_before():
    assert data_to_use(radiotherapy_before='["naosabe", "2020"]') == True


#############################################################################
# test diagnostic_mammogram
# test wrong type
# test wrong type in value
# short value
# long value  
# test not exist option


def test_right_diagnostic_mammogram_exame_clinico():
    assert data_to_use(diagnostic_mammogram='''{
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
    }''') == True

def test_right_diagnostic_mammogram_controle_radiologico():
    assert data_to_use(diagnostic_mammogram='''{
        controleRadiologico:{
        direta: ["nodulo", "microca", "assimetria_focal"],
        esquerda: ["nodulo", "microca", "assimetria_focal"]
        }
    }''') == True

def test_right_diagnostic_mammogram_lesao_diagnostico():
    assert data_to_use(diagnostic_mammogram='''{
        lesaoDiagnostico: {
        direta: ["nodulo", "microca", "assimetria_focal"],
        esquerda: ["nodulo", "microca", "assimetria_focal"] 
        }
    }''') == True

def test_right_diagnostic_mammogram_avaliacao_resposta():
    assert data_to_use(diagnostic_mammogram='''{
        avaliacaoResposta: ["direita", "esquerda"]
    }''') == True

def test_right_diagnostic_mammogram_revisao_mamografia_lesao():
    assert data_to_use(diagnostic_mammogram='''{
        revisaoMamografiaLesao: {
        direta: ["0", "3", "4", "5"],
        esquerda: ["0", "3", "4", "5"]
        }
    }''') == True

def test_right_diagnostic_mammogram_revisao_controle_lesao():
    assert data_to_use(diagnostic_mammogram='''{
        controleLesao: {
        direta: ["nodulo", "microca", "assimetria_focal"],
        esquerda: ["nodulo", "microca", "assimetria_focal"]
        }
        }''') == True

























