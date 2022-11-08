from app.graphql.mutations.pdfs import pdf_solicit_mamografia
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
    health_unit_adress_uf='SP',
    health_unit_cnes=1234567,
    health_unit_name="Health Unit Name",
    health_unit_adress_city='Unit City',
    health_unit_city_ibge_code=1234567,
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
    patient_city_ibge_code=1234567,
    patient_adress_city='Patient City',
    patient_adress_uf='SP',
    patient_ethnicity=['INDIGENA', 'Indigena'],
    patient_adress_reference='Adress Reference',
    patient_schooling='SUPCOMPL',
    patient_adress_cep=12345678,
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
    health_unit_adress_uf=health_unit_adress_uf,
    health_unit_cnes=health_unit_cnes,
    health_unit_name=health_unit_name,
    health_unit_adress_city=health_unit_adress_city,
    health_unit_city_ibge_code=health_unit_city_ibge_code,
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
    patient_city_ibge_code=patient_city_ibge_code,
    patient_adress_city=patient_adress_city,
    patient_adress_uf=patient_adress_uf,
    patient_ethnicity=patient_ethnicity,
    patient_adress_reference=patient_adress_reference,
    patient_schooling=patient_schooling,
    patient_adress_cep=patient_adress_cep,
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


####################################################################
# TEST ADRESS VARIABLES
# health_unit_adress_uf
# health_unit_adress_city
# health_unit_city_ibge_code
# patient_city_ibge_code
# patient_adress
# patient_adress_number
# patient_adress_adjunct
# patient_adress_neighborhood
# patient_adress_city
# patient_adress_uf (already tested in option tests)
# patient_adress_reference
# patient_adress_cep
# test wrong type
# test empty value
# test empty space value
# invalid value
# Long value

def test_wrongtype_patient_adress():
    assert data_to_use(patient_adress=1212312).status == Response(status=400).status

def test_empty_value_patient_adress():
    assert type(data_to_use(patient_adress='')) != type(Response())

def test_empty_space_patient_adress():
    assert type(data_to_use(patient_adress='  ')) != type(Response())

def test_invalid_value_patient_adress():
    assert data_to_use(patient_adress='111').status == Response(status=400).status

def test_long_value_patient_adress():
    assert data_to_use(patient_adress=lenght_test[:45]).status == Response(status=400).status

def test_wrongtype_patient_adress_city():
    assert data_to_use(patient_adress_city=1212312).status == Response(status=400).status

def test_empty_value_patient_adress_city():
    assert type(data_to_use(patient_adress_city='')) != type(Response())

def test_empty_space_patient_adress_city():
    assert type(data_to_use(patient_adress_city='  ')) != type(Response())

def test_invalid_value_patient_adress_city():
    assert data_to_use(patient_adress_city='111').status == Response(status=400).status

def test_long_value_patient_adress_city():
    assert data_to_use(patient_adress_city=lenght_test[:20]).status == Response(status=400).status

def test_wrongtype_health_unit_adress_city():
    assert data_to_use(health_unit_adress_city=1212312).status == Response(status=400).status

def test_empty_value_health_unit_adress_city():
    assert type(data_to_use(health_unit_adress_city='')) != type(Response())

def test_empty_space_health_unit_adress_city():
    assert type(data_to_use(health_unit_adress_city='  ')) != type(Response())

def test_invalid_value_health_unit_adress_city():
    assert data_to_use(health_unit_adress_city='111').status == Response(status=400).status

def test_long_value_patient_adress_adjunct():
    assert data_to_use(patient_adress_adjunct=lenght_test[:30]).status == Response(status=400).status

def test_wrongtype_patient_adress_adjunct():
    assert data_to_use(patient_adress_adjunct=1212312).status == Response(status=400).status

def test_empty_value_patient_adress_adjunct():
    assert type(data_to_use(patient_adress_adjunct='')) != type(Response())

def test_empty_space_patient_adress_adjunct():
    assert type(data_to_use(patient_adress_adjunct='  ')) != type(Response())

def test_invalid_value_patient_adress_adjunct():
    assert data_to_use(patient_adress_adjunct='111').status == Response(status=400).status

def test_long_value_patient_adress_neighborhood():
    assert data_to_use(patient_adress_neighborhood=lenght_test[:20]).status == Response(status=400).status

def test_wrongtype_patient_adress_neighborhood():
    assert data_to_use(patient_adress_neighborhood=1212312).status == Response(status=400).status

def test_empty_value_patient_adress_neighborhood():
    assert type(data_to_use(patient_adress_neighborhood='')) != type(Response())

def test_empty_space_patient_adress_neighborhood():
    assert type(data_to_use(patient_adress_neighborhood='  ')) != type(Response())

def test_invalid_value_patient_adress_neighborhood():
    assert data_to_use(patient_adress_neighborhood='111').status == Response(status=400).status

def test_long_value_patient_adress_reference():
    assert data_to_use(patient_adress_reference=lenght_test[:35]).status == Response(status=400).status

def test_wrongtype_patient_adress_reference():
    assert data_to_use(patient_adress_reference=1212312).status == Response(status=400).status

def test_empty_value_patient_adress_reference():
    assert type(data_to_use(patient_adress_reference='')) != type(Response())

def test_empty_space_patient_adress_reference():
    assert type(data_to_use(patient_adress_reference='  ')) != type(Response())

def test_invalid_value_patient_adress_reference():
    assert data_to_use(patient_adress_reference='111').status == Response(status=400).status

def test_wrongtype_health_unit_city_ibge_code():
    assert data_to_use(health_unit_city_ibge_code='1212312').status == Response(status=400).status

def test_empty_value_health_unit_city_ibge_code():
    assert data_to_use(health_unit_city_ibge_code='').status == Response(status=400).status

def test_empty_space_health_unit_city_ibge_code():
    assert data_to_use(health_unit_city_ibge_code='  ').status == Response(status=400).status

def test_invalid_value_health_unit_city_ibge_code():
    assert data_to_use(health_unit_city_ibge_code=2411).status == Response(status=400).status

def test_long_value_health_unit_city_ibge_code():
    assert data_to_use(health_unit_city_ibge_code=52352352352352352352352352352).status == Response(status=400).status

def test_wrongtype_patient_city_ibge_code():
    assert data_to_use(patient_city_ibge_code='1212312').status == Response(status=400).status

def test_empty_value_patient_city_ibge_code():
    assert data_to_use(patient_city_ibge_code='').status == Response(status=400).status

def test_empty_space_patient_city_ibge_code():
    assert data_to_use(patient_city_ibge_code='  ').status == Response(status=400).status

def test_invalid_value_patient_city_ibge_code():
    assert data_to_use(patient_city_ibge_code=2411).status == Response(status=400).status

def test_long_value_patient_city_ibge_code():
    assert data_to_use(patient_city_ibge_code=52352352352352352352352352352).status == Response(status=400).status
def test_wrongtype_patient_adress_number():
    assert data_to_use(patient_adress_number='1212312').status == Response(status=400).status

def test_empty_value_patient_adress_number():
    assert data_to_use(patient_adress_number='').status == Response(status=400).status

def test_empty_space_patient_adress_number():
    assert data_to_use(patient_adress_number='  ').status == Response(status=400).status

def test_invalid_value_patient_adress_number():
    assert data_to_use(patient_adress_number=123456789).status == Response(status=400).status

def test_long_value_patient_adress_number():
    assert data_to_use(patient_adress_number=52352352352352352352352352352).status == Response(status=400).status

def test_wrongtype_patient_adress_cep():
    assert data_to_use(patient_adress_cep='1212312').status == Response(status=400).status

def test_empty_value_patient_adress_cep():
    assert data_to_use(patient_adress_cep='').status == Response(status=400).status

def test_empty_space_patient_adress_cep():
    assert data_to_use(patient_adress_cep='  ').status == Response(status=400).status

def test_invalid_value_patient_adress_cep():
    assert data_to_use(patient_adress_cep=2411).status == Response(status=400).status

def test_long_value_patient_adress_cep():
    assert data_to_use(patient_adress_cep=52352352352352352352352352352).status == Response(status=400).status

def test_wrongtype_patient_adress_uf():
    assert data_to_use(patient_adress_uf=1231).status == Response(status=400).status

def test_notexistopiton_patient_adress_uf():
    assert data_to_use(patient_adress_uf='AUYD').status == Response(status=400).status

def test_AC_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AC')) != type(Response())

def test_AC_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ac')) != type(Response())

def test_AL_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AL')) != type(Response())

def test_AL_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='al')) != type(Response())

def test_AP_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AP')) != type(Response())

def test_AP_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ap')) != type(Response())

def test_AM_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AM')) != type(Response())

def test_AM_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='am')) != type(Response())

def test_BA_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='BA')) != type(Response())

def test_BA_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ba')) != type(Response())

def test_CE_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='CE')) != type(Response())

def test_CE_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ce')) != type(Response())

def test_DF_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='DF')) != type(Response())

def test_DF_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='df')) != type(Response())

def test_ES_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ES')) != type(Response())

def test_ES_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='es')) != type(Response())

def test_GO_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='GO')) != type(Response())

def test_GO_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='go')) != type(Response())

def test_MA_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MA')) != type(Response())

def test_MA_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ma')) != type(Response())

def test_MS_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MS')) != type(Response())

def test_MS_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ms')) != type(Response())

def test_MT_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MT')) != type(Response())

def test_MT_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='mt')) != type(Response())

def test_MG_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MG')) != type(Response())

def test_MG_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='mg')) != type(Response())

def test_PA_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PA')) != type(Response())

def test_PA_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pa')) != type(Response())

def test_PB_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PB')) != type(Response())

def test_PB_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pb')) != type(Response())

def test_PR_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PR')) != type(Response())

def test_PR_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pr')) != type(Response())

def test_PE_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PE')) != type(Response())

def test_PE_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pe')) != type(Response())

def test_PI_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PI')) != type(Response())

def test_PI_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pi')) != type(Response())

def test_RJ_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RJ')) != type(Response())

def test_RJ_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rj')) != type(Response())

def test_RN_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RN')) != type(Response())

def test_RN_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rn')) != type(Response())

def test_RS_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RS')) != type(Response())

def test_RS_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rs')) != type(Response())

def test_RO_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RO')) != type(Response())

def test_RO_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ro')) != type(Response())

def test_RR_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RR')) != type(Response())

def test_RR_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rr')) != type(Response())

def test_SC_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='SC')) != type(Response())

def test_SC_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='sc')) != type(Response())

def test_SP_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='SP')) != type(Response())

def test_SP_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='sp')) != type(Response())

def test_SE_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='SE')) != type(Response())

def test_SE_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='se')) != type(Response())

def test_TO_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='TO')) != type(Response())

def test_TO_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='to')) != type(Response())

def test_wrongtype_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf=1231).status == Response(status=400).status

def test_notexistopiton_health_unit_adress_uf():
    assert data_to_use(health_unit_adress_uf='AUYD').status == Response(status=400).status

def test_AC_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='AC')) != type(Response())

def test_AC_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='ac')) != type(Response())

def test_AL_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='AL')) != type(Response())

def test_AL_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='al')) != type(Response())

def test_AP_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='AP')) != type(Response())

def test_AP_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='ap')) != type(Response())

def test_AM_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='AM')) != type(Response())

def test_AM_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='am')) != type(Response())

def test_BA_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='BA')) != type(Response())

def test_BA_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='ba')) != type(Response())

def test_CE_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='CE')) != type(Response())

def test_CE_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='ce')) != type(Response())

def test_DF_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='DF')) != type(Response())

def test_DF_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='df')) != type(Response())

def test_ES_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='ES')) != type(Response())

def test_ES_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='es')) != type(Response())

def test_GO_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='GO')) != type(Response())

def test_GO_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='go')) != type(Response())

def test_MA_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='MA')) != type(Response())

def test_MA_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='ma')) != type(Response())

def test_MS_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='MS')) != type(Response())

def test_MS_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='ms')) != type(Response())

def test_MT_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='MT')) != type(Response())

def test_MT_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='mt')) != type(Response())

def test_MG_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='MG')) != type(Response())

def test_MG_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='mg')) != type(Response())

def test_PA_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='PA')) != type(Response())

def test_PA_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='pa')) != type(Response())

def test_PB_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='PB')) != type(Response())

def test_PB_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='pb')) != type(Response())

def test_PR_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='PR')) != type(Response())

def test_PR_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='pr')) != type(Response())

def test_PE_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='PE')) != type(Response())

def test_PE_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='pe')) != type(Response())

def test_PI_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='PI')) != type(Response())

def test_PI_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='pi')) != type(Response())

def test_RJ_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='RJ')) != type(Response())

def test_RJ_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='rj')) != type(Response())

def test_RN_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='RN')) != type(Response())

def test_RN_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='rn')) != type(Response())

def test_RS_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='RS')) != type(Response())

def test_RS_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='rs')) != type(Response())

def test_RO_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='RO')) != type(Response())

def test_RO_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='ro')) != type(Response())

def test_RR_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='RR')) != type(Response())

def test_RR_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='rr')) != type(Response())

def test_SC_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='SC')) != type(Response())

def test_SC_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='sc')) != type(Response())

def test_SP_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='SP')) != type(Response())

def test_SP_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='sp')) != type(Response())

def test_SE_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='SE')) != type(Response())

def test_SE_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='se')) != type(Response())

def test_TO_optionUpper_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='TO')) != type(Response())

def test_TO_optionLower_health_unit_adress_uf():
    assert type(data_to_use(health_unit_adress_uf='to')) != type(Response())


#############################################################################
# TEST BIG TEXT WITH LINE BRAKES
# patient_name
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

def test_wrong_type_patient_name():
    assert data_to_use(patient_name=131).status == Response(status=400).status

def test_empty_value_patient_name():
    assert data_to_use(patient_name='').status == Response(status=400).status

def test_empty_spaces_patient_name():
    assert data_to_use(patient_name='    ').status == Response(status=400).status

def test_shortText_patient_name():
    assert data_to_use(patient_name='abla').status == Response(status=400).status

def test_more_than_limit_patient_name():
    assert data_to_use(patient_name=lenght_test[:45]).status == Response(status=400).status

#############################################################################
# NORMAL TEXT VARIABLES THAT CAN BE NULL
# protocol_number
# patient_nationality
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

def test_wrong_type_protocol_number():
    assert data_to_use(protocol_number=131).status == Response(status=400).status

def test_empty_value_protocol_number():
    assert type(data_to_use(protocol_number='')) != type(Response())

def test_empty_spaces_protocol_number():
    assert type(data_to_use(protocol_number='    ')) != type(Response())

def test_more_than_limit_protocol_number():
    assert data_to_use(protocol_number=lenght_test[:30]).status == Response(status=400).status

def test_wrong_type_patient_nationality():
    assert data_to_use(patient_nationality=131).status == Response(status=400).status

def test_empty_value_patient_nationality():
    assert type(data_to_use(patient_nationality='')) != type(Response())

def test_empty_spaces_patient_nationality():
    assert type(data_to_use(patient_nationality='    ')) != type(Response())

def test_shortText_patient_nationality():
    assert data_to_use(patient_nationality='aa').status == Response(status=400).status

def test_more_than_limit_patient_nationality():
    assert data_to_use(patient_nationality=lenght_test[:35]).status == Response(status=400).status


#################################################################################
# TEST INT VARIABLES CAN/CANNOT BE NULL
# document_chart_number
# exam_number
# patient_phonenumber
# !!!!! TESTING
# wrong type
# test empty value
# test empty space
# short value
# long value  

def test_wrong_type_document_chart_number():
    assert data_to_use(document_chart_number='131').status == Response(status=400).status

def test_empty_value_document_chart_number():
    assert data_to_use(document_chart_number='').status == Response(status=400).status

def test_empty_spaces_document_chart_number():
    assert data_to_use(document_chart_number='    ').status == Response(status=400).status

def test_longValue_document_chart_number():
    assert data_to_use(document_chart_number=int(lenght_test[:15])).status == Response(status=400).status

def test_wrong_type_exam_number():
    assert data_to_use(exam_number='131').status == Response(status=400).status

def test_empty_value_exam_number():
    assert data_to_use(exam_number='').status == Response(status=400).status

def test_empty_spaces_exam_number():
    assert data_to_use(exam_number='    ').status == Response(status=400).status

def test_longValue_exam_number():
    assert data_to_use(exam_number=int(lenght_test[:20])).status == Response(status=400).status

def test_wrong_type_patient_phonenumber():
    assert data_to_use(patient_phonenumber='131').status == Response(status=400).status

def test_empty_value_patient_phonenumber():
    assert data_to_use(patient_phonenumber='').status == Response(status=400).status

def test_empty_spaces_patient_phonenumber():
    assert data_to_use(patient_phonenumber='    ').status == Response(status=400).status

def test_longValue_patient_phonenumber():
    assert data_to_use(patient_phonenumber=int(lenght_test[:14])).status == Response(status=400).status


#################################################################################
# TEST markable square and oneline text
# radiotherapy_before
# patient_ethnicity
# mammogram_before
# test wrong type
# short value
# long value  
# test not exist option
# test all options in Upper Case
# test all options in lower Case

def test_empty_spaces_patient_ethnicity():
    assert data_to_use(patient_ethnicity='    ').status == Response(status=400).status

def test_longValue_patient_ethnicity():
    assert data_to_use(patient_ethnicity=['INDIGENA', lenght_test[:15]]).status == Response(status=400).status

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

def test_empty_spaces_radiotherapy_before():
    assert data_to_use(radiotherapy_before='    ').status == Response(status=400).status

def test_longValue_radiotherapy_before():
    assert data_to_use(radiotherapy_before=['SIMDIR', lenght_test[:6]]).status == Response(status=400).status

def test_wrongtype_radiotherapy_before():
    assert data_to_use(radiotherapy_before=1231).status == Response(status=400).status

def test_notexistopiton_radiotherapy_before():
    assert data_to_use(radiotherapy_before='Gaa').status == Response(status=400).status

def test_SIMDIR_optionUpper_radiotherapy_before():
    assert type(data_to_use(radiotherapy_before=['SIMDIR', '2020'])) != type(Response())

def test_SIMDIR_optionLower_radiotherapy_before():
    assert type(data_to_use(radiotherapy_before=['simdir', '2020'])) != type(Response())

def test_SIMESQ_optionUpper_radiotherapy_before():
    assert type(data_to_use(radiotherapy_before=['SIMESQ', '2020'])) != type(Response())

def test_SIMESQ_optionLower_radiotherapy_before():
    assert type(data_to_use(radiotherapy_before=['simesq', '2020'])) != type(Response())

def test_NAO_optionUpper_radiotherapy_before():
    assert type(data_to_use(radiotherapy_before=['NAO', '2020'])) != type(Response())

def test_NAO_optionLower_radiotherapy_before():
    assert type(data_to_use(radiotherapy_before=['nao', '2020'])) != type(Response())

def test_NAOSABE_optionUpper_radiotherapy_before():
    assert type(data_to_use(radiotherapy_before=['NAOSABE', '2020'])) != type(Response())

def test_NAOSABE_optionLower_radiotherapy_before():
    assert type(data_to_use(radiotherapy_before=['naosabe', '2020'])) != type(Response())


#############################################################################
# test breast_surgery_before
# test wrong type
# test wrong type in value
# short value
# long value  
# test not exist option




def test_empty_spaces_breast_surgery_before():
    assert data_to_use(breast_surgery_before='    ').status == Response(status=400).status

def test_longValue_breast_surgery_before():
    assert data_to_use(breast_surgery_before={
'did_not':False,
"biopsia_insinonal":(654556, 216),
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
}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_did_not():
    assert data_to_use(breast_surgery_before={"did_not":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_biopsia_insinonal():
    assert data_to_use(breast_surgery_before={"biopsia_insinonal":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_biopsia_excisional():
    assert data_to_use(breast_surgery_before={"biopsia_excisional":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_centraledomia():
    assert data_to_use(breast_surgery_before={"centraledomia":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_segmentectomia():
    assert data_to_use(breast_surgery_before={"segmentectomia":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_dutectomia():
    assert data_to_use(breast_surgery_before={"dutectomia":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_mastectomia():
    assert data_to_use(breast_surgery_before={"mastectomia":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_mastectomia_poupadora_pele():
    assert data_to_use(breast_surgery_before={"mastectomia_poupadora_pele":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_mastectomia_poupadora_pele_complexo_areolo():
    assert data_to_use(breast_surgery_before={"mastectomia_poupadora_pele_complexo_areolo":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_linfadenectomia_axilar():
    assert data_to_use(breast_surgery_before={"linfadenectomia_axilar":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_biopsia_linfonodo():
    assert data_to_use(breast_surgery_before={"biopsia_linfonodo":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_reconstrucao_mamaria():
    assert data_to_use(breast_surgery_before={"reconstrucao_mamaria":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_mastoplastia_redutora():
    assert data_to_use(breast_surgery_before={"mastoplastia_redutora":'worntype'}).status == Response(status=400).status

def test_wrongtype_breast_surgery_before_indusao_implantes():
    assert data_to_use(breast_surgery_before={"indusao_implantes":'worntype'}).status == Response(status=400).status

def test_notexistopiton_breast_surgery_before():
    assert type(data_to_use(breast_surgery_before={"nonedxistas":(334, 41)})) != type(Response())


#############################################################################
# test diagnostic_mammogram
# test wrong type
# test wrong type in value
# short value
# long value  
# test not exist option

def test_empty_spaces_diagnostic_mammogram():
    assert data_to_use(diagnostic_mammogram='    ').status == Response(status=400).status

def test_wrongtype_diagnostic_mammogram():
    assert data_to_use(diagnostic_mammogram={
    'exame_clinico':[
        [
            'PAPILAR', 
            {'123': 12121221,
            'nodulo': ['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'],
            'espessamento':['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'],
            'linfonodo_palpavel':['AXILAR', 'SUPRACLAVICULAR']}
            ],
        [
            'PAPILAR', 
            {'descarga_papilar': ['CRISTALINA', 'HEMORRAGICA'],
            'nodulo': ['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'],
            'espessamento':['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'],
            'linfonodo_palpavel':['AXILAR', 'SUPRACLAVICULAR']}
            ]
        ]}).status == Response(status=400).status


def test_right_diagnostic_mammogram_exame_clinico():
    assert type(data_to_use(diagnostic_mammogram={
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
        }})) != type(Response())

def test_right_diagnostic_mammogram_controle_radiologico():
    assert type(data_to_use(diagnostic_mammogram={
        'controle_radiologico':
        {'direita': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo'],
        'esquerda': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo']
        }
        })) != type(Response())

def test_right_diagnostic_mammogram_lesao_diagnostico():
    assert type(data_to_use(diagnostic_mammogram={
        'lesao_diagnostico':
        {'direita': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo'],
        'esquerda': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo']
        }})) != type(Response())

def test_right_diagnostic_mammogram_avaliacao_resposta():
    assert type(data_to_use(diagnostic_mammogram={
        'avaliacao_resposta':
        ['direita', 'esquerda']})) != type(Response())

def test_right_diagnostic_mammogram_revisao_mamografia_lesao():
    assert type(data_to_use(diagnostic_mammogram={
        'revisao_mamografia_lesao':
        {'direita': ['0', '3', '4', '5'],
        'esquerda': ['0', '3', '4', '5']
        }})) != type(Response())

def test_right_diagnostic_mammogram_revisao_controle_lesao():
    assert type(data_to_use(diagnostic_mammogram={
        'controle_lesao':
        {'direita': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo'],
        'esquerda': ['nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo']
        }})) != type(Response())

























