from werkzeug.test import Client
from werkzeug.wrappers import Response

from ariadne.constants import DATA_TYPE_JSON
from ariadne.types import ExtensionSync
from ariadne.wsgi import GraphQL


# Add TestClient to keep test similar to ASGI
class TestClient(Client):
    __test__ = False

    def __init__(self, app):
        super().__init__(app, Response)


def test_hero_name_query(schema):
    app = GraphQL(schema, context_value={"test": "TEST-CONTEXT"})
    _, result = app.execute_query({}, {"query": "{ testContext }"})
    assert result == {"data": {"testContext": "TEST-CONTEXT"}}
    query = gql(
        '''
        mutation {
            createUser(
                masterKey: "passw@rd"
                user: {
                    name: "Filipe Rocha Lopes"
                    email: "contato@filipelopes.med.br"
                    phone: "71992518950"
                    password: "passw@rd"
                    cpf: "01817013599"
                    cns: "856077573000002"
                    birthdate: "1995-12-01"
                    professionalCategory: "doc"
                    professionalDocumentUf: "BA"
                    professionalDocumentNumber: "37825"
            }){
                id
                email
                name
                professionalCategory
                professionalDocumentUf
            }
        }
        '''
    )
    print(client.execute(query), file=sys.stderr)
    assert 1 == 1