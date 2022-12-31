from app.services.utils.PdfFolhaPrescricao import PdfFolhaPrescricao


def func_generate_pdf_folha_prescricao(timestamp_start:str, timestamp_ending:str, prescriptions:dict) -> str:
    """Fill pdf folha prescricao

    Args:
        timestamp_start (str): date start   
        timestamp_ending (str): date end
        prescriptions (dict): prescriptions

    Returns:
        str: Request with pdf in base64
    """    

    try:
        pdf = PdfFolhaPrescricao()
        # Writing all data in respective fields
        # not null data
        try:
            pdf.add_rect_prescription_background(pos=(24, 500))
            pdf.add_oneline_text(text="Testing", pos=(28, 511), camp_name='Testing', len_max=30, len_min=1)
        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido correu enquanto adicionava dados obrigatorios')


        #Get pdf base64
        pdf_base64_enconded = pdf.get_base64()

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except Exception as error:
        return error
    except:
        return Exception("Erro desconhecido enquanto preenchia o documento Folha de Prescricao")