from app.env import FONT_DIRECTORY, TEMPLATE_FOLHA_PRESCRICAO_DIRECTORY, WRITE_FOLHA_PRESCRICAO_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfWriter, PdfReader
from reportlab.lib.colors import pink, green


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
        self.can.setFont('Roboto-Mono', 12)
    

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

    def add_rect_prescription_background(self, pos:tuple,width:int=789, height:int=28) -> None:
        """Add the gray rectangle in prescription background

        Args:
            pos (tuple): position (x, y)
            width (int): rectangle width
            height (int): rectangle height
        """
        #Change fill color do draw rect
        self.can.setFillColorRGB(.9215, .9215, .9215, 1)
        self.can.rect(pos[0], pos[1], width=width, height=height, stroke=0, fill=1)
        #Change fill color to black
        self.can.setFillColorRGB(0, 0, 0, 1)

        return None

    def add_prescriptions(self, prescriptions:list):
        """Add prescriptions to pdf

        Args:
            prescriptions (list): list with prescriptions
        """        
        try:
            self.validate_func_args(function_to_verify=self.add_prescriptions, variables_to_verify={'prescriptions':prescriptions})

            cont = 1
            CHAR_PER_LINES = 108
            DEFAULT_RECT_HEIGHT = 28
            y_text_pos = 511
            for presc in prescriptions:
                # Create text
                prescription_text = f'{cont}.{presc["description"]}'.strip()
                # Get quant of lines
                break_lines_quant = int(len(prescription_text)/CHAR_PER_LINES)
                # Get rect heigt with the total lines will need
                rect_height = DEFAULT_RECT_HEIGHT + (break_lines_quant * 12)
                rect_y_pos = int(y_text_pos - 11) - int(break_lines_quant * 12) 
                self.add_rect_prescription_background(pos=(24, rect_y_pos), height=rect_height)
                self.add_morelines_text(text=prescription_text, initial_pos=(28, y_text_pos), decrease_ypos=12, camp_name=f'{cont} Prescription', len_max=4032, char_per_lines=CHAR_PER_LINES)

                cont += 1

            
            return None

        except Exception as error:
            raise error
        except:
            raise Exception('Erro desconhecido enquanto adicionava prescricoes')