import pdfs
import datetime
from flask import Response

global lenght_test
lenght_test = ''
for x in range(0, 1100):
    lenght_test += str(x)

datetime_to_use = datetime.datetime.now()

def test_create_aih_sus_pdf():
    output = pdfs.pdf_aih_sus.fill_pdf_aih_sus(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        establishment_exec_name='Establshment Exec Name',
        establishment_exec_cnes=7654321,
        patient_name='Patient Name',
        patient_cns=928976954930007,
        patient_birthday=datetime_to_use,
        patient_sex='F',
        patient_mother_name='Patient Mother Name',
        patient_adress='Patient Adress street neighobourd',
        patient_adressCity='Patient City',
        patient_adressCity_ibgeCode=1234567,
        patient_adressUF='SP',
        patient_adressCEP=12345678,
        main_clinical_signs_symptoms="Patient main clinical signs sympthoms",
        conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',
        initial_diagnostic='Patient Initial Diagnostic',
        principalCid10="A00",
        procedure_solicited='Procedure Solicited',
        procedure_code='1234567890', 
        clinic='Clinic Name', 
        internation_carater='Internation Carater', 
        prof_solicitor_document={'CPF':28445400070},
        prof_solicitor_name='Profissional Solicit Name', 
        solicitation_datetime=datetime_to_use, 
        autorization_prof_name='Autorization professional name', 
        emission_org_code='OrgCode2022', 
        autorizaton_prof_document={'CNS':928976954930007}, 
        autorizaton_datetime=datetime_to_use,
        hospitalization_autorization_number=1234567890,
        exam_results='Xray tibia broken',
        chart_number=1234,
        patient_ethnicity='Preta', 
        patient_responsible_name='Patient Responsible Name', 
        patient_mother_phonenumber=5613248546, 
        patient_responsible_phonenumber=8564721598, 
        secondary_cid10='A01',
        cid10_associated_causes='A02',
        acident_type='traffic', 
        insurance_company_cnpj=37549670000171, 
        insurance_company_ticket_number=123450123456, 
        insurance_company_series='Insurn',
        company_cnpj=37549670000171, 
        company_cnae=5310501, 
        company_cbor=123456, 
        pension_status='retired'
    )
    assert type(output) == type(bytes())


def test_create_apac_pdf():
    output = pdfs.pdf_apac.fill_pdf_apac(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        patient_name='Patient Name',
        patient_cns=928976954930007,
        patient_sex='M',
        patient_birthday=datetime_to_use,
        patient_adress_city='Patient Adress City',
        main_procedure_name='Main procedure Name',
        main_procedure_code='1234567890',
        main_procedure_quant=4,
        patient_mother_name='Patient Mother Name',
        patient_mother_phonenumber=5286758957, 
        patient_responsible_name='Patient Responsible Name', patient_responsible_phonenumber=5465981345, 
        patient_adress='Patient Adress',
        patient_color='Branca',
        patient_ethnicity='Indigena',
        patient_adressUF='BA',
        patient_adressCEP=86425910, 
        document_chart_number=12345,
        patient_adress_city_IBGEcode=4528765,
        procedure_justification_description='Procedure Justification Description', 
        procedure_justification_main_cid10='A98', 
        procedure_justification_sec_cid10='A01', procedure_justification_associated_cause_cid10='A45',
        procedure_justification_comments='Procedure Justification Comments',establishment_exec_name='Establishment Exec Name', 
        establishment_exec_cnes=7654321,
        prof_solicitor_document={'CPF':28445400070}, 
        prof_solicitor_name='Profissional Solicit Name', 
        solicitation_datetime=datetime_to_use,
        signature_datetime=datetime_to_use,
        validity_period_start=datetime_to_use,
        validity_period_end=datetime_to_use,
        autorization_prof_name='Autorization Professional Name', 
        emission_org_code='Cod121234', 
        autorizaton_prof_document={'CPF':28445400070}, 
        autorizaton_datetime=datetime_to_use,
        secondaries_procedures=[{"procedure_name":"Procedure Name", "procedure_code":"cod4521578", "quant":5}, {"procedure_name":"Another Procedure", "procedure_code":"123Another", "quant":1}]
    )
    assert type(output) == type(bytes())


def test_create_exam_request_pdf():
    output = pdfs.pdf_exam_request.fill_pdf_exam_request(
        patient_name='Patient Name', 
        patient_cns=928976954930007, 
        patient_birthday=datetime_to_use, 
        patient_adress="Patient Adress", 
        exams=lenght_test[:800],
        solicitation_reason="Solicitation Reason", 
        prof_solicitor="Professional Solicitor", 
        prof_authorized="Professional Authorized", 
        solicitation_datetime=datetime_to_use, 
        autorization_datetime=datetime_to_use, document_pacient_date=datetime_to_use, 
        document_pacient_name='Document pacient name'
    )
    assert type(output) == type(bytes())


def test_create_ficha_internamento_pdf():
    output = pdfs.pdf_ficha_internamento.fill_pdf_ficha_internamento(
        document_datetime=datetime_to_use, 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime_to_use,
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CPF':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_drug_allergies='Penicillin, Aspirin, Ibuprofen, Anticonvulsants.',
        patient_comorbidities='Heart disease, High blood pressure, Diabetes, Cerebrovascular disease.',
        current_illness_history='Current illnes hsitoryaaaaaaaaaaaedqeqa',
        initial_diagnostic_suspicion='Diagnostic suspicion and referral bias in studies of venous thromboembolism and oral.',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123,
        has_additional_healthInsurance=False
        )
    assert type(output) == type(bytes())


def test_create_lme_pdf():
    output = pdfs.pdf_lme.fill_pdf_lme(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        patient_name='Patient Name',
        patient_mother_name='Patient Mother Name',
        patient_weight=142,
        patient_height=180,
        cid10='A123',
        anamnese="Anamnese",
        prof_solicitor_name="Professional Solicitor Name",
        solicitation_datetime=datetime_to_use,
        prof_solicitor_document={'CPF':28445400070},
        capacity_attest=['nao', 'Responsible Name'],
        filled_by=['MEDICO', 'Other name', {'CPF':28445400070}],
        patient_ethnicity=['SEMINFO', 'Patient Ethnicity'],
        previous_treatment=['SIM', 'Previout Theatment'],
        diagnostic='Diagnostic',
        patient_document={'CNS':928976954930007},
        patient_email='patietemail@gmail.com',
        contacts_phonenumbers=[1254875652, 4578456598],
        medicines=[{"medicine_name":lenght_test[:60], "quant_1month":"20 comp", "quant_2month":"15 comp", "quant_3month":"5 comp"}, {"medicine_name":lenght_test[:60], "quant_1month":"20 comp", "quant_2month":"15 comp", "quant_3month":"5 comp"}, {"medicine_name":lenght_test[:60], "quant_1month":"20 comp", "quant_2month":"15 comp", "quant_3month":"5 comp"}, {"medicine_name":lenght_test[:60], "quant_1month":"20 comp", "quant_2month":"15 comp", "quant_3month":"5 comp"}, {"medicine_name":lenght_test[:60], "quant_1month":"20 comp", "quant_2month":"15 comp", "quant_3month":"5 comp"}]
    )
    assert type(output) == type(bytes())

def test_create_precricao_medica_pdf():
    output = pdfs.pdf_prescricao_medica.fill_pdf_prescricao_medica(
        document_datetime=datetime_to_use,
        patient_name='Pacient Name',
        prescription=[{"medicine_name":"Dipirona 500mg", "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}, {"medicine_name":"Metocoplamina 10mg", "amount":"6 comprimidos", "use_mode":"1 comprimido, via oral, de 8/8h por 2 dias"}]
    )
    assert type(output) == type(bytes())

def test_create_relatorio_alta_pdf():
    output = pdfs.pdf_relatorio_de_alta.fill_pdf_relatorio_alta(
        documentDatetime=datetime_to_use, 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime_to_use,
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CPF':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        evolution='Current illnes hsitoryaaaaaaaaaaaedqeqa',
        doctor_name='Doctor Name',
        doctor_cns=928976954930007,
        doctor_crm='CRM/UF 123456',
        orientations='Do not jump'
        )
    assert type(output) == type(bytes())


def test_create_solicit_mamografia_pdf():
    output = pdfs.pdf_solicit_mamografia.fill_pdf_solicit_mamografia(
        patient_name='Patient Name',
        patient_cns=928976954930007,
        patient_mother_name='Patient Mother Name',
        patient_birthday=datetime_to_use,
        nodule_lump='NAO',
        high_risk='NAOSABE',
        examinated_before='NAOSABE',
        mammogram_before=['NAOSABE', '2020'],
        patient_age=23,
        health_unit_adressUF='SP',
        health_unit_cnes=1234567,
        health_unit_name="Health Unit Name",
        health_unit_adress_city='Unit City',
        health_unit_city_IBGEcode=1234567,
        document_chart_number=1234567895,
        protocol_number='5478546135245165',
        patient_sex='F',
        patient_surname='Patient Surname',
        patient_document_cpf={'CPF':28445400070},
        patient_nationality='Patient Nationality',
        patient_adress='Patient Adress',
        patient_adress_number=123456,
        patient_adress_adjunct='Patient Adress Adjunct',
        patient_adress_neighborhood='Neighborhood',
        patient_city_IBGEcode=1234567,
        patient_adress_city='Patient City',
        patient_adressUF='SP',
        patient_ethnicity=['INDIGENA', 'Indigena'],
        patient_adress_reference='Adress Reference',
        patient_schooling='SUPCOMPL',
        patient_adressCEP=12345678,
        patient_phonenumber=1234567890
        )
    assert type(output) == type(bytes())


