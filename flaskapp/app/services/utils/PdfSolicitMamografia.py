from app.env import FONT_DIRECTORY, TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY, WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfWriter, PdfReader



class PdfSolicitMamografia(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY
    WRITE_DIRECTORY = WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY

    def __init__(self) -> None:

        self.packet_1 = io.BytesIO()
        # Create canvas and add data
        self.can_1 = canvas.Canvas(self.packet_1, pagesize=letter)
        #Create second canvas
        self.packet_2 = io.BytesIO()
        # Create canvas and add data
        self.can_2 = canvas.Canvas(self.packet_2, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        self.can_1.setFont('Roboto-Mono', 13)
        self.can_2.setFont('Roboto-Mono', 13)
        self.can = self.can_1
    

    def get_output(self) -> PdfWriter:
        """Return a PdfWriter Object to output a file"""
        self.can_1.save()
        self.can_2.save()
        self.packet_1.seek(0)
        self.packet_2.seek(0)
        new_pdf = PdfReader(self.packet_1)
        new_pdf_2 = PdfReader(self.packet_2)
        # read the template pdf 
        template_pdf = PdfReader(open(self.TEMPLATE_DIRECTORY, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        page_2 = template_pdf.pages[1]
        page_2.merge_page(new_pdf_2.pages[0])
        output.add_page(page)
        output.add_page(page_2)
        
        return output
    
    def change_canvas(self) -> None:
        """Change to second canvas to write new data"""
        self.can_1 = self.can
        self.can = self.can_2
        return None