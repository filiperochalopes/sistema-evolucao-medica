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
    assert global_functions.isCNSvalid(914874125754123) == False

def test_truevalidateCNS():
    assert global_functions.isCNSvalid(928976954930007) == True

def test_wrongCNStype():
    assert global_functions.isCNSvalid('8167423414').status == Response(status=500).status


def test_longnotvalidateRG():
    assert global_functions.isRGvalid(9197841521982457189247195271597495195714) == False
    
def test_notvalidateRG():
    assert global_functions.isRGvalid(91454) == False

def test_truevalidateRG():
    assert global_functions.isRGvalid(928976954930007) == True

def test_wrongRGtype():
    assert global_functions.isRGvalid('8167423414').status == Response(status=500).status


#test CNPJ
def test_notvalidateCNPJ():
    assert global_functions.isCNPJvalid('375496712311271') == False

def test_truevalidateCNPJ():
    assert global_functions.isCNPJvalid('37549670000171') == True

def test_wrongCNPJtype():
    assert global_functions.isCNPJvalid(37549670000171).status == Response(status=500).status


#Test UF exists

def test_wrongtype_patient_adressUF():
    assert global_functions.ufExists(1231).status == Response(status=500).status

def test_notexistopiton_patient_adressUF():
    assert global_functions.ufExists('AUYD') == False

def test_AC_optionUpper_patient_adressUF():
    assert global_functions.ufExists('AC') == True

def test_AC_optionLower_patient_adressUF():
    assert global_functions.ufExists('ac') == True

def test_AL_optionUpper_patient_adressUF():
    assert global_functions.ufExists('AL') == True

def test_AL_optionLower_patient_adressUF():
    assert global_functions.ufExists('al') == True

def test_AP_optionUpper_patient_adressUF():
    assert global_functions.ufExists('AP') == True

def test_AP_optionLower_patient_adressUF():
    assert global_functions.ufExists('ap') == True

def test_AM_optionUpper_patient_adressUF():
    assert global_functions.ufExists('AM') == True

def test_AM_optionLower_patient_adressUF():
    assert global_functions.ufExists('am') == True

def test_BA_optionUpper_patient_adressUF():
    assert global_functions.ufExists('BA') == True

def test_BA_optionLower_patient_adressUF():
    assert global_functions.ufExists('ba') == True

def test_CE_optionUpper_patient_adressUF():
    assert global_functions.ufExists('CE') == True

def test_CE_optionLower_patient_adressUF():
    assert global_functions.ufExists('ce') == True

def test_DF_optionUpper_patient_adressUF():
    assert global_functions.ufExists('DF') == True

def test_DF_optionLower_patient_adressUF():
    assert global_functions.ufExists('df') == True

def test_ES_optionUpper_patient_adressUF():
    assert global_functions.ufExists('ES') == True

def test_ES_optionLower_patient_adressUF():
    assert global_functions.ufExists('es') == True

def test_GO_optionUpper_patient_adressUF():
    assert global_functions.ufExists('GO') == True

def test_GO_optionLower_patient_adressUF():
    assert global_functions.ufExists('go') == True

def test_MA_optionUpper_patient_adressUF():
    assert global_functions.ufExists('MA') == True

def test_MA_optionLower_patient_adressUF():
    assert global_functions.ufExists('ma') == True

def test_MS_optionUpper_patient_adressUF():
    assert global_functions.ufExists('MS') == True

def test_MS_optionLower_patient_adressUF():
    assert global_functions.ufExists('ms') == True

def test_MT_optionUpper_patient_adressUF():
    assert global_functions.ufExists('MT') == True

def test_MT_optionLower_patient_adressUF():
    assert global_functions.ufExists('mt') == True

def test_MG_optionUpper_patient_adressUF():
    assert global_functions.ufExists('MG') == True

def test_MG_optionLower_patient_adressUF():
    assert global_functions.ufExists('mg') == True

def test_PA_optionUpper_patient_adressUF():
    assert global_functions.ufExists('PA') == True

def test_PA_optionLower_patient_adressUF():
    assert global_functions.ufExists('pa') == True

def test_PB_optionUpper_patient_adressUF():
    assert global_functions.ufExists('PB') == True

def test_PB_optionLower_patient_adressUF():
    assert global_functions.ufExists('pb') == True

def test_PR_optionUpper_patient_adressUF():
    assert global_functions.ufExists('PR') == True

def test_PR_optionLower_patient_adressUF():
    assert global_functions.ufExists('pr') == True

def test_PE_optionUpper_patient_adressUF():
    assert global_functions.ufExists('PE') == True

def test_PE_optionLower_patient_adressUF():
    assert global_functions.ufExists('pe') == True

def test_PI_optionUpper_patient_adressUF():
    assert global_functions.ufExists('PI') == True

def test_PI_optionLower_patient_adressUF():
    assert global_functions.ufExists('pi') == True

def test_RJ_optionUpper_patient_adressUF():
    assert global_functions.ufExists('RJ') == True

def test_RJ_optionLower_patient_adressUF():
    assert global_functions.ufExists('rj') == True

def test_RN_optionUpper_patient_adressUF():
    assert global_functions.ufExists('RN') == True

def test_RN_optionLower_patient_adressUF():
    assert global_functions.ufExists('rn') == True

def test_RS_optionUpper_patient_adressUF():
    assert global_functions.ufExists('RS') == True

def test_RS_optionLower_patient_adressUF():
    assert global_functions.ufExists('rs') == True

def test_RO_optionUpper_patient_adressUF():
    assert global_functions.ufExists('RO') == True

def test_RO_optionLower_patient_adressUF():
    assert global_functions.ufExists('ro') == True

def test_RR_optionUpper_patient_adressUF():
    assert global_functions.ufExists('RR') == True

def test_RR_optionLower_patient_adressUF():
    assert global_functions.ufExists('rr') == True

def test_SC_optionUpper_patient_adressUF():
    assert global_functions.ufExists('SC') == True

def test_SC_optionLower_patient_adressUF():
    assert global_functions.ufExists('sc') == True

def test_SP_optionUpper_patient_adressUF():
    assert global_functions.ufExists('SP') == True

def test_SP_optionLower_patient_adressUF():
    assert global_functions.ufExists('sp') == True

def test_SE_optionUpper_patient_adressUF():
    assert global_functions.ufExists('SE') == True

def test_SE_optionLower_patient_adressUF():
    assert global_functions.ufExists('se') == True

def test_TO_optionUpper_patient_adressUF():
    assert global_functions.ufExists('TO') == True

def test_TO_optionLower_patient_adressUF():
    assert global_functions.ufExists('to') == True