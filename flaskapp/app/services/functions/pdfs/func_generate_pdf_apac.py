import datetime
from PyPDF2 import PdfWriter, PdfReader
import io
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from app.services.utils import pdf_functions
from app.env import FONT_DIRECTORY, TEMPLATE_APAC_DIRECTORY, WRITE_APAC_DIRECTORY
from app.services.utils.PdfApac import PdfApac


def func_generate_pdf_apac(establishment_solitc_name:str, establishment_solitc_cnes:int, patient_name:str, patient_cns:str, patient_sex:str, patient_birthday:str, patient_adress_city:str, main_procedure:dict, patient_mother_name:str=None, patient_mother_phonenumber:str=None, patient_responsible_name:str=None, patient_responsible_phonenumber:str=None, patient_adress:str=None, patient_ethnicity:str=None, patient_color:str=None, patient_adress_uf:str=None, patient_adress_cep:str=None, document_chart_number:str=None, patient_adress_city_ibge_code:str=None, procedure_justification_description:str=None, procedure_justification_main_cid_10:str=None, procedure_justification_sec_cid_10:str=None, procedure_justification_associated_cause_cid_10:str=None, procedure_justification_comments:str=None, establishment_exec_name:str=None, establishment_exec_cnes:int=None,prof_solicitor_document:dict=None, prof_solicitor_name:str=None, solicitation_datetime:datetime.datetime=None, prof_autorization_name:str=None, emission_org_code:str=None, autorizaton_prof_document:dict=None, autorizaton_datetime:datetime.datetime=None, signature_datetime:datetime.datetime=None, validity_period_start:datetime.datetime=None, validity_period_end:datetime.datetime=None, secondaries_procedures:list=None) -> str:
    """fill pdf apac

    Args:
        establishment_solitc_name (str): establishment_solitc_name
        establishment_solitc_cnes (int): establishment_solitc_cnes
        patient_name (str): patient_name
        patient_cns (str): patient_cns
        patient_sex (str): patient_sex
        patient_birthday (str): patient_birthday
        patient_adress_city (str): patient_adress_city
        main_procedure (dict): dict with name, code and quat of main procedure
        patient_mother_name (str, optional): patient_mother_name. Defaults to None.
        patient_mother_phonenumber (int, optional): patient_mother_phonenumber. Defaults to None.
        patient_responsible_name (str, optional): patient_responsible_name. Defaults to None.
        patient_responsible_phonenumber (int, optional): patient_responsible_phonenumber. Defaults to None.
        patient_adress (str, optional): patient_adress. Defaults to None.
        patient_ethnicity (str, optional): patient_ethnicity. Defaults to None.
        patient_color (str, optional): patient_color. Defaults to None.
        patient_adress_uf (str, optional): patient_adress_uf. Defaults to None.
        patient_adress_cep (int, optional): patient_adress_cep. Defaults to None.
        document_chart_number (str, optional): document_chart_number. Defaults to None.
        patient_adress_city_ibge_code (str, optional): patient_adress_city_ibge_code. Defaults to None.
        procedure_justification_description (str, optional): procedure_justification_description. Defaults to None.
        procedure_justification_main_cid_10 (str, optional): procedure_justification_main_cid_10. Defaults to None.
        procedure_justification_sec_cid_10 (str, optional): procedure_justification_sec_cid_10. Defaults to None.
        procedure_justification_associated_cause_cid_10 (str, optional): procedure_justification_associated_cause_cid_10. Defaults to None.
        procedure_justification_comments (str, optional): procedure_justification_comments. Defaults to None.
        establishment_exec_name (str, optional): establishment_exec_name. Defaults to None.
        establishment_exec_cnes (int, optional): establishment_exec_cnes. Defaults to None.
        prof_solicitor_document (dict, optional): prof_solicitor_document. Defaults to None.
        prof_solicitor_name (str, optional): prof_solicitor_name. Defaults to None.
        solicitation_datetime (datetime.datetime, optional): solicitation_datetime. Defaults to None.
        prof_autorization_name (str, optional): prof_autorization_name. Defaults to None.
        emission_org_code (str, optional): emission_org_code. Defaults to None.
        autorizaton_prof_document (dict, optional): autorizaton_prof_document. Defaults to None.
        autorizaton_datetime (datetime.datetime, optional): autorizaton_datetime. Defaults to None.
        signature_datetime (datetime.datetime, optional): signature_datetime. Defaults to None.
        validity_period_start (datetime.datetime, optional): validity_period_start. Defaults to None.
        validity_period_end (datetime.datetime, optional): validity_period_end. Defaults to None.
        secondaries_procedures (list, optional): list with dict with procedure, eg: 
        [{"procedure_name":"Procedure Name", "procedure_code":"cod4521578", "quant":5}, 
        {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]
        . Defaults to None.

    Returns:
        str: Request with pdf in base64
    """    
    try:
        pdf = PdfApac()
        packet = io.BytesIO()
        # Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        c.setFont('Roboto-Mono', 10)
        # Writing all data in respective fields
        # not null data
        try:
            pdf.add_cns(cns=patient_cns, pos=(36, 678), camp_name='Patient CNS', interval='  ')
            pdf.add_procedure(procedure=main_procedure, code_pos=(36,542), name_pos=(220, 542), quant_pos=(508, 542), camp_name='Main Procedure')

            pdf.set_font('Roboto-Mono', 9)
            pdf.add_oneline_text(text=establishment_solitc_name, pos=(36, 742), camp_name='Establishment Solict Name', len_max=77, len_min=7)
            pdf.add_oneline_text(text=patient_name, pos=(36, 702), camp_name='Patient Name', len_max=67, len_min=7)
            pdf.add_sex_square(sex=patient_sex, pos_male=(423, 699), pos_fem=(456, 699), camp_name='Patient Sex', square_size=(9,9))
            pdf.add_datetime(date=patient_birthday, pos=(315, 678), camp_name='Patient Birthday', hours=False, interval='  ', formated=False)
            pdf.add_oneline_text(text=patient_adress_city, pos=(36, 584), camp_name='Patient Adress City', len_max=58, len_min=3)
            pdf.add_oneline_intnumber(number=establishment_solitc_cnes, pos=(468, 742), camp_name='Establishment Solict CNES', len_max=7, len_min=7,value_min=0, value_max=99999999)
        
        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados obrigatorios')

        #Adding data that can be null
        try:
            c.setFont('Roboto-Mono', 11)
            c = pdf_functions.add_oneline_intnumber(can=c, number=establishment_exec_cnes, pos=(450, 28), camp_name='Establishment Exec CNES', len_max=7, len_min=7,value_min=0, value_max=99999999, interval=' ', nullable=True)
            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(36, 654), camp_name='Patient Mother Name', len_max=67, len_min=7, nullable=True)
            c = pdf_functions.add_phonenumber(can=c, number=patient_mother_phonenumber, pos=(409, 650), camp_name='Patient Mother Phone Number', nullable=True, interval='  ')
            c = pdf_functions.add_oneline_text(can=c, text=patient_responsible_name, pos=(36, 630), camp_name='Patient Responsible Name', len_max=67, len_min=7, nullable=True)
            c = pdf_functions.add_phonenumber(can=c, number=patient_responsible_phonenumber, pos=(409, 626), camp_name='Patient Responsible Phone Number', nullable=True, interval='  ')
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress, pos=(36, 608), camp_name='Patient Adress', len_max=97, len_min=7, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_color, pos=(404, 678), camp_name='Patient Color', len_max=10, len_min=4, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_ethnicity, pos=(470, 678), camp_name='Patient Ehinicity', len_max=17, len_min=4, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_cep, pos=(476, 582), camp_name='Patient Adress CEP', len_max=8, len_min=8, nullable=True, interval=' ')
            c = pdf_functions.add_oneline_text(can=c, text=document_chart_number, pos=(483, 702), camp_name='Document Chart Number', len_max=14, len_min=1, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_city_ibge_code, pos=(370, 582), camp_name='Patient Adress City IBGE code', len_max=7, len_min=7, nullable=True)
            c = pdf_functions.add_UF(can=c, uf=patient_adress_uf, pos=(443, 582), camp_name='Patient Adress UF', nullable=True, interval='  ')
            c = pdf_functions.add_oneline_text(can=c, text=procedure_justification_description, pos=(36, 344), camp_name='Procedure Justification Description', len_max=55, len_min=4, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=procedure_justification_main_cid_10, pos=(352, 344), camp_name='Procedure Justification main CID10', len_max=4, len_min=3, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=procedure_justification_sec_cid_10, pos=(420, 344), camp_name='Procedure Justification secondary CID10', len_max=4, len_min=3, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=procedure_justification_associated_cause_cid_10, pos=(505, 344), camp_name='Procedure Justification Associated Causes CID10', len_max=4, len_min=3, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=establishment_exec_name, pos=(36, 30), camp_name='Establishment Exec Name', len_max=71, len_min=5, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=prof_solicitor_name, pos=(36, 204), camp_name='Profissional Solicitor Name', len_max=48, len_min=5, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=prof_autorization_name, pos=(36, 136), camp_name='Profissional Authorizator Name', len_max=46, len_min=5, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=emission_org_code, pos=(290, 136), camp_name='Emission Org Code', len_max=16, len_min=2, nullable=True)
            c = pdf_functions.add_datetime(can=c, date=solicitation_datetime, pos=(310, 204), camp_name='Solicitation Datetime', hours=False, interval='  ', formated=False, nullable=True)
            c = pdf_functions.add_datetime(can=c, date=autorizaton_datetime, pos=(36, 68), camp_name='Authorization Datetime', hours=False,formated=True, nullable=True)
            c = pdf_functions.add_datetime(can=c, date=signature_datetime, pos=(154, 68), camp_name='Signature Datetime', hours=False, interval='  ', formated=False, nullable=True)
            c = pdf_functions.add_datetime(can=c, date=validity_period_start, pos=(402, 66), camp_name='Validity Period Start', hours=False, interval='  ', formated=False, nullable=True)
            c = pdf_functions.add_datetime(can=c, date=validity_period_end, pos=(492, 66), camp_name='Validity Period End', hours=False, interval='  ', formated=False, nullable=True)
            c = add_secondary_procedures(can=c, procedures=secondaries_procedures)
            c = pdf_functions.add_morelines_text(can=c, text=procedure_justification_comments, initial_pos=(36, 318), decrease_ypos= 10, camp_name='Procedura justification Comments', len_max=776, char_per_lines=97, len_min=5, nullable=True)
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=prof_solicitor_document, pos_square_cpf=(103, 180), pos_square_cns=(51,180), pos_cns=(151, 181), pos_cpf=(151, 181),camp_name='Professional Solicitor Document', interval='  ',nullable=True)
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=autorizaton_prof_document, pos_square_cpf=(103, 104), pos_square_cns=(51,104), pos_cns=(149, 105), pos_cpf=(151, 105),camp_name='Professional Authorizator Document', interval='  ',nullable=True)
        
        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados opcionais')

        # create a new PDF with Reportlab
        # c.save()
        # packet.seek(0)
        # new_pdf = PdfReader(packet)
        # # read the template pdf 
        # template_pdf = PdfReader(open(TEMPLATE_APAC_DIRECTORY, "rb"))
        # output = PdfWriter()
        # # add the "watermark" (which is the new pdf) on the existing page
        # page = template_pdf.pages[0]
        # page.merge_page(new_pdf.pages[0])
        # output.add_page(page)

        # pdf_base64_enconded = pdf_functions.get_base64(newpdf=output)
        
        #Get pdf base64
        pdf_base64_enconded = pdf.get_base64()

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except Exception as error:
        return error
    except:
        return Exception("Erro desconhecido enquanto preenchia o documento Apac")


def add_procedure(can:canvas.Canvas, procedure:dict, code_pos:tuple, name_pos:tuple, quant_pos:tuple, camp_name:str) -> canvas.Canvas:
    """Add proceure to canvas

    Args:
        can (canvas.Canvas): canvas to use
        procedure (dict): dict with procedure info
        code_pos (tuple): position of code
        name_pos (tuple): position of name
        quant_pos (tuple): position of quant
        camp_name (str): camp name

    Returns:
        canvas.Canvas: canvas updated
    """
    try:
        if procedure == None:
            return can
        if type(procedure) != type(dict()):
            raise Exception('procedure deve ser um dicionario, exemplo: {"name":"Procedure Name", "code":"cod124235", "quant":5}')
        necessaryKeys = ["name", "code", "quant"]
        #Verify if the necessary keys are in the dict
        if 'name' not in procedure.keys() or 'code' not in procedure.keys() or "quant" not in procedure.keys():
            raise Exception('Algumas chaves do dicionario estao faltando, o dicionario deve ter as chaves "name", "code", "quant"')
        #Verify if the value in the dics is the needed
        elif type(procedure['name']) != type(str()) or type(procedure['code']) != type(str()) or type(procedure["quant"]) != type(int()):
            raise Exception('Os valores das chaves "name", "code" devem ser string e "quant" deve ser um numero inteiro')
        #Verify if the dict has more keys than the needed
        for key in procedure.keys():
            if key not in necessaryKeys:
                raise Exception('O dicionario deve ter somente 3 chaves, sendo elas: "name", "code", "quant"')
        
        ## Add to canvas
        # Change size to add Code
        can.setFont('Roboto-Mono', 10)
        can = pdf_functions.add_oneline_text(can=can, text=procedure['code'], pos=code_pos, camp_name=f'{camp_name} Procedure Code', len_max=10, len_min=10, interval='  ')
        #Change size to add Code and Name
        can.setFont('Roboto-Mono', 9)
        can = pdf_functions.add_oneline_text(can=can, text=procedure['name'], pos=name_pos, camp_name=f'{camp_name} Procedure Name', len_max=50, len_min=7)
        can = pdf_functions.add_oneline_intnumber(can=can, number=procedure['quant'], pos=quant_pos, camp_name=f'{camp_name} Procedure Quantity', len_max=8, len_min=1, value_min=1, value_max=99999999)

        return can
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquanto adicionava o procedimento (procedure)')


def add_secondary_procedures(can:canvas.Canvas, procedures:list) -> canvas.Canvas:
    """Add secondary procedures

    Args:
        can (canvas.Canvas): canvas to use
        procedures (list): list with dicts with procedures

    Returns:
        canvas.Canvas: canvas updated 
    """    
    #verify if the type is list
    try:
        if procedures == None:
            return can
        if type(procedures) != type(list()):
            raise Exception('procedimentos (procedures) devem ser uma lista de dicionarios, exemplo: [{"name":"Procedure Name", "code":"cod124235", "quant":5}, {"name":"Another Procedure", "code":"another12", "quant":1}]')
        if len(procedures) > 5:
            raise Exception('Voce nao pode adicionar mais que 5 procedimentos secundarios')
        
        #Add to cnavas
        cont = 1
        NAME_X_POS = 220
        CODE_X_POS = 36
        QUANT_X_POS = 516
        ypos = 495
        REDUCE_Y = 26
        #Add code fist with upper font
        can.setFont('Roboto-Mono', 10)
        # Add all procedures
        for proc in procedures:
            can = add_procedure(can=can, procedure=proc, code_pos=(CODE_X_POS, ypos), name_pos=(NAME_X_POS, ypos), quant_pos=(QUANT_X_POS, ypos), camp_name=f'({cont}) second procedures')
            ypos -= REDUCE_Y

        return can

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquanto adicionava procedimentos secundarios')
