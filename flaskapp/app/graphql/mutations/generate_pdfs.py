from datetime import datetime
from pprint import pprint
import bcrypt
import sys
from ariadne import convert_kwargs_to_snake_case
from app.graphql import mutation
from app.services.functions.pdfs.func_generate_pdf_aih_sus import func_generate_pdf_aih_sus
from app.services.functions.pdfs.func_generate_pdf_apac import func_generate_pdf_apac
from app.services.functions.pdfs.func_generate_pdf_exam_request import func_generate_pdf_exam_request
from app.services.functions.pdfs.func_generate_pdf_ficha_internamento import func_generate_pdf_ficha_internamento
from app.services.functions.pdfs.func_generate_pdf_lme import func_generate_pdf_lme
from app.services.functions.pdfs.func_generate_pdf_prescricao_medica import func_generate_pdf_prescricao_medica
from app.services.functions.pdfs.func_generate_pdf_relatorio_alta import func_generate_pdf_relatorio_alta
from app.services.functions.pdfs.func_generate_pdf_solicit_mamografia import func_generate_pdf_solicit_mamografia


@mutation.field('generatePdf_AihSus')
@convert_kwargs_to_snake_case
def generate_pdf_aih_sus(_, info, **kwargs):
    return func_generate_pdf_aih_sus(**kwargs)

@mutation.field('generatePdf_Apac')
@convert_kwargs_to_snake_case
def generate_pdf_apac(_, info, **kwargs):
    return func_generate_pdf_apac(**kwargs)

@mutation.field('generatePdf_SolicitExames')
@convert_kwargs_to_snake_case
def generate_pdf_exam_request(_, info, **kwargs):
    return func_generate_pdf_exam_request(**kwargs)

@mutation.field('generatePdf_FichaInternamento')
@convert_kwargs_to_snake_case
def generate_pdf_ficha_internamento(_, info, **kwargs):
    return func_generate_pdf_ficha_internamento(**kwargs)


@mutation.field('generatePdf_Lme')
@convert_kwargs_to_snake_case
def generate_pdf_lme(_, info, **kwargs):
    return func_generate_pdf_lme(**kwargs)


@mutation.field('generatePdf_PrescricaoMedica')
@convert_kwargs_to_snake_case
def generate_pdf_prescricao_medica(_, info, **kwargs):
    return func_generate_pdf_prescricao_medica(**kwargs)

@mutation.field('generatePdf_RelatorioAlta')
@convert_kwargs_to_snake_case
def generate_pdf_relatorio_alta(_, info, **kwargs):
    return func_generate_pdf_relatorio_alta(**kwargs)


@mutation.field('generatePdf_SolicitMamografia')
@convert_kwargs_to_snake_case
def generate_pdf_solicit_mamografia(_, info, **kwargs):
    return func_generate_pdf_solicit_mamografia(**kwargs)

