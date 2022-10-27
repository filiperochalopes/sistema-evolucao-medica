import os

SECRET = os.getenv('SECRET_KEY')
MASTER_KEY = os.getenv('MASTER_KEY')
TOKEN_HOUR_EXPIRATION = os.getenv('TOKEN_HOUR_EXPIRATION', 6)

# Dados iniciais da instituição para cadastro do mesmo pelo `flask seed` para preenchimento de dados iniciais

class InstitutionData:
    NAME = os.getenv('INSTITUTION_NAME', 'Hospital Maternidade Luís Eduardo Magalhães'),
    ADDRESS = os.getenv('INSTITUTION_ADDRESS', 'Av. Antônio Sérgio Carneiro, 122 - Centro - Água Fria/BA CEP 48170-000'),
    CNPJ = os.getenv('INSTITUTION_CNPJ', '13.606.702/0001-65'),
    DIRECTOR = os.getenv('INSTITUTION_DIRECTOR', 'Filipe Lopes'),
    CNES = os.getenv('INSTITUTION_CNES', '2602202'),