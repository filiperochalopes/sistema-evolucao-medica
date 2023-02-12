from app.env import TEMPLATE_LME_DIRECTORY, WRITE_LME_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader
from ast import literal_eval



class PdfLme(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_LME_DIRECTORY
    WRITE_DIRECTORY = WRITE_LME_DIRECTORY

    def __init__(self) -> None:
        super().__init__(canvas_pagesize=letter)
        self.can.setFont('Roboto-Mono', 10)
    

    def get_output(self) -> PdfWriter:
        return super().get_output()

    def add_filled_by(self, filled_by:list) -> None:
        """add filled by

        Args:
            filled_by (list): list with option, name and document if outro option is choosed

        Returns:
            None
        """    
        self.add_markable_square_and_onelinetext(option=filled_by[0], valid_options=['PACIENTE','MAE', 'RESPONSAVEL', 'MEDICO','OUTRO'], text_options=['OUTRO'], text_pos=(128, 152), options_positions=((227, 166), (277, 166), (354, 166), (486, 166), (40, 152)), camp_name='Filled By option and Name', len_max=42, text=filled_by[1], len_min=5, square_size=(5, 8))
        if filled_by[0].upper() == 'OUTRO':
            filled_by_document = literal_eval(filled_by[2])
            self.add_document_cns_cpf_rg(document=filled_by_document, pos_cpf=(388, 152),camp_name='Filled by', interval='  ')
        return None

        
    def add_contact_phonenumbers(self, phonenumbers:list, pos:tuple, interval:str) -> None:
        """Add contact numbers

        Args:
            phonenumbers (list): list with phone numbers
            pos (tuple): position
            interval (str): interval between data

        Returns:
            None
        """    
            
        try:
            if phonenumbers == None:
                return None
            elif type(phonenumbers) != type(list()):
                raise Exception('Numeros de telefone de contatos (contacts phonenumbers) deve ser uma lista')
            elif len(phonenumbers) > 2:
                raise Exception('A lista de Numeros de telefone de contatos (contacts phonenumbers) pode ter no maximo 2 numeros')

            #Verify if all numbers are str and has 10 digits
            for number in phonenumbers:
                if type(number) != type(str()):
                    raise Exception('Numeros de telefone de contatos devem ser string')
                elif len(number) != 10:
                    raise Exception('Numeros de telefone de contatos devem ter 10 digitos')

            cont = 1
            for number in phonenumbers:
                formated_number = number[:2] + ' ' + number[2:]
                self.add_oneline_text(text=formated_number, pos=(pos[0], pos[1]), camp_name=f'Numero de telefone de contato {cont}', len_max=11, len_min=11, nullable=True, interval=interval)
                cont += 1
                pos = (pos[0], pos[1]-20)

            return None

        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido enquanto adicionava numeros de telefone de contatos')

        
    def add_medicines(self, medicines:list) -> None:
        """Add medicines to canvas

        Args:
            medicines (list): list with dict to with medicines, eg: [{"medicine_name":"Procedure Name", "quant_1_month:"cod124235", "quant_2_month":"123", "quant_3_month":"quant"}]

        Returns:
            None
        """    
            
        try:
            if medicines == None:
                    return None
            if type(medicines) != type(list()):
                raise Exception('medicines (medicamentos) deve ser uma lista de dicionarios, exemplo: [{"medicine_name":"Procedure Name", "quant_1_month:"cod124235", "quant_2_month":"123", "quant_3_month":"quant"}]')
            necessaryKeys = ["medicine_name", "quant_1_month", "quant_2_month", "quant_3_month"]
            if len(medicines) > 5:
                    raise Exception('Você nao pode adicionar mais que 5 medicamentos secundarios')
            for med in medicines:
                #verify if the item in list is a dict
                if type(med) != type(dict()):
                    raise Exception('Todos os itens da lista de medicamentos devem ser dicionarios')
                #Verify if the necessary keys are in the dict
                if 'medicine_name' not in med.keys() or 'quant_1_month' not in med.keys() or "quant_2_month" not in med.keys() or "quant_3_month" not in med.keys():
                    raise Exception('Algumas chaves estao faltado no dicionarios, o dicionario deve ter as chaves: "medicine_name", "quant_1_month", "quant_2_month", "quant_3_month"')
                #Verify if the value in the dics is the needed
                elif type(med['medicine_name']) != type(str()) or type(med['quant_1_month']) != type(str()) or type(med['quant_2_month']) != type(str()) or type(med['quant_3_month']) != type(str()):
                    raise Exception('Os valores nas chaves "medicine_name", "quant_1_month", "quant_2_month", "quant_3_month" devem ser strings')
                #Verify if the dict has more keys than the needed
                for key in med.keys():
                    if key not in necessaryKeys:
                        raise Exception('O dicionario pode ter somente 4 chaves: "medicine_name", "quant_1_month", "quant_2_month", "quant_3_month"')

                #Add to cnavas
                cont = 1
                NAME_X_POS = 53
                MONTH1_X_POS = 408
                MONTH2_X_POS = 462
                MONTH3_X_POS = 515
                ypos = 556
                REDUCE_Y = 18

                for med in medicines:
                    self.add_oneline_text(text=med['medicine_name'], pos=(NAME_X_POS, ypos), camp_name=f'{cont} Medicine name', len_max=65, len_min=4)
                    self.add_oneline_text(text=med['quant_1_month'], pos=(MONTH1_X_POS, ypos), camp_name=f'{cont} Medicine month1 quant', len_max=9, len_min=1)
                    self.add_oneline_text(text=med['quant_2_month'], pos=(MONTH2_X_POS, ypos), camp_name=f'{cont} Medicine month2 quant', len_max=9, len_min=1)
                    self.add_oneline_text(text=med['quant_3_month'], pos=(MONTH3_X_POS, ypos), camp_name=f'{cont} Medicine month3 quant', len_max=8, len_min=1)

                    ypos -= REDUCE_Y
                return None
        
        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido enquanto adicionava medicamentos')
