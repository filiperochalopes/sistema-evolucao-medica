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

template_directory = "./graphql/mutations/pdfs/pdfs_templates/two_pages_precricao_medica_template.pdf"
pagesizePoints = (841.92, 595.2)
font_directory = "./graphql/mutations/pdfs/Roboto-Mono.ttf"

def fill_pdf_precricao_medica(document_datetime:datetime.datetime, pacient_name:str, prescrition:list):
    
    packet = io.BytesIO()
    # Create canvas and add data
    c = canvas.Canvas(packet, pagesize=pagesizePoints)
    # Change canvas font to mach with the document
    # this is also changed in the document to some especific fields
    pdfmetrics.registerFont(TTFont('Roboto-Mono', font_directory))
    c.setFont('Roboto-Mono', 12)
    # Writing all data in respective fields
    # not null data
    try:
        c = add_document_datetime(canvas=c, date=document_datetime)
        if type(c) == type(Response()): return c
        c = add_patient_name(canvas=c, name=pacient_name)
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


def add_patient_name(canvas:canvas.Canvas, name:str):
    """Add patient name to document

    Args:
        canvas (canvas.Canvas): canvas to add
        name (str): name to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(name) != type(str()):
            return Response('patient name has to be string', status=400)
        # verify if patient name is smaller than 60 characters
        name = str(name)
        if 7 < len(name.strip()) <= 34:
            canvas = global_functions.add_data(canvas=canvas, data=name, pos=(120, 505))
            canvas = global_functions.add_data(canvas=canvas, data=name, pos=(571, 505))
            return canvas
        else:
            return Response("Unable to add patient name because is longer than 34 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding patient name', status=500)


def add_document_datetime(canvas:canvas.Canvas, date:datetime.datetime):
    """add document datetime to respective fields

    Args:
        canvas (canvas.Canvas): canvas to add
        date (datetime.datetime): document datetime

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(date) != type(datetime.datetime.now()):
            return Response('Document datetime isnt a datetime.datetime object', status=400)
        #Add to respective fields
        date = str(date.day) + '.' + str(date.month) + '.' + str(date.year)
        interval = ' ' * 2
        date = date.replace('.', interval)
        canvas = global_functions.add_data(canvas=canvas, data=date, pos=(294, 38))
        canvas = global_functions.add_data(canvas=canvas, data=date, pos=(744, 38))
        return canvas
    except:
        return Response('Unkown error while adding document datetime', status=500)


if __name__ == "__main__":
    import global_functions
    output = fill_pdf_precricao_medica(
        document_datetime=datetime.datetime.now(),
        pacient_name='Pacient Name',
        prescrition=['aaa']
    )

    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/prescricao_medica_teste.pdf")