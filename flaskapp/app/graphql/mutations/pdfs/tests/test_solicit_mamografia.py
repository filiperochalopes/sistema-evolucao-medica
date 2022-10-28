from pdfs import pdf_solicit_mamografia
import datetime
from flask import Response

global lenght_test
lenght_test = ''
for x in range(0, 1100):
    lenght_test += str(x)

datetime_to_use = datetime.datetime.now()

def data_to_use(
    patient_name='Patient Name',
    patient_cns=928976954930007,
    patient_mother_name='Patient Mother Name',
    patient_birthday=datetime_to_use,
    solicitation_datetime=datetime_to_use,
    prof_solicitor_name='Professional Name',
    nodule_lump='NAO',
    high_risk='NAOSABE',
    examinated_before='NAOSABE',
    mammogram_before=['SIM', '2020'],
    patient_age=23,
    health_unit_adressUF='SP',
    health_unit_cnes=1234567,
    health_unit_name="Health Unit Name",
    health_unit_adress_city='Unit City',
    health_unit_city_IBGEcode=1234567,
    document_chart_number=1234567895,
    protocol_number='5478546135245165',
    patient_sex='F',
    patient_surname='Patient Surname',
    patient_document_cpf={'CPF':28445400070},
    patient_nationality='Patient Nationality',
    patient_adress='Patient Adress',
    patient_adress_number=123456,
    patient_adress_adjunct='Patient Adress Adjunct',
    patient_adress_neighborhood='Neighborhood',
    patient_city_IBGEcode=1234567,
    patient_adress_city='Patient City',
    patient_adressUF='SP',
    patient_ethnicity=['INDIGENA', 'Indigena'],
    patient_adress_reference='Adress Reference',
    patient_schooling='SUPCOMPL',
    patient_adressCEP=12345678,
    exam_number=int(lenght_test[:10]),
    tracking_mammogram='JATRATADO',
    patient_phonenumber=1234567890,
    radiotherapy_before=['SIMESQ', '2020'],
    breast_surgery_before={
'did_not':False,
'biopsia_insinonal':(2021, 2020),
'biopsia_excisional':(2021, 2020),
'centraledomia':(2021, 2020),
'segmentectomia':None,
'dutectomia':(2021, 2020),
'mastectomia':(2021, 2020),
'mastectomia_poupadora_pele':(2021, 2020),
'mastectomia_poupadora_pele_complexo_areolo':(2021, 2020),
'linfadenectomia_axilar':(2021, 2020),
'biopsia_linfonodo':(2021, 2020),
'reconstrucao_mamaria':(2021, 2020),
'mastoplastia_redutora':(2021, 2020),
'indusao_implantes':(2021, 2020)
},
    diagnostic_mammogram={
'exame_clinico':
    {'direita':[
        'PAPILAR', 
        {'descarga_papilar': ['CRISTALINA', 'HEMORRAGICA'],
        'nodulo': ['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'],
        'espessamento':['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'],
        'linfonodo_palpavel':['AXILAR', 'SUPRACLAVICULAR']}
        ],
    'esquerda':[
        'PAPILAR', 
        {'descarga_papilar': ['CRISTALINA', 'HEMORRAGICA'],
        'nodulo': ['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'],
        'espessamento':['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'],
        'linfonodo_palpavel':['AXILAR', 'SUPRACLAVICULAR']}
        ]
    },
'controle_radiologico':
    {'direita': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo'],
    'esquerda': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo']
    },
'lesao_diagnostico':
    {'direita': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo'],
    'esquerda': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo']
    },
'avaliacao_resposta':
    ['direita', 'esquerda'],
'revisao_mamografia_lesao':
    {'direita': ['0', '3', '4', '5'],
    'esquerda': ['0', '3', '4', '5']
    },
'controle_lesao':
    {'direita': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo'],
    'esquerda': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo']
    }
}):
    return pdf_solicit_mamografia.fill_pdf_solicit_mamografia(
        patient_name,
        patient_cns,
        patient_mother_name,
        patient_birthday,
        solicitation_datetime,
        prof_solicitor_name,
        nodule_lump,
        high_risk,
        examinated_before,
        mammogram_before,
        patient_age,
        health_unit_adressUF,
        health_unit_cnes,
        health_unit_name,
        health_unit_adress_city,
        health_unit_city_IBGEcode,
        document_chart_number,
        protocol_number,
        patient_sex,
        patient_surname,
        patient_document_cpf,
        patient_nationality,
        patient_adress,
        patient_adress_number,
        patient_adress_adjunct,
        patient_adress_neighborhood,
        patient_city_IBGEcode,
        patient_adress_city,
        patient_adressUF,
        patient_ethnicity,
        patient_adress_reference,
        patient_schooling,
        patient_adressCEP,
        exam_number,
        tracking_mammogram,
        patient_phonenumber,
        radiotherapy_before,
        breast_surgery_before,
        diagnostic_mammogram)


def test_with_data_in_function():
    assert type(data_to_use()) != type(Response())

def test_answer_with_all_fields():
    assert data_to_use().response == type(Response())
    #assert type(data_to_use()) != type(Response())

def test_awnser_with_only_required_data():

    assert type(pdf_solicit_mamografia.fill_pdf_solicit_mamografia(patient_name='Patient Name',patient_cns=928976954930007,patient_mother_name='Patient Mother Name',patient_birthday=datetime_to_use,solicitation_datetime=datetime_to_use,prof_solicitor_name='Professional Name',        nodule_lump='NAO',        high_risk='NAOSABE',        examinated_before='NAOSABE',        mammogram_before=['SIM', '2020'],        patient_age=23,)) != type(Response())




















































