from ariadne import convert_kwargs_to_snake_case
from app.graphql import mutation
from app.env import InstitutionData
from app.models import db, Internment, FluidBalance, FluidBalanceDescription
from app.services.utils.decorators import token_authorization
from app.services.functions.pdfs.func_generate_pdf_aih_sus import func_generate_pdf_aih_sus
from app.services.functions.pdfs.func_generate_pdf_apac import func_generate_pdf_apac
from app.services.functions.pdfs.func_generate_pdf_exam_request import func_generate_pdf_exam_request
from app.services.functions.pdfs.func_generate_pdf_ficha_internamento import func_generate_pdf_ficha_internamento
from app.services.functions.pdfs.func_generate_pdf_lme import func_generate_pdf_lme
from app.services.functions.pdfs.func_generate_pdf_prescricao_medica import func_generate_pdf_prescricao_medica
from app.services.functions.pdfs.func_generate_pdf_relatorio_alta import func_generate_pdf_relatorio_alta
from app.services.functions.pdfs.func_generate_pdf_solicit_mamografia import func_generate_pdf_solicit_mamografia
from app.services.functions.pdfs.func_generate_pdf_folha_prescricao import func_generate_pdf_folha_prescricao
from app.services.functions.pdfs.func_generate_pdf_folha_evolucao import func_generate_pdf_folha_evolucao
from app.services.functions.pdfs.func_generate_pdf_balanco_hidrico import func_generate_pdf_balanco_hidrico


@mutation.field('printPdf_AihSus')
@convert_kwargs_to_snake_case
@token_authorization
def print_pdf_aih_sus(_, info, internment_id: int, secondary_cid_10: str):
    internment = db.session.query(Internment).get(internment_id)

    return func_generate_pdf_aih_sus(establishment_solitc={
        'name': InstitutionData.NAME,
        'cnes': InstitutionData.CNES
    }, patient={
        'name': internment.patient.name,
        'motherName': internment.patient.mother_name,
        'sex': internment.patient.sex,
        'weightKg': internment.patient.weight_kg,
        'birthdate': internment.patient.birthdate,
        'cpf': internment.patient.cpf,
        'cns': internment.patient.cns,
        'rg': internment.patient.rg,
        'nationality': 'brasileiro(a)',
        'ethnicity': None,
        'comorbidities': [c.value for c in internment.patient.comorbidities],
        'allergies': [a.value for a in internment.patient.allergies],
        'address': {
            'street': internment.patient.address.street,
            'complement': internment.patient.address.street,
            'number': internment.patient.address.number,
            'zip_code': internment.patient.address.zip_code,
            'neighborhood': internment.patient.address.neighborhood,
            'uf': internment.patient.address.uf,
            'city': internment.patient.address.city
        }
    }, main_clinical_signs_symptoms=internment.hpi, conditions_justify_hospitalization=internment.justification, initial_diagnosis=internment.cid10.description, principal_cid_10=)


@mutation.field('printPdf_FichaInternamento')
@convert_kwargs_to_snake_case
@token_authorization
def print_pdf_ficha_internamento(_, info, **kwargs):
    return func_generate_pdf_ficha_internamento(**kwargs)
