import datetime
from app.services.utils.PdfAihSus import PdfAihSus



def func_generate_pdf_aih_sus(requesting_establishment:dict, patient:dict, main_clinical_signs_symptoms:str, conditions_justify_hospitalization:str, initial_diagnosis:str, principal_cid_10:str, requesting_professional_document:dict, requesting_professional_name:str, request_date:datetime.datetime, establishment_exec:dict=None,requested_procedure:str=None, procedure_code:str=None, clinic:str=None, internation_carater:str=None, emission_org_code:str=None, hospitalization_authorization_number:str=None, authorization_professional_document:dict=None, authorization_date:datetime.datetime=None, professional_authorization_name:str=None, exam_results:str=None, chart_number:str=None, patient_responsible_name:str=None, patient_mother_phonenumber:str=None, patient_responsible_phonenumber:str=None, secondary_cid_10:str=None, cid_10_associated_causes:str=None, acident_type:str=None, insurance_company_cnpj:str=None, insurance_company_ticket_number:str=None, insurance_company_series:str=None,company_cnpj:str=None, company_cnae:int=None, company_cbor:int=None, pension_status:str=None) -> str:
    """fill pdf aih sus 

    Args:
        requesting_establishment (dict): requesting_establishment
        establishment_exec (dict): establishment_exec
        patient (dict): Patient info
        main_clinical_signs_symptoms (str): main_clinical_signs_symptoms
        conditions_justify_hospitalization (str): conditions_justify_hospitalization
        initial_diagnosis (str): initial_diagnosis
        principal_cid_10 (str): principal_cid_10
        requested_procedure (str): requested_procedure
        procedure_code (str): procedure_code
        clinic (str): clinic
        internation_carater (str): internation_carater
        requesting_professional_document (dict): dict requesting_professional_document
        requesting_professional_name (str): requesting_professional_name
        request_date (datetime.datetime): request_date
        professional_authorization_name (str): professional_authorization_name
        emission_org_code (str): emission_org_code
        authorization_professional_document (dict): authorization_professional_document
        authorization_date (datetime.datetime): authorization_date
        hospitalization_authorization_number (str): hospitalization_authorization_number
        exam_results (str, optional): exam_results. Defaults to None.
        chart_number (str, optional): chart_number. Defaults to None.
        patient_responsible_name (str, optional): patient_responsible_name. Defaults to None.
        patient_mother_phonenumber (int, optional): patient_mother_phonenumber. Defaults to None.
        patient_responsible_phonenumber (int, optional): patient_responsible_phonenumber. Defaults to None.
        secondary_cid_10 (str, optional): secondary_cid_10. Defaults to None.
        cid_10_associated_causes (str, optional): cid_10_associated_causes. Defaults to None.
        acident_type (str, optional): acident_type. Defaults to None.
        insurance_company_cnpj (int, optional): insurance_company_cnpj. Defaults to None.
        insurance_company_ticket_number (str, optional): insurance_company_ticket_number. Defaults to None.
        insurance_company_series (str, optional): insurance_company_series. Defaults to None.
        company_cnpj (int, optional): company_cnpj. Defaults to None.
        company_cnae (int, optional): company_cnae. Defaults to None.
        company_cbor (int, optional): company_cbor. Defaults to None.
        pension_status (str, optional): pension_status. Defaults to None.

    Returns:
        str: Request with pdf in base64
    """
    try:
        pdf = PdfAihSus()
        # Writing all data in respective fields
        # not null data
        try:     
            pdf.add_oneline_text(text=requesting_establishment['name'], pos=(25, 750), camp_name='Establishment Solicit Name', len_max=82, len_min=8)
            pdf.add_oneline_text(text=requesting_establishment['cnes'], pos=(470, 750), camp_name='Establishment Solict CNES', len_max=7, len_min=7,interval='  ')
            pdf.add_oneline_text(text=patient['name'], pos=(25, 683), camp_name='Patient Name', len_max=79, len_min=7)
            #Data that change Font Size

            pdf.set_font('Roboto-Mono', 10)
            pdf.add_cns(cns=patient['cns'], pos=(28, 658), camp_name='Patient CNS', interval='  ')
            pdf.add_oneline_text(text=patient['address']['zip_code'], pos=(482, 566), camp_name='Patient Adress CEP', len_max=8, len_min=8, interval=' ')
            
            pdf.set_font('Roboto-Mono', 9)
            pdf.add_datetime(date=patient['birthdate'], pos=(312, 658), camp_name='Patient Birthday', hours=False, interval='  ', formated=False)
            pdf.add_sex_square(sex=patient['sex'], pos_male=(415, 657), pos_fem=(468, 657), camp_name='Patient Sex', square_size=(8,9))
            pdf.add_oneline_text(text=patient['mother_name'], pos=(25, 636), camp_name='Patient Mother Name', len_max=70, len_min=7)
            pdf.add_oneline_text(text=patient['address']['street'], pos=(25, 593), camp_name='Patient Adress', len_max=101, len_min=7)
            pdf.add_oneline_text(text=patient['address']['city'], pos=(25, 566), camp_name='Patient Adress City', len_max=58, len_min=3)
            pdf.add_oneline_text(text=patient['address']['ibge_city_code'], pos=(388, 566), camp_name='Patient Adress City IBGE code', len_max=7, len_min=7)
            pdf.add_UF(uf=patient['address']['uf'], pos=(450, 566), camp_name='Patient Adress UF', interval='  ')
            pdf.add_morelines_text(text=main_clinical_signs_symptoms, initial_pos=(25, 530), decrease_ypos= 10, camp_name='Main Clinical Signs Symptoms', len_max=1009, char_per_lines=101, len_min=5)
            pdf.add_morelines_text(text=conditions_justify_hospitalization, initial_pos=(25, 422), decrease_ypos= 10, camp_name='Conditions that Justify hospitalization', len_max=403, char_per_lines=101, len_min=5)
            pdf.add_oneline_text(text=initial_diagnosis, pos=(25, 314), camp_name='Initial Diagnostic', len_max=44, len_min=5)
            pdf.add_oneline_text(text=principal_cid_10, pos=(306, 314), camp_name='Principal Cid10', len_max=4, len_min=3)
            pdf.add_document_cns_cpf_rg(document=requesting_professional_document, pos_square_cpf=(290, 244), pos_square_cns=(247,244), pos_cns=(335, 246), pos_cpf=(335, 246),camp_name='Professional Solicitor Document', interval='  ')
            pdf.add_oneline_text(text=requesting_professional_name, pos=(25, 222), camp_name='Professional Solicitor Name', len_max=48, len_min=8)
            pdf.add_datetime(date=request_date, pos=(300, 222), camp_name='Solicitation Datetime', hours=False, interval='  ', formated=False)   

            
        except Exception as error:
            return error
        
        except:
            return Exception('Erro desconhecido correu enquanto adicionava dados obrigatorios')

        #Adding data that can be null
        try:
            pdf.add_oneline_text(text=requested_procedure, pos=(25, 269), camp_name='Procedure Solicited', len_max=65, len_min=6, nullable=True)
            pdf.add_oneline_text(text=procedure_code, pos=(404, 269), camp_name='Procedure Code', len_max=10, len_min=10, interval='  ', nullable=True)
            pdf.add_oneline_text(text=clinic, pos=(25, 246), camp_name='Clinic', len_max=18, len_min=6, nullable=True)
            pdf.add_oneline_text(text=internation_carater, pos=(128, 246), camp_name='Internation Caracter', len_max=19, len_min=6, nullable=True)
            if establishment_exec is not None:
                pdf.add_oneline_text(text=establishment_exec.get('name'), pos=(25, 726), camp_name='Establishment Exec Name', len_max=82, len_min=8, nullable=True)
                pdf.add_oneline_text(text=establishment_exec.get('cnes'), pos=(470, 726), camp_name='Establishment Exec CNES', len_max=7, len_min=7,interval='  ', nullable=True)
            pdf.add_morelines_text(text=exam_results, initial_pos=(25, 362), decrease_ypos= 10, camp_name='Exam Results', len_max=403, char_per_lines=101, len_min=5, nullable=True)            
            pdf.add_oneline_text(text=chart_number, pos=(466, 683), camp_name='Chart Number', len_max=20, len_min=1,nullable=True)            
            pdf.add_oneline_text(text=patient.get('ethnicity'), pos=(510, 658), camp_name='Patient Ehinicity', len_max=11, len_min=4, nullable=True)
            pdf.add_oneline_text(text=patient_responsible_name, pos=(25, 612), camp_name='Patient Responsible Name', len_max=70, len_min=7, nullable=True)        
            pdf.add_phonenumber(number=patient_mother_phonenumber, pos=(415, 631), camp_name='Patient Mother phone number', nullable=True, interval='  ')
            pdf.add_phonenumber(number=patient_responsible_phonenumber, pos=(415, 608), camp_name='Patient responsible phone number', nullable=True, interval='  ')
            pdf.add_oneline_text(text=secondary_cid_10, pos=(406, 314), camp_name='Secondary Cid10', len_max=4, len_min=3, nullable=True)
            pdf.add_oneline_text(text=cid_10_associated_causes, pos=(512, 314), camp_name='Associated causes Cid10', len_max=4, len_min=3, nullable=True)
            pdf.add_markable_square(option=acident_type, valid_options=['TRAFFIC', 'WORK', 'WORK_PATH'], options_positions=((38,184),(38,170), (38,156)), square_size=(9,9), camp_name='Acident Type', nullable=True)

            pdf.set_font('Roboto-Mono', 16)       
            pdf.add_oneline_text(text=hospitalization_authorization_number, pos=(480, 66), camp_name='Hospitalization authorization Number', len_max=18, len_min=1, centralized=True, nullable=True)
            
            #Data that change Font Size
            pdf.set_font('Roboto-Mono', 10)
            pdf.add_cnpj(cnpj=insurance_company_cnpj, pos=(168,183), camp_name='Insurance Company CNPJ', nullable=True, interval='  ')           
            pdf.add_cnpj(cnpj=company_cnpj, pos=(168,156), camp_name='Company CNPJ', nullable=True, interval='  ')
            

            pdf.set_font('Roboto-Mono', 9)
            pdf.add_oneline_text(text=insurance_company_ticket_number, pos=(465, 183), camp_name='Insurance company ticket number', len_max=16, len_min=1,nullable=True, centralized=True)           
            pdf.add_oneline_text(text=insurance_company_series, pos=(543, 183), camp_name='Insurance Company Series', len_max=10, len_min=1, nullable=True, centralized=True)           
            pdf.add_cnae(cnae=company_cnae, pos=(434, 156), camp_name='Company CNAE', nullable=True, formated=True)
            pdf.add_cbor(cbor=company_cbor, pos=(529, 156), camp_name='Company CBOR', nullable=True, formated=True)
            pdf.add_markable_square(option=pension_status, valid_options=['WORKER', 'EMPLOYER', 'AUTONOMOUS', 'UNEMPLOYED', 'RETIRED', 'NOT_INSURED'], options_positions=((33,131),(124,131),(219,131),(305,131),(408,131),(500,131),), square_size=(9,9), camp_name='Pension Status', nullable=True)
            pdf.add_oneline_text(text=emission_org_code, pos=(292, 93), camp_name='Emission Organization Code', len_max=17, len_min=2, nullable=True)
            pdf.add_oneline_text(text=professional_authorization_name, pos=(25, 93), camp_name='Professional Authorizator Name', len_max=48, len_min=8, nullable=True)
            pdf.add_document_cns_cpf_rg(document=authorization_professional_document, pos_square_cpf=(95, 66), pos_square_cns=(41,66), pos_cns=(146, 66), pos_cpf=(146, 66),camp_name='Professional Authorizator Document', interval='  ', nullable=True)
            pdf.add_datetime(date=authorization_date, pos=(30, 30), camp_name='Authorization Datetime', hours=False, interval='  ', formated=False, nullable=True)
            

        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados opcionais')


        #Get pdf base64
        pdf_base64_enconded = pdf.get_base64()

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except Exception as error:
        return error
    except:
        return Exception("Erro desconhecido enquanto preenchia o documento Aih Sus")