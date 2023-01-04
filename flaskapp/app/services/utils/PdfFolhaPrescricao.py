from app.env import TEMPLATE_FOLHA_PRESCRICAO_DIRECTORY, WRITE_FOLHA_PRESCRICAO_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from PyPDF2 import PdfWriter, PdfReader


class PdfFolhaPrescricao(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_FOLHA_PRESCRICAO_DIRECTORY
    WRITE_DIRECTORY = WRITE_FOLHA_PRESCRICAO_DIRECTORY

    def __init__(self) -> None:

        # Create canvas and add data
        page_size_points = (842, 595)
        super().__init__(canvas_pagesize=page_size_points)
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
            CHAR_PER_LINES = 71
            DEFAULT_RECT_HEIGHT = 28
            DEFAULT_DECREASE_Y_POS = 12
            y_text_pos = 511
            for presc in prescriptions:
                # Create text
                prescription_text = f'{cont}.{presc["type"]} {presc["description"]} ({presc["route"]})'.strip()
                # Get quant of lines
                break_lines_quant = int(len(prescription_text)/CHAR_PER_LINES)
                # Get rect heigt with the total lines will need
                rect_height = DEFAULT_RECT_HEIGHT + (break_lines_quant * DEFAULT_DECREASE_Y_POS)
                rect_y_pos = int(y_text_pos - 11) - int(break_lines_quant * DEFAULT_DECREASE_Y_POS)
                if cont % 2 != 0:
                    self.add_rect_prescription_background(pos=(24, rect_y_pos), height=rect_height)
                self.add_morelines_text(text=prescription_text, initial_pos=(28, y_text_pos), decrease_ypos=DEFAULT_DECREASE_Y_POS, camp_name=f'{cont} Prescription', len_max=4032, char_per_lines=CHAR_PER_LINES)

                # New y pos
                y_text_pos = rect_y_pos - 20
                cont += 1
                # Verify if the document is full
                if rect_y_pos < 100:
                    raise Exception('The data reached the end of the document')

            return None

        except Exception as error:
            raise error
        except:
            raise Exception('Erro desconhecido enquanto adicionava prescricoes')

    
    def create_professional_info_text(self, professional:dict, nullable:bool=True):
        """Create professional info string.
        Example: "Responsavel Medico {name} CRM {number}/{uf}"

        Args:
            professional (dict): Dict with professioanl info
        """

        self.validate_func_args(function_to_verify=self.create_professional_info_text, variables_to_verify={'professional':professional, 'nullable':nullable})

        # getting data
        name = professional.get('name')
        crm = professional.get('professional_document_number')
        crm_uf = professional.get('professional_document_uf')

        if not nullable:
            # if any camp can be null, the function will check all variables and return a Exception if is missing
            for camp in [name, crm, crm_uf]:
                if camp == None:
                    raise Exception('Algum campo do profissional está faltando, o documento precisa do nome, crm e sigla uf do estado do crm')

        prof_info = f"Responsável Médico {str(name).strip()} CRM {str(crm).strip()}/{str(crm_uf).strip()}"

        return prof_info



