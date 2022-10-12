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
for x in range(0, 500):
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
establishment_exec_name:str, establishment_exec_cnes:int, patient_name:str, patient_cns:int, patient_birthday:datetime.datetime, patient_sex:str, patient_mother_name:str, patient_adress:str, patient_adressCity:str, patient_adressCity_ibgeCode:int, patient_adressUF:str, patient_adressCEP:int, main_clinical_signs_symptoms:str, conditions_justify_hospitalization:str, exam_results:dict):
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
            c = add_patient_birthday(canvas=c, birthday=patient_birthday)
            if type(c) == type(Response()): return c
            c = add_patient_sex(canvas=c, sex=patient_sex)
            if type(c) == type(Response()): return c
            c = add_patient_mother_name(canvas=c, motherName=patient_mother_name)
            if type(c) == type(Response()): return c
            c = add_patient_adress(canvas=c, adress=patient_adress)
            if type(c) == type(Response()): return c
            c = add_patient_adressCity(canvas=c, city=patient_adressCity)
            if type(c) == type(Response()): return c
            c = add_patient_adressCity_ibgeCode(canvas=c, ibgeCode=patient_adressCity_ibgeCode)
            if type(c) == type(Response()): return c
            c = add_patient_adressUF(canvas=c, uf=patient_adressUF)
            if type(c) == type(Response()): return c
            c = add_patient_adressCEP(canvas=c, cep=patient_adressCEP)
            if type(c) == type(Response()): return c
            c = add_main_clinical_signs_symptoms(canvas=c, symptoms=main_clinical_signs_symptoms)
            if type(c) == type(Response()): return c
            c = add_conditions_justify_hospitalization(canvas=c, conditions=conditions_justify_hospitalization)
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
            canvas = add_data(canvas=canvas, data=name, pos=(25, 750))
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
            canvas = add_data(canvas=canvas, data=name, pos=(25, 726))
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
            canvas = add_data(canvas=canvas, data=name, pos=(25, 683))
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


def add_patient_birthday(canvas:canvas.Canvas, birthday:datetime.datetime):
    """add patient birthday to respective fields

    Args:
        canvas (canvas.Canvas): canvas to add
        birthday (datetime.datetime): patient birthday

    Returns:
        canvas or Response:canvas if everthing is allright or Response ifhapens some error 
    """    
    try:
        if type(birthday) != type(datetime.datetime.now()):
            return Response('Pacient birthday isnt a datetime.datetime object', status=400)
        #Add to respective fields
        day = str(birthday.day)
        month = str(birthday.month)
        year = str(birthday.year)
        canvas = add_data(canvas=canvas, data=day, pos=(312, 658))
        canvas = add_data(canvas=canvas, data=month, pos=(335, 658))
        canvas = add_data(canvas=canvas, data=year, pos=(360, 658))
        del(day)
        del(month)
        del(year)
        return canvas
    except:
        return Response('Unkown error while adding patient birthday', status=500)


def add_patient_sex(canvas:canvas.Canvas, sex:str):
    """add patient sex to document 

    Args:
        canvas (canvas.Canvas): canvas to use
        sex (str): patient sex

    Returns:
        canvas or Response:canvas if everthing is allright or Response ifhapens some error 
    """    
    try:
        sex = str(sex).upper()
        if len(sex) != 1:
            return Response('Pacient sex has to be only one character F or M', status=400)
        if sex not in ['M', 'F']:
            return Response('Pacient sex is not valid, use F or M', status=400)
        else:
            if sex == 'M':
                canvas = add_square(canvas=canvas, pos=(415, 657), size=(8, 9))
                return canvas
            else:
                canvas = add_square(canvas=canvas, pos=(468, 657), size=(8, 9))
                return canvas
    except:
        return Response('Unkown error while adding patient sex', status=500)
    

def add_patient_mother_name(canvas:canvas.Canvas, motherName:str):
    """add patient mother name

    Args:
        canvas (canvas.Canvas): canvas to use
        motherName (str): patient mother name

    Returns:
        canvas or Response:canvas if everthing is allright or Response ifhapens some error 
    """    
    try:
        if type(motherName) != type(str()):
            return Response('Mother name has to be str', status=400)
        # verify if patient motherName is smaller than 60 characters
        if 7 < len(motherName.strip()) <= 68:
            canvas = add_data(canvas=canvas, data=motherName, pos=(25, 636))
            return canvas
        else:
            return Response("Unable to add patient motherName because is longer than 68 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding patient motherName', status=500)


def add_patient_adress(canvas:canvas.Canvas, adress:str):
    """add patient adress

    Args:
        canvas (canvas.Canvas): canvas to use
        adress (str): patient adress

    Returns:
        canvas or Response:canvas if everthing is allright or Response ifhapens some error 
    """    
    try:
        if type(adress)!= type(str()):
            return Response('Adress has to be str', status=400)
        if 7 < len(adress) <= 100:
            canvas = add_data(canvas=canvas, data=adress, pos=(25, 593))
            return canvas
        else:
            return Response("Unable to add patient adress because is longer than 100 characters or smaller than 7", status=400)
    except:
        Response('Unknow error while adding patient Adress', status=500)


def add_patient_adressCity(canvas:canvas.Canvas, city:str):
    """add pacient adress City

    Args:
        canvas (canvas.Canvas): canvas to use
        city (str): pactient city

    Returns:
        canvas or Response:canvas if everthing is allright or Response ifhapens some error 
    """    
    try:
        if type(city) != type(str()):
            return Response('Patient adress city has to be a str', status=400)
        if 7 < len(city) > 59:
            return Response('Unable to add patient city is longer than 59 characters or smaller than 7', status=400)
        else:
            canvas = add_data(canvas=canvas, data=city, pos=(25, 566))
            return canvas
    except:
        return Response('Unknow error while adding patient Adress City', status=500)


def add_patient_adressCity_ibgeCode(canvas:canvas.Canvas, ibgeCode:int):
    """aadd patient adress city ibge code

    Args:
        canvas (canvas.Canvas): canvas to use
        ibgeCode (int): ibge cpde

    Returns:
        canvas or Response:canvas if everthing is allright or Response ifhapens some error 
    """    
    try:
        if type(ibgeCode) != type(int()):
            return Response('Patient adress city Igbe code has to be a int', status=400)
        ibgeCode = str(ibgeCode)
        if len(ibgeCode) != 7:
            return Response('Patient adress city Igbe code do not have 7 digits', status=400) 
        else:
            canvas = add_data(canvas=canvas, data=ibgeCode, pos=(388, 566))
            return canvas
    except:
        return Response('Unknow error while adding Patient adress city Igbe code', status=500)


def add_patient_adressUF(canvas:canvas.Canvas, uf:str):
    """add patient adres Uf to document

    Args:
        canvas (canvas.Canvas): canvas to use
        uf (str): uf to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response ifhapens some error 
    """    
    try:
        if type(uf) != type(str()):
            return Response('Adress UF has to be a string', status=400)
        uf = uf.upper()
        if global_functions.ufExists(uf=uf):
            canvas = add_data(canvas=canvas, data=uf[0], pos=(450, 566))
            canvas = add_data(canvas=canvas, data=uf[1], pos=(464, 566))
            return canvas
        else:
            return Response('Patient Adress UF not exists in Brazil', status=400) 
    except:
        return Response('Unknow error while adding patient Adress UF', status=500)


def add_patient_adressCEP(canvas:canvas.Canvas, cep:int):
    """add patient cep to document

    Args:
        canvas (canvas.Canvas): canvas to use
        cep (int): cep to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response ifhapens some error 
    """    
    try:
        if type(cep) != type(int()):
            return Response('Patient adress CEP has to be a int', status=400)
        cep = str(cep)
        if len(cep) != 8:
            return Response('Patient Adress CEP do not have 8 digits', status=400) 
        else:
            cont = 0
            xpos = 481
            while cont <= 7:
                canvas = add_data(canvas=canvas, data=cep[cont], pos=(xpos, 566))
                cont += 1
                xpos += 12
            return canvas
    except:
        return Response('Unknow error while adding patient Adress CEP', status=500)


def add_main_clinical_signs_symptoms(canvas:canvas.Canvas, symptoms:str):
    """Add Main clinical signs symptoms to document

    Args:
        canvas (canvas.Canvas): canvas to use
        symptoms (str): all symphtoms

    Returns:
        canvas or Response:canvas if everthing is allright or Response ifhapens some error 
    """    
    try:
        if type(symptoms) != type(str()):
            return Response('Clinical Signs Symptoms has to be a string', status=400)
        if len(symptoms) > 1060:
            return Response('Clinical Signs Symptoms is too big, has to been in 1060 characters', status=400)
        str_symptoms = ''
        brokeLinexTimes = int(len(symptoms)/107)
        currentLine = 107
        lastline = 0
        yposition = 530
        # Making the line break whem has 107 charater in a line
        while brokeLinexTimes >= 0:
            str_symptoms = symptoms[lastline:currentLine]
            canvas = add_data(canvas=canvas, data=str_symptoms, pos=(25, yposition))
            lastline = currentLine
            currentLine += 107
            brokeLinexTimes -= 1
            yposition -= 10

        del(str_symptoms)
        del(brokeLinexTimes)
        del(currentLine)
        del(lastline)
        del(yposition)
        return canvas
    except:
        return Response('Unknow error while adding patient Clinical Signs Symptoms', status=500)


def add_conditions_justify_hospitalization(canvas:canvas.Canvas, conditions:str):
    """Add contitionis to justify hospitalizaion in documents

    Args:
        canvas (canvas.Canvas): canvas to use
        conditions (str): conditions to justify

    Returns:
        canvas or Response:canvas if everthing is allright or Response ifhapens some error 
    """    
    try:
        if type(conditions) != type(str()):
            return Response('Conditions to Justify Hospitalization has to be a string', status=400)
        if len(conditions) > 425:
            return Response('Conditions to Justify Hospitalization is too big, has to been in 425 characters', status=400)
        str_conditions = ''
        brokeLinexTimes = int(len(conditions)/107)
        currentLine = 107
        lastline = 0
        yposition = 422
        # Making the line break whem has 107 charater in a line
        while brokeLinexTimes >= 0:
            str_conditions = conditions[lastline:currentLine]
            canvas = add_data(canvas=canvas, data=str_conditions, pos=(25, yposition))
            lastline = currentLine
            currentLine += 107
            brokeLinexTimes -= 1
            yposition -= 10

        del(str_conditions)
        del(brokeLinexTimes)
        del(currentLine)
        del(lastline)
        del(yposition)
        return canvas
    except:
        return Response('Unknow error while adding patient Conditions to Justify Hospitalization', status=500)


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


def add_square(canvas:canvas.Canvas, pos:tuple, size:tuple=(9, 9)):
    """Add square in document using canvas object

    Args:
        canvas (canvas.Canvas): canvas to use
        pos (tuple): position to add the square
        size (tuple, optional): square size default is the size of the option quare. Defaults to 9.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response: with the error)
    """    
    try:
        canvas.rect(x=pos[0], y=pos[1], width=size[0], height=size[1], fill=1)
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
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_mother_name='Patient Mother Name',
        patient_adress='Patient Adress street neighobourd',
        patient_adressCity='Patient City',
        patient_adressCity_ibgeCode=1234567,
        patient_adressUF='SP',
        patient_adressCEP=12345678,
        main_clinical_signs_symptoms="Patient main clinical signs sysmpthoms",
        conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',
        exam_results={'Xray':'Tibia Broken'}
    )
    if type(output) == type(Response()): 
        print(output.response)
    write_newpdf(output, "./graphql/mutations/pdfs/aih_sus_teste.pdf")