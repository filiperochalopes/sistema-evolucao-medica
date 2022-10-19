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
                c = global_functions.add_datetime(can=c, date=solicitation_datetime, pos=(30, solicitation_datetime_ypos), campName='Solicitation Datetime', hours=False, formated=True, nullable=True)
                if type(c) == type(Response()): return c
                c = global_functions.add_datetime(can=c, date=autorization_datetime, pos=(195, autorization_datetime_ypos), campName='Authorization Datetime', hours=False, formated=True, nullable=True)
                if type(c) == type(Response()): return c
                c = global_functions.add_datetime(can=c, date=document_pacient_date, pos=(362, document_pacient_date_ypos), campName='Document Pacient Datetime', hours=False, formated=True, nullable=True)
                if type(c) == type(Response()): return c

                prof_authorized_ypos -= decreaseYpos
                document_pacient_name_ypos -= decreaseYpos
                solicitation_datetime_ypos -= decreaseYpos
                autorization_datetime_ypos -= decreaseYpos
                document_pacient_date_ypos -= decreaseYpos

            if type(c) == type(Response()): return 

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