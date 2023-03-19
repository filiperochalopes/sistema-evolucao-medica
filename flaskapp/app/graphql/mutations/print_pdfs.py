import sys
from app import env
from datetime import datetime
from app.utils import get_default_timestamp_interval_with_extra_interval_options
from ariadne import convert_kwargs_to_snake_case
from app.graphql import mutation
from app.env import InstitutionData
from app.models import db, Internment, Evolution, Prescription, Measure, FluidBalance, ProfessionalCategoryEnum
from app.services.utils.decorators import token_authorization
from app.services.functions.pdfs.func_generate_pdf_aih_sus import func_generate_pdf_aih_sus
from app.services.functions.pdfs.func_generate_pdf_apac import func_generate_pdf_apac
from app.services.functions.pdfs.func_generate_pdf_ficha_internamento import func_generate_pdf_ficha_internamento
from app.services.functions.pdfs.func_generate_pdf_relatorio_alta import func_generate_pdf_relatorio_alta
from app.services.functions.pdfs.func_generate_pdf_folha_prescricao import func_generate_pdf_folha_prescricao
from app.services.functions.pdfs.func_generate_pdf_folha_evolucao import func_generate_pdf_folha_evolucao
from app.services.functions.pdfs.func_generate_pdf_balanco_hidrico import func_generate_pdf_balanco_hidrico


@mutation.field('printPdf_AihSus')
@convert_kwargs_to_snake_case
@token_authorization
def print_pdf_aih_sus(_, info, internment_id: int, current_user: dict, extra: dict = None):
    internment = db.session.query(Internment).get(internment_id)

    return func_generate_pdf_aih_sus(
        requesting_establishment={
            'name': InstitutionData.NAME,
            'cnes': InstitutionData.CNES
        }, patient={
            'name': internment.patient.name,
            'mother_name': internment.patient.mother_name,
            'sex': 'M' if internment.patient.sex.value == 'Masculino' else 'F',
            'phone': internment.patient.phone,
            'birthdate': datetime.strftime(internment.patient.birthdate, '%Y-%m-%d'),
            'cpf': internment.patient.cpf,
            'cns': internment.patient.cns,
            'rg': internment.patient.rg,
            'nationality': 'brasileiro(a)',
            'ethnicity': None,
            'comorbidities': [c.value for c in internment.patient.comorbidities],
            'allergies': [a.value for a in internment.patient.allergies],
            'address': {
                'street': internment.patient.address.street,
                'complement': internment.patient.address.complement,
                'number': internment.patient.address.number,
                'zip_code': internment.patient.address.zip_code,
                'neighborhood': internment.patient.address.neighborhood,
                'uf': internment.patient.address.uf,
                'city': internment.patient.address.city
            }
        }, main_clinical_signs_symptoms=internment.hpi, conditions_justify_hospitalization=internment.justification, initial_diagnosis=internment.cid10.description, principal_cid_10=internment.cid10.code, requesting_professional_name=internment.professional.name, requesting_professional_document={
            'cns': internment.professional.cns,
            'cpf': internment.professional.cpf
        }
        , request_date=datetime.strftime(internment.admission_datetime, '%Y-%m-%dT%H:%M:%S'))


@mutation.field('printPdf_FichaInternamento')
@convert_kwargs_to_snake_case
@token_authorization
def print_pdf_ficha_internamento(_, info, internment_id: int, current_user: dict, extra: dict = None):
    internment = db.session.query(Internment).get(internment_id)

    return func_generate_pdf_ficha_internamento(
        document_datetime=datetime.strftime(internment.admission_datetime, '%Y-%m-%dT%H:%M:%S'),
        patient={
            'name': internment.patient.name,
            'mother_name': internment.patient.mother_name,
            'sex': 'M' if internment.patient.sex.value == 'Masculino' else 'F',
            'phone': internment.patient.phone,
            'birthdate': datetime.strftime(internment.patient.birthdate, '%Y-%m-%d'),
            'cpf': internment.patient.cpf,
            'cns': internment.patient.cns,
            'rg': internment.patient.rg,
            'weight_kg': internment.patient.weight_kg,
            'nationality': 'brasileiro(a)',
            'ethnicity': None,
            'comorbidities': [c.value for c in internment.patient.comorbidities],
            'allergies': [a.value for a in internment.patient.allergies],
            'address': {
                'street': internment.patient.address.street,
                'complement': internment.patient.address.complement,
                'number': internment.patient.address.number,
                'zip_code': internment.patient.address.zip_code,
                'neighborhood': internment.patient.address.neighborhood,
                'uf': internment.patient.address.uf,
                'city': internment.patient.address.city
            }
        }, history_of_present_illness=internment.hpi,
        initial_diagnosis_suspicion=f'{internment.cid10.code} - {internment.cid10.description}',
        doctor_name=internment.professional.name, doctor_cns=internment.professional.cns, doctor_crm=internment.professional.professional_document_number, has_additional_health_insurance=extra['has_additional_health_insurance'] if 'has_additional_health_insurance' in extra else None)


@mutation.field('printPdf_RelatorioAlta')
@convert_kwargs_to_snake_case
@token_authorization
def print_pdf_relatorio_alta(_, info, internment_id: int, current_user: dict, extra: dict = {}):
    internment = db.session.query(Internment).get(internment_id)

    # TODO Gerar resumo da história por meio de NLP https://spacedata.com.br/resumo-de-texto-em-python/

    evolution = ''
    
    # Captura a história de admissão
    history_of_present_illness = internment.hpi
    # Captura a última evolução médica para capturar quem fez a alta
    last_medical_evolution = db.session.query(Evolution).filter(Evolution.internment_id == internment.id).order_by(Evolution.created_at.desc()).first()

    evolution = f'''
    {history_of_present_illness}

    {last_medical_evolution.text}
    '''

    return func_generate_pdf_relatorio_alta(
        patient={
            'name': internment.patient.name,
            'mother_name': internment.patient.mother_name,
            'sex': 'M' if internment.patient.sex.value == 'Masculino' else 'F',
            'phone': internment.patient.phone,
            'birthdate': datetime.strftime(internment.patient.birthdate, '%Y-%m-%d'),
            'cpf': internment.patient.cpf,
            'cns': internment.patient.cns,
            'rg': internment.patient.rg,
            'nationality': 'brasileiro(a)',
            'ethnicity': None,
            'comorbidities': [c.value for c in internment.patient.comorbidities],
            'allergies': [a.value for a in internment.patient.allergies],
            'address': {
                'street': internment.patient.address.street,
                'complement': internment.patient.address.complement,
                'number': internment.patient.address.number,
                'zip_code': internment.patient.address.zip_code,
                'neighborhood': internment.patient.address.neighborhood,
                'uf': internment.patient.address.uf,
                'city': internment.patient.address.city
            }
        }, document_datetime=extra['datetime_stamp'] if ('datetime_stamp' in extra and extra['datetime_stamp'] is not None) else datetime.strftime(last_medical_evolution.created_at, '%Y-%m-%dT%H:%M:%S'), evolution=evolution, 
        doctor_name=last_medical_evolution.professional.name, doctor_cns=last_medical_evolution.professional.cns, doctor_crm=last_medical_evolution.professional.professional_document_number, orientations=extra['orientations'] if ('orientations' in extra and extra['orientations'] is not None) else None)
        
@mutation.field('printPdf_FolhaPrescricao')
@convert_kwargs_to_snake_case
@token_authorization
def print_pdf_folha_prescricao(_, info, internment_id: int, current_user: dict, extra: dict = None):
    # Verifica se o usuário que vai imprimir é um médico
    if current_user.professional_category != ProfessionalCategoryEnum.doc:
        raise Exception('Apenas um médico pode imprimir uma prescrição')

    internment = db.session.query(Internment).get(internment_id)

    start_datetime_stamp, ending_datetime_stamp = get_default_timestamp_interval_with_extra_interval_options(extra)

    # Capturando todas as prescrições no horário determinado e ordenando por data, para capturar a última prescrição como data da prescrição atualizada
    prescriptions_by_interval = db.session.query(Prescription).filter(Prescription.internment_id==internment_id).filter(Prescription.created_at>=start_datetime_stamp).filter(Prescription.created_at<=ending_datetime_stamp).order_by(Prescription.created_at.desc()).all()

    # Trnasformando em forma legível para função generate pdf ADAPTER
    prescriptions_by_interval_by_item = []
    for p in prescriptions_by_interval:
        # Capturando tipo Repouso
        prescriptions_by_interval_by_item.append({
            'type': 'Repouso',
            'description': p.resting_activity.name,
        })
        # Capturando tipo Dieta
        prescriptions_by_interval_by_item.append({
            'type': 'Dieta',
            'description': p.diet.name,
        })
        # Capturando tipo Cuidados de Enfermagem
        for na in p.nursing_activities:
            prescriptions_by_interval_by_item.append({
                'type': 'Cuidados de Enfermagem',
                'description': na.name,
            })
        # Capturando tipo Medicação
        for dp in p.drug_prescriptions:
            prescriptions_by_interval_by_item.append({
                'type': 'Medicação',
                'description': f'{dp.drug.name} | {dp.dosage}',
                'route': dp.route,
                'start_date': dp.initial_date,
                'ending_date': dp.ending_date,
            })

    return func_generate_pdf_folha_prescricao(
        patient={
            'name': internment.patient.name,
            'weight_kg': internment.patient.weight_kg,
            'birthdate': datetime.strftime(internment.patient.birthdate, '%Y-%m-%d'),
        },professional={
            'name': current_user.name,
            'professional_document_number': current_user.professional_document_number,
            'professional_document_uf': current_user.professional_document_uf
        }, created_at=datetime.strftime(prescriptions_by_interval[0].created_at, '%Y-%m-%dT%H:%M:%S'), prescriptions=prescriptions_by_interval_by_item)

@mutation.field('printPdf_FolhaEvolucao')
@convert_kwargs_to_snake_case
@token_authorization
def print_pdf_folha_evolucao(_, info, internment_id: int, current_user: dict, extra: dict = None):
    internment = db.session.query(Internment).get(internment_id)

    start_datetime_stamp, ending_datetime_stamp = get_default_timestamp_interval_with_extra_interval_options(extra)
    
    evolutions_by_interval = db.session.query(Evolution).filter(Evolution.internment_id==internment_id).filter(Evolution.created_at>=start_datetime_stamp).filter(Evolution.created_at<=ending_datetime_stamp).order_by(Evolution.created_at.desc()).all()
    measures_by_interval = db.session.query(Measure).filter(Measure.internment_id==internment_id).filter(Measure.created_at>=start_datetime_stamp).filter(Measure.created_at<=ending_datetime_stamp).order_by(Measure.created_at.desc()).all()

    # TODO Rever a função do generate_pdf para deixar os termos mais semelhantes
    return func_generate_pdf_folha_evolucao(patient={
            'name': internment.patient.name,
            'weight_kg': internment.patient.weight_kg,
            'birthdate': datetime.strftime(internment.patient.birthdate, '%Y-%m-%d'),
        }, evolutions=[{
            **e.__dict__,
            'created_at': datetime.strftime(e.created_at, '%Y-%m-%dT%H:%M:%S'),
            'professional': {
                **e.professional.__dict__,
                'category': 'M' if e.professional.professional_category.value == 'Médico' else 'E',
                'document': f'{e.professional.professional_document_number}/{e.professional.professional_document_uf}' if e.professional.professional_category.value == 'Médico' else f'{e.professional.professional_document_number}'
            }
        } for e in evolutions_by_interval], measures=[{
            'cardiac_frequency': m.systolic_bp, 
            'respiratory_frequency': m.respiratory_freq, 
            'sistolic_blood_pressure': m.diastolic_bp, 
            'diastolic_blood_pressure': m.diastolic_bp,
            'glucose': m.glucose, 
            'sp_o_2': m.spO2, 
            'celcius_axillary_temperature': m.celcius_axillary_temperature, 
            'created_at': datetime.strftime(m.created_at, '%Y-%m-%dT%H:%M:%S'),
            'professional': {
                **m.professional.__dict__,
                'category': 'M' if m.professional.professional_category.value == 'Médico' else 'E',
                'document': f'{m.professional.professional_document_number}/{m.professional.professional_document_uf}' if m.professional.professional_category.value == 'Médico' else f'{m.professional.professional_document_number}'
            }
        } for m in measures_by_interval])
    

@mutation.field('printPdf_BalancoHidrico')
@convert_kwargs_to_snake_case
@token_authorization
def print_pdf_balanco_hidrico(_, info, internment_id: int, current_user: dict, extra: dict = None):
    internment = db.session.query(Internment).get(internment_id)
    start_datetime_stamp, ending_datetime_stamp = get_default_timestamp_interval_with_extra_interval_options(extra)

    fluid_balance_by_interval = db.session.query(FluidBalance).filter(FluidBalance.internment_id==internment_id).filter(FluidBalance.created_at>=start_datetime_stamp).filter(FluidBalance.created_at<=ending_datetime_stamp).order_by(FluidBalance.created_at.desc()).all()
    
    return func_generate_pdf_balanco_hidrico(fluid_balance=[{
        'created_at': datetime.strftime(f.created_at, '%Y-%m-%dT%H:%M:%S'),
        'volume_ml': f.volume_ml,
        'description': f.description.value
        } for f in fluid_balance_by_interval], patient={
            'name': internment.patient.name,
            'weight_kg': internment.patient.weight_kg,
            'birthdate': datetime.strftime(internment.patient.birthdate, '%Y-%m-%d'),
        })

@mutation.field('printPdf_Apac')
@convert_kwargs_to_snake_case
@token_authorization
def print_pdf_apac(_, info, internment_id: int, current_user: dict, extra: dict):
    internment = db.session.query(Internment).get(internment_id)

    return func_generate_pdf_apac(
        patient={
            'name': internment.patient.name,
            'mother_name': internment.patient.mother_name,
            'sex': 'M' if internment.patient.sex.value == 'Masculino' else 'F',
            'phone': internment.patient.phone,
            'birthdate': datetime.strftime(internment.patient.birthdate, '%Y-%m-%d'),
            'cpf': internment.patient.cpf,
            'cns': internment.patient.cns,
            'rg': internment.patient.rg,
            'nationality': 'brasileiro(a)',
            'ethnicity': None,
            'comorbidities': [c.value for c in internment.patient.comorbidities],
            'allergies': [a.value for a in internment.patient.allergies],
            'address': {
                'street': internment.patient.address.street,
                'complement': internment.patient.address.complement,
                'number': internment.patient.address.number,
                'zip_code': internment.patient.address.zip_code,
                'neighborhood': internment.patient.address.neighborhood,
                'uf': internment.patient.address.uf,
                'city': internment.patient.address.city
            }
        }, requesting_establishment={
            'name': env.InstitutionData.NAME,
            'cnes': env.InstitutionData.CNES
        }, main_procedure={
            'code': extra['procedure']['code'],
            'name': extra['procedure']['name'],
            'quantity': extra['procedure']['quantity'] if 'procedure' in extra and 'quantity' in extra['procedure'] else 1
        }, secondaries_procedures=extra['secondary_procedures'] if 'secondary_procedures' in extra else None, procedure_justification_main_cid_10=extra['diagnosis']['code'] if 'diagnosis' in extra and 'code' in extra['diagnosis'] else internment.cid10.code, procedure_justification_description=extra['diagnosis']['description'] if 'diagnosis' in extra and 'description' in extra['diagnosis'] else internment.cid10.description,  procedure_justification_sec_cid_10=extra['secondary_diagnosis']['code'] if 'secondary_diagnosis' in extra and 'code' in extra['secondary_diagnosis'] else None, procedure_justification_observations=extra['observations'] if 'observations' in extra else internment.hpi, procedure_justification_associated_cause_cid_10= extra['associated_cause']['code'] if 'associated_cause' in extra and 'code' in extra['associated_cause'] else None, requesting_professional_name=current_user.name, requesting_professional_document={
            'cpf': current_user.cpf,
            'cns': current_user.cns
        })
        
