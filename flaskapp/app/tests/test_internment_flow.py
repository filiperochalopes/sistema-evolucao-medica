from gql import gql
import jwt
from app.env import SECRET
from app.tests.conftest import get_query_from_txt


class TestInternmentFlow:
    create_user_query = gql(get_query_from_txt('create_user'))
    hello_query = gql(get_query_from_txt('hello'))
    signin_query = gql(get_query_from_txt('signin'))
    alembic_version_query = gql(get_query_from_txt('alembic_version'))
    create_internment_query = gql(get_query_from_txt('create_internment'))
    create_evolution_query = gql(get_query_from_txt('create_evolution'))
    create_prescription_query = gql(get_query_from_txt('create_prescription'))
    create_measure_query = gql(get_query_from_txt('create_measure'))
    create_fluid_balance_query_1 = gql(get_query_from_txt('create_fluid_balance_1'))
    create_fluid_balance_query_2 = gql(get_query_from_txt('create_fluid_balance_2'))
    create_pending_query = gql(get_query_from_txt('create_pending'))

    def test_graphql_query(self, client):
        '''Verifica se a API está funcional'''
        result = client.execute(self.hello_query)
        assert result == {'hello': 'World!'}

    def test_migration(self, client):
        '''Verifica se o banco de dados está com algum registro de migração'''
        result = client.execute(self.alembic_version_query)
        assert isinstance(result['alembicVersion']['version'], str)

    def test_create_user(self, client):
        try:
            # Reconectando banco de dados, após exclusão manual que geralmente é feita antes de rodar o script de teste. A primeira execução não funciona, queixa de um erro de desligamento do banco de dados pelo administrador
            result = client.execute(self.create_user_query)
        except Exception as e:
            result = client.execute(self.create_user_query)
        assert int(result['createUser']['id']) > 0

    def test_signin(self, client):
        result = client.execute(self.signin_query)
        token = result['signin']['token']
        decoded_jwt = jwt.decode(token, SECRET, algorithms=["HS256"])
        assert isinstance(decoded_jwt, dict)

    def test_create_internement_and_new_patient(self, auth_client):
        result = auth_client.execute(self.create_internment_query)
        assert int(result['createInternment']['id']) > 0

    def test_write_an_evolution(self, auth_client):
        result = auth_client.execute(self.create_evolution_query)
        assert int(result['createEvolution']['id']) > 0

    def test_write_a_prescription(self, auth_client):
        result = auth_client.execute(self.create_prescription_query)
        assert int(result['createPrescription']['id']) > 0
    
    def test_take_measures(self, auth_client):
        result = auth_client.execute(self.create_measure_query)
        assert int(result['createMeasure']['id']) > 0
    
    def test_add_fluid_balance_input(self, auth_client):
        result = auth_client.execute(self.create_fluid_balance_query_1)
        assert int(result['createFluidBalance']['id']) > 0
        result = auth_client.execute(self.create_fluid_balance_query_2)
        assert int(result['createFluidBalance']['id']) > 0

    def test_write_a_pending_message(self, auth_client):
        result = auth_client.execute(self.create_pending_query)
        assert int(result['createPending']['id']) > 0
