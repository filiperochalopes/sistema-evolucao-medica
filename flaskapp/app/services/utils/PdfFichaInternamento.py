from app.env import TEMPLATE_FICHA_INTERN_DIRECTORY, WRITE_FICHA_INTERN_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader


class PdfFichaInternamento(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_FICHA_INTERN_DIRECTORY
    WRITE_DIRECTORY = WRITE_FICHA_INTERN_DIRECTORY

    def __init__(self) -> None:
        super().__init__(canvas_pagesize=letter)
        self.can.setFont('Roboto-Mono', 12)
    

    def get_output(self) -> PdfWriter:
        return super().get_output()