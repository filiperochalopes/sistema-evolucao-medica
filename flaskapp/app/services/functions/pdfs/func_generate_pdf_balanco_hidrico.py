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

            pdf.set_font('Roboto-Mono', 16)
            
            pdf.add_datetime(date=created_at, pos=(717, 556), camp_name="Document created date (upper position)", hours=False)


            pdf.set_font('Roboto-Mono', 11)
            pdf.add_fluid_balance(balances=fluid_balance)

            pdf.set_font('Roboto-Mono', 13)
            pdf.add_oneline_text(text=f'{patient_weight}kg', pos=(531, 256), camp_name='Peso do Paciente', len_max=8)
            # Add metrics in pdf
            pdf.add_metrics()
            pdf.add_morelines_text(text=pdf.diurese_info, initial_pos=(417, 149), camp_name='Metricas da diurese', char_per_lines=46, len_max=80, decrease_ypos=15)

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