import datetime
from app.services.utils.PdfLme import PdfLme


def func_generate_pdf_lme(requesting_establishment:dict, patient:dict, patient_height:int, cid_10:str, anamnese:str, requesting_professional_name:str, solicitation_date:datetime.datetime, requesting_professional_document:dict, capacity_attest:list, filled_by:list, patient_ethnicity:list, previous_treatment:list, diagnostic:str=None, patient_email:str=None, contacts_phonenumbers:list=None, medicines:list=None) -> str:
    """fill pdf lme (laudo de solicitacao, avaliacao e autorizacao e documentos)

    Args:
        requesting_establishment_name (dict): requesting_establishment info
        patient (dict): patient info
        patient_height (int): patient_height
        cid_10 (str): cid_10
        anamnese (str): anamnese
        requesting_professional_name (str): requesting_professional_name
        solicitation_date (datetime.datetime): solicitation_date
        requesting_professional_document (dict): requesting_professional_document
        capacity_attest (list): list with option and text, eg: ['nao', 'Responsible Name']
        filled_by (list): lits with option name and document, eg ['MEDICO', 'Other name', {'CPF':28445400070}],
        patient_ethnicity (list): list with options and text (if others options is) eg ['SEMINFO', 'Patient Ethnicity']
        previous_treatment (list): list with option and text if sim option eg ['SIM', 'Previout Theatment']
        diagnostic (str, optional): diagnostic. Defaults to None.
        patient_email (str, optional): patient_email. Defaults to None.
        contacts_phonenumbers (list, optional): lsit with contacts_phonenumbers . Defaults to None.
        medicines (list, optional): list with dicts eg: [{"medicine_name":lenght_test[:60], "quant_1_month":"20 comp", "quant_2_month":"15 comp", "quant_3_month":"5 comp"}] . Defaults to None.

    Returns:
        str: Request with pdf in base64
    """    
    try:
        pdf = PdfLme()
        # Writing all data in respective fields
        # not null data

        try:
            pdf.add_oneline_text(text=requesting_establishment['cnes'], pos=(38, 658), camp_name='Establishment Solict CNES', len_max=7, len_min=7,interval='   ')
            patient_weight = int(patient['weight_kg'])
            pdf.add_oneline_intnumber(number=patient_weight, pos=(485, 628), camp_name='Patient Weight', len_max=3, len_min=1,value_min=1, value_max=999, interval='   ')
            pdf.add_oneline_intnumber(number=patient_height, pos=(485, 602), camp_name='Patient Height', len_max=3, len_min=1,value_min=1, value_max=999, interval='   ')
            pdf.add_oneline_text(text=cid_10, pos=(34, 455), camp_name='cid_10', len_max=4, len_min=3, interval='  ')
            pdf.add_datetime(date=solicitation_date, pos=(292, 222), camp_name='Solicitation Datetime', hours=False, interval='   ', formated=False)
            pdf.add_document_cns_cpf_rg(document=requesting_professional_document, pos_square_cpf=(41, 195), pos_square_cns=(84,194), pos_cns=(129, 195), pos_cpf=(129, 195),camp_name='Professional Solicitor Document', interval='  ', square_size=(5, 8))


            pdf.set_font('Roboto-Mono', 9)
            pdf.add_oneline_text(text=requesting_establishment['name'], pos=(206, 658), camp_name='Establishment Solicit Name', len_max=65, len_min=8)
            pdf.add_oneline_text(text=patient['name'], pos=(36, 628), camp_name='Patient Name', len_max=79, len_min=7)
            pdf.add_oneline_text(text=patient['mother_name'], pos=(36, 602), camp_name='Patient Mother Name', len_max=79, len_min=7)
            pdf.add_morelines_text(text=anamnese, initial_pos=(36, 430), decrease_ypos= 10, camp_name='Anamnese', len_max=485, char_per_lines=97, len_min=5)
            pdf.add_oneline_text(text=requesting_professional_name, pos=(36, 224), camp_name='Professional Solicitor Name', len_max=45, len_min=8)
            if type(capacity_attest) != type(list()) or len(capacity_attest) > 2:
                raise Exception('Cappacity Attest deve ser uma lista com 2 itens')
            pdf.add_markable_square_and_onelinetext(option=capacity_attest[0], valid_options=['SIM','NAO'], text_options=['SIM'], text_pos=(308, 268), options_positions=((79, 271), (42,270)), camp_name='Capacity Attest', len_max=46, text=capacity_attest[1], len_min=5, square_size=(5, 8))
            if type(filled_by) != type(list()) or len(filled_by) > 3:
                raise Exception('filled_by deve ser uma lista com 3 itens')
            pdf.add_filled_by(filled_by=filled_by)
            if type(patient_ethnicity) != type(list()) or len(patient_ethnicity) > 2:
                raise Exception('patient_ethnicity deve ser uma lista com 2 itens')
            pdf.add_markable_square_and_onelinetext(option=patient_ethnicity[0], valid_options=['BRANCA','PRETA', 'PARDA', 'AMARELA', 'INDIGENA', 'SEMINFO', 'INFORMAR'], text_options=['INFORMAR'], text_pos=(192, 108), options_positions=((40, 121), (40, 108),(40, 93),(94, 118), (94, 106),(94, 93), (94, 93)),camp_name='Patietn Ethinicity', len_max=31, text=patient_ethnicity[1], len_min=4, square_size=(5, 8))
            if type(previous_treatment) != type(list()) or len(previous_treatment) > 2:
                raise Exception('previous_treatment deve ser uma lista com 2 itens')
            pdf.add_markable_square_and_morelinestext(option=previous_treatment[0], valid_options=['SIM','NAO'],text_options=['SIM'], text_pos=(100, 355), options_positions=((40, 355), (40, 337)), camp_name='Previous Treatment', len_max=170, text=previous_treatment[1], len_min=4, square_size=(5, 8),char_per_lines=85, decrease_ypos=15)

        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados obrigadorios')

        #Adding data that can be null
        try:
            pdf.set_font('Roboto-Mono', 9)
            pdf.add_document_cns_cpf_rg(document={'cpf': patient.get('cpf'), 'cns': patient.get('cns')}, pos_square_cpf=(40, 66), pos_square_cns=(84,66), pos_cns=(129, 66), pos_cpf=(129, 66),camp_name='Patient Document', interval='  ', nullable=True, square_size=(5, 8))
            pdf.add_oneline_text(text=diagnostic, pos=(105, 455), camp_name='Diagnostic', len_max=84, len_min=4, nullable=True)
            pdf.add_oneline_text(text=patient_email, pos=(36, 42), camp_name='Patient Email', len_max=62, len_min=8, nullable=True)
            pdf.add_contact_phonenumbers(phonenumbers=contacts_phonenumbers, pos=(384, 116), interval='  ')
            pdf.add_medicines(medicines=medicines)

        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados opcionais')
        
        pdf_base64_enconded = pdf.get_base64()

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except Exception as error:
        return error
    except:
        return Exception("Erro desconhecido enquanto preenchia o documento aih sus")

