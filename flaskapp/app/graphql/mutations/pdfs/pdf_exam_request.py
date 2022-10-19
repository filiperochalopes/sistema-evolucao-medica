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
exams:str, prof_solicitor:str, solicitation_datetime:datetime.datetime,prof_authorized:str=None, autorization_datetime:datetime.datetime=None, document_pacient_date:datetime.datetime=None, document_pacient_name:str=None):

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
            pags_quant = 0
            c, pags_quant = add_exams(canvas=c, exams=exams)
            # verify if c is a error at some point
            if type(c) == type(Response()): return c

            #Add to multiple pages
            decreaseYpos = 280
            patient_name_ypos = 775
            patient_cns_ypos = 765
            patient_birthday_ypos = 784
            patient_adress_ypos = 734
            solicitation_reason_ypos = 690
            prof_solicitor_ypos = 595
            for x in range(pags_quant):
                c = global_functions.add_oneline_text(can=c, text=patient_name, pos=(7, patient_name_ypos), campName='Patient Name', lenMax=70, lenMin=7)
                if type(c) == type(Response()): return c
                c = global_functions.add_cns(can=c, cns=patient_cns, pos=(450, patient_cns_ypos), campName='Patient CNS',formated=True)
                if type(c) == type(Response()): return c
                c = global_functions.add_datetime(can=c, date=patient_birthday, pos=(441, patient_birthday_ypos), campName='Patient Birthday', hours=False, formated=True)
                if type(c) == type(Response()): return c
                c = global_functions.add_morelines_text(can=c, text=patient_adress, initial_pos=(7, patient_adress_ypos), decrease_ypos=10, campName='Patient Adress', lenMax=216, lenMin=7, charPerLines=108)
                if type(c) == type(Response()): return c
                c = global_functions.add_morelines_text(can=c, text=solicitation_reason, initial_pos=(7, solicitation_reason_ypos), decrease_ypos=10, campName='Solicitation Reason', lenMax=216, lenMin=7, charPerLines=108)
                if type(c) == type(Response()): return c
                c = global_functions.add_oneline_text(can=c, text=prof_solicitor, pos=(7, prof_solicitor_ypos), campName='Professional Solicitor Name', lenMax=29, lenMin=7)
                if type(c) == type(Response()): return c

                #Decrese ypos in all lines to complete the page
                patient_name_ypos -= decreaseYpos
                patient_cns_ypos -= decreaseYpos
                patient_birthday_ypos -= decreaseYpos
                patient_adress_ypos -= decreaseYpos
                solicitation_reason_ypos -= decreaseYpos
                prof_solicitor_ypos -= decreaseYpos

            #c = add_patientName(canvas=c, name=patient_name)
            if type(c) == type(Response()): return c
            #c = add_patient_cns(canvas=c, cns=patient_cns)
            if type(c) == type(Response()): return c
            #c = add_patient_birthday(canvas=c, birthday=patient_birthday)
            if type(c) == type(Response()): return c
            #c = add_patient_adress(canvas=c, adress=patient_adress)
            if type(c) == type(Response()): return c
            #c = add_solicitation_reason(canvas=c, reason=solicitation_reason)
            if type(c) == type(Response()): return c
            #c = add_prof_solicitor(canvas=c, prof=prof_solicitor)
            if type(c) == type(Response()): return c

        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            prof_authorized_ypos = 595
            document_pacient_name_ypos = 605
            solicitation_datetime_ypos = 572
            autorization_datetime_ypos = 572
            document_pacient_date_ypos = 572
            for x in range(pags_quant):
                c = global_functions.add_oneline_text(can=c, text=prof_authorized, pos=(174, prof_authorized_ypos), campName='Professional Authorized Name', lenMax=29, lenMin=7, nullable=True)
                if type(c) == type(Response()): return c
                c = global_functions.add_oneline_text(can=c, text=document_pacient_name, pos=(340, document_pacient_name_ypos), campName='Document Pacient Name', lenMax=46, lenMin=7, nullable=True)
                if type(c) == type(Response()): return c
                c = global_functions.add_datetime(can=c, date=solicitation_datetime, pos=(30, solicitation_datetime_ypos), campName='Solicitation Datetime', hours=False, formated=True)
                c = global_functions.add_datetime(can=c, date=autorization_datetime, pos=(195, autorization_datetime_ypos), campName='Authorization Datetime', hours=False, formated=True)
                c = global_functions.add_datetime(can=c, date=document_pacient_date, pos=(362, document_pacient_date_ypos), campName='Document Pacient Datetime', hours=False, formated=True)

                prof_authorized_ypos -= decreaseYpos
                document_pacient_name_ypos -= decreaseYpos
                solicitation_datetime_ypos -= decreaseYpos
                autorization_datetime_ypos -= decreaseYpos
                document_pacient_date_ypos -= decreaseYpos


            #if prof_authorized is not None and str(prof_authorized).strip() != "":
            #    c = add_prof_authorized(canvas=c, prof=prof_authorized)
            if type(c) == type(Response()): return c
            #if document_pacient_name is not None and str(document_pacient_name).strip() != "":
            #    c = add_document_pacient_name(canvas=c, name=document_pacient_name)
            if type(c) == type(Response()): return c
            #if solicitation_datetime is not None:
            #    c = add_solicitation_datetime(canvas=c, solicit=solicitation_datetime)
            if type(c) == type(Response()): return c
            #if autorization_datetime is not None:
            #    c = add_autorization_datetime(canvas=c, autori=autorization_datetime)
            if type(c) == type(Response()): return c
            if document_pacient_date is not None:
                c = add_document_pacient_date(canvas=c, date=document_pacient_date)
            if type(c) == type(Response()): return c

        except:
            return Response('Critical error happen when adding data that can be null to fields', status=500)

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
        name = str(name).strip()
        if 7 < len(name) <= 70:
            ypos = 775
            for x in range(pags_quant):
                canvas = global_functions.add_data(can=canvas, data=name, pos=(7, ypos))
                ypos -= 280
            return canvas
        else:
            return Response("Unable to add patient name because is longer than 70 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding patient name', status=500)


def add_prof_solicitor(canvas:canvas.Canvas, prof:str):
    """Add professional solicitator

    Args:
        canvas (canvas.Canvas): canvas to use
        prof (str): professional name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """  
    try:
        if type(prof) != type(str()):
            return Response('Professional Solicitor has to be string', status=400)
        # verify if Professional Solicitor is smaller than 29 characters
        prof = str(prof).strip()
        if 7 < len(prof) <= 29:
            ypos = 595
            for x in range(pags_quant):
                canvas = global_functions.add_data(can=canvas, data=prof, pos=(7, ypos))
                ypos -= 280
            return canvas
        else:
            return Response("Unable to add Professional Solicitor because is longer than 29 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding Professional Solicitor', status=500)


def add_prof_authorized(canvas:canvas.Canvas, prof:str):
    """Add professional authorized

    Args:
        canvas (canvas.Canvas): canvas to use
        prof (str): professional name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """  
    try:
        if type(prof) != type(str()):
            return Response('Professional Authorized has to be string', status=400)
        # verify if Professional Authorized is smaller than 29 characters
        prof = str(prof).strip()
        if 7 < len(prof) <= 29:
            ypos = 595
            for x in range(pags_quant):
                canvas = global_functions.add_data(can=canvas, data=prof, pos=(174, ypos))
                ypos -= 280
            return canvas
        else:
            return Response("Unable to add Professional Authorized because is longer than 29 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding Professional Authorized', status=500)


def add_document_pacient_name(canvas:canvas.Canvas, name:str):
    """Add document pacient name

    Args:
        canvas (canvas.Canvas): canvas to use
        name (str): document pacient name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """  
    try:
        if type(name) != type(str()):
            return Response('Document pacient name has to be string', status=400)
        # verify if Document pacient name is smaller than 29 characters
        name = str(name).strip()
        if 7 < len(name) <= 46:
            ypos = 605
            for x in range(pags_quant):
                canvas = global_functions.add_data(can=canvas, data=name, pos=(340, ypos))
                ypos -= 280
            return canvas
        else:
            return Response("Unable to add Document pacient name because is longer than 46 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding Document pacient name', status=500)


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
            return Response('Exams has to be a string', status=400), 0
        exams = exams.strip()
        if len(exams.strip()) > 972 or len(exams.strip()) < 5:
            return Response('Exams has to be at least 5 characters and no more than 972 characters', status=400), 0
        # Making the line break whem has 105 charater in a line
        str_exams = ''
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
                canvas = global_functions.add_data(can=canvas, data=str_exams, pos=(7, yposition))
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
        return Response('Unknow error while adding Solicited Exams', status=500), 0


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
                canvas = global_functions.add_data(can=canvas, data=cns, pos=(450, ypos))
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
            canvas = global_functions.add_data(can=canvas, data=birthday, pos=(441, ypos))
            ypos -= 280
        return canvas
    except:
        return Response('Unkown error while adding patient birthday', status=500)


def add_solicitation_datetime(canvas:canvas.Canvas, solicit:datetime.datetime):
    """Add solicitation datetime to document

    Args:
        canvas (canvas.Canvas): canvas to use
        solicit (datetime.datetime): solicitation_datetime

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(solicit) != type(datetime.datetime.now()):
            return Response('Solicitation datetime isnt a datetime.datetime object', status=400)
        # Format solicit to format DD/MM/YYYY
        solicit = str(solicit.day) + '/' + str(solicit.month) + '/' + str(solicit.year)
        ypos = 572
        for x in range(pags_quant):
            canvas = global_functions.add_data(can=canvas, data=solicit, pos=(30, ypos))
            ypos -= 280
        return canvas
    except:
        return Response('Unkown error while adding Solicitation datetime', status=500)


def add_autorization_datetime(canvas:canvas.Canvas, autori:datetime.datetime):
    """Add autorization_datetime to document

    Args:
        canvas (canvas.Canvas): canvas to use
        autori (datetime.datetime): autorization_datetime

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(autori) != type(datetime.datetime.now()):
            return Response('Autorization datetime isnt a datetime.datetime object', status=400)
        # Format autori to format DD/MM/YYYY
        autori = str(autori.day) + '/' + str(autori.month) + '/' + str(autori.year)
        ypos = 572
        for x in range(pags_quant):
            canvas = global_functions.add_data(can=canvas, data=autori, pos=(195, ypos))
            ypos -= 280
        return canvas
    except:
        return Response('Unkown error while adding Autorization datetime', status=500)


def add_document_pacient_date(canvas:canvas.Canvas, date:datetime.datetime):
    """add document pacient date

    Args:
        canvas (canvas.Canvas): canvas to use
        date (datetime.datetime): document pacient date

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(date) != type(datetime.datetime.now()):
            return Response('Document pacient datetime isnt a datetime.datetime object', status=400)
        # Format date to format DD/MM/YYYY
        date = str(date.day) + '/' + str(date.month) + '/' + str(date.year)
        ypos = 572
        for x in range(pags_quant):
            canvas = global_functions.add_data(can=canvas, data=date, pos=(362, ypos))
            ypos -= 280
        return canvas
    except:
        return Response('Unkown error while adding Document pacient datetime', status=500)


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
            # Making the line break whem has 108 charater in a line
            str_adress = ''
            charByLine = 108
            brokeLinexTimes = int(len(adress)/charByLine)
            currentLine = charByLine
            lastline = 0
            yposition = 734
            while brokeLinexTimes >= 0:
                str_adress = adress[lastline:currentLine]
                canvas = global_functions.add_data(can=canvas, data=str_adress, pos=(7, yposition))
                if pags_quant == 2:
                    canvas = global_functions.add_data(can=canvas, data=str_adress, pos=(7, yposition - 280))
                elif pags_quant == 3:
                    canvas = global_functions.add_data(can=canvas, data=str_adress, pos=(7, yposition - 280))
                    canvas = global_functions.add_data(can=canvas, data=str_adress, pos=(7, yposition - 560))
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


def add_solicitation_reason(canvas:canvas.Canvas, reason:str):
    """add solicitation reason

    Args:
        canvas (canvas.Canvas): canvas to use
        reason (str): reason

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(reason)!= type(str()):
            return Response('Solicitation reason has to be str', status=400)
        if 7 < len(reason) <= 216:
            # Making the line break whem has 108 charater in a line
            str_reason = ''
            charByLine = 108
            brokeLinexTimes = int(len(reason)/charByLine)
            currentLine = charByLine
            lastline = 0
            yposition = 690
            while brokeLinexTimes >= 0:
                str_reason = reason[lastline:currentLine]
                canvas = global_functions.add_data(can=canvas, data=str_reason, pos=(7, yposition))
                if pags_quant == 2:
                    canvas = global_functions.add_data(can=canvas, data=str_reason, pos=(7, yposition - 280))
                if pags_quant == 3:
                    canvas = global_functions.add_data(can=canvas, data=str_reason, pos=(7, yposition - 280))
                    canvas = global_functions.add_data(can=canvas, data=str_reason, pos=(7, yposition - 560))
                lastline = currentLine
                currentLine += charByLine
                brokeLinexTimes -= 1
                yposition -= 10

            del(str_reason)
            del(brokeLinexTimes)
            del(currentLine)
            del(lastline)
            del(yposition)
            return canvas
        else:
            return Response("Unable to add Solicitation reason because is longer than 216 characters or smaller than 7", status=400)
    except:
        Response('Unknow error while adding Solicitation reason', status=500)



if __name__ == "__main__":
    import global_functions
    output = fill_pdf_exam_request(
        patient_name='Patient Name', 
        patient_cns=928976954930007, 
        patient_birthday=datetime.datetime.now(), 
        patient_adress="Patient Adress", 
        exams=lenghtTest[:800],
        solicitation_reason="Solicitation Reason", 
        prof_solicitor="Professional Solicitor", 
        prof_authorized="Professional Authorized", 
        solicitation_datetime=datetime.datetime.now(), 
        autorization_datetime=datetime.datetime.now(), document_pacient_date=datetime.datetime.now(), 
        document_pacient_name='Document pacient name'
    )
    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/exam_request.pdf")