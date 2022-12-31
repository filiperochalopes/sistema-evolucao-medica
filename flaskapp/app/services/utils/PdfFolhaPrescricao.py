from app.env import FONT_DIRECTORY, TEMPLATE_FOLHA_PRESCRICAO_DIRECTORY, WRITE_FOLHA_PRESCRICAO_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfWriter, PdfReader


class PdfFolhaPrescricao(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_FOLHA_PRESCRICAO_DIRECTORY
    WRITE_DIRECTORY = WRITE_FOLHA_PRESCRICAO_DIRECTORY

    def __init__(self) -> None:

        self.packet = io.BytesIO()
        # Create canvas and add data
        page_size_points = (842, 595)
        self.can = canvas.Canvas(self.packet, pagesize=page_size_points)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        self.can.setFont('Roboto-Mono', 15)
    

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