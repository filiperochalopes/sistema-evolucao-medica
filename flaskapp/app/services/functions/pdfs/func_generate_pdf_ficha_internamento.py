import datetime
from app.services.utils.PdfFichaInternamento import PdfFichaInternamento


def func_generate_pdf_ficha_internamento(document_datetime:datetime.datetime, patient:dict, history_of_present_illness:str, initial_diagnosis_suspicion:str, doctor_name:str, doctor_cns:str, doctor_crm:str, has_additional_health_insurance:bool=None) -> str:
    """fill pdf ficha internamento

    Args:
        document_datetime (datetime.datetime): document_datetime
        patient (dict): patient info
        history_of_present_illness (str): history_of_present_illness
        initial_diagnosis_suspicion (str): initial_diagnosis_suspicion
        doctor_name (str): doctor_name
        doctor_cns (int): doctor_cns
        doctor_crm (str): doctor_crm
        has_additional_health_insurance (bool, optional): has_additional_health_insurance. Defaults to None.

    Returns:
        str: Request with pdf in base64
    """    

    try:
        pdf = PdfFichaInternamento()

        # Writing all data in respective fields
        # not null data
        try:
            # change font size to datetime            
            pdf.add_datetime(date=document_datetime, pos=(475, 740), camp_name='Document Datetime', hours=True, formated=True, centralized=True)
            
            pdf.set_font('Roboto-Mono', 9)
            #Normal font size
            pdf.add_oneline_text(text=patient['name'], pos=(27, 674), camp_name='Patient Name', len_max=64, len_min=7)
            # verify if c is a error at some point
            pdf.add_cns(cns=patient['cns'], pos=(393, 674), camp_name='Patient CNS', formated=True)
            pdf.add_datetime(date=patient['birthdate'], pos=(27, 642), camp_name='Patient Birthday', hours=False, formated=True)
            pdf.add_sex_square(sex=patient['sex'], pos_male=(117, 640), pos_fem=(147, 640), camp_name='Patient Sex', square_size=(9,9))
            pdf.add_oneline_text(text=patient['mother_name'], pos=(194, 642), camp_name='Patient Mother Name', len_max=69, len_min=7)
            pdf.add_document_cns_cpf_rg(document={'cpf': patient['cpf'], 'rg': patient['rg']}, pos_square_cpf=(24, 608), pos_square_rg=(58,608), pos_rg=(92, 610), pos_cpf=(92, 610),camp_name='Pacient Document', formated=True)
            pdf.add_oneline_text(text=patient['address']['street'], pos=(230, 610), camp_name='Patient Adress', len_max=63, len_min=7)
            pdf.add_phonenumber(number=patient['phone'], pos=(173, 547), camp_name='Patient phone number', formated=True)
            pdf.add_oneline_text(text=str(patient['allergies']).replace('[', '').replace(']', ''), pos=(26, 481), camp_name='Patient Drugs Allergies', len_max=100, len_min=5)
            pdf.add_oneline_text(text=str(patient['comorbidities']).replace('[', '').replace(']', ''), pos=(26, 449), camp_name='Patient Commorbidites', len_max=100, len_min=5)
            pdf.add_morelines_text(text=history_of_present_illness, initial_pos=(26, 418), decrease_ypos= 10, camp_name='Current Illness History', len_max=1600, char_per_lines=100, len_min=10)
            pdf.add_oneline_text(text=initial_diagnosis_suspicion, pos=(26, 244), camp_name='Initial Diagnostic Suspicion', len_max=100, len_min=5)
            pdf.add_oneline_text(text=doctor_name, pos=(304, 195), camp_name='Doctor Name', len_max=49, len_min=7)
            pdf.add_cns(cns=doctor_cns, pos=(304, 163), camp_name='Doctor CNS', formated=True)
            pdf.add_oneline_text(text=doctor_crm, pos=(304, 131), camp_name='Doctor CRM', len_max=13, len_min=11)
        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados obrigadorios')

        #Adding data that can be null
        try:
            
            pdf.add_oneline_text(text=patient['address'].get('number'), pos=(24, 580), camp_name='Patient Adress Number', len_max=6, len_min=1,nullable=True)
            pdf.add_oneline_text(text=patient['address'].get('neighborhood'), pos=(66, 580), camp_name='Patient Adress Neighborhood', len_max=31, len_min=4, nullable=True)
            pdf.add_oneline_text(text=patient['address'].get('city'), pos=(243, 580), camp_name='Patient Adress City', len_max=34, len_min=3, nullable=True)
            pdf.add_UF(uf=patient['address'].get('uf'), pos=(444, 580), camp_name='Patient Adress UF', nullable=True)
            pdf.add_CEP(cep=patient['address'].get('zip_code'), pos=(483, 580), camp_name='Patient Adress CEP', nullable=True, formated=True)
            pdf.add_oneline_text(text=patient.get('nationality'), pos=(27, 547), camp_name='Patient nationality', len_max=25, len_min=3, nullable=True)
            patient_weight = patient.get('weight_kg')
            if patient_weight != None:
                patient_weight = int(patient_weight)
            pdf.add_oneline_intnumber(number=patient_weight, pos=(507, 547), camp_name='Patient Estimate Weight', len_max=6, len_min=1, value_min=1, value_max=500, nullable=True)
            if has_additional_health_insurance != None:
                pdf.add_markable_square(option=str(has_additional_health_insurance), valid_options=['SIM','NAO'], options_positions=((419, 544), (380, 544)), camp_name='Has additional Healt insurance', nullable=False)

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
        return Exception("Erro desconhecido enquanto preenchia o documento ficha de internamento")
