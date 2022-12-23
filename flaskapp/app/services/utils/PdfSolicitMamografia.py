from app.env import FONT_DIRECTORY, TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY, WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfWriter, PdfReader



class PdfSolicitMamografia(ReportLabCanvasUtils):

    TEMPLATE_DIRECTORY = TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY
    WRITE_DIRECTORY = WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY

    def __init__(self) -> None:

        self.packet_1 = io.BytesIO()
        # Create canvas and add data
        self.can_1 = canvas.Canvas(self.packet_1, pagesize=letter)
        #Create second canvas
        self.packet_2 = io.BytesIO()
        # Create canvas and add data
        self.can_2 = canvas.Canvas(self.packet_2, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
        self.can_1.setFont('Roboto-Mono', 13)
        self.can_2.setFont('Roboto-Mono', 13)
        self.can = self.can_1
    

    def get_output(self) -> PdfWriter:
        """Return a PdfWriter Object to output a file"""
        self.can_1.save()
        self.can_2.save()
        self.packet_1.seek(0)
        self.packet_2.seek(0)
        new_pdf = PdfReader(self.packet_1)
        new_pdf_2 = PdfReader(self.packet_2)
        # read the template pdf 
        template_pdf = PdfReader(open(self.TEMPLATE_DIRECTORY, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        page_2 = template_pdf.pages[1]
        page_2.merge_page(new_pdf_2.pages[0])
        output.add_page(page)
        output.add_page(page_2)
        
        return output
    
    def change_canvas(self) -> None:
        """Change to second canvas to write new data"""
        self.can_1 = self.can
        self.can = self.can_2
        return None
    
    def add_patient_adress_cep(self, number:str) -> None:
        """add patient addes cep to document

        Args:
            number (str): adress cep

        Returns:
            None
        """    
        try:
            if number == None:
                return None
            if type(number) != type(str()) and number != None:
                raise Exception('Endereco de CEP do paciente (Patient Adress CEP) deve ser um string')
            number = str(number).strip()
            if len(number) == 8:
                self.add_oneline_text(text=number[:5], pos=(47, 438), camp_name='Patient Adress CEP', len_max=5, len_min=5, interval=' ', nullable=True)
                self.add_oneline_text(text=number[5:], pos=(138, 438), camp_name='Patient Adress CEP', len_max=3, len_min=3, interval=' ', nullable=True)
                return None
            else:
                raise Exception("Nao foi possivel adicionar o Endereco de CEP do paciente (Patient Adress CEP) porque deve ter somente 8 caracteres")
        except Exception as error:
            raise error
        except:
            raise Exception('Erro desconhecido ocorreu enquanto adicionava Endereco de CEP do paciente (Patient Adress CEP)')


    def add_patient_phonenumber(self, number:str) -> None:
        """add patient phonenumber to document

        Args:
            number (str): phone number

        Returns:
            None
        """
        try:
            if number == None:
                return None
            if type(number) != type(str()) and number != None:
                raise Exception('Numero de Telefone do paciente deve ser uma string')
            number = str(number).strip()
            if len(number) == 10:
                self.add_oneline_text(text=number[:2], pos=(227, 438), camp_name='Patient Phonenumber', len_max=2, len_min=2, interval=' ', nullable=True)
                self.add_oneline_text(text=number[2:6], pos=(288, 438), camp_name='Patient Phonenumber', len_max=4, len_min=4, interval=' ', nullable=True)
                self.add_oneline_text(text=number[6:], pos=(365, 438), camp_name='Patient Phonenumber', len_max=4, len_min=4, interval=' ', nullable=True)
                return None
            else:
                raise Exception("Nao foi possivel adicionar o Numero de Telefone do paciente porque deve ter somente 10 caracteres")

        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido ocorreu enquanto adicionava o numero de telefone do paciente')


    def add_radiotherapy_before(self, radiotherapy_before:list):
        """add radiotherapy option to document

        Args:
            radiotherapy_before (list): radiotherapy option

        Returns:
            None
        """
        try:
            if radiotherapy_before == None:
                return None
            if type(radiotherapy_before) != type(list()):
                raise Exception('radiotherapy_before deve ser uma lista (list)')
            self.add_markable_square_and_onelinetext(option=radiotherapy_before[0], valid_options=['SIMDIR', 'SIMESQ', 'NAO', 'NAOSABE'], text_options=['SIMDIR'], options_positions=((336,332), (336,319), (336, 307), (336, 294)), camp_name='Has made radiotherapy before', square_size=(15,9), len_max=4, len_min=4, text=radiotherapy_before[1], text_pos=(420, 334), interval=' ', nullable=True)
            if radiotherapy_before[0].upper() == 'SIMESQ':
                self.add_oneline_text(text=radiotherapy_before[1], pos=(420, 321), camp_name='Has made radiotherapy before', len_max=4, len_min=4, interval=' ', nullable=True)
            return None

        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido ocorreu enquanto adicionava as radioterapias anteriores(radiotherapy before)')


