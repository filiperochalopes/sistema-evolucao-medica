from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from datetime import datetime
from base64 import b64decode
from app.env import GRAPHQL_MUTATION_QUERY_URL, QUERIES_DIRECTORY, TMP_FILES_FOLDER
import pytest


@pytest.fixture
def client():
    # Select your transport with ag graphql url endpoint
    transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)
    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)


@pytest.fixture
def get_query_from_txt(request):
    '''
    Retorna o texto de uma querie armazenada em txt

    request.param deve ser o nome do arquivo a ser buscado
    '''
    with open(f'{QUERIES_DIRECTORY}/{request.param}.txt', 'r') as file:
        request = file.read()
    return request


@pytest.fixture
def download_pdf(request):
    '''
    Converte string em base64 para um arquivo pdf temporário
    lembrando sempre de excluir os dados mais antigos que um 
    dia.

    request.param deve ser uma tupla (label, base64string)
    '''
    created = False
    try:
        generated_pdf_b64 = b64decode(request.param[1], validate=True)

        now = datetime.now()
        f = open(
            f"{TMP_FILES_FOLDER}/{request.param[0]}__{now.strftime('%Y_ %m_%d_%H_%M_%S')}.pdf", 'wb')
        f.write(generated_pdf_b64)
        f.close()
        created = True
    except:
        created = False
    
    return created
    
