from .. import global_functions


#Testing globals functions
def test_notvalidateCPF():
    assert global_functions.isCPFvalid('434.123.123-99') == False

def test_truevalidateCPF():
    assert global_functions.isCPFvalid('434.234.123-99') == True