from app.services.utils.PdfPrescricaoMedica import PdfPrescricaoMedica


def func_generate_pdf_prescricao_medica(document_datetime:str, patient:dict, professional:dict, prescription:list) -> str:
    """fill pdf prescricao medica with 2 pages 

    Args:
        document_datetime (str): document_datetime in %d/%m/%Y %H:%M format
        patient (dict): patient info
        prescription (list): list of dicts precriptions, like [{"medicine_name":"Dipirona 500mg", "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}]

    Returns:
        str: Request with pdf in base64
    """    

    
    try:
        try:
            pdf = PdfPrescricaoMedica()

            initial_date_X_pos = 294
            initial_name_X_pos = 120
            initial_professional_X_pos = 190
            for x in range(0, 2):
                pdf.add_datetime(date=document_datetime, pos=(initial_date_X_pos, 38), camp_name='Document Datetime', hours=False, interval='  ', formated=False)
                pdf.add_oneline_text(text=patient['name'], pos=(initial_name_X_pos, 505), camp_name='Patient Name', len_max=34, len_min=7)
                pdf.add_oneline_text(text=pdf.create_professional_info(professional=professional), pos=(initial_professional_X_pos, 60), len_max=800, centralized=True, camp_name='Professional Info') 
                initial_date_X_pos += 450
                initial_name_X_pos += 451
                initial_professional_X_pos += 451

            pdf.set_font('Roboto-Mono', 10)
            pdf.add_prescription(prescription=prescription)
        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados obrigadorios')
    

        #Get pdf base64
        pdf_base64_enconded = pdf.get_base64()

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except Exception as error:
        return error
    except:
        return Exception('Erro desconhecido enquanto preenchia o documento de prescricao medica')

