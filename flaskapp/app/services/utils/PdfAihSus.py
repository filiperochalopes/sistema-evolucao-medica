from app.env import FONT_DIRECTORY, TEMPLATE_AIH_SUS_DIRECTORY, WRITE_AIH_SUS_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont


class PdfAihSus(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_AIH_SUS_DIRECTORY
    WRITE_DIRECTORY = WRITE_AIH_SUS_DIRECTORY

    def __init__(self):
        self.packet = io.BytesIO()
        # Create canvas and add data
        self.can = canvas.Canvas(self.packet, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        self.can.setFont('Roboto-Mono', 9)


    

if __name__ == '__main__':
    bah = PdfAihSus()
    bah.add_data('testando', pos=(34, 32))
    print(bah)

def test_class():
    bah = PdfAihSus()
    bah.add_data('NOVO DATOOOO', pos=(34, 32))
    bah.write_newpdf()
    print(bah)
    assert type(bah) == 'str'