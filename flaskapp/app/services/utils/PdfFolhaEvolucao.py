from app.env import FONT_DIRECTORY, BOLD_FONT_DIRECTORY,TEMPLATE_FOLHA_EVOLUCAO_DIRECTORY, WRITE_FOLHA_EVOLUCAO_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfWriter, PdfReader
import datetime


class PdfFolhaEvolucao(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_FOLHA_EVOLUCAO_DIRECTORY
    WRITE_DIRECTORY = WRITE_FOLHA_EVOLUCAO_DIRECTORY

    def __init__(self) -> None:

        self.packet = io.BytesIO()
        # Create canvas and add data
        page_size_points = (842, 595)
        self.can = canvas.Canvas(self.packet, pagesize=page_size_points)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        pdfmetrics.registerFont(TTFont('Roboto-Condensed-Bold', BOLD_FONT_DIRECTORY))
        self.can.setFont('Roboto-Condensed-Bold', 20)
    

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
        

    def add_medical_nursing_evolution(self, evolution_description:str, responsible:dict, evolution_initial_pos:tuple, responsible_initial_pos:tuple, camp_name:str) -> None:
        """Add a medical evolution to the pdf

        Args:
            evolution_description (str): evolution description
            responsible (dict): Responsible info 
            evolution_initial_pos (tuple): initial evolution description position in pdf
            responsible_initial_pos (tuple): initial responsible info position in pdf
            camp_name (str): Camp name (Medica | De enfermagem)

        Returns:
            None
        """
        self.validate_func_args(function_to_verify=self.add_medical_nursing_evolution, variables_to_verify={'evolution_description':evolution_description, 'responsible':responsible, 'responsible_initial_pos':responsible_initial_pos, 'evolution_initial_pos':evolution_initial_pos, 'camp_name':camp_name})


        # getting data
        name = responsible.get('name')
        crm = responsible.get('professional_document_number')
        crm_uf = responsible.get('professional_document_uf')

        for camp in [name, crm, crm_uf]:
            if camp == None:
                raise Exception('Algum campo do profissional está faltando, o documento precisa do nome, crm e sigla uf do estado do crm')

        professional_info = f"{str(name).strip()} CRM {str(crm).strip()}/{str(crm_uf).strip()}"

        self.add_morelines_text(text=evolution_description, initial_pos=evolution_initial_pos, decrease_ypos=13, camp_name=f'Descricao evolucao {camp_name}', len_max=406, char_per_lines=58)

        self.add_morelines_text(text=professional_info, initial_pos=responsible_initial_pos, decrease_ypos=13, camp_name=f'Informacao do responsavel na evolucao {camp_name}', len_max=99, char_per_lines=49)
        
        return None




