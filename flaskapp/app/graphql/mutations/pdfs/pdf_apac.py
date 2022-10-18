import datetime
from PyPDF2  import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from flask import Response

# Doing the import this way only when is called by antoher file (like pytest)
if __name__ != "__main__":
    from . import global_functions

lenghtTest = ''
for x in range(0, 2000):
    lenghtTest += str(x)

template_directory = "./graphql/mutations/pdfs/pdfs_templates/apac.pdf"
font_directory = "./graphql/mutations/pdfs/Roboto-Mono.ttf"


def fill_pdf_apac(establishment_solitc_name:str, establishment_solitc_cnes:int, patient_name:str, patient_cns:int, patient_sex:str, patient_birthday:datetime.datetime, patient_adress_city:str, main_procedure_name:str, main_procedure_code:str, main_procedure_quant:int, patient_mother_name:str=None, patient_mother_phonenumber:int=None, patient_responsible_name:str=None, patient_responsible_phonenumber:int=None, patient_adress:str=None, patient_ethnicity:str=None, patient_color:str=None, patient_adressUF:str=None, patient_adressCEP:int=None, document_chart_number:int=None, patient_adress_city_IBGEcode:int=None, procedure_justification_description:str=None, prodedure_justification_main_cid10:str=None, prodedure_justification_sec_cid10:str=None, prodedure_justification_associated_cause_cid10:str=None, prodedure_justification_comments:str=None, establishment_exec_name:str=None, establishment_exec_cnes:int=None,prof_solicitant_document:dict=None, prof_solicitor_name:str=None, solicitation_datetime:datetime.datetime=None, autorization_prof_name:str=None, emission_org_code:str=None, autorizaton_prof_document:dict=None, autorizaton_datetime:datetime.datetime=None, signature_datetime:datetime.datetime=None, validity_period_start:datetime.datetime=None, validity_period_end:datetime.datetime=None):
    try:
        packet = io.BytesIO()
        # Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', font_directory))
        c.setFont('Roboto-Mono', 10)
        # Writing all data in respective fields
        # not null data
        try:
            c = global_functions.add_cns(can=c, cns=patient_cns, pos=(36, 678), campName='Patient CNS', interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=main_procedure_code, pos=(36, 542), campName='Main Procedure Code', lenMax=10, lenMin=10, interval='  ')
            if type(c) == type(Response()): return c

            c.setFont('Roboto-Mono', 9)
            c = global_functions.add_oneline_text(can=c, text=establishment_solitc_name, pos=(36, 742), campName='Establishment Solict Name', lenMax=77, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_name, pos=(36, 702), campName='Patient Name', lenMax=67, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(423, 699), pos_fem=(456, 699), campName='Patient Sex', square_size=(9,9))
            if type(c) == type(Response()): return c

            
            c = global_functions.add_datetime(can=c, date=patient_birthday, pos=(315, 678), campName='Patient Birthday', hours=False, interval='  ', formated=False)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adress_city, pos=(36, 584), campName='Patient Adress City', lenMax=58, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=main_procedure_name, pos=(220, 542), campName='Main Procedure Name', lenMax=50, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=main_procedure_quant, pos=(508, 542), campName='Main Procedure Quantity', lenMax=8, lenMin=1, valueMin=1, valueMax=99999999)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=establishment_solitc_cnes, pos=(468, 742), campName='Establishment Solict CNES', lenMax=7, lenMin=7,valueMin=0, valueMax=99999999)
            if type(c) == type(Response()): return c
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            c.setFont('Roboto-Mono', 11)
            c = global_functions.add_oneline_intnumber(can=c, number=establishment_exec_cnes, pos=(450, 28), campName='Establishment Exec CNES', lenMax=7, lenMin=7,valueMin=0, valueMax=99999999, interval=' ')
            if type(c) == type(Response()): return c


            c.setFont('Roboto-Mono', 9)
            c = global_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(36, 654), campName='Patient Mother Name', lenMax=67, lenMin=7, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_mother_phonenumber, pos=(409, 650), campName='Patient Mother Phone Number', lenMax=10, lenMin=10, valueMin=0, valueMax=9999999999, nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_responsible_name, pos=(36, 630), campName='Patient Responsible Name', lenMax=67, lenMin=7, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_responsible_phonenumber, pos=(409, 626), campName='Patient Responsible Phone Number', lenMax=10, lenMin=10, valueMin=0, valueMax=9999999999, nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adress, pos=(36, 608), campName='Patient Adress', lenMax=97, lenMin=7, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_color, pos=(404, 678), campName='Patient Color', lenMax=10, lenMin=4, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_ethnicity, pos=(470, 678), campName='Patient Ehinicity', lenMax=17, lenMin=4, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_adressCEP, pos=(476, 582), campName='Patient Adress CEP', lenMax=8, lenMin=8, valueMin=0, valueMax=99999999, nullable=True, interval=' ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=document_chart_number, pos=(483, 702), campName='Document Chart Number', lenMax=14, lenMin=1, valueMin=0, valueMax=99999999999999, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_adress_city_IBGEcode, pos=(370, 582), campName='Patient Adress City IBGE code', lenMax=7, lenMin=7, valueMin=0, valueMax=9999999, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_UF(can=c, uf=patient_adressUF, pos=(443, 582), campName='Patient Adress UF', nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=procedure_justification_description, pos=(36, 344), campName='Procedure Justification Description', lenMax=55, lenMin=4, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=prodedure_justification_main_cid10, pos=(352, 344), campName='Procedure Justification main CID10', lenMax=4, lenMin=3, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=prodedure_justification_sec_cid10, pos=(420, 344), campName='Procedure Justification secondary CID10', lenMax=4, lenMin=3, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=prodedure_justification_associated_cause_cid10, pos=(505, 344), campName='Procedure Justification Associated Causes CID10', lenMax=4, lenMin=3, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=establishment_exec_name, pos=(36, 30), campName='Establishment Exec Name', lenMax=71, lenMin=5, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=prof_solicitor_name, pos=(36, 204), campName='Profissional Solicitor Name', lenMax=48, lenMin=5, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=autorization_prof_name, pos=(36, 136), campName='Profissional Authorizator Name', lenMax=46, lenMin=5, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=emission_org_code, pos=(290, 136), campName='Emission Org Code', lenMax=16, lenMin=2, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_datetime(can=c, date=solicitation_datetime, pos=(310, 204), campName='Solicitation Datetime', hours=False, interval='  ', formated=False, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_datetime(can=c, date=autorizaton_datetime, pos=(36, 68), campName='Authorization Datetime', hours=False,formated=True, nullable=True)
            if type(c) == type(Response()): return c
        
        except:
            return Response('Critical error happen when adding data that can be null to fields', status=500)
        # create a new PDF with Reportlab
        c.save()
        packet.seek(0)
        new_pdf = PdfReader(packet)
        # read the template pdf 
        template_pdf = PdfReader(open(template_directory, "rb"))
        output = PdfWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = template_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        return output
    except:
        return Response("Error while filling apac", status=500)



if __name__ == "__main__":
    import global_functions
    output = fill_pdf_apac(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        patient_name='Patient Name',
        patient_cns=928976954930007,
        patient_sex='M',
        patient_birthday=datetime.datetime.now(),
        patient_adress_city='Patient Adress City',
        main_procedure_name='Main procedure Name',
        main_procedure_code='1234567890',
        main_procedure_quant=4,
        patient_mother_name='Patient Mother Name',
        patient_mother_phonenumber=5286758957, 
        patient_responsible_name='Patient Responsible Name', patient_responsible_phonenumber=5465981345, 
        patient_adress='Patient Adress',
        patient_color='Branca',
        patient_ethnicity='Indigena',
        patient_adressUF='BA',
        patient_adressCEP=86425910, 
        document_chart_number=12345,
        patient_adress_city_IBGEcode=4528765,
        procedure_justification_description='Procedure Justification Description', 
        prodedure_justification_main_cid10='A98', 
        prodedure_justification_sec_cid10='A01', prodedure_justification_associated_cause_cid10='A45',
        prodedure_justification_comments='Procedure Justification Comments',establishment_exec_name='Establishment Exec Name', 
        establishment_exec_cnes=7654321,
        prof_solicitant_document={'CPF':28445400070}, 
        prof_solicitor_name='Profissional Solicit Name', 
        solicitation_datetime=datetime.datetime.now(),
        validity_period_start=datetime.datetime.now(),
        validity_period_end=datetime.datetime.now(),
        autorization_prof_name='Autorization Professional Name', 
        emission_org_code='Cod121234', 
        autorizaton_prof_document={'CNS':928976954930007}, 
        autorizaton_datetime=datetime.datetime.now()
    )

    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/apac_teste.pdf")
