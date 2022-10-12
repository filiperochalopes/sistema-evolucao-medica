import datetime
from PyPDF2  import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from flask import Response

# Doing the import this way only when is called by antoher file (like pytest)
if __name__ != "__main__":
    from . import global_functions


template_directory = "./graphql/mutations/pdfs/pdfs_templates/ficha_de_internamento_hmlem.pdf"

#REMOVE THIS AFTER TESTS
testLenght = ''
for x in range(0, 400):
    testLenght += str(x)


def fill_pdf_ficha_internamento(documentDatetime:datetime.datetime, patient_name:str, patient_cns:int, patient_birthday:datetime.datetime, patient_sex:str, patient_motherName:str, patient_document:dict, patient_adress:str, patient_phonenumber:int, patient_drug_allergies:list, patient_comorbidities:list, current_illness_history:str, initial_diagnostic_suspicion:str, patient_adressNumber:int=None, patient_adressNeigh:str=None, patient_adressCity:str=None, patient_adressUF:str=None, patient_adressCEP:int=None, patient_nationality:str=None, patient_estimateWeight:float=None, has_additional_healthInsurance:bool=None):

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
            c = add_patientName(canvas=c, name=patient_name)
            # verify if c is a error at some point
            if type(c) == type(Response()): return c
            c = add_patientCNS(canvas=c, cns=patient_cns)
            if type(c) == type(Response()): return c
            # change font size to datetime            
            c.setFont('Helvetica', 14)            
            c = add_documentDatetime(canvas=c, docDatetime=documentDatetime)
            if type(c) == type(Response()): return c            
            c.setFont('Helvetica', 9)            
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
            c = add_patientPhoneNumber(canvas=c, phonenumber=patient_phonenumber)
            if type(c) == type(Response()): return c
            c = add_patient_drug_allergies(canvas=c, drug_allergies=patient_drug_allergies)
            if type(c) == type(Response()): return c
            c = add_patient_comorbidities(canvas=c, comorbidities=patient_comorbidities)
            if type(c) == type(Response()): return c
            c = add_current_illness_history(canvas=c, current_illness_history=current_illness_history)
            if type(c) == type(Response()): return c
            c = add_initial_diagnostic_suspicion(canvas=c, ids=initial_diagnostic_suspicion)
            if type(c) == type(Response()): return c
            
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            if patient_adressNumber is not None:
                c = add_patient_adressNumber(canvas=c,adressNumber=patient_adressNumber)
            if type(c) == type(Response()): return c
            if patient_adressNeigh is not None and patient_adressNeigh.strip() != "":
                c = add_patient_adressNeigh(canvas=c, adressNeigh=patient_adressNeigh)
            if type(c) == type(Response()): return c
            if patient_adressCity is not None and patient_adressCity.strip() != "":
                c = add_patientAdressCity(canvas=c, adressCity=patient_adressCity)
            if type(c) == type(Response()): return c
            if patient_adressUF is not None and patient_adressUF.strip() != '':
                c = add_patientAdressUF(canvas=c, adressUF=patient_adressUF)
            if type(c) == type(Response()): return c
            if patient_adressCEP is not None:
                c = add_patientAdressCEP(canvas=c, adressCEP=patient_adressCEP)
            if type(c) == type(Response()): return c
            if patient_nationality is not None and patient_nationality.strip() != '':
                c = add_patientNationality(canvas=c, nationality=patient_nationality)
            if type(c) == type(Response()): return c
            if patient_estimateWeight is not None:
                c = add_patient_estimateWeight(canvas=c, estimateWeight=patient_estimateWeight)
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
        # verify if patient name is smaller than 60 characters
        name = str(name)
        if 7 < len(name.strip()) <= 60:
            canvas = add_data(canvas=canvas, data=name, pos=(27, 674))
            return canvas
        else:
            return Response("Unable to add patient name because is longer than 60 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding patient name', status=500)


def add_patientCNS(canvas:canvas.Canvas, cns:int):
    """Add patient cns to document

    Args:
        canvas (canvas.Canvas): canvas to use
        cns (int): patient cns

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        # Verify if the cns is valid
        if global_functions.isCNSvalid(cns):
            # format cns to add in document
            cns = str(cns)
            cns = cns[:3] + " " + cns[3:7] + " " + cns[7:11] + " " + cns[11:15]
            canvas = add_data(canvas=canvas, data=cns, pos=(434, 674))
            return canvas
        else:
            return Response("Unable to add patient cns because is a invalid CNS", status=400)
    except:
        return Response('Unknow error while adding patient cns', status=500)


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
        canvas = add_data(canvas=canvas, data=docDatetime, pos=(415, 741))
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
        canvas = add_data(canvas=canvas, data=birthday, pos=(43, 643))
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
        sex = sex.upper()
        if sex not in ['M', 'F']:
            return Response('Pacient sex is not valid, use F or M', status=400)
        else:
            if sex == 'M':
                canvas = add_square(canvas=canvas, pos=(117, 640))
                return canvas
            else:
                canvas = add_square(canvas=canvas, pos=(147, 640))
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
        # verify if patient motherName is smaller than 60 characters
        if 7 < len(motherName.strip()) <= 60:
            canvas = add_data(canvas=canvas, data=motherName, pos=(194, 643))
            return canvas
        else:
            return Response("Unable to add patient motherName because is longer than 60 characters or Smaller than 7", status=400)
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
        # See id document is CPF or RG
        if 'RG' in document.keys():
            #The only verificatinon is that rg is not greater than 16 characteres
            if global_functions.isRGvalid(document['RG']):
                canvas = add_data(canvas=canvas, data=str(document['RG']), pos=(92, 610))
                canvas = add_square(canvas=canvas, pos=(58, 608))
                return canvas
            else:
                return Response('Patient RG is not valid', status=400)
        elif 'CPF' in document.keys():
            #Format cpf to validate
            cpf = str(document['CPF'])
            cpf = cpf[:3] + "." + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
            if global_functions.isCPFvalid(cpf):
                canvas = add_data(canvas=canvas, data=cpf, pos=(92, 610))
                canvas = add_square(canvas=canvas, pos=(24, 608))
                return canvas
            else:
                return Response('Patient CPF is not valid', status=400)
        else:
            Response('The document was not CPF or RG', status=400)
    except:
        Response('Unknow error while adding patient Document', status=500)


def add_patientAdress(canvas:canvas.Canvas, adress:str):
    """Add patient Adress to document

    Args:
        canvas (canvas.Canvas): canvas to use
        adress (str): adress to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if len(adress) <= 60:
            canvas = add_data(canvas=canvas, data=adress, pos=(230, 610))
            return canvas
        else:
            return Response("Unable to add patient adress because is longer than 60 characters", status=400)
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
        phonenumber = str(phonenumber)
        #See if phone number has 11 digits
        if len(phonenumber) != 11:
            return Response('Patient phone number doesnt have 11 digits requiered, remeber to add DDD', status=400)
        else:
            #Format phone number
            phonenumber = '(' + phonenumber[:2] + ') ' + phonenumber[2:7] + '-' + phonenumber[7:]
            canvas = add_data(canvas=canvas, data=phonenumber, pos=(173, 547))
            return canvas
    except:
        Response('Unknow error while adding patient Phone Number', status=500)


def add_patient_drug_allergies(canvas:canvas.Canvas, drug_allergies:list):
    """add patient drug allergis to document

    Args:
        canvas (canvas.Canvas): canvas to use
        drug_allergies (list): drugs allergies

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """
    try:
        #catching all drug allergies
        str_drugsallergies = ''
        #Cont to know when use .
        cont = 0
        len_drugsAllergies = len(drug_allergies)
        for allergie in drug_allergies:
            str_drugsallergies += allergie
            cont += 1
            if cont == len_drugsAllergies:
                str_drugsallergies += '.'
            else:
                str_drugsallergies += ', '
        del(len_drugsAllergies)
        if len(str_drugsallergies) <= 105:
            canvas = add_data(canvas=canvas, data=str_drugsallergies, pos=(26, 481))
            return canvas
        else:
            return Response('So much drug allergies, the limit is 105 characters', status=400)
    except:
        return Response('Unknow error while adding patient drug alleries', status=500)


def add_patient_comorbidities(canvas:canvas.Canvas, comorbidities:list):
    """add patient comorbidities to document

    Args:
        canvas (canvas.Canvas): canvas to use
        comorbidities (list): comorbidities list

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """
    try:
        #catching all comorbidities
        str_comorbidities = ''
        #Cont to know when use .
        cont = 0
        len_comorbidities = len(comorbidities)
        for commorb in comorbidities:
            str_comorbidities += commorb
            cont += 1
            if cont == len_comorbidities:
                str_comorbidities += '.'
            else:
                str_comorbidities += ', '
        del(len_comorbidities)
        if len(str_comorbidities) <= 105:
            canvas = add_data(canvas=canvas, data=str_comorbidities, pos=(26, 449))
            return canvas
        else:
            return Response('So much comorbidities, the limit is 105 characters', status=400)
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
        # Making the line break whem has 105 charater in a line
        if len(current_illness_history) > 1680:
            return Response('Current illiness history is too big, has to been in 1680 characters', status=400)
        str_current_illness_history = ''
        brokeLinexTimes = int(len(current_illness_history)/105)
        currentLine = 105
        lastline = 0
        yposition = 417
        while brokeLinexTimes > 0:
            str_current_illness_history = current_illness_history[lastline:currentLine]
            canvas = add_data(canvas=canvas, data=str_current_illness_history, pos=(26, yposition))
            lastline = currentLine
            currentLine += 105
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
        if len(ids) < 105:
            canvas = add_data(canvas=canvas, data=ids, pos=(26, 244))
            return canvas
        return Response('inital diagnostic supicion has to be less than 105 characters', status=400)
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
        adressNumber = str(adressNumber)
        if len(adressNumber) > 6:
            return Response('Adress Number is too long, theres be until 6 digits', status=400)
        else:
            canvas = add_data(canvas=canvas, data=adressNumber, pos=(24, 580))
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
        if len(adressNeigh) > 28:
            return Response('patient neighborhood is to long, more than 28 characters', status=400)
        else:
            canvas = add_data(canvas=canvas, data=adressNeigh, pos=(66, 580))
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
        if len(adressCity) > 32:
            return Response('patient city is to long, more than 32 characters', status=400)
        else:
            canvas = add_data(canvas=canvas, data=adressCity, pos=(243, 580))
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
        ufs = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MS','MT','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
        adressUF = adressUF.upper()
        if adressUF not in ufs:
            return Response('Patient Adress UF not exists in Brazil', status=400) 
        else:
            canvas = add_data(canvas=canvas, data=adressUF, pos=(443, 580))
            return canvas
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
        adressCEP = str(adressCEP)
        if len(adressCEP) != 8:
            return Response('Patient Adress CEP do not have 8 digits', status=400) 
        else:
            #format CEP
            adressCEP = adressCEP[:5] + '-' + adressCEP[5:]
            canvas = add_data(canvas=canvas, data=adressCEP, pos=(483, 580))
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
        if len(nationality) > 22:
            return Response('patient nationality is to long, more than 22 characters', status=400)
        else:
            canvas = add_data(canvas=canvas, data=nationality, pos=(27, 547))
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
        estimateWeight = str(round(estimateWeight, 2))
        if len(estimateWeight) > 6:
            return Response('Invalid estimate weight, is too high', status=400)
        else:
            canvas = add_data(canvas=canvas, data=estimateWeight, pos=(507, 547))
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
        if has_additional_healthInsurance:
            canvas = add_square(canvas=canvas, pos=(419, 544))
        else:
            canvas = add_square(canvas=canvas, pos=(380, 544))
        return canvas
    except:
        return Response('Unknow error while adding has additional health insurance', status=500)

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


def add_square(canvas:canvas.Canvas, pos:tuple, size:int=9):
    """Add square in document using canvas object

    Args:
        canvas (canvas.Canvas): canvas to use
        pos (tuple): position to add the square
        size (int, optional): square size default is the size of the option quare. Defaults to 9.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Reponse(flask.Response: with the error)
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
        Reponse(flask.Response: with the error)
    """ 
    try:
        outputFile = open(new_directory, 'wb')
        newpdf.write(outputFile)
        outputFile.close()
    except:
        return Response("Error when writing new pdf", status=500)


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
        patient_drug_allergies=['Penicillin', 'Aspirin', 'Ibuprofen', 'Anticonvulsants'],
        patient_comorbidities=['Heart disease', 'High blood pressure', 'Diabetes', 'Cerebrovascular disease'],
        current_illness_history=str(testLenght),
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral contraceptive use.',
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
    write_newpdf(output, "./graphql/mutations/pdfs/ficha_teste.pdf")
    