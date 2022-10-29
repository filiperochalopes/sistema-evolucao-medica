import re
from flask import Response
from itertools import cycle
from reportlab.pdfgen import canvas
from PyPDF2  import PdfWriter
import datetime
from typing import Union
from inspect import getfullargspec

def validate_func_args(function_to_verify, variables_to_verify:dict, nullable_variables:list=[]) -> Union[None, Response]:
    """validate all args with the type needed or default values

    Args:
        function_to_verify: function to verify, like function_to_verify
        variables_to_verify (dict): dict with variable name and variable valuea
        nullable_variables (list): list with variables that can be null

    Returns:
        [None, Response]: None if is all alright or Response with a error
    """  
    try:
    #get args types and defaults types form function
        args_types = getfullargspec(function_to_verify)[6]
        defaults_types = getfullargspec(function_to_verify)[3]
        if defaults_types == None:
            defaults_types = (None, None)
        
        defaults_types = [type(x) for x in defaults_types]
        #Verify every key
        for variables_keys in args_types.keys():
            if variables_keys == 'return':
                continue

            right_type = args_types[variables_keys]
            arg_to_validate = type(variables_to_verify[variables_keys])
            
            if right_type == arg_to_validate:
                continue
            elif arg_to_validate in defaults_types and variables_keys in nullable_variables:
                continue
            else:
                return Response(f'{variables_keys} has wrong type, has to be {right_type}', status=400)
        return None
    except KeyError:
        return Response(f'KeyError, some key in {function_to_verify} is missing, when validate types, keys needed {args_types.keys()}', status=500)
    except:
        return Response(f'{arg_to_validate} type {right_type} unkown error while validate_func_args {variables_keys} in {function_to_verify} function', status=500)
        #return Response(f'unkown error while validate_func_args {variables_keys} in {function_to_verify} function', status=500)



def is_CNS_valid(cns:int) -> bool:
    """verify if the CNS is valid
    code by: philippeoz

    Args:
        cns (int): cns number that will be validated
    """
    verify = validate_func_args(function_to_verify=is_CNS_valid, variables_to_verify={'cns':cns})
    if type(verify) == type(Response()):
        return verify
    cns = ''.join(filter(str.isdigit, str(cns)))
    if len(cns) != 15:
        return False
    
    return sum(
        [int(cns[i]) * (15 - i) for i in range(15)]
    ) % 11 == 0


def is_RG_valid(rg:int) -> bool:
    # Notice that RG changes a lot in every brazillian state
    # so theres a chance that a invalid RG has pass as Valid
    # just because RG is matematician valid dont mean that exists in government database
    #the only verification that can do is the maximum value
    verify = validate_func_args(function_to_verify=is_RG_valid, variables_to_verify={'rg':rg})
    if type(verify) == type(Response()):
        return verify
    if 5 < len(str(rg)) < 17:
        return True
    return False


def is_CPF_valid(cpf: str) -> bool:
    """Verify if the CPF is valid

    Args:
        cpf (str): cpf to be validated

    Returns:
        bool: true or false
    """
    verify = validate_func_args(function_to_verify=is_CPF_valid, variables_to_verify={'cpf':cpf}, nullable_variables=['cpf'])
    if type(verify) == type(Response()):
        return verify
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


def uf_exists(uf:str) -> Union[bool, Response]:
    """Verify if a uf exists in Brazil

    Args:
        uf (str): uf to verify 

    Returns:
        Bollean true or false
        Reponse if the receive worng type
    """    
    verify = validate_func_args(function_to_verify=uf_exists, variables_to_verify={'uf':uf})
    if type(verify) == type(Response()):
        return verify
    return bool(re.match(r'^(\s*(AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RJ|RN|RS|RO|RR|SC|SP|SE|TO)?)$', uf, flags=re.I))


def is_CNPJ_valid(cnpj:str) -> Union[bool, Response]:
    """Verify if a cnpj is valid

    Args:
        cnpj (str): cnpj without symbols

    Returns:
        Bollean true or false
        Reponse if the receive worng type
    """
    verify = validate_func_args(function_to_verify=is_CNPJ_valid, variables_to_verify={'cnpj':cnpj})
    if type(verify) == type(Response()):
        return verify

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


def add_data(can:canvas.Canvas, data:str, pos:tuple) -> Union[canvas.Canvas, Response]:
    """Add data in pdf using canvas object

    Args:
        can (canvas.Canvas): canvas that will be used to add data
        data (str): data to be added
        pos (tuple): data insert position in points

    Returns:
        can(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """
    try:
        can.drawString(pos[0], pos[1], data)
        return can
    except:
        return Response("Error when adding data to document with canvas", status=500)


def add_square(can:canvas.Canvas, pos:tuple, size:tuple=(9, 9)) -> Union[canvas.Canvas, Response]:
    """Add square in document using canvas object

    Args:
        can (canvas.Canvas): canvas to use
        pos (tuple): position to add the square
        size (tuple, optional): square size default is the size of the option quare. Defaults to 9.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        can.rect(x=pos[0], y=pos[1], width=size[0], height=size[1], fill=1)
        return can
    except:
        return Response("Error when adding square to document with canvas", status=500)


def add_centralized_data(can:canvas.Canvas, data:str, pos:tuple) -> Union[canvas.Canvas, Response]:
    """Add centralized_data in pdf using canvas object

    Args:
        can (canvas.Canvas): canvas that will be used to add centralized_data
        data (str): centralized_data to be added
        pos (tuple): centralized_data insert position in points

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """
    try:
        can.drawCentredString(pos[0], pos[1], data)
        return can
    except:
        return Response("Error when adding centralized data to document with canvas", status=500)

        
def write_newpdf(newpdf:PdfWriter, new_directory:str) -> Union[None, Response]:
    """Write new pdf in a file

    Args:
        newpdf (PdfFileWriter): new pdf with all the changes made by canvas
        new_directory (str): directory to save the new pdf
    Returns:
        None
        or
        Response(flask.Response): with the error
    """ 
    try:
        output_file = open(new_directory, 'wb')
        newpdf.write(output_file)
        output_file.close()
    except:
        return Response("Error when writing new pdf", status=500)


def add_oneline_text(can:canvas.Canvas, text:str, pos:tuple, camp_name:str, len_max:int, nullable:bool=False, len_min:int=0, interval:str='', centralized:bool=False) -> Union[canvas.Canvas, Response]:
    """Add text that is fill in one line

    Args:
        can (canvas.Canvas): canvas to use
        text (str): text value
        pos (tuple): position in canvas
        camp_name (str): Camp name, this is used when return Responses
        len_max (int): maximum text lenght
        nullable (bool, optional): Data can me None. Defaults to False.
        len_min (int, optional): Minimum text lenght. Defaults to 0.
        interval (str): interval to add between every char
        centralized (bool, optional): Data has to be centralized. Defaults to False.
    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """
    try:
        if nullable:
            if text == None or len(str(text).strip()) == 0:
                return can

        verify = validate_func_args(function_to_verify=add_oneline_text, variables_to_verify={'can':can, 'text':text, 'pos':pos, 'camp_name':camp_name, 'len_max':len_max, 'nullable':nullable, 'len_min':len_min, 'interval':interval, 'centralized':centralized})
        if type(verify) == type(Response()):
            return verify
        

        if not nullable:
            text = text.strip()
            if len(text) == 0:
                return Response(f'{camp_name} cannot be empty', status=400)
        # verify if text is in the need lenght
        text = text.strip()
        if len_min <= len(text) <= len_max:
            text = add_interval_to_data(data=text, interval=interval)
            if centralized:
                can = add_centralized_data(can=can, data=text, pos=pos)
            else:
                can = add_data(can=can, data=text, pos=pos)
            return can
        else:
            return Response(f"Unable to add {camp_name} because is longer than {len_max} characters or smaller than {len_min}", status=400)
    except:
        return Response(f'Unknow error while adding {camp_name}', status=500)


def add_morelines_text(can:canvas.Canvas, text:str, initial_pos:tuple, decrease_ypos:int, camp_name:str, len_max:int, char_per_lines:int, max_lines_amount:int=None, nullable:bool=False, len_min:int=0, interval:str='') -> Union[canvas.Canvas, Response]:
    """Add text that is fill in one line

    Args:
        can (canvas.Canvas): canvas to use
        text (str): text value
        initial_pos (tuple): initial position in canvas
        decrease_ypos (int): decrease y value to break lines
        camp_name (str): Camp name, this is used when return Responses
        len_max (int): maximum text lenght
        char_per_lines (int): char amount for every lines
        max_lines_amount (int, optional): maximum lines amount . Defaults to None.
        nullable (bool, optional): Data can me None. Defaults to False.
        len_min (int, optional): Minimum text lenght. Defaults to 0.
        interval (str): interval to add between every char
    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error_summary_
    """    
    try:
        if nullable:
            if text == None or len(str(text).strip()) == 0:
                return can
        verify = validate_func_args(function_to_verify=add_morelines_text, variables_to_verify={'can':can, 'text':text, 'initial_pos':initial_pos, 'decrease_ypos':decrease_ypos, 'camp_name':camp_name, 'len_max':len_max, 'char_per_lines':char_per_lines, 'max_lines_amount':max_lines_amount, 'nullable':nullable, 'len_min':len_min, 'interval':interval}, nullable_variables=['max_lines_amount'])
        if type(verify) == type(Response()):
            return verify

        if type(text) != type(str()):
            return Response(f'{camp_name} has to be string, if can be null, please add nullable option', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(initial_pos) != type(tuple()):
            return Response(f'initial_pos has to be tuple', status=500)
        elif type(decrease_ypos) != type(int()):
            return Response(f'decrease_ypos has to be int', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(len_max) != type(int()):
            return Response(f'len_max has to be int', status=500)
        elif type(char_per_lines) != type(int()):
            return Response(f'char_per_lines has to be int', status=500)
        elif type(max_lines_amount) != type(int()) and max_lines_amount != None:
            return Response(f'max_lines_amount has to be int', status=500)
        elif type(len_min) != type(int()):
            return Response(f'len_min has to be int', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)

        if not nullable:
            text = text.strip()
            if len(text) == 0:
                return Response(f'{camp_name} cannot be empty', status=400)
        # verify if text is in the need lenght
        text = text.strip()
        if len_min <= len(text) <= len_max:
            text = add_interval_to_data(data=text, interval=interval)
            str_to_line = ''
            broke_lines_times = int(len(text)/char_per_lines)
            if max_lines_amount != None and broke_lines_times + 1 > max_lines_amount:
                return Response(f'Unable to add {camp_name} because lines amount needed is more than {max_lines_amount}', status=500)
            current_line = char_per_lines
            last_line = 0
            xpos = initial_pos[0]
            ypos = initial_pos[1]
            # Making the line break whem has max charater limiti reached in a line
            while broke_lines_times >= 0:
                str_to_line = text[last_line:current_line]
                can = add_data(can=can, data=str_to_line, pos=(xpos, ypos))
                last_line = current_line
                current_line += char_per_lines
                broke_lines_times -= 1
                ypos -= decrease_ypos

            return can
        else:
            return Response(f"Unable to add {camp_name} because is longer than {len_max} characters or smaller than {len_min}", status=400)
    except:
        return Response(f'Unknow error while adding {camp_name}', status=500)


def add_phonenumber(can:canvas.Canvas, number:int, pos:tuple, camp_name:str, nullable:bool=False, interval:str='', formated:bool=False) -> Union[canvas.Canvas, Response]:
    """_summary_

    Args:
        can (canvas.Canvas):  canvas to use
        number (int): number to add
        pos (tuple): position in canvas
        camp_name (str): camp name to Responses
        nullable (bool, optional):  Data can me None. Defaults to False.
        interval (str, optional): interval to add between every char
        formated (bool, optional): format phone number to (xx) xxxxx-xxxx. Defaults to False.
    """
    try:
        if nullable:
            if number == None:
                return can
        if type(number) != type(int()):
            return Response(f'{camp_name} has to be int, if can be null, please add nullable option', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos) != type(tuple()):
            return Response(f'pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)
        elif type(formated) != type(bool()):
            return Response(f'formated has to be bool', status=500)
        
        number = str(number)
        if 10 <= len(number) <= 11:
            if formated:
                number = '(' + number[:2] + ') ' + number[2:7] + '-' + number[7:]

            number = add_interval_to_data(data=number, interval=interval)
            can = add_data(can=can, data=number, pos=pos)
            return can
        else:
            return Response(f"Unable to add {camp_name} because is longer than {10} characters or smaller than {11}", status=400)
    except:
        return Response(f'Unknow error while adding {camp_name}', status=500)


def add_CEP(can:canvas.Canvas, cep:int, pos:tuple, camp_name:str, nullable:bool=False, interval:str='', formated:bool=False) -> Union[canvas.Canvas, Response]:
    """Add cep to canvas

    Args:
        can (canvas.Canvas):  canvas to use
        cep (int): cep to add
        pos (tuple): position in canvas
        camp_name (str): camp name to Responses
        nullable (bool, optional):  Data can me None. Defaults to False.
        interval (str, optional): interval to add between every char
        formated (bool, optional): format phone cep to xxxxx-xxx. Defaults to False.
    """
    try:
        if nullable:
            if cep == None:
                return can
        if type(cep) != type(int()):
            return Response(f'{camp_name} has to be int, if can be null, please add nullable option', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos) != type(tuple()):
            return Response(f'pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)
        elif type(formated) != type(bool()):
            return Response(f'formated has to be bool', status=500)
        
        cep = str(cep)
        if len(cep) == 8:
            if formated:
                cep = cep[:5] + '-' + cep[5:]

            cep = add_interval_to_data(data=cep, interval=interval)
            can = add_data(can=can, data=cep, pos=pos)
            return can
        else:
            return Response(f"Unable to add {camp_name} because cpf dont have 8 digits", status=400)
    except:
        return Response(f'Unknow error while adding {camp_name}', status=500)


def add_oneline_intnumber(can:canvas.Canvas, number:int, pos:tuple, camp_name:str, len_max:int, value_min:int, value_max:int, nullable:bool=False, len_min:int=0, interval:str='', centralized:bool=False) -> Union[canvas.Canvas, Response]:
    """Add one line number to canvas

    Args:
        can (canvas.Canvas): canvas to use
        number (int): number to add
        pos (tuple): position in canvas
        camp_name (str): camp name to Responses
        len_max (int): Maximum Lenght
        value_max (int): Maximum Value
        value_min (int): Minimun Value
        nullable (bool, optional): Data can me None. Defaults to False.
        len_min (int, optional): Minimun Lenght. Defaults to 0.
        interval (str): interval to add between every char
        centralized (bool, optional): Data has to be centralized. Defaults to False.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if number == None:
                return can
        if type(number) != type(int()):
            return Response(f'{camp_name} has to be int, if can be null, please add nullable option', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos) != type(tuple()):
            return Response(f'pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(len_max) != type(int()):
            return Response(f'len_max has to be int', status=500)
        elif type(len_min) != type(int()):
            return Response(f'len_min has to be int', status=500)
        elif type(value_max) != type(int()):
            return Response(f'value_max has to be int', status=500)
        elif type(value_min) != type(int()):
            return Response(f'value_min has to be int', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)
        elif type(centralized) != type(bool()):
            return Response(f'centralized has to be bool', status=500)

        # verify if number is in the need lenght
        if value_min > number or value_max < number:
            return Response(f"Unable to add {camp_name} because is bigger than {value_max} and smaller than {value_min}", status=400)
        number = str(number)
        if len_min <= len(number) <= len_max:
            number = add_interval_to_data(data=number, interval=interval)
            if centralized:
                can = add_centralized_data(can=can, data=number, pos=pos)
            else:
                can = add_data(can=can, data=number, pos=pos)
            return can
        else:
            return Response(f"Unable to add {camp_name} because is longer than {len_max} characters or smaller than {len_min}", status=400)
    except:
        return Response(f'Unknow error while adding {camp_name}', status=500)


def add_oneline_floatnumber(can:canvas.Canvas, number:float, pos:tuple, camp_name:str, len_max:int, value_min:float, value_max:float, nullable:bool=False, len_min:int=0, interval:str='', centralized:bool=False, ndigits:int=2) -> Union[canvas.Canvas, Response]:
    """Add one line number to canvas

    Args:
        can (canvas.Canvas): canvas to use
        number (float): number to add
        pos (tuple): position in canvas
        camp_name (str): camp name to Responses
        len_max (int): Maximum Lenght
        value_max (float): Maximum Value
        value_min (float): Minimun Value
        nullable (bool, optional): Data can me None. Defaults to False.
        len_min (int, optional): Minimun Lenght. Defaults to 0.
        interval (str): interval to add between every char
        centralized (bool, optional): Data has to be centralized. Defaults to False.
        ndigits (int, optional): Number of digits after , . Defaults to 2.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if number == None:
                return can
        if type(number) != type(float()) and type(number) != type(int()):
            return Response(f'{camp_name} has to be float, if can be null, please add nullable option', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos) != type(tuple()):
            return Response(f'pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(len_max) != type(int()):
            return Response(f'len_max has to be int', status=500)
        elif type(len_min) != type(int()):
            return Response(f'len_min has to be int', status=500)
        elif type(value_max) != type(float()) and type(number) != type(int()):
            return Response(f'value_max has to be float', status=500)
        elif type(value_min) != type(float()) and type(number) != type(int()):
            return Response(f'value_min has to be float', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)
        elif type(centralized) != type(bool()):
            return Response(f'centralized has to be bool', status=500)
        elif type(ndigits) != type(int()):
            return Response(f'ndigits has to be int', status=500)

        # verify if number is in the need lenght
        if value_min > number or value_max < number:
            return Response(f"Unable to add {camp_name} because is bigger than {value_max} and smaller than {value_min}", status=400)
        number = round(number, ndigits)
        number = str(number)
        if len_min <= len(number) <= len_max:
            number = add_interval_to_data(data=number, interval=interval)
            if centralized:
                can = add_centralized_data(can=can, data=number, pos=pos)
            else:
                can = add_data(can=can, data=number, pos=pos)
            return can
        else:
            return Response(f"Unable to add {camp_name} because is longer than {len_max} characters or smaller than {len_min}", status=400)
    except:
        return Response(f'Unknow error while adding {camp_name}', status=500)


def add_interval_to_data(data:str, interval:str) -> Union[str, Response]:
    """add interval to data

    Args:
        data (str): data
        interval (str): interval to add betwaeen every char

    Returns:
        interval(str): data with the intervals add
        or
        Response(flask.Response): with the error
    """    
    if type(data) != type(str()):
        return Response('The api has to use data in add interval as string, please check te function', status=500)
    elif type(interval) != type(str()):
        return Response('The api has to use interval in add interval as string, please check te function', status=500)
    # Add nterval between data
    return interval.join(data)


def add_cns(can:canvas.Canvas, cns:int, pos:tuple, camp_name:str,nullable:bool=False, formated:bool=False, interval:str='') -> Union[canvas.Canvas, Response]:
    """Add cns to canvas

    Args:
        can (canvas.Canvas): canvas to add
        cns (int): cns to add
        pos (tuple): position in canvas
        camp_name (str): camp nam
        nullable (bool, optional): can be null. Defaults to False.
        formated (bool, optional): format cns to xxx xxxx xxxx xxxx. Defaults to False.
        interval (str, optional): interval to add between interval. Defaults to ''.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if cns == None:
                return can
        if type(cns) != type(int()):
            return Response(f'{camp_name} has to be int', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos) != type(tuple()):
            return Response(f'pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(formated) != type(bool()):
            return Response(f'formated has to be bool', status=500)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)

        # Verify if the cns is valid
        if is_CNS_valid(cns):
            cns = str(cns)
            # Add interval selected
            cns = add_interval_to_data(data=cns, interval=interval)
            if type(cns) == type(Response()): return cns
            if formated: 
                cns = cns[:3] + " " + cns[3:7] + " " + cns[7:11] + " " + cns[11:15]
            can = add_data(can=can, data=cns, pos=pos)
            return can
        else:
            return Response(f"Unable to add {camp_name} because is a invalid CNS", status=400)
    except:
        return Response(f'Unknow error while adding {camp_name}', status=500)


def add_cnpj(can:canvas.Canvas, cnpj:int, pos:tuple, camp_name:str,nullable:bool=False, interval:str='') -> Union[canvas.Canvas, Response]:
    """Add cnpj to canvas

    Args:
        can (canvas.Canvas): canvas to add
        cnpj (int): cnpj to add
        pos (tuple): position in canvas
        camp_name (str): camp nam
        nullable (bool, optional): can be null. Defaults to False.
        interval (str, optional): interval to add between interval. Defaults to ''.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if cnpj == None:
                return can
        if type(cnpj) != type(int()):
            return Response(f'{camp_name} has to be int', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos) != type(tuple()):
            return Response(f'pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)

        # Verify if the cnpj is valid
        cnpj = str(cnpj)
        if is_CNPJ_valid(cnpj):
            # Add interval selected
            cnpj = add_interval_to_data(data=cnpj, interval=interval)
            if type(cnpj) == type(Response()): return cnpj
            can = add_data(can=can, data=cnpj, pos=pos)
            return can
        else:
            return Response(f"Unable to add {camp_name} because is a invalid cnpj", status=400)
    except:
        return Response(f'Unknow error while adding {camp_name}', status=500)


def add_cnae(can:canvas.Canvas, cnae:int, pos:tuple, camp_name:str, nullable:bool=False, formated:bool=False) -> Union[canvas.Canvas, Response]:
    """Add cnae to canvas

    Args:
        can (canvas.Canvas): canvas to add
        cnae (int): cnae to add
        pos (tuple): position in canvas
        camp_name (str): camp nam
        nullable (bool, optional): can be null. Defaults to False.
        interval (str, optional): interval to add between interval. Defaults to ''.
        formated (bool, optional): format (add '/' and ':'). Defaults to True.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if cnae == None:
                return can
        if type(cnae) != type(int()):
            return Response(f'{camp_name} has to be int', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos) != type(tuple()):
            return Response(f'pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(formated) != type(bool()):
            return Response(f'formated has to be bool', status=500)

        cnae = str(cnae)
        if len(cnae) == 7:
            #Format cnae to add in doc
            if formated:
                cnae = cnae[:2] + '.' + cnae[2:4] + '-' + cnae[4] + '-' + cnae[5:]
            can = add_data(can=can, data=cnae, pos=pos)
            return can
        else:
            return Response(f"Unable to add {camp_name} because is a invalid cnae", status=400)
    except:
        return Response(f'Unknow error while adding {camp_name}', status=500)


def add_cbor(can:canvas.Canvas, cbor:int, pos:tuple, camp_name:str, nullable:bool=False, formated:bool=False) -> Union[canvas.Canvas, Response]:
    """Add cbor to canvas

    Args:
        can (canvas.Canvas): canvas to add
        cbor (int): cbor to add
        pos (tuple): position in canvas
        camp_name (str): camp nam
        nullable (bool, optional): can be null. Defaults to False.
        formated (bool, optional): format (add '/' and ':'). Defaults to True.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if cbor == None:
                return can
        if type(cbor) != type(int()):
            return Response(f'{camp_name} has to be int', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos) != type(tuple()):
            return Response(f'pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(formated) != type(bool()):
            return Response(f'formated has to be bool', status=500)

        cbor = str(cbor)
        if len(cbor) == 6:
            #Format cbor to add in doc
            if formated:
                cbor = cbor[:5] + '-' + cbor[5:]
            can = add_data(can=can, data=cbor, pos=pos)
            return can
        else:
            return Response(f"Unable to add {camp_name} because is a invalid cbor", status=400)
    except:
        return Response(f'Unknow error while adding {camp_name}', status=500)


def add_sex_square(can:canvas.Canvas, sex:str, pos_male:tuple, pos_fem:tuple, camp_name:str, square_size:tuple=(9,9), nullable:bool=False) -> Union[canvas.Canvas, Response]:
    """Add sex square to canvas

    Args:
        can (canvas.Canvas): canvas to use
        sex (str): sex select
        pos_male (tuple): male option position
        pos_fem (tuple): female option position
        square_size (tuple): square size. Defaults to (9,9).
        camp_name (str): camp name
        nullable (bool, optional): can be null. Defaults to False.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if sex == None or len(str(sex).strip()) == 0:
                return can
        if type(sex) != type(str()):
            return Response(f'{camp_name} has to be str', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos_male) != type(tuple()):
            return Response(f'pos_male has to be tuple', status=500)
        elif type(pos_fem) != type(tuple()):
            return Response(f'pos_fem has to be tuple', status=500)
        elif type(square_size) != type(tuple()):
            return Response(f'square_size has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)

        sex = sex.upper()
        if len(sex) != 1:
            return Response(f'{camp_name} has to be only one character F or M', status=400)
        if sex not in ['M', 'F']:
            return Response(f'{camp_name} is not valid, use F or M', status=400)
        else:
            if sex == 'M':
                can = add_square(can=can, pos=pos_male, size=square_size)
                return can
            else:
                can = add_square(can=can, pos=pos_fem, size=square_size)
                return can
    except:
        return Response(f'Unkown error while adding {camp_name}', status=500)


def add_datetime(can:canvas.Canvas, date:datetime.datetime, pos:tuple, camp_name:str, hours:bool=True, nullable:bool=False, formated:bool=True, interval:str='', interval_between_numbers:str='') -> Union[canvas.Canvas, Response]:
    """Add datetime to canvas

    Args:
        can (canvas.Canvas): canvas to use
        date (datetime.datetime): date to use
        pos (tuple): position
        camp_name (str): camp name
        hours (bool): add hours. Defaults to True
        nullable (bool, optional): can be null. Defaults to False.
        formated (bool, optional): format (add '/' and ':'). Defaults to True.
        interval (str, optional): add interval between  day, month, year, hour, min, sec. Defaults to ''.
        interval_between_numbers (str, optional): add interval between  every number. Defaults to ''.
    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if date == None:
                return can
        if type(date) != type(datetime.datetime.now()):
            return Response(f'{camp_name} has to be datetime object', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos) != type(tuple()):
            return Response(f'pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(hours) != type(bool()):
            return Response(f'hours has to be bool', status=500)
        elif type(formated) != type(bool()):
            return Response(f'formated has to be bool', status=500)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)
        elif type(interval_between_numbers) != type(str()):
            return Response(f'interval_between_numbers has to be str', status=500)

        #Add to respective fields
        str_date = str('%02d/%02d/%d %02d:%02d:%02d') % (date.day, date.month, date.year, date.hour, date.minute, date.second)
        if hours:  
            if not formated:
                str_date = add_interval_to_data(data=str_date, interval=interval_between_numbers)
                str_date = str_date.replace('/', interval)
                str_date = str_date.replace(':', interval)
        else:
            str_date = str_date[0:10]
            if not formated:
                str_date = str_date.replace('/', interval)
            str_date = add_interval_to_data(data=str_date, interval=interval_between_numbers)
        can = add_data(can=can, data=str_date, pos=pos)
        return can

    except:
        return Response(f'Unkown error while adding {camp_name}', status=500)


def add_UF(can:canvas.Canvas, uf:str, pos:tuple, camp_name:str, nullable:bool=False, interval:str='') -> Union[canvas.Canvas, Response]:
    """Verify uf and add to document

    Args:
        can (canvas.Canvas): canvas to use
        uf (str): uf to add
        pos (tuple): position uf
        camp_name (str): camp name
        nullable (bool, optional): can be null. Defaults to False.
        interval (str, optional): and interval between char. Defaults to ''.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if uf == None or str(uf).strip() == '':
                return can
        if type(uf) != type(str()):
            return Response(f'{camp_name} has to be string, if can be null, please add nullable option', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(pos) != type(tuple()):
            return Response(f'pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)
        
        uf = uf.strip()
        if uf_exists(uf=uf):
            # Add empty spaces interval between averu character
            uf = add_interval_to_data(data=uf, interval=interval)
            can = add_data(can=can, data=uf, pos=pos)
            return can
        else:
            return Response(f'{camp_name} not exists in Brazil', status=400) 
    except:
        return Response(f'Unknow error while adding {camp_name}', status=500)


def add_document_cns_cpf_rg(can:canvas.Canvas, document:dict, camp_name:str, square_size:tuple=(9,9), pos_cpf:tuple=None, pos_cns:tuple=None, pos_rg:tuple=None, pos_square_cpf:tuple=None, pos_square_cns:tuple=None, pos_square_rg:tuple=None, nullable:bool=False, interval:str='', formated:bool=False) -> Union[canvas.Canvas, Response]:
    """Validate and add document to canvas, can be CPF, RG or CNS

    Args:
        can (canvas.Canvas): canvas to use
        document (dict): dict with the document
        camp_name (str): camp name 
        square_size (tuple, optional): suqare size if has mark option. Defaults to (9,9).
        pos_cpf (tuple, optional): cpf number position in canvas. Defaults to None.
        pos_cns (tuple, optional): cns number position in canvas. Defaults to None.
        pos_rg (tuple, optional): rg number position in canvas. Defaults to None.
        pos_square_cpf (tuple, optional): cpf square position in canvas. Defaults to None.
        pos_square_cns (tuple, optional): cns square position in canvas. Defaults to None.
        pos_square_rg (tuple, optional): rg number position in canvas. Defaults to None.
        nullable (bool, optional): can be null. Defaults to False.
        interval (str, optional): intervale between every number. Defaults to ''.
        formated (bool, optional): has to format, format using the default for every doc (rg is exception). Defaults to False.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if document == None:
                return can
        if type(document) != type(dict()):
            return Response(f'{camp_name} document has to be a dict ("document":"number")', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(square_size) != type(tuple()):
            return Response(f'square_size has to be tuple', status=500)
        elif type(pos_cpf) != type(tuple()) and pos_cpf != None:
            return Response(f'pos_cpf has to be tuple', status=500)
        elif type(pos_cns) != type(tuple()) and pos_cns != None:
            return Response(f'pos_cns has to be tuple', status=500)
        elif type(pos_rg) != type(tuple()) and pos_rg != None:
            return Response(f'pos_rg has to be tuple', status=500)
        elif type(pos_square_cpf) != type(tuple()) and pos_square_cpf != None:
            return Response(f'pos_square_cpf has to be tuple', status=500)
        elif type(pos_square_cns) != type(tuple()) and pos_square_cns != None:
            return Response(f'pos_square_cns has to be tuple', status=500)
        elif type(pos_square_rg) != type(tuple()) and pos_square_rg != None:
            return Response(f'pos_square_rg has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)
        elif type(formated) != type(bool()):
            return Response(f'formated has to be bool', status=500)
        
        # See id document is CPF, CNS or RG
        all_document_keys = document.keys()
        if 'CNS' in all_document_keys:
            if type(document['CNS']) != type(int()):
                return Response(f'{camp_name} value CNS has to be int', status=400)
            if is_CNS_valid(document['CNS']):
                if pos_square_cns != None:
                    can = add_square(can=can, pos=pos_square_cns, size=square_size)
                # Add empty spaces interval between every character

                cns = str(document['CNS'])
                cns = add_interval_to_data(data=cns, interval=interval)
                if formated:
                    cns = cns[:3] + " " + cns[3:7] + " " + cns[7:11] + " " + cns[11:15]
                can = add_data(can=can, data=cns, pos=pos_cns)
                return can
            else:
                return Response(f'{camp_name} CNS is not valid', status=400)
        elif 'CPF' in all_document_keys:
            if type(document['CPF']) != type(int()):
                return Response(f'{camp_name} value CPF has to be int', status=400)
            #Format cpf to validate
            cpf = str(document['CPF'])
            numbers_cpf = str(cpf)
            formated_cpf = cpf[:3] + "." + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
            if is_CPF_valid(formated_cpf):
                if pos_square_cpf != None:
                    can = add_square(can=can, pos=pos_square_cpf, size=square_size)
                # Add empty spaces interval between averu character
                if formated:
                    cpf = add_interval_to_data(data=formated_cpf, interval=interval)
                else:
                    cpf = add_interval_to_data(data=numbers_cpf, interval=interval)

                can = add_data(can=can, data=cpf, pos=pos_cpf)
                return can
            else:
                return Response(f'{camp_name} CPF is not valid', status=400)
        elif 'RG' in all_document_keys:
            rg = document['RG']
            if type(rg) != type(int()):
                return Response(f'{camp_name} value RG has to be int', status=400)
            #The only verificatinon is that rg is not greater than 16 characteres
            if is_RG_valid(rg):
                rg = str(document['RG'])
                if pos_square_rg != None:
                    can = add_square(can=can, pos=pos_square_rg, size=square_size)
                can = add_data(can=can, data=rg, pos=pos_rg)
                return can
            else:
                return Response(f'{camp_name} RG is not valid', status=400)
        else:
            return Response('The document was not CPF, CNS or RG', status=400)
    except:
        return Response(f'Unknow error while adding {camp_name} Document', status=500)


def add_markable_square(can:canvas.Canvas, option:str, valid_options:list, options_positions:tuple, camp_name:str, square_size:tuple=(9,9), nullable:bool=False) -> Union[canvas.Canvas, Response]:
    """Verifiy option choose and add to canvas, the option is automatic upper cased

    Args:
        can (canvas.Canvas): canvas to use
        option (str): option select, will be upperCased
        valid_options (list): list of valid options, recommendend UPPER (str)
        options_positions (tuple): tuple of tuples with positions to every option
        square_size (tuple): square size. Defaults to (9,9).
        camp_name (str): camp name
        nullable (bool, optional): can be null. Defaults to False.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if option == None or len(str(option).strip()) == 0:
                return can
        if type(option) != type(str()):
            return Response(f'{camp_name} has to be str', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(valid_options) != type(list()):
            return Response(f'valid_options has to be list', status=500)
        elif type(options_positions) != type(tuple()):
            return Response(f'options_positions has to be tuple', status=500)
        elif type(square_size) != type(tuple()):
            return Response(f'square_size has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif len(valid_options) != len(options_positions):
            return Response(f'valid_options and options_positions has to be the same size', status=500)


        option = option.upper()
        for opt in range(0, len(valid_options)):
            if option == valid_options[opt]:
                can = add_square(can=can, pos=options_positions[opt], size=square_size)
                return can
        return Response(f'Cannot add {camp_name} because the option choosed does not exists', status=400)
    except:
        return Response(f'Unkown error while adding {camp_name}', status=500)


def add_multiple_markable_square(can:canvas.Canvas, options:list, valid_options:list, options_positions:tuple, camp_name:str, square_size:tuple=(9,9), nullable:bool=False) -> Union[canvas.Canvas, Response]:
    """Verifiy option choose and add to canvas, the option is automatic upper cased

    Args:
        can (canvas.Canvas): canvas to use
        options (list): list of option selects, will be upperCased
        valid_options (list): list of valid options, recommendend UPPER (str)
        options_positions (tuple): tuple of tuples with positions to every option
        square_size (tuple): square size. Defaults to (9,9).
        camp_name (str): camp name
        nullable (bool, optional): can be null. Defaults to False.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if option == None or len(str(option).strip()) == 0:
                return can
        if type(option) != type(list()):
            return Response(f'{camp_name} has to be list', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(valid_options) != type(list()):
            return Response(f'valid_options has to be list', status=500)
        elif type(options_positions) != type(tuple()):
            return Response(f'options_positions has to be tuple', status=500)
        elif type(square_size) != type(tuple()):
            return Response(f'square_size has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif len(valid_options) != len(options_positions):
            return Response(f'valid_options and options_positions has to be the same size', status=500)


        option = option.upper()
        exist = False
        for opt in range(0, len(valid_options)):
            if option == valid_options[opt]:
                can = add_square(can=can, pos=options_positions[opt], size=square_size)
                exist = True
        if exist:
            return can
        return Response(f'Cannot add {camp_name} because the option choosed does not exists', status=400)
    except:
        return Response(f'Unkown error while adding {camp_name}', status=500)


def add_markable_square_and_onelinetext(can:canvas.Canvas, option:str, valid_options:list, text_options:list, text_pos:tuple, options_positions:tuple, camp_name:str, len_max:int, text:str=None, len_min:int=0, interval:str='', square_size:tuple=(9,9), nullable:bool=False) -> Union[canvas.Canvas, Response]:
    """Verifiy option choose and add to canvas, the option is automatic upper cased

    Args:
        can (canvas.Canvas): canvas to use
        option (str): option select, will be upperCased
        valid_options (list): list of valid options, recommendend UPPER (str)
        options_positions (tuple): tuple of tuples with positions to every option
        square_size (tuple): square size. Defaults to (9,9).
        camp_name (str): camp name
        nullable (bool, optional): can be null. Defaults to False.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if option == None or len(str(option).strip()) == 0:
                return can
        if type(option) != type(str()):
            return Response(f'{camp_name} has to be str', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(text_options) != type(list()):
            return Response(f'text_options has to be list', status=500)
        elif type(valid_options) != type(list()):
            return Response(f'valid_options has to be list', status=500)
        elif type(options_positions) != type(tuple()):
            return Response(f'options_positions has to be tuple', status=500)
        elif type(square_size) != type(tuple()):
            return Response(f'square_size has to be tuple', status=500)
        elif type(text_pos) != type(tuple()):
            return Response(f'text_pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(text) != type(str()) and text != None:
            return Response(f'text has to be str or None', status=400)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(len_max) != type(int()):
            return Response(f'len_max has to be int', status=500)
        elif type(len_min) != type(int()):
            return Response(f'len_min has to be int', status=500)
        elif len(valid_options) != len(options_positions):
            return Response(f'valid_options and options_positions has to be the same size', status=500)

        #Verify if option exist
        option = option.upper()
        for opt in range(0, len(valid_options)):
            if option == valid_options[opt]:
                #Verify if option requer a text
                if option in text_options:
                    if text == None or str(text).strip() == '':
                        return Response(f'Cannot add {camp_name} because a text is required for {option} option', status=400)
                    else:
                        #Add text line
                        can = add_oneline_text(can=can, text=text, pos=text_pos, camp_name=camp_name, len_max=len_max, len_min=len_min, interval=interval)
                if type(can) == type(Response()): return can
                can = add_square(can=can, pos=options_positions[opt], size=square_size)
                return can
        return Response(f'Cannot add {camp_name} because the option choosed does not exists in {valid_options}', status=400)
    except:
        return Response(f'Unkown error while adding {camp_name}', status=500)


def add_markable_square_and_morelinestext(can:canvas.Canvas, option:str, valid_options:list, text_options:list, text_pos:tuple, options_positions:tuple, camp_name:str, len_max:int, decrease_ypos:int, char_per_lines:int, max_lines_amount:int=None, text:str=None, len_min:int=0, interval:str='', square_size:tuple=(9,9), nullable:bool=False) -> Union[canvas.Canvas, Response]:
    """Verifiy option choose and add to canvas, the option is automatic upper cased

    Args:
        can (canvas.Canvas): canvas to use
        option (str): option select, will be upperCased
        valid_options (list): list of valid options, recommendend UPPER (str)
        options_positions (tuple): tuple of tuples with positions to every option
        square_size (tuple): square size. Defaults to (9,9).
        camp_name (str): camp name
        nullable (bool, optional): can be null. Defaults to False.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        or
        Response(flask.Response): with the error
    """    
    try:
        if nullable:
            if option == None or len(str(option).strip()) == 0:
                return can
        if type(option) != type(str()):
            return Response(f'{camp_name} has to be str', status=400)
        elif type(can) != type(canvas.Canvas(filename=None)):
            return Response(f'can has to be canvas.Canvas object', status=500)
        elif type(text_options) != type(list()):
            return Response(f'text_options has to be list', status=500)
        elif type(valid_options) != type(list()):
            return Response(f'valid_options has to be list', status=500)
        elif type(options_positions) != type(tuple()):
            return Response(f'options_positions has to be tuple', status=500)
        elif type(square_size) != type(tuple()):
            return Response(f'square_size has to be tuple', status=500)
        elif type(text_pos) != type(tuple()):
            return Response(f'text_pos has to be tuple', status=500)
        elif type(camp_name) != type(str()):
            return Response(f'camp_name has to be str', status=500)
        elif type(text) != type(str()) and text != None:
            return Response(f'text has to be str', status=400)
        elif type(interval) != type(str()):
            return Response(f'interval has to be str', status=500)
        elif type(nullable) != type(bool()):
            return Response(f'nullable has to be bool', status=500)
        elif type(len_max) != type(int()):
            return Response(f'len_max has to be int', status=500)
        elif type(len_min) != type(int()):
            return Response(f'len_min has to be int', status=500)
        elif len(valid_options) != len(options_positions):
            return Response(f'valid_options and options_positions has to be the same size', status=500)

        #Verify if option exist
        option = option.upper()
        for opt in range(0, len(valid_options)):
            if option == valid_options[opt]:
                #Verify if option requer a text
                if option in text_options:
                    if text == None or str(text).strip() == '':
                        return Response(f'Cannot add {camp_name} because a text is required for {option} option', status=400)
                    else:
                        #Add text line
                        can = add_morelines_text(can=can, text=text, initial_pos=text_pos, camp_name=camp_name, len_max=len_max, len_min=len_min, decrease_ypos=decrease_ypos, interval=interval, char_per_lines=char_per_lines, max_lines_amount=max_lines_amount)
                if type(can) == type(Response()): return can
                can = add_square(can=can, pos=options_positions[opt], size=square_size)
                return can
        return Response(f'Cannot add {camp_name} because the option choosed does not exists in {valid_options}', status=400)
    except:
        return Response(f'Unkown error while adding {camp_name}', status=500)





if __name__ == "__main__":
    cpf = 142342343234
    print(is_CPF_valid(cpf))
    