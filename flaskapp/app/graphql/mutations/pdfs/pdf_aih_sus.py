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

template_directory = "./graphql/mutations/pdfs/pdfs_templates/aih_sus.pdf"
font_directory = "./graphql/mutations/pdfs/Roboto-Mono.ttf"

def fill_pdf_aih_sus(establishment_solitc_name:str, establishment_solitc_cnes:int, establishment_exec_name:str, establishment_exec_cnes:int, patient_name:str, patient_cns:int, patient_birthday:datetime.datetime, patient_sex:str, patient_mother_name:str, patient_adress:str, patient_adressCity:str, patient_adressCity_ibgeCode:int, patient_adressUF:str, patient_adressCEP:int, main_clinical_signs_symptoms:str, conditions_justify_hospitalization:str, initial_diagnostic:str, principalCid10:str, procedure_solicited:str, procedure_code:str, clinic:str, internation_carater:str, prof_solicitor_document:dict, prof_solicitor_name:str, solicitation_datetime:datetime.datetime, autorization_prof_name:str, emission_org_code:str, autorizaton_prof_document:dict, autorizaton_datetime:datetime.datetime, hospitalization_autorization_number:int ,exam_results:str=None, chart_number:int=None, patient_ethnicity:str=None, patient_responsible_name:str=None, patient_mother_phonenumber:int=None, patient_responsible_phonenumber:int=None, secondary_cid10:str=None, cid10_associated_causes:str=None, acident_type:str=None, insurance_company_cnpj:int=None, insurance_company_ticket_number:int=None, insurance_company_series:str=None,company_cnpj:int=None, company_cnae:int=None, company_cbor:int=None, pension_status:str=None):
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
            c = global_functions.add_oneline_text(can=c, text=establishment_solitc_name, pos=(25, 750), campName='Establishment Solicit Name', lenMax=82, lenMin=8)
            if type(c) == type(Response()): return c
            #c = add_establishment_solitc_name(canvas=c, name=establishment_solitc_name)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=establishment_solitc_cnes, pos=(470, 750), campName='Establishment Solict CNES', lenMax=7, lenMin=7,valueMin=0, valueMax=99999999, interval='  ')
            #c = add_establishment_solitc_cnes(canvas=c, cnes=establishment_solitc_cnes)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=establishment_exec_name, pos=(25, 726), campName='Establishment Exec Name', lenMax=82, lenMin=8)
            #c = add_establishment_exec_name(canvas=c, name=establishment_exec_name)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=establishment_exec_cnes, pos=(470, 726), campName='Establishment Exec CNES', lenMax=7, lenMin=7,valueMin=0, valueMax=99999999, interval='  ')
            #c = add_establishment_exec_cnes(canvas=c, cnes=establishment_exec_cnes)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_name, pos=(25, 683), campName='Patient Name', lenMax=79, lenMin=7)
            #c = add_patient_name(canvas=c, name=patient_name)
            if type(c) == type(Response()): return c
            #Data that change Font Size

            c.setFont('Roboto-Mono', 10)
            c = global_functions.add_cns(can=c, cns=patient_cns, pos=(28, 658), campName='Patient CNS', interval='  ')
            #c = add_patient_cns(canvas=c, cns=patient_cns)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_adressCEP, pos=(482, 566), campName='Patient Adress CEP', lenMax=8, lenMin=8, valueMin=0, valueMax=99999999, nullable=True, interval=' ')
            #c = add_patient_adressCEP(canvas=c, cep=patient_adressCEP)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=procedure_code, pos=(404, 269), campName='Procedure Code', lenMax=10, lenMin=10, interval='  ')
            #c = add_procedure_code(canvas=c, code=procedure_code)
            if type(c) == type(Response()): return c
            
            c.setFont('Roboto-Mono', 9)
            c = global_functions.add_datetime(can=c, date=patient_birthday, pos=(312, 658), campName='Patient Birthday', hours=False, interval='  ', formated=False)
            #c = add_patient_birthday(canvas=c, birthday=patient_birthday)
            if type(c) == type(Response()): return c
            c = global_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(415, 657), pos_fem=(468, 657), campName='Patient Sex', square_size=(8,9))
            #c = add_patient_sex(canvas=c, sex=patient_sex)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(25, 636), campName='Patient Mother Name', lenMax=70, lenMin=7)
            #c = add_patient_mother_name(canvas=c, motherName=patient_mother_name)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adress, pos=(25, 593), campName='Patient Adress', lenMax=101, lenMin=7)
            #c = add_patient_adress(canvas=c, adress=patient_adress)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adressCity, pos=(25, 566), campName='Patient Adress City', lenMax=58, lenMin=7)
            #c = add_patient_adressCity(canvas=c, city=patient_adressCity)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_adressCity_ibgeCode, pos=(388, 566), campName='Patient Adress City IBGE code', lenMax=7, lenMin=7, valueMin=0, valueMax=9999999)
            #c = add_patient_adressCity_ibgeCode(canvas=c, ibgeCode=patient_adressCity_ibgeCode)
            if type(c) == type(Response()): return c
            c = global_functions.add_UF(can=c, uf=patient_adressUF, pos=(450, 566), campName='Patient Adress UF', interval='  ')
            #c = add_patient_adressUF(canvas=c, uf=patient_adressUF)
            if type(c) == type(Response()): return c
            c = global_functions.add_morelines_text(can=c, text=main_clinical_signs_symptoms, initial_pos=(25, 530), decrease_ypos= 10, campName='Main Clinical Signs Symptoms', lenMax=1009, charPerLines=101, lenMin=5)
            #c = add_main_clinical_signs_symptoms(canvas=c, symptoms=main_clinical_signs_symptoms)
            if type(c) == type(Response()): return c
            c = global_functions.add_morelines_text(can=c, text=conditions_justify_hospitalization, initial_pos=(25, 422), decrease_ypos= 10, campName='Conditions that Justify hospitalization', lenMax=403, charPerLines=101, lenMin=5)
            #c = add_conditions_justify_hospitalization(canvas=c, conditions=conditions_justify_hospitalization)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=initial_diagnostic, pos=(25, 314), campName='Initial Diagnostic', lenMax=44, lenMin=5)
            #c = add_initial_diagnostic(canvas=c, diagnostic=initial_diagnostic)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=principalCid10, pos=(306, 314), campName='Principal Cid10', lenMax=4, lenMin=3)
            #c = add_principalCid10(canvas=c, cid10=principalCid10)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=procedure_solicited, pos=(25, 269), campName='Procedure Solicited', lenMax=65, lenMin=6)
            #c = add_procedure_solicited(canvas=c, procedure=procedure_solicited)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=clinic, pos=(25, 246), campName='Clinic', lenMax=18, lenMin=6)
            #c = add_clinic(canvas=c, name=clinic)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=internation_carater, pos=(128, 246), campName='Internation Caracter', lenMax=19, lenMin=6)
            #c = add_internation_carater(canvas=c, carater=internation_carater)
            if type(c) == type(Response()): return c
            c = global_functions.add_document_cns_cpf_rg(can=c, document=prof_solicitor_document, pos_square_cpf=(290, 244), pos_square_cns=(247,244), pos_cns=(335, 246), pos_cpf=(335, 246),campName='Professional Solicitor Document', interval='  ',nullable=True)
            #c = add_prof_solicitor_document(canvas=c, document=prof_solicitor_document)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=prof_solicitor_name, pos=(25, 222), campName='Professional Solicitor Name', lenMax=48, lenMin=8)
            #c = add_prof_solicitor_name(canvas=c, name=prof_solicitor_name)
            if type(c) == type(Response()): return c
            c = global_functions.add_datetime(can=c, date=solicitation_datetime, pos=(300, 222), campName='Solicitation Datetime', hours=False, interval='  ', formated=False)
            #c = add_solicitation_datetime(canvas=c, solitDate=solicitation_datetime)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=autorization_prof_name, pos=(25, 93), campName='Professional Authorizator Name', lenMax=48, lenMin=8)
            #c = add_autorization_prof_name(canvas=c, name=autorization_prof_name)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=emission_org_code, pos=(292, 93), campName='Emission Organization Code', lenMax=17, lenMin=2)
            #c = add_emission_org_code(canvas=c, code=emission_org_code)
            if type(c) == type(Response()): return c
            c = global_functions.add_document_cns_cpf_rg(can=c, document=autorizaton_prof_document, pos_square_cpf=(95, 66), pos_square_cns=(41,66), pos_cns=(146, 66), pos_cpf=(146, 66),campName='Professional Authorizator Document', interval='  ')
            #c = add_autorizaton_prof_document(canvas=c, document=autorizaton_prof_document)
            if type(c) == type(Response()): return c
            c = global_functions.add_datetime(can=c, date=autorizaton_datetime, pos=(30, 30), campName='Authorization Datetime', hours=False, interval='  ', formated=False)
            #c = add_autorizaton_datetime(canvas=c, authDate=autorizaton_datetime)
            if type(c) == type(Response()): return c
            c.setFont('Roboto-Mono', 16)       
            c = global_functions.add_oneline_intnumber(can=c, number=hospitalization_autorization_number, pos=(480, 66), campName='Hospitalization autorization Number', lenMax=18, lenMin=1, valueMin=0, valueMax=999999999999999999, centralized=True)
            #c = add_hospitalization_autorization_number(canvas=c, number=hospitalization_autorization_number)
            if type(c) == type(Response()): return c
            c.setFont('Roboto-Mono', 9)       

            
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            c = global_functions.add_morelines_text(can=c, text=exam_results, initial_pos=(25, 362), decrease_ypos= 10, campName='Exam Results', lenMax=403, charPerLines=101, lenMin=5, nullable=True)
            #if exam_results is not None and str(exam_results).strip() != "":
            #    c = add_exam_results(canvas=c, results=exam_results)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=chart_number, pos=(466, 683), campName='Chart Number', lenMax=20, lenMin=1, valueMin=0, valueMax=99999999999999999999, nullable=True)
            #if chart_number is not None:
            #    c = add_chart_number(canvas=c, number=chart_number)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_ethnicity, pos=(510, 658), campName='Patient Ehinicity', lenMax=11, lenMin=4, nullable=True)
            #if patient_ethnicity is not None and str(patient_ethnicity).strip() != "":
            #    c = add_patient_ethnicity(canvas=c, ethnicity=patient_ethnicity)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_responsible_name, pos=(25, 612), campName='Patient Responsible Name', lenMax=70, lenMin=7, nullable=True)
            #if patient_responsible_name is not None and str(patient_responsible_name).strip() != "":
            #    c = add_patient_responsible_name(canvas=c, name=patient_responsible_name)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_mother_phonenumber, pos=(415, 631), campName='Patient Mother phone number', lenMax=10, lenMin=10, valueMin=1111111111, valueMax=9999999999, nullable=True, interval='  ')
            #if patient_mother_phonenumber is not None:
            #    c = add_patient_mother_phonenumber(canvas=c, number=patient_mother_phonenumber)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_responsible_phonenumber, pos=(415, 608), campName='Patient responsible phone number', lenMax=10, lenMin=10, valueMin=1111111111, valueMax=9999999999, nullable=True, interval='  ')
            #if patient_responsible_phonenumber is not None:
            #    c = add_patient_responsible_phonenumber(canvas=c, number=patient_responsible_phonenumber)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=secondary_cid10, pos=(406, 314), campName='Secondary Cid10', lenMax=4, lenMin=3, nullable=True)
            #if secondary_cid10 is not None and str(secondary_cid10).strip() != "":
            #    c = add_secondary_cid10(canvas=c, cid10=secondary_cid10)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=cid10_associated_causes, pos=(512, 314), campName='Associated causes Cid10', lenMax=4, lenMin=3, nullable=True)
            #if cid10_associated_causes is not None and str(cid10_associated_causes).strip() != "":
            #    c = add_cid10_associated_causes(canvas=c, cid10=cid10_associated_causes)
            if type(c) == type(Response()): return c
###############################################################################
            if acident_type is not None and str(acident_type).strip() != "":
                c = add_acident_type(canvas=c, acident=acident_type)
            if type(c) == type(Response()): return c
#######################################################################
            #Data that change Font Size
            c.setFont('Roboto-Mono', 10)
            c = global_functions.add_cnpj(can=c, cnpj=insurance_company_cnpj, pos=(168,183), campName='Insurance Company CNPJ', nullable=True, interval='  ')
            #if insurance_company_cnpj is not None:
            #    c = add_insurance_company_cnpj(canvas=c, cnpj=insurance_company_cnpj)
            if type(c) == type(Response()): return c
            c = global_functions.add_cnpj(can=c, cnpj=company_cnpj, pos=(168,156), campName='Company CNPJ', nullable=True, interval='  ')
            #if company_cnpj is not None:
            #    c = add_company_cnpj(canvas=c, cnpj=company_cnpj)
            if type(c) == type(Response()): return c
            
            
            c.setFont('Roboto-Mono', 9)
            c = global_functions.add_oneline_intnumber(can=c, number=insurance_company_ticket_number, pos=(465, 183), campName='Insurance company ticket number', lenMax=16, lenMin=1, valueMin=0, valueMax=9999999999999999, nullable=True, centralized=True)
            #if insurance_company_ticket_number is not None:
            #    c = add_insurance_company_ticket_number(canvas=c, ticket=insurance_company_ticket_number)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=insurance_company_series, pos=(543, 183), campName='Insurance Company Series', lenMax=10, lenMin=1, nullable=True, centralized=True)

            #if insurance_company_series is not None and str(insurance_company_series).strip() != "":
            #    c = add_insurance_company_series(canvas=c, series=insurance_company_series)
            if type(c) == type(Response()): return c
            c = global_functions.add_cnae(can=c, cnae=company_cnae, pos=(434, 156), campName='Company CNAE', nullable=True, formated=True)
            #if company_cnae is not None:
            #    c = add_company_cnae(canvas=c, cnae=company_cnae)
            if type(c) == type(Response()): return c
            c = global_functions.add_cbor(can=c, cbor=company_cbor, pos=(529, 156), campName='Company CBOR', nullable=True, formated=True)
            #if company_cbor is not None :
            #    c = add_company_cbor(canvas=c, cbo=company_cbor)
            if type(c) == type(Response()): return c
            if pension_status is not None and str(pension_status).strip() != "":
                c = add_pension_status(canvas=c, status=pension_status)
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
        return Response("Error while filling aih sus", status=500)


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
        if 7 < len(name.strip()) <= 82:
            canvas = global_functions.add_data(can=canvas, data=name, pos=(25, 750))
            return canvas
        else:
            return Response("Unable to add Solicitate Establishment name because is longer than 82 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding Solicitate Establishment  name', status=500)


def add_patient_ethnicity(canvas:canvas.Canvas, ethnicity:str):
    """add patient ethnicity

    Args:
        canvas (canvas.Canvas): canvas to use
        ethnicity (str): paien ethnicity

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(ethnicity) != type(str()):
            return Response('Patient ethnicity has to be string', status=400)
        # verify if Patient ethnicity is smaller than 60 characters
        ethnicity = str(ethnicity)
        if 4 < len(ethnicity.strip()) <= 11:
            canvas = global_functions.add_data(can=canvas, data=ethnicity, pos=(510, 658))
            return canvas
        else:
            return Response("Unable to add Patient ethnicity because is longer than 11 characters or Smaller than 5", status=400)
    except:
        return Response('Unknow error while adding Patient ethnicity', status=500)


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
            # Add empty spaces interval between averu character
            interval = ' ' * 2
            cnes = interval.join(cnes)
            canvas = global_functions.add_data(can=canvas, data=cnes, pos=(470, 750))
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
        if 7 < len(name.strip()) <= 82:
            canvas = global_functions.add_data(can=canvas, data=name, pos=(25, 726))
            return canvas
        else:
            return Response("Unable to add Exec Establishment name because is longer than 82 characters or Smaller than 7", status=400)
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
            # Add empty spaces interval between averu character
            interval = ' ' * 2
            cnes = interval.join(cnes)
            canvas = global_functions.add_data(can=canvas, data=cnes, pos=(470, 726))
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
        if 7 < len(name.strip()) <= 79:
            canvas = global_functions.add_data(can=canvas, data=name, pos=(25, 683))
            return canvas
        else:
            return Response("Unable to add patient name because is longer than 79 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding patient name', status=500)


def add_prof_solicitor_name(canvas:canvas.Canvas, name:str):
    """add professional solicitor name

    Args:
        canvas (canvas.Canvas): canvas to use
        name (str): professional solicitor name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(name) != type(str()):
            return Response('Professional solitic name has to be string', status=400)
        # verify if Professional solitic name is smaller than 49 characters
        name = str(name)
        if 7 < len(name.strip()) <= 48:
            canvas = global_functions.add_data(can=canvas, data=name, pos=(25, 222))
            return canvas
        else:
            return Response("Unable to add Professional solitic name because is longer than 48 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding Professional solitic name', status=500)


def add_autorization_prof_name(canvas:canvas.Canvas, name:str):
    """add autorizaton professional name

    Args:
        canvas (canvas.Canvas): canvas to use
        name (str): professional autorization name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(name) != type(str()):
            return Response('Professional autorizator name has to be string', status=400)
        # verify if Professional autorizator name is smaller than 49 characters
        name = str(name)
        if 7 < len(name.strip()) <= 48:
            canvas = global_functions.add_data(can=canvas, data=name, pos=(25, 93))
            return canvas
        else:
            return Response("Unable to add Professional autorizator name because is longer than 48 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding Professional autorizator name', status=500)

def add_patient_cns(canvas:canvas.Canvas, cns:int):
    """add patient cns to every block

    Args:
        canvas (canvas.Canvas): canvas to use
        cns (int): cns to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 

    """    
    try:
        if type(cns) != type(int()):
            return Response('patient CNS has to be int', status=400)
        # Verify if the cns is valid
        if global_functions.isCNSvalid(cns):
            #Add one number at every field
            cns = str(cns)
            # Add empty spaces interval between averu character
            interval = ' '  * 2
            cns = interval.join(cns)
            canvas = global_functions.add_data(can=canvas, data=cns, pos=(28, 658))

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
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(birthday) != type(datetime.datetime.now()):
            return Response('Pacient birthday isnt a datetime.datetime object', status=400)
        #Add to respective fields
        date = str(birthday.day) + '.' + str(birthday.month) + '.' + str(birthday.year)
        interval = ' ' * 2
        date = date.replace('.', interval)
        canvas = global_functions.add_data(can=canvas, data=date, pos=(312, 658))
        return canvas
    except:
        return Response('Unkown error while adding patient birthday', status=500)


def add_solicitation_datetime(canvas:canvas.Canvas, solitDate:datetime.datetime):
    """Add solititation date to document

    Args:
        canvas (canvas.Canvas): canvas to use
        solitDate (datetime.datetime): solicitation datetime

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(solitDate) != type(datetime.datetime.now()):
            return Response('solitication date isnt a datetime.datetime object', status=400)
        #Add to respective fields
        date = str(solitDate.day) + '.' + str(solitDate.month) + '.' + str(solitDate.year)
        interval = ' ' * 2
        date = date.replace('.', interval)
        canvas = global_functions.add_data(can=canvas, data=date, pos=(300, 222))
        return canvas
    except:
        return Response('Unkown error while adding solitication date', status=500)


def add_autorizaton_datetime(canvas:canvas.Canvas, authDate:datetime.datetime):
    """add atuorizaton date to document

    Args:
        canvas (canvas.Canvas): canvas to use
        authDate (datetime.datetime): datetime object

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(authDate) != type(datetime.datetime.now()):
            return Response('autorization date isnt a datetime.datetime object', status=400)
        #Add to respective fields
        date = str(authDate.day) + '.' + str(authDate.month) + '.' + str(authDate.year)
        interval = ' ' * 2
        date = date.replace('.', interval)
        canvas = global_functions.add_data(can=canvas, data=date, pos=(30, 30))
        return canvas
    except:
        return Response('Unkown error while adding autorization date', status=500)


def add_patient_sex(canvas:canvas.Canvas, sex:str):
    """add patient sex to document 

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
                canvas = global_functions.add_square(can=canvas, pos=(415, 657), size=(8, 9))
                return canvas
            else:
                canvas = global_functions.add_square(can=canvas, pos=(468, 657), size=(8, 9))
                return canvas
    except:
        return Response('Unkown error while adding patient sex', status=500)
    

def add_patient_mother_name(canvas:canvas.Canvas, motherName:str):
    """add patient mother name

    Args:
        canvas (canvas.Canvas): canvas to use
        motherName (str): patient mother name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(motherName) != type(str()):
            return Response('Mother name has to be str', status=400)
        # verify if patient motherName is smaller than 60 characters
        motherName = motherName.strip()
        if 7 < len(motherName) <= 70:
            canvas = global_functions.add_data(can=canvas, data=motherName, pos=(25, 636))
            return canvas
        else:
            return Response("Unable to add patient motherName because is longer than 70 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding patient motherName', status=500)


def add_patient_responsible_name(canvas:canvas.Canvas, name:str):
    """add patient responsible name

    Args:
        canvas (canvas.Canvas): canvas to use
        name (str): patient responsible name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(name) != type(str()):
            return Response('Responsible name has to be str', status=400)
        # verify if patient responsible name is smaller than 60 characters
        name = name.strip()
        if 7 < len(name) <= 70:
            canvas = global_functions.add_data(can=canvas, data=name, pos=(25, 612))
            return canvas
        else:
            return Response("Unable to add responsible name because is longer than 70 characters or Smaller than 7", status=400)
    except:
        return Response('Unknow error while adding responsible name', status=500)


def add_emission_org_code(canvas:canvas.Canvas, code:str):
    """add emission organization code to document

    Args:
        canvas (canvas.Canvas): canvas to use
        code (str): emission organizaton code

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(code) != type(str()):
            return Response('Emission org code has to be str', status=400)
        # verify if emission_org_code is smaller than 60 characters
        code = code.strip()
        if 2 < len(code) <= 17:
            canvas = global_functions.add_data(can=canvas, data=code, pos=(292, 93))
            return canvas
        else:
            return Response("Unable to add emission org code( because is longer than 17 characters or Smaller than 2", status=400)
    except:
        return Response('Unknow error while adding emission org code', status=500)


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
        if 7 < len(adress) <= 101:
            canvas = global_functions.add_data(can=canvas, data=adress, pos=(25, 593))
            return canvas
        else:
            return Response("Unable to add patient adress because is longer than 101 characters or smaller than 7", status=400)
    except:
        Response('Unknow error while adding patient Adress', status=500)


def add_patient_adressCity(canvas:canvas.Canvas, city:str):
    """add pacient adress City

    Args:
        canvas (canvas.Canvas): canvas to use
        city (str): pactient city

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(city) != type(str()):
            return Response('Patient adress city has to be a str', status=400)
        city = city.strip()
        if 7 > len(city) or len(city) > 61:
            return Response('Unable to add patient city is longer than 61 characters or smaller than 7', status=400)
        else:
            canvas = global_functions.add_data(can=canvas, data=city, pos=(25, 566))
            return canvas
    except:
        return Response('Unknow error while adding patient Adress City', status=500)


def add_patient_adressCity_ibgeCode(canvas:canvas.Canvas, ibgeCode:int):
    """aadd patient adress city ibge code

    Args:
        canvas (canvas.Canvas): canvas to use
        ibgeCode (int): ibge cpde

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(ibgeCode) != type(int()):
            return Response('Patient adress city Igbe code has to be a int', status=400)
        ibgeCode = str(ibgeCode)
        if len(ibgeCode) != 7:
            return Response('Patient adress city Igbe code do not have 7 digits', status=400) 
        else:
            canvas = global_functions.add_data(can=canvas, data=ibgeCode, pos=(388, 566))
            return canvas
    except:
        return Response('Unknow error while adding Patient adress city Igbe code', status=500)


def add_patient_adressUF(canvas:canvas.Canvas, uf:str):
    """add patient adres Uf to document

    Args:
        canvas (canvas.Canvas): canvas to use
        uf (str): uf to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(uf) != type(str()):
            return Response('Adress UF has to be a string', status=400)
        uf = uf.upper()
        if global_functions.ufExists(uf=uf):
            # Add empty spaces interval between averu character
            interval = ' ' * 2
            uf = interval.join(uf)
            canvas = global_functions.add_data(can=canvas, data=uf, pos=(450, 566))
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
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(cep) != type(int()):
            return Response('Patient adress CEP has to be a int', status=400)
        cep = str(cep)
        if len(cep) != 8:
            return Response('Patient Adress CEP do not have 8 digits', status=400) 
        else:
            # Add empty spaces interval between averu character
            interval = ' ' * 1
            cep = interval.join(cep)
            canvas = global_functions.add_data(can=canvas, data=cep, pos=(482, 566))

            return canvas
    except:
        return Response('Unknow error while adding patient Adress CEP', status=500)


def add_insurance_company_cnpj(canvas:canvas.Canvas, cnpj:int):
    """Add insurance company cpnj to document

    Args:
        canvas (canvas.Canvas): canvas to use
        cnpj (int): cnpj to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(cnpj) != type(int()):
            return Response('Insurance company cnpj has to be a int', status=400)
        cnpj = str(cnpj)
        if global_functions.isCNPJvalid(cnpj):
            # Add empty spaces interval between averu character
            interval = ' ' * 2
            cnpj = interval.join(cnpj)
            canvas = global_functions.add_data(can=canvas, data=cnpj, pos=(168, 183))
            return canvas
        else:
            return Response('Insurance company cnpj is not valid', status=400) 
    except:
        return Response('Unknow error while adding Insurance company cnpj', status=500)


def add_company_cnpj(canvas:canvas.Canvas, cnpj:int):
    """add company cnpj to document

    Args:
        canvas (canvas.Canvas): canvas to add
        cnpj (int): company cnpj

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(cnpj) != type(int()):
            return Response('Company cnpj has to be a int', status=400)
        cnpj = str(cnpj)
        if global_functions.isCNPJvalid(cnpj):
            # Add empty spaces interval between averu character
            interval = ' ' * 2
            cnpj = interval.join(cnpj)
            canvas = global_functions.add_data(can=canvas, data=cnpj, pos=(168, 156))
            return canvas
        else:
            return Response('Company cnpj is not valid', status=400) 
    except:
        return Response('Unknow error while adding Company cnpj', status=500)


def add_company_cnae(canvas:canvas.Canvas, cnae:int):
    """add company cnae

    Args:
        canvas (canvas.Canvas): canvas to use
        cnae (int): company cnae

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(cnae) != type(int()):
            return Response('Company cnae has to be a int', status=400)
        cnae = str(cnae)
        if len(cnae) == 7:
            #Format cnae to add in doc
            cnae = cnae[:2] + '.' + cnae[2:4] + '-' + cnae[4] + '-' + cnae[5:]
            canvas = global_functions.add_data(can=canvas, data=cnae, pos=(434, 156))
            return canvas
        else:
            return Response('Company cnae is longer than 7 digits', status=400) 
    except:
        return Response('Unknow error while adding Company cnae', status=500)


def add_company_cbor(canvas:canvas.Canvas, cbo:int):
    """add company cbor to canvas

    Args:
        canvas (canvas.Canvas): canvas to add
        cbo (int): company cbo

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(cbo) != type(int()):
            return Response('Company cbo has to be a int', status=400)
        cbo = str(cbo)
        if len(cbo) == 6:
            #Format cbo to add in doc
            cbo = cbo[:5] + '-' + cbo[5:]
            canvas = global_functions.add_data(can=canvas, data=cbo, pos=(529, 156))
            return canvas
        else:
            return Response('Company cbo is longer than 6 digits, remeber to use CBO 2002 format', status=400) 
    except:
        return Response('Unknow error while adding Company cbo', status=500)


def add_chart_number(canvas:canvas.Canvas, number:int):
    """add chart number to document

    Args:
        canvas (canvas): canvas to use
        number (int): chart number

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(number) != type(int()):
            return Response('Chart number has to be a int', status=400)
        number = str(number)
        if len(number) > 20:
            return Response('Chart number cannot has more than 20 digits', status=400) 
        else:
            canvas = global_functions.add_data(can=canvas, data=number, pos=(466,683))
            return canvas
    except:
        return Response('Unknow error while adding Chart number', status=500)


def add_hospitalization_autorization_number(canvas:canvas.Canvas, number:int):
    """add hospitalization autorizatoin number

    Args:
        canvas (canvas.Canvas): canvas to use
        number (int): hospitalization autorization number

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(number) != type(int()):
            return Response('Hospitalization autorizaton number has to be a int', status=400)
        number = str(number)
        if len(number) > 18:
            return Response('Hospitalization autorizaton number cannot has more than 18 digits', status=400) 
        else:
            #Add the string centetred only this time
            canvas = global_functions.add_centralized_data(can=canvas, data=number, pos=(480,66))
            return canvas
    except:
        return Response('Unknow error while adding Hospitalization autorizaton number', status=500)


def add_main_clinical_signs_symptoms(canvas:canvas.Canvas, symptoms:str):
    """Add Main clinical signs symptoms to document

    Args:
        canvas (canvas.Canvas): canvas to use
        symptoms (str): all symphtoms

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(symptoms) != type(str()):
            return Response('Clinical Signs Symptoms has to be a string', status=400)
        symptoms = symptoms.strip()
        if 5 > len(symptoms) or len(symptoms) > 1010:
            return Response('Clinical Signs Symptoms has to be at least 5 characters and not bigger than 1010 characters', status=400)
        str_symptoms = ''
        charByLine = 101
        brokeLinexTimes = int(len(symptoms)/charByLine)
        currentLine = charByLine
        lastline = 0
        yposition = 530
        # Making the line break whem has 101 charater in a line
        while brokeLinexTimes >= 0:
            str_symptoms = symptoms[lastline:currentLine]
            canvas = global_functions.add_data(can=canvas, data=str_symptoms, pos=(25, yposition))
            lastline = currentLine
            currentLine += charByLine
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
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(conditions) != type(str()):
            return Response('Conditions to Justify Hospitalization has to be a string', status=400)
        if 5 > len(conditions) or len(conditions) > 404:
            return Response('Conditions to Justify Hospitalization has to be at least 5 characters and not bigger than 404 characters', status=400)
        str_conditions = ''
        charByLine = 101
        brokeLinexTimes = int(len(conditions)/charByLine)
        currentLine = charByLine
        lastline = 0
        yposition = 422
        # Making the line break whem has 101 charater in a line
        while brokeLinexTimes >= 0:
            str_conditions = conditions[lastline:currentLine]
            canvas = global_functions.add_data(can=canvas, data=str_conditions, pos=(25, yposition))
            lastline = currentLine
            currentLine += charByLine
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


def add_exam_results(canvas:canvas.Canvas, results:str):
    """add patient exam results to database

    Args:
        canvas (canvas.Canvas): canvas to use
        results (str): results to add

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(results) != type(str()):
            return Response('Patient exame results has to be a string', status=400)
        if 5 > len(results) or len(results) > 404:
            return Response('Patient exame results has to be at least 5 characters and not bigger than 404 characters', status=400)
        str_results = ''
        charByLine = 101
        brokeLinexTimes = int(len(results)/charByLine)
        currentLine = charByLine
        lastline = 0
        yposition = 362
        # Making the line break whem has 101 charater in a line
        while brokeLinexTimes >= 0:
            str_results = results[lastline:currentLine]
            canvas = global_functions.add_data(can=canvas, data=str_results, pos=(25, yposition))
            lastline = currentLine
            currentLine += charByLine
            brokeLinexTimes -= 1
            yposition -= 10

        del(str_results)
        del(brokeLinexTimes)
        del(currentLine)
        del(lastline)
        del(yposition)
        return canvas
    except:
        return Response('Unknow error while adding Patient exame results', status=500)


def add_initial_diagnostic(canvas:canvas.Canvas, diagnostic:str):
    """add initial diagnostic in doc

    Args:
        canvas (canvas.Canvas): canvas to use
        diagnostic (str): initial diagnostic

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(diagnostic) != type(str()):
            return Response('Patient initial diagnostic has to be string', status=400)
        # verify if patient diagnostic is smaller than 60 characters
        diagnostic = str(diagnostic).strip()
        if 4 < len(diagnostic) <= 44:
            canvas = global_functions.add_data(can=canvas, data=diagnostic, pos=(25, 314))
            return canvas
        else:
            return Response("Unable to add patient initial diagnostic because is longer than 44 characters or Smaller than 4", status=400)
    except:
        return Response('Unknow error while adding patient initial diagnostic', status=500)


def add_principalCid10(canvas:canvas.Canvas, cid10:str):
    """Add principal Cid10 in the document

    Args:
        canvas (canvas.Canvas): canvas to add
        cid10 (str): principal cid10

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(cid10) != type(str()):
            return Response('Patient principal cid10 has to be string', status=400)
        # verify if patient cid10 is smaller than 5 characters
        cid10 = str(cid10).strip()
        if 2 < len(cid10) <= 4:
            canvas = global_functions.add_data(can=canvas, data=cid10, pos=(306, 314))
            return canvas
        else:
            return Response("Unable to add patient principal cid10 because is longer than 4 characters or Smaller than 3", status=400)
    except:
        return Response('Unknow error while adding patient principal cid10', status=500)


def add_secondary_cid10(canvas:canvas.Canvas, cid10:str):
    """add secondary cid10 to document

    Args:
        canvas (canvas.Canvas): canvas to use
        cid10 (str): cid10

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(cid10) != type(str()):
            return Response('Patient secondary cid10 has to be string', status=400)
        # verify if patient secondary cid10 is smaller than 5 characters
        cid10 = str(cid10).strip()
        if 2 < len(cid10) <= 4:
            canvas = global_functions.add_data(can=canvas, data=cid10, pos=(406, 314))
            return canvas
        else:
            return Response("Unable to add patient secondary cid10 because is longer than 4 characters or Smaller than 3", status=400)
    except:
        return Response('Unknow error while adding patient secondary cid10', status=500)


def add_cid10_associated_causes(canvas:canvas.Canvas, cid10:str):
    """add cid10 associated causes

    Args:
        canvas (canvas.Canvas): canvas to add
        cid10 (str): cid10 associated causes

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(cid10) != type(str()):
            return Response('Cid10 associated causes has to be string', status=400)
        # verify if Cid10 associated causes is smaller than 5 characters
        cid10 = str(cid10).strip()
        if 2 < len(cid10) <= 4:
            canvas = global_functions.add_data(can=canvas, data=cid10, pos=(512, 314))
            return canvas
        else:
            return Response("Unable to add Cid10 associated causes because is longer than 4 characters or Smaller than 3", status=400)
    except:
        return Response('Unknow error while adding Cid10 associated causes', status=500)


def add_insurance_company_series(canvas:canvas.Canvas, series:str):
    """add insurance company series

    Args:
        canvas (canvas.Canvas): canvas to use
        series (str): insurance company series

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(series) != type(str()):
            return Response('Insurance company series has to be string', status=400)
        # verify if Insurance company series is longer than 13 characters
        series = str(series).strip()
        if len(series) <= 10:
            canvas = global_functions.add_centralized_data(can=canvas, data=series, pos=(543, 183))
            return canvas
        else:
            return Response("Unable to add Insurance company series because is longer than 10 characters", status=400)
    except:
        return Response('Unknow error while adding Insurance company series', status=500)


def add_procedure_solicited(canvas:canvas.Canvas, procedure:str):
    """add procedure solicited to document

    Args:
        canvas (canvas.Canvas): canvas to use
        procedure (str): procudere solicited

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(procedure) != type(str()):
            return Response('Patient procedure solicited has to be string', status=400)
        # verify if patient procedure is smaller than 5 characters
        procedure = str(procedure).strip()
        if 5 < len(procedure) <= 65:
            canvas = global_functions.add_data(can=canvas, data=procedure, pos=(25, 269))
            return canvas
        else:
            return Response("Unable to add patient procedure solicited because is longer than 65 characters or Smaller than 5", status=400)
    except:
        return Response('Unknow error while adding patient procedure solicited', status=500)


def add_procedure_code(canvas:canvas.Canvas, code:str):
    """add procedure code in document

    Args:
        canvas (canvas.Canvas): canvas to use
        code (str): procedure code

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(code) != type(str()):
            return Response('procedure code has to be string', status=400)
        # verify if procedure code is smaller than 5 characters
        code = str(code).strip()
        if len(code) == 10:
            # Add empty spaces interval between averu character
            interval = ' ' * 2
            code = interval.join(code)
            canvas = global_functions.add_data(can=canvas, data=code, pos=(404, 269))
            return canvas
        else:
            return Response("Procedure code solicited dont have 10 characters", status=400)
    except:
        return Response('Unknow error while adding procedure code solicited', status=500)


def add_patient_mother_phonenumber(canvas:canvas.Canvas, number:int):
    """add patien mother phonenumber

    Args:
        canvas (canvas.Canvas): canvas to use
        number (int): patien mother number

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(number) != type(int()):
            return Response('mother phone number has to be int', status=400)
        number = str(number)
        if len(number) == 10:
            # Add empty spaces interval between averu character
            interval = ' ' * 2
            number = interval.join(number)
            canvas = global_functions.add_data(can=canvas, data=number, pos=(415, 631))

            return canvas
        else:
            return Response("mother phone number solicited has to be 10 digits, do not add the 9 after DDD", status=400)
    except:
        return Response('Unknow error while adding mother phone number solicited', status=500)


def add_patient_responsible_phonenumber(canvas:canvas.Canvas, number:int):
    """add patietn respnosible phone number

    Args:
        canvas (canvas.Canvas): canvas to use
        number (int): responsible phone number

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(number) != type(int()):
            return Response('responsible phone number has to be int', status=400)
        number = str(number)
        if len(number) == 10:
            # Add empty spaces interval between averu character
            interval = ' ' * 2
            number = interval.join(number)
            canvas = global_functions.add_data(can=canvas, data=number, pos=(415, 608))
            return canvas
        else:
            return Response("responsible phone number solicited has to be 10 digits, do not add the 9 after DDD", status=400)
    except:
        return Response('Unknow error while adding responsible phone number solicited', status=500)

def add_insurance_company_ticket_number(canvas:canvas.Canvas, ticket:int):
    """add insurance company ticket number

    Args:
        canvas (canvas.Canvas): canvas to add
        ticket (int): company insurance ticket

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(ticket) != type(int()):
            return Response('Insurance Company ticket number has to be int', status=400)
        ticket = str(ticket)
        if len(ticket) <= 16:
            canvas = global_functions.add_centralized_data(can=canvas, data=ticket, pos=(465, 183))
            return canvas
        else:
            return Response("Insurance company ticket has to be smaller than 16 digits", status=400)
    except:
        return Response('Unknow error while adding responsible phone ticket solicited', status=500)


def add_clinic(canvas:canvas.Canvas, name:str):
    """add clinic name to document

    Args:
        canvas (canvas.Canvas): canvas to use
        name (str): clinic name

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 

    """    
    try:
        if type(name) != type(str()):
            return Response('Clinic has to be string', status=400)
        # verify if clinic name is smaller than 5 characters
        name = str(name).strip()
        if 5 < len(name) <= 18:
            canvas = global_functions.add_data(can=canvas, data=name, pos=(25, 246))
            return canvas
        else:
            return Response("Unable to add Clinic because is longer than 18 characters or Smaller than 5", status=400)
    except:
        return Response('Unknow error while adding Clinic', status=500)


def add_internation_carater(canvas:canvas.Canvas, carater:str):
    """add internation carater to documetn

    Args:
        canvas (canvas.Canvas): canvas to use
        carater (str): internation carater

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(carater) != type(str()):
            return Response('internation carater has to be string', status=400)
        # verify if internation carater is smaller than 5 characters
        carater = str(carater).strip()
        if 5 < len(carater) <= 19:
            canvas = global_functions.add_data(can=canvas, data=carater, pos=(128, 246))
            return canvas
        else:
            return Response("Unable to add internation carater because is longer than 19 characters or Smaller than 5", status=400)
    except:
        return Response('Unknow error while adding Clinic', status=500)


def add_prof_solicitor_document(canvas:canvas.Canvas, document:dict):
    """add prof solicitoro document

    Args:
        canvas (canvas.Canvas): canvas to use
        document (dict): dict with the document and values

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error 
    """    
    try:
        if type(document) != type(dict()):
            return Response('Profissional solicitate document has to be a dict {"document":"number"}', status=400)
        # See id document is CPF or CNS
        if 'CNS' in document.keys():
            if type(document['CNS']) != type(int()):
                return Response('Profissional solicitate value CNS has to be int', status=400)
            if global_functions.isCNSvalid(document['CNS']):
                canvas = global_functions.add_square(can=canvas, pos=(247, 244))
                # Add empty spaces interval between averu character
                interval = ' ' * 2
                cns = str(document['CNS'])
                cns = interval.join(cns)
                canvas = global_functions.add_data(can=canvas, data=cns, pos=(335, 246))
                return canvas
            else:
                return Response('Profissional solicitate CNS is not valid', status=400)
        elif 'CPF' in document.keys():
            if type(document['CPF']) != type(int()):
                return Response('Profissional solicitate value CPF has to be int', status=400)
            #Format cpf to validate
            cpf = str(document['CPF'])
            numbersCpf = str(cpf)
            cpf = cpf[:3] + "." + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
            if global_functions.isCPFvalid(cpf):
                canvas = global_functions.add_square(can=canvas, pos=(290, 244))
                # Add empty spaces interval between averu character
                interval = ' ' * 2
                numbersCpf = interval.join(numbersCpf)
                canvas = global_functions.add_data(can=canvas, data=numbersCpf, pos=(335, 246))
                return canvas
            else:
                return Response('Profissional solicitate CPF is not valid', status=400)
        else:
            return Response('The document was not CPF or CNS', status=400)
    except:
        return Response('Unknow error while adding Profissional solicitate Document', status=500)


def add_autorizaton_prof_document(canvas:canvas.Canvas, document:dict):
    """add document type and number in pdf

    Args:
        canvas (canvas.Canvas): canvas to use
        document (dict): dict with doc name and numbers

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(document) != type(dict()):
            return Response('Profissional autorizate document has to be a dict {"document":"number"}', status=400)
        # See id document is CPF or CNS
        if 'CNS' in document.keys():
            if type(document['CNS']) != type(int()):
                return Response('Profissional autorizate value CNS has to be int', status=400)
            if global_functions.isCNSvalid(document['CNS']):
                canvas = global_functions.add_square(can=canvas, pos=(41, 66))
                # Add empty spaces interval between averu character
                interval = ' ' * 2
                cns = str(document['CNS'])
                cns = interval.join(cns)
                canvas = global_functions.add_data(can=canvas, data=cns, pos=(146, 66))
                return canvas
            else:
                return Response('Profissional autorizate CNS is not valid', status=400)
        elif 'CPF' in document.keys():
            if type(document['CPF']) != type(int()):
                return Response('Profissional autorizate value CPF has to be int', status=400)
            #Format cpf to validate
            cpf = str(document['CPF'])
            numbersCpf = str(cpf)
            cpf = cpf[:3] + "." + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
            if global_functions.isCPFvalid(cpf):
                canvas = global_functions.add_square(can=canvas, pos=(95, 66))
                # Add empty spaces interval between averu character
                interval = ' ' * 2
                numbersCpf = interval.join(numbersCpf)
                canvas = global_functions.add_data(can=canvas, data=numbersCpf, pos=(146, 66))
                return canvas
            else:
                return Response('Profissional autorizate CPF is not valid', status=400)
        else:
            return Response('The document was not CPF or CNS', status=400)
    except:
        return Response('Unknow error while adding Profissional autorizate Document', status=500)


def add_acident_type(canvas:canvas.Canvas, acident:str):
    """add acident type to document

    Args:
        canvas (canvas.Canvas): canvas to use
        acident (str): acident type

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(acident) != type(str()):
            return Response('Acident type has to be a str', status=400)
        # See if acident type is valid
        acidentTypes = ['traffic', 'work', 'work_path']
        acident = acident.lower()
        if acident in acidentTypes:
            if acident == 'traffic':
                canvas = global_functions.add_square(can=canvas, pos=(38, 184))
                return canvas
            elif acident == 'work':
                canvas = global_functions.add_square(can=canvas, pos=(38, 170))
                return canvas
            elif acident == 'work_path':
                canvas = global_functions.add_square(can=canvas, pos=(38, 156))
                return canvas
            else:
                return Response('Unknow error while searching Acident type', status=500)
        else:
            return Response('The acident type has to be "traffic", "work" or "work_path"', status=400)
    except:
        return Response('Unknow error while adding Acident type', status=500)


def add_pension_status(canvas:canvas.Canvas, status:str):
    """add pension status to document

    Args:
        canvas (canvas.Canvas): canvas to use
        status (str): pension status

    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
    """    
    try:
        if type(status) != type(str()):
            return Response('pension status type has to be a str', status=400)
        # See if pension status type is valid
        statusTypes = ['worker', 'employer', 'autonomous', 'unemployed', 'retired', 'not_insured']
        status = status.lower()
        ypos = 131
        if status in statusTypes:
            if status == 'worker':
                canvas = global_functions.add_square(can=canvas, pos=(33, ypos))
                return canvas
            elif status == 'employer':
                canvas = global_functions.add_square(can=canvas, pos=(124, ypos))
                return canvas
            elif status == 'autonomous':
                canvas = global_functions.add_square(can=canvas, pos=(219, ypos))
                return canvas
            elif status == 'unemployed':
                canvas = global_functions.add_square(can=canvas, pos=(305, ypos))
                return canvas
            elif status == 'retired':
                canvas = global_functions.add_square(can=canvas, pos=(408, ypos))
                return canvas
            elif status == 'not_insured':
                canvas = global_functions.add_square(can=canvas, pos=(500, ypos))
                return canvas
            else:
                return Response('Unknow error while searching pension status type', status=500)
        else:
            return Response('The pension status type has to be "worker", "employer","autonomous","unemployed","retired","not_insured"', status=400)
    except:
        return Response('Unknow error while adding pension status type', status=500)



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
        main_clinical_signs_symptoms="Patient main clinical signs sympthoms",
        conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',
        initial_diagnostic='Patient Initial Diagnostic',
        principalCid10="A00",
        procedure_solicited='Procedure Solicited',
        procedure_code='1234567890', 
        clinic='Clinic Name', 
        internation_carater='Internation Carater', 
        prof_solicitor_document={'CPF':28445400070},
        prof_solicitor_name='Profissional Solicit Name', 
        solicitation_datetime=datetime.datetime.now(), 
        autorization_prof_name='Autorization professional name', 
        emission_org_code='OrgCode2022', 
        autorizaton_prof_document={'CNS':928976954930007}, 
        autorizaton_datetime=datetime.datetime.now(),
        hospitalization_autorization_number=1234567890,
        exam_results='Xray tibia broken',
        chart_number=1234,
        patient_ethnicity='Preta', 
        patient_responsible_name='Patient Responsible Name', 
        patient_mother_phonenumber=5613248546, 
        patient_responsible_phonenumber=8564721598, 
        secondary_cid10='A01',
        cid10_associated_causes='A02',
        acident_type='work_path', 
        insurance_company_cnpj=37549670000171, 
        insurance_company_ticket_number=123450123456, 
        insurance_company_series='Insurn',
        company_cnpj=37549670000171, 
        company_cnae=5310501, 
        company_cbor=123456, 
        pension_status='not_insured'
    )

    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/aih_sus_teste.pdf")