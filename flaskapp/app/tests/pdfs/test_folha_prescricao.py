from gql import gql
from base64 import b64decode
import pytest

from app.env import TMP_FILES_FOLDER
from app.tests.pdfs.request_queries_examples import (
    folha_prescricao_request_strings
)


def make_request(client, request_string):
    query = gql(request_string)
    # When some exception is created in grphql he return a error
    client.execute(query)
    return True


@pytest.mark.skip(reason="We have to fix mutation first")
def test_all_test_queries(client):
    for request_string in folha_prescricao_request_strings:
        assert make_request(client, request_string) == True


@pytest.mark.skip(reason="We have to fix mutation first")
def test_create_pdf_file_from_queries(client):
    PDF_START_STRING = 'folha_prescricao'

    DIRECTORY_START = f"{TMP_FILES_FOLDER}/{PDF_START_STRING}_"
    count = 1
    for request_string in folha_prescricao_request_strings:
        query = gql(request_string)
        result = client.execute(query)
        generated_pdf_b64 = b64decode(result["generatePdf_FolhaPrescricao"]["base64Pdf"], validate=True)

        f = open(f"{DIRECTORY_START}{count}.pdf", 'wb')
        f.write(generated_pdf_b64)
        f.close()
        count += 1
        assert True

