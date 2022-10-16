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
        c.setFont('Roboto-Mono', 9)
    
        # Writing all data in respective fields
        # not null data
        try:
            c = add_patientName(canvas=c, name=patient_name)
            # verify if c is a error at some point
            if type(c) == type(Response()): return c
            c = add_patientCNS(canvas=c, cns=patient_cns)
            if type(c) == type(Response()): return c
            # change font size to datetime            
            c.setFont('Roboto-Mono', 13)            
            c = add_documentDatetime(canvas=c, docDatetime=documentDatetime)
            if type(c) == type(Response()): return c            
            c.setFont('Roboto-Mono', 9)            
            c = add_patientBirthday(canvas=c, birthday=patient_birthday)
            if type(c) == type(Response()): return c
            c = add_patient_sex(canvas=c, sex=patient_sex)
            if type(c) == type(Response()): return c
            c = add_patientMotherName(canvas=c, motherName=patient_motherName)
            if type(c) == type(Response()): return c
            c = add_patientDocument(canvas=c, document=patient_document)
            if type(c) == type(Response()): return c
            c = add_patientAdress(canvas=c, adress=patient_adress)
            if type(c) == type(Response()): return c
            c = add_doctorName(canvas=c, name=doctor_name)
            if type(c) == type(Response()): return c
            c = add_doctorCNS(canvas=c, cns=doctor_cns)
            if type(c) == type(Response()): return c
            c = add_doctorCRM(canvas=c, crm=doctor_crm)
            if type(c) == type(Response()): return c
            c = add_evolution(canvas=c, evol=evolution)
            if type(c) == type(Response()): return c
        
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)
            
        #Adding data that can be null
        try:
            if orientations is not None and str(orientations).strip() != "":
                c = add_orientations(canvas=c, orientations=orientations)
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
        return Response("Error while filling ficha de internamento", status=500)


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
        # verify if patient name is smaller than 60 characters
        name = str(name)
        if 7 < len(name.strip()) <= 64:
            canvas = global_functions.add_data(canvas=canvas, data=name, pos=(27, 674))
            return canvas
        else:
            return Response("Unable to add patient name because is longer than 64 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding patient name', status=500)


def add_doctorName(canvas:canvas.Canvas, name:str):
    """add doctor name

    Args:
        canvas (canvas.Canvas): canvas to user
        name (str): doctor name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """
    try:
        if type(name) != type(str()):
            return Response('Doctor name has to be string', status=400)
        # verify if doctor name is smaller than 60 characters
        name = str(name)
        if 7 < len(name.strip()) <= 49:
            canvas = global_functions.add_data(canvas=canvas, data=name, pos=(304, 195))
            return canvas
        else:
            return Response("Unable to add doctor name because is longer than 49 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding doctor name', status=500)


def add_patientCNS(canvas:canvas.Canvas, cns:int):
    """Add patient cns to document

    Args:
        canvas (canvas.Canvas): canvas to use
        cns (int): patient cns

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(cns) != type(int()):
            return Response('Patient CNS has to be int', status=400)
        # Verify if the cns is valid
        if global_functions.isCNSvalid(cns):
            # format cns to add in document
            cns = str(cns)
            cns = cns[:3] + " " + cns[3:7] + " " + cns[7:11] + " " + cns[11:15]
            canvas = global_functions.add_data(canvas=canvas, data=cns, pos=(393, 674))
            return canvas
        else:
            return Response("Unable to add patient cns because is a invalid CNS", status=400)
    except:
        return Response('Unknow error while adding patient cns', status=500)


def add_doctorCNS(canvas:canvas.Canvas, cns:int):
    """Add doctor cns to document

    Args:
        canvas (canvas.Canvas): canvas to use
        cns (int): doctor cns

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(cns) != type(int()):
            return Response('Doctor CNS has to be int', status=400)
        # Verify if the cns is valid
        if global_functions.isCNSvalid(cns):
            # format cns to add in document
            cns = str(cns)
            cns = cns[:3] + " " + cns[3:7] + " " + cns[7:11] + " " + cns[11:15]
            canvas = global_functions.add_data(canvas=canvas, data=cns, pos=(304, 163))
            return canvas
        else:
            return Response("Unable to add doctor cns because is a invalid CNS", status=400)
    except:
        return Response('Unknow error while adding doctor cns', status=500)


def add_doctorCRM(canvas:canvas.Canvas, crm:str):
    """add doctor crm to document

    Args:
        canvas (canvas.Canvas): canvas to use
        crm (str): doctor crm

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(crm) != type(str()):
            return Response('Doctor CRM has to be str', status=400)
        if 11 > len(crm) or len(crm) > 13:
            return Response('CRM is not valid, use the format "CRM/UF 123456"', status=400)
        canvas = global_functions.add_data(canvas=canvas, data=crm, pos=(304, 131))
        return canvas
    except:
        return Response('Unknow error while adding doctor crm', status=500)


def add_documentDatetime(canvas:canvas.Canvas, docDatetime:datetime.datetime):
    """Add document datetime to docuemnt

    Args:
        canvas (canvas.Canvas): canvas to use
        docDatetime (datetime.datetime): datetime to add
    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(docDatetime) != type(datetime.datetime.now()):
            return Response('Document Datetime isnt a datetime.datetime object', status=400)
        # Format docDatetime to format DD/MM/YYYY H:M:S
        docDatetime = docDatetime.strftime("%m/%d/%Y %H:%M:%S")

        canvas = global_functions.add_data(canvas=canvas, data=docDatetime, pos=(410, 740))
        return canvas
    except:
        return Response('Unkown error while adding document datetime', status=500)


def add_patientBirthday(canvas:canvas.Canvas, birthday:datetime.datetime):
    """Add patient birthday to document

    Args:
        canvas (canvas.Canvas): canvas to use
        birthday (datetime.datetime): birthday to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(birthday) != type(datetime.datetime.now()):
            return Response('Pacient birthday isnt a datetime.datetime object', status=400)
        # Format birthday to format DD/MM/YYYY
        birthday = birthday.strftime("%m/%d/%Y")
        canvas = global_functions.add_data(canvas=canvas, data=birthday, pos=(27, 642))
        return canvas
    except:
        return Response('Unkown error while adding patient birthday', status=500)


def add_patient_sex(canvas:canvas.Canvas, sex:str):
    """Add patient sex to document

    Args:
        canvas (canvas.Canvas): canvas to use
        sex (str): patient sex

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        sex = str(sex).upper()
        if len(sex) != 1:
            return Response('Pacient sex has to be only one character F or M', status=400)
        if sex not in ['M', 'F']:
            return Response('Pacient sex is not valid, use F or M', status=400)
        else:
            if sex == 'M':
                canvas = global_functions.add_square(canvas=canvas, pos=(117, 640))
                return canvas
            else:
                canvas = global_functions.add_square(canvas=canvas, pos=(147, 640))
                return canvas
    except:
        return Response('Unkown error while adding patient sex', status=500)


def add_patientMotherName(canvas:canvas.Canvas, motherName:str):
    """Add patient mother name to document

    Args:
        canvas (canvas.Canvas): canvas ro use
        motherName (str): patient mother name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(motherName) != type(str()):
            return Response('Mother name has to be str', status=400)
        # verify if patient motherName is smaller than 60 characters
        if 7 < len(motherName.strip()) <= 69:
            canvas = global_functions.add_data(canvas=canvas, data=motherName, pos=(194, 642))
            return canvas
        else:
            return Response("Unable to add patient motherName because is longer than 69 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding patient motherName', status=500)


def add_patientDocument(canvas:canvas.Canvas, document:dict):
    """Add patient document, CPF or Rg

    Args:
        canvas (canvas.Canvas): canvas to use
        document (dict): dict with format {"doc":number}
    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(document) != type(dict()):
            return Response('Patient document has to be a dict {"document":"number"}', status=400)
        # See id document is CPF or RG
        if 'RG' in document.keys():
            #The only verificatinon is that rg is not greater than 16 characteres
            if global_functions.isRGvalid(document['RG']):
                canvas = global_functions.add_data(canvas=canvas, data=str(document['RG']), pos=(92, 610))
                canvas = global_functions.add_square(canvas=canvas, pos=(58, 608))
                return canvas
            else:
                return Response('Patient RG is not valid', status=400)
        elif 'CPF' in document.keys():
            #Format cpf to validate
            cpf = str(document['CPF'])
            cpf = cpf[:3] + "." + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
            if global_functions.isCPFvalid(cpf):
                canvas = global_functions.add_data(canvas=canvas, data=cpf, pos=(92, 610))
                canvas = global_functions.add_square(canvas=canvas, pos=(24, 608))
                return canvas
            else:
                return Response('Patient CPF is not valid', status=400)
        else:
            return Response('The document was not CPF or RG', status=400)
    except:
        return Response('Unknow error while adding patient Document', status=500)


def add_patientAdress(canvas:canvas.Canvas, adress:str):
    """Add patient Adress to document

    Args:
        canvas (canvas.Canvas): canvas to use
        adress (str): adress to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(adress)!= type(str()):
            return Response('Adress has to be str', status=400)
        adress = adress.strip()
        if 7 < len(adress) <= 63:
            canvas = global_functions.add_data(canvas=canvas, data=adress, pos=(230, 610))
            return canvas
        else:
            return Response("Unable to add patient adress because is longer than 63 characters or smaller than 7", status=400)
    except:
        Response('Unknow error while adding patient Adress', status=500)


def add_evolution(canvas:canvas.Canvas, evol:str):
    """add evolution to document

    Args:
        canvas (canvas.Canvas): canvas to use
        evol (str): Evolution

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(evol) != type(str()):
            return Response('Evolution has to be a string', status=400)
        evol = evol.strip()
        if len(evol) > 2100 or len(evol) < 10:
            return Response('Evolution has to be at least 10 characters and no more than 2100 characters', status=400)
        # Making the line break whem has 105 charater in a line
        str_evol = ''
        brokeLinexTimes = int(len(evol)/100)
        currentLine = 100
        lastline = 0
        yposition = 540
        while brokeLinexTimes >= 0:
            str_evol = evol[lastline:currentLine]
            canvas = global_functions.add_data(canvas=canvas, data=str_evol, pos=(26, yposition))
            lastline = currentLine
            currentLine += 100
            brokeLinexTimes -= 1
            yposition -= 10

        del(str_evol)
        del(brokeLinexTimes)
        del(currentLine)
        del(lastline)
        del(yposition)
        return canvas
    except:
        return Response('Unknow error while adding patient Evolution', status=500)


def add_orientations(canvas:canvas.Canvas, orientations:str):
    """add orientations to documento

    Args:
        canvas (canvas.Canvas): canvas to use
        orientations (str): orientations

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(orientations) != type(str()):
            return Response('Orientations has to be a string', status=400)
        orientations = orientations.strip()
        if len(orientations) > 800 or len(orientations) < 10:
            return Response('Orientations has to be at least 10 characters and no more than 800 characters', status=400)
        # Making the line break whem has 105 charater in a line
        str_orientations = ''
        brokeLinexTimes = int(len(orientations)/100)
        currentLine = 100
        lastline = 0
        yposition = 312
        while brokeLinexTimes >= 0:
            str_orientations = orientations[lastline:currentLine]
            canvas = global_functions.add_data(canvas=canvas, data=str_orientations, pos=(26, yposition))
            lastline = currentLine
            currentLine += 100
            brokeLinexTimes -= 1
            yposition -= 10

        del(str_orientations)
        del(brokeLinexTimes)
        del(currentLine)
        del(lastline)
        del(yposition)
        return canvas
    except:
        return Response('Unknow error while adding patient Orientations', status=500)

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
    