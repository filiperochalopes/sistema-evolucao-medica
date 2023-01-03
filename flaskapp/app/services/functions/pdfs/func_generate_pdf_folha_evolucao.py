from app.services.utils.PdfFolhaEvolucao import PdfFolhaEvolucao


def func_generate_pdf_folha_evolucao(created_at:str, patient_name:str, evolutions:list, measures:list, 
#current_user: dict
) -> str:

    

    try:
        pdf = PdfFolhaEvolucao()
        # Writing all data in respective fields
        # not null data

        # Provisory data to test
        lenght_test = ''
        for x in range(0, 1100):
            lenght_test += str(x)
        patient = {'name': 'Marcos Antonia de Freitas testando o Nome'}
        professional = {'name': 'Professioanl Complete name', 'professional_document_uf': 'BA', 'professional_document_number':'12457'}
        today = '12/12/2020 15:10'
        today_day = '12/12/2020'


        try:
            pdf.add_abbreviated_name(name=patient['name'], pos=(535, 550), camp_name='Patient Name', len_max=26, centralized=True, uppered=True)

            pdf.set_font('Roboto-Mono', 16)
            pdf.add_datetime(date=today_day, pos=(717, 556), camp_name="Document created date (upper position)", hours=False)

            pdf.set_font('Roboto-Mono', 11)

            #Data that arent in mutations wet
            if len(evolutions) > 4:
                raise Exception('You cant add more than 4 evolutions')
            
            # Add evolutions
            pdf.add_evolutions(evolutions=evolutions)

            #Add measures
            pdf.set_font('Roboto-Mono', 9)
            pdf.add_measures(measures=measures)

            



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
        return Exception("Erro desconhecido enquanto preenchia o documento Folha de Evolucao")