import datetime
from PyPDF2  import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from flask import Response
from typing import Union
from pdfs import global_functions


template_directory = "/app/app/assets/pdfs_templates/ficha_de_internamento_hmlem.pdf"
font_directory = "/app/app/assets/pdfs_templates/Roboto-Mono.ttf"

def fill_pdf_ficha_internamento(document_datetime:datetime.datetime, patient_name:str, patient_cns:int, patient_birthday:datetime.datetime, patient_sex:str, patient_motherName:str, patient_document:dict, patient_adress:str, patient_phonenumber:int, patient_drug_allergies:str, patient_comorbidities:str, current_illness_history:str, initial_diagnostic_suspicion:str, doctor_name:str, doctor_cns:int, doctor_crm:str, patient_adressNumber:int=None, patient_adressNeigh:str=None, patient_adressCity:str=None, patient_adressUF:str=None, patient_adressCEP:int=None, patient_nationality:str=None, patient_estimateWeight:int=None, has_additional_healthInsurance:bool=None) -> Union[PdfWriter, Response]:

    try:
        packet = io.BytesIO()
        # Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', font_directory))
        c.setFont('Roboto-Mono', 12)

        # Writing all data in respective fields
        # not null data
        try:
            # change font size to datetime            
            c = global_functions.add_datetime(can=c, date=document_datetime, pos=(410, 740), camp_name='Document Datetime', hours=True, formated=True)
            if type(c) == type(Response()): return c      
            
            
            c.setFont('Roboto-Mono', 9)
            #Normal font size
            c = global_functions.add_oneline_text(can=c, text=patient_name, pos=(27, 674), camp_name='Patient Name', len_max=64, len_min=7)
            # verify if c is a error at some point
            if type(c) == type(Response()): return c
            c = global_functions.add_cns(can=c, cns=patient_cns, pos=(393, 674), camp_name='Patient CNS', formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_datetime(can=c, date=patient_birthday, pos=(27, 642), camp_name='Patient Birthday', hours=False, formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(117, 640), pos_fem=(147, 640), camp_name='Patient Sex', square_size=(9,9))
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_motherName, pos=(194, 642), camp_name='Patient Mother Name', len_max=69, len_min=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_document_cns_cpf_rg(can=c, document=patient_document, pos_square_cpf=(24, 608), pos_square_rg=(58,608), pos_rg=(92, 610), pos_cpf=(92, 610),camp_name='Pacient Document', formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adress, pos=(230, 610), camp_name='Patient Adress', len_max=63, len_min=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_phonenumber(can=c, number=patient_phonenumber, pos=(173, 547), camp_name='Patient phone number', formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_drug_allergies, pos=(26, 481), camp_name='Patient Drugs Allergies', len_max=100, len_min=5)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_comorbidities, pos=(26, 449), camp_name='Patient Commorbidites', len_max=100, len_min=5)
            if type(c) == type(Response()): return c
            c = global_functions.add_morelines_text(can=c, text=current_illness_history, initial_pos=(26, 418), decrease_ypos= 10, camp_name='Current Illness History', len_max=1600, char_per_lines=100, len_min=10)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=initial_diagnostic_suspicion, pos=(26, 244), camp_name='Initial Diagnostic Suspicion', len_max=100, len_min=5)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=doctor_name, pos=(304, 195), camp_name='Doctor Name', len_max=49, len_min=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_cns(can=c, cns=doctor_cns, pos=(304, 163), camp_name='Doctor CNS', formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=doctor_crm, pos=(304, 131), camp_name='Doctor CRM', len_max=13, len_min=11)
            if type(c) == type(Response()): return c
            
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            c = global_functions.add_oneline_intnumber(can=c, number=patient_adressNumber, pos=(24, 580), camp_name='Patient Adress Number', len_max=6, len_min=1, value_min=0, value_max=999999, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adressNeigh, pos=(66, 580), camp_name='Patient Adress Neighborhood', len_max=31, len_min=4, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adressCity, pos=(243, 580), camp_name='Patient Adress City', len_max=34, len_min=4, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_UF(can=c, uf=patient_adressUF, pos=(444, 580), camp_name='Patient Adress UF', nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_CEP(can=c, cep=patient_adressCEP, pos=(483, 580), camp_name='Patient Adress CEP', nullable=True, formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_nationality, pos=(27, 547), camp_name='Patient nationality', len_max=25, len_min=3, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_estimateWeight, pos=(507, 547), camp_name='Patient Estimate Weight', len_max=6, len_min=1, value_min=1, value_max=500, nullable=True)
            if type(c) == type(Response()): return c
            if has_additional_healthInsurance != None:
                c = global_functions.add_markable_square(can=c, option=str(has_additional_healthInsurance), valid_options=['TRUE','FALSE'], options_positions=((419, 544), (380, 544)), camp_name='Has additional Healt insurance', nullable=False)
            if type(c) == type(Response()): return c

        except:
            return Response('Critical error happen when adding data that can be null to fields', status=500)

        # create a new PDF with Reportlab
        c.save()
        packet.seek(0)
        new_pdf = PdfReader(packet)
        # read the template pdf 
        template_pdf = PdfReader(open(template_directory, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        return output
    except:
        return Response("Error while filling ficha de internamento", status=500)
