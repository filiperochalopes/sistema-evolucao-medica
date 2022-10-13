#from ..pdf_ficha_internamento import fill_pdf_ficha_internamento
from .. import pdf_aih_sus
import datetime
from flask import Response


def data_to_use(establishment_solitc_name='Establishment Solicit Name',establishment_solitc_cnes=1234567,establishment_exec_name='Establshment Exec Name',establishment_exec_cnes=7654321,patient_name='Patient Name',patient_cns=928976954930007,patient_birthday=datetime.datetime.now(),patient_sex='F',patient_mother_name='Patient Mother Name',patient_adress='Patient Adress street neighobourd',patient_adressCity='Patient City',patient_adressCity_ibgeCode=1234567,patient_adressUF='SP',patient_adressCEP=12345678,main_clinical_signs_symptoms="Patient main clinical signs sysmpthoms",conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',initial_diagnostic='Patient Initial Diagnostic',principalCid10="A00",procedure_solicited='Procedure Solicited',procedure_code='1234567890', clinic='Clinic Name', internation_carater='Internation Carater', prof_solicitant_document={'CNS':928976954930007},prof_solicitant_name='Profissional Solicit Name', solicitation_datetime=datetime.datetime.now(), autorization_prof_name='Autorization professional name', emission_org_code='OrgCode2022', autorizaton_prof_document={'CPF':28445400070}, autorizaton_datetime=datetime.datetime.now(),hospitalization_autorization_number=1234567890,exam_results='Xray tibia broken',chart_number=1234,patient_ethnicity='Preta', patient_responsible_name='Patient Responsible Name', patient_mother_phonenumber=5613248546, patient_responsible_phonenumber=8564721598, secondary_cid10='A01',cid10_associated_causes='A02',acident_type='work_path', insurance_company_cnpj=37549670000171, insurance_company_ticket_number=123450123456, insurance_company_series='Insurn Series',company_cnpj=37549670000171, company_cnae=5310501, company_cbor=123456, pension_status='not_insured'):
        return pdf_aih_sus.fill_pdf_aih_sus(establishment_solitc_name,establishment_solitc_cnes,establishment_exec_name,establishment_exec_cnes,patient_name,patient_cns,patient_birthday,patient_sex,patient_mother_name,patient_adress,patient_adressCity,patient_adressCity_ibgeCode,patient_adressUF,patient_adressCEP,main_clinical_signs_symptoms,conditions_justify_hospitalization,initial_diagnostic,principalCid10,procedure_solicited,procedure_code, clinic, internation_carater, prof_solicitant_document,prof_solicitant_name, solicitation_datetime, autorization_prof_name, emission_org_code, autorizaton_prof_document, autorizaton_datetime,hospitalization_autorization_number, exam_results,chart_number,patient_ethnicity, patient_responsible_name, patient_mother_phonenumber, patient_responsible_phonenumber,secondary_cid10,cid10_associated_causes,acident_type, insurance_company_cnpj, insurance_company_ticket_number, insurance_company_series,company_cnpj, company_cnae, company_cbor,pension_status)

#Testing Ficha Internamento
def test_with_data_in_function():
    assert type(data_to_use()) != type(Response())

def test_answer_with_all_fields():
    
    assert type(data_to_use()) != type(Response())

def test_awnser_with_only_required_data():
    assert type(pdf_aih_sus.fill_pdf_aih_sus(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        establishment_exec_name='Establshment Exec Name',
        establishment_exec_cnes=7654321,
        patient_name='Patient Name',
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_mother_name='Patient Mother Name',
        patient_adress='Patient Adress street neighobourd',
        patient_adressCity='Patient City',
        patient_adressCity_ibgeCode=1234567,
        patient_adressUF='SP',
        patient_adressCEP=12345678,
        main_clinical_signs_symptoms="Patient main clinical signs sysmpthoms",
        conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',
        initial_diagnostic='Patient Initial Diagnostic',
        principalCid10="A00",
        procedure_solicited='Procedure Solicited',
        procedure_code='1234567890', 
        clinic='Clinic Name', 
        internation_carater='Internation Carater', 
        prof_solicitant_document={'CNS':928976954930007},
        prof_solicitant_name='Profissional Solicit Name', 
        solicitation_datetime=datetime.datetime.now(), 
        autorization_prof_name='Autorization professional name', 
        emission_org_code='OrgCode2022', 
        autorizaton_prof_document={'CPF':28445400070}, 
        autorizaton_datetime=datetime.datetime.now(),
        hospitalization_autorization_number=1234567890
        )) != type(Response())


def test_name_longer():
    """Test if can put a name with more than 60 character"""
    assert data_to_use(patient_name="iashubfiuyasgfuygasfgasygifuygsayfiasuygfyagsfiuygsydgfaiuyfyausfgiuasgfyagsfiuasgyfiuasygfvisuyagfiuyasfguyagfiuysagfiuyagfiuyg").status == Response(status=400).status

def test_empty_name():    
    assert data_to_use(patient_name='').status == Response(status=400).status


def test_with_space_name():    
    assert data_to_use(patient_name='  ').status == Response(status=400).status

def test_wrong_solicitationdatetimeType():    
    assert data_to_use(solicitation_datetime="aaaaa").status == Response(status=400).status
    
def test_wrong_birthdaydatetimeType():    
    assert data_to_use(patient_birthday='aygduiaydg').status == Response(status=400).status

def test_wrong_patientnametype():    
    assert data_to_use(patient_name=123124124124).status == Response(status=400).status

def test_wrong_sexType():
    assert data_to_use(patient_sex=12347).status == Response(status=400).status

def test_wrong_sexOption():
    assert data_to_use(patient_sex='G').status == Response(status=400).status
    
def test_wrong_sexOptionExtend():    
    assert data_to_use(patient_sex='Female').status == Response(status=400).status

def test_wrong_pateintmothernameType():    
    assert data_to_use(patient_mother_name=12313).status == Response(status=400).status

def test_wrong_solicitantdocument_type():
    assert data_to_use(prof_solicitant_document=654658).status == Response(status=400).status

def test_invalid_document_option():
    assert data_to_use(prof_solicitant_document={'AAAA':928976954930007}).status == Response(status=400).status

def test_solicitdoc_invalid_CPF():
    assert data_to_use(prof_solicitant_document={'CPF':12345678955}).status == Response(status=400).status

def test_atiorizationdoc_invalid_CPF():

    assert data_to_use(autorizaton_prof_document={'CPF':55568421956}).status == Response(status=400).status

def test_patientinvalidCNS():
    assert data_to_use(patient_cns=2222213565489689).status == Response(status=400).status

def test_solicitDoc_invalidCNS():
    assert data_to_use(prof_solicitant_document={'CNS':5641654864983}).status == Response(status=400).status

def test_autorization_invalidCNS():
    assert data_to_use(prof_solicitant_document={'CNS':5641654864983}).status == Response(status=400).status

def test_wrong_patientadressType():
    assert data_to_use(patient_adress=13123124124).status == Response(status=400).status

def test_wrong_patientResponsiblePhonenumberType():
    assert data_to_use(patient_responsible_phonenumber='8564721598').status == Response(status=400).status

def test_wrong_patientMotherPhonenumberType():
    assert data_to_use(patient_mother_phonenumber='5613248546').status == Response(status=400).status 

def test_wrong_patientadresscityType():
    assert data_to_use(patient_adressCity=1231241241).status == Response(status=400).status

def test_wrong_adressCEPtype():
    assert data_to_use(patient_adressCEP='12345678').status == Response(status=400).status

def test_invalid_patient_adressCEP():
    assert data_to_use(patient_adressCEP=12345671238).status == Response(status=400).status

if __name__ == "__main__":
    pdf_aih_sus.fill_pdf_aih_sus(
        documentDatetime=datetime.datetime.now(), 
        patient_name="iashubfiuyasgfuygasfgasygifuygsayfiasuygfyagsfiuygsydgfaiuyfyausfgiuasgfyagsfiuasgyfiuasygfvisuyagfiuyasfguyagfiuysagfiuyagfiuyg",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_motherName="Patient Mother Name",
        patient_document={'CPF':28445400070},
        patient_adress='pacient street, 43, paciten, USA',
        patient_phonenumber=44387694628,
        patient_adressNumber=123456,
        patient_adressNeigh='Patient Neighborhood',
        patient_adressCity='Patient city',
        patient_adressUF='sp',
        patient_adressCEP=12345678,
        patient_nationality='Brasileira',
        patient_estimateWeight=123.32,
        has_additional_healthInsurance=False
        )