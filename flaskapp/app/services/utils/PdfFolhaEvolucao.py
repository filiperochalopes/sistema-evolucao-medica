from app.env import TEMPLATE_FOLHA_EVOLUCAO_DIRECTORY, WRITE_FOLHA_EVOLUCAO_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from PyPDF2 import PdfWriter, PdfReader
import datetime
from dateutil.parser import isoparse
import sys

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
        print('============ PROFESSIONAL ============', file=sys.stderr)
        print([name, document, category], file=sys.stderr)
        for camp in [name, document, category]:
            if camp == None:
                raise Exception('Algum campo do profissional está faltando, o documento precisa do name, document e category')

        date_object = isoparse(date)
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


    def add_evolution_morelines_text(self, text:str, initial_pos:tuple, decrease_ypos:int, field_name:str, len_max:int, char_per_lines:int, Y_LIMIT_FIRST_COLLUM:int=None, max_lines_amount:int=None, nullable:bool=False, len_min:int=0, interval:str='', return_lines_used:bool=False) -> None:
        """Add text that is fill in one line

        Args:
            text (str): text value
            initial_pos (tuple): initial position in canvas
            decrease_ypos (int): decrease y value to break lines
            field_name (str): Camp name, this is used when return Responses
            len_max (int): maximum text lenght
            char_per_lines (int): char amount for every lines
            max_lines_amount (int, optional): maximum lines amount . Defaults to None.
            nullable (bool, optional): Data can me None. Defaults to False.
            len_min (int, optional): Minimum text lenght. Defaults to 0.
            interval (str): interval to add between every char
        Returns:
            None
        """    
        try:
            if nullable:
                if text == None or len(str(text).strip()) == 0:
                    return None
            self.validate_func_args(function_to_verify=self.add_evolution_morelines_text, variables_to_verify={'text':text, 'initial_pos':initial_pos, 'decrease_ypos':decrease_ypos, 'field_name':field_name, 'len_max':len_max, 'char_per_lines':char_per_lines, 'max_lines_amount':max_lines_amount, 'nullable':nullable, 'len_min':len_min, 'interval':interval, 'return_lines_used':return_lines_used, 'Y_LIMIT_FIRST_COLLUM':Y_LIMIT_FIRST_COLLUM}, nullable_variables=['max_lines_amount', 'Y_LIMIT_FIRST_COLLUM'])


            if not nullable:
                text = text.strip()
                if len(text) == 0:
                    raise Exception(f'{field_name} nao pode ser vazio')
            # verify if text is in the need lenght
            text = text.strip()
            if len_min <= len(text) <= len_max:
                text = self.add_interval_to_data(data=text, interval=interval)
                str_to_line = ''
                broke_lines_times = int(len(text)/char_per_lines)

                if max_lines_amount != None and broke_lines_times + 1 > max_lines_amount:
                    raise Exception(f'Nao foi possivel adicionar {field_name} pois a quantidade de linhas necessrias e maior que {max_lines_amount}')
                current_line = char_per_lines
                last_line = 0
                xpos = initial_pos[0]
                ypos = initial_pos[1]
                # Making the line break whem has max charater limiti reached in a line
                total_lines = broke_lines_times + 1
                changed_collum_positon = False
                first_collum_y_decrease = 0
                second_collum_y_decrease = 0
                while broke_lines_times >= 0:
                    str_to_line = text[last_line:current_line]
                    # Get the text limit 1 line above from limit 
                    if Y_LIMIT_FIRST_COLLUM == None:
                        text_limit_in_first_collum = decrease_ypos
                    else:
                        text_limit_in_first_collum = Y_LIMIT_FIRST_COLLUM + decrease_ypos
                    if ypos < text_limit_in_first_collum:
                        ypos = 490 + (2 * decrease_ypos)
                        xpos = 440
                        new_position = (xpos, ypos)
                        changed_collum_positon = True
                    self.add_data(data=str_to_line, pos=(xpos, ypos))
                    last_line = current_line
                    current_line += char_per_lines
                    broke_lines_times -= 1
                    ypos -= decrease_ypos
                    if changed_collum_positon:
                        second_collum_y_decrease += decrease_ypos
                    else:
                        first_collum_y_decrease += decrease_ypos
                if return_lines_used:
                    return total_lines
                if changed_collum_positon:
                    return new_position, True, first_collum_y_decrease, second_collum_y_decrease
                second_collum_y_decrease = decrease_ypos
                return initial_pos, False, first_collum_y_decrease, second_collum_y_decrease
            else:
                raise Exception(f"Nao foi possivel adicionar {field_name} porque e maior que {len_max} characteres ou menor que {len_min} caracteres")

        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido enquando adicionava {field_name}')


    def add_responsible_evolution(self, evolution_initial_pos:tuple, total_y_decrease:int, DECREASE_Y_POS:int, professional_info:str, evolution_field_name:str, CHAR_PER_LINES:int, Y_LIMIT_SECOND_COLLUM:int,is_in_second_collum:bool) -> None:
        responsible_y_pos = evolution_initial_pos[1] - total_y_decrease - int(DECREASE_Y_POS * 2)

        responsible_initial_pos = (evolution_initial_pos[0], responsible_y_pos)

        self.set_font('Roboto-Mono', 9)
        total_used_lines = self.add_evolution_morelines_text(text=professional_info, initial_pos=responsible_initial_pos, decrease_ypos=DECREASE_Y_POS, field_name=f'Informacao do responsavel na evolucao {evolution_field_name}', len_max=99, char_per_lines=CHAR_PER_LINES, max_lines_amount=3, return_lines_used=True, Y_LIMIT_FIRST_COLLUM=None)

        responsible_y_pos -= total_used_lines * DECREASE_Y_POS

        if responsible_y_pos <= Y_LIMIT_SECOND_COLLUM and is_in_second_collum:
            raise Exception('Voce atingiu o limite do documento')

        return None


    def add_evolution_rectangles(self, evolution_initial_pos:tuple, old_initial_position:tuple, total_y_decrease:int, DECREASE_Y_POS:int, CHAR_PER_LINES:int,CHAR_POINT_SIZE:float, changed_collum:bool, second_collum_y_decrease:int, first_collum_y_decrease:int) -> None:

        if changed_collum:
            # draw black rectangle to first colum
            black_rectangle_x_pos = old_initial_position[0] - 8
            # 5 its just to put rectangle closer to text
            black_rectangle_y_pos = old_initial_position[1] - first_collum_y_decrease + 7 #- DECREASE_Y_POS
            black_rectangle_width = int(CHAR_PER_LINES * CHAR_POINT_SIZE) + 16 # 16 to add 8 extra points in right and left
            #5 is just to test a rectangle creation
            black_rectangle_height = first_collum_y_decrease + (DECREASE_Y_POS * 2) + 5

            self.add_rectangle(pos=(black_rectangle_x_pos, black_rectangle_y_pos), width=black_rectangle_width, height=black_rectangle_height, color=(0, 0, 0), stroke=1, fill=0)

            # draw black rectangle to second collum
            black_rectangle_x_pos = evolution_initial_pos[0] - 8
            black_rectangle_y_pos = evolution_initial_pos[1] - second_collum_y_decrease #- DECREASE_Y_POS
            black_rectangle_width = int(CHAR_PER_LINES * CHAR_POINT_SIZE) + 16 # 16 to add 8 extra points in right and left
            black_rectangle_height = second_collum_y_decrease + DECREASE_Y_POS

            self.add_rectangle(pos=(black_rectangle_x_pos, black_rectangle_y_pos), width=black_rectangle_width, height=black_rectangle_height, color=(0, 0, 0), stroke=1, fill=0)
        else:
            # draw black rectangle
            black_rectangle_x_pos = evolution_initial_pos[0] - 8
            black_rectangle_y_pos = evolution_initial_pos[1] - total_y_decrease - DECREASE_Y_POS
            black_rectangle_width = int(CHAR_PER_LINES * CHAR_POINT_SIZE) + 16 # 16 to add 8 extra points in right and left
            black_rectangle_height = total_y_decrease + (DECREASE_Y_POS * 4)

            self.add_rectangle(pos=(black_rectangle_x_pos, black_rectangle_y_pos), width=black_rectangle_width, height=black_rectangle_height, color=(0, 0, 0), stroke=1, fill=0)
        
        # draw blue rectangle
        blue_rectangle_x_pos = old_initial_position[0] - 8
        blue_rectangle_y_pos = old_initial_position[1] + DECREASE_Y_POS
        blue_rectangle_width = black_rectangle_width
        blue_rectangle_height = 2 * DECREASE_Y_POS

        self.add_rectangle(pos=(blue_rectangle_x_pos, blue_rectangle_y_pos), width=blue_rectangle_width, height=blue_rectangle_height, color=(0, .33, .62), stroke=0, fill=1)

        return None


    def add_evolution_responsible_title(self, responsible:dict, evolution_initial_pos:tuple, DECREASE_Y_POS:int) -> None:
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
        self.add_oneline_text(text=title, pos=(evolution_initial_pos[0], title_y_pos), field_name='Titulo da Evolucao', len_max=40)
        #Change fill color to black again to write text
        self.can.setFillColorRGB(0, 0, 0, 1)

        return None


    def add_medical_nursing_evolution(self, evolution_text:str, responsible:dict, date:str, evolution_initial_pos:tuple, field_name:str, CHAR_PER_LINES:int, CHAR_POINT_SIZE:float, DECREASE_Y_POS:int,Y_LIMIT_SECOND_COLLUM:int, Y_LIMIT_FIRST_COLLUM:int,is_in_second_collum:bool) -> None:
        """Add a medical and nursing evolution to the pdf, this function only works to the 2 big squares with data, in order, the first and third square, the other 2 minor nursing evolution will be created by another function

        Args:
            evolution_text (str): evolution description
            responsible (dict): Responsible info 
            date (str): date of the evolution with format DD/MM/YYYY HH:mm
            evolution_initial_pos (tuple): initial evolution description position in pdf
            responsible_initial_pos (tuple): initial responsible info position in pdf
            field_name (str): Camp name (Medica | De enfermagem)

        Returns:
            None
        """
        self.validate_func_args(function_to_verify=self.add_medical_nursing_evolution, variables_to_verify={'evolution_text':evolution_text, 'responsible':responsible, 'evolution_initial_pos':evolution_initial_pos, 'field_name':field_name, 'date':date, 'CHAR_PER_LINES':CHAR_PER_LINES, 'CHAR_POINT_SIZE':CHAR_POINT_SIZE, 'DECREASE_Y_POS':DECREASE_Y_POS, 'Y_LIMIT_SECOND_COLLUM':Y_LIMIT_SECOND_COLLUM,'is_in_second_collum':is_in_second_collum, 'Y_LIMIT_FIRST_COLLUM':Y_LIMIT_FIRST_COLLUM})

        # get professional info text
        professional_info = 'Responsável: ' + self.create_professional_info(professional=responsible, date=date)
        # Evolution decrease pos
        total_y_decrease = int(len(evolution_text)/CHAR_PER_LINES) * DECREASE_Y_POS
        # get rectangle y decrease
        rectangle_responsible_y_decrease = total_y_decrease
        # Continue total y decrease calculum
        total_y_decrease += int(len(professional_info)/CHAR_PER_LINES) * DECREASE_Y_POS

        self.set_font('Roboto-Mono', 11)
        new_initial_pos, changed_collum, first_collum_y_decrease, second_collum_y_decrease = self.add_evolution_morelines_text(text=evolution_text, initial_pos=evolution_initial_pos, decrease_ypos=DECREASE_Y_POS, field_name=f'Descricao evolucao {field_name}', len_max=5000, char_per_lines=CHAR_PER_LINES, Y_LIMIT_FIRST_COLLUM=Y_LIMIT_FIRST_COLLUM)
        
        if changed_collum:
            #Recude 2 lines
            y_decrease_to_use = second_collum_y_decrease - int(DECREASE_Y_POS)
            self.add_responsible_evolution(evolution_initial_pos=new_initial_pos, total_y_decrease=y_decrease_to_use, DECREASE_Y_POS=DECREASE_Y_POS, professional_info=professional_info, evolution_field_name=f'Descricao evolucao {field_name}', CHAR_PER_LINES=CHAR_PER_LINES, Y_LIMIT_SECOND_COLLUM=Y_LIMIT_SECOND_COLLUM, is_in_second_collum=is_in_second_collum)
        else:
            self.add_responsible_evolution(evolution_initial_pos=new_initial_pos, total_y_decrease=rectangle_responsible_y_decrease, DECREASE_Y_POS=DECREASE_Y_POS, professional_info=professional_info, evolution_field_name=f'Descricao evolucao {field_name}', CHAR_PER_LINES=CHAR_PER_LINES, Y_LIMIT_SECOND_COLLUM=Y_LIMIT_SECOND_COLLUM, is_in_second_collum=is_in_second_collum)
        
        self.add_evolution_rectangles(evolution_initial_pos=new_initial_pos, total_y_decrease=rectangle_responsible_y_decrease, old_initial_position=evolution_initial_pos, DECREASE_Y_POS=DECREASE_Y_POS, CHAR_PER_LINES=CHAR_PER_LINES, CHAR_POINT_SIZE=CHAR_POINT_SIZE, changed_collum=changed_collum, first_collum_y_decrease=first_collum_y_decrease, second_collum_y_decrease=second_collum_y_decrease)

        self.add_evolution_responsible_title(responsible=responsible, evolution_initial_pos=evolution_initial_pos, DECREASE_Y_POS=DECREASE_Y_POS)
        
        if changed_collum:
            # Add one more line to y decrease
            y_decrease_to_use += DECREASE_Y_POS
            return y_decrease_to_use, changed_collum, new_initial_pos
        else:
            return total_y_decrease, changed_collum, new_initial_pos


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

        CHAR_PER_LINES = 58
        # Char size in points
        CHAR_POINT_SIZE = 6.6
        DECREASE_Y_POS = 13


        evolution_x_pos = 20
        evolution_y_pos = 490
        Y_LIMIT_FIRST_COLLUM = 60
        Y_LIMIT_SECOND_COLLUM = 283
        y_limit = Y_LIMIT_FIRST_COLLUM
        cont = 1
        second_collum = False
        for e in evolutions:
            total_y_decrease, changed_collum, new_evolution_pos = self.add_medical_nursing_evolution(evolution_text=e['text'], responsible=e['professional'], date=e['created_at'], evolution_initial_pos=(evolution_x_pos, evolution_y_pos), field_name=f'{cont} evolucao medica', CHAR_PER_LINES=CHAR_PER_LINES, CHAR_POINT_SIZE=CHAR_POINT_SIZE, DECREASE_Y_POS=DECREASE_Y_POS, Y_LIMIT_SECOND_COLLUM=Y_LIMIT_SECOND_COLLUM, is_in_second_collum=second_collum, Y_LIMIT_FIRST_COLLUM=Y_LIMIT_FIRST_COLLUM)

            evolution_x_pos = new_evolution_pos[0]
            evolution_y_pos = new_evolution_pos[1]

            #Calculate new evolution
            evolution_y_pos -= total_y_decrease + int(DECREASE_Y_POS * 6)

            #Verify if the collum has been changed
            if changed_collum:
                second_collum = True

            # Chnage the collum to second if needed
            if evolution_y_pos < y_limit and not changed_collum:
                if second_collum:
                    raise Exception('Voce atingiu o limite do documento')
                evolution_x_pos = 440
                evolution_y_pos = 490
                y_limit = Y_LIMIT_SECOND_COLLUM
                second_collum = True

            cont += 1

        return None
        

    def get_measures_list(self, date_object:datetime, measure:dict):
        """Return measures list with the tabel order to use index

        Args:
            date_object (datetime): date object
            measure (dict): current measure

        Returns:
            _type_: _description_
        """        
        created_at = str('%02d:%02d') % (date_object.hour, date_object.minute)
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

        measures_list = [created_at, cardiac_frequency, respiratory_frequency, blood_pressure, glucose, spO2, celcius_axillary_temperature, pain]

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
            

            for m in measures:
                complete_time = m.get('created_at')
                if complete_time == None:
                    raise Exception('create_at cannot be null')

                # Transform create_at to datetime object
                try:
                    date_object = isoparse(complete_time)
                except:
                    raise Exception(f'A data nao corresponde ao formato ISO %Y-%m-%dT%H:%M:%S')
                
                # Reset x_pos_cont
                x_pos_cont = 0

                measures_list, professional = self.get_measures_list(date_object=date_object, measure=m)

                for value in measures_list:
                    if value == None:
                        x_pos_cont += 1
                        continue
                    
                    # Create current value string with measure
                    current_value = f'{value}{x_pos_and_meas_list[x_pos_cont][1]}'
                    current_x_pos = x_pos_and_meas_list[x_pos_cont][0]
                    self.add_oneline_text(text=current_value, pos=(current_x_pos, y_pos), centralized=True, nullable=True, len_max=20, field_name=f'{global_cont} - {x_pos_and_meas_keys[x_pos_cont]}')
                    x_pos_cont += 1
                
                # Update count variables
                y_pos -= 12
                global_cont += 1
        
                # Add new responsible names to document
                all_responsible_names += self.create_professional_info(professional=professional, date=complete_time, abbreviated=True) + '| '

            # Add new responsible name to docs
            self.set_font('Roboto-Mono', 8)
            self.add_morelines_text(text=all_responsible_names, initial_pos=(428, 66), decrease_ypos=8, field_name='All professionals names in measures', len_max=4060, char_per_lines=80)

            return None
        except Exception as error:
            raise error
        except:
            raise Exception('Erro inesperado enquanto adicionava measures em folha de Evolucao')