from PyPDF2  import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from app.services.utils import pdf_functions
from app.env import FONT_DIRECTORY, TEMPLATE_PRESCRICAO_MEDICA_DIRECTORY, WRITE_PRESCRICAO_MEDICA_DIRECTORY


def func_generate_pdf_prescricao_medica( document_datetime:str, patient_name:str, prescription:list) -> str:
    """fill pdf prescricao medica with 2 pages 

    Args:
        document_datetime (str): document_datetime in %d/%m/%Y %H:%M format
        patient_name (str): patient_name
        prescription (list): list of dicts precriptions, like [{"medicine_name":"Dipirona 500mg", "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}]

    Returns:
        str: Request with pdf in base64
    """    

    
    try:
        try:
            packet = io.BytesIO()
            # Create canvas and add data
            page_size_points = (841.92, 595.2)
            c = canvas.Canvas(packet, pagesize=page_size_points)
            # Change canvas font to mach with the document
            # this is also changed in the document to some especific fields
            pdfmetrics.registerFont(TTFont('Roboto-Mono', FONT_DIRECTORY))
            c.setFont('Roboto-Mono', 12)
            # Writing all data in respective fields
            # not null data
            initial_date_X_pos = 294
            initial_name_X_pos = 120
            for x in range(0, 2):

                c = pdf_functions.add_datetime(can=c, date=document_datetime, pos=(initial_date_X_pos, 38), camp_name='Document Datetime', hours=False, interval='  ', formated=False)
                c = pdf_functions.add_oneline_text(can=c, text=patient_name, pos=(initial_name_X_pos, 505), camp_name='Patient Name', len_max=34, len_min=7)
                initial_date_X_pos += 450
                initial_name_X_pos += 451

            c.setFont('Roboto-Mono', 10)
            c = add_prescription(canvas=c, prescription=prescription)

        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados obrigadorios')
    
        # create a new PDF with Reportlab
        c.save()
        packet.seek(0)
        new_pdf = PdfReader(packet)
        # read the template pdf 
        template_pdf = PdfReader(open(TEMPLATE_PRESCRICAO_MEDICA_DIRECTORY, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        pdf_base64_enconded = pdf_functions.get_base64(newpdf=output)

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except Exception as error:
        return error
    except:
        return Exception('Erro desconhecido enquanto preenchia o documento de prescricao medica')


def add_prescription(canvas:canvas.Canvas, prescription:list) -> canvas.Canvas:
    """add prescription to database

    Args:
        canvas (canvas.Canvas): canvas to use
        precription (list): list of dicts
    Returns:
        canvas or Response:canvas if everthing is allright or Response if hapens some error
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
    if totalChar + (61 * len(prescription)) == 2623:
        raise Exception('O total do docmuento nao pode ultrapassar 2623 caracteres. Lembre-se que 1 linha inteira (61 caracteres) sao destinadas ao nome do medicamento e a quantidade')

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
        canvas = pdf_functions.add_data(can=canvas, data=str_title, pos=(22, yposition))
        canvas = pdf_functions.add_data(can=canvas, data=str_title, pos=(472, yposition))
        yposition -= 10
        # Making the line break whem has 61 charater in a line
        while broke_lines_times >= 0:
            str_use_mode = use_mode[last_line:current_line]
            canvas = pdf_functions.add_data(can=canvas, data=str_use_mode, pos=(22, yposition))
            canvas = pdf_functions.add_data(can=canvas, data=str_use_mode, pos=(472, yposition))
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
    return canvas

