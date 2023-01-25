from gql import gql
import pytest

@pytest.mark.parametrize(
    'get_query_from_txt',
    ('hello',),
    indirect=True
)
def test_hello(client, get_query_from_txt):
    result = client.execute(gql(get_query_from_txt))
    assert result == {'hello': 'World!'}