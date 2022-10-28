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
    mammogram_before=['nao', "2020"],
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
        }}
):
    return pdf_solicit_mamografia.fill_pdf_solicit_mamografia(
        patient_name=patient_name,
    patient_cns=patient_cns,
    patient_mother_name=patient_mother_name,
    patient_birthday=patient_birthday,
    solicitation_datetime=solicitation_datetime,
    prof_solicitor_name=prof_solicitor_name,
    nodule_lump=nodule_lump,
    high_risk=high_risk,
    examinated_before=examinated_before,
    patient_age=patient_age,
    health_unit_adressUF=health_unit_adressUF,
    health_unit_cnes=health_unit_cnes,
    health_unit_name=health_unit_name,
    health_unit_adress_city=health_unit_adress_city,
    health_unit_city_IBGEcode=health_unit_city_IBGEcode,
    document_chart_number=document_chart_number,
    protocol_number=protocol_number,
    patient_sex=patient_sex,
    patient_surname=patient_surname,
    patient_document_cpf=patient_document_cpf,
    patient_nationality=patient_nationality,
    patient_adress=patient_adress,
    patient_adress_number=patient_adress_number,
    patient_adress_adjunct=patient_adress_adjunct,
    patient_adress_neighborhood=patient_adress_neighborhood,
    patient_city_IBGEcode=patient_city_IBGEcode,
    patient_adress_city=patient_adress_city,
    patient_adressUF=patient_adressUF,
    patient_ethnicity=patient_ethnicity,
    patient_adress_reference=patient_adress_reference,
    patient_schooling=patient_schooling,
    patient_adressCEP=patient_adressCEP,
    exam_number=exam_number,
    tracking_mammogram=tracking_mammogram,
    patient_phonenumber=patient_phonenumber,
    radiotherapy_before=radiotherapy_before,
    breast_surgery_before=breast_surgery_before,
    diagnostic_mammogram=diagnostic_mammogram,
    mammogram_before=mammogram_before)


def test_with_data_in_function():
    assert type(data_to_use()) != type(Response())

def test_answer_with_all_fields():
    assert type(data_to_use()) == type(bytes())
    #assert type(data_to_use()) != type(Response())

def test_awnser_with_only_required_data():

    assert type(pdf_solicit_mamografia.fill_pdf_solicit_mamografia(patient_name='Patient Name',patient_cns=928976954930007,patient_mother_name='Patient Mother Name',patient_birthday=datetime_to_use,solicitation_datetime=datetime_to_use,prof_solicitor_name='Professional Name',        nodule_lump='NAO',        high_risk='NAOSABE',        examinated_before='NAOSABE',        mammogram_before=['SIM', '2020'],        patient_age=23,)) != type(Response())


##############################################################
# ERRORS IN NAMES CAMPS
# patient_name
# patient_surname
# patient_mother_name
# prof_solicitor_name
# health_unit_name
# !!!!!!! TESTING !!!!!!!
# Name empty
# Name with space
# long name
# short name
# wrong name type

def test_empty_patient_name():    
    assert data_to_use(patient_name='').status == Response(status=400).status

def test_with_space_patient_name():    
    assert data_to_use(patient_name='  ').status == Response(status=400).status

def test_long_patient_name():    
    assert data_to_use(patient_name=lenght_test[:45]).status == Response(status=400).status

def test_short_patient_name():    
    assert data_to_use(patient_name='bro').status == Response(status=400).status

def test_wrongtype_patient_name():    
    assert data_to_use(patient_name=123124).status == Response(status=400).status

def test_empty_patient_surname():    
    assert type(data_to_use(patient_surname='')) != type(Response())

def test_with_space_patient_surname():    
    assert type(data_to_use(patient_surname='')) != type(Response())

def test_long_patient_surname():    
    assert data_to_use(patient_surname=lenght_test[:21]).status == Response(status=400).status

def test_short_patient_surname():    
    assert data_to_use(patient_surname='bro').status == Response(status=400).status

def test_wrongtype_patient_surname():    
    assert data_to_use(patient_surname=123124).status == Response(status=400).status

def test_empty_patient_mother_name():    
    assert data_to_use(patient_mother_name='').status == Response(status=400).status

def test_with_space_patient_mother_name():    
    assert data_to_use(patient_mother_name='  ').status == Response(status=400).status

def test_long_patient_mother_name():    
    assert data_to_use(patient_mother_name=lenght_test[:45]).status == Response(status=400).status

def test_short_patient_mother_name():    
    assert data_to_use(patient_mother_name='bro').status == Response(status=400).status

def test_wrongtype_patient_mother_name():    
    assert data_to_use(patient_mother_name=123124).status == Response(status=400).status

def test_empty_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='').status == Response(status=400).status

def test_with_space_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='  ').status == Response(status=400).status

def test_long_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=lenght_test[:25]).status == Response(status=400).status

def test_short_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='bro').status == Response(status=400).status

def test_wrongtype_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=123124).status == Response(status=400).status

def test_empty_health_unit_name():    
    assert type(data_to_use(health_unit_name='')) != type(Response())

def test_with_space_health_unit_name():    
    assert type(data_to_use(health_unit_name='')) != type(Response())

def test_long_health_unit_name():    
    assert data_to_use(health_unit_name=lenght_test[:45]).status == Response(status=400).status

def test_short_health_unit_name():    
    assert data_to_use(health_unit_name='bro').status == Response(status=400).status

def test_wrongtype_health_unit_name():    
    assert data_to_use(health_unit_name=123124).status == Response(status=400).status


####################################################################
# TEST CNES 
# health_unit_cnes
# empty
# wrong type
# invalid cnes

def test_none_empty_health_unit_cnes():
    assert type(data_to_use(health_unit_cnes=None)) != type(Response())

def test_empty_health_unit_cnes():
    assert data_to_use(health_unit_cnes='').status == Response(status=400).status

def test_wrongtype_health_unit_cnes():
    assert data_to_use(health_unit_cnes='adsadad').status == Response(status=400).status

def test_invalidcnes_health_unit_cnes():
    assert data_to_use(health_unit_cnes=451236548).status == Response(status=400).status

#################################################################
# TEST DOCUMENTS CNS AND CPF
# patient_cns
# patient_document_cpf
# wrong type
# invalid cns
# invalid cpf
# wrong option

def test_wrongtype_patient_cns():
    assert data_to_use(patient_cns='451236548').status == Response(status=400).status

def test_invalid_patient_cns():
    assert data_to_use(patient_cns=451236548554).status == Response(status=400).status

def test_wrongtype_patient_document_cpf():
    assert data_to_use(patient_document_cpf='451236548554').status == Response(status=400).status

def test_invalidcns_patient_document_cpf():
    assert data_to_use(patient_document_cpf={'CNS':284123312123}).status == Response(status=400).status

def test_invalidccpf_patient_document_cpf():
    assert data_to_use(patient_document_cpf={'CPF':284123312123}).status == Response(status=400).status

def test_wrongoption_patient_document_cpf():
    assert data_to_use(patient_document_cpf={'CNS':284123312123}).status == Response(status=400).status

#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_datetime
# test wrong type
# test valid datetime

def test_wrongtype_patient_birthday():
    assert data_to_use(patient_birthday='bahabah').status == Response(status=400).status

def test_valid_patient_birthday():
    assert type(data_to_use(patient_birthday=datetime_to_use)) != type(Response())

def test_wrongtype_solicitation_datetime():
    assert data_to_use(solicitation_datetime='bahabah').status == Response(status=400).status

def test_valid_solicitation_datetime():
    assert type(data_to_use(solicitation_datetime=datetime_to_use)) != type(Response())

##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# nodule_lump
# high_risk
# examinated_before
# patient_ethnicity
# patient_schooling
# tracking_mammogram
# test wrong type
# test not exist option
# test all options in Upper Case
# test all options in lower Case

def test_wrongtype_patient_sex():
    assert data_to_use(patient_sex=1231).status == Response(status=400).status

def test_notexistopiton_patient_sex():
    assert data_to_use(patient_sex='G').status == Response(status=400).status

def test_M_optionUpper_patient_sex():
    assert type(data_to_use(patient_sex='M')) != type(Response())

def test_M_optionLower_patient_sex():
    assert type(data_to_use(patient_sex='m')) != type(Response())

def test_F_optionUpper_patient_sex():
    assert type(data_to_use(patient_sex='F')) != type(Response())

def test_F_optionLower_patient_sex():
    assert type(data_to_use(patient_sex='f')) != type(Response())

def test_wrongtype_nodule_lump():
    assert data_to_use(nodule_lump=1231).status == Response(status=400).status

def test_notexistopiton_nodule_lump():
    assert data_to_use(nodule_lump='Gaa').status == Response(status=400).status

def test_SIMDIR_optionUpper_nodule_lump():
    assert type(data_to_use(nodule_lump='SIMDIR')) != type(Response())

def test_SIMDIR_optionLower_nodule_lump():
    assert type(data_to_use(nodule_lump='simdir')) != type(Response())

def test_SIMESQ_optionUpper_nodule_lump():
    assert type(data_to_use(nodule_lump='SIMESQ')) != type(Response())

def test_SIMESQ_optionLower_nodule_lump():
    assert type(data_to_use(nodule_lump='simesq')) != type(Response())

def test_NAO_optionUpper_nodule_lump():
    assert type(data_to_use(nodule_lump='NAO')) != type(Response())

def test_NAO_optionLower_nodule_lump():
    assert type(data_to_use(nodule_lump='nao')) != type(Response())

def test_wrongtype_high_risk():
    assert data_to_use(high_risk=1231).status == Response(status=400).status

def test_notexistopiton_high_risk():
    assert data_to_use(high_risk='Gaa').status == Response(status=400).status

def test_SIM_optionUpper_high_risk():
    assert type(data_to_use(high_risk='SIM')) != type(Response())

def test_SIM_optionLower_high_risk():
    assert type(data_to_use(high_risk='sim')) != type(Response())

def test_NAOSABE_optionUpper_high_risk():
    assert type(data_to_use(high_risk='NAOSABE')) != type(Response())

def test_NAOSABE_optionLower_high_risk():
    assert type(data_to_use(high_risk='naosabe')) != type(Response())

def test_NAO_optionUpper_high_risk():
    assert type(data_to_use(high_risk='NAO')) != type(Response())

def test_NAO_optionLower_high_risk():
    assert type(data_to_use(high_risk='nao')) != type(Response())

def test_wrongtype_examinated_before():
    assert data_to_use(examinated_before=1231).status == Response(status=400).status

def test_notexistopiton_examinated_before():
    assert data_to_use(examinated_before='Gaa').status == Response(status=400).status

def test_SIM_optionUpper_examinated_before():
    assert type(data_to_use(examinated_before='SIM')) != type(Response())

def test_SIM_optionLower_examinated_before():
    assert type(data_to_use(examinated_before='sim')) != type(Response())

def test_NUNCA_optionUpper_examinated_before():
    assert type(data_to_use(examinated_before='NUNCA')) != type(Response())

def test_NUNCA_optionLower_examinated_before():
    assert type(data_to_use(examinated_before='nunca')) != type(Response())

def test_NAOSABE_optionUpper_examinated_before():
    assert type(data_to_use(examinated_before='NAOSABE')) != type(Response())

def test_NAOSABE_optionLower_examinated_before():
    assert type(data_to_use(examinated_before='naosabe')) != type(Response())

def test_wrongtype_patient_ethnicity():
    assert data_to_use(patient_ethnicity=1231).status == Response(status=400).status

def test_notexistopiton_patient_ethnicity():
    assert data_to_use(patient_ethnicity='Gaa').status == Response(status=400).status

def test_BRANCA_optionUpper_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=['BRANCA', 'ehinith'])) != type(Response())

def test_BRANCA_optionLower_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=['branca', 'ehinith'])) != type(Response())

def test_PRETA_optionUpper_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=['PRETA', 'ehinith'])) != type(Response())

def test_PRETA_optionLower_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=['preta', 'ehinith'])) != type(Response())

def test_PARDA_optionUpper_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=['PARDA', 'ehinith'])) != type(Response())

def test_PARDA_optionLower_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=['parda', 'ehinith'])) != type(Response())

def test_AMARELA_optionUpper_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=['AMARELA', 'ehinith'])) != type(Response())

def test_AMARELA_optionLower_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=['amarela', 'ehinith'])) != type(Response())

def test_INDIGENA_optionUpper_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=['INDIGENA', 'ehinith'])) != type(Response())

def test_INDIGENA_optionLower_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=['indigena', 'ehinith'])) != type(Response())


def test_wrongtype_patient_schooling():
    assert data_to_use(patient_schooling=1231).status == Response(status=400).status

def test_notexistopiton_patient_schooling():
    assert data_to_use(patient_schooling='Gaa').status == Response(status=400).status

def test_ANALFABETO_optionUpper_patient_schooling():
    assert type(data_to_use(patient_schooling='ANALFABETO')) != type(Response())

def test_ANALFABETO_optionLower_patient_schooling():
    assert type(data_to_use(patient_schooling='analfabeto')) != type(Response())

def test_FUNDINCOM_optionUpper_patient_schooling():
    assert type(data_to_use(patient_schooling='FUNDINCOM')) != type(Response())

def test_FUNDINCOM_optionLower_patient_schooling():
    assert type(data_to_use(patient_schooling='fundincom')) != type(Response())

def test_FUNDCOMPL_optionUpper_patient_schooling():
    assert type(data_to_use(patient_schooling='FUNDCOMPL')) != type(Response())

def test_FUNDCOMPL_optionLower_patient_schooling():
    assert type(data_to_use(patient_schooling='fundcompl')) != type(Response())

def test_MEDIOCOMPL_optionUpper_patient_schooling():
    assert type(data_to_use(patient_schooling='MEDIOCOMPL')) != type(Response())

def test_MEDIOCOMPL_optionLower_patient_schooling():
    assert type(data_to_use(patient_schooling='mediocompl')) != type(Response())

def test_SUPCOMPL_optionUpper_patient_schooling():
    assert type(data_to_use(patient_schooling='SUPCOMPL')) != type(Response())

def test_SUPCOMPL_optionLower_patient_schooling():
    assert type(data_to_use(patient_schooling='supcompl')) != type(Response())

def test_wrongtype_tracking_mammogram():
    assert data_to_use(tracking_mammogram=1231).status == Response(status=400).status

def test_notexistopiton_tracking_mammogram():
    assert data_to_use(tracking_mammogram='Gaa').status == Response(status=400).status

def test_POPALVO_optionUpper_tracking_mammogram():
    assert type(data_to_use(tracking_mammogram='POPALVO')) != type(Response())

def test_POPALVO_optionLower_tracking_mammogram():
    assert type(data_to_use(tracking_mammogram='popalvo')) != type(Response())

def test_RISCOELEVADO_optionUpper_tracking_mammogram():
    assert type(data_to_use(tracking_mammogram='RISCOELEVADO')) != type(Response())

def test_RISCOELEVADO_optionLower_tracking_mammogram():
    assert type(data_to_use(tracking_mammogram='riscoelevado')) != type(Response())

def test_JATRATADO_optionUpper_tracking_mammogram():
    assert type(data_to_use(tracking_mammogram='JATRATADO')) != type(Response())

def test_JATRATADO_optionLower_tracking_mammogram():
    assert type(data_to_use(tracking_mammogram='jatratado')) != type(Response())











