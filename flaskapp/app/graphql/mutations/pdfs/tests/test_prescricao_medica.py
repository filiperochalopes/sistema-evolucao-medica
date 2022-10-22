from pdfs import pdf_prescricao_medica
import datetime
from flask import Response

global lenght_test
lenght_test = ''
for x in range(0, 2000):
    lenght_test += str(x)

def data_to_use(document_datetime=datetime.datetime.now(),
        patient_name='Pacient Name',
        prescription=[{"medicine_name":"Dipirona 500mg", "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}, {"medicine_name":"Metocoplamina 10mg", "amount":"6 comprimidos", "use_mode":"1 comprimido, via oral, de 8/8h por 2 dias"}]):
        return pdf_prescricao_medica.fill_pdf_prescricao_medica(document_datetime, patient_name, prescription)

#Testing Ficha Internamento
def test_answer_with_all_fields():
    """Test fill ficha internamento with all data correct"""
    assert data_to_use() != type(Response())


##############################################################
# ERRORS IN NAMES CAMPS
# patient_name

def test_wrongtype_patient_name():    
    assert data_to_use(patient_name=123124).status == Response(status=400).status

def test_empty_patient_name():    
    assert data_to_use(patient_name='').status == Response(status=400).status

def test_with_space_patient_name():    
    assert data_to_use(patient_name='  ').status == Response(status=400).status

def test_long_patient_name():    
    assert data_to_use(patient_name=str(lenght_test[:36])).status == Response(status=400).status

def test_short_patient_name():    
    assert data_to_use(patient_name='11113').status == Response(status=400).status

#################################################################
# TEST DATETIMES VARIABLES
# document_datetime

def test_wrongtype_document_datetime():
    assert data_to_use(document_datetime='bahabah').status == Response(status=400).status

def test_valid_document_datetime():
    assert type(data_to_use(document_datetime=datetime.datetime.now())) != type(Response())

#################################################################
# TEST prescriptions
# test wrong type
# test list with other type
# test dicts wihtout necessary keys
# test dicts with more than necessary keys
# test message_name with wrong type
# test message_name longer
# test amount with wrong type
# test amount longer
# test use_mode with wrong type
# test use_mode longer

def test_wrongtype_prescriptions():
    assert data_to_use(prescription='bahabah').status == Response(status=400).status

def test_list_with_other_types():
    assert data_to_use(prescription=['bahabah', 12313]).status == Response(status=400).status

def test_list_with_other_types():
    assert data_to_use(prescription=['bahabah', 12313]).status == Response(status=400).status

def test_dicts_without_necessary_keys():
    assert data_to_use(prescription=[{"medicine_name":"Dipirona 500mg", "amount":"4 comprimidos"}]).status == Response(status=400).status

def test_dicts_with_more_than_necessary_keys():
    assert data_to_use(prescription=[{"medicine_name":"Dipirona 500mg", "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias", "dontExiste":"aidsuad"}]).status == Response(status=400).status

def test_message_name_with_wrongtype():
    assert data_to_use(prescription=[{"medicine_name":123123123, "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}]).status == Response(status=400).status

def test_message_name_longer():
    assert data_to_use(prescription=[{"medicine_name":lenght_test[:70], "amount":"4 comprimidos", "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}]).status == Response(status=400).status

def test_amount_with_wrongtype():
    assert data_to_use(prescription=[{"medicine_name":'123123123', "amount":1213, "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}]).status == Response(status=400).status

def test_amount_longer():
    assert data_to_use(prescription=[{"medicine_name":"sadfasdf", "amount":lenght_test[:70], "use_mode":"1 comprimido, via oral, de 6/6h por 3 dias"}]).status == Response(status=400).status

def test_use_mode_with_wrongtype():
    assert data_to_use(prescription=[{"medicine_name":'123123123', "amount":"4 comprimidos", "use_mode":12312313}]).status == Response(status=400).status

def test_use_mode_longer():
    assert data_to_use(prescription=[{"medicine_name":lenght_test[:70], "amount":"4 comprimidos", "use_mode":lenght_test[:250]}]).status == Response(status=400).status













