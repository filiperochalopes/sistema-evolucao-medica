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

    
    def add_fluid_balance(self, balances:list) -> None:
        
        self.validate_func_args(function_to_verify=self.add_fluid_balance, variables_to_verify={'balances':balances})
        #maximum balances in first collum
        FIRST_COLLUM_LIMIT = 13
        y_rectangle_pos = 500

        for balan in balances:

            self.add_rectangle(pos=(25, y_rectangle_pos), width=118, height=25)
            y_rectangle_pos -= 30
        
        

        return None
