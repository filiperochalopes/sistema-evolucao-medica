from app.env import TEMPLATE_FOLHA_PRESCRICAO_DIRECTORY, WRITE_FOLHA_PRESCRICAO_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from PyPDF2 import PdfWriter, PdfReader
import sys

class PdfFolhaPrescricao(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_FOLHA_PRESCRICAO_DIRECTORY
    WRITE_DIRECTORY = WRITE_FOLHA_PRESCRICAO_DIRECTORY

    def __init__(self) -> None:

        # Create canvas and add data
        page_size_points = (842, 595)
        super().__init__(canvas_pagesize=page_size_points)
        self.can.setFont('Roboto-Condensed-Bold', 20)
    

    def get_output(self) -> PdfWriter:
        return super().get_output()


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
            for p in prescriptions:
                # Create text
                print('============== PRESCRIPTION ==============', file=sys.stderr)
                print(p, file=sys.stderr)
                prescription_text = f'{cont}.{p["type"]} {p["description"]} ({p["route"]})'.strip()
                # Get quant of lines
                break_lines_quant = int(len(prescription_text)/CHAR_PER_LINES)
                # Get rect heigt with the total lines will need
                rect_height = DEFAULT_RECT_HEIGHT + (break_lines_quant * DEFAULT_DECREASE_Y_POS)
                rect_y_pos = int(y_text_pos - 11) - int(break_lines_quant * DEFAULT_DECREASE_Y_POS)
                if cont % 2 != 0:
                    self.add_rectangle(pos=(24, rect_y_pos), height=rect_height, width=789)
                self.add_morelines_text(text=prescription_text, initial_pos=(28, y_text_pos), decrease_ypos=DEFAULT_DECREASE_Y_POS, field_name=f'{cont} Prescription', len_max=4032, char_per_lines=CHAR_PER_LINES)

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



