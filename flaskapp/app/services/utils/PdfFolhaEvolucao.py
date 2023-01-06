from app.env import TEMPLATE_FOLHA_EVOLUCAO_DIRECTORY, WRITE_FOLHA_EVOLUCAO_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from PyPDF2 import PdfWriter, PdfReader
import datetime


class PdfFolhaEvolucao(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_FOLHA_EVOLUCAO_DIRECTORY
    WRITE_DIRECTORY = WRITE_FOLHA_EVOLUCAO_DIRECTORY

    def __init__(self) -> None:
        # Create canvas and add data
        page_size_points = (842, 595)
        super().__init__(canvas_pagesize=page_size_points)
        self.can.setFont('Roboto-Condensed-Bold', 20)
    

    def get_output(self) -> PdfWriter:
        return super().get_output()
        

    def create_professional_info(self, professional:dict, date:str, abbreviated:bool=False) -> str:
        """Create professional info merging name, document and date

        Args:
            professional (dict): _description_
            date (str): _description_
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

        date_object = datetime.datetime.strptime(date, '%d/%m/%Y %H:%M')
        str_date = str('%02d/%02d/%d %02d:%02d') % (date_object.day, date_object.month, date_object.year, date_object.hour, date_object.minute)

        if category.lower() == 'm':
            doc_type = 'CRM '
        elif category.lower() == 'e':
            doc_type = 'COREM '
        else:
            raise Exception(f'A categoria de profissional {category} nao existe, envie "e" ou "M", sendo "e" para emfermeiros e "m" para medicos')

        if abbreviated:
            name = self.get_abbrevitate_name(name=name)

        professional_info = f"{str(name).strip()} " + doc_type + str(document) + ' Criado em: ' + str_date

        return str(professional_info)


    def add_medical_nursing_evolution(self, evolution_description:str, responsible:dict, date:str, evolution_initial_pos:tuple, camp_name:str) -> None:
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
        self.validate_func_args(function_to_verify=self.add_medical_nursing_evolution, variables_to_verify={'evolution_description':evolution_description, 'responsible':responsible, 'evolution_initial_pos':evolution_initial_pos, 'camp_name':camp_name, 'date':date})

        CHAR_PER_LINES = 58
        # Char size in points
        CHAR_POINT_SIZE = 6.6
        DECREASE_Y_POS = 13

        professional_info = 'Responsável: ' + self.create_professional_info(professional=responsible, date=date)
        
        self.set_font('Roboto-Mono', 11)
        self.add_morelines_text(text=evolution_description, initial_pos=evolution_initial_pos, decrease_ypos=DECREASE_Y_POS, camp_name=f'Descricao evolucao {camp_name}', len_max=1000, char_per_lines=CHAR_PER_LINES)

        total_y_decrease = int(len(evolution_description)/CHAR_PER_LINES) * DECREASE_Y_POS 

        responsible_y_pos = evolution_initial_pos[1] - total_y_decrease - int(DECREASE_Y_POS * 2)

        responsible_initial_pos = (evolution_initial_pos[0], responsible_y_pos)

        self.set_font('Roboto-Mono', 9)
        self.add_morelines_text(text=professional_info, initial_pos=responsible_initial_pos, decrease_ypos=DECREASE_Y_POS, camp_name=f'Informacao do responsavel na evolucao {camp_name}', len_max=99, char_per_lines=CHAR_PER_LINES, max_lines_amount=3)

        # draw black rectangle
        black_rectangle_x_pos = evolution_initial_pos[0] - 8
        black_rectangle_y_pos = evolution_initial_pos[1] - total_y_decrease - DECREASE_Y_POS
        black_rectangle_width = int(CHAR_PER_LINES * CHAR_POINT_SIZE) + 16 # 16 to add 8 extra points in right and left
        black_rectangle_height = total_y_decrease + (DECREASE_Y_POS * 4)

        self.add_rectangle(pos=(black_rectangle_x_pos, black_rectangle_y_pos), width=black_rectangle_width, height=black_rectangle_height, color=(0, 0, 0), stroke=1, fill=0)
        
        # draw blue rectangle
        blue_rectangle_x_pos = black_rectangle_x_pos
        blue_rectangle_y_pos = evolution_initial_pos[1] + DECREASE_Y_POS
        blue_rectangle_width = black_rectangle_width
        blue_rectangle_height = 2 * DECREASE_Y_POS

        self.add_rectangle(pos=(blue_rectangle_x_pos, blue_rectangle_y_pos), width=blue_rectangle_width, height=blue_rectangle_height, color=(0, .33, .62), stroke=0, fill=1)
        responsible_category = responsible.get('category')
        if responsible_category.lower() == 'm':
            title = 'EVOLUÇÃO MÉDICA'
        elif responsible_category.lower() == 'e':
            title = 'EVOLUÇÃO DE ENFERMAGEM'
        else:
            raise Exception('Erro inesperado enquanto criava o titulo da evolucao')

        self.set_font('Roboto-Condensed-Bold', 15)
        self.can.setFillColorRGB(1, 1, 1, 1)
        
        title_y_pos = evolution_initial_pos[1] + DECREASE_Y_POS + (DECREASE_Y_POS/2)
        self.add_oneline_text(text=title, pos=(evolution_initial_pos[0], title_y_pos), camp_name='Titulo da Evolucao', len_max=40)
        #Change fill color to black again to write text
        self.can.setFillColorRGB(0, 0, 0, 1)


        total_y_decrease += int(len(professional_info)/CHAR_PER_LINES) * DECREASE_Y_POS
        
        return total_y_decrease


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

        evolution_initial_x_pos = 30
        evolution_initial_y_pos = 498
        y_limit = 60
        cont = 1
        second_collum = False
        for evo in evolutions:
            total_y_decrease = self.add_medical_nursing_evolution(evolution_description=evo['description'], responsible=evo['professional'], date=evo['created_at'], evolution_initial_pos=(evolution_initial_x_pos, evolution_initial_y_pos), camp_name=f'{cont} evolucao medica')

            evolution_initial_y_pos -= total_y_decrease

            cont += 1

            if evolution_initial_y_pos < y_limit:
                if second_collum:
                    raise Exception('Voce atingiu o limite do documento')
                evolution_initial_x_pos = 440
                evolution_initial_y_pos = 498
                y_limit = 283
                second_collum = True


        return None
        

    def get_measures_list(self, date_object:datetime, measure:dict):
        """Return measures list with the tabel order to use index

        Args:
            date_object (datetime): date object
            measure (dict): current measure

        Returns:
            _type_: _description_
        """        
        
        create_at = str('%02d:%02d') % (date_object.hour, date_object.minute)
        cardiac_frequency = measure.get('cardiac_frequency')
        respiratory_frequency = measure.get('respiratory_frequency')
        sistolic_blood_pressure = measure.get('sistolic_blood_pressure')
        diastolic_blood_pressure = measure.get('diastolic_blood_pressure')
        glucose = measure.get('glucose')
        spO2 = measure.get('sp_o_2')
        celcius_axillary_temperature = measure.get('celcius_axillary_temperature')
        pain = measure.get('pain')

        professional = measure.get('professional')

        # Creating blood plesure
        blood_pressure = str(sistolic_blood_pressure) + '/' + str(diastolic_blood_pressure)

        measures_list = [create_at, cardiac_frequency, respiratory_frequency, blood_pressure, glucose, spO2, celcius_axillary_temperature, pain]

        return measures_list, professional


    def get_x_positions_and_measures(self):
        """Return the x positiions and measures needed to add measures

        Returns:
            list
        """        
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

        return x_pos_and_meas_list, x_pos_and_meas_keys


    def add_measures(self, measures:list) -> None:
        """Add measures to pdf

        Args:
            measures (list): list of dicts

        Returns:
            None
        """
        try:

            self.validate_func_args(function_to_verify=self.add_measures, variables_to_verify={'measures':measures})
            
            if len(measures) > 14:
                raise Exception('You cant add more than 14 measures')

            # get all x positions and keys
            x_pos_and_meas_list, x_pos_and_meas_keys = self.get_x_positions_and_measures()

            INITIAL_Y_POS = 234
            #Add to cnavas
            global_cont = 0
            y_pos = INITIAL_Y_POS
            all_responsible_names = 'Responsaveis:' #get all responsible names to add in bottom
            

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

                measures_list, professional = self.get_measures_list(date_object=date_object, measure=measur)

                for value in measures_list:
                    if value == None:
                        x_pos_cont += 1
                        continue
                    
                    # Create current value string with measure
                    current_value = f'{value}{x_pos_and_meas_list[x_pos_cont][1]}'
                    current_x_pos = x_pos_and_meas_list[x_pos_cont][0]
                    self.add_oneline_text(text=current_value, pos=(current_x_pos, y_pos), centralized=True, nullable=True, len_max=20, camp_name=f'{global_cont} - {x_pos_and_meas_keys[x_pos_cont]}')
                    x_pos_cont += 1
                
                # Update count variables
                y_pos -= 12
                global_cont += 1
                # Add new responsible names to document
                all_responsible_names += self.create_professional_info(professional=professional, date=complete_time, abbreviated=True) + '| '

            # Add new responsible name to docs
            self.set_font('Roboto-Mono', 8)
            self.add_morelines_text(text=all_responsible_names, initial_pos=(428, 66), decrease_ypos=8, camp_name='All professionals names in measures', len_max=4060, char_per_lines=80)

            return None
        except Exception as error:
            raise error
        except:
            raise Exception('Erro inesperado enquanto adicionava measures em folha de Evolucao')