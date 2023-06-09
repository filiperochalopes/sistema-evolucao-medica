import datetime
from app.services.utils.PdfEvolCompact import PdfEvolCompact


def func_generate_pdf_evol_compact(patient: dict, evolution: dict,document_created_at: str, admission_history: dict, prescription:list, prescription_cares:str, measures:list) -> str:
    try: 
        pdf = PdfEvolCompact()
        lenght_test = ''
        for x in range(0, 1100):
            lenght_test += str(x)
        try:
            pdf.add_abbreviated_name(name=patient['name'], pos=(554, 553), field_name="Patient Name", len_max=31, len_min=5, uppered=True, centralized=True)
            pdf.add_datetime(date=document_created_at, pos=(716, 553), field_name="Document Date", hours=False, formated=True)

            pdf.set_font('Roboto-Mono', 10)
            patient_sex = patient['sex']
            if len(patient_sex) == 1:
                if patient_sex == 'M':
                    patient_sex = "Masculino"
                elif patient_sex == 'F':
                    patient_sex = "Feminino"
                else:
                    raise Exception('Sexo do paciente deve ser M ou F')

            patient_weight = int(patient['weight_kg'])
            # pdf.add_oneline_text(text=patient_sex, pos=(47, 497), field_name="Patient Sex", len_max=11, len_min=5)
            # patient_weight = int(patient['weight_kg'])
            # pdf.add_oneline_text(text=f"{patient_weight}kg", pos=(47, 485), field_name="Patient Weight", len_max=11, len_min=1)
            # pdf.add_datetime(date=patient['birthdate'], pos=(196, 497), field_name="Patient Birthday", hours=False, formated=True)
            # pdf.add_cns(cns=patient['cns'], pos=(115, 485), field_name='Patient CNS', formated=False)
            # pdf.set_font('Roboto-Mono', 8)
            # pdf.add_oneline_text(text=str(patient['comorbidities']).replace("'", "").replace('[', '').replace(']', ''), pos=(90, 472), field_name='Patient Commorbidites', len_max=38, len_min=5)
            # pdf.add_morelines_text(text=str(patient['allergies']).replace("'", "").replace('[', '').replace(']', ''), initial_pos=(61, 461), field_name='Patient Drugs Allergies', len_max=150, len_min=5, char_per_lines=44, decrease_ypos=10, max_lines_amount=4)

            print(patient_data)

            patient_allergies = str(patient['allergies']).replace("'", "").replace('[', '').replace(']', '')
            patient_commorbidities = str(patient['comorbidities']).replace("'", "").replace('[', '').replace(']', '')

            pdf.add_morelines_text(text=f'Sexo: {patient_sex}  Peso: {patient_weight}kg  CNS: {patient["cns"]}  Comorbidades: {patient_commorbidities}  Alergias: {patient_allergies}', initial_pos=(20, 497), field_name='Patient Info', len_max=403, len_min=5, char_per_lines=42, decrease_ypos=11, max_lines_amount=8)

            pdf.set_font('Roboto-Condensed-Bold', 10)
            pdf.can.setFillColorRGB(255, 255, 255, 1)
            # Patient Data with White text
            pdf.add_abbreviated_name(name=patient['name'], pos=(19, 515), field_name="Patient Name", len_max=31, len_min=5, uppered=True)
            patient_age = pdf.get_patient_age(birthdate=patient['birthdate'])
            pdf.add_oneline_text(text=f",{patient_age} ANOS", pos=(215, 515), field_name="Patient Age", len_max=11, len_min=5)
            pdf.add_datetime(date=admission_history['admission_date'], pos=(408, 515), field_name="Data da Admissao", hours=False, formated=True)
            pdf.add_oneline_text(text=f"{admission_history['internment_day']} DE INTERNAMENTO", pos=(540, 515), field_name="Dia da internacao", len_max=40, len_min=5)
            pdf.can.setFillColorRGB(0, 0, 0, 1)
            pdf.set_font('Roboto-Mono', 10)
            
            pdf.add_morelines_text(text=admission_history['admission_text'], initial_pos=(286, 498), field_name="Texto do Historico de Admissao", len_max=630, len_min=3, char_per_lines=89, decrease_ypos=10, max_lines_amount=7)
            professional_info = pdf.create_professional_info_text(professional=admission_history['professional'], date=admission_history['professional_created_date'],nullable=False) 
            pdf.add_oneline_text(text=professional_info, pos=(348, 421), field_name="Admission Professional Info", len_max=80, len_min=5)

            pdf.add_morelines_text(text=evolution['text'], initial_pos=(357, 114), field_name="Texto da Evolucao", len_max=800, len_min=5, max_lines_amount=10, char_per_lines=77, decrease_ypos=10)
            professional_info = pdf.create_professional_info_text(professional=evolution['professional'], date=admission_history['professional_created_date'],nullable=False)

            pdf.set_font('Roboto-Mono', 8)
            pdf.add_oneline_text(text=professional_info, pos=(420, 8), field_name="Evolution Professional Info", len_max=84, len_min=5)

            pdf.add_prescription(prescription=prescription)
            pdf.add_morelines_text(text=prescription_cares, initial_pos=(18, 124), field_name='Cuidados de Enfermagem', len_max=403, len_min=5, char_per_lines=67, decrease_ypos=10, max_lines_amount=6)

            pdf.add_measures(measures=measures)
        
        except Exception as error:
            return error

        except:
            return Exception(
                "Erro desconhecido correu enquanto adicionava dados obrigatorios"
            )

        # Get pdf base64
        pdf_base64_enconded = pdf.get_base64()

        return {"base64Pdf": str(pdf_base64_enconded)[2:-1]}

    except Exception as error:
        return error
    except:
        return Exception(
            "Erro desconhecido enquanto preenchia o documento Evol Compact"
        )
