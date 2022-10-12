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

def fill_pdf_aih_sus(establishment_solitc_name:str, establishment_solitc_cnes:int,
establishment_exec_name:str, establishment_exec_cnes:int, patient_name:str, patient_cns:int):
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
            c = add_establishment_solitc_name(canvas=c, name=establishment_solitc_name)
            if type(c) == type(Response()): return c
            c = add_establishment_solitc_cnes(canvas=c, cnes=establishment_solitc_cnes)
            if type(c) == type(Response()): return c
            c = add_establishment_exec_name(canvas=c, name=establishment_exec_name)
            if type(c) == type(Response()): return c
            c = add_establishment_exec_cnes(canvas=c, cnes=establishment_exec_cnes)
            if type(c) == type(Response()): return c
            c = add_patient_name(canvas=c, name=patient_name)
            if type(c) == type(Response()): return c
            c = add_patient_cns(canvas=c, cns=patient_cns)
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


def add_establishment_solitc_name(canvas:canvas.Canvas, name:str):
    """add establishment solict name

    Args:
        canvas (canvas.Canvas): canvas to use
        name (str): establishment solict name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(name) != type(str()):
            return Response('Solicitate Establishment name has to be string', status=400)
        # verify if Solicitate Establishment name is smaller than 60 characters
        name = str(name)
        if 7 < len(name.strip()) <= 78:
            canvas = add_data(canvas=canvas, data=name, pos=(43, 750))
            return canvas
        else:
            return Response("Unable to add Solicitate Establishment name because is longer than 78 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding Solicitate Establishment  name', status=500)


def add_establishment_solitc_cnes(canvas:canvas.Canvas, cnes:int):
    """add establshment solitc cnes in document

    Args:
        canvas (canvas.Canvas): canvas to use
        cnes (int): cnes to insert

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(cnes) != type(int()):
            return Response('Establishment Solitc Cnes has to be int', status=400)
        # Verify if the cnes is valid
        cnes = str(cnes)
        if len(cnes) == 7:
            #Add one number at every field
            cont = 0
            xpos = 471
            while cont < 7:
                canvas = add_data(canvas=canvas, data=cnes[cont], pos=(xpos, 750))
                cont += 1
                xpos += 15
            return canvas
        return Response('unable to add establshment CNES because is a invalid CNES', status=400)
    except:
        return Response('Unknow error while adding establishment solict cnes', status=500)


def add_establishment_exec_name(canvas:canvas.Canvas, name:str):
    """add establishment exec name 

    Args:
        canvas (canvas.Canvas): canavs to user
        name (str): establishment name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(name) != type(str()):
            return Response('Exec Establishment name has to be string', status=400)
        # verify if Exec Establishment name is smaller than 60 characters
        name = str(name)
        if 7 < len(name.strip()) <= 78:
            canvas = add_data(canvas=canvas, data=name, pos=(43, 726))
            return canvas
        else:
            return Response("Unable to add Exec Establishment name because is longer than 78 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding Exec Establishment name', status=500)


def add_establishment_exec_cnes(canvas:canvas.Canvas, cnes:int):
    """add establishment exec cnes

    Args:
        canvas (canvas.Canvas): canvas to user
        cnes (int): cns to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(cnes) != type(int()):
            return Response('Establishment Exec Cnes has to be int', status=400)
        # Verify if the cnes is valid
        cnes = str(cnes)
        if len(cnes) == 7:
            #Add one number at every field
            cont = 0
            xpos = 471
            while cont < 7:
                canvas = add_data(canvas=canvas, data=cnes[cont], pos=(xpos, 726))
                cont += 1
                xpos += 15
            return canvas
        return Response('unable to add Establishment Exec Cnes because is a invalid CNES', status=400)
    except:
        return Response('Unknow error while adding Establishment Exec Cnes', status=500)

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
        if 7 < len(name.strip()) <= 70:
            canvas = add_data(canvas=canvas, data=name, pos=(43, 683))
            return canvas
        else:
            return Response("Unable to add patient name because is longer than 70 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding patient name', status=500)


def add_patient_cns(canvas:canvas.Canvas, cns:int):
    """add patient cns to every block

    Args:
        canvas (canvas.Canvas): canvas to use
        cns (int): cns to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response ifhapens some error 

    """    
    try:
        if type(cns) != type(int()):
            return Response('patient CNS has to be int', status=400)
        # Verify if the cns is valid
        if global_functions.isCNSvalid(cns):
            #Add one number at every field
            cns = str(cns)
            cont = 0
            xpos = 28
            while cont < 15:
                canvas = add_data(canvas=canvas, data=cns[cont], pos=(xpos, 658))
                cont += 1
                xpos += 18
            return canvas
        else:
            return Response("Unable to add patient cns because is a invalid CNS", status=400)
    except:
        return Response('Unknow error while adding patient cns', status=500)


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
    output = fill_pdf_aih_sus(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        establishment_exec_name='Establshment Exec Name',
        establishment_exec_cnes=7654321,
        patient_name='Patient Name',
        patient_cns=928976954930007
    )
    if type(output) == type(Response()): 
        print(output.response)
    write_newpdf(output, "./graphql/mutations/pdfs/aih_sus_teste.pdf")