from .. import pdf_exam_request
import datetime
from flask import Response

global lenghtTest
lenghtTest = ''
for x in range(0, 1100):
    lenghtTest += str(x)

def data_to_use(patient_name='Patient Name',patient_cns=928976954930007, patient_birthday=datetime.datetime.now(),patient_adress="Patient Adress",exams=lenghtTest[:800],solicitation_reason="Solicitation Reason",prof_solicitor="Professional Solicitor",prof_authorized="Professional Authorized",solicitation_datetime=datetime.datetime.now(),autorization_datetime=datetime.datetime.now(), document_pacient_date=datetime.datetime.now(),document_pacient_name='Document pacient name'):
    return pdf_exam_request.fill_pdf_exam_request(patient_name, patient_cns, patient_birthday, patient_adress, solicitation_reason,
    exams, prof_solicitor, solicitation_datetime,prof_authorized, autorization_datetime, document_pacient_date, document_pacient_name)

#Testing Ficha Internamento
def test_with_data_in_function():
    assert type(data_to_use()) != type(Response())

def test_answer_with_all_fields():
    assert type(data_to_use()) != type(Response())

def test_awnser_with_only_required_data():
    assert type(pdf_exam_request.fill_pdf_exam_request(
        patient_name='Patient Name', 
        patient_cns=928976954930007, 
        patient_birthday=datetime.datetime.now(), 
        patient_adress="Patient Adress", 
        exams=lenghtTest[:800],
        solicitation_datetime=datetime.datetime.now(),
        solicitation_reason="Solicitation Reason", 
        prof_solicitor="Professional Solicitor"
    )) != type(Response())

##############################################################
# ERRORS IN NAMES CAMPS
# patientName
# prof_authorized
# prof_solicitor
# document_pacient_name
# Name empty
# Name with space
# long name
# short name
# wrong name type

def test_empty_patientName():    
    assert data_to_use(patient_name='').status == Response(status=400).status

def test_with_space_patientName():    
    assert data_to_use(patient_name='  ').status == Response(status=400).status

def test_long_patientName():    
    assert data_to_use(patient_name=lenghtTest[:84]).status == Response(status=400).status

def test_short_patientName():    
    assert data_to_use(patient_name='bro').status == Response(status=400).status

def test_wrongtype_patientName():    
    assert data_to_use(patient_name=123124).status == Response(status=400).status

def test_empty_prof_authorized():    
    assert type(data_to_use(prof_authorized='')) != type(Response())

def test_with_space_prof_authorized():    
    assert type(data_to_use(prof_authorized='  ')) != type(Response())

def test_long_prof_authorized():    
    assert data_to_use(prof_authorized=lenghtTest[:32]).status == Response(status=400).status

def test_short_prof_authorized():    
    assert data_to_use(prof_authorized='bro').status == Response(status=400).status

def test_wrongtype_prof_authorized():    
    assert data_to_use(prof_authorized=123124).status == Response(status=400).status

def test_empty_prof_solicitor():    
    assert data_to_use(prof_solicitor='').status == Response(status=400).status

def test_with_space_prof_solicitor():    
    assert data_to_use(prof_solicitor='  ').status == Response(status=400).status

def test_long_prof_solicitor():    
    assert data_to_use(prof_solicitor=lenghtTest[:32]).status == Response(status=400).status

def test_short_prof_solicitor():    
    assert data_to_use(prof_solicitor='bro').status == Response(status=400).status

def test_wrongtype_prof_solicitor():    
    assert data_to_use(prof_solicitor=123124).status == Response(status=400).status

def test_empty_document_pacient_name():    
    assert type(data_to_use(document_pacient_name='')) != type(Response())

def test_with_space_document_pacient_name():    
    assert type(data_to_use(document_pacient_name='  ')) != type(Response())

def test_long_document_pacient_name():    
    assert data_to_use(document_pacient_name=lenghtTest[:50]).status == Response(status=400).status

def test_short_document_pacient_name():    
    assert data_to_use(document_pacient_name='bro').status == Response(status=400).status

def test_wrongtype_document_pacient_name():    
    assert data_to_use(document_pacient_name=123124).status == Response(status=400).status

####################################################################
# TEST CNES 
# patient_cns
# empty
# wrong type
# invalid cnes

def test_empty_patient_cns():
    assert data_to_use(patient_cns='').status == Response(status=400).status

def test_wrongtype_patient_cns():
    assert data_to_use(patient_cns='adsadad').status == Response(status=400).status

def test_invalidcnes_patient_cns():
    assert data_to_use(patient_cns=451236548).status == Response(status=400).status



#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_datetime
# autorization_datetime
# document_pacient_date
# test wrong type
# test valid datetime

def test_wrongtype_patient_birthday():
    assert data_to_use(patient_birthday='bahabah').status == Response(status=400).status

def test_valid_patient_birthday():
    assert type(data_to_use(patient_birthday=datetime.datetime.now())) != type(Response())

def test_wrongtype_solicitation_datetime():
    assert data_to_use(solicitation_datetime='bahabah').status == Response(status=400).status

def test_valid_solicitation_datetime():
    assert type(data_to_use(solicitation_datetime=datetime.datetime.now())) != type(Response())

def test_wrongtype_autorization_datetime():
    assert data_to_use(autorization_datetime='bahabah').status == Response(status=400).status

def test_valid_autorization_datetime():
    assert type(data_to_use(autorization_datetime=datetime.datetime.now())) != type(Response())

def test_wrongtype_document_pacient_date():
    assert data_to_use(document_pacient_date='bahabah').status == Response(status=400).status

def test_valid_document_pacient_date():
    assert type(data_to_use(document_pacient_date=datetime.datetime.now())) != type(Response())


####################################################################
# TEST ADRESS VARIABLES
# patient_adress
# test wrong type
# test empty value
# test empty space value
# invalid value
# Long value

def test_wrongtype_patient_adress():
    assert data_to_use(patient_adress=1212312).status == Response(status=400).status

def test_empty_value_patient_adress():
    assert data_to_use(patient_adress='').status == Response(status=400).status

def test_empty_space_patient_adress():
    assert data_to_use(patient_adress='  ').status == Response(status=400).status

def test_invalid_value_patient_adress():
    assert data_to_use(patient_adress='111').status == Response(status=400).status

def test_long_value_patient_adress():
    assert data_to_use(patient_adress=lenghtTest[:220]).status == Response(status=400).status


#############################################################################
# NORMAL TEXT VARIABLES THAT CANNOT BE NULL
# solicitation_reason
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit


def test_wrong_type_solicitation_reason():
    assert data_to_use(solicitation_reason=131).status == Response(status=400).status

def test_empty_value_solicitation_reason():
    assert data_to_use(solicitation_reason='').status == Response(status=400).status

def test_empty_spaces_solicitation_reason():
    assert data_to_use(solicitation_reason='    ').status == Response(status=400).status

def test_shortText_solicitation_reason():
    assert data_to_use(solicitation_reason='abla').status == Response(status=400).status

def test_more_than_limit_solicitation_reason():
    assert data_to_use(solicitation_reason=lenghtTest[:220]).status == Response(status=400).status


#############################################################################
# TEST TEXT VARIABLES THAT CHANGE NUMBER OF PAGS
# exams
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit
# test 1 page long 
# test 2 pages long
# test 3 pages long

def test_wrong_type_exams():
    assert data_to_use(exams=131).status == Response(status=400).status

def test_empty_value_exams():
    assert data_to_use(exams='').status == Response(status=400).status

def test_empty_spaces_exams():
    assert data_to_use(exams='    ').status == Response(status=400).status

def test_shortText_exams():
    assert data_to_use(exams='abla').status == Response(status=400).status

def test_more_than_limit_exams():
    assert data_to_use(exams=lenghtTest[:980]).status == Response(status=400).status

def test_1_pages_long_exams():
    assert type(data_to_use(exams=lenghtTest[:200])) != type(Response())

def test_2_pages_long_exams():
    assert type(data_to_use(exams=lenghtTest[:400])) != type(Response())

def test_3_pages_long_exams():
    assert type(data_to_use(exams=lenghtTest[:750])) != type(Response())






