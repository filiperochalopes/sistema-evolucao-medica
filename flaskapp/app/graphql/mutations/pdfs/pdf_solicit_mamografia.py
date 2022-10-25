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


def fill_pdf_solicit_mamografia(patient_name:str, patient_cns:int, patient_mother_name:str, patient_birthday:datetime.datetime, nodule_lump:str, high_risk:str, examinated_before:str, mammogram_before:list, patient_age:int, health_unit_adressUF:str=None, health_unit_cnes:int=None, health_unit_name:str=None, health_unit_adress_city:str=None, health_unit_city_IBGEcode:int=None, document_chart_number:int=None, protocol_number:str=None, patient_sex:str=None, patient_surname:str=None, patient_document_cpf:dict=None, patient_nationality:str=None, patient_adress:str=None, patient_adress_number:int=None, patient_adress_adjunct:str=None, patient_adress_neighborhood:str=None, patient_city_IBGEcode:int=None, patient_adress_city:str=None, patient_adressUF:str=None, patient_ethnicity:list=None, patient_adress_reference:str=None, patient_schooling:str=None) -> Union[PdfWriter, Response]:
    try:
        packet = io.BytesIO()
        # Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        #####packet_2 = io.BytesIO()
        # Create canvas and add data
        #####c_2 = canvas.Canvas(packet_2, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        c.setFont('Roboto-Mono', 13)
        # Writing all data in respective fields
        # not null data
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
            #c = pdf_functions.add_morelines_text(can=c, text=patient_name, initial_pos=(48, 653), decrease_ypos=18, camp_name='Patient Name', len_max=42, len_min=7, interval='  ', char_per_lines=87)
            if type(c) == type(Response()): return c
            #c = pdf_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(48, 612), camp_name='Patient Mother Name', len_max=42, len_min=7, interval='  ')
            if type(c) == type(Response()): return c
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
                return Response('Some error happen when adding not null data to fields', status=500)

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




            c.setFont('Roboto-Mono', 12)
            #c = pdf_functions.add_UF(can=c, uf=health_unit_adressUF, pos=(50, 762), camp_name='Health Unit Adress UF', nullable=True, interval=' ')
            if type(c) == type(Response()): return c
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
            #c = pdf_functions.add_oneline_text(can=c, text=health_unit_name, pos=(48, 743), camp_name='Health Unit Name', len_max=42, len_min=7, interval='  ', nullable=True)
            if type(c) == type(Response()): return c
            #c = pdf_functions.add_oneline_text(can=c, text=health_unit_adress_city, pos=(170, 720), camp_name='Health Unit Adress City', len_max=14, len_min=4, interval='  ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=health_unit_city_IBGEcode, pos=(47, 720), camp_name='Health Unit City IBGE code', len_max=7, len_min=7, value_min=0, value_max=9999999, nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=document_chart_number, pos=(410, 720), camp_name='Document Chart Number', len_max=10, len_min=1, value_min=0, value_max=99999999999999, nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(291, 672), pos_fem=(338, 672), camp_name='Patient Sex', square_size=(11,9), nullable=True)
            if type(c) == type(Response()): return c
            #c = pdf_functions.add_oneline_text(can=c, text=patient_surname, pos=(290, 635), camp_name='Patient Surname', len_max=18, len_min=4, interval='  ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_nationality, pos=(278, 587), camp_name='Patient Nationality', len_max=32, len_min=3, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress, pos=(48, 529), camp_name='Patient Adress', len_max=42, len_min=7, interval='  ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_adjunct, pos=(172, 507), camp_name='Patient Adress Adjunct', len_max=25, len_min=7, interval='  ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_neighborhood, pos=(294, 484), camp_name='Patient Adress Neighborhood', len_max=14, len_min=7, interval='  ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_city_IBGEcode, pos=(47, 461), camp_name='Patient City IBGE code', len_max=7, len_min=7, value_min=0, value_max=9999999, nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_city, pos=(170, 461), camp_name='Patient Adress City', len_max=14, len_min=4, interval='  ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square_and_onelinetext(can=c, option=patient_ethnicity[0], valid_options=['BRANCA','PRETA', 'PARDA', 'AMARELA', 'INDIGENA'], text_options=['INDIGENA'], text_pos=(516, 563), options_positions=((278, 560), (323, 560),(363, 560),(401, 560), (450, 560)), camp_name='Patient Ethinicity', len_max=10, text=patient_ethnicity[1], len_min=4, square_size=(11, 9), nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_reference, pos=(47, 413), camp_name='Patient Adress Reference', len_max=33, len_min=4, interval='  ', nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square(can=c, option=patient_schooling, valid_options=['ANALFABETO', 'FUNDINCOM', 'FUNDCOMPL', 'MEDIOCOMPL', 'SUPCOMPL'], options_positions=((55, 380), (115, 381), (223, 381), (325, 381), (408, 381)), camp_name='Patient Schooling', square_size=(10,9))
            if type(c) == type(Response()): return c
            
        except:
            return Response('Critical error happen when adding data that can be null to fields', status=500)



        # create a new PDF with Reportlab
        c.save()
        ######c_2.save()
        packet.seek(0)
        ######packet_2.seek(0)
        new_pdf = PdfReader(packet)
        #####new_pdf_2 = PdfReader(packet_2)
        # read the template pdf 
        template_pdf = PdfReader(open(TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        ######page_2 = template_pdf.pages[1]
        ######page_2.merge_page(new_pdf_2.pages[0])
        output.add_page(page)
        ######output.add_page(page_2)

        pdf_functions.write_newpdf(output, WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY)
        
        with open(WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY, "rb") as pdf_file:
            pdf_base64_enconded = base64.b64encode(pdf_file.read())

        return pdf_base64_enconded
    except:
        return Response("Error while filling aih sus", status=500)