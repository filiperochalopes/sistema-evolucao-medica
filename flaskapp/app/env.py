import os

# Dados de autenticação
SECRET = os.getenv('SECRET_KEY')
MASTER_KEY = os.getenv('MASTER_KEY')
TOKEN_HOUR_EXPIRATION = os.getenv('TOKEN_HOUR_EXPIRATION', 6)

# Dados para criação de pdfs
FONT_DIRECTORY = "/app/app/assets/pdfs_templates/Roboto-Mono.ttf"
BOLD_FONT_DIRECTORY = "/app/app/assets/pdfs_templates/Roboto-Condensed-Bold.ttf"
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
TEMPLATE_FOLHA_EVOLUCAO_DIRECTORY       = f"{TEMPLATE_BASE_URL}folha_evolucao.pdf"
TEMPLATE_BALANCO_HIDRICO_DIRECTORY      = f"{TEMPLATE_BASE_URL}balanco_hidrico.pdf"
TEMPLATE_FOLHA_PRESCRICAO_DIRECTORY     = f"{TEMPLATE_BASE_URL}folha_prescricao.pdf"

TMP_FILES_FOLDER = "/app/app/tests/files/tmp"

# Write directories when creating pdf that will be enconded to base64
WRITE_AIH_SUS_DIRECTORY             = f"{TMP_FILES_FOLDER}/aih_sus_teste.pdf"  
WRITE_APAC_DIRECTORY                = f"{TMP_FILES_FOLDER}/apac_teste.pdf"
WRITE_EXAM_REQUEST_DIRECTORY        = f"{TMP_FILES_FOLDER}/exam_request_teste.pdf"
WRITE_FICHA_INTERN_DIRECTORY        = f"{TMP_FILES_FOLDER}/ficha_teste.pdf"
WRITE_LME_DIRECTORY                 = f"{TMP_FILES_FOLDER}/lme_teste.pdf"
WRITE_PRESCRICAO_MEDICA_DIRECTORY   = f"{TMP_FILES_FOLDER}/prescricao_medica_teste.pdf"
WRITE_RELATORIO_ALTA_DIRECTORY      = f"{TMP_FILES_FOLDER}/relatorio_alta_teste.pdf"
WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY  = f"{TMP_FILES_FOLDER}/solicit_mamografia_teste.pdf"
WRITE_FOLHA_EVOLUCAO_DIRECTORY      = f"{TMP_FILES_FOLDER}/folha_evolucao_teste.pdf"
WRITE_BALANCO_HIDRICO_DIRECTORY     = f"{TMP_FILES_FOLDER}/balanco_hidrico_teste.pdf"
WRITE_FOLHA_PRESCRICAO_DIRECTORY    = f"{TMP_FILES_FOLDER}/folha_prescricao_teste.pdf"

# Write directires that tests will use to decode pdfs from base64 
WRITE_DECODE_AIH_SUS_DIRECTORY             = f"{TMP_FILES_FOLDER}/aih_sus_decoded_teste.tmp.pdf"
WRITE_DECODE_APAC_DIRECTORY                = f"{TMP_FILES_FOLDER}/apac_decoded_teste.tmp.pdf"
WRITE_DECODE_EXAM_REQUEST_DIRECTORY        = f"{TMP_FILES_FOLDER}/exam_request_decoded_teste.tmp.pdf"
WRITE_DECODE_EXAM_REQUEST_2_PAGES_DIRECTORY        = f"{TMP_FILES_FOLDER}/exam_request_2_pages_decoded_teste.tmp.pdf"
WRITE_DECODE_EXAM_REQUEST_3_PAGES_DIRECTORY        = f"{TMP_FILES_FOLDER}/exam_request_3_pages_decoded_teste.tmp.pdf"
WRITE_DECODE_FICHA_INTERN_DIRECTORY        = f"{TMP_FILES_FOLDER}/ficha_decoded_teste.tmp.pdf"
WRITE_DECODE_LME_DIRECTORY                 = f"{TMP_FILES_FOLDER}/lme_decoded_teste.tmp.pdf"
WRITE_DECODE_PRESCRICAO_MEDICA_DIRECTORY   = f"{TMP_FILES_FOLDER}/prescricao_medica_decoded_teste.tmp.pdf"
WRITE_DECODE_RELATORIO_ALTA_DIRECTORY      = f"{TMP_FILES_FOLDER}/relatorio_alta_decoded_teste.tmp.pdf"
WRITE_DECODE_SOLICIT_MAMOGRAFIA_DIRECTORY  = f"{TMP_FILES_FOLDER}/solicit_mamografia_decoded_teste.tmp.pdf"
WRITE_DECODE_FOLHA_EVOLUCAO_DIRECTORY       = f"{TMP_FILES_FOLDER}/folha_evolucao_decoded_teste.tmp.pdf"
WRITE_DECODE_BALANCO_HIDRICO_DIRECTORY      = f"{TMP_FILES_FOLDER}/balanco_hidrico_decoded_teste.tmp.pdf"
WRITE_DECODE_FOLHA_PRESCRICAO_DIRECTORY     = f"{TMP_FILES_FOLDER}/folha_prescricao_decoded_teste.tmp.pdf"
WRITE_DECODE_APAC_REQUIRED_DATA_DIRECTORY     = f"{TMP_FILES_FOLDER}apac_required_decoded_teste.tmp.pdf"
WRITE_DECODE_EXAM_REQUEST_REQUIRED_DATA_DIRECTORY     = f"{TMP_FILES_FOLDER}exam_request_required_decoded_teste.tmp.pdf"
WRITE_DECODE_FICHA_INTERN_REQUIRED_DATA_DIRECTORY     = f"{TMP_FILES_FOLDER}ficha_intern_required_decoded_teste.tmp.pdf"
WRITE_DECODE_AIH_SUS_REQUIRED_DATA_DIRECTORY     = f"{TMP_FILES_FOLDER}aih_sus_required_decoded_teste.tmp.pdf"
WRITE_DECODE_LME_REQUIRED_DATA_DIRECTORY     = f"{TMP_FILES_FOLDER}lme_required_decoded_teste.tmp.pdf"
WRITE_DECODE_RELATORIO_ALTA_REQUIRED_DATA_DIRECTORY     = f"{TMP_FILES_FOLDER}relatorio_alta_required_decoded_teste.tmp.pdf"
WRITE_DECODE_SOLICIT_MAMOGRAFIA_REQUIRED_DATA     = f"{TMP_FILES_FOLDER}solicit_mamogram_required_decoded_teste.tmp.pdf"

PDF_QUERIES_DIRECTORY = '/app/app/tests/pdfs/queries_examples'
QUERIES_DIRECTORY = '/app/app/tests/queries'

class InstitutionData:
    NAME = os.getenv('INSTITUTION_NAME', 'Hospital Maternidade Luís Eduardo Magalhães')
    ADDRESS = os.getenv('INSTITUTION_ADDRESS', 'Av. Antônio Sérgio Carneiro, 122 - Centro - Água Fria/BA CEP 48170-000')
    CNPJ = os.getenv('INSTITUTION_CNPJ', '13.606.702/0001-65')
    DIRECTOR = os.getenv('INSTITUTION_DIRECTOR', 'Filipe Lopes')
    CNES = os.getenv('INSTITUTION_CNES', '2602202')

class DatabaseSettings:
    def __init__(self, env='production') -> None:
        if env == 'production':
            self.HOST = 'db'
            self.PORT = 5432
        elif env == 'testing':
            self.HOST = 'db_test'
            self.PORT = 5433
        
        self.NAME = os.getenv('POSTGRES_NAME', 'hmlem')
        self.USER = os.getenv('POSTGRES_USER', 'postgres')
        self.PASSWORD = os.getenv('POSTGRES_PASS', '7xyed8uDyi0=')
        self.URL = f'postgresql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}'