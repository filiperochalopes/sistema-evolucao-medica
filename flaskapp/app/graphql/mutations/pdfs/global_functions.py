import re
from flask import Response

def isCNSvalid(cns:int) -> bool:
    """verify if the CNS is valid
    code by: philippeoz

    Args:
        cns (int): cns number that will be validated
    """
    if type(cns) != type(int()):
        return Response('The api has to use CNS as intenger to validate, please check te function', status=500)
    cns = ''.join(filter(str.isdigit, str(cns)))
    if len(cns) != 15:
        return False
    
    return sum(
        [int(cns[i]) * (15 - i) for i in range(15)]
    ) % 11 == 0


def isRGvalid(rg:int) -> bool:
    # Notice that RG changes a lot in every brazillian state
    # so theres a chance that a invalid RG has pass as Valid
    # just because RG is matematician valid dont mean that exists in government database
    #the only verification that can do is the maximum value
    if type(rg) != type(int()):
        return Response('The api has to use RG as intenger to validate, please check te function', status=500)
    if 6 <= len(str(rg)) and len(str(rg)) <= 16:
        return True
    return False


def isCPFvalid(cpf: str) -> bool:
    """Verify if the CPF is valid

    Args:
        cpf (str): cpf to be validated

    Returns:
        bool: true or false
    """    
    if type(cpf) != type(str()):
        return Response('The api has to use CPF as string to validate, please check te function', status=500)
    # Verify format
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # receive only numbers
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # See if all numbers are equal or longer than 11 digits
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validate first verificator digit
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validate second verificator digit

    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False
    return True


if __name__ == "__main__":
    cpf = 142342343234
    print(isCPFvalid(cpf))

    