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

def fill_pdf_prescricao_medica(document_datetime:datetime.datetime, patient_name:str, prescription:list):

    try:
        try:
            packet = io.BytesIO()
            # Create canvas and add data
            c = canvas.Canvas(packet, pagesize=pagesizePoints)
            # Change canvas font to mach with the document
            # this is also changed in the document to some especific fields
            pdfmetrics.registerFont(TTFont('Roboto-Mono', font_directory))
            c.setFont('Roboto-Mono', 12)
            # Writing all data in respective fields
            # not null data
            initial_dateXpos = 294
            initial_nameXpos = 120
            for x in range(0, 2):
                c = global_functions.add_datetime(can=c, date=document_datetime, pos=(initial_dateXpos, 38), campName='Document Datetime', hours=False, interval='  ', formated=False)
                c = global_functions.add_oneline_text(can=c, text=patient_name, pos=(initial_nameXpos, 505), campName='Patient Name', lenMax=34, lenMin=7)
                initial_dateXpos += 450
                initial_nameXpos += 450

            #c = add_document_datetime(canvas=c, date=document_datetime)
            if type(c) == type(Response()): return c
            #c = add_patient_name(canvas=c, name=patient_name)
            if type(c) == type(Response()): return c
            c.setFont('Roboto-Mono', 10)
            c = add_prescription(canvas=c, prescription=prescription)
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
        return Response('Unknow error while adding medical prescription', status=500)


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
            canvas = global_functions.add_data(can=canvas, data=name, pos=(120, 505))
            canvas = global_functions.add_data(can=canvas, data=name, pos=(571, 505))
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
        canvas = global_functions.add_data(can=canvas, data=date, pos=(294, 38))
        canvas = global_functions.add_data(can=canvas, data=date, pos=(744, 38))
        return canvas
    except:
        return Response('Unkown error while adding document datetime', status=500)


def add_prescription(canvas:canvas.Canvas, prescription:list):
    """add prescription to database

    Args:
        canvas (canvas.Canvas): canvas to use
        precription (list): list of dicts
    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    #verify if the type is list
    if type(prescription) != type(list()):
        return Response('prescription has to be a list of dicts, like: [{"medicine_name":"Dipirona 500mg", "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}, {"medicine_name":"Metocoplamina 10mg", "amount":"6 comprimidos", "use_mode":"1 comprimido, via oral, de 8/8h por 2 dias"}]', status=400)
    necessaryKeys = ["medicine_name", "amount", "use_mode"]
    totalChar = 0
    for presc in prescription:
        #verify if the item in list is a dict
        if type(presc) != type(dict()):
            return Response('All itens in list has to be a dict', status=400)
        #Verify if the necessary keys are in the dict
        if 'medicine_name' not in presc.keys() or 'amount' not in presc.keys() or "use_mode" not in presc.keys():
            return Response('Some keys in dict is missing, dict has to have "medicine_name", "amount", "use_mode"', status=400)
        #Verify if the value in the dics is str
        elif type(presc['medicine_name']) != type(str()) or type(presc['amount']) != type(str()) or type(presc["use_mode"]) != type(str()):
            return Response('The values in the keys "medicine_name", "amount", "use_mode" has to be string', status=400)
        #verify if medicine_name and amount together isnt bigger than 1 line (61 characters)
        elif len(presc['medicine_name'].strip() + presc['amount'].strip()) > 61:
            return Response('"medicine_name" and "amount" cannot be longer than 61 characters', status=400)
        #Verify id use_mode isnt bigger than 3 lines (244 characters)
        elif len(presc['use_mode'].strip()) > 244:
            return Response('"use_mode"cannot be longer than 244 characters', status=400)
        #Verify if the dict has more keys than the needed
        for key in presc.keys():
            if key not in necessaryKeys:
                return Response('The dict can only have 3 keys "medicine_name", "amount", "use_mode"', status=400)
        #calculate the total lenght of use_mode
        totalChar += len(presc['use_mode'].strip())
    # Verify if user_mode total lenght and the 2 line that every medicine and amount need isnt bigger than the total of de document
    if totalChar + (61 * len(prescription)) == 2623:
        return Response('The total document cannot has more than 2623 characters.Remember than 1 line (61 character) is just to medidine and amount', status=400)

    yposition = 475
    for presc in prescription:
        medicine_name = presc['medicine_name'].strip()
        amount = presc['amount'].strip()
        use_mode = presc['use_mode'].strip()
        str_use_mode = ''
        charByLine = 61
        brokeLinexTimes = int(len(use_mode)/charByLine)
        currentLine = charByLine
        lastline = 0
        #Discover how many . dots hhas to be between medicinename and amount
        dotQuant = 61 - len(medicine_name + amount)
        str_title = medicine_name + '.' * dotQuant + amount
        #Add medicinename and amount
        canvas = global_functions.add_data(can=canvas, data=str_title, pos=(22, yposition))
        canvas = global_functions.add_data(can=canvas, data=str_title, pos=(472, yposition))
        yposition -= 10
        # Making the line break whem has 61 charater in a line
        while brokeLinexTimes >= 0:
            str_use_mode = use_mode[lastline:currentLine]
            canvas = global_functions.add_data(can=canvas, data=str_use_mode, pos=(22, yposition))
            canvas = global_functions.add_data(can=canvas, data=str_use_mode, pos=(472, yposition))
            lastline = currentLine
            currentLine += charByLine
            brokeLinexTimes -= 1
            yposition -= 10
        yposition -= 10

    del(str_use_mode)
    del(brokeLinexTimes)
    del(currentLine)
    del(lastline)
    del(yposition)
    return canvas


if __name__ == "__main__":
    import global_functions
    output = fill_pdf_prescricao_medica(
        document_datetime=datetime.datetime.now(),
        patient_name='Pacient Name',
        prescription=[{"medicine_name":"Dipirona 500mg", "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}, {"medicine_name":"Metocoplamina 10mg", "amount":"6 comprimidos", "use_mode":"1 comprimido, via oral, de 8/8h por 2 dias"}]
    )

    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/prescricao_medica_teste.pdf")