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



template_directory = "/app/app/assets/pdfs_templates/relatorio_de_alta.pdf"
font_directory = "/app/app/assets/pdfs_templates/Roboto-Mono.ttf"

def fill_pdf_relatorio_alta(documentDatetime:datetime.datetime, patient_name:str, patient_cns:int, patient_birthday:datetime.datetime, patient_sex:str, patient_motherName:str, patient_document:dict, patient_adress:str, evolution:str, doctor_name:str, doctor_cns:int, doctor_crm:str, orientations:str=None) -> Union[PdfWriter, Response]:
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
            c = global_functions.add_datetime(can=c, date=documentDatetime, pos=(410, 740), camp_name='Document Datetime', hours=True, formated=True)
            if type(c) == type(Response()): return c          
            
            
            # change font size to normal            
            c.setFont('Roboto-Mono', 9)            
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
            c = global_functions.add_oneline_text(can=c, text=doctor_name, pos=(304, 195), camp_name='Doctor Name', len_max=49, len_min=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_cns(can=c, cns=doctor_cns, pos=(304, 163), camp_name='Doctor CNS', formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=doctor_crm, pos=(304, 131), camp_name='Doctor CRM', len_max=13, len_min=11)
            if type(c) == type(Response()): return c
            c = global_functions.add_morelines_text(can=c, text=evolution, initial_pos=(26, 540), decrease_ypos=10, camp_name='Evolution Resume', len_max=2100, len_min=10, char_per_lines=100)

            if type(c) == type(Response()): return c
        
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)
            
        #Adding data that can be null
        try:
            c = global_functions.add_morelines_text(can=c, text=orientations, initial_pos=(26, 312), decrease_ypos=10, camp_name='Orientations', len_max=800, len_min=10, char_per_lines=100, nullable=True)
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
        return Response("Error while filling relatorio de alta", status=500)
