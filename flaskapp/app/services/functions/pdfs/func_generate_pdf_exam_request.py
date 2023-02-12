import datetime
from app.services.utils.PdfExamRequest import PdfExamRequest


def func_generate_pdf_exam_request(patient:dict, solicitation_reason:str,
exams:str, requesting_professional_name:str, solicitation_date:datetime.datetime, professional_authorized_name:str=None, authorization_date:datetime.datetime=None, document_pacient_date:datetime.datetime=None, document_pacient_name:str=None) -> str:
    """fill pdf exam request (Solicitacao de exames e procedimentos)

    Args:
        patient (dict): patient info
        solicitation_reason (str): solicitation_reason
        exams (str): text with exams, this is what extends pdf size to fill all exams
        requesting_professional_name (str): requesting_professional_name
        solicitation_date (datetime.datetime): solicitation_date
        professional_authorized_name (str, optional): professional_authorized_name. Defaults to None.
        authorization_date (datetime.datetime, optional): authorization_date. Defaults to None.
        document_pacient_date (datetime.datetime, optional): document_pacient_date. Defaults to None.
        document_pacient_name (str, optional): document_pacient_name. Defaults to None.

    Returns:
        str: Request with pdf in base64
    """

    try:
        pdf = PdfExamRequest()
        # Writing all data in respective fields
        # not null data
        try:
            
            
            pdf.add_exams(exams=exams)
            #Add to multiple pages
            decreaseYpos = 280
            patient_name_ypos = 775
            patient_cns_ypos = 765
            patient_birthday_ypos = 784
            solicitation_datetime_ypos = 572
            patient_adress_ypos = 734
            solicitation_reason_ypos = 690
            requesting_professional_ypos = 595
            for x in range(pdf.pags_quant):
                pdf.add_oneline_text(text=patient['name'], pos=(7, patient_name_ypos), camp_name='Patient Name', len_max=70, len_min=7)
                pdf.add_cns(cns=patient['cns'], pos=(450, patient_cns_ypos), camp_name='Patient CNS',formated=True)
                pdf.add_datetime(date=patient['birthdate'], pos=(441, patient_birthday_ypos), camp_name='Patient Birthday', hours=False, formated=True)
                pdf.add_morelines_text(text=f"{patient['address']['street']}, {patient['address']['city']} - {patient['address']['uf']}", initial_pos=(7, patient_adress_ypos), decrease_ypos=10, camp_name='Patient Adress', len_max=216, len_min=7, char_per_lines=108)
                pdf.add_morelines_text(text=solicitation_reason, initial_pos=(7, solicitation_reason_ypos), decrease_ypos=10, camp_name='Solicitation Reason', len_max=216, len_min=7, char_per_lines=108)
                pdf.add_oneline_text(text=requesting_professional_name, pos=(7, requesting_professional_ypos), camp_name='Professional Solicitor Name', len_max=29, len_min=7)
                pdf.add_datetime(date=solicitation_date, pos=(30, solicitation_datetime_ypos), camp_name='Solicitation Datetime', hours=False, formated=True)

                #Decrese ypos in all lines to complete the page
                patient_name_ypos -= decreaseYpos
                patient_cns_ypos -= decreaseYpos
                patient_birthday_ypos -= decreaseYpos
                patient_adress_ypos -= decreaseYpos
                solicitation_reason_ypos -= decreaseYpos
                requesting_professional_ypos -= decreaseYpos
                solicitation_datetime_ypos -= decreaseYpos


        except Exception as error:
            return error
        except:
            return Exception('Erro desconhecido ocorreu enquanto adicionava dados obrigadorios')

        #Adding data that can be null
        try:
            professional_authorized_ypos = 595
            document_pacient_name_ypos = 605
            authorization_datetime_ypos = 572
            document_pacient_date_ypos = 572
            for x in range(pdf.pags_quant):
                pdf.add_oneline_text(text=professional_authorized_name, pos=(174, professional_authorized_ypos), camp_name='Professional Authorized Name', len_max=29, len_min=7, nullable=True)
                pdf.add_oneline_text(text=document_pacient_name, pos=(340, document_pacient_name_ypos), camp_name='Document Pacient Name', len_max=46, len_min=7, nullable=True)
                pdf.add_datetime(date=authorization_date, pos=(195, authorization_datetime_ypos), camp_name='Authorization Datetime', hours=False, formated=True, nullable=True)
                pdf.add_datetime(date=document_pacient_date, pos=(362, document_pacient_date_ypos), camp_name='Document Pacient Datetime', hours=False, formated=True, nullable=True)

                professional_authorized_ypos -= decreaseYpos
                document_pacient_name_ypos -= decreaseYpos
                authorization_datetime_ypos -= decreaseYpos
                document_pacient_date_ypos -= decreaseYpos

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
        return Exception("Erro desconhecido enquanto preenchia o documento de solicitacao de exames (exam request)")
