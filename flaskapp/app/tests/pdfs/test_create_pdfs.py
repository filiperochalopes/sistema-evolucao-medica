from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from base64 import b64decode
from app.env import GRAPHQL_MUTATION_QUERY_URL, WRITE_DECODE_BASE_URL, WRITE_DECODE_AIH_SUS_DIRECTORY, WRITE_DECODE_APAC_DIRECTORY,WRITE_DECODE_EXAM_REQUEST_DIRECTORY,WRITE_DECODE_FICHA_INTERN_DIRECTORY, WRITE_DECODE_LME_DIRECTORY, WRITE_DECODE_PRESCRICAO_MEDICA_DIRECTORY, WRITE_DECODE_RELATORIO_ALTA_DIRECTORY, WRITE_DECODE_SOLICIT_MAMOGRAFIA_DIRECTORY, WRITE_DECODE_EXAM_REQUEST_2_PAGES_DIRECTORY, WRITE_DECODE_EXAM_REQUEST_3_PAGES_DIRECTORY
import pytest
from app.tests.pdfs.request_queries_examples import aih_sus_request_string, apac_request_string, exam_request_request_string, ficha_internamento_request_string, prescricao_medica_request_string, lme_request_string, solicit_mamografia_request_string, relatorio_alta_request_string, exam_request_2_pages_request_string, exam_request_3_pages_request_string

@pytest.fixture
def client():
    # Select your transport with ag graphql url endpoint
    transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)
    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)


@pytest.mark.parametrize("request_string", [aih_sus_request_string, apac_request_string, exam_request_request_string, ficha_internamento_request_string, prescricao_medica_request_string, lme_request_string, solicit_mamografia_request_string, relatorio_alta_request_string, exam_request_2_pages_request_string, exam_request_3_pages_request_string])
def test_create_requests(request_string, client):
    query = gql(request_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True



def test_create_aih_sus_pdf(client):
    query = gql(aih_sus_request_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True


def test_decode_base64_aih_sus_pdf(client):
    query = gql(aih_sus_request_string)
    created = False
    try:
        #When some exception is created in grphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result['generatePdf_AihSus']['base64Pdf'], validate=True)


        f = open(WRITE_DECODE_AIH_SUS_DIRECTORY, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True


def test_create_apac_pdf(client):
    query = gql(apac_request_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True

def test_decode_base64_apac_pdf(client):
    query = gql(apac_request_string)
    created = False
    try:
        #When some exception is created in grphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result['generatePdf_Apac']['base64Pdf'], validate=True)


        f = open(WRITE_DECODE_APAC_DIRECTORY, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True

def test_create_exam_request_pdf(client):
    query = gql(exam_request_request_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True

def test_decode_base64_exam_request_pdf(client):
    query = gql(exam_request_request_string)
    created = False
    try:
        #When some exception is created in grphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result['generatePdf_SolicitExames']['base64Pdf'], validate=True)


        f = open(WRITE_DECODE_EXAM_REQUEST_DIRECTORY, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True

def test_create_exam_request_2_pages_pdf(client):
    query = gql(exam_request_2_pages_request_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True

def test_decode_base64_exam_request_2_pages_pdf(client):
    query = gql(exam_request_2_pages_request_string)
    created = False
    try:
        #When some exception is created in grphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result['generatePdf_SolicitExames']['base64Pdf'], validate=True)


        f = open(WRITE_DECODE_EXAM_REQUEST_2_PAGES_DIRECTORY, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True

def test_create_exam_request_3_pages_pdf(client):
    query = gql(exam_request_3_pages_request_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True

def test_decode_base64_exam_request_3_pages_pdf(client):
    query = gql(exam_request_3_pages_request_string)
    created = False
    try:
        #When some exception is created in grphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result['generatePdf_SolicitExames']['base64Pdf'], validate=True)


        f = open(WRITE_DECODE_EXAM_REQUEST_3_PAGES_DIRECTORY, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True

def test_create_ficha_internamento_pdf(client):
    query = gql(ficha_internamento_request_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True

def test_decode_base64_ficha_internamento_pdf(client):
    query = gql(ficha_internamento_request_string)
    created = False
    try:
        #When some exception is created in grphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result['generatePdf_FichaInternamento']['base64Pdf'], validate=True)


        f = open(WRITE_DECODE_FICHA_INTERN_DIRECTORY, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True


def test_create_lme_pdf(client):
    query = gql(lme_request_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True

def test_decode_base64_lme_pdf(client):
    query = gql(lme_request_string)
    created = False
    try:
        #When some exception is created in grphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result['generatePdf_Lme']['base64Pdf'], validate=True)


        f = open(WRITE_DECODE_LME_DIRECTORY, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True

def test_create_precricao_medica_pdf(client):
    query = gql(prescricao_medica_request_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True

def test_decode_base64_precricao_medica_pdf(client):
    query = gql(prescricao_medica_request_string)
    created = False
    try:
        #When some exception is created in grphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result['generatePdf_PrescricaoMedica']['base64Pdf'], validate=True)


        f = open(WRITE_DECODE_PRESCRICAO_MEDICA_DIRECTORY, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True


def test_create_relatorio_alta_pdf(client):
    query = gql(relatorio_alta_request_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True

def test_decode_base64_relatorio_alta_pdf(client):
    query = gql(relatorio_alta_request_string)
    created = False
    try:
        #When some exception is created in grphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result['generatePdf_RelatorioAlta']['base64Pdf'], validate=True)


        f = open(WRITE_DECODE_RELATORIO_ALTA_DIRECTORY, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True

def test_create_solicit_mamografia_pdf(client):
    query = gql(solicit_mamografia_request_string)
    result = False
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False 
    
    assert result == True

def test_decode_base64_solicit_mamografia_pdf(client):
    query = gql(solicit_mamografia_request_string)
    created = False
    try:
        #When some exception is created in grphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result['generatePdf_SolicitMamografia']['base64Pdf'], validate=True)


        f = open(WRITE_DECODE_SOLICIT_MAMOGRAFIA_DIRECTORY, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True

