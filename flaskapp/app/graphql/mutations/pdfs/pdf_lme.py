import datetime
from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from flask import Response
from typing import Union


# Doing the import this way only when is called by antoher file (like pytest)
if __name__ != "__main__":
    from pdfs import global_functions

template_directory = "/app/app/assets/pdfs_templates/lme.pdf"
font_directory = "/app/app/assets/pdfs_templates/Roboto-Mono.ttf"

def fill_pdf_lme(establishment_solitc_name:str, establishment_solitc_cnes:int) -> Union[PdfWriter, Response]:
    try:
        packet = io.BytesIO()
        # Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', font_directory))
        c.setFont('Roboto-Mono', 10)
        # Writing all data in respective fields
        # not null data

        try:
            c = global_functions.add_oneline_intnumber(can=c, number=establishment_solitc_cnes, pos=(38, 658), camp_name='Establishment Solict CNES', len_max=7, len_min=7,value_min=0, value_max=99999999, interval='   ')
            if type(c) == type(Response()): return c


            c.setFont('Roboto-Mono', 9)
            c = global_functions.add_oneline_text(can=c, text=establishment_solitc_name, pos=(206, 658), camp_name='Establishment Solicit Name', len_max=65, len_min=8)
            if type(c) == type(Response()): return c


        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)
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
        return Response("Error while filling aih sus", status=500)



if __name__ == "__main__":
    lenght_test = ''
    for x in range(0, 2000):
        lenght_test += str(x)
    import global_functions
    output = fill_pdf_lme(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567
    )

    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/tests/pdfs_created_files_test/lme_teste.pdf")












