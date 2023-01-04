from app.env import TEMPLATE_AIH_SUS_DIRECTORY, WRITE_AIH_SUS_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader


class PdfAihSus(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_AIH_SUS_DIRECTORY
    WRITE_DIRECTORY = WRITE_AIH_SUS_DIRECTORY

    def __init__(self) -> None:
        super().__init__(canvas_pagesize=letter)
        self.can.setFont('Roboto-Mono', 9)
    

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

