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


template_directory = "./graphql/mutations/pdfs/pdfs_templates/ficha_de_internamento_hmlem.pdf"
font_directory = "./graphql/mutations/pdfs/Roboto-Mono.ttf"

def fill_pdf_ficha_internamento(documentDatetime:datetime.datetime, patient_name:str, patient_cns:int, patient_birthday:datetime.datetime, patient_sex:str, patient_motherName:str, patient_document:dict, patient_adress:str, patient_phonenumber:int, patient_drug_allergies:str, patient_comorbidities:str, current_illness_history:str, initial_diagnostic_suspicion:str, doctor_name:str, doctor_cns:int, doctor_crm:str, patient_adressNumber:int=None, patient_adressNeigh:str=None, patient_adressCity:str=None, patient_adressUF:str=None, patient_adressCEP:int=None, patient_nationality:str=None, patient_estimateWeight:float=None, has_additional_healthInsurance:bool=None):

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
            c = global_functions.add_oneline_text(can=c, text=patient_name, pos=(27, 674), campName='Patient Name', lenMax=64, lenMin=7)
            #c = add_patientName(canvas=c, name=patient_name)
            # verify if c is a error at some point
            if type(c) == type(Response()): return c
            c = global_functions.add_cns(can=c, cns=patient_cns, pos=(393, 674), campName='Patient CNS', formated=True)
            #c = add_patientCNS(canvas=c, cns=patient_cns)
            if type(c) == type(Response()): return c

            # change font size to datetime            
            c.setFont('Roboto-Mono', 14)
            c = global_functions.add_datetime(can=c, date=documentDatetime, pos=(400, 740), campName='Document Datetime', hours=True, formated=True)
            #c = add_documentDatetime(canvas=c, docDatetime=documentDatetime)
            if type(c) == type(Response()): return c      

            c.setFont('Roboto-Mono', 9)
            c = global_functions.add_datetime(can=c, date=patient_birthday, pos=(27, 642), campName='Patient Birthday', hours=False, formated=True)
            #c = add_patientBirthday(canvas=c, birthday=patient_birthday)
            if type(c) == type(Response()): return c
            c = global_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(117, 640), pos_fem=(147, 640), campName='Patient Sex', square_size=(9,9))
            #c = add_patient_sex(canvas=c, sex=patient_sex)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_motherName, pos=(194, 642), campName='Patient Mother Name', lenMax=69, lenMin=7)
            #c = add_patientMotherName(canvas=c, motherName=patient_motherName)
            if type(c) == type(Response()): return c
            c = global_functions.add_document_cns_cpf_rg(can=c, document=patient_document, pos_square_cpf=(24, 608), pos_square_rg=(58,608), pos_rg=(92, 610), pos_cpf=(92, 610),campName='Pacient Document', formated=True)
            #c = add_patientDocument(canvas=c, document=patient_document)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adress, pos=(230, 610), campName='Patient Adress', lenMax=63, lenMin=7)
            #c = add_patientAdress(canvas=c, adress=patient_adress)
            if type(c) == type(Response()): return c
            c = global_functions.add_phonenumber(can=c, number=patient_phonenumber, pos=(173, 547), campName='Patient phone number', formated=True)
            #c = add_patientPhoneNumber(canvas=c, phonenumber=patient_phonenumber)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_drug_allergies, pos=(26, 481), campName='Patient Drugs Allergies', lenMax=100, lenMin=5)
            #c = add_patient_drug_allergies(canvas=c, drug_allergies=patient_drug_allergies)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_comorbidities, pos=(26, 449), campName='Patient Commorbidites', lenMax=100, lenMin=5)
            #c = add_patient_comorbidities(canvas=c, comorbidities=patient_comorbidities)
            if type(c) == type(Response()): return c
            c = global_functions.add_morelines_text(can=c, text=current_illness_history, initial_pos=(26, 418), decrease_ypos= 10, campName='Current Illness History', lenMax=1600, charPerLines=100, lenMin=10)
            #c = add_current_illness_history(canvas=c, current_illness_history=current_illness_history)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=initial_diagnostic_suspicion, pos=(26, 244), campName='Initial Diagnostic Suspicion', lenMax=100, lenMin=5)
            #c = add_initial_diagnostic_suspicion(canvas=c, ids=initial_diagnostic_suspicion)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=doctor_name, pos=(304, 195), campName='Doctor Name', lenMax=49, lenMin=7)
            #c = add_doctorName(canvas=c, name=doctor_name)
            if type(c) == type(Response()): return c
            c = global_functions.add_cns(can=c, cns=doctor_cns, pos=(304, 163), campName='Doctor CNS', formated=True)
            #c = add_doctorCNS(canvas=c, cns=doctor_cns)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=doctor_crm, pos=(304, 131), campName='Doctor CRM', lenMax=13, lenMin=11)
            #c = add_doctorCRM(canvas=c, crm=doctor_crm)
            if type(c) == type(Response()): return c
            
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            c = global_functions.add_oneline_intnumber(can=c, number=patient_adressNumber, pos=(24, 580), campName='Patient Adress Number', lenMax=6, lenMin=1, valueMin=0, valueMax=999999, nullable=True)
            #if patient_adressNumber is not None:
                #c = add_patient_adressNumber(canvas=c,adressNumber=patient_adressNumber)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adressNeigh, pos=(66, 580), campName='Patient Adress Neighborhood', lenMax=31, lenMin=4, nullable=True)
            #if patient_adressNeigh is not None and str(patient_adressNeigh).strip() != "":
                #c = add_patient_adressNeigh(canvas=c, adressNeigh=patient_adressNeigh)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adressCity, pos=(243, 580), campName='Patient Adress City', lenMax=34, lenMin=4, nullable=True)
            #if patient_adressCity is not None and str(patient_adressCity).strip() != "":
                #c = add_patientAdressCity(canvas=c, adressCity=patient_adressCity)
            if type(c) == type(Response()): return c
            c = global_functions.add_UF(can=c, uf=patient_adressUF, pos=(443, 580), campName='Patient Adress UF', nullable=True)
            #if patient_adressUF is not None and str(patient_adressUF).strip() != '':
                #c = add_patientAdressUF(canvas=c, adressUF=patient_adressUF)
            if type(c) == type(Response()): return c
            c = global_functions.add_CEP(can=c, cep=patient_adressCEP, pos=(483, 580), campName='Patient Adress CEP', nullable=True, formated=True)
            #if patient_adressCEP is not None:
                #c = add_patientAdressCEP(canvas=c, adressCEP=patient_adressCEP)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_nationality, pos=(27, 547), campName='Patient nationality', lenMax=25, lenMin=3, nullable=True)
            #if patient_nationality is not None and str(patient_nationality).strip() != '':
                #c = add_patientNationality(canvas=c, nationality=patient_nationality)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_floatnumber(can=c, number=patient_estimateWeight, pos=(507, 547), campName='Patient Estimate Weight', lenMax=6, lenMin=1, valueMin=0.1, valueMax=500.10, nullable=True, ndigits=2)
            #if patient_estimateWeight is not None:
                #c = add_patient_estimateWeight(canvas=c, estimateWeight=patient_estimateWeight)
            if type(c) == type(Response()): return c
            if has_additional_healthInsurance is not None:
                c = add_has_additional_healthInsurance(canvas=c, has_additional_healthInsurance=has_additional_healthInsurance)
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
            canvas = global_functions.add_data(can=canvas, data=name, pos=(27, 674))
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
            canvas = global_functions.add_data(can=canvas, data=name, pos=(304, 195))
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
            canvas = global_functions.add_data(can=canvas, data=cns, pos=(393, 674))
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
            canvas = global_functions.add_data(can=canvas, data=cns, pos=(304, 163))
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
        canvas = global_functions.add_data(can=canvas, data=crm, pos=(304, 131))
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
        docDatetime = docDatetime.strftime("%d/%m/%Y %H:%M:%S")
        canvas = global_functions.add_data(can=canvas, data=docDatetime, pos=(400, 740))
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
        birthday = birthday.strftime("%d/%m/%Y")
        canvas = global_functions.add_data(can=canvas, data=birthday, pos=(27, 642))
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
                canvas = global_functions.add_square(can=canvas, pos=(117, 640))
                return canvas
            else:
                canvas = global_functions.add_square(can=canvas, pos=(147, 640))
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
            canvas = global_functions.add_data(can=canvas, data=motherName, pos=(194, 642))
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
                canvas = global_functions.add_data(can=canvas, data=str(document['RG']), pos=(92, 610))
                canvas = global_functions.add_square(can=canvas, pos=(58, 608))
                return canvas
            else:
                return Response('Patient RG is not valid', status=400)
        elif 'CPF' in document.keys():
            #Format cpf to validate
            cpf = str(document['CPF'])
            cpf = cpf[:3] + "." + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
            if global_functions.isCPFvalid(cpf):
                canvas = global_functions.add_data(can=canvas, data=cpf, pos=(92, 610))
                canvas = global_functions.add_square(can=canvas, pos=(24, 608))
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
            canvas = global_functions.add_data(can=canvas, data=adress, pos=(230, 610))
            return canvas
        else:
            return Response("Unable to add patient adress because is longer than 63 characters or smaller than 7", status=400)
    except:
        Response('Unknow error while adding patient Adress', status=500)


def add_patientPhoneNumber(canvas:canvas.Canvas, phonenumber:int):
    """Add patient phone number to document

    Args:
        canvas (canvas.Canvas): canvas to use
        phonenumber (int): patient phone number

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(phonenumber) != type(int()):
            return Response('Phone number has to be int', status=400)
        phonenumber = str(phonenumber)
        #See if phone number has 11 digits
        if len(phonenumber) != 11:
            return Response('Patient phone number doesnt have 11 digits requiered, remeber to add DDD', status=400)
        else:
            #Format phone number
            phonenumber = '(' + phonenumber[:2] + ') ' + phonenumber[2:7] + '-' + phonenumber[7:]
            canvas = global_functions.add_data(can=canvas, data=phonenumber, pos=(173, 547))
            return canvas
    except:
        Response('Unknow error while adding patient Phone Number', status=500)


def add_patient_drug_allergies(canvas:canvas.Canvas, drug_allergies:str):
    """add patient drug allergis to document

    Args:
        canvas (canvas.Canvas): canvas to use
        drug_allergies (str): drugs allergies

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """
    try:
        #veirfy if is a str
        if type(drug_allergies)!= type(str()):
            return Response('Drug allergies has to be a str', status=400)
        #catching all drug allergies
        drug_allergies = drug_allergies.strip()
        if 5 < len(drug_allergies) <= 100:
            canvas = global_functions.add_data(can=canvas, data=drug_allergies, pos=(26, 481))
            return canvas
        else:
            return Response('Drug allergies has to be more than 5 characters and less than 100', status=400)
    except:
        return Response('Unknow error while adding patient drug alleries', status=500)


def add_patient_comorbidities(canvas:canvas.Canvas, comorbidities:str):
    """add patient comorbidities to document

    Args:
        canvas (canvas.Canvas): canvas to use
        comorbidities (str): comorbidities str

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """
    try:
        #veirfy if is a str
        if type(comorbidities)!= type(str()):
            return Response('Comorbidities has to be a str', status=400)
        if 5 < len(comorbidities) <= 100:
            canvas = global_functions.add_data(can=canvas, data=comorbidities, pos=(26, 449))
            return canvas
        else:
            return Response('patient commorbidities has to be more than 5 characters and less than 100', status=400)
    except:
        return Response('Unknow error while adding patient comorbidities', status=500)


def add_current_illness_history(canvas:canvas.Canvas, current_illness_history:str):
    """add current illness hsitory

    Args:
        canvas (canvas.Canvas): canvas to use
        current_illness_history (str): current illness history

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(current_illness_history) != type(str()):
            return Response('Current Illness History has to be a string', status=400)
        # Making the line break whem has 105 charater in a line
        current_illness_history = current_illness_history.strip()
        if len(current_illness_history) > 1600 or len(current_illness_history) < 10:
            return Response('Current illiness history has to be at least 10 characters and no more than 1600 characters', status=400)
        str_current_illness_history = ''
        brokeLinexTimes = int(len(current_illness_history)/100)
        currentLine = 100
        lastline = 0
        yposition = 418
        while brokeLinexTimes >= 0:
            str_current_illness_history = current_illness_history[lastline:currentLine]
            canvas = global_functions.add_data(can=canvas, data=str_current_illness_history, pos=(26, yposition))
            lastline = currentLine
            currentLine += 100
            brokeLinexTimes -= 1
            yposition -= 10

        del(str_current_illness_history)
        del(brokeLinexTimes)
        del(currentLine)
        del(lastline)
        del(yposition)
        return canvas
    except:
        return Response('Unknow error while adding patient current illness history', status=500)


def add_initial_diagnostic_suspicion(canvas:canvas.Canvas, ids:str):
    """add initial diagnostic suspicion

    Args:
        canvas (canvas.Canvas): canvas to add
        ids (str): ids text

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """
    try:
        if type(ids) != type(str()):
            return Response('Initial Diagnostic Suspicion has do be string', status=400)
        if 5 < len(ids) < 100:
            canvas = global_functions.add_data(can=canvas, data=ids, pos=(26, 244))
            return canvas
        return Response('inital diagnostic supicion has to be more than 5 characters and less than 100', status=400)
    except:
        return Response('Unknow error while adding initial diagnostic suspicion', status=500)


def add_patient_adressNumber(canvas:canvas.Canvas, adressNumber:int):
    """Add patient adress number to document

    Args:
        canvas (canvas.Canvas): canvas to use
        adressNumber (int): patient adres number

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(adressNumber) != type(int()):
            return Response('Patient adress Number has to be a int', status=400)
        adressNumber = str(adressNumber)
        if len(adressNumber) > 6:
            return Response('Adress Number is too long, theres be until 6 digits', status=400)
        else:
            canvas = global_functions.add_data(can=canvas, data=adressNumber, pos=(24, 580))
            return canvas
    except:
        return Response('Unknow error while adding patient Adress Number', status=500)


def add_patient_adressNeigh(canvas:canvas.Canvas, adressNeigh:str):
    """add patient adress neighborhood to document

    Args:
        canvas (canvas.Canvas): canvas to use
        adressNeigh (str): patient neighborhood

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(adressNeigh) != type(str()):
            return Response('Patient adress neighborhood has to be a str', status=400)
        if len(adressNeigh) > 31 or len(adressNeigh) < 4:
            return Response('patient neighborhood has to be at least 4 character and no more than 31 character long', status=400)
        else:
            canvas = global_functions.add_data(can=canvas, data=adressNeigh, pos=(66, 580))
            return canvas
    except:
        return Response('Unknow error while adding patient Adress neighborhood', status=500)


def add_patientAdressCity(canvas:canvas.Canvas, adressCity:str):
    """add patient adress city

    Args:
        canvas (canvas.Canvas): canvas to use
        adressCity (str): patient adress city

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(adressCity) != type(str()):
            return Response('Patient adress city has to be a str', status=400)
        if len(adressCity) > 34 or len(adressCity) < 4:
            return Response('patient city has to be more than 4 characters and less than 34', status=400)
        else:
            canvas = global_functions.add_data(can=canvas, data=adressCity, pos=(243, 580))
            return canvas
    except:
        return Response('Unknow error while adding patient Adress City', status=500)


def add_patientAdressUF(canvas:canvas.Canvas, adressUF:str):
    """Verify if the uf exists in brasil and add uf in document

    Args:
        canvas (canvas.Canvas): canvas to use
        adressUF (str): patient uf

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(adressUF) != type(str()):
            return Response('Adress UF has to be a string', status=400)
        
        adressUF = adressUF.upper()
        if global_functions.ufExists(uf=adressUF):
            canvas = global_functions.add_data(can=canvas, data=adressUF, pos=(443, 580))
            return canvas
        else:      
            return Response('Patient Adress UF not exists in Brazil', status=400) 
    except:
        return Response('Unknow error while adding patient Adress UF', status=500)


def add_patientAdressCEP(canvas:canvas.Canvas, adressCEP:int):
    """add patient CEP

    Args:
        canvas (canvas.Canvas): canvas to use
        adressCEP (int): patietn adress CEP

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(adressCEP) != type(int()):
            return Response('Patient adress CEP has to be a int', status=400)
        adressCEP = str(adressCEP)
        if len(adressCEP) != 8:
            return Response('Patient Adress CEP do not have 8 digits', status=400) 
        else:
            #format CEP
            adressCEP = adressCEP[:5] + '-' + adressCEP[5:]
            canvas = global_functions.add_data(can=canvas, data=adressCEP, pos=(483, 580))
            return canvas
    except:
        return Response('Unknow error while adding patient Adress CEP', status=500)


def add_patientNationality(canvas:canvas.Canvas, nationality:str):
    """Add patient Nationality

    Args:
        canvas (canvas.Canvas): canvas to use
        nationality (str): patient antionality

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(nationality) != type(str()):
            return Response('Patient Nationality has to be a str', status=400)
        nationality = nationality.strip()
        if len(nationality) > 25 or len(nationality) < 3:
            return Response('patient nationality has to be more than 2 characters and less than 26 characters', status=400)
        else:
            canvas = global_functions.add_data(can=canvas, data=nationality, pos=(27, 547))
            return canvas
    except:
        return Response('Unknow error while adding patient nationality', status=500)


def add_patient_estimateWeight(canvas:canvas.Canvas, estimateWeight:float):
    """Add patient estimate weight

    Args:
        canvas (canvas.Canvas): canvas to use
        estimateWeight (float): Patient estimate weight

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(estimateWeight) != type(float()) and type(estimateWeight) != type(int()):
            return Response('Patient estimate Weight has to be float or int', status=400)
        estimateWeight = str(round(float(estimateWeight), 2))
        if len(estimateWeight) > 6:
            return Response('Invalid estimate weight, is too high', status=400)
        else:
            canvas = global_functions.add_data(can=canvas, data=estimateWeight, pos=(507, 547))
            return canvas
    except:
        return Response('Unknow error while adding patient estimate weight', status=500)


def add_has_additional_healthInsurance(canvas:canvas.Canvas, has_additional_healthInsurance:bool):
    """add has additional health insurance

    Args:
        canvas (canvas.Canvas): canvas to use
        has_additional_healthInsurance (bool): status

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(has_additional_healthInsurance) != type(bool()):
            return Response('Patient has additional healthInsurance has to be bool', status=400)
        if has_additional_healthInsurance:
            canvas = global_functions.add_square(can=canvas, pos=(419, 544))
        else:
            canvas = global_functions.add_square(can=canvas, pos=(380, 544))
        return canvas
    except:
        return Response('Unknow error while adding has additional health insurance', status=500)


if __name__ == "__main__":
    import global_functions
    output = fill_pdf_ficha_internamento(
        documentDatetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CPF':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_drug_allergies='Penicillin, Aspirin, Ibuprofen, Anticonvulsants.',
        patient_comorbidities='Heart disease, High blood pressure, Diabetes, Cerebrovascular disease.',
        current_illness_history='Current illnes hsitoryaaaaaaaaaaaedqeqa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        )
    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/ficha_teste.pdf")
    