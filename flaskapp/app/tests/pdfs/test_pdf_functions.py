from app.services.utils import pdf_functions
from flask import Response
import pytest


def test_longnotvalidateRG():
    assert pdf_functions.is_RG_valid("9197841521982457189247195271597495195714") == False
    
def test_notvalidateRG():
    assert pdf_functions.is_RG_valid("91454") == False

def test_truevalidateRG():
    assert pdf_functions.is_RG_valid("928976954930007") == True



#Test UF exists

@pytest.mark.parametrize("test_input", ['AC', 'ac', 'AL', 'al', 'AP', 'ap', 'AM', 'am', 'BA', 'ba', 'CE', 'ce', 'DF', 'df', 'ES', 'es', 'GO', 'go', 'MA', 'ma', 'MS', 'ms', 'MT','mt', 'MG', 'mg', 'PA', 'pa', 'PB', 'pb', 'PE', 'pe', 'PR', 'pr', 'PI', 'pi', 'RJ', 'rj', 'RN', 'rn', 'RS', 'rs', 'RO', 'ro', 'RR', 'rr', 'SC', 'sc', 'SP', 'sp', 'SE', 'se', 'TO', 'to'])
def test_ufs(test_input):
    assert pdf_functions.uf_exists(test_input) == True
