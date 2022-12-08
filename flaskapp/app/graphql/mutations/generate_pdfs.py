from datetime import datetime
from pprint import pprint
import bcrypt
import sys

from ariadne import convert_kwargs_to_snake_case
from app.graphql import mutation
from app.services.functions.pdfs.func_generate_pdf_aih_sus import func_generate_pdf_aih_sus


@mutation.field('generatePdf_AihSus')
@convert_kwargs_to_snake_case
def generate_pdf_aih_sus(_, info, **kwargs) -> str:
    return func_generate_pdf_aih_sus(kwargs)