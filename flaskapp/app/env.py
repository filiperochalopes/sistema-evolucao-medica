import os

# Dados de autenticação
SECRET = os.getenv('SECRET_KEY')
MASTER_KEY = os.getenv('MASTER_KEY')
TOKEN_HOUR_EXPIRATION = os.getenv('TOKEN_HOUR_EXPIRATION', 6)

# Dados para criação de pdfs
# TODO o trecho "/app/app/" se repete muito ele deve ser criado com base em alguma variável base_url usando o pacote path do python ou algo semelhante

FONT_DIRECTORY = "/app/app/assets/pdfs_templates/Roboto-Mono.ttf"

# Templates Directorys
TEMPLATE_AIH_SUS_DIRECTORY = "/app/app/assets/pdfs_templates/aih_sus.pdf"
TEMPLATE_APAC_DIRECTORY = "/app/app/assets/pdfs_templates/apac.pdf"
TEMPLATE_EXAM_REQUEST_DIRECTORY = ["/app/app/assets/pdfs_templates/one_exam_request.pdf", "/app/app/assets/pdfs_templates/two_exam_request.pdf", "/app/app/assets/pdfs_templates/three_exam_request.pdf"]
TEMPLATE_FICHA_INTERN_DIRECTORY = "/app/app/assets/pdfs_templates/ficha_de_internamento_hmlem.pdf"
TEMPLATE_LME_DIRECTORY = "/app/app/assets/pdfs_templates/lme.pdf"
TEMPLATE_PRESCRICAO_MEDICA_DIRECTORY = "/app/app/assets/pdfs_templates/two_pages_precricao_medica_template.pdf"
TEMPLATE_RELATORIO_ALTA_DIRECTORY = "/app/app/assets/pdfs_templates/relatorio_de_alta.pdf"
TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY = "/app/app/assets/pdfs_templates/solicitacao_mamografia.pdf"

# Write directories when creating pdf that will be enconded to base64 
WRITE_AIH_SUS_DIRECTORY = "./graphql/mutations/pdfs/tests/pdfs_created_files_test/aih_sus_teste.pdf"
WRITE_APAC_DIRECTORY = "./graphql/mutations/pdfs/tests/pdfs_created_files_test/apac_teste.pdf"
WRITE_EXAM_REQUEST_DIRECTORY = "./graphql/mutations/pdfs/tests/pdfs_created_files_test/apac_teste.pdf"
WRITE_FICHA_INTERN_DIRECTORY = "./graphql/mutations/pdfs/tests/pdfs_created_files_test/ficha_teste.pdf"
WRITE_LME_DIRECTORY = "./graphql/mutations/pdfs/tests/pdfs_created_files_test/lme_teste.pdf"
WRITE_PRESCRICAO_MEDICA_DIRECTORY = "./graphql/mutations/pdfs/tests/pdfs_created_files_test/prescricao_medica_teste.pdf"
WRITE_RELATORIO_ALTA_DIRECTORY = "./graphql/mutations/pdfs/tests/pdfs_created_files_test/relatorio_alta_teste.pdf"
WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY = "./graphql/mutations/pdfs/tests/pdfs_created_files_test/solicit_mamografia_teste.pdf"

class InstitutionData:
    # Dados iniciais da instituição para cadastro do mesmo pelo `flask seed` para preenchimento de dados iniciais
    NAME = os.getenv('INSTITUTION_NAME', 'Hospital Maternidade Luís Eduardo Magalhães'),
    ADDRESS = os.getenv('INSTITUTION_ADDRESS', 'Av. Antônio Sérgio Carneiro, 122 - Centro - Água Fria/BA CEP 48170-000'),
    CNPJ = os.getenv('INSTITUTION_CNPJ', '13.606.702/0001-65'),
    DIRECTOR = os.getenv('INSTITUTION_DIRECTOR', 'Filipe Lopes'),
    CNES = os.getenv('INSTITUTION_CNES', '2602202'),