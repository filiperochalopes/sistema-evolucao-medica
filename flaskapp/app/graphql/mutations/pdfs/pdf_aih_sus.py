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

template_directory = "./graphql/mutations/pdfs/pdfs_templates/aih_sus.pdf"
font_directory = "./graphql/mutations/pdfs/Roboto-Mono.ttf"

def fill_pdf_aih_sus(establishment_solitc_name:str, establishment_solitc_cnes:int, establishment_exec_name:str, establishment_exec_cnes:int, patient_name:str, patient_cns:int, patient_birthday:datetime.datetime, patient_sex:str, patient_mother_name:str, patient_adress:str, patient_adressCity:str, patient_adressCity_ibgeCode:int, patient_adressUF:str, patient_adressCEP:int, main_clinical_signs_symptoms:str, conditions_justify_hospitalization:str, initial_diagnostic:str, principalCid10:str, procedure_solicited:str, procedure_code:str, clinic:str, internation_carater:str, prof_solicitor_document:dict, prof_solicitor_name:str, solicitation_datetime:datetime.datetime, autorization_prof_name:str, emission_org_code:str, autorizaton_prof_document:dict, autorizaton_datetime:datetime.datetime, hospitalization_autorization_number:int ,exam_results:str=None, chart_number:int=None, patient_ethnicity:str=None, patient_responsible_name:str=None, patient_mother_phonenumber:int=None, patient_responsible_phonenumber:int=None, secondary_cid10:str=None, cid10_associated_causes:str=None, acident_type:str=None, insurance_company_cnpj:int=None, insurance_company_ticket_number:int=None, insurance_company_series:str=None,company_cnpj:int=None, company_cnae:int=None, company_cbor:int=None, pension_status:str=None):
    try:
        packet = io.BytesIO()
        # Create canvas and add data
        c = canvas.Canvas(packet, pagesize=letter)
        # Change canvas font to mach with the document
        # this is also changed in the document to some especific fields
        pdfmetrics.registerFont(TTFont('Roboto-Mono', font_directory))
        c.setFont('Roboto-Mono', 9)
        # Writing all data in respective fields
        # not null data
        try:
            c = global_functions.add_oneline_text(can=c, text=establishment_solitc_name, pos=(25, 750), campName='Establishment Solicit Name', lenMax=82, lenMin=8)
            if type(c) == type(Response()): return c
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=establishment_solitc_cnes, pos=(470, 750), campName='Establishment Solict CNES', lenMax=7, lenMin=7,valueMin=0, valueMax=99999999, interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=establishment_exec_name, pos=(25, 726), campName='Establishment Exec Name', lenMax=82, lenMin=8)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=establishment_exec_cnes, pos=(470, 726), campName='Establishment Exec CNES', lenMax=7, lenMin=7,valueMin=0, valueMax=99999999, interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_name, pos=(25, 683), campName='Patient Name', lenMax=79, lenMin=7)
            if type(c) == type(Response()): return c
            #Data that change Font Size

            c.setFont('Roboto-Mono', 10)
            c = global_functions.add_cns(can=c, cns=patient_cns, pos=(28, 658), campName='Patient CNS', interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_adressCEP, pos=(482, 566), campName='Patient Adress CEP', lenMax=8, lenMin=8, valueMin=0, valueMax=99999999, nullable=True, interval=' ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=procedure_code, pos=(404, 269), campName='Procedure Code', lenMax=10, lenMin=10, interval='  ')
            if type(c) == type(Response()): return c
            
            c.setFont('Roboto-Mono', 9)
            c = global_functions.add_datetime(can=c, date=patient_birthday, pos=(312, 658), campName='Patient Birthday', hours=False, interval='  ', formated=False)
            if type(c) == type(Response()): return c
            c = global_functions.add_sex_square(can=c, sex=patient_sex, pos_male=(415, 657), pos_fem=(468, 657), campName='Patient Sex', square_size=(8,9))
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_mother_name, pos=(25, 636), campName='Patient Mother Name', lenMax=70, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adress, pos=(25, 593), campName='Patient Adress', lenMax=101, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_adressCity, pos=(25, 566), campName='Patient Adress City', lenMax=58, lenMin=7)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=patient_adressCity_ibgeCode, pos=(388, 566), campName='Patient Adress City IBGE code', lenMax=7, lenMin=7, valueMin=0, valueMax=9999999)
            if type(c) == type(Response()): return c
            c = global_functions.add_UF(can=c, uf=patient_adressUF, pos=(450, 566), campName='Patient Adress UF', interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_morelines_text(can=c, text=main_clinical_signs_symptoms, initial_pos=(25, 530), decrease_ypos= 10, campName='Main Clinical Signs Symptoms', lenMax=1009, charPerLines=101, lenMin=5)
            if type(c) == type(Response()): return c
            c = global_functions.add_morelines_text(can=c, text=conditions_justify_hospitalization, initial_pos=(25, 422), decrease_ypos= 10, campName='Conditions that Justify hospitalization', lenMax=403, charPerLines=101, lenMin=5)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=initial_diagnostic, pos=(25, 314), campName='Initial Diagnostic', lenMax=44, lenMin=5)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=principalCid10, pos=(306, 314), campName='Principal Cid10', lenMax=4, lenMin=3)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=procedure_solicited, pos=(25, 269), campName='Procedure Solicited', lenMax=65, lenMin=6)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=clinic, pos=(25, 246), campName='Clinic', lenMax=18, lenMin=6)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=internation_carater, pos=(128, 246), campName='Internation Caracter', lenMax=19, lenMin=6)
            if type(c) == type(Response()): return c
            c = global_functions.add_document_cns_cpf_rg(can=c, document=prof_solicitor_document, pos_square_cpf=(290, 244), pos_square_cns=(247,244), pos_cns=(335, 246), pos_cpf=(335, 246),campName='Professional Solicitor Document', interval='  ',nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=prof_solicitor_name, pos=(25, 222), campName='Professional Solicitor Name', lenMax=48, lenMin=8)
            if type(c) == type(Response()): return c
            c = global_functions.add_datetime(can=c, date=solicitation_datetime, pos=(300, 222), campName='Solicitation Datetime', hours=False, interval='  ', formated=False)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=autorization_prof_name, pos=(25, 93), campName='Professional Authorizator Name', lenMax=48, lenMin=8)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=emission_org_code, pos=(292, 93), campName='Emission Organization Code', lenMax=17, lenMin=2)
            if type(c) == type(Response()): return c
            c = global_functions.add_document_cns_cpf_rg(can=c, document=autorizaton_prof_document, pos_square_cpf=(95, 66), pos_square_cns=(41,66), pos_cns=(146, 66), pos_cpf=(146, 66),campName='Professional Authorizator Document', interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_datetime(can=c, date=autorizaton_datetime, pos=(30, 30), campName='Authorization Datetime', hours=False, interval='  ', formated=False)
            if type(c) == type(Response()): return c
            c.setFont('Roboto-Mono', 16)       
            c = global_functions.add_oneline_intnumber(can=c, number=hospitalization_autorization_number, pos=(480, 66), campName='Hospitalization autorization Number', lenMax=18, lenMin=1, valueMin=0, valueMax=999999999999999999, centralized=True)
            if type(c) == type(Response()): return c
            c.setFont('Roboto-Mono', 9)       

            
        except:
            if type(c) == type(Response()):
                return c
            else:
                return Response('Some error happen when adding not null data to fields', status=500)

        #Adding data that can be null
        try:
            c = global_functions.add_morelines_text(can=c, text=exam_results, initial_pos=(25, 362), decrease_ypos= 10, campName='Exam Results', lenMax=403, charPerLines=101, lenMin=5, nullable=True)            
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_intnumber(can=c, number=chart_number, pos=(466, 683), campName='Chart Number', lenMax=20, lenMin=1, valueMin=0, valueMax=99999999999999999999, nullable=True)            
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_ethnicity, pos=(510, 658), campName='Patient Ehinicity', lenMax=11, lenMin=4, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=patient_responsible_name, pos=(25, 612), campName='Patient Responsible Name', lenMax=70, lenMin=7, nullable=True)        
            if type(c) == type(Response()): return c
            c = global_functions.add_phonenumber(can=c, number=patient_mother_phonenumber, pos=(415, 631), campName='Patient Mother phone number', nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_phonenumber(can=c, number=patient_responsible_phonenumber, pos=(415, 608), campName='Patient responsible phone number', nullable=True, interval='  ')
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=secondary_cid10, pos=(406, 314), campName='Secondary Cid10', lenMax=4, lenMin=3, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=cid10_associated_causes, pos=(512, 314), campName='Associated causes Cid10', lenMax=4, lenMin=3, nullable=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_markable_square(can=c, option=acident_type, valid_options=['TRAFFIC', 'WORK', 'WORK_PATH'], options_positions=((38,184),(38,170), (38,156)), square_size=(9,9), campName='Acident Type', nullable=True)
            if type(c) == type(Response()): return c

            #Data that change Font Size
            c.setFont('Roboto-Mono', 10)
            c = global_functions.add_cnpj(can=c, cnpj=insurance_company_cnpj, pos=(168,183), campName='Insurance Company CNPJ', nullable=True, interval='  ')           
            if type(c) == type(Response()): return c
            c = global_functions.add_cnpj(can=c, cnpj=company_cnpj, pos=(168,156), campName='Company CNPJ', nullable=True, interval='  ')
            if type(c) == type(Response()): return c            
            

            c.setFont('Roboto-Mono', 9)
            c = global_functions.add_oneline_intnumber(can=c, number=insurance_company_ticket_number, pos=(465, 183), campName='Insurance company ticket number', lenMax=16, lenMin=1, valueMin=0, valueMax=9999999999999999, nullable=True, centralized=True)           
            if type(c) == type(Response()): return c
            c = global_functions.add_oneline_text(can=c, text=insurance_company_series, pos=(543, 183), campName='Insurance Company Series', lenMax=10, lenMin=1, nullable=True, centralized=True)           
            if type(c) == type(Response()): return c
            c = global_functions.add_cnae(can=c, cnae=company_cnae, pos=(434, 156), campName='Company CNAE', nullable=True, formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_cbor(can=c, cbor=company_cbor, pos=(529, 156), campName='Company CBOR', nullable=True, formated=True)
            if type(c) == type(Response()): return c
            c = global_functions.add_markable_square(can=c, option=pension_status, valid_options=['WORKER', 'EMPLOYER', 'AUTONOMOUS', 'UNEMPLOYED', 'RETIRED', 'NOT_INSURED'], options_positions=((33,131),(124,131),(219,131),(305,131),(408,131),(500,131),), square_size=(9,9), campName='Pension Status', nullable=True)
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
        return Response("Error while filling aih sus", status=500)


if __name__ == "__main__":
    import global_functions
    output = fill_pdf_aih_sus(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        establishment_exec_name='Establshment Exec Name',
        establishment_exec_cnes=7654321,
        patient_name='Patient Name',
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_mother_name='Patient Mother Name',
        patient_adress='Patient Adress street neighobourd',
        patient_adressCity='Patient City',
        patient_adressCity_ibgeCode=1234567,
        patient_adressUF='SP',
        patient_adressCEP=12345678,
        main_clinical_signs_symptoms="Patient main clinical signs sympthoms",
        conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',
        initial_diagnostic='Patient Initial Diagnostic',
        principalCid10="A00",
        procedure_solicited='Procedure Solicited',
        procedure_code='1234567890', 
        clinic='Clinic Name', 
        internation_carater='Internation Carater', 
        prof_solicitor_document={'CPF':28445400070},
        prof_solicitor_name='Profissional Solicit Name', 
        solicitation_datetime=datetime.datetime.now(), 
        autorization_prof_name='Autorization professional name', 
        emission_org_code='OrgCode2022', 
        autorizaton_prof_document={'CNS':928976954930007}, 
        autorizaton_datetime=datetime.datetime.now(),
        hospitalization_autorization_number=1234567890,
        exam_results='Xray tibia broken',
        chart_number=1234,
        patient_ethnicity='Preta', 
        patient_responsible_name='Patient Responsible Name', 
        patient_mother_phonenumber=5613248546, 
        patient_responsible_phonenumber=8564721598, 
        secondary_cid10='A01',
        cid10_associated_causes='A02',
        acident_type='traffic', 
        insurance_company_cnpj=37549670000171, 
        insurance_company_ticket_number=123450123456, 
        insurance_company_series='Insurn',
        company_cnpj=37549670000171, 
        company_cnae=5310501, 
        company_cbor=123456, 
        pension_status='retired'
    )

    if type(output) == type(Response()): 
        print(output.response)
    global_functions.write_newpdf(output, "./graphql/mutations/pdfs/aih_sus_teste.pdf")