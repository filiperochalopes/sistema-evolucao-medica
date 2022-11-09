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
from app.env import FONT_DIRECTORY, TEMPLATE_LME_DIRECTORY, WRITE_LME_DIRECTORY

from app.graphql import mutation
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def fill_pdf_lme(establishment_solitc_name:str, establishment_solitc_cnes:int, patient_name:str, patient_mother_name:str, patient_weight:int, patient_height:int, cid_10:str, anamnese:str, prof_solicitor_name:str, solicitation_datetime:datetime.datetime, prof_solicitor_document:dict, capacity_attest:list, filled_by:list, patient_ethnicity:list, previous_treatment:list, diagnostic:str=None, patient_document:dict=None, patient_email:str=None, contacts_phonenumbers:list=None, medicines:list=None) -> Union[bytes, Response]:
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
        medicines (list, optional): list with dicts eg: [{"medicine_name":lenght_test[:60], "quant_1month":"20 comp", "quant_2month":"15 comp", "quant_3month":"5 comp"}] . Defaults to None.

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
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_weight, pos=(485, 628), camp_name='Patient Weight', len_max=3, len_min=1,value_min=1, value_max=999, interval='   ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_height, pos=(485, 602), camp_name='Patient Height', len_max=3, len_min=1,value_min=1, value_max=999, interval='   ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=cid_10, pos=(34, 455), camp_name='cid_10', len_max=4, len_min=3, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_datetime(can=c, date=solicitation_datetime, pos=(292, 222), camp_name='Solicitation Datetime', hours=False, interval='   ', formated=False)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=prof_solicitor_document, pos_square_cpf=(41, 195), pos_square_cns=(84,194), pos_cns=(129, 195), pos_cpf=(129, 195),camp_name='Professional Solicitor Document', interval='  ', square_size=(5, 8))
            if type(c) == type(Response()): return c


            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_oneline_text(can=c, text=establishment_solitc_name, pos=(206, 658), camp_name='Establishment Solicit Name', len_max=65, len_min=8)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_name, pos=(36, 628), camp_name='Patient Name', len_max=79, len_min=7)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(36, 602), camp_name='Patient Mother Name', len_max=79, len_min=7)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_morelines_text(can=c, text=anamnese, initial_pos=(36, 430), decrease_ypos= 10, camp_name='Anamnese', len_max=485, char_per_lines=97, len_min=5)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=prof_solicitor_name, pos=(36, 224), camp_name='Professional Solicitor Name', len_max=45, len_min=8)
            if type(c) == type(Response()): return c
            if type(capacity_attest) != type(list()) or len(capacity_attest) > 2:
                c = Response('Cappacity Attest has to be a list with 2 itens', status=400)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square_and_onelinetext(can=c, option=capacity_attest[0], valid_options=['SIM','NAO'], text_options=['SIM'], text_pos=(308, 268), options_positions=((79, 271), (42,270)), camp_name='Capacity Attest', len_max=46, text=capacity_attest[1], len_min=5, square_size=(5, 8))
            if type(c) == type(Response()): return c
            if type(filled_by) != type(list()) or len(filled_by) > 3:
                c = Response('filled_by has to be a list with 3 itens', status=400)
            if type(c) == type(Response()): return c
            c = add_filled_by(can=c, filled_by=filled_by)
            if type(c) == type(Response()): return c
            if type(patient_ethnicity) != type(list()) or len(patient_ethnicity) > 2:
                c = Response('patient_ethnicity has to be a list with 2 itens', status=400)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square_and_onelinetext(can=c, option=patient_ethnicity[0], valid_options=['BRANCA','PRETA', 'PARDA', 'AMARELA', 'INDIGENA', 'SEMINFO'], text_options=['BRANCA','PRETA', 'PARDA', 'AMARELA', 'INDIGENA'], text_pos=(192, 108), options_positions=((40, 121), (40, 108),(40, 93),(94, 118), (94, 106),(94, 93)), camp_name='Patietn Ethinicity', len_max=31, text=patient_ethnicity[1], len_min=4, square_size=(5, 8))
            if type(c) == type(Response()): return c
            if type(previous_treatment) != type(list()) or len(previous_treatment) > 2:
                c = Response('previous_treatment has to be a list with 2 itens', status=400)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_markable_square_and_morelinestext(can=c, option=previous_treatment[0], valid_options=['SIM','NAO'],text_options=['SIM'], text_pos=(100, 355), options_positions=((40, 355), (40, 337)), camp_name='Previous Treatment', len_max=170, text=previous_treatment[1], len_min=4, square_size=(5, 8),char_per_lines=85, decrease_ypos=15)
            if type(c) == type(Response()): return c

        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=patient_document, pos_square_cpf=(40, 66), pos_square_cns=(84,66), pos_cns=(129, 66), pos_cpf=(129, 66),camp_name='Patient Document', interval='  ', nullable=True, square_size=(5, 8))
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=diagnostic, pos=(105, 455), camp_name='Diagnostic', len_max=84, len_min=4, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_email, pos=(36, 42), camp_name='Patient Email', len_max=62, len_min=8, nullable=True)
            if type(c) == type(Response()): return c
            c = add_contat_phonenumbers(can=c, phonenumbers=contacts_phonenumbers, pos=(384, 116), interval='  ')
            if type(c) == type(Response()): return c
            c = add_medicines(can=c, medicines=medicines)
            if type(c) == type(Response()): return c


        except:
            return Response('Critical error happen when adding data that can be null to fields', status=500)
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

        return pdf_base64_enconded
    except:
        return Response("Error while filling aih sus", status=500)


def add_contat_phonenumbers(can:canvas.Canvas, phonenumbers:list, pos:tuple, interval:str) -> Union[canvas.Canvas, Response]:
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
            return Response('contacts phonenumbers has to be list', status=400)
        elif len(phonenumbers) > 2:
            return Response('Contats phonenumbers list cannot has more than 2 phonenumbers', status=400)

        #Verify if all numbers are int and has 10 digits
        for number in phonenumbers:
            if type(number) != type(int()):
                return Response('Contats phonenumbers has to be a int', status=400)
            elif len(str(number)) != 10:
                return Response('Contats phonenumbers must have 10 digits', status=400)

        cont = 1
        for number in phonenumbers:
            number = str(number)
            formated_number = number[:2] + ' ' + number[2:]
            can = pdf_functions.add_oneline_text(can=can, text=formated_number, pos=(pos[0], pos[1]), camp_name=f'Phone Number {cont}', len_max=11, len_min=11, nullable=True, interval=interval)
            if type(can) == type(Response()): return can
            cont += 1
            pos = (pos[0], pos[1]-20)

        return can
    except:
        return Response('Unknow erro when adding contact phone numbers', status=500)


def add_medicines(can:canvas.Canvas, medicines:list) -> Union[canvas.Canvas, Response]:
    """Add medicines to canvas

    Args:
        can (canvas.Canvas): canvas to use
        medicines (list): list with dict to with medicines, eg: [{"medicine_name":"Procedure Name", "quant_1month:"cod124235", "quant_2month":"123", "quant_3month":"quant"}]

    Returns:
        Union[canvas.Canvas, Response]: canvas updated or Response with error
    """    
        
    try:
        if medicines == None:
                return can
        if type(medicines) != type(list()):
            return Response('medicines has to be a list of dicts, like: [{"medicine_name":"Procedure Name", "quant_1month:"cod124235", "quant_2month":"123", "quant_3month":"quant"}]', status=400)
        necessaryKeys = ["medicine_name", "quant_1month", "quant_2month", "quant_3month"]
        if len(medicines) > 5:
                return Response('You cannot add more than 5 secondary medicines', status=400)
        for med in medicines:
            #verify if the item in list is a dict
            if type(med) != type(dict()):
                return Response('All itens in list has to be a dict', status=400)
            #Verify if the necessary keys are in the dict
            if 'medicine_name' not in med.keys() or 'quant_1month' not in med.keys() or "quant_2month" not in med.keys() or "quant_3month" not in med.keys():
                return Response('Some keys in dict is missing, dict has to have "medicine_name", "quant_1month", "quant_2month", "quant_3month"', status=400)
            #Verify if the value in the dics is the needed
            elif type(med['medicine_name']) != type(str()) or type(med['quant_1month']) != type(str()) or type(med['quant_2month']) != type(str()) or type(med['quant_3month']) != type(str()):
                return Response('The values in the keys "medicine_name", "quant_1month", "quant_2month", "quant_3month" has to be string', status=400)
            #Verify if the dict has more keys than the needed
            for key in med.keys():
                if key not in necessaryKeys:
                    return Response('The dict can only have 4 keys "medicine_name", "quant_1month", "quant_2month", "quant_3month"', status=400)

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
                if type(can) == type(Response()): return can
                can = pdf_functions.add_oneline_text(can=can, text=med['quant_1month'], pos=(MONTH1_X_POS, ypos), camp_name=f'{cont} Medicine month1 quant', len_max=9, len_min=1)
                if type(can) == type(Response()): return can
                can = pdf_functions.add_oneline_text(can=can, text=med['quant_2month'], pos=(MONTH2_X_POS, ypos), camp_name=f'{cont} Medicine month2 quant', len_max=9, len_min=1)
                if type(can) == type(Response()): return can
                can = pdf_functions.add_oneline_text(can=can, text=med['quant_3month'], pos=(MONTH3_X_POS, ypos), camp_name=f'{cont} Medicine month3 quant', len_max=8, len_min=1)
                if type(can) == type(Response()): return can

                ypos -= REDUCE_Y
            return can
    except: 
        return Response('Unkown error while adding Medicines', status=500)


def add_filled_by(can:canvas.Canvas, filled_by:list) -> Union[canvas.Canvas, Response]:
    """add filled by

    Args:
        can (canvas.Canvas): canvas to use
        filled_by (list): list with option, name and document if outro option is choosed

    Returns:
        Union[canvas.Canvas, Response]: canvas updated or response with error
    """    
    can = pdf_functions.add_markable_square_and_onelinetext(can=can, option=filled_by[0], valid_options=['PACIENTE','MAE', 'RESPONSAVEL', 'MEDICO','OUTRO'], text_options=['OUTRO'], text_pos=(128, 152), options_positions=((227, 166), (277, 166), (354, 166), (486, 166), (40, 152)), camp_name='Filled By option and Name', len_max=42, text=filled_by[1], len_min=5, square_size=(5, 8))
    if type(can) == type(Response()): return can
    if filled_by[0].upper() == 'OUTRO':
        can = pdf_functions.add_document_cns_cpf_rg(can=can, document=filled_by[2], pos_cpf=(388, 152),camp_name='Filled by CPF', interval='  ')
    return can

