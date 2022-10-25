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


def fill_pdf_solicit_mamografia(patient_name:str, patient_cns:int) -> Union[PdfWriter, Response]:
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
            
            
            c.setFont('Roboto-Mono', 10)
            c = pdf_functions.add_morelines_text(can=c, text=patient_name, initial_pos=(48, 653), decrease_ypos=18, camp_name='Patient Name', len_max=42, len_min=7, interval='  ', char_per_lines=87)
            if type(c) == type(Response()): return c
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)
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