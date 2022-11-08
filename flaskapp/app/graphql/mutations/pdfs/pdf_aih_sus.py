import base64
import datetime
from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from flask import Response
from typing import Union
from app.utils import pdf_functions
from app.env import FONT_DIRECTORY, TEMPLATE_AIH_SUS_DIRECTORY, WRITE_AIH_SUS_DIRECTORY

from app.graphql import mutation
from ariadne import convert_kwargs_to_snake_case

@mutation.field('generatePdf_AihSus')
@convert_kwargs_to_snake_case
def fill_pdf_aih_sus(establishment_solitc_name:str, establishment_solitc_cnes:int, establishment_exec_name:str, establishment_exec_cnes:int, patient_name:str, patient_cns:int, patient_birthday:datetime.datetime, patient_sex:str, patient_mother_name:str, patient_adress:str, patient_adressCity:str, patient_adressCity_ibgeCode:int, patient_adressUF:str, patient_adressCEP:int, main_clinical_signs_symptoms:str, conditions_justify_hospitalization:str, initial_diagnostic:str, principalCid10:str, procedure_solicited:str, procedure_code:str, clinic:str, internation_carater:str, prof_solicitor_document:dict, prof_solicitor_name:str, solicitation_datetime:datetime.datetime, autorization_prof_name:str, emission_org_code:str, autorizaton_prof_document:dict, autorizaton_datetime:datetime.datetime, hospitalization_autorization_number:int ,exam_results:str=None, chart_number:int=None, patient_ethnicity:str=None, patient_responsible_name:str=None, patient_mother_phonenumber:int=None, patient_responsible_phonenumber:int=None, secondary_cid10:str=None, cid10_associated_causes:str=None, acident_type:str=None, insurance_company_cnpj:int=None, insurance_company_ticket_number:int=None, insurance_company_series:str=None,company_cnpj:int=None, company_cnae:int=None, company_cbor:int=None, pension_status:str=None) -> Union[bytes, Response]:
    """fill pdf aih sus 

    Args:
        establishment_solitc_name (str): establishment_solitc_name
        establishment_solitc_cnes (int): establishment_solitc_cnes
        establishment_exec_name (str): establishment_exec_name
        establishment_exec_cnes (int): establishment_exec_cnes
        patient_name (str): patient_name
        patient_cns (int): patient_cns
        patient_birthday (datetime.datetime): patient_birthday
        patient_sex (str): patient_sex
        patient_mother_name (str): patient_mother_name
        patient_adress (str): patient_adress
        patient_adressCity (str): patient_adressCity
        patient_adressCity_ibgeCode (int): patient_adressCity_ibgeCode
        patient_adressUF (str): patient_adressUF
        patient_adressCEP (int): patient_adressCEP
        main_clinical_signs_symptoms (str): main_clinical_signs_symptoms
        conditions_justify_hospitalization (str): conditions_justify_hospitalization
        initial_diagnostic (str): initial_diagnostic
        principalCid10 (str): principalCid10
        procedure_solicited (str): procedure_solicited
        procedure_code (str): procedure_code
        clinic (str): clinic
        internation_carater (str): internation_carater
        prof_solicitor_document (dict): dict prof_solicitor_document
        prof_solicitor_name (str): prof_solicitor_name
        solicitation_datetime (datetime.datetime): solicitation_datetime
        autorization_prof_name (str): autorization_prof_name
        emission_org_code (str): emission_org_code
        autorizaton_prof_document (dict): autorizaton_prof_document
        autorizaton_datetime (datetime.datetime): autorizaton_datetime
        hospitalization_autorization_number (int): hospitalization_autorization_number
        exam_results (str, optional): exam_results. Defaults to None.
        chart_number (int, optional): chart_number. Defaults to None.
        patient_ethnicity (str, optional): patient_ethnicity. Defaults to None.
        patient_responsible_name (str, optional): patient_responsible_name. Defaults to None.
        patient_mother_phonenumber (int, optional): patient_mother_phonenumber. Defaults to None.
        patient_responsible_phonenumber (int, optional): patient_responsible_phonenumber. Defaults to None.
        secondary_cid10 (str, optional): secondary_cid10. Defaults to None.
        cid10_associated_causes (str, optional): cid10_associated_causes. Defaults to None.
        acident_type (str, optional): acident_type. Defaults to None.
        insurance_company_cnpj (int, optional): insurance_company_cnpj. Defaults to None.
        insurance_company_ticket_number (int, optional): insurance_company_ticket_number. Defaults to None.
        insurance_company_series (str, optional): insurance_company_series. Defaults to None.
        company_cnpj (int, optional): company_cnpj. Defaults to None.
        company_cnae (int, optional): company_cnae. Defaults to None.
        company_cbor (int, optional): company_cbor. Defaults to None.
        pension_status (str, optional): pension_status. Defaults to None.

    Returns:
        Union[bytes, Response]: base64 pdf enconded or a Response with a error
    """    
    try:
        packet = io.BytesIO()
        # Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        c.setFont('Roboto-Mono', 9)
        # Writing all data in respective fields
        # not null data
        try:
            c = pdf_functions.add_oneline_text(can=c, text=establishment_solitc_name, pos=(25, 750), camp_name='Establishment Solicit Name', len_max=82, len_min=8)
            if type(c) == type(Response()): return c
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=establishment_solitc_cnes, pos=(470, 750), camp_name='Establishment Solict CNES', len_max=7, len_min=7,value_min=0, value_max=99999999, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=establishment_exec_name, pos=(25, 726), camp_name='Establishment Exec Name', len_max=82, len_min=8)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=establishment_exec_cnes, pos=(470, 726), camp_name='Establishment Exec CNES', len_max=7, len_min=7,value_min=0, value_max=99999999, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_name, pos=(25, 683), camp_name='Patient Name', len_max=79, len_min=7)
            if type(c) == type(Response()): return c
            #Data that change Font Size

            c.setFont('Roboto-Mono', 10)
            c = pdf_functions.add_cns(can=c, cns=patient_cns, pos=(28, 658), camp_name='Patient CNS', interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_adressCEP, pos=(482, 566), camp_name='Patient Adress CEP', len_max=8, len_min=8, value_min=0, value_max=99999999, nullable=True, interval=' ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=procedure_code, pos=(404, 269), camp_name='Procedure Code', len_max=10, len_min=10, interval='  ')
            if type(c) == type(Response()): return c
            
            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_datetime(can=c, date=patient_birthday, pos=(312, 658), camp_name='Patient Birthday', hours=False, interval='  ', formated=False)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(415, 657), pos_fem=(468, 657), camp_name='Patient Sex', square_size=(8,9))
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(25, 636), camp_name='Patient Mother Name', len_max=70, len_min=7)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress, pos=(25, 593), camp_name='Patient Adress', len_max=101, len_min=7)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adressCity, pos=(25, 566), camp_name='Patient Adress City', len_max=58, len_min=7)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_adressCity_ibgeCode, pos=(388, 566), camp_name='Patient Adress City IBGE code', len_max=7, len_min=7, value_min=0, value_max=9999999)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_UF(can=c, uf=patient_adressUF, pos=(450, 566), camp_name='Patient Adress UF', interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_morelines_text(can=c, text=main_clinical_signs_symptoms, initial_pos=(25, 530), decrease_ypos= 10, camp_name='Main Clinical Signs Symptoms', len_max=1009, char_per_lines=101, len_min=5)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_morelines_text(can=c, text=conditions_justify_hospitalization, initial_pos=(25, 422), decrease_ypos= 10, camp_name='Conditions that Justify hospitalization', len_max=403, char_per_lines=101, len_min=5)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=initial_diagnostic, pos=(25, 314), camp_name='Initial Diagnostic', len_max=44, len_min=5)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=principalCid10, pos=(306, 314), camp_name='Principal Cid10', len_max=4, len_min=3)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=procedure_solicited, pos=(25, 269), camp_name='Procedure Solicited', len_max=65, len_min=6)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=clinic, pos=(25, 246), camp_name='Clinic', len_max=18, len_min=6)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=internation_carater, pos=(128, 246), camp_name='Internation Caracter', len_max=19, len_min=6)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=prof_solicitor_document, pos_square_cpf=(290, 244), pos_square_cns=(247,244), pos_cns=(335, 246), pos_cpf=(335, 246),camp_name='Professional Solicitor Document', interval='  ',nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=prof_solicitor_name, pos=(25, 222), camp_name='Professional Solicitor Name', len_max=48, len_min=8)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_datetime(can=c, date=solicitation_datetime, pos=(300, 222), camp_name='Solicitation Datetime', hours=False, interval='  ', formated=False)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=autorization_prof_name, pos=(25, 93), camp_name='Professional Authorizator Name', len_max=48, len_min=8)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=emission_org_code, pos=(292, 93), camp_name='Emission Organization Code', len_max=17, len_min=2)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=autorizaton_prof_document, pos_square_cpf=(95, 66), pos_square_cns=(41,66), pos_cns=(146, 66), pos_cpf=(146, 66),camp_name='Professional Authorizator Document', interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_datetime(can=c, date=autorizaton_datetime, pos=(30, 30), camp_name='Authorization Datetime', hours=False, interval='  ', formated=False)
            if type(c) == type(Response()): return c
            c.setFont('Roboto-Mono', 16)       
            c = pdf_functions.add_oneline_intnumber(can=c, number=hospitalization_autorization_number, pos=(480, 66), camp_name='Hospitalization autorization Number', len_max=18, len_min=1, value_min=0, value_max=999999999999999999, centralized=True)
            if type(c) == type(Response()): return c
            c.setFont('Roboto-Mono', 9)       

            
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            c = pdf_functions.add_morelines_text(can=c, text=exam_results, initial_pos=(25, 362), decrease_ypos= 10, camp_name='Exam Results', len_max=403, char_per_lines=101, len_min=5, nullable=True)            
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=chart_number, pos=(466, 683), camp_name='Chart Number', len_max=20, len_min=1, value_min=0, value_max=99999999999999999999, nullable=True)            
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_ethnicity, pos=(510, 658), camp_name='Patient Ehinicity', len_max=11, len_min=4, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_responsible_name, pos=(25, 612), camp_name='Patient Responsible Name', len_max=70, len_min=7, nullable=True)        
            if type(c) == type(Response()): return c
            c = pdf_functions.add_phonenumber(can=c, number=patient_mother_phonenumber, pos=(415, 631), camp_name='Patient Mother phone number', nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_phonenumber(can=c, number=patient_responsible_phonenumber, pos=(415, 608), camp_name='Patient responsible phone number', nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=secondary_cid10, pos=(406, 314), camp_name='Secondary Cid10', len_max=4, len_min=3, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=cid10_associated_causes, pos=(512, 314), camp_name='Associated causes Cid10', len_max=4, len_min=3, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square(can=c, option=acident_type, valid_options=['TRAFFIC', 'WORK', 'WORK_PATH'], options_positions=((38,184),(38,170), (38,156)), square_size=(9,9), camp_name='Acident Type', nullable=True)
            if type(c) == type(Response()): return c

            #Data that change Font Size
            c.setFont('Roboto-Mono', 10)
            c = pdf_functions.add_cnpj(can=c, cnpj=insurance_company_cnpj, pos=(168,183), camp_name='Insurance Company CNPJ', nullable=True, interval='  ')           
            if type(c) == type(Response()): return c
            c = pdf_functions.add_cnpj(can=c, cnpj=company_cnpj, pos=(168,156), camp_name='Company CNPJ', nullable=True, interval='  ')
            if type(c) == type(Response()): return c            
            

            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_oneline_intnumber(can=c, number=insurance_company_ticket_number, pos=(465, 183), camp_name='Insurance company ticket number', len_max=16, len_min=1, value_min=0, value_max=9999999999999999, nullable=True, centralized=True)           
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=insurance_company_series, pos=(543, 183), camp_name='Insurance Company Series', len_max=10, len_min=1, nullable=True, centralized=True)           
            if type(c) == type(Response()): return c
            c = pdf_functions.add_cnae(can=c, cnae=company_cnae, pos=(434, 156), camp_name='Company CNAE', nullable=True, formated=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_cbor(can=c, cbor=company_cbor, pos=(529, 156), camp_name='Company CBOR', nullable=True, formated=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square(can=c, option=pension_status, valid_options=['WORKER', 'EMPLOYER', 'AUTONOMOUS', 'UNEMPLOYED', 'RETIRED', 'NOT_INSURED'], options_positions=((33,131),(124,131),(219,131),(305,131),(408,131),(500,131),), square_size=(9,9), camp_name='Pension Status', nullable=True)
            if type(c) == type(Response()): return c


        except:
            return Response('Critical error happen when adding data that can be null to fields', status=500)

        # create a new PDF with Reportlab
        c.save()
        packet.seek(0)
        new_pdf = PdfReader(packet)
        # read the template pdf 
        template_pdf = PdfReader(open(TEMPLATE_AIH_SUS_DIRECTORY, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)
        
        pdf_functions.write_newpdf(output, WRITE_AIH_SUS_DIRECTORY)
        
        with open(WRITE_AIH_SUS_DIRECTORY, "rb") as pdf_file:
            pdf_base64_enconded = base64.b64encode(pdf_file.read())

        return pdf_base64_enconded
    except:
        return Response("Error while filling aih sus", status=500)


