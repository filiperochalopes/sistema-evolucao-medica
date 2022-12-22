from app.env import FONT_DIRECTORY, TEMPLATE_LME_DIRECTORY, WRITE_LME_DIRECTORY

from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfWriter, PdfReader
from ast import literal_eval



class PdfLme(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_LME_DIRECTORY
    WRITE_DIRECTORY = WRITE_LME_DIRECTORY

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
        template_pdf = PdfReader(open(self.TEMPLATE_DIRECTORY, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)
        return output

    def add_filled_by(self, filled_by:list) -> None:
        """add filled by

        Args:
            filled_by (list): list with option, name and document if outro option is choosed

        Returns:
            None
        """    
        self.add_markable_square_and_onelinetext(option=filled_by[0], valid_options=['PACIENTE','MAE', 'RESPONSAVEL', 'MEDICO','OUTRO'], text_options=['OUTRO'], text_pos=(128, 152), options_positions=((227, 166), (277, 166), (354, 166), (486, 166), (40, 152)), camp_name='Filled By option and Name', len_max=42, text=filled_by[1], len_min=5, square_size=(5, 8))
        if filled_by[0].upper() == 'OUTRO':
            filled_by_document = literal_eval(filled_by[2])
            self.add_document_cns_cpf_rg(document=filled_by_document, pos_cpf=(388, 152),camp_name='Filled by', interval='  ')
        return None