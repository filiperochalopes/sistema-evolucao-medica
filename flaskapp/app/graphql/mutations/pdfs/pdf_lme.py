import base64
import datetime
from PyPDF2 import PdfWriter, PdfReader
import io
from ast import literal_eval
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from typing import Union
from app.utils import pdf_functions
from app.env import FONT_DIRECTORY, TEMPLATE_LME_DIRECTORY, WRITE_LME_DIRECTORY

from app.graphql import mutation
from ariadne import convert_kwargs_to_snake_case

@mutation.field('generatePdf_Lme')
@convert_kwargs_to_snake_case
def fill_pdf_lme(_, info, establishment_solitc_name:str, establishment_solitc_cnes:int, patient_name:str, patient_mother_name:str, patient_weight:int, patient_height:int, cid_10:str, anamnese:str, prof_solicitor_name:str, solicitation_datetime:datetime.datetime, prof_solicitor_document:dict, capacity_attest:list, filled_by:list, patient_ethnicity:list, previous_treatment:list, diagnostic:str=None, patient_document:dict=None, patient_email:str=None, contacts_phonenumbers:list=None, medicines:list=None) -> str:
    """fill pdf lme (laudo de solicitacao, avaliacao e autorizacao e documentos)

    Args:
        establishment_solitc_name (str): establishment_solitc_name
        establishment_solitc_cnes (int): establishment_solitc_cnes
        patient_name (str): patient_name
        patient_mother_name (str): patient_mother_name
        patient_weight (int): patient_weight
        patient_height (int): patient_height
        cid_10 (str): cid_10
        anamnese (str): anamnese
        prof_solicitor_name (str): prof_solicitor_name
        solicitation_datetime (datetime.datetime): solicitation_datetime
        prof_solicitor_document (dict): prof_solicitor_document
        capacity_attest (list): list with option and text, eg: ['nao', 'Responsible Name']
        filled_by (list): lits with option name and document, eg ['MEDICO', 'Other name', {'CPF':28445400070}],
        patient_ethnicity (list): list with options and text (if others options is) eg ['SEMINFO', 'Patient Ethnicity']
        previous_treatment (list): list with option and text if sim option eg ['SIM', 'Previout Theatment']
        diagnostic (str, optional): diagnostic. Defaults to None.
        patient_document (dict, optional): patient_document. Defaults to None.
        patient_email (str, optional): patient_email. Defaults to None.
        contacts_phonenumbers (list, optional): lsit with contacts_phonenumbers . Defaults to None.
        medicines (list, optional): list with dicts eg: [{"medicine_name":lenght_test[:60], "quant_1_month":"20 comp", "quant_2_month":"15 comp", "quant_3_month":"5 comp"}] . Defaults to None.

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
        c.setFont('Roboto-Mono', 10)
        # Writing all data in respective fields
        # not null data

        try:
            c = pdf_functions.add_oneline_intnumber(can=c, number=establishment_solitc_cnes, pos=(38, 658), camp_name='Establishment Solict CNES', len_max=7, len_min=7,value_min=0, value_max=99999999, interval='   ')
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_weight, pos=(485, 628), camp_name='Patient Weight', len_max=3, len_min=1,value_min=1, value_max=999, interval='   ')
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_height, pos=(485, 602), camp_name='Patient Height', len_max=3, len_min=1,value_min=1, value_max=999, interval='   ')
            c = pdf_functions.add_oneline_text(can=c, text=cid_10, pos=(34, 455), camp_name='cid_10', len_max=4, len_min=3, interval='  ')
            c = pdf_functions.add_datetime(can=c, date=solicitation_datetime, pos=(292, 222), camp_name='Solicitation Datetime', hours=False, interval='   ', formated=False)
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=prof_solicitor_document, pos_square_cpf=(41, 195), pos_square_cns=(84,194), pos_cns=(129, 195), pos_cpf=(129, 195),camp_name='Professional Solicitor Document', interval='  ', square_size=(5, 8))


            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_oneline_text(can=c, text=establishment_solitc_name, pos=(206, 658), camp_name='Establishment Solicit Name', len_max=65, len_min=8)
            c = pdf_functions.add_oneline_text(can=c, text=patient_name, pos=(36, 628), camp_name='Patient Name', len_max=79, len_min=7)
            c = pdf_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(36, 602), camp_name='Patient Mother Name', len_max=79, len_min=7)
            c = pdf_functions.add_morelines_text(can=c, text=anamnese, initial_pos=(36, 430), decrease_ypos= 10, camp_name='Anamnese', len_max=485, char_per_lines=97, len_min=5)
            c = pdf_functions.add_oneline_text(can=c, text=prof_solicitor_name, pos=(36, 224), camp_name='Professional Solicitor Name', len_max=45, len_min=8)
            if type(capacity_attest) != type(list()) or len(capacity_attest) > 2:
                raise Exception('Cappacity Attest has to be a list with 2 itens')
            c = pdf_functions.add_markable_square_and_onelinetext(can=c, option=capacity_attest[0], valid_options=['SIM','NAO'], text_options=['SIM'], text_pos=(308, 268), options_positions=((79, 271), (42,270)), camp_name='Capacity Attest', len_max=46, text=capacity_attest[1], len_min=5, square_size=(5, 8))
            if type(filled_by) != type(list()) or len(filled_by) > 3:
                raise Exception('filled_by has to be a list with 3 itens')
            c = add_filled_by(can=c, filled_by=filled_by)
            if type(patient_ethnicity) != type(list()) or len(patient_ethnicity) > 2:
                raise Exception('patient_ethnicity has to be a list with 2 itens')
            c = pdf_functions.add_markable_square_and_onelinetext(can=c, option=patient_ethnicity[0], valid_options=['BRANCA','PRETA', 'PARDA', 'AMARELA', 'INDIGENA', 'SEMINFO', 'INFORMAR'], text_options=['INFORMAR'], text_pos=(192, 108), options_positions=((40, 121), (40, 108),(40, 93),(94, 118), (94, 106),(94, 93), (94, 93)),camp_name='Patietn Ethinicity', len_max=31, text=patient_ethnicity[1], len_min=4, square_size=(5, 8))
            if type(previous_treatment) != type(list()) or len(previous_treatment) > 2:
                raise Exception('previous_treatment has to be a list with 2 itens')
            c = pdf_functions.add_markable_square_and_morelinestext(can=c, option=previous_treatment[0], valid_options=['SIM','NAO'],text_options=['SIM'], text_pos=(100, 355), options_positions=((40, 355), (40, 337)), camp_name='Previous Treatment', len_max=170, text=previous_treatment[1], len_min=4, square_size=(5, 8),char_per_lines=85, decrease_ypos=15)

        except Exception as error:
            return error
        except:
            return Exception('Some error happen when adding not null data to fields')

        #Adding data that can be null
        try:
            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=patient_document, pos_square_cpf=(40, 66), pos_square_cns=(84,66), pos_cns=(129, 66), pos_cpf=(129, 66),camp_name='Patient Document', interval='  ', nullable=True, square_size=(5, 8))
            c = pdf_functions.add_oneline_text(can=c, text=diagnostic, pos=(105, 455), camp_name='Diagnostic', len_max=84, len_min=4, nullable=True)
            c = pdf_functions.add_oneline_text(can=c, text=patient_email, pos=(36, 42), camp_name='Patient Email', len_max=62, len_min=8, nullable=True)
            c = add_contat_phonenumbers(can=c, phonenumbers=contacts_phonenumbers, pos=(384, 116), interval='  ')
            c = add_medicines(can=c, medicines=medicines)

        except Exception as error:
            return error
        except:
            return Exception('Critical error happen when adding data that can be null to fields')
        
        # create a new PDF with Reportlab
        c.save()
        packet.seek(0)
        new_pdf = PdfReader(packet)
        # read the template pdf 
        template_pdf = PdfReader(open(TEMPLATE_LME_DIRECTORY, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        pdf_functions.write_newpdf(output, WRITE_LME_DIRECTORY)
        
        with open(WRITE_LME_DIRECTORY, "rb") as pdf_file:
            pdf_base64_enconded = base64.b64encode(pdf_file.read())

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except:
        return Exception("Error while filling aih sus")


def add_contat_phonenumbers(can:canvas.Canvas, phonenumbers:list, pos:tuple, interval:str) -> canvas.Canvas:
    """Add contact numbers

    Args:
        can (canvas.Canvas): canvas
        phonenumbers (list): list with phone numbers
        pos (tuple): position
        interval (str): interval between data

    Returns:
        Union[canvas.Canvas, Response]: canvas updated or Response with error
    """    
        
    try:
        if phonenumbers == None:
            return can
        elif type(phonenumbers) != type(list()):
            raise Exception('contacts phonenumbers has to be list')
        elif len(phonenumbers) > 2:
            raise Exception('Contats phonenumbers list cannot has more than 2 phonenumbers')

        #Verify if all numbers are str and has 10 digits
        for number in phonenumbers:
            if type(number) != type(str()):
                raise Exception('Contats phonenumbers has to be a str')
            elif len(number) != 10:
                raise Exception('Contats phonenumbers must have 10 digits')

        cont = 1
        for number in phonenumbers:
            formated_number = number[:2] + ' ' + number[2:]
            can = pdf_functions.add_oneline_text(can=can, text=formated_number, pos=(pos[0], pos[1]), camp_name=f'Phone Number {cont}', len_max=11, len_min=11, nullable=True, interval=interval)
            cont += 1
            pos = (pos[0], pos[1]-20)

        return can

    except Exception as error:
        raise error
    except:
        raise Exception(f'Unknow error while adding contact phone numbers')
    


def add_medicines(can:canvas.Canvas, medicines:list) -> canvas.Canvas:
    """Add medicines to canvas

    Args:
        can (canvas.Canvas): canvas to use
        medicines (list): list with dict to with medicines, eg: [{"medicine_name":"Procedure Name", "quant_1_month:"cod124235", "quant_2_month":"123", "quant_3_month":"quant"}]

    Returns:
        Union[canvas.Canvas, Response]: canvas updated or Response with error
    """    
        
    try:
        if medicines == None:
                return can
        if type(medicines) != type(list()):
            raise Exception('medicines has to be a list of dicts, like: [{"medicine_name":"Procedure Name", "quant_1_month:"cod124235", "quant_2_month":"123", "quant_3_month":"quant"}]')
        necessaryKeys = ["medicine_name", "quant_1_month", "quant_2_month", "quant_3_month"]
        if len(medicines) > 5:
                raise Exception('You cannot add more than 5 secondary medicines')
        for med in medicines:
            #verify if the item in list is a dict
            if type(med) != type(dict()):
                raise Exception('All itens in list has to be a dict')
            #Verify if the necessary keys are in the dict
            if 'medicine_name' not in med.keys() or 'quant_1_month' not in med.keys() or "quant_2_month" not in med.keys() or "quant_3_month" not in med.keys():
                raise Exception('Some keys in dict is missing, dict has to have "medicine_name", "quant_1_month", "quant_2_month", "quant_3_month"')
            #Verify if the value in the dics is the needed
            elif type(med['medicine_name']) != type(str()) or type(med['quant_1_month']) != type(str()) or type(med['quant_2_month']) != type(str()) or type(med['quant_3_month']) != type(str()):
                raise Exception('The values in the keys "medicine_name", "quant_1_month", "quant_2_month", "quant_3_month" has to be string')
            #Verify if the dict has more keys than the needed
            for key in med.keys():
                if key not in necessaryKeys:
                    raise Exception('The dict can only have 4 keys "medicine_name", "quant_1_month", "quant_2_month", "quant_3_month"')

            #Add to cnavas
            cont = 1
            NAME_X_POS = 53
            MONTH1_X_POS = 408
            MONTH2_X_POS = 462
            MONTH3_X_POS = 515
            ypos = 556
            REDUCE_Y = 18

            for med in medicines:
                can = pdf_functions.add_oneline_text(can=can, text=med['medicine_name'], pos=(NAME_X_POS, ypos), camp_name=f'{cont} Medicine name', len_max=65, len_min=4)
                can = pdf_functions.add_oneline_text(can=can, text=med['quant_1_month'], pos=(MONTH1_X_POS, ypos), camp_name=f'{cont} Medicine month1 quant', len_max=9, len_min=1)
                can = pdf_functions.add_oneline_text(can=can, text=med['quant_2_month'], pos=(MONTH2_X_POS, ypos), camp_name=f'{cont} Medicine month2 quant', len_max=9, len_min=1)
                can = pdf_functions.add_oneline_text(can=can, text=med['quant_3_month'], pos=(MONTH3_X_POS, ypos), camp_name=f'{cont} Medicine month3 quant', len_max=8, len_min=1)

                ypos -= REDUCE_Y
            return can
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Unknow error while adding Medicines')



def add_filled_by(can:canvas.Canvas, filled_by:list) -> canvas.Canvas:
    """add filled by

    Args:
        can (canvas.Canvas): canvas to use
        filled_by (list): list with option, name and document if outro option is choosed

    Returns:
        Union[canvas.Canvas, Response]: canvas updated or response with error
    """    
    can = pdf_functions.add_markable_square_and_onelinetext(can=can, option=filled_by[0], valid_options=['PACIENTE','MAE', 'RESPONSAVEL', 'MEDICO','OUTRO'], text_options=['OUTRO'], text_pos=(128, 152), options_positions=((227, 166), (277, 166), (354, 166), (486, 166), (40, 152)), camp_name='Filled By option and Name', len_max=42, text=filled_by[1], len_min=5, square_size=(5, 8))
    if filled_by[0].upper() == 'OUTRO':
        filled_by_document = literal_eval(filled_by[2])
        can = pdf_functions.add_document_cns_cpf_rg(can=can, document=filled_by_document, pos_cpf=(388, 152),camp_name='Filled by', interval='  ')
    return can

