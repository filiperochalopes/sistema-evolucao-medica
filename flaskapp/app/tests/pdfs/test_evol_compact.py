from gql import gql
from base64 import b64decode

import pytest

from app.env import WRITE_DECODE_COMPACTED_DIRECTORY, WRITE_DECODE_COMPACTED_REQUIRED_DATA
from app.tests.pdfs.request_queries_examples import (
    evol_compact_request_string,
    evol_compact_required_data_request_string,
)


def make_request(client, request_string):
    query = gql(request_string)
    # When some exception is created in grphql he return a error
    client.execute(query)
    return True


def test_with_all_data(client):
    assert make_request(client, evol_compact_request_string) == True


def test_awnser_with_only_required_data(client):
    assert make_request(client, evol_compact_required_data_request_string) == True


@pytest.mark.parametrize("request_string, decode_directory", [(evol_compact_request_string, WRITE_DECODE_COMPACTED_DIRECTORY), (evol_compact_required_data_request_string, WRITE_DECODE_COMPACTED_REQUIRED_DATA)])
def test_create_pdf_file_from_query(client, request_string, decode_directory):
    try:
        query = gql(request_string)
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result["generatePdf_EvolCompact"]["base64Pdf"], validate=True)

        f = open(decode_directory, 'wb')
        f.write(generated_pdf_b64)
        f.close()
        assert True
    except:
        assert False

