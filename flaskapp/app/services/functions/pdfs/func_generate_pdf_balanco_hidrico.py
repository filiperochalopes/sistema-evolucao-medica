from app.services.utils.PdfBalancoHidrico import PdfBalancoHidrico


def func_generate_pdf_balanco_hidrico(created_at:str, patient_name:str, patient_weight, fluid_balance:list,
#current_user: dict
) -> str:

    

    try:
        pdf = PdfBalancoHidrico()
        # Writing all data in respective fields
        # not null data

        try:
            pdf.add_abbreviated_name(name=patient_name, pos=(535, 550), camp_name='Patient Name', len_max=26, centralized=True, uppered=True)


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
        return Exception("Erro desconhecido enquanto preenchia o documento Balanco Hidrico")