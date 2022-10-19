import datetime
from PyPDF2  import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from flask import Response

# Doing the import this way only when is called by antoher file (like pytest)
if __name__ != "__main__":
    from . import global_functions

lenghtTest = ''
for x in range(0, 2000):
    lenghtTest += str(x)

template_directory = "./graphql/mutations/pdfs/pdfs_templates/relatorio_de_alta.pdf"
font_directory = "./graphql/mutations/pdfs/Roboto-Mono.ttf"

def fill_pdf_relatorio_alta(documentDatetime:datetime.datetime, patient_name:str, patient_cns:int, patient_birthday:datetime.datetime, patient_sex:str, patient_motherName:str, patient_document:dict, patient_adress:str, evolution:str, doctor_name:str, doctor_cns:int, doctor_crm:str, orientations:str=None):
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
            c = global_functions.add_datetime(can=c, date=documentDatetime, pos=(410, 740), campName='Document Datetime', hours=True, formated=True)
            if type(c) == type(Response()): return c          
            
            
            # change font size to normal            
            c.setFont('Roboto-Mono', 9)            
            c = global_functions.add_oneline_text(can=c, text=patient_name, pos=(27, 674), campName='Patient Name', lenMax=64, lenMin=7)
            # verify if c is a error at some point
            if type(c) == type(Response()): return c
            c = global_functions.add_cns(can=c, cns=patient_cns, pos=(393, 674), campName='Patient CNS', formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_datetime(can=c, date=patient_birthday, pos=(27, 642), campName='Patient Birthday', hours=False, formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(117, 640), pos_fem=(147, 640), campName='Patient Sex', square_size=(9,9))
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_motherName, pos=(194, 642), campName='Patient Mother Name', lenMax=69, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_document_cns_cpf_rg(can=c, document=patient_document, pos_square_cpf=(24, 608), pos_square_rg=(58,608), pos_rg=(92, 610), pos_cpf=(92, 610),campName='Pacient Document', formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adress, pos=(230, 610), campName='Patient Adress', lenMax=63, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=doctor_name, pos=(304, 195), campName='Doctor Name', lenMax=49, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_cns(can=c, cns=doctor_cns, pos=(304, 163), campName='Doctor CNS', formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=doctor_crm, pos=(304, 131), campName='Doctor CRM', lenMax=13, lenMin=11)
            if type(c) == type(Response()): return c
            c = global_functions.add_morelines_text(can=c, text=evolution, initial_pos=(26, 540), decrease_ypos=10, campName='Evolution Resume', lenMax=2100, lenMin=10, charPerLines=100)

            if type(c) == type(Response()): return c
        
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)
            
        #Adding data that can be null
        try:
            c = global_functions.add_morelines_text(can=c, text=orientations, initial_pos=(26, 312), decrease_ypos=10, campName='Orientations', lenMax=800, lenMin=10, charPerLines=100, nullable=True)
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


if __name__ == "__main__":
    import global_functions
    output = fill_pdf_relatorio_alta(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CPF':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        evolution='Current illnes hsitoryaaaaaaaaaaaedqeqa',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        orientations='Do not jump'
        )
    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/relatorio_alta_teste.pdf")
    