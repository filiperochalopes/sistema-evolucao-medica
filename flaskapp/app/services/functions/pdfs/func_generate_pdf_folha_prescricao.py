from app.services.utils.PdfFolhaPrescricao import PdfFolhaPrescricao


def func_generate_pdf_folha_prescricao(timestamp_start:str, timestamp_ending:str, prescriptions:list) -> str:
    """Fill pdf folha prescricao

    Args:
        timestamp_start (str): date start   
        timestamp_ending (str): date end
        prescriptions (list): prescriptions

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


        try:
            pdf.add_abbreviated_name(name=patient['name'], pos=(535, 550), camp_name='Patient Name', len_max=26, centralized=True)

            pdf.set_font('Roboto-Mono', 12)
            pdf.add_prescriptions(prescriptions=prescriptions)
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