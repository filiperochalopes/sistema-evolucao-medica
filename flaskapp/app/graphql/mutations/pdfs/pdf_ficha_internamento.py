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
        c.setFont('Roboto-Mono', 12)

        # Writing all data in respective fields
        # not null data
        try:
            # change font size to datetime            
            c = global_functions.add_datetime(can=c, date=documentDatetime, pos=(400, 740), campName='Document Datetime', hours=True, formated=True)
            if type(c) == type(Response()): return c      
            
            
            c.setFont('Roboto-Mono', 9)
            #Normal font size
            c = global_functions.add_oneline_text(can=c, text=patient_name, pos=(27, 674), campName='Patient Name', lenMax=64, lenMin=7)
            # verify if c is a error at some point
            if type(c) == type(Response()): return c
            c = global_functions.add_cns(can=c, cns=patient_cns, pos=(393, 674), campName='Patient CNS', formated=True)
            if type(c) == type(Response()): return c


            c = global_functions.add_datetime(can=c, date=patient_birthday, pos=(27, 642), campName='Patient Birthday', hours=False, formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(117, 640), pos_fem=(147, 640), campName='Patient Sex', square_size=(9,9))
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_motherName, pos=(194, 642), campName='Patient Mother Name', lenMax=69, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_document_cns_cpf_rg(can=c, document=patient_document, pos_square_cpf=(24, 608), pos_square_rg=(58,608), pos_rg=(92, 610), pos_cpf=(92, 610),campName='Pacient Document', formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adress, pos=(230, 610), campName='Patient Adress', lenMax=63, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_phonenumber(can=c, number=patient_phonenumber, pos=(173, 547), campName='Patient phone number', formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_drug_allergies, pos=(26, 481), campName='Patient Drugs Allergies', lenMax=100, lenMin=5)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_comorbidities, pos=(26, 449), campName='Patient Commorbidites', lenMax=100, lenMin=5)
            if type(c) == type(Response()): return c
            c = global_functions.add_morelines_text(can=c, text=current_illness_history, initial_pos=(26, 418), decrease_ypos= 10, campName='Current Illness History', lenMax=1600, charPerLines=100, lenMin=10)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=initial_diagnostic_suspicion, pos=(26, 244), campName='Initial Diagnostic Suspicion', lenMax=100, lenMin=5)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=doctor_name, pos=(304, 195), campName='Doctor Name', lenMax=49, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_cns(can=c, cns=doctor_cns, pos=(304, 163), campName='Doctor CNS', formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=doctor_crm, pos=(304, 131), campName='Doctor CRM', lenMax=13, lenMin=11)
            if type(c) == type(Response()): return c
            
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            c = global_functions.add_oneline_intnumber(can=c, number=patient_adressNumber, pos=(24, 580), campName='Patient Adress Number', lenMax=6, lenMin=1, valueMin=0, valueMax=999999, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adressNeigh, pos=(66, 580), campName='Patient Adress Neighborhood', lenMax=31, lenMin=4, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adressCity, pos=(243, 580), campName='Patient Adress City', lenMax=34, lenMin=4, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_UF(can=c, uf=patient_adressUF, pos=(443, 580), campName='Patient Adress UF', nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_CEP(can=c, cep=patient_adressCEP, pos=(483, 580), campName='Patient Adress CEP', nullable=True, formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_nationality, pos=(27, 547), campName='Patient nationality', lenMax=25, lenMin=3, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_floatnumber(can=c, number=patient_estimateWeight, pos=(507, 547), campName='Patient Estimate Weight', lenMax=6, lenMin=1, valueMin=0.1, valueMax=500.10, nullable=True, ndigits=2)
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
    