#from ..pdf_ficha_internamento import fill_pdf_ficha_internamento
from .. import pdf_ficha_internamento
import datetime
from flask import Response


#Testing Ficha Internamento
def test_answer():
    """Test fill ficha internamento with all data correct"""
    assert type(pdf_ficha_internamento.fill_pdf_ficha_internamento(datetime=datetime.datetime.now(), 
        patient_name="Patient Name",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now()
        )) != type(Response())

def test_name_longer():
    """Test if can put a name with more than 60 character"""
    assert pdf_ficha_internamento.fill_pdf_ficha_internamento(datetime=datetime.datetime.now(), 
        patient_name="iashubfiuyasgfuygasfgasygifuygsayfiasuygfyagsfiuygsydgfaiuyfyausfgiuasgfyagsfiuasgyfiuasygfvisuyagfiuyasfguyagfiuysagfiuyagfiuyg",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now()
        ).status == Response(status=400).status
        

if __name__ == "__main__":
    fill_pdf_ficha_internamento(datetime=datetime.datetime.now(), 
        patient_name="iashubfiuyasgfuygasfgasygifuygsayfiasuygfyagsfiuygsydgfaiuyfyausfgiuasgfyagsfiuasgyfiuasygfvisuyagfiuyasfguyagfiuysagfiuyagfiuyg",
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now()
        )