import datetime
from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from math import ceil
from typing import Union
from app.services.utils import pdf_functions
from app.env import FONT_DIRECTORY, TEMPLATE_EXAM_REQUEST_DIRECTORY, WRITE_EXAM_REQUEST_DIRECTORY
from app.services.utils.PdfExamRequest import PdfExamRequest


def func_generate_pdf_exam_request(patient_name:str, patient_cns:str, patient_birthday:datetime.datetime, patient_adress:str, solicitation_reason:str,
exams:str, prof_solicitor_name:str, solicitation_datetime:datetime.datetime,prof_authorized_name:str=None, autorization_datetime:datetime.datetime=None, document_pacient_date:datetime.datetime=None, document_pacient_name:str=None) -> str:
    """fill pdf exam request (Solicitacao de exames e procedimentos)

    Args:
        patient_name (str): patient_name
        patient_cns (str): patient_cns
        patient_birthday (datetime.datetime): patient_birthday
        patient_adress (str): patient_adress
        solicitation_reason (str): solicitation_reason
        exams (str): text with exams, this is what extends pdf size to fill all exams
        prof_solicitor_name (str): prof_solicitor_name
        solicitation_datetime (datetime.datetime): solicitation_datetime
        prof_authorized_name (str, optional): prof_authorized_name. Defaults to None.
        autorization_datetime (datetime.datetime, optional): autorization_datetime. Defaults to None.
        document_pacient_date (datetime.datetime, optional): document_pacient_date. Defaults to None.
        document_pacient_name (str, optional): document_pacient_name. Defaults to None.

    Returns:
        str: Request with pdf in base64
    """

    try:
        pdf = PdfExamRequest()

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
            global pags_quant
            pags_quant = 0
            c, pags_quant = add_exams(canvas=c, exams=exams)
            # verify if c is a error at some point

            pdf.add_exams(exams=exams)
            #Add to multiple pages
            decreaseYpos = 280
            patient_name_ypos = 775
            patient_cns_ypos = 765
            patient_birthday_ypos = 784
            solicitation_datetime_ypos = 572
            patient_adress_ypos = 734
            solicitation_reason_ypos = 690
            prof_solicitor_ypos = 595
            for x in range(pags_quant):
                c = pdf_functions.add_oneline_text(can=c, text=patient_name, pos=(7, patient_name_ypos), camp_name='Patient Name', len_max=70, len_min=7)
                c = pdf_functions.add_cns(can=c, cns=patient_cns, pos=(450, patient_cns_ypos), camp_name='Patient CNS',formated=True)
                c = pdf_functions.add_datetime(can=c, date=patient_birthday, pos=(441, patient_birthday_ypos), camp_name='Patient Birthday', hours=False, formated=True)
                c = pdf_functions.add_morelines_text(can=c, text=patient_adress, initial_pos=(7, patient_adress_ypos), decrease_ypos=10, camp_name='Patient Adress', len_max=216, len_min=7, char_per_lines=108)
                c = pdf_functions.add_morelines_text(can=c, text=solicitation_reason, initial_pos=(7, solicitation_reason_ypos), decrease_ypos=10, camp_name='Solicitation Reason', len_max=216, len_min=7, char_per_lines=108)
                c = pdf_functions.add_oneline_text(can=c, text=prof_solicitor_name, pos=(7, prof_solicitor_ypos), camp_name='Professional Solicitor Name', len_max=29, len_min=7)
                c = pdf_functions.add_datetime(can=c, date=solicitation_datetime, pos=(30, solicitation_datetime_ypos), camp_name='Solicitation Datetime', hours=False, formated=True)

                #Decrese ypos in all lines to complete the page
                patient_name_ypos -= decreaseYpos
                patient_cns_ypos -= decreaseYpos
                patient_birthday_ypos -= decreaseYpos
                patient_adress_ypos -= decreaseYpos
                solicitation_reason_ypos -= decreaseYpos
                prof_solicitor_ypos -= decreaseYpos
                solicitation_datetime_ypos -= decreaseYpos

        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados obrigadorios')

        #Adding data that can be null
        try:
            prof_authorized_ypos = 595
            document_pacient_name_ypos = 605
            autorization_datetime_ypos = 572
            document_pacient_date_ypos = 572
            for x in range(pags_quant):
                c = pdf_functions.add_oneline_text(can=c, text=prof_authorized_name, pos=(174, prof_authorized_ypos), camp_name='Professional Authorized Name', len_max=29, len_min=7, nullable=True)
                c = pdf_functions.add_oneline_text(can=c, text=document_pacient_name, pos=(340, document_pacient_name_ypos), camp_name='Document Pacient Name', len_max=46, len_min=7, nullable=True)
                c = pdf_functions.add_datetime(can=c, date=autorization_datetime, pos=(195, autorization_datetime_ypos), camp_name='Authorization Datetime', hours=False, formated=True, nullable=True)
                c = pdf_functions.add_datetime(can=c, date=document_pacient_date, pos=(362, document_pacient_date_ypos), camp_name='Document Pacient Datetime', hours=False, formated=True, nullable=True)

                prof_authorized_ypos -= decreaseYpos
                document_pacient_name_ypos -= decreaseYpos
                autorization_datetime_ypos -= decreaseYpos
                document_pacient_date_ypos -= decreaseYpos

        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados opcionais')
        

        # # create a new PDF with Reportlab
        # c.save()
        # packet.seek(0)
        # new_pdf = PdfReader(packet)
        # # read the template pdf 
        # template_pdf = PdfReader(open(TEMPLATE_EXAM_REQUEST_DIRECTORY[pags_quant-1], "rb"))
        # output = PdfWriter()
        # # add the "watermark" (which is the new pdf) on the existing page
        # page = template_pdf.pages[0]
        # page.merge_page(new_pdf.pages[0])
        # output.add_page(page)

        #pdf_base64_enconded = pdf_functions.get_base64(newpdf=output)

        #Get pdf base64
        pdf_base64_enconded = pdf.get_base64()

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except Exception as error:
        return error
    except:
        return Exception("Erro desconhecido enquanto preenchia o documento de solicitacao de exames (exam request)")

def add_exams(canvas:canvas.Canvas, exams:str) -> canvas.Canvas:
    """add solicited exams

    Args:
        canvas (canvas.Canvas): canvas to use
        exams (str): exams

    Returns:
        canvas :canvas if everthing is allright
    """    
    try:
        if type(exams) != type(str()):
            raise Exception('Exams deve ser string')
        exams = exams.strip()
        if len(exams.strip()) > 972 or len(exams.strip()) < 5:
            raise Exception('Exams deve ter entre 5 e 972 caracteres')
        # Making the line break whem has 105 charater in a line
        str_exams = ''
        #Calculate how many pags will have, ceil function round to upper int
        pags_quant = ceil(len(exams)/324)
        CHAR_PER_LINES = 108
        broke_lines_times = int(len(exams)/CHAR_PER_LINES)
        current_line = CHAR_PER_LINES
        last_line = 0
        y_position = 649
        cont = 0
        for x in range(pags_quant):
            while broke_lines_times >= 0:
                str_exams = exams[last_line:current_line]
                canvas = pdf_functions.add_data(can=canvas, data=str_exams, pos=(7, y_position))
                last_line = current_line
                current_line += CHAR_PER_LINES
                broke_lines_times -= 1
                cont += 1
                if cont%3 == 0:
                    break
                y_position -= 10
            y_position -= 260

        del(str_exams)
        del(broke_lines_times)
        del(current_line)
        del(last_line)
        del(y_position)
        return canvas, pags_quant

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava os exames solicitados')


