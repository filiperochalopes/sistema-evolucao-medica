from gql import gql
from base64 import b64decode
from app.env import GRAPHQL_MUTATION_QUERY_URL, WRITE_DECODE_AIH_SUS_DIRECTORY, WRITE_DECODE_APAC_DIRECTORY, WRITE_DECODE_LME_DIRECTORY,  WRITE_DECODE_RELATORIO_ALTA_DIRECTORY, WRITE_DECODE_SOLICIT_MAMOGRAFIA_DIRECTORY, WRITE_DECODE_COMPACTED_DIRECTORY, WRITE_DECODE_APAC_REQUIRED_DATA_DIRECTORY,WRITE_DECODE_AIH_SUS_REQUIRED_DATA_DIRECTORY,WRITE_DECODE_LME_REQUIRED_DATA_DIRECTORY, WRITE_DECODE_RELATORIO_ALTA_REQUIRED_DATA_DIRECTORY, WRITE_DECODE_SOLICIT_MAMOGRAFIA_REQUIRED_DATA

import pytest
from app.tests.pdfs.request_queries_examples import   solicit_mamografia_request_string, solicit_mamografia_required_data_request_string


@pytest.mark.parametrize("request_string, decode_directory, mutation_name", [ (solicit_mamografia_request_string, WRITE_DECODE_SOLICIT_MAMOGRAFIA_DIRECTORY, "generatePdf_SolicitMamografia"),(solicit_mamografia_required_data_request_string, WRITE_DECODE_SOLICIT_MAMOGRAFIA_REQUIRED_DATA, "generatePdf_SolicitMamografia")])

def test_decode_base64(request_string, decode_directory, mutation_name, client):
    query = gql(request_string)
    created = False
    try:
        # When some exception is created in graphql he return a error
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result[mutation_name]['base64Pdf'], validate=True)


        f = open(decode_directory, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False

    assert created == True
