from pdfs import pdf_lme
import datetime
from flask import Response

global lenght_test
lenght_test = ''
for x in range(0, 1100):
    lenght_test += str(x)


def data_to_use(establishment_solitc_name='Establishment Solicit Name',
establishment_solitc_cnes=1234567,
patient_name='Patient Name',
patient_mother_name='Patient Mother Name',
patient_weight=142,
patient_height=180,
cid10='A123',
anamnese="Anamnese",
prof_solicitor_name="Professional Solicitor Name",
solicitation_datetime=datetime.datetime.now(),
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
    ):
    return pdf_lme.fill_pdf_lme(establishment_solitc_name,establishment_solitc_cnes,patient_name,patient_mother_name,patient_weight,patient_height,cid10,anamnese,prof_solicitor_name,solicitation_datetime,prof_solicitor_document,capacity_attest,filled_by,patient_ethnicity,previous_treatment,diagnostic,patient_document,patient_email,contacts_phonenumbers,medicines)


#Testing APAC
def test_with_data_in_function():
    assert type(data_to_use()) != type(Response())

def test_answer_with_all_fields():
    assert type(data_to_use()) != type(Response())

def test_awnser_with_only_required_data():
    assert type(pdf_lme.fill_pdf_lme(
        establishment_solitc_name='Establishment Solicit Name',
establishment_solitc_cnes=1234567,
patient_name='Patient Name',
patient_mother_name='Patient Mother Name',
patient_weight=142,
patient_height=180,
cid10='A123',
anamnese="Anamnese",
prof_solicitor_name="Professional Solicitor Name",
solicitation_datetime=datetime.datetime.now(),
prof_solicitor_document={'CPF':28445400070},
capacity_attest=['nao', 'Responsible Name'],
filled_by=['MEDICO', 'Other name', {'CPF':28445400070}],
patient_ethnicity=['SEMINFO', 'Patient Ethnicity'],
previous_treatment=['SIM', 'Previout Theatment'])) != type(Response())






















