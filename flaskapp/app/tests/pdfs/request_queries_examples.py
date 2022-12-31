QUERIES_DIRECTORY = '/app/app/tests/pdfs/queries_examples/'

def get_request_from_txt(filename:str):
    """Return as string with a request"""
    with open(f'{QUERIES_DIRECTORY}{filename}', 'r') as file:
        request = file.read()
    file.close()
    return request


## Requests strings
apac_request_string = get_request_from_txt('apac.txt') 

exam_request_request_string = get_request_from_txt('exam_request.txt')

exam_request_2_pages_request_string = get_request_from_txt('exam_request_2_pages.txt')

exam_request_3_pages_request_string = get_request_from_txt('exam_request_3_pages.txt')

ficha_internamento_request_string = get_request_from_txt('ficha_internamento.txt')

aih_sus_request_string = get_request_from_txt('aih_sus.txt')

lme_request_string = get_request_from_txt('lme.txt')

prescricao_medica_request_string = get_request_from_txt('prescricao_medica.txt')

relatorio_alta_request_string = get_request_from_txt('relatorio_alta.txt')

solicit_mamografia_request_string = get_request_from_txt('solicit_mamografia.txt')

folha_prescricao_request_string = get_request_from_txt('folha_prescricao.txt')