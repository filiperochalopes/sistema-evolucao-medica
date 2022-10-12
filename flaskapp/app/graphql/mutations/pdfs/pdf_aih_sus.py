import datetime
from PyPDF2  import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from flask import Response

# Doing the import this way only when is called by antoher file (like pytest)
if __name__ != "__main__":
    from . import global_functions

template_directory = "./graphql/mutations/pdfs/pdfs_templates/aih_sus.pdf"

#REMOVE THIS AFTER TESTS
testLenght = ''
for x in range(0, 400):
    testLenght += str(x)

#CAMPOS NÃO OBRIGATÓRIOS: 
# Número do prontuário, 
# raça, 
# nome do responsável, 
# telefones, 
# Resultados de exames realizados, 
# CID10 Secundário, 
# CID10 Causas Associadas. 
# Seção de Acidentes ou Violências e Autorização.

def fill_pdf_aih_sus():
    try:
        packet = io.BytesIO()
        # Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        c.setFont('Helvetica', 9)
        # Writing all data in respective fields
        # not null data
        try:
            
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
        return Response("Error while filling ficha de internamento", status=500)

def add_data(canvas:canvas.Canvas, data:str, pos:tuple):
    """Add data in pdf using canvas object

    Args:
        canvas (canvas.Canvas): canvas that will be used to add data
        data (str): data to be added
        pos (tuple): data insert position in points

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response: with the error)
    """
    try:
        canvas.drawString(pos[0], pos[1], data)
        return canvas
    except:
        return Response("Error when adding data to document with canvas", status=500)


def add_square(canvas:canvas.Canvas, pos:tuple, size:int=9):
    """Add square in document using canvas object

    Args:
        canvas (canvas.Canvas): canvas to use
        pos (tuple): position to add the square
        size (int, optional): square size default is the size of the option quare. Defaults to 9.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response: with the error)
    """    
    try:
        canvas.rect(x=pos[0], y=pos[1], width=size, height=size, fill=1)
        return canvas
    except:
        return Response("Error when adding square to document with canvas", status=500)


def write_newpdf(newpdf:PdfWriter, new_directory:str):
    """Write new pdf in a file

    Args:
        newpdf (PdfFileWriter): new pdf with all the changes made by canvas
        new_directory (str): directory to save the new pdf
    Returns:
        None
        or
        Response(flask.Response: with the error)
    """ 
    try:
        outputFile = open(new_directory, 'wb')
        newpdf.write(outputFile)
        outputFile.close()
    except:
        return Response("Error when writing new pdf", status=500)

if __name__ == "__main__":
    import global_functions
    output = fill_pdf_aih_sus()
    if type(output) == type(Response()): 
        print(output.response)
    write_newpdf(output, "./graphql/mutations/pdfs/aih_sus_teste.pdf")