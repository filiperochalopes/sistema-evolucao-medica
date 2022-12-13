from datetime import datetime
from pprint import pprint
import bcrypt
import sys
import datetime

from ariadne import convert_kwargs_to_snake_case
from app.graphql import mutation
from app.services.functions.pdfs.func_generate_pdf_aih_sus import func_generate_pdf_aih_sus


@mutation.field('generatePdf_AihSus')
@convert_kwargs_to_snake_case
def generate_pdf_aih_sus(_, info, establishment_solitc_name:str, establishment_solitc_cnes:int, establishment_exec_name:str, establishment_exec_cnes:int, patient_name:str, patient_cns:str, patient_birthday:datetime.datetime, patient_sex:str, patient_mother_name:str, patient_adress:str, patient_adress_city:str, patient_adress_city_ibge_code:int, patient_adress_uf:str, patient_adress_cep:str, main_clinical_signs_symptoms:str, conditions_justify_hospitalization:str, initial_diagnostic:str, principal_cid_10:str, procedure_solicited:str, procedure_code:str, clinic:str, internation_carater:str, prof_solicitor_document:dict, prof_solicitor_name:str, solicitation_datetime:datetime.datetime, prof_autorization_name:str, emission_org_code:str, autorizaton_prof_document:dict, autorizaton_datetime:datetime.datetime, hospitalization_autorization_number:str ,exam_results:str=None, chart_number:str=None, patient_ethnicity:str=None, patient_responsible_name:str=None, patient_mother_phonenumber:str=None, patient_responsible_phonenumber:str=None, secondary_cid_10:str=None, cid_10_associated_causes:str=None, acident_type:str=None, insurance_company_cnpj:str=None, insurance_company_ticket_number:str=None, insurance_company_series:str=None,company_cnpj:str=None, company_cnae:int=None, company_cbor:int=None, pension_status:str=None):

    return func_generate_pdf_aih_sus(establishment_solitc_name, establishment_solitc_cnes, establishment_exec_name, establishment_exec_cnes, patient_name, patient_cns, patient_birthday, patient_sex, patient_mother_name, patient_adress, patient_adress_city, patient_adress_city_ibge_code, patient_adress_uf, patient_adress_cep, main_clinical_signs_symptoms, conditions_justify_hospitalization, initial_diagnostic, principal_cid_10, procedure_solicited, procedure_code, clinic, internation_carater, prof_solicitor_document, prof_solicitor_name, solicitation_datetime, prof_autorization_name, emission_org_code, autorizaton_prof_document, autorizaton_datetime, hospitalization_autorization_number ,exam_results, chart_number, patient_ethnicity, patient_responsible_name, patient_mother_phonenumber, patient_responsible_phonenumber, secondary_cid_10, cid_10_associated_causes, acident_type, insurance_company_cnpj, insurance_company_ticket_number, insurance_company_series,company_cnpj, company_cnae, company_cbor, pension_status)