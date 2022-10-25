from pdfs import pdf_functions
from flask import Response


#Testing globals functions
def test_notvalidateCPF():
    assert pdf_functions.is_CPF_valid('434.123.123-99') == False

def test_truevalidateCPF():
    assert pdf_functions.is_CPF_valid('434.234.123-99') == True

def test_wrongCPFtype():
    assert pdf_functions.is_CPF_valid(8167423414).status == Response(status=500).status


def test_emptyCPF():
    assert pdf_functions.is_CPF_valid('            ') == False

def test_notvalidateCNS():
    assert pdf_functions.is_CNS_valid(914874125754123) == False

def test_truevalidateCNS():
    assert pdf_functions.is_CNS_valid(928976954930007) == True

def test_wrongCNStype():
    assert pdf_functions.is_CNS_valid('8167423414').status == Response(status=500).status


def test_longnotvalidateRG():
    assert pdf_functions.is_RG_valid(9197841521982457189247195271597495195714) == False
    
def test_notvalidateRG():
    assert pdf_functions.is_RG_valid(91454) == False

def test_truevalidateRG():
    assert pdf_functions.is_RG_valid(928976954930007) == True

def test_wrongRGtype():
    assert pdf_functions.is_RG_valid('8167423414').status == Response(status=500).status


#test CNPJ
def test_notvalidateCNPJ():
    assert pdf_functions.is_CNPJ_valid('375496712311271') == False

def test_truevalidateCNPJ():
    assert pdf_functions.is_CNPJ_valid('37549670000171') == True

def test_wrongCNPJtype():
    assert pdf_functions.is_CNPJ_valid(37549670000171).status == Response(status=500).status


#Test UF exists

def test_wrongtype_patient_adressUF():
    assert pdf_functions.uf_exists(1231).status == Response(status=500).status

def test_notexistopiton_patient_adressUF():
    assert pdf_functions.uf_exists('AUYD') == False

def test_AC_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('AC') == True

def test_AC_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('ac') == True

def test_AL_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('AL') == True

def test_AL_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('al') == True

def test_AP_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('AP') == True

def test_AP_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('ap') == True

def test_AM_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('AM') == True

def test_AM_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('am') == True

def test_BA_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('BA') == True

def test_BA_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('ba') == True

def test_CE_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('CE') == True

def test_CE_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('ce') == True

def test_DF_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('DF') == True

def test_DF_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('df') == True

def test_ES_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('ES') == True

def test_ES_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('es') == True

def test_GO_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('GO') == True

def test_GO_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('go') == True

def test_MA_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('MA') == True

def test_MA_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('ma') == True

def test_MS_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('MS') == True

def test_MS_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('ms') == True

def test_MT_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('MT') == True

def test_MT_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('mt') == True

def test_MG_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('MG') == True

def test_MG_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('mg') == True

def test_PA_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('PA') == True

def test_PA_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('pa') == True

def test_PB_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('PB') == True

def test_PB_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('pb') == True

def test_PR_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('PR') == True

def test_PR_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('pr') == True

def test_PE_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('PE') == True

def test_PE_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('pe') == True

def test_PI_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('PI') == True

def test_PI_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('pi') == True

def test_RJ_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('RJ') == True

def test_RJ_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('rj') == True

def test_RN_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('RN') == True

def test_RN_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('rn') == True

def test_RS_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('RS') == True

def test_RS_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('rs') == True

def test_RO_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('RO') == True

def test_RO_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('ro') == True

def test_RR_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('RR') == True

def test_RR_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('rr') == True

def test_SC_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('SC') == True

def test_SC_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('sc') == True

def test_SP_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('SP') == True

def test_SP_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('sp') == True

def test_SE_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('SE') == True

def test_SE_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('se') == True

def test_TO_optionUpper_patient_adressUF():
    assert pdf_functions.uf_exists('TO') == True

def test_TO_optionLower_patient_adressUF():
    assert pdf_functions.uf_exists('to') == True