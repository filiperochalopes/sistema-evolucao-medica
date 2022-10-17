import re
from flask import Response
from itertools import cycle
from reportlab.pdfgen import canvas
from PyPDF2  import PdfWriter

ufs = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MS','MT','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']

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
    if 5 < len(str(rg)) and len(str(rg)) < 17:
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


def ufExists(uf:str):
    """Verify if a uf exists in Brazil

    Args:
        uf (str): uf to berify

    Returns:
        Bollean true or false
        Reponse if the receive worng type
    """    
    if type(uf) != type(str()):
        return Response('The api has to use UF as string to validate, please check te function', status=500)
    
    return True if uf.upper() in ufs else False


def isCNPJvalid(cnpj:str):
    """Verify if a cnpj is valid

    Args:
        cnpj (str): cnpj without symbols

    Returns:
        Bollean true or false
        Reponse if the receive worng type
    """    
    if type(cnpj) != type(str()):
        return Response('The api has to use cnpj as string to validate, please check te function', status=500)
    if len(cnpj) != 14:
        return False

    if cnpj in (c * 14 for c in "1234567890"):
        return False

    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False

    return True


def add_data(can:canvas.Canvas, data:str, pos:tuple):
    """Add data in pdf using canvas object

    Args:
        can (canvas.Canvas): canvas that will be used to add data
        data (str): data to be added
        pos (tuple): data insert position in points

    Returns:
        can(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response: with the error)
    """
    try:
        can.drawString(pos[0], pos[1], data)
        return can
    except:
        return Response("Error when adding data to document with canvas", status=500)


def add_square(canvas:canvas.Canvas, pos:tuple, size:tuple=(9, 9)):
    """Add square in document using canvas object

    Args:
        canvas (canvas.Canvas): canvas to use
        pos (tuple): position to add the square
        size (tuple, optional): square size default is the size of the option quare. Defaults to 9.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response: with the error)
    """    
    try:
        canvas.rect(x=pos[0], y=pos[1], width=size[0], height=size[1], fill=1)
        return canvas
    except:
        return Response("Error when adding square to document with canvas", status=500)


def add_centralized_data(canvas:canvas.Canvas, data:str, pos:tuple):
    """Add centralized_data in pdf using canvas object

    Args:
        canvas (canvas.Canvas): canvas that will be used to add centralized_data
        data (str): centralized_data to be added
        pos (tuple): centralized_data insert position in points

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response: with the error)
    """
    try:
        canvas.drawCentredString(pos[0], pos[1], data)
        return canvas
    except:
        return Response("Error when adding centralized data to document with canvas", status=500)

        
def write_newpdf(newpdf:PdfWriter, new_directory:str):
    """Write new pdf in a file

    Args:
        newpdf (PdfFileWriter): new pdf with all the changes made by canvas
        new_directory (str): directory to save the new pdf
    Returns:
        None
        or
        Response(flask.Response: with the error)
    """ 
    try:
        outputFile = open(new_directory, 'wb')
        newpdf.write(outputFile)
        outputFile.close()
    except:
        return Response("Error when writing new pdf", status=500)


def add_oneline_text(can:canvas.Canvas, text:str, pos:tuple, campName:str, lenMax:int, lenMin:int=0):
    """Add text that is fill in one line

    Args:
        can (canvas.Canvas): canvas to use
        text (str): text value
        pos (tuple): position in canvas
        campName (str): Camp name, this is used when return Responses
        lenMax (int): maximum text lenght
        lenMin (int, optional): Minimum text lenght. Defaults to 0.
    """    
    try:
        if type(text) != type(str()):
            return Response(f'text has to be string', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos) != type(tuple()):
            return Response(f'pos has to be tuple', status=500)
        elif type(campName) != type(str()):
            return Response(f'campName has to be str', status=500)
        elif type(lenMax) != type(int()):
            return Response(f'lenMax has to be int', status=500)
        elif type(lenMin) != type(int()):
            return Response(f'lenMin has to be int', status=500)

        # verify if text is in the need lenght
        text = text.strip()
        if lenMin < len(text) <= lenMax:
            can = add_data(can=can, data=text, pos=pos)
            return can
        else:
            return Response(f"Unable to add {campName} because is longer than {lenMax} characters or smaller than {lenMin}", status=400)
    except:
        return Response(f'Unknow error while adding {campName}', status=500)




if __name__ == "__main__":
    cpf = 142342343234
    print(isCPFvalid(cpf))
    