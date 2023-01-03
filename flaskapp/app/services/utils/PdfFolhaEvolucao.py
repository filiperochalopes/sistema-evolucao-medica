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
        

    
    def create_professional_info(self, professional:dict, date:str) -> str:
        """Create professional info merging name, document and date

        Args:
            professional (dict): _description_
            date (str): _description_

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

        date_object = datetime.datetime.strptime(date, '%d/%m/%Y %H:%M')
        str_date = str('%02d/%02d/%d %02d:%02d:%02d') % (date_object.day, date_object.month, date_object.year, date_object.hour, date_object.minute, date_object.second)

        if category.lower() == 'm':
            doc_type = 'CRM '
        elif category.lower() == 'e':
            doc_type = 'COREM '
        else:
            raise Exception(f'A categoria de profissional {category} nao existe, envie "e" ou "M", sendo "e" para emfermeiros e "m" para medicos')

        professional_info = f"{str(name).strip()} " + doc_type + str(document) + ' Criado em: ' + str_date

        return professional_info


    def add_medical_nursing_evolution_big_squares(self, evolution_description:str, responsible:dict, date:str, evolution_initial_pos:tuple, responsible_initial_pos:tuple, camp_name:str) -> None:
        """Add a medical and nursing evolution to the pdf, this function only works to the 2 big squares with data, in order, the first and third square, the other 2 minor nursing evolution will be created by another function

        Args:
            evolution_description (str): evolution description
            responsible (dict): Responsible info 
            date (str): date of the evolution with format DD/MM/YYYY HH:mm
            evolution_initial_pos (tuple): initial evolution description position in pdf
            responsible_initial_pos (tuple): initial responsible info position in pdf
            camp_name (str): Camp name (Medica | De enfermagem)

        Returns:
            None
        """
        self.validate_func_args(function_to_verify=self.add_medical_nursing_evolution_big_squares, variables_to_verify={'evolution_description':evolution_description, 'responsible':responsible, 'responsible_initial_pos':responsible_initial_pos, 'evolution_initial_pos':evolution_initial_pos, 'camp_name':camp_name, 'date':date})

        professional_info = self.create_professional_info(professional=responsible, date=date)

        self.add_morelines_text(text=evolution_description, initial_pos=evolution_initial_pos, decrease_ypos=13, camp_name=f'Descricao evolucao {camp_name}', len_max=406, char_per_lines=58)

        self.add_morelines_text(text=professional_info, initial_pos=responsible_initial_pos, decrease_ypos=13, camp_name=f'Informacao do responsavel na evolucao {camp_name}', len_max=99, char_per_lines=49, max_lines_amount=3)
        
        return None


    def add_nursing_evolution(self, evolution_description:str, responsible:dict, date:str, evolution_initial_pos:tuple, responsible_initial_pos:tuple, camp_name:str) -> None:

        self.validate_func_args(function_to_verify=self.add_medical_nursing_evolution_big_squares, variables_to_verify={'evolution_description':evolution_description, 'responsible':responsible, 'responsible_initial_pos':responsible_initial_pos, 'evolution_initial_pos':evolution_initial_pos, 'camp_name':camp_name, 'date':date})

        professional_info = self.create_professional_info(professional=responsible, date=date)

        self.add_morelines_text(text=evolution_description, initial_pos=evolution_initial_pos, decrease_ypos=13, camp_name=f'Descricao evolucao {camp_name}', len_max=175, char_per_lines=58)

        self.add_morelines_text(text=professional_info, initial_pos=responsible_initial_pos, decrease_ypos=13, camp_name=f'Informacao do responsavel na evolucao {camp_name}', len_max=99, char_per_lines=49, max_lines_amount=3)
        
        return None


    def add_evolutions(self, evolutions:list) -> None:
        """Add evolutions to pdf

        Args:
            evolutions (list): list with dict of evolutions

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """        

        self.validate_func_args(function_to_verify=self.add_evolutions, variables_to_verify={'evolutions':evolutions})

        for evo in evolutions:
            current_category = str(evo['category']).strip().lower()
            # Add the big squares first
            if current_category == 'e2':
            # Add nursing evolution with the same square size than medical evolution
                self.add_medical_nursing_evolution_big_squares(evolution_description=evo['description'], responsible=evo['professional'], date=evo['created_at'], evolution_initial_pos=(30, 224), responsible_initial_pos=(90, 126), camp_name='de Enfermagem - bloco 2')
                
            elif current_category == 'm':
                # Add medical evolution
                self.add_medical_nursing_evolution_big_squares(evolution_description=evo['description'], responsible=evo['professional'], date=evo['created_at'], evolution_initial_pos=(30, 498), responsible_initial_pos=(90, 399), camp_name='Medica')
            elif current_category == 'e1':
                # Adding nursing evolution
                self.add_nursing_evolution(evolution_description=evo['description'], responsible=evo['professional'], date=evo['created_at'], evolution_initial_pos=(30, 339), responsible_initial_pos=(90, 285), camp_name='de Enfermagem - Bloco 1')
            elif current_category == 'e3':
                self.add_nursing_evolution(evolution_description=evo['description'], responsible=evo['professional'], date=evo['created_at'], evolution_initial_pos=(432, 498), responsible_initial_pos=(490, 445), camp_name='de Enfermagem - Bloco 3')
            else:   
                raise Exception(f'A categoria {current_category} nao existe, voce deve escolher M, E1, E2 ou E3, sendo que o numero significa a ordem do bloco, nao se preocupe com espacos ou letras maiusculas')

        return None
        

    def add_measures(self, measures:list) -> None:
        
        try:

            self.validate_func_args(function_to_verify=self.add_measures, variables_to_verify={'measures':measures})
            
            
            INITIAL_Y_POS = 234


            #Dict with x position and increment string to every measure, DO NOT CHANGE THE ORDER, the list x_pos_and_measures use the index position
            x_positions_and_measures = {
                'created_at': (440, ''),
                'cardiac_frequency': (475, 'bpm'), 
                'respiratory_frequency': (517, 'ipm'), 
                'blood_pressure': (572, 'mmHg'), 
                'glucose': (633, 'mg/dL'), 
                'sp_o_2': (677, '%'), 
                'celcius_axillary_temperature': (714, '°C'), 
                'pain': (750, '/10'), 
            }

            x_pos_and_meas_list = list(x_positions_and_measures.values())
            x_pos_and_meas_keys = list(x_positions_and_measures.keys())

            #Add to cnavas
            global_cont = 0
            y_pos = INITIAL_Y_POS

            for measur in measures:

                complete_time = measur.get('created_at')
                if complete_time == None:
                    raise Exception('create_at cannot be null')

                # Transform create_at to datetime object
                try:
                    date_object = datetime.datetime.strptime(complete_time, '%d/%m/%Y %H:%M')
                except:
                    raise Exception(f'A data nao corresponde ao formato dd/mm/yyyy HH:MM')
                
                #Reset x_pos_cont
                x_pos_cont = 0

                create_at = str('%02d:%02d') % (date_object.hour, date_object.minute)
                cardiac_frequency = measur.get('cardiac_frequency')
                respiratory_frequency = measur.get('respiratory_frequency')
                sistolic_blood_pressure = measur.get('sistolic_blood_pressure')
                diastolic_blood_pressure = measur.get('diastolic_blood_pressure')
                glucose = measur.get('glucose')
                spO2 = measur.get('sp_o_2')
                celcius_axillary_temperature = measur.get('celcius_axillary_temperature')
                pain = measur.get('pain')

                # Creating blood plesure
                blood_pressure = str(sistolic_blood_pressure) + '/' + str(diastolic_blood_pressure)

                measures_list = [create_at, cardiac_frequency, respiratory_frequency, blood_pressure, glucose, spO2, celcius_axillary_temperature, pain]

                for value in measures_list:
                    if value == None:
                        x_pos_cont += 1
                        continue
                    
                    # Create current value string with measure
                    current_value = f'{value}{x_pos_and_meas_list[x_pos_cont][1]}'
                    current_x_pos = x_pos_and_meas_list[x_pos_cont][0]
                    self.add_oneline_text(text=current_value, pos=(current_x_pos, y_pos), centralized=True, nullable=True, len_max=20, camp_name=f'{global_cont} - {x_pos_and_meas_keys[x_pos_cont]}')
                    x_pos_cont += 1

            return None

        except Exception as error:
            raise error
        except:
            raise Exception('Erro inesperado enquanto adicionava measures em folha de Evolucao')