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

def fill_pdf_lme(establishment_solitc_name:str, establishment_solitc_cnes:int, patient_name:str, patient_mother_name:str, patient_weight:int, patient_height:int, cid10:str, anamnese:str, prof_solicitor_name:str, solicitation_datetime:datetime.datetime, prof_solicitor_document:dict, diagnostic:str=None, patient_document:dict=None) -> Union[PdfWriter, Response]:
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
            c = global_functions.add_oneline_intnumber(can=c, number=patient_weight, pos=(485, 628), camp_name='Patient Weight', len_max=3, len_min=1,value_min=1, value_max=999, interval='   ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_height, pos=(485, 602), camp_name='Patient Height', len_max=3, len_min=1,value_min=1, value_max=999, interval='   ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=cid10, pos=(34, 455), camp_name='Cid10', len_max=4, len_min=3, interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_datetime(can=c, date=solicitation_datetime, pos=(292, 222), camp_name='Solicitation Datetime', hours=False, interval='   ', formated=False)
            if type(c) == type(Response()): return c
            c = global_functions.add_document_cns_cpf_rg(can=c, document=prof_solicitor_document, pos_square_cpf=(41, 195), pos_square_cns=(84,194), pos_cns=(129, 195), pos_cpf=(129, 195),camp_name='Professional Solicitor Document', interval='  ', square_size=(5, 8))
            if type(c) == type(Response()): return c


            c.setFont('Roboto-Mono', 9)
            c = global_functions.add_oneline_text(can=c, text=establishment_solitc_name, pos=(206, 658), camp_name='Establishment Solicit Name', len_max=65, len_min=8)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_name, pos=(36, 628), camp_name='Patient Name', len_max=79, len_min=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(36, 602), camp_name='Patient Mother Name', len_max=79, len_min=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_morelines_text(can=c, text=anamnese, initial_pos=(36, 430), decrease_ypos= 10, camp_name='Anamnese', len_max=485, char_per_lines=97, len_min=5)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=prof_solicitor_name, pos=(36, 224), camp_name='Professional Solicitor Name', len_max=45, len_min=8)
            if type(c) == type(Response()): return c

        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            c.setFont('Roboto-Mono', 10)
            
            
            
            c.setFont('Roboto-Mono', 9)
            c = global_functions.add_document_cns_cpf_rg(can=c, document=patient_document, pos_square_cpf=(40, 66), pos_square_cns=(84,66), pos_cns=(129, 66), pos_cpf=(129, 66),camp_name='Patient Document', interval='  ', nullable=True, square_size=(5, 8))
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=diagnostic, pos=(105, 455), camp_name='Diagnostic', len_max=84, len_min=4, nullable=True)
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
        return Response("Error while filling aih sus", status=500)



if __name__ == "__main__":
    lenght_test = ''
    for x in range(0, 2000):
        lenght_test += str(x)
    import global_functions
    output = fill_pdf_lme(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        patient_name='Patient Name',
        patient_mother_name='Patient Mother Name',
        patient_weight=142,
        patient_height=180,
        cid10='A123',
        anamnese="Anamnese",
        prof_solicitor_name="Professional Solicitor Name",
        solicitation_datetime=datetime.datetime.now(),
        prof_solicitor_document={'CPF':28445400070},
        diagnostic='Diagnostic',
        patient_document={'CNS':928976954930007}
    )

    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/tests/pdfs_created_files_test/lme_teste.pdf")












