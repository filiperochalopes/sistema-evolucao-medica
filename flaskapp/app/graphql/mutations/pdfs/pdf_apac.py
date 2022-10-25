import base64
import datetime
from PyPDF2  import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from flask import Response
from typing import Union
from pdfs import pdf_functions
from pdfs.constants import FONT_DIRECTORY, TEMPLATE_APAC_DIRECTORY, WRITE_APAC_DIRECTORY


def fill_pdf_apac(establishment_solitc_name:str, establishment_solitc_cnes:int, patient_name:str, patient_cns:int, patient_sex:str, patient_birthday:datetime.datetime, patient_adress_city:str, main_procedure_name:str, main_procedure_code:str, main_procedure_quant:int, patient_mother_name:str=None, patient_mother_phonenumber:int=None, patient_responsible_name:str=None, patient_responsible_phonenumber:int=None, patient_adress:str=None, patient_ethnicity:str=None, patient_color:str=None, patient_adressUF:str=None, patient_adressCEP:int=None, document_chart_number:int=None, patient_adress_city_IBGEcode:int=None, procedure_justification_description:str=None, procedure_justification_main_cid10:str=None, procedure_justification_sec_cid10:str=None, procedure_justification_associated_cause_cid10:str=None, procedure_justification_comments:str=None, establishment_exec_name:str=None, establishment_exec_cnes:int=None,prof_solicitor_document:dict=None, prof_solicitor_name:str=None, solicitation_datetime:datetime.datetime=None, autorization_prof_name:str=None, emission_org_code:str=None, autorizaton_prof_document:dict=None, autorizaton_datetime:datetime.datetime=None, signature_datetime:datetime.datetime=None, validity_period_start:datetime.datetime=None, validity_period_end:datetime.datetime=None, secondaries_procedures:list=None) -> Union[PdfWriter, Response]:
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
            c = pdf_functions.add_cns(can=c, cns=patient_cns, pos=(36, 678), camp_name='Patient CNS', interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=main_procedure_code, pos=(36, 542), camp_name='Main Procedure Code', len_max=10, len_min=10, interval='  ')
            if type(c) == type(Response()): return c

            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_oneline_text(can=c, text=establishment_solitc_name, pos=(36, 742), camp_name='Establishment Solict Name', len_max=77, len_min=7)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_name, pos=(36, 702), camp_name='Patient Name', len_max=67, len_min=7)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(423, 699), pos_fem=(456, 699), camp_name='Patient Sex', square_size=(9,9))
            if type(c) == type(Response()): return c

            
            c = pdf_functions.add_datetime(can=c, date=patient_birthday, pos=(315, 678), camp_name='Patient Birthday', hours=False, interval='  ', formated=False)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress_city, pos=(36, 584), camp_name='Patient Adress City', len_max=58, len_min=7)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=main_procedure_name, pos=(220, 542), camp_name='Main Procedure Name', len_max=50, len_min=7)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=main_procedure_quant, pos=(508, 542), camp_name='Main Procedure Quantity', len_max=8, len_min=1, value_min=1, value_max=99999999)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=establishment_solitc_cnes, pos=(468, 742), camp_name='Establishment Solict CNES', len_max=7, len_min=7,value_min=0, value_max=99999999)
            if type(c) == type(Response()): return c
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            c.setFont('Roboto-Mono', 11)
            c = pdf_functions.add_oneline_intnumber(can=c, number=establishment_exec_cnes, pos=(450, 28), camp_name='Establishment Exec CNES', len_max=7, len_min=7,value_min=0, value_max=99999999, interval=' ', nullable=True)
            if type(c) == type(Response()): return c
            c.setFont('Roboto-Mono', 9)
            c = pdf_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(36, 654), camp_name='Patient Mother Name', len_max=67, len_min=7, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_phonenumber(can=c, number=patient_mother_phonenumber, pos=(409, 650), camp_name='Patient Mother Phone Number', nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_responsible_name, pos=(36, 630), camp_name='Patient Responsible Name', len_max=67, len_min=7, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_phonenumber(can=c, number=patient_responsible_phonenumber, pos=(409, 626), camp_name='Patient Responsible Phone Number', nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_adress, pos=(36, 608), camp_name='Patient Adress', len_max=97, len_min=7, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_color, pos=(404, 678), camp_name='Patient Color', len_max=10, len_min=4, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=patient_ethnicity, pos=(470, 678), camp_name='Patient Ehinicity', len_max=17, len_min=4, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_adressCEP, pos=(476, 582), camp_name='Patient Adress CEP', len_max=8, len_min=8, value_min=0, value_max=99999999, nullable=True, interval=' ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=document_chart_number, pos=(483, 702), camp_name='Document Chart Number', len_max=14, len_min=1, value_min=0, value_max=99999999999999, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_intnumber(can=c, number=patient_adress_city_IBGEcode, pos=(370, 582), camp_name='Patient Adress City IBGE code', len_max=7, len_min=7, value_min=0, value_max=9999999, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_UF(can=c, uf=patient_adressUF, pos=(443, 582), camp_name='Patient Adress UF', nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=procedure_justification_description, pos=(36, 344), camp_name='Procedure Justification Description', len_max=55, len_min=4, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=procedure_justification_main_cid10, pos=(352, 344), camp_name='Procedure Justification main CID10', len_max=4, len_min=3, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=procedure_justification_sec_cid10, pos=(420, 344), camp_name='Procedure Justification secondary CID10', len_max=4, len_min=3, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=procedure_justification_associated_cause_cid10, pos=(505, 344), camp_name='Procedure Justification Associated Causes CID10', len_max=4, len_min=3, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=establishment_exec_name, pos=(36, 30), camp_name='Establishment Exec Name', len_max=71, len_min=5, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=prof_solicitor_name, pos=(36, 204), camp_name='Profissional Solicitor Name', len_max=48, len_min=5, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=autorization_prof_name, pos=(36, 136), camp_name='Profissional Authorizator Name', len_max=46, len_min=5, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_oneline_text(can=c, text=emission_org_code, pos=(290, 136), camp_name='Emission Org Code', len_max=16, len_min=2, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_datetime(can=c, date=solicitation_datetime, pos=(310, 204), camp_name='Solicitation Datetime', hours=False, interval='  ', formated=False, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_datetime(can=c, date=autorizaton_datetime, pos=(36, 68), camp_name='Authorization Datetime', hours=False,formated=True, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_datetime(can=c, date=signature_datetime, pos=(154, 68), camp_name='Signature Datetime', hours=False, interval='  ', formated=False, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_datetime(can=c, date=validity_period_start, pos=(402, 66), camp_name='Validity Period Start', hours=False, interval='  ', formated=False, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_datetime(can=c, date=validity_period_end, pos=(492, 66), camp_name='Validity Period End', hours=False, interval='  ', formated=False, nullable=True)
            if type(c) == type(Response()): return c
            c = add_secondary_procedures(can=c, procedures=secondaries_procedures)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_morelines_text(can=c, text=procedure_justification_comments, initial_pos=(36, 318), decrease_ypos= 10, camp_name='Procedura justification Comments', len_max=776, char_per_lines=97, len_min=5, nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=prof_solicitor_document, pos_square_cpf=(103, 180), pos_square_cns=(51,180), pos_cns=(151, 181), pos_cpf=(151, 181),camp_name='Professional Solicitor Document', interval='  ',nullable=True)
            if type(c) == type(Response()): return c
            c = pdf_functions.add_document_cns_cpf_rg(can=c, document=autorizaton_prof_document, pos_square_cpf=(103, 104), pos_square_cns=(51,104), pos_cns=(149, 105), pos_cpf=(151, 105),camp_name='Professional Authorizator Document', interval='  ',nullable=True)
            if type(c) == type(Response()): return c
        
        except:
            return Response('Critical error happen when adding data that can be null to fields', status=500)
        # create a new PDF with Reportlab
        c.save()
        packet.seek(0)
        new_pdf = PdfReader(packet)
        # read the template pdf 
        template_pdf = PdfReader(open(TEMPLATE_APAC_DIRECTORY, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        pdf_functions.write_newpdf(output, WRITE_APAC_DIRECTORY)
        
        with open(WRITE_APAC_DIRECTORY, "rb") as pdf_file:
            pdf_base64_enconded = base64.b64encode(pdf_file.read())

        return pdf_base64_enconded
    except:
        return Response("Error while filling apac", status=500)


def add_secondary_procedures(can:canvas.Canvas, procedures:list) -> Union[canvas.Canvas, Response]:
    #verify if the type is list
    try:
        if procedures == None:
            return can
        if type(procedures) != type(list()):
            return Response('procedures has to be a list of dicts, like: [{"procedure_name":"Procedure Name", "procedure_code":"cod124235", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"another12", "quant":1}]', status=400)
        necessaryKeys = ["procedure_name", "procedure_code", "quant"]
        if len(procedures) > 5:
            return Response('You cannot add more than 5 secondary procedures', status=400)
        for proc in procedures:
            #verify if the item in list is a dict
            if type(proc) != type(dict()):
                return Response('All itens in list has to be a dict', status=400)
            #Verify if the necessary keys are in the dict
            if 'procedure_name' not in proc.keys() or 'procedure_code' not in proc.keys() or "quant" not in proc.keys():
                return Response('Some keys in dict is missing, dict has to have "procedure_name", "procedure_code", "quant"', status=400)
            #Verify if the value in the dics is the needed
            elif type(proc['procedure_name']) != type(str()) or type(proc['procedure_code']) != type(str()) or type(proc["quant"]) != type(int()):
                return Response('The values in the keys "procedure_name", "procedure_code" has to be string and "quant" has to be int', status=400)

        
            #Verify if the dict has more keys than the needed
            for key in proc.keys():
                if key not in necessaryKeys:
                    return Response('The dict can only have 3 keys "procedure_name", "procedure_code", "quant"', status=400)
            
        #Add to cnavas
        cont = 1
        NAME_X_POS = 220
        CODE_X_POS = 36
        QUANT_X_POS = 516
        ypos = 495
        REDUCE_Y = 26
        #Add code fist with upper font
        can.setFont('Roboto-Mono', 10)
        for proc in procedures:
            can = pdf_functions.add_oneline_text(can=can, text=proc['procedure_code'], pos=(CODE_X_POS, ypos), camp_name=f'{cont} Secondary Procedure Code', len_max=10, len_min=10, interval='  ')
            if type(can) == type(Response()): return can
            ypos -= REDUCE_Y

        can.setFont('Roboto-Mono', 9)
        ypos = 495
        for proc in procedures:
            can = pdf_functions.add_oneline_text(can=can, text=proc['procedure_name'], pos=(NAME_X_POS, ypos), camp_name=f'{cont} Secondary procedure name', len_max=54, len_min=7)
            if type(can) == type(Response()): return can
            can = pdf_functions.add_oneline_intnumber(can=can, number=proc['quant'], pos=(QUANT_X_POS, ypos), camp_name=f'{cont} Secondary Procedure Quantity', len_max=8, len_min=1, value_min=1, value_max=99999999)
            if type(can) == type(Response()): return can
            ypos -= REDUCE_Y
        return can
    except: 
        return Response('Unkown error while adding Secondaries Procedures', status=500)
