from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from datetime import datetime, timezone, timedelta
from base64 import b64decode
from app.env import DatabaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.models import BaseModel
from app.env import GRAPHQL_MUTATION_QUERY_URL, QUERIES_DIRECTORY, TMP_FILES_FOLDER
import pytest


@pytest.fixture
def client():
    # Select your transport with ag graphql url endpoint
    transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)
    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)


@pytest.fixture
def auth_client(client):
    '''Cria um cliente de requisições com usuário de teste padrão'''
    signin_query = gql(get_query_from_txt('signin'))
    result = client.execute(signin_query)
    token = result['signin']['token']
    transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL, headers={'Authorization': f'Bearer {token}'})
    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)

def get_query_from_txt(filename: str):
    '''Retorna o texto de uma querie armazenada em txt'''
    with open(f'{QUERIES_DIRECTORY}/{filename}.txt', 'r') as file:
        request = file.read()
    return request


@pytest.fixture
def fixture_get_query_from_txt(request):
    get_query_from_txt(request.param)


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


@pytest.fixture(scope="session")
def engine():
    print(f"Conectando ao banco de dados {DatabaseSettings(env='production').URL}...")
    return create_engine(DatabaseSettings(env='production').URL)


@pytest.fixture(scope="session")
def tables(engine):
    print("Creating tables...")
    BaseModel.metadata.create_all(engine)
    yield
    print("Droping tables...")
    BaseModel.metadata.drop_all(engine)


@pytest.fixture
def dbsession(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()


@pytest.fixture
def lenght_test():
    """generate a string with data with charactes to test lenght"""
    lenght_test = ''
    for x in range(0, 1100):
        lenght_test += str(x)
    return lenght_test

@pytest.fixture
def datetime_to_use():
    """get current datetime to test"""
    return datetime.now().isoformat()

@pytest.fixture
def datetime_with_timezone_to_use():
    """get current datetime to test"""
    tmz = timezone(offset=timedelta(hours=-3))
    return datetime.now(tz=tmz).isoformat()

@pytest.fixture
def client():
    # Select your transport with ag graphql url endpoint
    transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)
    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)