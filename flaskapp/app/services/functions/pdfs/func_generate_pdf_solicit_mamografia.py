import datetime
from app.services.utils.PdfSolicitMamografia import PdfSolicitMamografia


def func_generate_pdf_solicit_mamografia(patient_name:str, patient_cns:str, patient_mother_name:str, patient_birthday:datetime.datetime, nodule_lump:str, high_risk:str, examinated_before:str, mammogram_before:list, patient_age:int, solicitation_datetime:datetime.datetime, prof_solicitor_name:str, health_unit_adress_uf:str=None, health_unit_cnes:int=None, health_unit_name:str=None, health_unit_adress_city:str=None, health_unit_city_ibge_code:str=None, document_chart_number:str=None, protocol_number:str=None, patient_sex:str=None, patient_surname:str=None, patient_document_cpf:dict=None, patient_nationality:str=None, patient_adress:str=None, patient_adress_number:int=None, patient_adress_adjunct:str=None, patient_adress_neighborhood:str=None, patient_city_ibge_code:str=None, patient_adress_city:str=None, patient_adress_uf:str=None, patient_ethnicity:list=None, patient_adress_reference:str=None, patient_schooling:str=None, patient_adress_cep:str=None, patient_phonenumber:str=None, radiotherapy_before:list=None, breast_surgery_before:dict=None, exam_number:str=None, tracking_mammogram:str=None, diagnostic_mammogram:dict=None) -> str:
    """Fill solicitacion mamografia (Solicitacao de Mamografia) 
    Args:
        patient_name (str): Patient Name
        patient_cns (str): patient_cns
        patient_mother_name (str): patient_mother_name
        patient_birthday (datetime.datetime): patient_birthday
        nodule_lump (str): nodule_lump
        high_risk (str): high_risk
        examinated_before (str): examinated_before
        mammogram_before (list): list with option and year, ['SIM', '2020']
        patient_age (int): patient_age
        solicitation_datetime (datetime.datetime): solicitation_datetime
        prof_solicitor_name (str): prof_solicitor_name
        health_unit_adress_uf (str, optional): health_unit_adress_uf. Defaults to None.
        health_unit_cnes (int, optional): health_unit_cnes. Defaults to None.
        health_unit_name (str, optional): health_unit_name. Defaults to None.
        health_unit_adress_city (str, optional): health_unit_adress_city. Defaults to None.
        health_unit_city_ibge_code (str, optional): health_unit_city_ibge_code. Defaults to None.
        document_chart_number (str, optional): document_chart_number. Defaults to None.
        protocol_number (str, optional): protocol_number. Defaults to None.
        patient_sex (str, optional): patient_sex. Defaults to None.
        patient_surname (str, optional): patient_surname. Defaults to None.
        patient_document_cpf (dict, optional): CPF dict format patient_document_cpf, {'CPF':1111111111}. Defaults to None.
        patient_nationality (str, optional): patient_nationality. Defaults to None.
        patient_adress (str, optional): patient_adress. Defaults to None.
        patient_adress_number (int, optional): patient_adress_number. Defaults to None.
        patient_adress_adjunct (str, optional): patient_adress_adjunct. Defaults to None.
        patient_adress_neighborhood (str, optional): patient_adress_neighborhood. Defaults to None.
        patient_city_ibge_code (str, optional): patient_city_ibge_code. Defaults to None.
        patient_adress_city (str, optional): patient_adress_city. Defaults to None.
        patient_adress_uf (str, optional): patient_adress_uf. Defaults to None.
        patient_ethnicity (list, optional): patient_ethnicity. Defaults to None.
        patient_adress_reference (str, optional): patient_adress_reference. Defaults to None.
        patient_schooling (str, optional): patient_schooling. Defaults to None.
        patient_adress_cep (str, optional): patient_adress_cep. Defaults to None.
        patient_phonenumber (int, optional): patient_phonenumber. Defaults to None.
        radiotherapy_before (list, optional): Option and year, eg ['SIMESQ', '2020']. Defaults to None.
        breast_surgery_before (dict, optional): dict with opions and years, eg:
        {
    'didNot':False,
    'biopsiaInsinonal':(2021, 2020),
    'biopsiaExcisional':(2021, 2020),
    'centraledomia':(2021, 2020),
    'segmentectomia':None,
    'dutectomia':(2021, 2020),
    'mastectomia':(2021, 2020),
    'mastectomiaPoupadoraPele':(2021, 2020),
    'mastectomiaPoupadoraPeleComplexoAreolo':(2021, 2020),
    'linfadenectomiaAxilar':(2021, 2020),
    'biopsiaLinfonodo':(2021, 2020),
    'reconstrucaoMamaria':(2021, 2020),
    'mastoplastiaRedutora':(2021, 2020),
    'indusaoImplantes':(2021, 2020)
    }. Defaults to None.
        exam_number (int, optional): exam_number. Defaults to None.
        tracking_mammogram (str, optional): tracking_mammogram. Defaults to None.
        diagnostic_mammogram (dict, optional): diagnostic mammogram option. eg:
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
        }. Defaults to None.

    Returns:
        str: Request with pdf in base64
    """    
    try:
        pdf = PdfSolicitMamografia()

        # Writing all data in respective fields
        # not null data

        try:
            pdf.add_cns(cns=patient_cns, pos=(46, 676), camp_name='Patient CNS', interval=' ')
            pdf.add_datetime(date=patient_birthday, pos=(48, 563), camp_name='Patient Birthday', hours=False, interval=' ', formated=False, interval_between_numbers=' ')
            
            pdf.add_markable_square_and_onelinetext(option=mammogram_before[0], valid_options=['SIM', 'NAO', 'NAOSABE'], text_options=['SIM'], options_positions=((51,64), (51,52), (51, 40)), camp_name='Has made mamogram before', square_size=(15,9), len_max=4, len_min=4, text=mammogram_before[1], text_pos=(200, 68), interval=' ')
            pdf.add_oneline_intnumber(number=patient_age, pos=(217, 563), camp_name='Patient Birthday', len_max=2, len_min=1,value_min=1, value_max=99, interval=' ')

            pdf.set_font('Roboto-Mono', 13)
            pdf.add_morelines_text(text=patient_name, initial_pos=(47, 653), decrease_ypos=18, camp_name='Patient Name', len_max=42, len_min=7, interval=' ', char_per_lines=87)
            pdf.add_oneline_text(text=patient_mother_name, pos=(47, 612), camp_name='Patient Mother Name', len_max=42, len_min=7, interval=' ')
            
            pdf.set_font('Roboto-Mono', 9)
            pdf.add_markable_square(option=nodule_lump, valid_options=['SIMDIR', 'SIMESQ', 'NAO'], options_positions=((50,332), (50,320), (50, 310)), camp_name='Has nodule lump', square_size=(15,9))
            pdf.add_markable_square(option=high_risk, valid_options=['SIM', 'NAO', 'NAOSABE'], options_positions=((51,278), (51,266), (51, 255)), camp_name='Has high risk', square_size=(15,9))
            pdf.add_markable_square(option=examinated_before, valid_options=['SIM', 'NUNCA', 'NAOSABE'], options_positions=((51,120), (51,107), (51, 94)), camp_name='Has been examinated before', square_size=(15,9))
        
        except Exception as error:
            raise error
        except:
            raise Exception('Algum erro nao diagnoticado ocorreu enquanto adicionava dados obrigatorios na pagina 1')

        #Adding data that can be null
        try:
            pdf.set_font('Roboto-Mono', 13)
            pdf.add_UF(uf=health_unit_adress_uf, pos=(47, 762), camp_name='Health Unit Adress UF', nullable=True, interval=' ')
            pdf.add_oneline_text(text=health_unit_name, pos=(47, 741), camp_name='Health Unit Name', len_max=42, len_min=7, interval=' ', nullable=True)
            pdf.add_oneline_text(text=health_unit_adress_city, pos=(168, 720), camp_name='Health Unit Adress City', len_max=14, len_min=3, interval=' ', nullable=True)
            pdf.add_oneline_text(text=patient_surname, pos=(288, 635), camp_name='Patient Surname', len_max=18, len_min=4, interval=' ', nullable=True)
            pdf.add_oneline_text(text=patient_adress, pos=(47, 529), camp_name='Patient Adress', len_max=42, len_min=7, interval=' ', nullable=True)
            pdf.add_oneline_text(text=patient_adress_adjunct, pos=(168, 507), camp_name='Patient Adress Adjunct', len_max=25, len_min=7, interval=' ', nullable=True)
            pdf.add_oneline_text(text=patient_adress_neighborhood, pos=(292, 484), camp_name='Patient Adress Neighborhood', len_max=14, len_min=7, interval=' ', nullable=True)
            pdf.add_oneline_text(text=patient_adress_reference, pos=(47, 413), camp_name='Patient Adress Reference', len_max=33, len_min=4, interval=' ', nullable=True)
            pdf.add_oneline_text(text=patient_adress_city, pos=(167, 461), camp_name='Patient Adress City', len_max=15, len_min=3, interval=' ', nullable=True)
            pdf.add_patient_adress_cep(number=patient_adress_cep)            
            pdf.add_patient_phonenumber(number=patient_phonenumber)            
            pdf.add_radiotherapy_before(radiotherapy_before=radiotherapy_before)
            pdf.add_breast_surgery_before(breast_surgery_before=breast_surgery_before)

            pdf.set_font('Roboto-Mono', 12)
            pdf.add_oneline_intnumber(number=health_unit_cnes, pos=(178, 761), camp_name='Health Unit CNES', len_max=7, len_min=7,value_min=0, value_max=99999999, interval=' ', nullable=True)
            pdf.add_oneline_text(text=protocol_number, pos=(406, 768), camp_name='Protocol Number', len_max=23, len_min=1, nullable=True)
            pdf.add_document_cns_cpf_rg(document=patient_document_cpf, pos_cpf=(52, 589),camp_name='Patient Document CPF', interval=' ', nullable=True)
            pdf.add_oneline_intnumber(number=patient_adress_number, pos=(52, 506), camp_name='Patient Adress Number', len_max=6, len_min=1, value_min=0, value_max=999999, interval=' ', nullable=True)
            pdf.add_UF(uf=patient_adress_uf, pos=(535, 484), camp_name='Patient Adress UF', nullable=True, interval=' ')


            pdf.set_font('Roboto-Mono', 9)
            pdf.add_oneline_text(text=health_unit_city_ibge_code, pos=(47, 720), camp_name='Health Unit City IBGE code', len_max=7, len_min=7, nullable=True, interval='  ')
            pdf.add_oneline_text(text=document_chart_number, pos=(410, 720), camp_name='Document Chart Number', len_max=10, len_min=1, nullable=True, interval='  ')
            pdf.add_sex_square(sex=patient_sex, pos_male=(291, 672), pos_fem=(338, 672), camp_name='Patient Sex', square_size=(11,9), nullable=True)
            pdf.add_oneline_text(text=patient_nationality, pos=(278, 587), camp_name='Patient Nationality', len_max=32, len_min=3, nullable=True)
            pdf.add_oneline_text(text=patient_city_ibge_code, pos=(47, 461), camp_name='Patient City IBGE code', len_max=7, len_min=7, nullable=True, interval='  ')
            if patient_ethnicity == None:
                patient_ethnicity = [None, None]
            if type(patient_ethnicity) != type(list()):
                raise Exception('Etnia do paciente (Patient ethnicity) deve ser uma lista')
            pdf.add_markable_square_and_onelinetext(option=patient_ethnicity[0], valid_options=['BRANCA','PRETA', 'PARDA', 'AMARELA', 'INDIGENA'], text_options=['INDIGENA'], text_pos=(516, 563), options_positions=((278, 560), (323, 560),(363, 560),(401, 560), (450, 560)), camp_name='Patient Ethinicity', len_max=10, text=patient_ethnicity[1], len_min=4, square_size=(11, 9), nullable=True)
            pdf.add_markable_square(option=patient_schooling, valid_options=['ANALFABETO', 'FUNDINCOM', 'FUNDCOMPL', 'MEDIOCOMPL', 'SUPCOMPL'], options_positions=((55, 380), (115, 381), (223, 381), (325, 381), (408, 381)), camp_name='Patient Schooling', square_size=(10,9), nullable=True)
            
        except Exception as error:
            return error
        except:
            return Exception('Erro critico ocorreu enquanto adicionava dados opcionais na pagina 1')


### Add Page 2
        pdf.change_canvas()

        try:
            pdf.add_oneline_text(text=prof_solicitor_name, pos=(206, 346), camp_name='Professional Solicitor Name', len_max=23, len_min=7, interval=' ')

            pdf.set_font('Roboto-Mono', 12)
            pdf.add_datetime(date=solicitation_datetime, pos=(48, 346), camp_name='Solicitation Datetime', hours=False, interval=' ', formated=False, interval_between_numbers=' ')
            pdf.add_oneline_text(text=exam_number, pos=(114, 324), camp_name='Exam number', len_max=16, len_min=1, nullable=True, interval=' ')
            pdf.set_font('Roboto-Mono', 9)
            pdf.add_markable_square(option=tracking_mammogram, valid_options=['POPALVO', 'RISCOELEVADO', 'JATRATADO'], options_positions=((56, 374), (152, 374), (328, 374)), camp_name='Tracking Mammogram', square_size=(11,10), nullable=True)
            pdf.add_diagnostic_mammogram(diagnostic_mammogram=diagnostic_mammogram)

        except Exception as error:
            return error
        except:
            return Exception('Algum erro nao diagnoticado ocorreu enquanto adicionava dados obrigatorios na pagina 2')


        #Get pdf base64
        pdf_base64_enconded = pdf.get_base64()

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except Exception as error:
        return error
    except:
        return Exception("Erro critico enquanto preenchia o documento de Solicitacao de Mamografia")

