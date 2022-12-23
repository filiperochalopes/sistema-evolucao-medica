import datetime
from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from app.services.utils import pdf_functions
from app.env import FONT_DIRECTORY, TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY, WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY
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

        packet = io.BytesIO()
        # Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        packet_2 = io.BytesIO()
        # Create canvas and add data
        c_2 = canvas.Canvas(packet_2, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        c.setFont('Roboto-Mono', 13)
        c_2.setFont('Roboto-Mono', 13)
        # Writing all data in respective fields
        # not null data

        try:
            pdf.add_cns(cns=patient_cns, pos=(46, 676), camp_name='Patient CNS', interval=' ')
            c = pdf_functions.add_cns(can=c, cns=patient_cns, pos=(46, 676), camp_name='Patient CNS', interval=' ')
            c = pdf_functions.add_datetime(can=c, date=patient_birthday, pos=(48, 563), camp_name='Patient Birthday', hours=False, interval=' ', formated=False, interval_between_numbers=' ')
            
            c = pdf_functions.add_markable_square_and_onelinetext(can=c, option=mammogram_before[0], valid_options=['SIM', 'NAO', 'NAOSABE'], text_options=['SIM'], options_positions=((51,64), (51,52), (51, 40)), camp_name='Has made mamogram before', square_size=(15,9), len_max=4, len_min=4, text=mammogram_before[1], text_pos=(200, 68), interval=' ')
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_age, pos=(217, 563), camp_name='Patient Birthday', len_max=2, len_min=1,value_min=1, value_max=99, interval=' ')


            c.setFont('Roboto-Mono', 13)
            c = pdf_functions.add_morelines_text(can=c, text=patient_name, initial_pos=(47, 653), decrease_ypos=18, camp_name='Patient Name', len_max=42, len_min=7, interval=' ', char_per_lines=87)
            c = pdf_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(47, 612), camp_name='Patient Mother Name', len_max=42, len_min=7, interval=' ')
            
            
            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_markable_square(can=c, option=nodule_lump, valid_options=['SIMDIR', 'SIMESQ', 'NAO'], options_positions=((50,332), (50,320), (50, 310)), camp_name='Has nodule lump', square_size=(15,9))
            c = pdf_functions.add_markable_square(can=c, option=high_risk, valid_options=['SIM', 'NAO', 'NAOSABE'], options_positions=((51,278), (51,266), (51, 255)), camp_name='Has high risk', square_size=(15,9))
            c = pdf_functions.add_markable_square(can=c, option=examinated_before, valid_options=['SIM', 'NUNCA', 'NAOSABE'], options_positions=((51,120), (51,107), (51, 94)), camp_name='Has been examinated before', square_size=(15,9))
        
        except Exception as error:
            raise error
        except:
            raise Exception('Algum erro nao diagnoticado ocorreu enquanto adicionava dados obrigatorios na pagina 1')

        #Adding data that can be null
        try:
            c.setFont('Roboto-Mono', 13)
            c = pdf_functions.add_UF(can=c, uf=health_unit_adress_uf, pos=(47, 762), camp_name='Health Unit Adress UF', nullable=True, interval=' ')
            c = pdf_functions.add_oneline_text(can=c, text=health_unit_name, pos=(47, 741), camp_name='Health Unit Name', len_max=42, len_min=7, interval=' ', nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=health_unit_adress_city, pos=(168, 720), camp_name='Health Unit Adress City', len_max=14, len_min=3, interval=' ', nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_surname, pos=(288, 635), camp_name='Patient Surname', len_max=18, len_min=4, interval=' ', nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress, pos=(47, 529), camp_name='Patient Adress', len_max=42, len_min=7, interval=' ', nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_adjunct, pos=(168, 507), camp_name='Patient Adress Adjunct', len_max=25, len_min=7, interval=' ', nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_neighborhood, pos=(292, 484), camp_name='Patient Adress Neighborhood', len_max=14, len_min=7, interval=' ', nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_reference, pos=(47, 413), camp_name='Patient Adress Reference', len_max=33, len_min=4, interval=' ', nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_city, pos=(167, 461), camp_name='Patient Adress City', len_max=15, len_min=3, interval=' ', nullable=True)
            c = add_patient_adress_cep(can=c, number=patient_adress_cep)            
            c = add_patient_phonenumber(can=c, number=patient_phonenumber)            
            c = add_radiotherapy_before(can=c, radiotherapy_before=radiotherapy_before)
            c = add_breast_surgery_before(can=c, breast_surgery_before=breast_surgery_before)



            c.setFont('Roboto-Mono', 12)
            c = pdf_functions.add_oneline_intnumber(can=c, number=health_unit_cnes, pos=(178, 761), camp_name='Health Unit CNES', len_max=7, len_min=7,value_min=0, value_max=99999999, interval=' ', nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=protocol_number, pos=(406, 768), camp_name='Protocol Number', len_max=23, len_min=1, nullable=True)
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=patient_document_cpf, pos_cpf=(52, 589),camp_name='Patient Document CPF', interval=' ', nullable=True)
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_adress_number, pos=(52, 506), camp_name='Patient Adress Number', len_max=6, len_min=1, value_min=0, value_max=999999, interval=' ', nullable=True)
            c = pdf_functions.add_UF(can=c, uf=patient_adress_uf, pos=(535, 484), camp_name='Patient Adress UF', nullable=True, interval=' ')


            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_oneline_text(can=c, text=health_unit_city_ibge_code, pos=(47, 720), camp_name='Health Unit City IBGE code', len_max=7, len_min=7, nullable=True, interval='  ')
            c = pdf_functions.add_oneline_text(can=c, text=document_chart_number, pos=(410, 720), camp_name='Document Chart Number', len_max=10, len_min=1, nullable=True, interval='  ')
            c = pdf_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(291, 672), pos_fem=(338, 672), camp_name='Patient Sex', square_size=(11,9), nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_nationality, pos=(278, 587), camp_name='Patient Nationality', len_max=32, len_min=3, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_city_ibge_code, pos=(47, 461), camp_name='Patient City IBGE code', len_max=7, len_min=7, nullable=True, interval='  ')
            if patient_ethnicity == None:
                patient_ethnicity = [None, None]
            if type(patient_ethnicity) != type(list()):
                raise Exception('Etnia do paciente (Patient ethnicity) deve ser uma lista')
            c = pdf_functions.add_markable_square_and_onelinetext(can=c, option=patient_ethnicity[0], valid_options=['BRANCA','PRETA', 'PARDA', 'AMARELA', 'INDIGENA'], text_options=['INDIGENA'], text_pos=(516, 563), options_positions=((278, 560), (323, 560),(363, 560),(401, 560), (450, 560)), camp_name='Patient Ethinicity', len_max=10, text=patient_ethnicity[1], len_min=4, square_size=(11, 9), nullable=True)
            c = pdf_functions.add_markable_square(can=c, option=patient_schooling, valid_options=['ANALFABETO', 'FUNDINCOM', 'FUNDCOMPL', 'MEDIOCOMPL', 'SUPCOMPL'], options_positions=((55, 380), (115, 381), (223, 381), (325, 381), (408, 381)), camp_name='Patient Schooling', square_size=(10,9), nullable=True)
            
        except Exception as error:
            return error
        except:
            return Exception('Erro critico ocorreu enquanto adicionava dados opcionais na pagina 1')


### Add Page 2
        pdf.change_canvas()

        packet_2 = io.BytesIO()
        # Create canvas and add data
        c_2 = canvas.Canvas(packet_2, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        c_2.setFont('Roboto-Mono', 13)
        try:
            pdf.add_oneline_text(text=prof_solicitor_name, pos=(206, 346), camp_name='Professional Solicitor Name', len_max=23, len_min=7, interval=' ')
            c_2 = pdf_functions.add_oneline_text(can=c_2, text=prof_solicitor_name, pos=(206, 346), camp_name='Professional Solicitor Name', len_max=23, len_min=7, interval=' ')

            c_2.setFont('Roboto-Mono', 12)
            c_2 = pdf_functions.add_datetime(can=c_2, date=solicitation_datetime, pos=(48, 346), camp_name='Solicitation Datetime', hours=False, interval=' ', formated=False, interval_between_numbers=' ')
            c_2 = pdf_functions.add_oneline_text(can=c_2, text=exam_number, pos=(114, 324), camp_name='Exam number', len_max=16, len_min=1, nullable=True, interval=' ')
            c_2.setFont('Roboto-Mono', 9)
            c_2 = pdf_functions.add_markable_square(can=c_2, option=tracking_mammogram, valid_options=['POPALVO', 'RISCOELEVADO', 'JATRATADO'], options_positions=((56, 374), (152, 374), (328, 374)), camp_name='Tracking Mammogram', square_size=(11,10), nullable=True)
            c_2 = add_diagnostic_mammogram(can=c_2, diagnostic_mammogram=diagnostic_mammogram)

        except Exception as error:
            return error
        except:
            return Exception('Algum erro nao diagnoticado ocorreu enquanto adicionava dados obrigatorios na pagina 2')

        # # create a new PDF with Reportlab
        # c.save()
        # c_2.save()
        # packet.seek(0)
        # packet_2.seek(0)
        # new_pdf = PdfReader(packet)
        # new_pdf_2 = PdfReader(packet_2)
        # # read the template pdf 
        # template_pdf = PdfReader(open(TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY, "rb"))
        # output = PdfWriter()
        # # add the "watermark" (which is the new pdf) on the existing page
        # page = template_pdf.pages[0]
        # page.merge_page(new_pdf.pages[0])
        # page_2 = template_pdf.pages[1]
        # page_2.merge_page(new_pdf_2.pages[0])
        # output.add_page(page)
        # output.add_page(page_2)

        # pdf_base64_enconded = pdf_functions.get_base64(newpdf=output)

        #Get pdf base64
        pdf_base64_enconded = pdf.get_base64()

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except Exception as error:
        return error
    except:
        return Exception("Erro critico enquanto preenchia o documento de Solicitacao de Mamografia")


def add_patient_adress_cep(can:canvas.Canvas, number:str):
    """add patient addes cep to document

    Args:
        can (canvas.Canvas): canvas to use
        number (str): adress cep

    Returns:
        canvas or Response: canvas updated or Response with error
    """    
    try:
        if number == None:
            return can
        if type(number) != type(str()) and number != None:
            raise Exception('Endereco de CEP do paciente (Patient Adress CEP) deve ser um string')
        number = str(number).strip()
        if len(number) == 8:
            can = pdf_functions.add_oneline_text(can=can, text=number[:5], pos=(47, 438), camp_name='Patient Adress CEP', len_max=5, len_min=5, interval=' ', nullable=True)
            can = pdf_functions.add_oneline_text(can=can, text=number[5:], pos=(138, 438), camp_name='Patient Adress CEP', len_max=3, len_min=3, interval=' ', nullable=True)
            return can
        else:
            raise Exception("Nao foi possivel adicionar o Endereco de CEP do paciente (Patient Adress CEP) porque deve ter somente 8 caracteres")
    except Exception as error:
        raise error
    except:
        raise Exception('Erro desconhecido ocorreu enquanto adicionava Endereco de CEP do paciente (Patient Adress CEP)')


def add_patient_phonenumber(can:canvas.Canvas, number:str):
    """add patient phonenumber to document

    Args:
        can (canvas.Canvas): canvas to use
        number (str): phone number

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        if number == None:
            return can
        if type(number) != type(str()) and number != None:
            raise Exception('Numero de Telefone do paciente deve ser uma string')
        number = str(number).strip()
        if len(number) == 10:
            can = pdf_functions.add_oneline_text(can=can, text=number[:2], pos=(227, 438), camp_name='Patient Phonenumber', len_max=2, len_min=2, interval=' ', nullable=True)
            can = pdf_functions.add_oneline_text(can=can, text=number[2:6], pos=(288, 438), camp_name='Patient Phonenumber', len_max=4, len_min=4, interval=' ', nullable=True)
            can = pdf_functions.add_oneline_text(can=can, text=number[6:], pos=(365, 438), camp_name='Patient Phonenumber', len_max=4, len_min=4, interval=' ', nullable=True)
            return can
        else:
            raise Exception("Nao foi possivel adicionar o Numero de Telefone do paciente porque deve ter somente 10 caracteres")

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido ocorreu enquanto adicionava o numero de telefone do paciente')


def add_radiotherapy_before(can:canvas.Canvas, radiotherapy_before:list):
    """add radiotherapy option to document

    Args:
        can (canvas.Canvas): canvas to use
        radiotherapy_before (list): radiotherapy option

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        if radiotherapy_before == None:
            return can
        if type(radiotherapy_before) != type(list()):
            raise Exception('radiotherapy_before deve ser uma lista (list)')
        can = pdf_functions.add_markable_square_and_onelinetext(can=can, option=radiotherapy_before[0], valid_options=['SIMDIR', 'SIMESQ', 'NAO', 'NAOSABE'], text_options=['SIMDIR'], options_positions=((336,332), (336,319), (336, 307), (336, 294)), camp_name='Has made radiotherapy before', square_size=(15,9), len_max=4, len_min=4, text=radiotherapy_before[1], text_pos=(420, 334), interval=' ', nullable=True)
        if radiotherapy_before[0].upper() == 'SIMESQ':
            can = pdf_functions.add_oneline_text(can=can, text=radiotherapy_before[1], pos=(420, 321), camp_name='Has made radiotherapy before', len_max=4, len_min=4, interval=' ', nullable=True)
        return can

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido ocorreu enquanto adicionava as radioterapias anteriores(radiotherapy before)')


def add_breast_surgery_before(can:canvas.Canvas, breast_surgery_before:dict):
    """add breast_surgery_before to document

    Args:
        can (canvas.Canvas): canvas to use
        breast_surgery_before (dict): breast_surgery_before

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        if breast_surgery_before == None:
            return can
        if type(breast_surgery_before) != type(dict()):
            raise Exception("breast_surgery_before deve ser um dicionarios com listas ou booleanos, exemplo {'surgery':(year_esq, year_dir)} or {'didNot':True}, {'didNot':False,'biopsiaInsinonal':(None, 2020),'biopsiaExcisional':(2021, None),'centraledomia':(None, None),'segmentectomia':(None),'dutectomia':(None, None),'mastectomia':(None, None),'mastectomiaPoupadoraPele':(None, None),'mastectomiaPoupadoraPeleComplexoAreolo':(None, None),'linfadenectomiaAxilar':(None, None),'biopsiaLinfonodo':(None, None),'reconstrucaoMamaria':(None, None),'mastoplastiaRedutora':(None, None),'indusaoImplantes':(None, None)}")
        necessary_keys_positions = {"didNot":(334, 41), "biopsiaInsinonal":((500, 251), (338, 251)), "biopsiaExcisional":((500, 235), (338, 235)), "centraledomia":((500, 220), (338, 220)), "segmentectomia":((500, 204), (338, 204)), "dutectomia":((500, 190), (338, 190)), "mastectomia":((500, 176), (338, 176)), "mastectomiaPoupadoraPele":((500, 159), (338, 159)), "mastectomiaPoupadoraPeleComplexoAreolo":((500, 143), (338, 143)), "linfadenectomiaAxilar":((500, 121), (338, 121)), "biopsiaLinfonodo":((500, 105), (338, 105)), "reconstrucaoMamaria":((500, 90), (338, 90)), "mastoplastiaRedutora":((500, 75), (338, 75)), "indusaoImplantes":((500, 60), (338, 60))}

        if len(breast_surgery_before) > 14:
            raise Exception('Você não pode adicionar mais que 14 chaves no dicionarios em breast_surgery_before')
        #Pick all valid keys
        valid_keys = [ x for x in breast_surgery_before.keys() if x in necessary_keys_positions.keys()]
        #Start adding data
        for surgery in valid_keys:
            #Receive the current surgery
            current_surgery = breast_surgery_before[surgery]
            if type(current_surgery) == type(bool()):
                # when is didNot key
                if current_surgery:
                    can = pdf_functions.add_square(can=can, pos=necessary_keys_positions[surgery], size=(15, 9))
                    return can
                else:
                    continue
            elif current_surgery[0] == None:
                continue
            elif type(current_surgery) != type(list()):
                raise Exception(f'{surgery} deve ser uma lista com os anos da cirurgias no seio direito e esquerdo ou None, exemplo: surgery: None or surgery:(None, 2020)')
            
            if len(current_surgery) != 2:
                raise Exception(f'{surgery} deve ser uma lista com 2 valores , exemplo: (ano_esquerdo, ano_direito)')
            
            cont = 0 
            for year in current_surgery:
                # Add year in right position
                can = pdf_functions.add_oneline_intnumber(can=can, number=year, pos=necessary_keys_positions[surgery][cont], camp_name=f'{surgery} year', len_max=4, len_min=4, value_min=1900, value_max=2100, nullable=True, interval=' ')
                cont = 1
            
            
        return can
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido ocorreu enquanto adicionava cirurgias anterioes nos seios (breast_surgery_before)')


def add_diagnostic_mammogram(can:canvas.Canvas, diagnostic_mammogram:dict):
    """add diagnostic_mammogram to document

    Args:
        can (canvas.Canvas): canvas to use
        diagnostic_mammogram (dict): diagnostic_mammogram

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        if diagnostic_mammogram == None:
            return can
        if type(diagnostic_mammogram) != type(dict()):
            raise Exception("""
Diagnostico de mamografia (diagnostic_mammogram) deve ser um dicionario com dicionarios no modelo da estrutura abaixo, existem mais exemplos na docstring da funcao, exemplo:
'exame_clinico':
        {'direita':[
            'PAPILAR', 
            {'descarga_papilar': ['CRISTALINA', 'HEMORRAGICA']},
            {'nodulo': ['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
            {'espessamento':['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
            {'linfonodo_palpavel':['AXILAR', 'SUPRACLAVICULAR']}
            ],
        'esquerda':[
            'PAPILAR', 
            {'descarga_papilar': ['CRISTALINA', 'HEMORRAGICA']},
            {'nodulo': ['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
            {'espessamento':['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
            {'linfonodo_palpavel':['AXILAR', 'SUPRACLAVICULAR']}
            ]
        }
    """)
        # secoes validas
        sections_keys = ['exame_clinico', 'controle_radiologico', 'lesao_diagnostico', 'avaliacao_resposta', 'revisao_mamografia_lesao', 'controle_lesao']
        
        if len(diagnostic_mammogram) > 6:
            raise Exception(f'O dicionario de diagnostic_mammogram nao pode ter mais que 6 keys, use somente {sections_keys}')
        
        
        

        for section in sections_keys:
            if section in diagnostic_mammogram.keys():
                # Mark sections options in mamografia diagnostica
                can = pdf_functions.add_markable_square(can=can, option=section, valid_options=['EXAME_CLINICO', 'CONTROLE_RADIOLOGICO', 'LESAO_DIAGNOSTICO', 'AVALIACAO_RESPOSTA', 'REVISAO_MAMOGRAFIA_LESAO', 'CONTROLE_LESAO'], options_positions=((56, 762), (55, 590), (226, 590),(402, 589),(55, 487),(312, 489),), camp_name='Diagnostic Mammogram Section', square_size=(11,10))
                current_options = diagnostic_mammogram[section]
                if section == 'exame_clinico':
                    if type(current_options) != type(dict()):
                        raise Exception('exame_clinico deve ser um dicionario, exemplo: "exame_clinico":["direita":["PAPILAR", {"":[]}]]')
                    # See all itens in dict
                    breast_keys = ['direita', 'esquerda']
                    for breast in breast_keys:
                        # Options in direita
                        # ['descarga_papilar', 'nodulo', 'espessamento', 'linfonodo_palpavel']
                        if breast in current_options.keys():
                            if breast == 'direita':
                                can = add_exame_clinico_direita(can=can, current_options=current_options['direita'])

                            if breast == 'esquerda':
                                can = add_exame_clinico_esquerda(can=can, current_options=current_options['esquerda'])
                
                if section == 'controle_radiologico':
                    if type(current_options) != type(dict()):
                        raise Exception('controle_radiologico deve ser um dicionario, exemplo: "controle_radiologico":{"direita": [],      "esquerda": []}')
                    # See all itens in dict
                    breast_keys = ['direita', 'esquerda']
                    for breast in breast_keys:
                        if breast in current_options.keys():
                            if breast == 'direita':
                                can = add_controle_radiologico_direita(can=can, current_options=current_options['direita'])

                            if breast == 'esquerda':
                                can = add_controle_radiologico_esquerda(can=can, current_options=current_options['esquerda'])
                                
                if section == 'lesao_diagnostico':
                    if type(current_options) != type(dict()):
                        raise Exception('lesao_diagnostico deve ser um dicionario, exemplo: "lesao_diagnostico":{"direita": [], "esquerda": []}')
                    # See all itens in dict
                    breast_keys = ['direita', 'esquerda']
                    for breast in breast_keys:
                        if breast in current_options.keys():
                            if breast == 'direita':
                                can = add_lesao_diagnostico_direita(can=can, current_options=current_options['direita'])

                            if breast == 'esquerda':
                                can = add_lesao_diagnostico_esquerda(can=can, current_options=current_options['esquerda'])

                if section == 'avaliacao_resposta':
                    if type(current_options) != type(list()):
                        raise Exception('avaliacao_resposta deve ser um dicionario, exemplo: "avaliacao_resposta":["direita", "esquerda"]')
                    # See all itens in list
                    for breast in current_options:
                        can = pdf_functions.add_markable_square(can=can, option=breast, valid_options=['DIREITA', 'ESQUERDA'], options_positions=((401, 562), (401, 547)), camp_name='avaliacao_resposta breastS', square_size=(11,10), nullable=True)
                        

                if section == 'revisao_mamografia_lesao':
                    if type(current_options) != type(dict()):
                        raise Exception('revisao_mamografia_lesao deve ser um dicionario, exemplo: "revisao_mamografia_lesao":{"direita": [], "esquerda": []}')
                    # See all itens in dict
                    breast_keys = ['direita', 'esquerda']
                    for breast in breast_keys:
                        if breast in current_options.keys():
                            if breast == 'direita':
                                can = add_revisao_mamografia_lesao_direita(can=can, current_options=current_options['direita'])

                            if breast == 'esquerda':
                                can = add_revisao_mamografia_lesao_esquerda(can=can, current_options=current_options['esquerda'])
                                pass

                if section == 'controle_lesao':
                    if type(current_options) != type(dict()):
                        raise Exception('controle_lesao deve ser um dicionario, exemplo: "controle_lesao":{"direita": [], "esquerda": []}')
                    # See all itens in dict
                    breast_keys = ['direita', 'esquerda']
                    for breast in breast_keys:
                        if breast in current_options.keys():
                            if breast == 'direita':
                                can = add_controle_lesao_direita(can=can, current_options=current_options['direita'])

                            if breast == 'esquerda':
                                can = add_controle_lesao_esquerda(can=can, current_options=current_options['esquerda'])
                                pass

            else:
                continue

        return can

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquanto adicionava historico de cirurgias nos seios (breast_surgery_before)')


def add_exame_clinico_direita(can:canvas.Canvas, current_options:dict):
    """add exame_clinico_direita to document

    Args:
        can (canvas.Canvas): canvas to use
        current_options (dict): exame_clinico_direita

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        
        if type(current_options) != type(dict()):
            raise Exception('o valores da direita em exame_clinico deve ser uma lista de dicionarios, exemplo: "exame_clinico":["direita":[{"":[]}]]')
        
        item_keys = current_options.keys()
        if 'papilar' in item_keys:
            if current_options['papilar']:
                can = pdf_functions.add_square(can=can, pos=(56, 732), size=(15, 9))

        if 'descarga_papilar' in item_keys:
            for option in current_options['descarga_papilar']:
                can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['CRISTALINA', 'HEMORRAGICA'], options_positions=((496, 737), (496, 723)), camp_name='descarga_capilar options in direita breast', square_size=(15,9), nullable=True)
        
        if 'nodulo' in item_keys:
            for option in current_options['nodulo']:
                can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'], options_positions=((312, 696), (361, 696), (412, 696), (466, 696), (512, 696), (312, 683), (361, 683), (412, 683), (466, 683), (512, 683)), camp_name='nodulo options in direita breast', square_size=(15,9), nullable=True)

        if 'espessamento' in item_keys:
            for option in current_options['espessamento']:
                can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'], options_positions=((313, 650), (362, 650), (413, 650), (467, 650), (513, 650), (313, 637), (362, 637), (413, 637), (467, 637), (513, 637)), camp_name='espessamento options in direita breast', square_size=(15,9), nullable=True)

        if 'linfonodo_palpavel' in item_keys:
            for option in current_options['linfonodo_palpavel']:
                can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['AXILAR', 'SUPRACLAVICULAR'], options_positions=((380, 615), (420, 615)), camp_name='linfonodo_palpavel options in direita breast', square_size=(15,9), nullable=True)
        return can

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquanto adicionava exame_clinico_direita')



def add_exame_clinico_esquerda(can:canvas.Canvas, current_options:dict):
    """add exame_clinico_esquerda to document

    Args:
        can (canvas.Canvas): canvas to use
        exame_clinico_esquerda (dict): current_options

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:

        if type(current_options) != type(dict()):
            raise Exception('valores da esquerda em exame_clinico deve ser uma lista de dicionarios, exemplo: "exame_clinico":["esquerda":[{"":[]}]]')
        item_keys = current_options.keys()
        if 'papilar' in item_keys:
            if current_options['papilar']:
                can = pdf_functions.add_square(can=can, pos=(314, 732), size=(15, 9))
        if 'descarga_papilar' in item_keys:
            for option in current_options['descarga_papilar']:
                can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['CRISTALINA', 'HEMORRAGICA'], options_positions=((238, 737), (238, 725)), camp_name='descarga_capilar options in esquerda breast', square_size=(15,9), nullable=True)
        
        if 'nodulo' in item_keys:
            for option in current_options['nodulo']:
                can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'], options_positions=((54, 696), (103, 696), (154, 696), (208, 696), (254, 696), (54, 683), (103, 683), (154, 683), (208, 683), (254, 683)), camp_name='nodulo options in esquerda breast', square_size=(15,9), nullable=True)

        if 'espessamento' in item_keys:
            for option in current_options['espessamento']:
                can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'], options_positions=((55, 650), (104, 650), (155, 650), (209, 650), (255, 650), (55, 637), (104, 637), (155, 637), (209, 637), (255, 637)), camp_name='espessamento options in esquerda breast', square_size=(15,9), nullable=True)

        if 'linfonodo_palpavel' in item_keys:
            for option in current_options['linfonodo_palpavel']:
                can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['AXILAR', 'SUPRACLAVICULAR'], options_positions=((121, 615), (162, 616)), camp_name='linfonodo_palpavel options in esquerda breast', square_size=(15,9), nullable=True)
        return can
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquanto adicionava exame_clinico_direita')


def add_controle_radiologico_direita(can:canvas.Canvas, current_options:list):
    """add controle_radiologico_direita to document

    Args:
        can (canvas.Canvas): canvas to use
        current_options (list): current_options

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        for option in current_options:    
            can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((61, 571), (61, 560), (61, 550), (61, 539), (61, 528), (61, 517), (61, 506)), camp_name='controle_radiologico_direita options in right breast', square_size=(10,5), nullable=True)

        return can
    except:
        raise Exception('Erro desconhecido enquanto adicionava controle_radiologico_direita')


def add_controle_radiologico_esquerda(can:canvas.Canvas, current_options:list):
    """add controle_radiologico_esquerda to document

    Args:
        can (canvas.Canvas): canvas to use
        current_options (list): current_options

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        for option in current_options:    
            can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((161, 571), (161, 560), (161, 548), (161, 538), (161, 528), (161, 517), (161, 505)), camp_name='controle_radiologico_esquerda options in right breast', square_size=(10,5), nullable=True)

        return can
    except:
        raise Exception('Erro desconhecido enquanto adicionava controle_radiologico_esquerda')


def add_lesao_diagnostico_direita(can:canvas.Canvas, current_options:list):
    """add lesao_diagnostico_direita to document

    Args:
        can (canvas.Canvas): canvas to use
        current_options (list): current_options

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        for option in current_options:    
            can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((243, 571), (243, 560), (243, 549), (243, 539), (243, 528), (243, 517), (243, 506)), camp_name='lesao_diagnostico_direita options in right breast', square_size=(10,5), nullable=True)

        return can
    except:
        raise Exception('Erro desconhecido enquanto adicionava lesao_diagnostico_direita')


def add_lesao_diagnostico_esquerda(can:canvas.Canvas, current_options:list):
    """add lesao_diagnostico_esquerda to document

    Args:
        can (canvas.Canvas): canvas to use
        current_options (list): current_options

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        for option in current_options:    
            can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((341, 571), (341, 560), (341, 550), (341, 539), (341, 528), (341, 517), (341, 506)), camp_name='lesao_diagnostico_esquerda options in right breast', square_size=(10,5), nullable=True)

        return can
    except:
        raise Exception('Erro desconhecido enquanto adicionava lesao_diagnostico_esquerda')


def add_revisao_mamografia_lesao_direita(can:canvas.Canvas, current_options:list):
    """add revisao_mamografia_lesao_direita to document

    Args:
        can (canvas.Canvas): canvas to use
        current_options (list): current_options

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        for option in current_options:    
            can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['0', '3', '4', '5'], options_positions=((64, 469), (64, 458), (64, 448), (64, 437)), camp_name='mamografia_lesao_direita options in right breast', square_size=(10,5), nullable=True)

        return can
    except:
        raise Exception('Erro desconhecido enquanto adicionava mamografia_lesao_direita')


def add_revisao_mamografia_lesao_esquerda(can:canvas.Canvas, current_options:list):
    """add revisao_mamografia_lesao_esquerda to document

    Args:
        can (canvas.Canvas): canvas to use
        current_options (list): current_options

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        for option in current_options:    
            can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['0', '3', '4', '5'], options_positions=((164, 469), (164, 458), (164, 446), (164, 436)), camp_name='mamografia_lesao_esquerda options in right breast', square_size=(10,5), nullable=True)
        return can
    except:
        raise Exception('Erro desconhecido enquanto adicionava mamografia_lesao_esquerda')


def add_controle_lesao_direita(can:canvas.Canvas, current_options:list):
    """add controle_lesao_direita to document

    Args:
        can (canvas.Canvas): canvas to use
        current_options (list): current_options

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        for option in current_options:    
            can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((329, 469), (329, 459), (329, 447), (329, 437), (329, 426), (329, 415), (329, 404)), camp_name='controle_lesao_direita options in right breast', square_size=(10,5), nullable=True)

        return can
    except:
        raise Exception('Erro desconhecido enquanto adicionava controle_lesao_direita')


def add_controle_lesao_esquerda(can:canvas.Canvas, current_options:list):
    """add controle_lesao_esquerda to document

    Args:
        can (canvas.Canvas): canvas to use
        current_options (list): current_options

    Returns:
        canvas or Response: canvas updated or Response with error
    """
    try:
        for option in current_options:    
            can = pdf_functions.add_markable_square(can=can, option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((427, 469), (427, 458), (427, 448), (427, 437), (427, 426), (427, 415), (427, 404)), camp_name='controle_lesao_esquerda options in right breast', square_size=(10,5), nullable=True)

        return can
    except:
        raise Exception('Erro desconhecido enquanto adicionava controle_lesao_esquerda')






