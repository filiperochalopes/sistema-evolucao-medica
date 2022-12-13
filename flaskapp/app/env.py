import os

# Dados de autenticação
SECRET = os.getenv('SECRET_KEY')
MASTER_KEY = os.getenv('MASTER_KEY')
TOKEN_HOUR_EXPIRATION = os.getenv('TOKEN_HOUR_EXPIRATION', 6)

# Dados para criação de pdfs

FONT_DIRECTORY = "/app/app/assets/pdfs_templates/Roboto-Mono.ttf"
GRAPHQL_MUTATION_QUERY_URL = "http://localhost:5000/api/v1/graphql"

# Templates Directorys
TEMPLATE_BASE_URL = "/app/app/assets/pdfs_templates/"
TEMPLATE_AIH_SUS_DIRECTORY              = f"{TEMPLATE_BASE_URL}aih_sus.pdf"
TEMPLATE_APAC_DIRECTORY                 = f"{TEMPLATE_BASE_URL}apac.pdf"
TEMPLATE_EXAM_REQUEST_DIRECTORY         = [f"{TEMPLATE_BASE_URL}one_exam_request.pdf", f"{TEMPLATE_BASE_URL}two_exam_request.pdf", f"{TEMPLATE_BASE_URL}three_exam_request.pdf"]
TEMPLATE_FICHA_INTERN_DIRECTORY         = f"{TEMPLATE_BASE_URL}ficha_de_internamento_hmlem.pdf"
TEMPLATE_LME_DIRECTORY                  = f"{TEMPLATE_BASE_URL}lme.pdf"
TEMPLATE_PRESCRICAO_MEDICA_DIRECTORY    = f"{TEMPLATE_BASE_URL}two_pages_precricao_medica_template.pdf"
TEMPLATE_RELATORIO_ALTA_DIRECTORY       = f"{TEMPLATE_BASE_URL}relatorio_de_alta.pdf"
TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY   = f"{TEMPLATE_BASE_URL}solicitacao_mamografia.pdf"

# Write directories when creating pdf that will be enconded to base64
WRITE_BASE_URL = "/app/app/tests/files/tmp/"
WRITE_AIH_SUS_DIRECTORY             = f"{WRITE_BASE_URL}aih_sus_teste.pdf"
WRITE_APAC_DIRECTORY                = f"{WRITE_BASE_URL}apac_teste.pdf"
WRITE_EXAM_REQUEST_DIRECTORY        = f"{WRITE_BASE_URL}exam_request_teste.pdf"
WRITE_FICHA_INTERN_DIRECTORY        = f"{WRITE_BASE_URL}ficha_teste.pdf"
WRITE_LME_DIRECTORY                 = f"{WRITE_BASE_URL}lme_teste.pdf"
WRITE_PRESCRICAO_MEDICA_DIRECTORY   = f"{WRITE_BASE_URL}prescricao_medica_teste.pdf"
WRITE_RELATORIO_ALTA_DIRECTORY      = f"{WRITE_BASE_URL}relatorio_alta_teste.pdf"
WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY  = f"{WRITE_BASE_URL}solicit_mamografia_teste.pdf"

# Write directires that tests will use to decode pdfs from base64 
WRITE_DECODE_BASE_URL = "/app/app/tests/files/tmp/"
WRITE_DECODE_AIH_SUS_DIRECTORY             = f"{WRITE_DECODE_BASE_URL}aih_sus_teste.tmp.pdf"
WRITE_DECODE_APAC_DIRECTORY                = f"{WRITE_DECODE_BASE_URL}apac_teste.tmp.pdf"
WRITE_DECODE_EXAM_REQUEST_DIRECTORY        = f"{WRITE_DECODE_BASE_URL}exam_request_teste.tmp.pdf"
WRITE_DECODE_FICHA_INTERN_DIRECTORY        = f"{WRITE_DECODE_BASE_URL}ficha_teste.tmp.pdf"
WRITE_DECODE_LME_DIRECTORY                 = f"{WRITE_DECODE_BASE_URL}lme_teste.tmp.pdf"
WRITE_DECODE_PRESCRICAO_MEDICA_DIRECTORY   = f"{WRITE_DECODE_BASE_URL}prescricao_medica_teste.tmp.pdf"
WRITE_DECODE_RELATORIO_ALTA_DIRECTORY      = f"{WRITE_DECODE_BASE_URL}relatorio_alta_teste.tmp.pdf"
WRITE_DECODE_SOLICIT_MAMOGRAFIA_DIRECTORY  = f"{WRITE_DECODE_BASE_URL}solicit_mamografia_teste.tmp.pdf"




class InstitutionData:
    # Dados iniciais da instituição para cadastro do mesmo pelo `flask seed` para preenchimento de dados iniciais
    NAME = os.getenv('INSTITUTION_NAME', 'Hospital Maternidade Luís Eduardo Magalhães'),
    ADDRESS = os.getenv('INSTITUTION_ADDRESS', 'Av. Antônio Sérgio Carneiro, 122 - Centro - Água Fria/BA CEP 48170-000'),
    CNPJ = os.getenv('INSTITUTION_CNPJ', '13.606.702/0001-65'),
    DIRECTOR = os.getenv('INSTITUTION_DIRECTOR', 'Filipe Lopes'),
    CNES = os.getenv('INSTITUTION_CNES', '2602202'),