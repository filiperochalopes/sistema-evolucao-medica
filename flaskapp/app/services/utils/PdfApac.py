from app.env import TEMPLATE_APAC_DIRECTORY, WRITE_APAC_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader


class PdfApac(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_APAC_DIRECTORY
    WRITE_DIRECTORY = WRITE_APAC_DIRECTORY

    def __init__(self) -> None:
        super().__init__(canvas_pagesize=letter)
        self.can.setFont('Roboto-Mono', 10)
    

    def get_output(self) -> PdfWriter:
        return super().get_output()

    def add_procedure(self, procedure:dict, code_pos:tuple, name_pos:tuple, quant_pos:tuple, field_name:str) -> None:
        """Add procedure to canvas

        Args:
            can (canvas.Canvas): canvas to use
            procedure (dict): dict with procedure info
            code_pos (tuple): position of code
            name_pos (tuple): position of name
            quant_pos (tuple): position of quant
            field_name (str): camp name

        Returns:
            None
        """
        try:
            if procedure == None:
                return None
            if type(procedure) != type(dict()):
                raise Exception('procedure deve ser um dicionario, exemplo: {"name":"Procedure Name", "code":"cod124235", "quantity":5}')
            necessaryKeys = ["name", "code", "quantity"]
            #Verify if the necessary keys are in the dict
            if 'name' not in procedure.keys() or 'code' not in procedure.keys() or "quantity" not in procedure.keys():
                raise Exception('Algumas chaves do dicionario estao faltando, o dicionario deve ter as chaves "name", "code", "quantity"')
            #Verify if the value in the dics is the needed
            elif type(procedure['name']) != type(str()) or type(procedure['code']) != type(str()) or type(procedure["quantity"]) != type(int()):
                raise Exception('Os valores das chaves "name", "code" devem ser string e "quantity" deve ser um numero inteiro')
            #Verify if the dict has more keys than the needed
            for key in procedure.keys():
                if key not in necessaryKeys:
                    raise Exception('O dicionario deve ter somente 3 chaves, sendo elas: "name", "code", "quantity"')
            
            ## Add to canvas
            # Change size to add Code
            self.set_font('Roboto-Mono', 10)
            self.add_oneline_text(text=str(procedure['code']).upper(), pos=code_pos, field_name=f'{field_name} Procedure Code', len_max=10, len_min=10, interval='  ')
            #Change size to add Code and Name
            self.set_font('Roboto-Mono', 9)
            self.add_oneline_text(text=str(procedure['name']).upper(), pos=name_pos, field_name=f'{field_name} Procedure Name', len_max=50, len_min=7)
            self.add_oneline_intnumber(number=procedure['quantity'], pos=quant_pos, field_name=f'{field_name} Procedure Quantity', len_max=8, len_min=1, value_min=1, value_max=99999999)

            return None
        
        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido enquanto adicionava o procedimento {procedure}')
    

    def add_secondary_procedures(self, procedures:list) -> None:
        """Add secondary procedures

        Args:
            can (canvas.Canvas): canvas to use
            procedures (list): list with dicts with procedures

        Returns:
            None
        """    
        #verify if the type is list
        try:
            if procedures == None:
                return None
            if type(procedures) != type(list()):
                raise Exception('procedimentos (procedures) devem ser uma lista de dicionarios, exemplo: [{"name":"Procedure Name", "code":"cod124235", "quantity":5}, {"name":"Another Procedure", "code":"another12", "quantity":1}]')
            if len(procedures) > 5:
                raise Exception('Voce nao pode adicionar mais que 5 procedimentos secundarios')
            
            #Add to cnavas
            cont = 1
            NAME_X_POS = 220
            CODE_X_POS = 36
            QUANT_X_POS = 516
            ypos = 495
            REDUCE_Y = 26
            #Add code fist with upper font
            self.set_font('Roboto-Mono', 10)
            # Add all procedures
            for proc in procedures:
                self.add_procedure(procedure=proc, code_pos=(CODE_X_POS, ypos), name_pos=(NAME_X_POS, ypos), quant_pos=(QUANT_X_POS, ypos), field_name=f'({cont}) second procedures')
                ypos -= REDUCE_Y

            return None

        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido enquanto adicionava procedimentos secundarios')

