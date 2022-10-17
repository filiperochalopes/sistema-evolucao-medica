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

def fill_pdf_apac(establishment_solitc_name:str):
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
            c = global_functions.add_oneline_text(can=c, text=str(lenghtTest[:500]), pos=(36, 744), campName='Establishment Solict Name', lenMax=600, lenMin=7)
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
        establishment_solitc_name='Establishment Solicit Name'
    )

    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/apac_teste.pdf")
