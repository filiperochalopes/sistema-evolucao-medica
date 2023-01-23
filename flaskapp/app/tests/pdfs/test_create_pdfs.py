from gql import gql
from base64 import b64decode
from app.env import GRAPHQL_MUTATION_QUERY_URL, WRITE_DECODE_AIH_SUS_DIRECTORY, WRITE_DECODE_APAC_DIRECTORY,WRITE_DECODE_EXAM_REQUEST_DIRECTORY,WRITE_DECODE_FICHA_INTERN_DIRECTORY, WRITE_DECODE_LME_DIRECTORY, WRITE_DECODE_PRESCRICAO_MEDICA_DIRECTORY, WRITE_DECODE_RELATORIO_ALTA_DIRECTORY, WRITE_DECODE_SOLICIT_MAMOGRAFIA_DIRECTORY, WRITE_DECODE_EXAM_REQUEST_2_PAGES_DIRECTORY, WRITE_DECODE_EXAM_REQUEST_3_PAGES_DIRECTORY, WRITE_DECODE_FOLHA_PRESCRICAO_DIRECTORY, WRITE_DECODE_FOLHA_EVOLUCAO_DIRECTORY,WRITE_DECODE_BALANCO_HIDRICO_DIRECTORY
import pytest
from app.tests.pdfs.request_queries_examples import aih_sus_request_string, apac_request_string, exam_request_request_string, ficha_internamento_request_string, prescricao_medica_request_string, lme_request_string, solicit_mamografia_request_string, relatorio_alta_request_string, exam_request_2_pages_request_string, exam_request_3_pages_request_string, folha_prescricao_request_string, folha_evolucao_request_string, balanco_hidrico_request_string


@pytest.mark.parametrize("request_string", [aih_sus_request_string, apac_request_string, exam_request_request_string, ficha_internamento_request_string, prescricao_medica_request_string, lme_request_string, solicit_mamografia_request_string, relatorio_alta_request_string, exam_request_2_pages_request_string, exam_request_3_pages_request_string, folha_prescricao_request_string, folha_evolucao_request_string, balanco_hidrico_request_string])
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

@pytest.mark.parametrize("request_string, decode_directory, mutation_name", [(aih_sus_request_string, WRITE_DECODE_AIH_SUS_DIRECTORY, "generatePdf_AihSus"), (apac_request_string, WRITE_DECODE_APAC_DIRECTORY, "generatePdf_Apac"), (exam_request_request_string, WRITE_DECODE_EXAM_REQUEST_DIRECTORY, "generatePdf_SolicitExames"), (ficha_internamento_request_string, WRITE_DECODE_FICHA_INTERN_DIRECTORY, "generatePdf_FichaInternamento"), (prescricao_medica_request_string, WRITE_DECODE_PRESCRICAO_MEDICA_DIRECTORY, "generatePdf_PrescricaoMedica"), (lme_request_string, WRITE_DECODE_LME_DIRECTORY, "generatePdf_Lme"), (solicit_mamografia_request_string, WRITE_DECODE_SOLICIT_MAMOGRAFIA_DIRECTORY, "generatePdf_SolicitMamografia"), (relatorio_alta_request_string, WRITE_DECODE_RELATORIO_ALTA_DIRECTORY, "generatePdf_RelatorioAlta"), (exam_request_2_pages_request_string, WRITE_DECODE_EXAM_REQUEST_2_PAGES_DIRECTORY, "generatePdf_SolicitExames"), (exam_request_3_pages_request_string, WRITE_DECODE_EXAM_REQUEST_3_PAGES_DIRECTORY, "generatePdf_SolicitExames"),
(folha_prescricao_request_string, WRITE_DECODE_FOLHA_PRESCRICAO_DIRECTORY, "generatePdf_FolhaPrescricao"), (folha_evolucao_request_string, WRITE_DECODE_FOLHA_EVOLUCAO_DIRECTORY, "generatePdf_FolhaEvolucao"), (balanco_hidrico_request_string, WRITE_DECODE_BALANCO_HIDRICO_DIRECTORY, "generatePdf_BalancoHidrico")])
def test_decode_base64(request_string, decode_directory, mutation_name, client):
    query = gql(request_string)
    created = False
    try:
        #When some exception is created in grphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result[mutation_name]['base64Pdf'], validate=True)


        f = open(decode_directory, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True
