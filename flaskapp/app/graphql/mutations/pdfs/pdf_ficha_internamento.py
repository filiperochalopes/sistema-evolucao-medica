import datetime
from PyPDF2  import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from flask import Response


template_directory = "./graphql/mutations/pdfs/pdfs_templates/ficha_de_internamento_hmlem.pdf"


def fill_pdf_ficha_internamento(datetime:datetime, patient_name:str, patient_cns:int, patient_birthday:datetime):

    try:

        packet = io.BytesIO()
        #Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        #Change canvas font to mach with the document
        c.setFont('Helvetica', 9)
        #Writing all data in respective fields
        try:
            c = add_patientName(canvas=c, name=patient_name)
            #c = add_patientCNS(canvas=c, cns=patient_cns)

            if type(c) == type(Response()):
                return c
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding data to fields', status=500)
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

def add_patientName(canvas:canvas.Canvas, name:str):

    try:
        #verify if patient name is smaller than 60 characters
        if len(name.strip()) <= 60:
            canvas = add_data(canvas=canvas, data=name, pos=(27, 673))
            return canvas
        else:
            return Response("Unable to add patient name because is longer than 60 characters", status=400)
    except:
        return Response('Unknow error while adding patient name', status=500)

def add_patientCNS(canvas:canvas.Canvas, cns:int):
    pass

def add_data(canvas:canvas.Canvas, data:str, pos:tuple):
    """Add data in pdf using canvas object

    Args:
        canvas (canvas.Canvas): canvas that will be used to add data
        data (str): data to be added
        pos (tuple): data insert position in points

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Reponse(flask.Response: with the error)
    """
    try:
        canvas.drawString(pos[0], pos[1], data)
        return canvas
    except:
        return Response("Error when adding data to document with canvas", status=500)


def write_newpdf(newpdf:PdfWriter, new_directory:str):
    """Write new pdf in a file

    Args:
        newpdf (PdfFileWriter): new pdf with all the changes made by canvas
        new_directory (str): directory to save the new pdf
    Returns:
        None
        or
        Reponse(flask.Response: with the error)
    """ 
    try:
        outputFile = open(new_directory, 'wb')
        newpdf.write(outputFile)
        outputFile.close()
    except:
        return Response("Error when writing new pdf", status=500)


if __name__ == "__main__":
    output = fill_pdf_ficha_internamento(
        datetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now()
        )
    print(output.response)
    write_newpdf(output, "./graphql/mutations/pdfs/ficha_teste.pdf")
    