import base64
import datetime
from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from flask import Response
from typing import Union
from pdfs import pdf_functions
from pdfs.constants import FONT_DIRECTORY, TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY, WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY


def fill_pdf_solicit_mamografia(patient_name:str, patient_cns:int, patient_mother_name:str, patient_birthday:datetime.datetime, nodule_lump:str, high_risk:str, examinated_before:str, mammogram_before:list, patient_age:int, solicitation_datetime:datetime.datetime, prof_solicitor_name:str, health_unit_adressUF:str=None, health_unit_cnes:int=None, health_unit_name:str=None, health_unit_adress_city:str=None, health_unit_city_IBGEcode:int=None, document_chart_number:int=None, protocol_number:str=None, patient_sex:str=None, patient_surname:str=None, patient_document_cpf:dict=None, patient_nationality:str=None, patient_adress:str=None, patient_adress_number:int=None, patient_adress_adjunct:str=None, patient_adress_neighborhood:str=None, patient_city_IBGEcode:int=None, patient_adress_city:str=None, patient_adressUF:str=None, patient_ethnicity:list=None, patient_adress_reference:str=None, patient_schooling:str=None, patient_adressCEP:str=None, patient_phonenumber:int=None, radiotherapy_before:list=None, breast_surgery_before:dict=None, exam_number:int=None, tracking_mammogram:str=None) -> Union[PdfWriter, Response]:
    try:
        packet = io.BytesIO()
        # Create canvas and add data
        #####c = canvas.Canvas(packet, pagesize=letter)
        packet_2 = io.BytesIO()
        # Create canvas and add data
        c_2 = canvas.Canvas(packet_2, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        #####c.setFont('Roboto-Mono', 13)
        c_2.setFont('Roboto-Mono', 13)
        # Writing all data in respective fields
        # not null data

        old = """
        try:
            c = pdf_functions.add_cns(can=c, cns=patient_cns, pos=(46, 676), camp_name='Patient CNS', interval=' ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_datetime(can=c, date=patient_birthday, pos=(48, 563), camp_name='Patient Birthday', hours=False, interval=' ', formated=False, interval_between_numbers=' ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square_and_onelinetext(can=c, option=mammogram_before[0], valid_options=['SIM', 'NAO', 'NAOSABE'], text_options=['SIM'], options_positions=((51,64), (51,52), (51, 40)), camp_name='Has made mamogram before', square_size=(15,9), len_max=4, len_min=4, text=mammogram_before[1], text_pos=(200, 68), interval=' ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_age, pos=(217, 563), camp_name='Patient Birthday', len_max=2, len_min=1,value_min=1, value_max=99, interval=' ')


            c.setFont('Roboto-Mono', 13)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_morelines_text(can=c, text=patient_name, initial_pos=(47, 653), decrease_ypos=18, camp_name='Patient Name', len_max=42, len_min=7, interval=' ', char_per_lines=87)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(47, 612), camp_name='Patient Mother Name', len_max=42, len_min=7, interval=' ')
            if type(c) == type(Response()): return c
            
            
            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_markable_square(can=c, option=nodule_lump, valid_options=['SIMDIR', 'SIMESQ', 'NAO'], options_positions=((50,332), (50,320), (50, 310)), camp_name='Has nodule lump', square_size=(15,9))
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square(can=c, option=high_risk, valid_options=['SIM', 'NAO', 'NAOSABE'], options_positions=((51,278), (51,266), (51, 255)), camp_name='Has high risk', square_size=(15,9))
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square(can=c, option=examinated_before, valid_options=['SIM', 'NUNCA', 'NAOSABE'], options_positions=((51,120), (51,107), (51, 94)), camp_name='Has been examinated before', square_size=(15,9))
            if type(c) == type(Response()): return c
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields in page 1', status=500)

        #Adding data that can be null
        try:
            c.setFont('Roboto-Mono', 13)
            c = pdf_functions.add_UF(can=c, uf=health_unit_adressUF, pos=(47, 762), camp_name='Health Unit Adress UF', nullable=True, interval=' ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=health_unit_name, pos=(47, 741), camp_name='Health Unit Name', len_max=42, len_min=7, interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=health_unit_adress_city, pos=(168, 720), camp_name='Health Unit Adress City', len_max=14, len_min=4, interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_surname, pos=(288, 635), camp_name='Patient Surname', len_max=18, len_min=4, interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress, pos=(47, 529), camp_name='Patient Adress', len_max=42, len_min=7, interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_adjunct, pos=(168, 507), camp_name='Patient Adress Adjunct', len_max=25, len_min=7, interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_neighborhood, pos=(292, 484), camp_name='Patient Adress Neighborhood', len_max=14, len_min=7, interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_reference, pos=(47, 413), camp_name='Patient Adress Reference', len_max=33, len_min=4, interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_city, pos=(167, 461), camp_name='Patient Adress City', len_max=15, len_min=4, interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c = add_patient_adress_cep(can=c, number=patient_adressCEP)            
            if type(c) == type(Response()): return c
            c = add_patient_phonenumber(can=c, number=patient_phonenumber)            
            if type(c) == type(Response()): return c
            c = add_radiotherapy_before(can=c, radiotherapy_before=radiotherapy_before)
            if type(c) == type(Response()): return c
            c = add_breast_surgery_before(can=c, breast_surgery_before=breast_surgery_before)
            if type(c) == type(Response()): return c



            c.setFont('Roboto-Mono', 12)
            c = pdf_functions.add_oneline_intnumber(can=c, number=health_unit_cnes, pos=(178, 761), camp_name='Health Unit CNES', len_max=7, len_min=7,value_min=0, value_max=99999999, interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=protocol_number, pos=(406, 768), camp_name='Protocol Number', len_max=23, len_min=1, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=patient_document_cpf, pos_cpf=(52, 589),camp_name='Patient Document CPF', interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_adress_number, pos=(52, 506), camp_name='Patient Adress Number', len_max=6, len_min=1, value_min=0, value_max=999999, interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_UF(can=c, uf=patient_adressUF, pos=(535, 484), camp_name='Patient Adress UF', nullable=True, interval=' ')
            if type(c) == type(Response()): return c


            c.setFont('Roboto-Mono', 9)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=health_unit_city_IBGEcode, pos=(47, 720), camp_name='Health Unit City IBGE code', len_max=7, len_min=7, value_min=0, value_max=9999999, nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=document_chart_number, pos=(410, 720), camp_name='Document Chart Number', len_max=10, len_min=1, value_min=0, value_max=99999999999999, nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(291, 672), pos_fem=(338, 672), camp_name='Patient Sex', square_size=(11,9), nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_nationality, pos=(278, 587), camp_name='Patient Nationality', len_max=32, len_min=3, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_city_IBGEcode, pos=(47, 461), camp_name='Patient City IBGE code', len_max=7, len_min=7, value_min=0, value_max=9999999, nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square_and_onelinetext(can=c, option=patient_ethnicity[0], valid_options=['BRANCA','PRETA', 'PARDA', 'AMARELA', 'INDIGENA'], text_options=['INDIGENA'], text_pos=(516, 563), options_positions=((278, 560), (323, 560),(363, 560),(401, 560), (450, 560)), camp_name='Patient Ethinicity', len_max=10, text=patient_ethnicity[1], len_min=4, square_size=(11, 9), nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square(can=c, option=patient_schooling, valid_options=['ANALFABETO', 'FUNDINCOM', 'FUNDCOMPL', 'MEDIOCOMPL', 'SUPCOMPL'], options_positions=((55, 380), (115, 381), (223, 381), (325, 381), (408, 381)), camp_name='Patient Schooling', square_size=(10,9))
            if type(c) == type(Response()): return c
            
        except:
            return Response('Critical error happen when adding data that can be null to fields in page 1', status=500)

"""
### Add Page 2
        packet_2 = io.BytesIO()
        # Create canvas and add data
        c_2 = canvas.Canvas(packet_2, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        c_2.setFont('Roboto-Mono', 13)
        try:
            c_2 = pdf_functions.add_oneline_text(can=c_2, text=prof_solicitor_name, pos=(206, 346), camp_name='Professional Solicitor Name', len_max=23, len_min=7, interval=' ')
            if type(c_2) == type(Response()): return c_2





            c_2.setFont('Roboto-Mono', 12)
            c_2 = pdf_functions.add_datetime(can=c_2, date=solicitation_datetime, pos=(48, 346), camp_name='Solicitation Datetime', hours=False, interval=' ', formated=False, interval_between_numbers=' ')
            if type(c_2) == type(Response()): return c_2
            c_2 = pdf_functions.add_oneline_intnumber(can=c_2, number=exam_number, pos=(114, 324), camp_name='Exam number', len_max=16, len_min=1, value_min=0, value_max=9999999999999999, nullable=True, interval=' ')
            if type(c_2) == type(Response()): return c_2
            
            c_2.setFont('Roboto-Mono', 9)
            c_2 = pdf_functions.add_markable_square(can=c_2, option=tracking_mammogram, valid_options=['POPALVO', 'RISCOELEVADO', 'JATRATADO'], options_positions=((56, 374), (152, 374), (328, 374)), camp_name='Tracking Mammogram', square_size=(11,10))
            if type(c_2) == type(Response()): return c_2
            c_2 = add_diagnostic_mammogram(can=c_2, diagnostic_mammogram=diagnostic_mammogram)
            if type(c_2) == type(Response()): return c_2

        except:
            if type(c_2) == type(Response()):
                return 
            else:
                return Response('Some error happen when adding not null data to fields in page 2', status=500)

        # create a new PDF with Reportlab
        ######c.save()
        c_2.save()
        ######packet.seek(0)
        packet_2.seek(0)
        ######new_pdf = PdfReader(packet)
        new_pdf_2 = PdfReader(packet_2)
        # read the template pdf 
        template_pdf = PdfReader(open(TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        ######page = template_pdf.pages[0]
        ######page.merge_page(new_pdf.pages[0])
        page_2 = template_pdf.pages[1]
        page_2.merge_page(new_pdf_2.pages[0])
        ######output.add_page(page)
        output.add_page(page_2)

        pdf_functions.write_newpdf(output, WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY)
        
        with open(WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY, "rb") as pdf_file:
            pdf_base64_enconded = base64.b64encode(pdf_file.read())

        return pdf_base64_enconded
    except:
        return Response("Error while filling aih sus", status=500)


def add_patient_adress_cep(can:canvas.Canvas, number:int):
    try:
        if type(number) != type(int()) and number != None:
            return Response('Patient Adress CEP has to be int, if can be null, please add nullable option and None', status=400)
        number = str(number)
        if len(number) == 8:
            can = pdf_functions.add_oneline_text(can=can, text=number[:5], pos=(47, 438), camp_name='Patient Adress CEP', len_max=5, len_min=5, interval=' ', nullable=True)
            if type(can) == type(Response()): return can
            can = pdf_functions.add_oneline_text(can=can, text=number[5:], pos=(138, 438), camp_name='Patient Adress CEP', len_max=3, len_min=3, interval=' ', nullable=True)
            return can
        else:
            return Response("Unable to add Patient Adress CEP because is longer than 8 characters or smaller than 8", status=400)
    except:
        return Response(f'Unknow error while adding Patient Adress CEP', status=500)


def add_patient_phonenumber(can:canvas.Canvas, number:int):
    try:
        if type(number) != type(int()) and number != None:
            return Response('Patient Phonenumber has to be int, if can be null, please add nullable option and None', status=400)
        number = str(number)
        if len(number) == 10:
            can = pdf_functions.add_oneline_text(can=can, text=number[:2], pos=(227, 438), camp_name='Patient Phonenumber', len_max=2, len_min=2, interval=' ', nullable=True)
            if type(can) == type(Response()): return can
            can = pdf_functions.add_oneline_text(can=can, text=number[2:6], pos=(288, 438), camp_name='Patient Phonenumber', len_max=4, len_min=4, interval=' ', nullable=True)
            if type(can) == type(Response()): return can
            can = pdf_functions.add_oneline_text(can=can, text=number[6:], pos=(365, 438), camp_name='Patient Phonenumber', len_max=4, len_min=4, interval=' ', nullable=True)
            return can
        else:
            return Response("Unable to add Patient Phonenumber because is longer than 10 characters or smaller than 10", status=400)
    except:
        return Response(f'Unknow error while adding Patient Phonenumber', status=500)


def add_radiotherapy_before(can:canvas.Canvas, radiotherapy_before:list):
    try:
        can = pdf_functions.add_markable_square_and_onelinetext(can=can, option=radiotherapy_before[0], valid_options=['SIMDIR', 'SIMESQ', 'NAO', 'NAOSABE'], text_options=['SIMDIR'], options_positions=((336,332), (336,319), (336, 307), (336, 294)), camp_name='Has made radiotherapy before', square_size=(15,9), len_max=4, len_min=4, text=radiotherapy_before[1], text_pos=(420, 334), interval=' ', nullable=True)
        if type(can) == type(Response()): return can
        if radiotherapy_before[0].upper() == 'SIMESQ':
            can = pdf_functions.add_oneline_text(can=can, text=radiotherapy_before[1], pos=(420, 321), camp_name='Has made radiotherapy before', len_max=4, len_min=4, interval=' ', nullable=True)
        return can
    except:
        return Response(f'Unknow error while adding radiotherapy before', status=500)


def add_breast_surgery_before(can:canvas.Canvas, breast_surgery_before:dict):
    try:
        if breast_surgery_before == None:
            return can
        if type(breast_surgery_before) != type(dict()):
            return Response("breast_surgery_before has to be a dict with tuples or bool, like {'surgery':(year_esq, year_dir)} or {'did_not':True}, {'did_not':False,'biopsia_insinonal':(None, 2020),'biopsia_excisional':(2021, None),'centraledomia':(None, None),'segmentectomia':(None),'dutectomia':(None, None),'mastectomia':(None, None),'mastectomia_poupadora_pele':(None, None),'mastectomia_poupadora_pele_complexo_areolo':(None, None),'linfadenectomia_axilar':(None, None),'biopsia_linfonodo':(None, None),'reconstrucao_mamaria':(None, None),'mastoplastia_redutora':(None, None),'indusao_implantes':(None, None)}", status=400)
        necessary_keys_positions = {"did_not":(334, 41), "biopsia_insinonal":((500, 251), (338, 251)), "biopsia_excisional":((500, 235), (338, 235)), "centraledomia":((500, 220), (338, 220)), "segmentectomia":((500, 204), (338, 204)), "dutectomia":((500, 190), (338, 190)), "mastectomia":((500, 176), (338, 176)), "mastectomia_poupadora_pele":((500, 159), (338, 159)), "mastectomia_poupadora_pele_complexo_areolo":((500, 143), (338, 143)), "linfadenectomia_axilar":((500, 121), (338, 121)), "biopsia_linfonodo":((500, 105), (338, 105)), "reconstrucao_mamaria":((500, 90), (338, 90)), "mastoplastia_redutora":((500, 75), (338, 75)), "indusao_implantes":((500, 60), (338, 60))}

        if len(breast_surgery_before) > 14:
            return Response('You cannot add more than 14 keys in dict', status=400)
        #Pick all valid keys
        valid_keys = [ x for x in breast_surgery_before.keys() if x in necessary_keys_positions.keys()]
        #Start adding data
        for surgery in valid_keys:
            #Receive the current surgery
            current_surgery = breast_surgery_before[surgery]
            if type(current_surgery) == type(bool()):
                # when is did_not key
                if current_surgery:
                    can = pdf_functions.add_square(can=can, pos=necessary_keys_positions[surgery], size=(15, 9))
                    return can
                else:
                    continue
            elif current_surgery == None:
                continue
            elif type(current_surgery) != type(tuple()):
                return Response(f'{surgery} has to be a tuple with the years right and left or just a None, like: surgery: None or surgery:(None, 2020)', status=400)
            
            if len(current_surgery) != 2:
                return Response(f'{surgery} has to be a tuple with 2 values, like (leftyear, rightyear)')
            
            cont = 0 
            for year in current_surgery:
                # Add year in right position
                can = pdf_functions.add_oneline_intnumber(can=can, number=year, pos=necessary_keys_positions[surgery][cont], camp_name=f'{surgery} year', len_max=4, len_min=4, value_min=1900, value_max=2100, nullable=True, interval=' ')
                if type(can) == type(Response()): return can
                cont = 1
            
            



        return can
    except:
        return Response(f'Unknow error while adding breast_surgery_before', status=500)


def add_diagnostic_mammogram(can:canvas.Canvas, diagnostic_mammogram:dict):
    try:
        if diagnostic_mammogram == None:
            return can
        if type(diagnostic_mammogram) != type(dict()):
            return Response("""
diagnostic_mammogram has to be a dict with dicts in this extructure, see more in docstring in the function,  like: 'exameclinico':[
    {'direita':[
        'PAPILAR', 
        {'descarga_papilar': ['CRISTALINA', 'HEMORRAGICA']},
        {'nodulo': ['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
        {'espessamento':['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
        {'linfonodo_palpavel':['AXILAR', 'SUPRACLAVICULAR']}
        ]
        }]""", status=400)





        return can
    except:
        return Response(f'Unknow error while adding breast_surgery_before', status=500)


dict_test = {
    'exameclinico':[
        {'direita':[
            'PAPILAR', 
            {'descarga_papilar': ['CRISTALINA', 'HEMORRAGICA']},
            {'nodulo': ['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
            {'espessamento':['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
            {'linfonodo_palpavel':['AXILAR', 'SUPRACLAVICULAR']}
            ]
        },
        {'esquerda':[
            'PAPILAR', 
            {'descarga_papilar': ['CRISTALINA', 'HEMORRAGICA']},
            {'nodulo': ['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
            {'espessamento':['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
            {'linfonodo_palpavel':['AXILAR', 'SUPRACLAVICULAR']}
            ]
        }
    ]
}