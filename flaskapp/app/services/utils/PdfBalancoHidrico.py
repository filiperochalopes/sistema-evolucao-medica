from app.env import TEMPLATE_BALANCO_HIDRICO_DIRECTORY, WRITE_BALANCO_HIDRICO_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
from PyPDF2 import PdfWriter, PdfReader
import datetime


class PdfBalancoHidrico(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_BALANCO_HIDRICO_DIRECTORY
    WRITE_DIRECTORY = WRITE_BALANCO_HIDRICO_DIRECTORY

    def __init__(self) -> None:
        page_size_points = (842, 595)
        super().__init__(canvas_pagesize=page_size_points)
        self.can.setFont('Roboto-Condensed-Bold', 20)


    def get_output(self) -> PdfWriter:
        return super().get_output()


    def get_description_values(self, value:int, description:str) -> str:
        """Create description text and update diurese

        Args:
            value (int): _description_
            description (str): _description_

        Returns:
            str: _description_
        """ 

        if value > 0:
            start = '+'
            self.administrated_fluids += int(value)
        else:
            start = ''
            self.losts += int(value)

        description = str(description).upper().strip()
        if description == 'DIURESE':
            self.diurese += int(value)
        
        return f'{start}{value}ml ({description})'


    def add_description(self, description:str, pos:tuple, camp_name:str) -> None:
        """Function to add description, change color

        Args:
            description (str): _description_
            pos (tuple): _description_
            camp_name (str): _description_
        """
        # Change color
        if description[0] == '-':
            self.can.setFillColorRGB(r=.7, g=0, b=0, alpha=1)
        else:
            self.can.setFillColorRGB(r=0, g=.7, b=0, alpha=1)
        self.add_oneline_text(text=description, pos=pos, camp_name=camp_name, len_max=40)
        # Change back to black
        self.can.setFillColorRGB(r=0, g=0, b=0, alpha=1)

        return None

    
    def add_fluid_balance(self, balances:list) -> None:
        """Add all fluid balances to document

        Args:
            balances (list): _description_

        Returns:
            _type_: _description_
        """        
        self.validate_func_args(function_to_verify=self.add_fluid_balance, variables_to_verify={'balances':balances})

        if len(balances) > 23:
            raise Exception('Nao e possivel adicionar mais que 23 fluidos')

        # Create info variables
        self.administrated_fluids = 0
        self.losts = 0
        self.diurese = 0

        # Maximum balances in first collum
        FIRST_COLLUM_LIMIT = 15
        INCREASE_TO_NEXT_COLLUM = 396
        RECTANGLE_WIDTH = 118
        RECTANGLE_HEIGHT = 25
        rectangle_y_pos = 500
        rectangle_x_pos = 25
        # Get Date position in rectangle
        date_x_pos = rectangle_x_pos + int(RECTANGLE_WIDTH/2)
        date_y_pos = rectangle_y_pos + 10
        # Get description position
        description_x_pos = rectangle_x_pos + RECTANGLE_WIDTH + 8
        description_y_pos = date_y_pos


        cont = 1
        for balan in balances:
            
            # Add data
            self.add_rectangle(pos=(rectangle_x_pos, rectangle_y_pos), width=RECTANGLE_WIDTH, height=RECTANGLE_HEIGHT)
            self.add_datetime(date=balan['created_at'], pos=(date_x_pos, date_y_pos), camp_name=f'{cont} balance creation date (createdAt)', centralized=True)
            description_str = self.get_description_values(value=balan['value'],description=balan['description'])
            self.add_description(description=description_str, pos=(description_x_pos, description_y_pos), camp_name=f'{cont} fluid balance description')

            # Update positions
            rectangle_y_pos -= 30
            date_y_pos = rectangle_y_pos + 10
            description_y_pos = date_y_pos

            
            if cont == FIRST_COLLUM_LIMIT:
                # Update positiokn to new collum
                rectangle_x_pos += INCREASE_TO_NEXT_COLLUM
                date_x_pos = rectangle_x_pos + int(RECTANGLE_WIDTH/2)
                description_x_pos = rectangle_x_pos + RECTANGLE_WIDTH + 8

                rectangle_y_pos = 500
                date_y_pos = rectangle_y_pos + 10
                description_y_pos = date_y_pos

            cont += 1

        return None
