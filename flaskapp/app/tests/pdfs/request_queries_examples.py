from app.env import QUERIES_DIRECTORY
import os

def get_request_from_txt(filename:str):
    """Return as string with a request"""
    with open(f'{QUERIES_DIRECTORY}/{filename}', 'r') as file:
        request = file.read()
    return request


def get_all_tests_requests(filename_start:str):
    all_queries = []
    for file in os.listdir(QUERIES_DIRECTORY):
        if file.startswith(filename_start):
            all_queries.append(get_request_from_txt(file))

    return all_queries

## Requests strings
apac_request_string = get_request_from_txt('apac.txt') 
apac_required_data_request_string = get_request_from_txt('apac_required_data.txt') 

exam_request_request_string = get_request_from_txt('exam_request.txt')
exam_request_required_data_request_string = get_request_from_txt('exam_request_required_data.txt')
exam_request_2_pages_request_string = get_request_from_txt('exam_request_2_pages.txt')
exam_request_3_pages_request_string = get_request_from_txt('exam_request_3_pages.txt')

ficha_internamento_request_string = get_request_from_txt('ficha_internamento.txt')
ficha_internamento_required_data_request_string = get_request_from_txt('ficha_internamento_required_data.txt')

aih_sus_request_string = get_request_from_txt('aih_sus.txt')
aih_sus_required_data_request_string = get_request_from_txt('aih_sus_required_data.txt')

lme_request_string = get_request_from_txt('lme.txt')
lme_required_data_request_string = get_request_from_txt('lme_required_data.txt')

prescricao_medica_request_string = get_request_from_txt('prescricao_medica.txt')

relatorio_alta_request_string = get_request_from_txt('relatorio_alta.txt')
relatorio_alta_required_data_request_string = get_request_from_txt('relatorio_alta_required_data.txt')

solicit_mamografia_request_string = get_request_from_txt('solicit_mamografia.txt')
solicit_mamografia_required_data_request_string = get_request_from_txt('solicit_mamografia_required_data.txt')

folha_prescricao_request_string = get_request_from_txt('folha_prescricao.txt')

folha_evolucao_request_string = get_request_from_txt('folha_evolucao.txt')

balanco_hidrico_request_string = get_request_from_txt('balanco_hidrico.txt')

# evol_compact_request_string = get_request_from_txt('evol_compact.txt')
# evol_compact_required_data_request_string = get_request_from_txt('evol_compact_required_data.txt')

evol_compact_request_strings = get_all_tests_requests('evol_compact')
