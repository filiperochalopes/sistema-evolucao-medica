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

template_directory = "./graphql/mutations/pdfs/pdfs_templates/apac.pdf"
font_directory = "./graphql/mutations/pdfs/Roboto-Mono.ttf"

#Aqui tem muito campo NÃO obrigatório. Só o que precisa de fato ser preenchido são: 
# Nome do estabelecimento, -
# CNES, -
# Nome do paciente,  -
# CNS, 
# data de nascimento, 
# sexo, 
# municipio de residência,  -
# código do procedimento principal, 
# nome do procedimento -
# quantidade proced princiapl. 
# A seção procedimento secundário é opcional. Descrição do diagnóstico, CID10 principal e observações são obrigattórios. Todo campo de seção "Solicitação" são obrigatórios
def fill_pdf_apac(establishment_solitc_name:str, establishment_solitc_cnes:int, patient_name:str, patient_cns:int,patient_adress_city:str, main_procedure_name:str):
    try:
        packet = io.BytesIO()
        # Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', font_directory))
        c.setFont('Roboto-Mono', 9)
        # Writing all data in respective fields
        # not null data
        try:
            c = global_functions.add_oneline_text(can=c, text=establishment_solitc_name, pos=(36, 742), campName='Establishment Solict Name', lenMax=77, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_name, pos=(36, 702), campName='Patient Name', lenMax=67, lenMin=7)
            if type(c) == type(Response()): return c

            c.setFont('Roboto-Mono', 10)
            c = global_functions.add_cns(can=c, cns=patient_cns, pos=(36, 678), campName='Patient CNS', interval='  ')
            if type(c) == type(Response()): return c

            c.setFont('Roboto-Mono', 9)
            c = global_functions.add_oneline_text(can=c, text=patient_adress_city, pos=(36, 584), campName='Patient Adress City', lenMax=58, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=main_procedure_name, pos=(220, 542), campName='Main Procedure Name', lenMax=50, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=establishment_solitc_cnes, pos=(468, 742), campName='Establishment Solict CNES', lenMax=7, lenMin=7)
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
        return Response("Error while filling apac", status=500)



if __name__ == "__main__":
    import global_functions
    output = fill_pdf_apac(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        patient_name='Patient Name',
        patient_cns=928976954930007,
        patient_adress_city='Patient Adress City',
        main_procedure_name='Main procedure Name'
    )

    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/apac_teste.pdf")
