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
        return super().get_output()

