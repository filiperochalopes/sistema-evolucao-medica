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


    def add_breast_surgery_before(self, breast_surgery_before:dict) -> None:
        """add breast_surgery_before to document

        Args:
            breast_surgery_before (dict): breast_surgery_before

        Returns:
            None
        """
        try:
            if breast_surgery_before == None:
                return None
            if type(breast_surgery_before) != type(dict()):
                raise Exception("breast_surgery_before deve ser um dicionarios com listas ou booleanos, exemplo {'surgery':(year_esq, year_dir)} or {'didNot':True}, {'didNot':False,'biopsiaInsinonal':(None, 2020),'biopsiaExcisional':(2021, None),'centraledomia':(None, None),'segmentectomia':(None),'dutectomia':(None, None),'mastectomia':(None, None),'mastectomiaPoupadoraPele':(None, None),'mastectomiaPoupadoraPeleComplexoAreolo':(None, None),'linfadenectomiaAxilar':(None, None),'biopsiaLinfonodo':(None, None),'reconstrucaoMamaria':(None, None),'mastoplastiaRedutora':(None, None),'indusaoImplantes':(None, None)}")
            necessary_keys_positions = {"did_not":(334, 41), "biopsia_insinonal":((500, 251), (338, 251)), "biopsia_excisional":((500, 235), (338, 235)), "centraledomia":((500, 220), (338, 220)), "segmentectomia":((500, 204), (338, 204)), "dutectomia":((500, 190), (338, 190)), "mastectomia":((500, 176), (338, 176)), "mastectomia_poupadora_pele":((500, 159), (338, 159)), "mastectomia_poupadora_pele_complexo_areolo":((500, 143), (338, 143)), "linfadenectomia_axilar":((500, 121), (338, 121)), "biopsia_linfonodo":((500, 105), (338, 105)), "reconstrucao_mamaria":((500, 90), (338, 90)), "mastoplastia_redutora":((500, 75), (338, 75)), "indusao_implantes":((500, 60), (338, 60))}

            if len(breast_surgery_before) > 14:
                raise Exception('Você não pode adicionar mais que 14 chaves no dicionarios em breast_surgery_before')
            #Pick all valid keys
            valid_keys = [ x for x in breast_surgery_before.keys() if x in necessary_keys_positions.keys()]
            #Start adding data
            for surgery in valid_keys:
                #Receive the current surgery
                current_surgery = breast_surgery_before[surgery]
                if surgery == 'did_not':
                    if current_surgery.lower() == 'true':
                        self.add_square(pos=necessary_keys_positions[surgery], size=(15, 9))
                        return None
                    else:
                        continue

                # if type(current_surgery) == type(bool()):
                #     # when is didNot key
                #     if current_surgery:
                #         self.add_square(pos=necessary_keys_positions[surgery], size=(15, 9))
                #         return None
                #     else:
                #         continue
                if current_surgery[0] == None:
                    continue
                elif type(current_surgery) != type(list()):
                    raise Exception(f'{surgery} deve ser uma lista com os anos da cirurgias no seio direito e esquerdo ou None, exemplo: surgery: None or surgery:(None, 2020)')
                
                if len(current_surgery) != 2:
                    raise Exception(f'{surgery} deve ser uma lista com 2 valores , exemplo: (ano_esquerdo, ano_direito)')
                
                cont = 0 
                for year in current_surgery:
                    # Add year in right position
                    self.add_oneline_intnumber(number=year, pos=necessary_keys_positions[surgery][cont], camp_name=f'{surgery} year', len_max=4, len_min=4, value_min=1900, value_max=2100, nullable=True, interval=' ')
                    cont = 1
                
                
            return None
        
        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido ocorreu enquanto adicionava cirurgias anterioes nos seios (breast_surgery_before)')