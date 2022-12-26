from app.env import FONT_DIRECTORY, TEMPLATE_EXAM_REQUEST_DIRECTORY, WRITE_EXAM_REQUEST_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfWriter, PdfReader
from math import ceil


class PdfExamRequest(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_EXAM_REQUEST_DIRECTORY
    WRITE_DIRECTORY = WRITE_EXAM_REQUEST_DIRECTORY

    def __init__(self) -> None:

        self.packet = io.BytesIO()
        # Create canvas and add data
        self.can = canvas.Canvas(self.packet, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        self.can.setFont('Roboto-Mono', 10)
    

    def get_output(self) -> PdfWriter:
        """Return a PdfWriter Object to output a file"""
        self.can.save()
        self.packet.seek(0)
        new_pdf = PdfReader(self.packet)
        # read the template pdf 
        template_pdf = PdfReader(open(self.TEMPLATE_DIRECTORY[self.pags_quant-1], "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)
        return output
    
    def add_exams(self, exams:str) -> None:
        """add solicited exams

        Args:
            exams (str): exams

        Returns:
            None
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
            self.pags_quant = ceil(len(exams)/324)
            CHAR_PER_LINES = 108
            broke_lines_times = int(len(exams)/CHAR_PER_LINES)
            current_line = CHAR_PER_LINES
            last_line = 0
            y_position = 649
            cont = 0
            for x in range(self.pags_quant):
                while broke_lines_times >= 0:
                    str_exams = exams[last_line:current_line]
                    self.add_data(data=str_exams, pos=(7, y_position))
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
            return None

        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido enquando adicionava os exames solicitados')