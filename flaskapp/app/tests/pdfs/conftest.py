from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
from app.env import GRAPHQL_MUTATION_QUERY_URL
import pytest

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
    return datetime.datetime.now().strftime('%d/%m/%Y')

@pytest.fixture
def datetime_with_timezone_to_use():
    """get current datetime to test"""
    timezone = datetime.timezone(offset=datetime.timedelta(hours=-3))
    return datetime.datetime.now(tz=timezone).strftime('%d/%m/%Y')

@pytest.fixture
def document_datetime_to_use():
    """get current datetime with hours and minutes to test"""
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

@pytest.fixture
def client():
    # Select your transport with ag graphql url endpoint
    transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)
    # Create a GraphQL client using the defined transport
    return Client(transport=transport, fetch_schema_from_transport=True)