from app.services.utils.PdfRelatorioAlta import PdfRelatorioAlta


def func_generate_pdf_relatorio_alta(document_datetime:str, patient_name:str, patient_cns:str, patient_birthday:str, patient_sex:str, patient_mother_name:str, patient_document:dict, patient_adress:str, evolution:str, doctor_name:str, doctor_cns:str, doctor_crm:str, orientations:str=None) -> str:
    """fill pdf relatorio alta
    
    Args:
        document_datetime (datetime.datetime): document_datetime
        patient_name (str): patient_name
        patient_cns (int): patient_cns
        patient_birthday (datetime.datetime): patient_birthday
        patient_sex (str): patient_sex
        patient_mother_name (str): patient_mother_name
        patient_document (dict): patient_document
        patient_adress (str): patient_adress
        evolution (str): evolution
        doctor_name (str): doctor_name
        doctor_cns (int): doctor_cns
        doctor_crm (str): doctor_crm
        orientations (str, optional): orientations. Defaults to None.

    Returns:
        str: Request with pdf in base64
    """    
    try:
        pdf = PdfRelatorioAlta()
        # Writing all data in respective fields
        # not null data
        try:
            
            pdf.add_datetime(date=document_datetime, pos=(410, 740), camp_name='Document Datetime', hours=True, formated=True)
            
            # change font size to normal            
            pdf.set_font('Roboto-Mono', 9)            
            pdf.add_oneline_text(text=patient_name, pos=(27, 674), camp_name='Patient Name', len_max=64, len_min=7)
            # verify if c is a error at some point
            pdf.add_cns(cns=patient_cns, pos=(393, 674), camp_name='Patient CNS', formated=True)
            pdf.add_datetime(date=patient_birthday, pos=(27, 642), camp_name='Patient Birthday', hours=False, formated=True)
            pdf.add_sex_square(sex=patient_sex, pos_male=(117, 640), pos_fem=(147, 640), camp_name='Patient Sex', square_size=(9,9))
            pdf.add_oneline_text(text=patient_mother_name, pos=(194, 642), camp_name='Patient Mother Name', len_max=69, len_min=7)
            pdf.add_document_cns_cpf_rg(document=patient_document, pos_square_cpf=(24, 608), pos_square_rg=(58,608), pos_rg=(92, 610), pos_cpf=(92, 610),camp_name='Pacient Document', formated=True)
            pdf.add_oneline_text(text=patient_adress, pos=(230, 610), camp_name='Patient Adress', len_max=63, len_min=7)
            pdf.add_oneline_text(text=doctor_name, pos=(304, 195), camp_name='Doctor Name', len_max=49, len_min=7)
            pdf.add_cns(cns=doctor_cns, pos=(304, 163), camp_name='Doctor CNS', formated=True)
            pdf.add_oneline_text(text=doctor_crm, pos=(304, 131), camp_name='Doctor CRM', len_max=13, len_min=11)
            pdf.add_morelines_text(text=evolution, initial_pos=(26, 540), decrease_ypos=10, camp_name='Evolution Resume', len_max=2100, len_min=10, char_per_lines=100)
        
        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados obrigadorios')
            
        #Adding data that can be null
        try:
            pdf.add_morelines_text(text=orientations, initial_pos=(26, 312), decrease_ypos=10, camp_name='Orientations', len_max=800, len_min=10, char_per_lines=100, nullable=True)
        
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
        return Exception("Erro desconhecido enquanto preenchia o documento de relatorio de alta")
