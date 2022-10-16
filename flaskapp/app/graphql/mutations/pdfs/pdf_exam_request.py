import datetime
from PyPDF2  import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from flask import Response
from math import ceil

# Doing the import this way only when is called by antoher file (like pytest)
if __name__ != "__main__":
    from . import global_functions

lenghtTest = ''
for x in range(0, 2000):
    lenghtTest += str(x)

#The templat will change depending on exems lenght
template_directory = ["./graphql/mutations/pdfs/pdfs_templates/one_exam_request.pdf", "./graphql/mutations/pdfs/pdfs_templates/two_exam_request.pdf", "./graphql/mutations/pdfs/pdfs_templates/three_exam_request.pdf"]
font_directory = "./graphql/mutations/pdfs/Roboto-Mono.ttf"


def fill_pdf_exam_request(patient_name:str, patient_cns:int, patient_birthday:datetime.datetime, patient_adress:str, solicitation_reason:str,
exams:str, prof_solicitor:str, prof_authorized:str, solicitation_datetime:datetime.datetime, autorization_datetime:datetime.datetime=None, document_pacient_date:datetime.datetime=None, document_pacient_name:str=None):

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
            global pags_quant
            c, pags_quant = add_exams(canvas=c, exams=exams)
            # verify if c is a error at some point
            if type(c) == type(Response()): return c
            c = add_patientName(canvas=c, name=patient_name)
            if type(c) == type(Response()): return c
            c = add_patient_cns(canvas=c, cns=patient_cns)
            if type(c) == type(Response()): return c
            c = add_patient_birthday(canvas=c, birthday=patient_birthday)
            if type(c) == type(Response()): return c
            c = add_patient_adress(canvas=c, adress=patient_adress)
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
            ypos = 775
            for x in range(pags_quant):
                canvas = global_functions.add_data(canvas=canvas, data=name, pos=(7, ypos))
                ypos -= 280

            return canvas
        else:
            return Response("Unable to add patient name because is longer than 70 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding patient name', status=500)


def add_exams(canvas:canvas.Canvas, exams:str):
    """add solicited exams

    Args:
        canvas (canvas.Canvas): canvas to use
        exams (str): exams

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(exams) != type(str()):
            return Response('Exams has to be a string', status=400)
        exams = exams.strip()
        if len(exams) > 972 or len(exams) < 5:
            return Response('Exams has to be at least 5 characters and no more than 972 characters', status=400)
        # Making the line break whem has 105 charater in a line
        str_exams = ''
        exams = lenghtTest[:850].strip()
        #Calculate how many pags will have, ceil function round to upper int
        pags_quant = ceil(len(exams)/324)
        charByLine = 108
        brokeLinexTimes = int(len(exams)/charByLine)
        currentLine = charByLine
        lastline = 0
        yposition = 649
        cont = 0
        for x in range(pags_quant):
            while brokeLinexTimes >= 0:
                str_exams = exams[lastline:currentLine]
                canvas = global_functions.add_data(canvas=canvas, data=str_exams, pos=(7, yposition))
                lastline = currentLine
                currentLine += charByLine
                brokeLinexTimes -= 1
                cont += 1
                if cont%3 == 0:
                    break
                yposition -= 10
            yposition -= 260

        del(str_exams)
        del(brokeLinexTimes)
        del(currentLine)
        del(lastline)
        del(yposition)
        return canvas, pags_quant
    except:
        return Response('Unknow error while adding Solicited Exams', status=500)


def add_patient_cns(canvas:canvas.Canvas, cns:int):
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
            ypos = 765
            for x in range(pags_quant):
                canvas = global_functions.add_data(canvas=canvas, data=cns, pos=(450, ypos))
                ypos -= 280
            return canvas
        else:
            return Response("Unable to add patient cns because is a invalid CNS", status=400)
    except:
        return Response('Unknow error while adding patient cns', status=500)


def add_patient_birthday(canvas:canvas.Canvas, birthday:datetime.datetime):
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
        birthday = str(birthday.day) + '/' + str(birthday.month) + '/' + str(birthday.year)
        ypos = 784
        for x in range(pags_quant):
            canvas = global_functions.add_data(canvas=canvas, data=birthday, pos=(441, ypos))
            ypos -= 280
        return canvas
    except:
        return Response('Unkown error while adding patient birthday', status=500)


def add_patient_adress(canvas:canvas.Canvas, adress:str):
    """add patient adress

    Args:
        canvas (canvas.Canvas): canvas to use
        adress (str): patient adress

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(adress)!= type(str()):
            return Response('Adress has to be str', status=400)
        if 7 < len(adress) <= 216:
            # Making the line break whem has 105 charater in a line
            str_adress = ''
            adress = lenghtTest[:216].strip()
            charByLine = 108
            brokeLinexTimes = int(len(adress)/charByLine)
            currentLine = charByLine
            lastline = 0
            yposition = 734
            while brokeLinexTimes > 0:
                str_adress = adress[lastline:currentLine]
                canvas = global_functions.add_data(canvas=canvas, data=adress, pos=(7, yposition))
                canvas = global_functions.add_data(canvas=canvas, data=adress, pos=(7, yposition - 280))
                canvas = global_functions.add_data(canvas=canvas, data=adress, pos=(7, yposition - 560))
                lastline = currentLine
                currentLine += charByLine
                brokeLinexTimes -= 1
                yposition -= 10

            del(str_adress)
            del(brokeLinexTimes)
            del(currentLine)
            del(lastline)
            del(yposition)
            return canvas
        else:
            return Response("Unable to add patient adress because is longer than 216 characters or smaller than 7", status=400)
    except:
        Response('Unknow error while adding patient Adress', status=500)

if __name__ == "__main__":
    import global_functions
    output = fill_pdf_exam_request(
        patient_name='Patient Name', 
        patient_cns=928976954930007, 
        patient_birthday=datetime.datetime.now(), 
        patient_adress="Patient Adress", 
        exams='amniocentesis, blood analysis, gastric fluid analysis, kidney function test, liver function test, lumbar puncture, malabsorption test,Pap smear.',
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