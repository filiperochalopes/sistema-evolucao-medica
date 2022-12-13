import base64
import datetime
from PyPDF2  import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from typing import Union
from app.services.utils import pdf_functions
from app.env import FONT_DIRECTORY, TEMPLATE_FICHA_INTERN_DIRECTORY, WRITE_FICHA_INTERN_DIRECTORY


def func_generate_pdf_ficha_internamento(document_datetime:datetime.datetime, patient_name:str, patient_cns:str, patient_birthday:datetime.datetime, patient_sex:str, patient_mother_name:str, patient_document:dict, patient_adress:str, patient_phonenumber:str, patient_drug_allergies:str, patient_comorbidities:str, current_illness_history:str, initial_diagnostic_suspicion:str, doctor_name:str, doctor_cns:str, doctor_crm:str, patient_adress_number:int=None, patient_adress_neigh:str=None, patient_adress_city:str=None, patient_adress_uf:str=None, patient_adress_cep:str=None, patient_nationality:str=None, patient_estimate_weight:int=None, has_additional_health_insurance:bool=None) -> str:
    """fill pdf ficha internamento

    Args:
        document_datetime (datetime.datetime): document_datetime
        patient_name (str): patient_name
        patient_cns (str):fill_pdf_ficha_internamento patient_cns
        patient_birthday (datetime.datetime): patient_birthday
        patient_sex (str): patient_sex
        patient_mother_name (str): patient_mother_name
        patient_document (dict): patient_document
        patient_adress (str): patient_adress
        patient_phonenumber (int): patient_phonenumber
        patient_drug_allergies (str): patient_drug_allergies
        patient_comorbidities (str): patient_comorbidities
        current_illness_history (str): current_illness_history
        initial_diagnostic_suspicion (str): initial_diagnostic_suspicion
        doctor_name (str): doctor_name
        doctor_cns (int): doctor_cns
        doctor_crm (str): doctor_crm
        patient_adress_number (int, optional): patient_adress_number. Defaults to None.
        patient_adress_neigh (str, optional): patient_adress_neigh. Defaults to None.
        patient_adress_city (str, optional): patient_adress_city. Defaults to None.
        patient_adress_uf (str, optional): patient_adress_uf. Defaults to None.
        patient_adress_cep (int, optional): patient_adress_cep. Defaults to None.
        patient_nationality (str, optional): patient_nationality. Defaults to None.
        patient_estimate_weight (int, optional): patient_estimate_weight. Defaults to None.
        has_additional_health_insurance (bool, optional): has_additional_health_insurance. Defaults to None.

    Returns:
        str: Request with pdf in base64
    """    

    try:
        packet = io.BytesIO()
        # Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        c.setFont('Roboto-Mono', 12)

        # Writing all data in respective fields
        # not null data
        try:
            # change font size to datetime            
            c = pdf_functions.add_datetime(can=c, date=document_datetime, pos=(410, 740), camp_name='Document Datetime', hours=True, formated=True)
            
            
            c.setFont('Roboto-Mono', 9)
            #Normal font size
            c = pdf_functions.add_oneline_text(can=c, text=patient_name, pos=(27, 674), camp_name='Patient Name', len_max=64, len_min=7)
            # verify if c is a error at some point
            c = pdf_functions.add_cns(can=c, cns=patient_cns, pos=(393, 674), camp_name='Patient CNS', formated=True)
            c = pdf_functions.add_datetime(can=c, date=patient_birthday, pos=(27, 642), camp_name='Patient Birthday', hours=False, formated=True)
            c = pdf_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(117, 640), pos_fem=(147, 640), camp_name='Patient Sex', square_size=(9,9))
            c = pdf_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(194, 642), camp_name='Patient Mother Name', len_max=69, len_min=7)
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=patient_document, pos_square_cpf=(24, 608), pos_square_rg=(58,608), pos_rg=(92, 610), pos_cpf=(92, 610),camp_name='Pacient Document', formated=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress, pos=(230, 610), camp_name='Patient Adress', len_max=63, len_min=7)
            c = pdf_functions.add_phonenumber(can=c, number=patient_phonenumber, pos=(173, 547), camp_name='Patient phone number', formated=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_drug_allergies, pos=(26, 481), camp_name='Patient Drugs Allergies', len_max=100, len_min=5)
            c = pdf_functions.add_oneline_text(can=c, text=patient_comorbidities, pos=(26, 449), camp_name='Patient Commorbidites', len_max=100, len_min=5)
            c = pdf_functions.add_morelines_text(can=c, text=current_illness_history, initial_pos=(26, 418), decrease_ypos= 10, camp_name='Current Illness History', len_max=1600, char_per_lines=100, len_min=10)
            c = pdf_functions.add_oneline_text(can=c, text=initial_diagnostic_suspicion, pos=(26, 244), camp_name='Initial Diagnostic Suspicion', len_max=100, len_min=5)
            c = pdf_functions.add_oneline_text(can=c, text=doctor_name, pos=(304, 195), camp_name='Doctor Name', len_max=49, len_min=7)
            c = pdf_functions.add_cns(can=c, cns=doctor_cns, pos=(304, 163), camp_name='Doctor CNS', formated=True)
            c = pdf_functions.add_oneline_text(can=c, text=doctor_crm, pos=(304, 131), camp_name='Doctor CRM', len_max=13, len_min=11)
            
        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados obrigadorios')

        #Adding data that can be null
        try:
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_adress_number, pos=(24, 580), camp_name='Patient Adress Number', len_max=6, len_min=1, value_min=0, value_max=999999, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_neigh, pos=(66, 580), camp_name='Patient Adress Neighborhood', len_max=31, len_min=4, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_city, pos=(243, 580), camp_name='Patient Adress City', len_max=34, len_min=3, nullable=True)
            c = pdf_functions.add_UF(can=c, uf=patient_adress_uf, pos=(444, 580), camp_name='Patient Adress UF', nullable=True)
            c = pdf_functions.add_CEP(can=c, cep=patient_adress_cep, pos=(483, 580), camp_name='Patient Adress CEP', nullable=True, formated=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_nationality, pos=(27, 547), camp_name='Patient nationality', len_max=25, len_min=3, nullable=True)
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_estimate_weight, pos=(507, 547), camp_name='Patient Estimate Weight', len_max=6, len_min=1, value_min=1, value_max=500, nullable=True)
            if has_additional_health_insurance != None:
                c = pdf_functions.add_markable_square(can=c, option=str(has_additional_health_insurance), valid_options=['SIM','NAO'], options_positions=((419, 544), (380, 544)), camp_name='Has additional Healt insurance', nullable=False)

        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados opcionais')

        # create a new PDF with Reportlab
        c.save()
        packet.seek(0)
        new_pdf = PdfReader(packet)
        # read the template pdf 
        template_pdf = PdfReader(open(TEMPLATE_FICHA_INTERN_DIRECTORY, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        pdf_functions.write_newpdf(output, WRITE_FICHA_INTERN_DIRECTORY)
        
        with open(WRITE_FICHA_INTERN_DIRECTORY, "rb") as pdf_file:
            pdf_base64_enconded = base64.b64encode(pdf_file.read())

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except:
        return Exception("Erro desconhecido enquanto preenchia o documento ficha de internamento")
