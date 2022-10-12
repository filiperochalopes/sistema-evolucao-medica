from .. import global_functions
from flask import Response


#Testing globals functions
def test_notvalidateCPF():
    assert global_functions.isCPFvalid('434.123.123-99') == False

def test_truevalidateCPF():
    assert global_functions.isCPFvalid('434.234.123-99') == True

def test_wrongCPFtype():
    assert global_functions.isCPFvalid(8167423414).status == Response(status=500).status

def test_emptyCPF():
    assert global_functions.isCPFvalid('            ') == False


def test_notvalidateCNS():
    assert global_functions.isCNSvalid(914874125754) == False

def test_truevalidateCNS():
    assert global_functions.isCNSvalid(928976954930007) == True

def test_wrongCNStype():
    assert global_functions.isCNSvalid('8167423414').status == Response(status=500).status


def test_notvalidateRG():
    assert global_functions.isRGvalid(91487412575413451235125) == False
    
def test_notvalidateRG():
    assert global_functions.isRGvalid(91454) == False

def test_truevalidateRG():
    assert global_functions.isRGvalid(928976954930007) == True

def test_wrongRGtype():
    assert global_functions.isRGvalid('8167423414').status == Response(status=500).status
