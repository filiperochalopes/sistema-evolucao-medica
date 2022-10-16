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

#The templat will change depending on exems lenght
pags_quant = 1
template_directory = ["./graphql/mutations/pdfs/pdfs_templates/one_exam_request.pdf", "./graphql/mutations/pdfs/pdfs_templates/two_exam_request.pdf", "./graphql/mutations/pdfs/pdfs_templates/three_exam_request.pdf"]
font_directory = "./graphql/mutations/pdfs/Roboto-Mono.ttf"


def fill_pdf_exam_request(patient_name:str, patient_cns:int, patient_birthday:datetime.datetime, patient_adress:str, solicitation_reason:str, prof_solicitor:str, prof_authorized:str, solicitation_datetime:datetime.datetime, autorization_datetime:datetime.datetime=None, document_pacient_date:datetime.datetime=None, document_pacient_name:str=None):
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
            c = add_patientName(canvas=c, name=patient_name)
            # verify if c is a error at some point
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
        template_pdf = PdfReader(open(template_directory[pags_quant-1], "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        return output
    except:
        return Response("Error while filling exam request", status=500)


def add_patientName(canvas:canvas.Canvas, name:str):
    """Add patient name to pdf

    Args:
        canvas (canvas.Canvas): canvas to use
        name (str): patient name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """  
    try:
        if type(name) != type(str()):
            return Response('Patient name has to be string', status=400)
        # verify if patient name is smaller than 70 characters
        name = str(name)
        if 7 < len(name.strip()) <= 70:
            canvas = global_functions.add_data(canvas=canvas, data=name, pos=(7, 775))
            return canvas
        else:
            return Response("Unable to add patient name because is longer than 70 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding patient name', status=500)




if __name__ == "__main__":
    import global_functions
    output = fill_pdf_exam_request(
        patient_name='Patient Name', 
        patient_cns=928976954930007, 
        patient_birthday=datetime.datetime.now(), 
        patient_adress="Patient Adress", 
        solicitation_reason="Solicitation Reason", 
        prof_solicitor="Professional Solicitor", 
        prof_authorized="Professional Authorized", 
        solicitation_datetime=datetime.datetime, 
        autorization_datetime=datetime.datetime.now(), document_pacient_date=datetime.datetime.now(), 
        document_pacient_name='Document pacient name'
    )
    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/exam_request.pdf")