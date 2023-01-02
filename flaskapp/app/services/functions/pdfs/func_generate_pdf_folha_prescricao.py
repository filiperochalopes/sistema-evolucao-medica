from app.services.utils.PdfFolhaPrescricao import PdfFolhaPrescricao
import datetime


def func_generate_pdf_folha_prescricao(created_at:str, printed_at:str, patient_name:str, prescriptions:list) -> str:
    """Fill pdf folha prescricao

    Args:
        created_at (str): created date
        printed_at (str): Printed date
        patient_name (str): Patient Name
        prescriptions (list): prescriptions
        current_user (dict): Professional info

    Returns:
        str: Request with pdf in base64
    """

    try:
        pdf = PdfFolhaPrescricao()
        # Writing all data in respective fields
        # not null data

        # Provisory data to test
        lenght_test = ''
        for x in range(0, 1100):
            lenght_test += str(x)
        patient = {'name': 'Marcos Antonia de Freitas testando o Nome'}
        current_user = {'name': 'Professioanl Info', 'professional_document_uf': 'BA', 'professional_document_number':'12457'}
        today = '12/12/2020 15:10'
        today_day = '12/12/2020'


        try:
            pdf.add_abbreviated_name(name=patient_name, pos=(535, 550), camp_name='Patient Name', len_max=26, centralized=True, uppered=True)

            pdf.set_font('Roboto-Mono', 16)
            pdf.add_datetime(date=created_at[:-6], pos=(717, 556), camp_name="Document created date (upper position)", hours=False)

            pdf.set_font('Roboto-Mono', 12)
            pdf.add_prescriptions(prescriptions=prescriptions)
            pdf.add_datetime(date=printed_at, pos=(673, 34), camp_name="Document printed date (Bottom position)")
            pdf.add_datetime(date=created_at, pos=(692, 20), camp_name="Document created date (Bottom position)")

            pdf.set_font('Roboto-Mono', 11)
            current_user_info = pdf.create_professional_info_text(professional=current_user, nullable=False)
            pdf.add_oneline_text(text=current_user_info, pos=(812, 50), camp_name='Professional Info', len_max=67, right_align=True)
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