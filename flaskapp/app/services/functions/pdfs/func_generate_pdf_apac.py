import datetime
from app.services.utils.PdfApac import PdfApac


def func_generate_pdf_apac(requesting_establishment:dict, patient:dict, main_procedure:dict,patient_responsible_name:str=None, patient_color:str=None, document_chart_number:str=None, procedure_justification_description:str=None, procedure_justification_main_cid_10:str=None, procedure_justification_sec_cid_10:str=None, procedure_justification_associated_cause_cid_10:str=None, procedure_justification_observations:str=None,requesting_professional_document:dict=None, requesting_professional_name:str=None, establishment_exec:dict=None, contacts_phonenumbers:list=None,solicitation_date:datetime.datetime=None, professional_authorization_name:str=None, emission_org_code:str=None, authorization_professional_document:dict=None, authorization_date:datetime.datetime=None, signature_date:datetime.datetime=None, validity_period_start:datetime.datetime=None, validity_period_end:datetime.datetime=None, secondaries_procedures:list=None) -> str:
    """fill pdf apac

    Args:
        requesting_establishment (dict): requesting_establishment
        establishment_exec (dict): establishment_exec
        patient (dict): info
        main_procedure (dict): dict with name, code and quat of main procedure
        patient_mother_phonenumber (int, optional): patient_mother_phonenumber. Defaults to None.
        patient_responsible_name (str, optional): patient_responsible_name. Defaults to None.
        patient_responsible_phonenumber (int, optional): patient_responsible_phonenumber. Defaults to None.
        patient_color (str, optional): patient_color. Defaults to None.
        document_chart_number (str, optional): document_chart_number. Defaults to None.
        procedure_justification_description (str, optional): procedure_justification_description. Defaults to None.
        procedure_justification_main_cid_10 (str, optional): procedure_justification_main_cid_10. Defaults to None.
        procedure_justification_sec_cid_10 (str, optional): procedure_justification_sec_cid_10. Defaults to None.
        procedure_justification_associated_cause_cid_10 (str, optional): procedure_justification_associated_cause_cid_10. Defaults to None.
        procedure_justification_observations (str, optional): procedure_justification_observations. Defaults to None.
        requesting_professional_document (dict, optional): requesting_professional_document. Defaults to None.
        requesting_professional_name (str, optional): requesting_professional_name. Defaults to None.
        solicitation_date (datetime.datetime, optional): solicitation_date. Defaults to None.
        professional_authorization_name (str, optional): professional_authorization_name. Defaults to None.
        emission_org_code (str, optional): emission_org_code. Defaults to None.
        authorization_professional_document (dict, optional): authorization_professional_document. Defaults to None.
        authorization_date (datetime.datetime, optional): authorization_date. Defaults to None.
        signature_date (datetime.datetime, optional): signature_date. Defaults to None.
        validity_period_start (datetime.datetime, optional): validity_period_start. Defaults to None.
        validity_period_end (datetime.datetime, optional): validity_period_end. Defaults to None.
        secondaries_procedures (list, optional): list with dict with procedure, eg: 
        [{"procedure_name":"Procedure Name", "procedure_code":"cod4521578", "quant":5}, 
        {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]
        . Defaults to None.

    Returns:
        str: Request with pdf in base64
    """    
    try:
        pdf = PdfApac()
        # Writing all data in respective fields
        # not null data
        try:
            pdf.add_cns(cns=patient['cns'], pos=(36, 678), camp_name='Patient CNS', interval='  ')
            pdf.add_procedure(procedure=main_procedure, code_pos=(36,542), name_pos=(220, 542), quant_pos=(508, 542), camp_name='Main Procedure')

            pdf.set_font('Roboto-Mono', 9)
            pdf.add_oneline_text(text=requesting_establishment['name'], pos=(36, 742), camp_name='Establishment Solict Name', len_max=77, len_min=7)
            pdf.add_oneline_text(text=patient['name'], pos=(36, 702), camp_name='Patient Name', len_max=67, len_min=7)
            pdf.add_sex_square(sex=patient['sex'], pos_male=(423, 699), pos_fem=(456, 699), camp_name='Patient Sex', square_size=(9,9))
            pdf.add_datetime(date=patient['birthdate'], pos=(315, 678), camp_name='Patient Birthday', hours=False, interval='  ', formated=False)
            pdf.add_oneline_text(text=patient['address']['city'], pos=(36, 584), camp_name='Patient Adress City', len_max=58, len_min=3)
            pdf.add_oneline_text(text=requesting_establishment['cnes'], pos=(468, 742), camp_name='Establishment Solict CNES', len_max=7, len_min=7)
        
        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados obrigatorios')

        #Adding data that can be null
        try:
            pdf.set_font('Roboto-Mono', 11)
            if establishment_exec is None:
                # Create empty dict
                establishment_exec = {'':''}
            pdf.add_oneline_text(text=establishment_exec.get('cnes'), pos=(450, 28), camp_name='Establishment Exec CNES', len_max=7, len_min=7,interval=' ', nullable=True)
            pdf.set_font('Roboto-Mono', 9)
            pdf.add_oneline_text(text=patient.get('mother_name'), pos=(36, 654), camp_name='Patient Mother Name', len_max=67, len_min=7, nullable=True)
            pdf.add_oneline_text(text=patient['address'].get('street'), pos=(36, 608), camp_name='Patient Adress', len_max=97, len_min=7, nullable=True)
            pdf.add_oneline_text(text=patient['address'].get('zip_code'), pos=(476, 582), camp_name='Patient Adress CEP', len_max=8, len_min=8, nullable=True, interval=' ')
            pdf.add_oneline_text(text=patient['address'].get('ibge_city_code'), pos=(370, 582), camp_name='Patient Adress City IBGE code', len_max=7, len_min=7, nullable=True)
            pdf.add_oneline_text(text=establishment_exec.get('name'), pos=(36, 30), camp_name='Establishment Exec Name', len_max=71, len_min=5, nullable=True)
            pdf.add_UF(uf=patient['address']['uf'], pos=(443, 582), camp_name='Patient Adress UF', nullable=True, interval='  ')
            pdf.add_oneline_text(text=str(procedure_justification_description).upper(), pos=(36, 344), camp_name='Procedure Justification Description', len_max=55, len_min=4, nullable=True)
            pdf.add_oneline_text(text=patient_responsible_name, pos=(36, 630), camp_name='Patient Responsible Name', len_max=67, len_min=7, nullable=True)

            pdf.add_contact_phonenumbers(phone_numbers=contacts_phonenumbers, pos=(409, 650), interval='  ', y_decrease=24, nullable=True)

            pdf.add_oneline_text(text=patient_color, pos=(404, 678), camp_name='Patient Color', len_max=10, len_min=4, nullable=True)
            pdf.add_oneline_text(text=patient.get('ethnicity'), pos=(470, 678), camp_name='Patient Ehinicity', len_max=17, len_min=4, nullable=True)
            pdf.add_oneline_text(text=document_chart_number, pos=(483, 702), camp_name='Document Chart Number', len_max=14, len_min=1, nullable=True)
            pdf.add_oneline_text(text=procedure_justification_main_cid_10, pos=(352, 344), camp_name='Procedure Justification main CID10', len_max=4, len_min=3, nullable=True)
            pdf.add_oneline_text(text=procedure_justification_sec_cid_10, pos=(420, 344), camp_name='Procedure Justification secondary CID10', len_max=4, len_min=3, nullable=True)
            pdf.add_oneline_text(text=procedure_justification_associated_cause_cid_10, pos=(505, 344), camp_name='Procedure Justification Associated Causes CID10', len_max=4, len_min=3, nullable=True)
            pdf.add_oneline_text(text=requesting_professional_name, pos=(36, 204), camp_name='Profissional Solicitor Name', len_max=48, len_min=5, nullable=True)
            pdf.add_oneline_text(text=professional_authorization_name, pos=(36, 136), camp_name='Profissional Authorizator Name', len_max=46, len_min=5, nullable=True)
            pdf.add_oneline_text(text=emission_org_code, pos=(290, 136), camp_name='Emission Org Code', len_max=16, len_min=2, nullable=True)
            pdf.add_datetime(date=solicitation_date, pos=(310, 204), camp_name='Solicitation Datetime', hours=False, interval='  ', formated=False, nullable=True)
            pdf.add_datetime(date=authorization_date, pos=(36, 68), camp_name='Authorization Datetime', hours=False,formated=True, nullable=True)
            pdf.add_datetime(date=signature_date, pos=(154, 68), camp_name='Signature Datetime', hours=False, interval='  ', formated=False, nullable=True)
            pdf.add_datetime(date=validity_period_start, pos=(402, 66), camp_name='Validity Period Start', hours=False, interval='  ', formated=False, nullable=True)
            pdf.add_datetime(date=validity_period_end, pos=(492, 66), camp_name='Validity Period End', hours=False, interval='  ', formated=False, nullable=True)
            pdf.add_secondary_procedures(procedures=secondaries_procedures)
            pdf.add_morelines_text(text=procedure_justification_observations, initial_pos=(36, 318), decrease_ypos= 10, camp_name='Procedure justification Observations', len_max=776, char_per_lines=97, len_min=5, nullable=True)
            pdf.add_document_cns_cpf_rg(document=requesting_professional_document, pos_square_cpf=(103, 180), pos_square_cns=(51,180), pos_cns=(151, 181), pos_cpf=(151, 181),camp_name='Professional Solicitor Document', interval='  ',nullable=True)
            pdf.add_document_cns_cpf_rg(document=authorization_professional_document, pos_square_cpf=(103, 104), pos_square_cns=(51,104), pos_cns=(149, 105), pos_cpf=(151, 105),camp_name='Professional Authorizator Document', interval='  ',nullable=True)
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
        return Exception("Erro desconhecido enquanto preenchia o documento Apac")

