from app.env import FONT_DIRECTORY, TEMPLATE_SOLICIT_MAMOGRAFIA_DIRECTORY, WRITE_SOLICIT_MAMOGRAFIA_DIRECTORY
from app.services.utils.ReportLabCanvasUtils import ReportLabCanvasUtils
import io
import datetime
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

    def get_patient_age(self, birthdate):
        try:
            # brazillian timezone UTC-3
            timezone = datetime.timezone(offset=datetime.timedelta(hours=-3))
            today = datetime.datetime.now(tz=timezone)
            age = datetime.datetime.strptime(birthdate, '%d/%m/%Y')

            return today.year - age.year - ((today.month, today.day) < (age.month, age.day))
        except Exception as error:
            raise Exception(f'A data de nascimento do paciente nao corresponde ao formato dd/mm/yyyy')

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
            if breast_surgery_before['did_not'].lower() == 'true':
                self.add_square(pos=necessary_keys_positions['did_not'], size=(15, 9))
                return None
        
            for surgery in valid_keys:
                #Receive the current surgery
                current_surgery = breast_surgery_before[surgery]
                if surgery == 'did_not':
                    if current_surgery.lower() == 'true':
                        self.add_square(pos=necessary_keys_positions[surgery], size=(15, 9))
                        return None
                    else:
                        continue

                if type(current_surgery) != type(list()):
                    raise Exception(f'{surgery} deve ser uma lista com os anos da cirurgias no seio direito e esquerdo ou None, exemplo: surgery: None or surgery:(None, 2020)')
                elif len(current_surgery) == 1 and current_surgery[0] == None:
                    continue
                
                if len(current_surgery) != 2:
                    raise Exception(f'{surgery} deve ser uma lista com 2 valores , exemplo: (ano_esquerdo, ano_direito)')
                
                cont = 0 
                for year in current_surgery:
                    # Add year in right position
                    self.add_oneline_text(text=year, pos=necessary_keys_positions[surgery][cont], camp_name=f'{surgery} year', len_max=4, len_min=4, nullable=True, interval=' ')
                    cont = 1
                
                
            return None
        
        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido ocorreu enquanto adicionava cirurgias anterioes nos seios (breast_surgery_before)')


    def add_diagnostic_mammogram(self, diagnostic_mammogram:dict):
        """add diagnostic_mammogram to document

        Args:
            
            diagnostic_mammogram (dict): diagnostic_mammogram

        Returns:
            None
        """
        try:
            if diagnostic_mammogram == None:
                return None
            if type(diagnostic_mammogram) != type(dict()):
                raise Exception("""
    Diagnostico de mamografia (diagnostic_mammogram) deve ser um dicionario com dicionarios no modelo da estrutura abaixo, existem mais exemplos na docstring da funcao, exemplo:
    'exame_clinico':
            {'direita':[
                'PAPILAR', 
                {'descarga_papilar': ['CRISTALINA', 'HEMORRAGICA']},
                {'nodulo': ['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
                {'espessamento':['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
                {'linfonodo_palpavel':['AXILAR', 'SUPRACLAVICULAR']}
                ],
            'esquerda':[
                'PAPILAR', 
                {'descarga_papilar': ['CRISTALINA', 'HEMORRAGICA']},
                {'nodulo': ['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
                {'espessamento':['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA']},
                {'linfonodo_palpavel':['AXILAR', 'SUPRACLAVICULAR']}
                ]
            }
        """)
            # secoes validas
            sections_keys = ['exame_clinico', 'controle_radiologico', 'lesao_diagnostico', 'avaliacao_resposta', 'revisao_mamografia_lesao', 'controle_lesao']
            
            if len(diagnostic_mammogram) > 6:
                raise Exception(f'O dicionario de diagnostic_mammogram nao pode ter mais que 6 keys, use somente {sections_keys}')
            
            
            

            for section in sections_keys:
                if section in diagnostic_mammogram.keys():
                    # Mark sections options in mamografia diagnostica
                    self.add_markable_square(option=section, valid_options=['EXAME_CLINICO', 'CONTROLE_RADIOLOGICO', 'LESAO_DIAGNOSTICO', 'AVALIACAO_RESPOSTA', 'REVISAO_MAMOGRAFIA_LESAO', 'CONTROLE_LESAO'], options_positions=((56, 762), (55, 590), (226, 590),(402, 589),(55, 487),(312, 489),), camp_name='Diagnostic Mammogram Section', square_size=(11,10))
                    current_options = diagnostic_mammogram[section]
                    if section == 'exame_clinico':
                        if type(current_options) != type(dict()):
                            raise Exception('exame_clinico deve ser um dicionario, exemplo: "exame_clinico":["direita":["PAPILAR", {"":[]}]]')
                        # See all itens in dict
                        breast_keys = ['direita', 'esquerda']
                        for breast in breast_keys:
                            # Options in direita
                            # ['descarga_papilar', 'nodulo', 'espessamento', 'linfonodo_palpavel']
                            if breast in current_options.keys():
                                if breast == 'direita':
                                    self.add_exame_clinico_direita(current_options=current_options['direita'])

                                if breast == 'esquerda':
                                    self.add_exame_clinico_esquerda(current_options=current_options['esquerda'])
                    
                    if section == 'controle_radiologico':
                        if type(current_options) != type(dict()):
                            raise Exception('controle_radiologico deve ser um dicionario, exemplo: "controle_radiologico":{"direita": [],      "esquerda": []}')
                        # See all itens in dict
                        breast_keys = ['direita', 'esquerda']
                        for breast in breast_keys:
                            if breast in current_options.keys():
                                if breast == 'direita':
                                    self.add_controle_radiologico_direita(current_options=current_options['direita'])

                                if breast == 'esquerda':
                                    self.add_controle_radiologico_esquerda(current_options=current_options['esquerda'])
                                    
                    if section == 'lesao_diagnostico':
                        if type(current_options) != type(dict()):
                            raise Exception('lesao_diagnostico deve ser um dicionario, exemplo: "lesao_diagnostico":{"direita": [], "esquerda": []}')
                        # See all itens in dict
                        breast_keys = ['direita', 'esquerda']
                        for breast in breast_keys:
                            if breast in current_options.keys():
                                if breast == 'direita':
                                    self.add_lesao_diagnostico_direita(current_options=current_options['direita'])

                                if breast == 'esquerda':
                                    self.add_lesao_diagnostico_esquerda(current_options=current_options['esquerda'])

                    if section == 'avaliacao_resposta':
                        if type(current_options) != type(list()):
                            raise Exception('avaliacao_resposta deve ser um dicionario, exemplo: "avaliacao_resposta":["direita", "esquerda"]')
                        # See all itens in list
                        for breast in current_options:
                            self.add_markable_square(option=breast, valid_options=['DIREITA', 'ESQUERDA'], options_positions=((401, 562), (401, 547)), camp_name='avaliacao_resposta breastS', square_size=(11,10), nullable=True)
                            

                    if section == 'revisao_mamografia_lesao':
                        if type(current_options) != type(dict()):
                            raise Exception('revisao_mamografia_lesao deve ser um dicionario, exemplo: "revisao_mamografia_lesao":{"direita": [], "esquerda": []}')
                        # See all itens in dict
                        breast_keys = ['direita', 'esquerda']
                        for breast in breast_keys:
                            if breast in current_options.keys():
                                if breast == 'direita':
                                    self.add_revisao_mamografia_lesao_direita(current_options=current_options['direita'])

                                if breast == 'esquerda':
                                    self.add_revisao_mamografia_lesao_esquerda(current_options=current_options['esquerda'])
                                    pass

                    if section == 'controle_lesao':
                        if type(current_options) != type(dict()):
                            raise Exception('controle_lesao deve ser um dicionario, exemplo: "controle_lesao":{"direita": [], "esquerda": []}')
                        # See all itens in dict
                        breast_keys = ['direita', 'esquerda']
                        for breast in breast_keys:
                            if breast in current_options.keys():
                                if breast == 'direita':
                                    self.add_controle_lesao_direita(current_options=current_options['direita'])

                                if breast == 'esquerda':
                                    self.add_controle_lesao_esquerda(current_options=current_options['esquerda'])
                                    pass

                else:
                    continue

            return None

        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido enquanto adicionava historico de cirurgias nos seios (breast_surgery_before)')


    def add_exame_clinico_direita(self, current_options:dict):
        """add exame_clinico_direita to document

        Args:
            
            current_options (dict): exame_clinico_direita

        Returns:
            None
        """
        try:
            
            if type(current_options) != type(dict()):
                raise Exception('o valores da direita em exame_clinico deve ser uma lista de dicionarios, exemplo: "exame_clinico":["direita":[{"":[]}]]')
            
            item_keys = current_options.keys()
            if 'papilar' in item_keys:
                if current_options['papilar']:
                    self.add_square(pos=(56, 732), size=(15, 9))

            if 'descarga_papilar' in item_keys:
                for option in current_options['descarga_papilar']:
                    self.add_markable_square(option=option, valid_options=['CRISTALINA', 'HEMORRAGICA'], options_positions=((496, 737), (496, 723)), camp_name='descarga_capilar options in direita breast', square_size=(15,9), nullable=True)
            
            if 'nodulo' in item_keys:
                for option in current_options['nodulo']:
                    self.add_markable_square(option=option, valid_options=['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'], options_positions=((312, 696), (361, 696), (412, 696), (466, 696), (512, 696), (312, 683), (361, 683), (412, 683), (466, 683), (512, 683)), camp_name='nodulo options in direita breast', square_size=(15,9), nullable=True)

            if 'espessamento' in item_keys:
                for option in current_options['espessamento']:
                    self.add_markable_square(option=option, valid_options=['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'], options_positions=((313, 650), (362, 650), (413, 650), (467, 650), (513, 650), (313, 637), (362, 637), (413, 637), (467, 637), (513, 637)), camp_name='espessamento options in direita breast', square_size=(15,9), nullable=True)

            if 'linfonodo_palpavel' in item_keys:
                for option in current_options['linfonodo_palpavel']:
                    self.add_markable_square(option=option, valid_options=['AXILAR', 'SUPRACLAVICULAR'], options_positions=((380, 615), (420, 615)), camp_name='linfonodo_palpavel options in direita breast', square_size=(15,9), nullable=True)
            return None

        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido enquanto adicionava exame_clinico_direita')



    def add_exame_clinico_esquerda(self, current_options:dict):
        """add exame_clinico_esquerda to document

        Args:
            
            exame_clinico_esquerda (dict): current_options

        Returns:
            None
        """
        try:

            if type(current_options) != type(dict()):
                raise Exception('valores da esquerda em exame_clinico deve ser uma lista de dicionarios, exemplo: "exame_clinico":["esquerda":[{"":[]}]]')
            item_keys = current_options.keys()
            if 'papilar' in item_keys:
                if current_options['papilar']:
                    self.add_square(pos=(314, 732), size=(15, 9))
            if 'descarga_papilar' in item_keys:
                for option in current_options['descarga_papilar']:
                    self.add_markable_square(option=option, valid_options=['CRISTALINA', 'HEMORRAGICA'], options_positions=((238, 737), (238, 725)), camp_name='descarga_capilar options in esquerda breast', square_size=(15,9), nullable=True)
            
            if 'nodulo' in item_keys:
                for option in current_options['nodulo']:
                    self.add_markable_square(option=option, valid_options=['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'], options_positions=((54, 696), (103, 696), (154, 696), (208, 696), (254, 696), (54, 683), (103, 683), (154, 683), (208, 683), (254, 683)), camp_name='nodulo options in esquerda breast', square_size=(15,9), nullable=True)

            if 'espessamento' in item_keys:
                for option in current_options['espessamento']:
                    self.add_markable_square(option=option, valid_options=['QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'], options_positions=((55, 650), (104, 650), (155, 650), (209, 650), (255, 650), (55, 637), (104, 637), (155, 637), (209, 637), (255, 637)), camp_name='espessamento options in esquerda breast', square_size=(15,9), nullable=True)

            if 'linfonodo_palpavel' in item_keys:
                for option in current_options['linfonodo_palpavel']:
                    self.add_markable_square(option=option, valid_options=['AXILAR', 'SUPRACLAVICULAR'], options_positions=((121, 615), (162, 616)), camp_name='linfonodo_palpavel options in esquerda breast', square_size=(15,9), nullable=True)
            return None
        
        except Exception as error:
            raise error
        except:
            raise Exception(f'Erro desconhecido enquanto adicionava exame_clinico_direita')


    def add_controle_radiologico_direita(self, current_options:list):
        """add controle_radiologico_direita to document

        Args:
            
            current_options (list): current_options

        Returns:
            None
        """
        try:
            for option in current_options:    
                self.add_markable_square(option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((61, 571), (61, 560), (61, 550), (61, 539), (61, 528), (61, 517), (61, 506)), camp_name='controle_radiologico_direita options in right breast', square_size=(10,5), nullable=True)

            return None
        except:
            raise Exception('Erro desconhecido enquanto adicionava controle_radiologico_direita')


    def add_controle_radiologico_esquerda(self, current_options:list):
        """add controle_radiologico_esquerda to document

        Args:
            
            current_options (list): current_options

        Returns:
            None
        """
        try:
            for option in current_options:    
                self.add_markable_square(option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((161, 571), (161, 560), (161, 548), (161, 538), (161, 528), (161, 517), (161, 505)), camp_name='controle_radiologico_esquerda options in right breast', square_size=(10,5), nullable=True)

            return None
        except:
            raise Exception('Erro desconhecido enquanto adicionava controle_radiologico_esquerda')


    def add_lesao_diagnostico_direita(self, current_options:list):
        """add lesao_diagnostico_direita to document

        Args:
            
            current_options (list): current_options

        Returns:
            None
        """
        try:
            for option in current_options:    
                self.add_markable_square(option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((243, 571), (243, 560), (243, 549), (243, 539), (243, 528), (243, 517), (243, 506)), camp_name='lesao_diagnostico_direita options in right breast', square_size=(10,5), nullable=True)

            return None
        except:
            raise Exception('Erro desconhecido enquanto adicionava lesao_diagnostico_direita')


    def add_lesao_diagnostico_esquerda(self, current_options:list):
        """add lesao_diagnostico_esquerda to document

        Args:
            
            current_options (list): current_options

        Returns:
            None
        """
        try:
            for option in current_options:    
                self.add_markable_square(option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((341, 571), (341, 560), (341, 550), (341, 539), (341, 528), (341, 517), (341, 506)), camp_name='lesao_diagnostico_esquerda options in right breast', square_size=(10,5), nullable=True)

            return None
        except:
            raise Exception('Erro desconhecido enquanto adicionava lesao_diagnostico_esquerda')


    def add_revisao_mamografia_lesao_direita(self, current_options:list):
        """add revisao_mamografia_lesao_direita to document

        Args:
            
            current_options (list): current_options

        Returns:
            None
        """
        try:
            for option in current_options:    
                self.add_markable_square(option=option, valid_options=['0', '3', '4', '5'], options_positions=((64, 469), (64, 458), (64, 448), (64, 437)), camp_name='mamografia_lesao_direita options in right breast', square_size=(10,5), nullable=True)

            return None
        except:
            raise Exception('Erro desconhecido enquanto adicionava mamografia_lesao_direita')


    def add_revisao_mamografia_lesao_esquerda(self, current_options:list):
        """add revisao_mamografia_lesao_esquerda to document

        Args:
            
            current_options (list): current_options

        Returns:
            None
        """
        try:
            for option in current_options:    
                self.add_markable_square(option=option, valid_options=['0', '3', '4', '5'], options_positions=((164, 469), (164, 458), (164, 446), (164, 436)), camp_name='mamografia_lesao_esquerda options in right breast', square_size=(10,5), nullable=True)
            return None
        except:
            raise Exception('Erro desconhecido enquanto adicionava mamografia_lesao_esquerda')


    def add_controle_lesao_direita(self, current_options:list):
        """add controle_lesao_direita to document

        Args:
            
            current_options (list): current_options

        Returns:
            None
        """
        try:
            for option in current_options:    
                self.add_markable_square(option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((329, 469), (329, 459), (329, 447), (329, 437), (329, 426), (329, 415), (329, 404)), camp_name='controle_lesao_direita options in right breast', square_size=(10,5), nullable=True)

            return None
        except:
            raise Exception('Erro desconhecido enquanto adicionava controle_lesao_direita')


    def add_controle_lesao_esquerda(self, current_options:list):
        """add controle_lesao_esquerda to document

        Args:
            
            current_options (list): current_options

        Returns:
            None
        """
        try:
            for option in current_options:    
                self.add_markable_square(option=option, valid_options=['NODULO', 'MICROCA', 'ASSIMETRIA_FOCAL', 'ASSIMETRIA_DIFUSA', 'AREA_DENSA', 'DISTORCAO', 'LINFONODO'], options_positions=((427, 469), (427, 458), (427, 448), (427, 437), (427, 426), (427, 415), (427, 404)), camp_name='controle_lesao_esquerda options in right breast', square_size=(10,5), nullable=True)

            return None
        except:
            raise Exception('Erro desconhecido enquanto adicionava controle_lesao_esquerda')





