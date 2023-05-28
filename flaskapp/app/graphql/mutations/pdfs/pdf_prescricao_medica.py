import base64
from PyPDF2  import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from app.utils import pdf_functions
from app.env import FONT_DIRECTORY, TEMPLATE_PRESCRICAO_MEDICA_DIRECTORY, WRITE_PRESCRICAO_MEDICA_DIRECTORY

from app.graphql import mutation
from ariadne import convert_kwargs_to_snake_case


@mutation.field('generatePdf_PrescricaoMedica')
@convert_kwargs_to_snake_case
def fill_pdf_prescricao_medica(_, info, document_datetime:str, patient_name:str, doctor_name:str, doctor_crm:str, prescription:list) -> str:
    """fill pdf prescricao medica with 2 pages 

    Args:
        document_datetime (str): document_datetime in %d/%m/%Y %H:%M format
        patient_name (str): patient_name
        doctor_name (str)> doctor_name
        doctor_crm (str): doctor_crm
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
            # Writing all data in respective fields
            # not null data
            initial_date_X_pos = 294
            initial_name_X_pos = 120
            initial_doctor_X_pos = 190
            initial_crm_X_pos = 184
            for x in range(0, 2):

                c.setFont('Roboto-Mono', 12)
                c = pdf_functions.add_datetime(can=c, date=document_datetime, pos=(initial_date_X_pos, 38), camp_name='Document Datetime', hours=False, interval='  ', formated=False)
                c = pdf_functions.add_oneline_text(can=c, text=patient_name, pos=(initial_name_X_pos, 505), camp_name='Patient Name', len_max=34, len_min=7)
                c = pdf_functions.add_oneline_text(can=c, text=doctor_name, pos=(initial_doctor_X_pos, 90), camp_name='Doctor Name', len_max=34, len_min=7, centralized=True)
                c.setFont('Roboto-Mono', 11)
                c = pdf_functions.add_oneline_text(can=c, text=doctor_crm, pos=(initial_crm_X_pos, 76), camp_name='Doctor CRM', len_max=13, len_min=11)
                initial_date_X_pos += 450
                initial_name_X_pos += 451
                initial_doctor_X_pos += 451
                initial_crm_X_pos += 451

            c.setFont('Roboto-Mono', 10)
            c = add_prescription(canvas=c, prescription=prescription)

        except Exception as error:
            return error
        except:
            return Exception('Some error happen when adding not null data to fields')
    
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
        pdf_functions.write_newpdf(output, WRITE_PRESCRICAO_MEDICA_DIRECTORY)
        
        with open(WRITE_PRESCRICAO_MEDICA_DIRECTORY, "rb") as pdf_file:
            pdf_base64_enconded = base64.b64encode(pdf_file.read())

        return {
        "base64Pdf":str(pdf_base64_enconded)[2:-1]
        }
        
    except:
        return Exception('Unknow error while adding medical prescription')


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
        raise Exception('prescription has to be a list of dicts, like: [{"medicine_name":"Dipirona 500mg", "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}, {"medicine_name":"Metocoplamina 10mg", "amount":"6 comprimidos", "use_mode":"1 comprimido, via oral, de 8/8h por 2 dias"}]')
    NECESSARY_KEYS = ["medicine_name", "amount", "use_mode"]
    totalChar = 0
    #Add , in the end to evade errors
    for presc in prescription:
        #verify if the item in list is a dict
        if type(presc) != type(dict()):
            raise Exception('All itens in list has to be a dict')
        #Verify if the necessary keys are in the dict
        if 'medicine_name' not in presc.keys() or 'amount' not in presc.keys() or "use_mode" not in presc.keys():
            raise Exception('Some keys in dict is missing, dict has to have "medicine_name", "amount", "use_mode"')
        #Verify if the value in the dics is str
        elif type(presc['medicine_name']) != type(str()) or type(presc['amount']) != type(str()) or type(presc["use_mode"]) != type(str()):
            raise Exception('The values in the keys "medicine_name", "amount", "use_mode" has to be string')
        #verify if medicine_name and amount together isnt bigger than 1 line (61 characters)
        elif len(presc['medicine_name'].strip() + presc['amount'].strip()) > 61:
            raise Exception('"medicine_name" and "amount" cannot be longer than 61 characters')
        #Verify id use_mode isnt bigger than 3 lines (244 characters)
        elif len(presc['use_mode'].strip()) > 244:
            raise Exception('"use_mode"cannot be longer than 244 characters')
        #Verify if the dict has more keys than the needed
        for key in presc.keys():
            if key not in NECESSARY_KEYS:
                raise Exception('The dict can only have 3 keys "medicine_name", "amount", "use_mode"')
        #calculate the total lenght of use_mode
        totalChar += len(presc['use_mode'].strip())
    # Verify if user_mode total lenght and the 2 line that every medicine and amount need isnt bigger than the total of de document
    if totalChar + (61 * len(prescription)) == 2623:
        raise Exception('The total document cannot has more than 2623 characters.Remember than 1 line (61 character) is just to medidine and amount')

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

