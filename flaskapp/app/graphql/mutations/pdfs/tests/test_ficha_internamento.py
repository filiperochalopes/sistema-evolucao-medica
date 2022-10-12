#from ..pdf_ficha_internamento import fill_pdf_ficha_internamento
from .. import pdf_ficha_internamento
from .. import global_functions
import datetime
from flask import Response


#Testing globals functions
def test_notvalidateCPF():
    assert global_functions.isCPFvalid('434.123.123-99') == False

def test_truevalidateCPF():
    assert global_functions.isCPFvalid('434.234.123-99') == True



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