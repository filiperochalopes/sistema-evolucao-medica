from app.services.utils.PdfFolhaPrescricao import PdfFolhaPrescricao
from datetime import datetime, timezone, timedelta
import sys

def func_generate_pdf_folha_prescricao(created_at:str, patient:dict, prescriptions:list, 
professional:dict=None
) -> str:
    """Fill pdf folha prescricao

    Args:
        created_at (str): created date
        printed_at (str): Printed date
        prescriptions (list): prescriptions
        professional (dict): Professional info

    Returns:
        str: Request with pdf in base64
    """

    try:
        pdf = PdfFolhaPrescricao()
        # Writing all data in respective fields
        # not null data        
        try:
            pdf.add_abbreviated_name(name=patient['name'], pos=(535, 550), field_name='Patient Name', len_max=26, centralized=True, uppered=True)

            pdf.set_font('Roboto-Mono', 16)
            pdf.add_datetime(date=created_at, pos=(717, 556), field_name="Document created date (upper position)", hours=False)

            pdf.set_font('Roboto-Mono', 12)
            pdf.add_prescriptions(prescriptions=prescriptions)

            tmz = timezone(offset=timedelta(hours=-3))
            printed_at = datetime.now(tz=tmz).isoformat()
            pdf.add_datetime(date=printed_at, pos=(692, 20), field_name="Document printed date (Bottom position)", nullable=True)
            pdf.add_datetime(date=created_at, pos=(673, 34), field_name="Document created date (Bottom position)")

            pdf.set_font('Roboto-Mono', 11)
            current_user_info = pdf.create_professional_info_text(professional=professional, nullable=False)
            pdf.add_oneline_text(text=current_user_info, pos=(812, 50), field_name='Professional Info', len_max=67, right_align=True)
        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido enquanto adicionava dados obrigatorios')


        #Get pdf base64
        pdf_base64_enconded = pdf.get_base64()

        return {
            "base64Pdf": str(pdf_base64_enconded)[2:-1]
        }
    except Exception as error:
        return error
    except:
        return Exception("Erro desconhecido enquanto preenchia o documento Folha de Prescricao")