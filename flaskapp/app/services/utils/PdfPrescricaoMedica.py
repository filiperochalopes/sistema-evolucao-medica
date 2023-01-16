from app.env import TEMPLATE_PRESCRICAO_MEDICA_DIRECTORY, WRITE_PRESCRICAO_MEDICA_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from PyPDF2 import PdfWriter, PdfReader


class PdfPrescricaoMedica(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_PRESCRICAO_MEDICA_DIRECTORY
    WRITE_DIRECTORY = WRITE_PRESCRICAO_MEDICA_DIRECTORY

    def __init__(self) -> None:

        # Create canvas and add data
        page_size_points = (841.92, 595.2)
        super().__init__(canvas_pagesize=page_size_points)
        self.can.setFont('Roboto-Mono', 12)
    

    def get_output(self) -> PdfWriter:
        return super().get_output()
    
    
    def add_prescription(self, prescription:list) -> None:
        """add prescription to database

        Args:
            precription (list): list of dicts
        Returns:
            None
        """    
        #verify if the type is list
        if type(prescription) != type(list()):
            raise Exception('prescription deve ser uma lista de dicionarios, exemplo: [{"medicine_name":"Dipirona 500mg", "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}, {"medicine_name":"Metocoplamina 10mg", "amount":"6 comprimidos", "use_mode":"1 comprimido, via oral, de 8/8h por 2 dias"}]')
        NECESSARY_KEYS = ["medicine_name", "amount", "use_mode"]
        totalChar = 0
        #Add , in the end to evade errors
        for presc in prescription:
            #verify if the item in list is a dict
            if type(presc) != type(dict()):
                raise Exception('Todos os itens na lista de prescricao devem ser dicionarios')
            #Verify if the necessary keys are in the dict
            if 'medicine_name' not in presc.keys() or 'amount' not in presc.keys() or "use_mode" not in presc.keys():
                raise Exception('Algumas chaves do dicionário estao faltando, o dicionario deve ter as chaves "medicine_name", "amount", "use_mode"')
            #Verify if the value in the dics is str
            elif type(presc['medicine_name']) != type(str()) or type(presc['amount']) != type(str()) or type(presc["use_mode"]) != type(str()):
                raise Exception('Os valores nas chaves "medicine_name", "amount", "use_mode" devem ser strings')
            #verify if medicine_name and amount together isnt bigger than 1 line (61 characters)
            elif len(presc['medicine_name'].strip() + presc['amount'].strip()) > 61:
                raise Exception('"medicine_name" e "amount" juntas nao podem ultrapassar 61 caracteres')
            #Verify id use_mode isnt bigger than 3 lines (244 characters)
            elif len(presc['use_mode'].strip()) > 244:
                raise Exception('"use_mode" nao pode ultrapassar 244 caracteres')
            #Verify if the dict has more keys than the needed
            for key in presc.keys():
                if key not in NECESSARY_KEYS:
                    raise Exception('O dicionario pode ter somente 3 chaves, sendo elas: "medicine_name", "amount", "use_mode"')
            #calculate the total lenght of use_mode
            totalChar += len(presc['use_mode'].strip())
        # Verify if user_mode total lenght and the 2 line that every medicine and amount need isnt bigger than the total of de document
        if totalChar + (61 * len(prescription)) == 2501:
            raise Exception('O total do docmuento nao pode ultrapassar 2501 caracteres. Lembre-se que 1 linha inteira (61 caracteres) sao destinadas ao nome do medicamento e a quantidade')

        yposition = 475
        for presc in prescription:
            medicine_name = presc['medicine_name'].strip()
            amount = presc['amount'].strip()
            use_mode = presc['use_mode'].strip()
            str_use_mode = ''
            CHAR_PER_LINES = 61
            broke_lines_times = int(len(use_mode)/CHAR_PER_LINES)
            current_line = CHAR_PER_LINES
            last_line = 0
            #Discover how many . dots hhas to be between medicinename and amount
            dot_quant = 61 - len(medicine_name + amount)
            str_title = medicine_name + '.' * dot_quant + amount
            #Add medicinename and amount
            self.add_data(data=str_title, pos=(22, yposition))
            self.add_data(data=str_title, pos=(472, yposition))
            yposition -= 10
            # Making the line break whem has 61 charater in a line
            while broke_lines_times >= 0:
                if yposition <= 70:
                    raise Exception('Voce chegou ao limite do documento, reduza o numero de prescricoes')
                str_use_mode = use_mode[last_line:current_line]
                self.add_data(data=str_use_mode, pos=(22, yposition))
                self.add_data(data=str_use_mode, pos=(472, yposition))
                last_line = current_line
                current_line += CHAR_PER_LINES
                broke_lines_times -= 1
                yposition -= 10
            yposition -= 10

        del(str_use_mode)
        del(broke_lines_times)
        del(current_line)
        del(last_line)
        del(yposition)
        return None


    def create_professional_info(self, professional:dict, abbreviated:bool=False) -> str:
        """Create professional info merging name, document and date

        Args:
            professional (dict): _description_
            abbreviated (str): abbreviate professioanl name

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """        
        # getting data
        name = professional.get('name')
        document = professional.get('document')
        category = professional.get('category')

        for camp in [name, document, category]:
            if camp == None:
                raise Exception('Algum campo do profissional está faltando, o documento precisa do nome, document e category')

        if category.lower() == 'm':
            doc_type = 'CRM '
        elif category.lower() == 'e':
            doc_type = 'COREM '
        else:
            raise Exception(f'A categoria de profissional {category} nao existe, envie "e" ou "M", sendo "e" para emfermeiros e "m" para medicos')

        if abbreviated:
            name = self.get_abbrevitate_name(name=name)

        professional_info = f"{str(name).strip()} " + doc_type + str(document)

        return str(professional_info)
