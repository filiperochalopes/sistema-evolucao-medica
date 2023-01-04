from app.env import TEMPLATE_RELATORIO_ALTA_DIRECTORY, WRITE_RELATORIO_ALTA_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader



class PdfRelatorioAlta(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_RELATORIO_ALTA_DIRECTORY
    WRITE_DIRECTORY = WRITE_RELATORIO_ALTA_DIRECTORY

    def __init__(self) -> None:

        super().__init__(canvas_pagesize=letter)
        self.can.setFont('Roboto-Mono', 12)
    

    def get_output(self) -> PdfWriter:
        return super().get_output()