import re
from reportlab.pdfgen import canvas
from PyPDF2  import PdfWriter
import datetime
from inspect import getfullargspec
from validate_docbr import CNS, CPF, CNPJ


def validate_func_args(function_to_verify, variables_to_verify:dict, nullable_variables:list=[]) -> None:
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
                raise Exception(f'{variables_keys} estao com o tipo errado, deve ser {right_type}')
        return None
    except Exception as error:
        raise error
    except KeyError:
        raise Exception(f'KeyError, Alguma chave em {function_to_verify} esta faltando, enquanto validava os tipos, a chaves necessarias sao {args_types.keys()}')
    except:
        raise Exception(f'{arg_to_validate} tipo {right_type} erro desconhecido enquanto validava os argumentos {variables_keys} na funcao {function_to_verify}')


def is_RG_valid(rg:str) -> bool:
    # Notice that RG changes a lot in every brazillian state
    # so theres a chance that a invalid RG has pass as Valid
    # just because RG is matematician valid dont mean that exists in government database
    #the only verification that can do is the maximum value
    validate_func_args(function_to_verify=is_RG_valid, variables_to_verify={'rg':rg})

    if 5 < len(str(rg)) < 17:
        return True
    return False


def uf_exists(uf:str) -> bool:
    """Verify if a uf exists in Brazil

    Args:
        uf (str): uf to verify 

    Returns:
        Bollean true or false
        Reponse if the receive worng type
    """    
    validate_func_args(function_to_verify=uf_exists, variables_to_verify={'uf':uf})

    return bool(re.match(r'^(\s*(AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RJ|RN|RS|RO|RR|SC|SP|SE|TO)?)$', uf, flags=re.I))


def add_data(can:canvas.Canvas, data:str, pos:tuple) -> canvas.Canvas:
    """Add data in pdf using canvas object

    Args:
        can (canvas.Canvas): canvas that will be used to add data
        data (str): data to be added
        pos (tuple): data insert position in points

    Returns:
        can(canvas.Canvas): canvas with all changes
        
    """
    try:
        can.drawString(pos[0], pos[1], data)
        return can
    except:
        raise Exception("Erro desconhecido enquanto adicionava um dado no documento com o canvas")


def add_square(can:canvas.Canvas, pos:tuple, size:tuple=(9, 9)) -> canvas.Canvas:
    """Add square in document using canvas object

    Args:
        can (canvas.Canvas): canvas to use
        pos (tuple): position to add the square
        size (tuple, optional): square size default is the size of the option quare. Defaults to 9.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        
    """
    try:
        can.rect(x=pos[0], y=pos[1], width=size[0], height=size[1], fill=1)
        return can
    except:
        raise Exception("Erro desconhecido enquanto adicionava um quadrado (opcoes de marcar) no documento com o canvas")


def add_centralized_data(can:canvas.Canvas, data:str, pos:tuple) -> canvas.Canvas:
    """Add centralized_data in pdf using canvas object

    Args:
        can (canvas.Canvas): canvas that will be used to add centralized_data
        data (str): centralized_data to be added
        pos (tuple): centralized_data insert position in points

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        
    """
    try:
        can.drawCentredString(pos[0], pos[1], data)
        return can
    except:
        raise Exception("Erro desconhecido enquanto adicionava um dado centralizado no documento com o canvas")

        
def write_newpdf(newpdf:PdfWriter, new_directory:str) -> None:
    """Write new pdf in a file

    Args:
        newpdf (PdfFileWriter): new pdf with all the changes made by canvas
        new_directory (str): directory to save the new pdf
    Returns:
        None
        
    """ 
    try:
        output_file = open(new_directory, 'wb')
        newpdf.write(output_file)
        output_file.close()
    except:
        raise Exception("Erro desconhecido enquanto criava um novo arquivo pdf")


def add_oneline_text(can:canvas.Canvas, text:str, pos:tuple, camp_name:str, len_max:int, nullable:bool=False, len_min:int=0, interval:str='', centralized:bool=False) -> canvas.Canvas:
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
        
    """
    try:
        if nullable:
            if text == None or len(str(text).strip()) == 0:
                return can

        validate_func_args(function_to_verify=add_oneline_text, variables_to_verify={'can':can, 'text':text, 'pos':pos, 'camp_name':camp_name, 'len_max':len_max, 'nullable':nullable, 'len_min':len_min, 'interval':interval, 'centralized':centralized})

        if not nullable:
            text = text.strip()
            if len(text) == 0:
                raise Exception(f"{camp_name} cannot be empty")
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
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque e maior que {len_max} characteres ou menor que {len_min} caracteres")
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')




def add_morelines_text(can:canvas.Canvas, text:str, initial_pos:tuple, decrease_ypos:int, camp_name:str, len_max:int, char_per_lines:int, max_lines_amount:int=None, nullable:bool=False, len_min:int=0, interval:str='') -> canvas.Canvas:
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
        _summary_
    """    
    try:
        if nullable:
            if text == None or len(str(text).strip()) == 0:
                return can
        validate_func_args(function_to_verify=add_morelines_text, variables_to_verify={'can':can, 'text':text, 'initial_pos':initial_pos, 'decrease_ypos':decrease_ypos, 'camp_name':camp_name, 'len_max':len_max, 'char_per_lines':char_per_lines, 'max_lines_amount':max_lines_amount, 'nullable':nullable, 'len_min':len_min, 'interval':interval}, nullable_variables=['max_lines_amount'])


        if not nullable:
            text = text.strip()
            if len(text) == 0:
                raise Exception(f'{camp_name} nao pode ser vazio')
        # verify if text is in the need lenght
        text = text.strip()
        if len_min <= len(text) <= len_max:
            text = add_interval_to_data(data=text, interval=interval)
            str_to_line = ''
            broke_lines_times = int(len(text)/char_per_lines)
            if max_lines_amount != None and broke_lines_times + 1 > max_lines_amount:
                raise Exception(f'Nao foi possivel adicionar {camp_name} pois a quantidade de linhas necessrias e maior que {max_lines_amount}')
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
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque e maior que {len_max} characteres ou menor que {len_min} caracteres")

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_phonenumber(can:canvas.Canvas, number:str, pos:tuple, camp_name:str, nullable:bool=False, interval:str='', formated:bool=False) -> canvas.Canvas:
    """_summary_

    Args:
        can (canvas.Canvas):  canvas to use
        number (str): number to add
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

        validate_func_args(function_to_verify=add_phonenumber, variables_to_verify={'can':can, 'number':number, 'pos':pos, 'camp_name':camp_name, 'nullable':nullable, 'interval':interval, 'formated':formated})
        
        number = str(number).strip()
        if 10 <= len(number) <= 11:
            if formated:
                number = '(' + number[:2] + ') ' + number[2:7] + '-' + number[7:]

            number = add_interval_to_data(data=number, interval=interval)
            can = add_data(can=can, data=number, pos=pos)
            return can
        else:
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque e maior que {10} caracteres ou menor que {11} caracteres")
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_CEP(can:canvas.Canvas, cep:str, pos:tuple, camp_name:str, nullable:bool=False, interval:str='', formated:bool=False) -> canvas.Canvas:
    """Add cep to canvas

    Args:
        can (canvas.Canvas):  canvas to use
        cep (str): cep to add
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

        validate_func_args(function_to_verify=add_CEP, variables_to_verify={'can':can, 'cep':cep, 'pos':pos, 'camp_name':camp_name, 'nullable':nullable, 'interval':interval, 'formated':formated})

        cep = str(cep).strip()
        if len(cep) == 8:
            if formated:
                cep = cep[:5] + '-' + cep[5:]

            cep = add_interval_to_data(data=cep, interval=interval)
            can = add_data(can=can, data=cep, pos=pos)
            return can
        else:
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque o cpf nao possui 8 digitos")

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_oneline_intnumber(can:canvas.Canvas, number:int, pos:tuple, camp_name:str, len_max:int, value_min:int, value_max:int, nullable:bool=False, len_min:int=0, interval:str='', centralized:bool=False) -> canvas.Canvas:
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
        
    """    
    try:
        if nullable:
            if number == None:
                return can

        verify = validate_func_args(function_to_verify=add_oneline_intnumber, variables_to_verify={'can':can, 'number':number, 'pos':pos, 'camp_name':camp_name, 'len_max':len_max, 'value_min':value_min, 'value_max':value_max, 'nullable':nullable, 'len_min':len_min, 'interval':interval, 'centralized':centralized})

        # verify if number is in the need lenght
        if value_min > number or value_max < number:
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque e maior que {value_max} ou menor que {value_min}")
        number = str(number)
        if len_min <= len(number) <= len_max:
            number = add_interval_to_data(data=number, interval=interval)
            if centralized:
                can = add_centralized_data(can=can, data=number, pos=pos)
            else:
                can = add_data(can=can, data=number, pos=pos)
            return can
        else:
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque e maior que {len_max} characteres ou menor que {len_min} caracteres")

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_oneline_floatnumber(can:canvas.Canvas, number:float, pos:tuple, camp_name:str, len_max:int, value_min:float, value_max:float, nullable:bool=False, len_min:int=0, interval:str='', centralized:bool=False, ndigits:int=2) -> canvas.Canvas:
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
        
    """    
    try:
        if nullable:
            if number == None:
                return can

        validate_func_args(function_to_verify=add_oneline_floatnumber, variables_to_verify={'can':can, 'number':number, 'pos':pos, 'camp_name':camp_name, 'len_max':len_max, 'value_min':value_min, 'value_max':value_max, 'nullable':nullable, 'len_min':len_min, 'interval':interval, 'centralized':centralized, 'ndigits':ndigits})
        

        # verify if number is in the need lenght
        if value_min > number or value_max < number:
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque e maior que {value_max} e menor que {value_min}")
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
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque e maior que {len_max} characteres ou menor que {len_min} caracteres")
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')



def add_interval_to_data(data:str, interval:str) -> str:
    """add interval to data

    Args:
        data (str): data
        interval (str): interval to add betwaeen every char

    Returns:
        interval(str): data with the intervals add
        
    """    
    if type(data) != type(str()):
        return Exception('O sistema deve enviar o dado para a funcao add_interval sendo do tipo string, contate o administrador do sistema')
    elif type(interval) != type(str()):
        return Exception('O sistema deve enviar o intervalo a ser adicionado no dado para a funcao add_interval sendo do tipo string, contate o administrador do sistema')
    # Add nterval between data
    return interval.join(data)


def add_cns(can:canvas.Canvas, cns:str, pos:tuple, camp_name:str,nullable:bool=False, formated:bool=False, interval:str='') -> canvas.Canvas:
    """Add cns to canvas

    Args:
        can (canvas.Canvas): canvas to add
        cns (str): cns to add
        pos (tuple): position in canvas
        camp_name (str): camp nam
        nullable (bool, optional): can be null. Defaults to False.
        formated (bool, optional): format cns to xxx xxxx xxxx xxxx. Defaults to False.
        interval (str, optional): interval to add between interval. Defaults to ''.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        
    """    
    try:
        if nullable:
            if cns == None:
                return can

        cns_validator = CNS()

        validate_func_args(function_to_verify=add_cns, variables_to_verify={'can':can, 'cns':cns, 'pos':pos, 'camp_name':camp_name,'nullable':nullable, 'formated':formated, 'interval':interval})
        

        # Verify if the cns is valid
        if cns_validator.validate(cns):
            cns = str(cns)
            # Add interval selected
            cns = add_interval_to_data(data=cns, interval=interval)
            if formated: 
                cns = cns[:3] + " " + cns[3:7] + " " + cns[7:11] + " " + cns[11:15]
            can = add_data(can=can, data=cns, pos=pos)
            return can
        else:
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque e um CNS invalido")
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_cnpj(can:canvas.Canvas, cnpj:str, pos:tuple, camp_name:str,nullable:bool=False, interval:str='') -> canvas.Canvas:
    """Add cnpj to canvas

    Args:
        can (canvas.Canvas): canvas to add
        cnpj (str): cnpj to add
        pos (tuple): position in canvas
        camp_name (str): camp nam
        nullable (bool, optional): can be null. Defaults to False.
        interval (str, optional): interval to add between interval. Defaults to ''.

    Returns:
        canvas(canvas.Canvas): canvas with all changes
        
    """    
    try:
        if nullable:
            if cnpj == None:
                return can

        validate_func_args(function_to_verify=add_cnpj, variables_to_verify={'can':can, 'cnpj':cnpj, 'pos':pos, 'camp_name':camp_name,'nullable':nullable, 'interval':interval})


        cnpj_validator = CNPJ()
        # Verify if the cnpj is valid
        cnpj = cnpj.strip()
        if cnpj_validator.validate(cnpj):
            # Add interval selected
            cnpj = add_interval_to_data(data=cnpj, interval=interval)
            can = add_data(can=can, data=cnpj, pos=pos)
            return can
        else:
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque e um CNPJ invalido")

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_cnae(can:canvas.Canvas, cnae:int, pos:tuple, camp_name:str, nullable:bool=False, formated:bool=False) -> canvas.Canvas:
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
        
    """    
    try:
        if nullable:
            if cnae == None:
                return can

        validate_func_args(function_to_verify=add_cnae, variables_to_verify={'can':can, 'cnae':cnae, 'pos':pos, 'camp_name':camp_name,'nullable':nullable, 'formated':formated})


        cnae = str(cnae)
        if len(cnae) == 7:
            #Format cnae to add in doc
            if formated:
                cnae = cnae[:2] + '.' + cnae[2:4] + '-' + cnae[4] + '-' + cnae[5:]
            can = add_data(can=can, data=cnae, pos=pos)
            return can
        else:
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque e um CNAE invalido")

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_cbor(can:canvas.Canvas, cbor:int, pos:tuple, camp_name:str, nullable:bool=False, formated:bool=False) -> canvas.Canvas:
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
        
    """    
    try:
        if nullable:
            if cbor == None:
                return can

        validate_func_args(function_to_verify=add_cbor, variables_to_verify={'can':can, 'cbor':cbor, 'pos':pos, 'camp_name':camp_name,'nullable':nullable, 'formated':formated})


        cbor = str(cbor)
        if len(cbor) == 6:
            #Format cbor to add in doc
            if formated:
                cbor = cbor[:5] + '-' + cbor[5:]
            can = add_data(can=can, data=cbor, pos=pos)
            return can
        else:
            raise Exception(f"Nao foi possivel adicionar {camp_name} porque e um CBOR invalido")
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_sex_square(can:canvas.Canvas, sex:str, pos_male:tuple, pos_fem:tuple, camp_name:str, square_size:tuple=(9,9), nullable:bool=False) -> canvas.Canvas:
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
        
    """    
    try:
        if nullable:
            if sex == None or len(str(sex).strip()) == 0:
                return can

        validate_func_args(function_to_verify=add_sex_square, variables_to_verify={'can':can, 'sex':sex, 'pos_male':pos_male, 'pos_fem':pos_fem, 'camp_name':camp_name, 'square_size':square_size, 'nullable':nullable})

        sex = sex.upper()
        if len(sex) != 1:
            raise Exception(f'{camp_name} deve ter somente 1 caractere, F ou M')
        if sex not in ['M', 'F']:
            raise Exception(f'{camp_name} deve ter somente 1 caractere, F ou M')
        else:
            if sex == 'M':
                can = add_square(can=can, pos=pos_male, size=square_size)
                return can
            else:
                can = add_square(can=can, pos=pos_fem, size=square_size)
                return can
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_datetime(can:canvas.Canvas, date:str, pos:tuple, camp_name:str, hours:bool=True, nullable:bool=False, formated:bool=True, interval:str='', interval_between_numbers:str='') -> canvas.Canvas:
    """Add datetime to canvas

    Args:
        can (canvas.Canvas): canvas to use
        date (str): date to use
        pos (tuple): position
        camp_name (str): camp name
        hours (bool): add hours. Defaults to True
        nullable (bool, optional): can be null. Defaults to False.
        formated (bool, optional): format (add '/' and ':'). Defaults to True.
        interval (str, optional): add interval between  day, month, year, hour, min, sec. Defaults to ''.
        interval_between_numbers (str, optional): add interval between  every number. Defaults to ''.
    Returns:
        canvas(canvas.Canvas): canvas with all changes
        
    """    
    try:
        if nullable:
            if date == None:
                return can
        
        validate_func_args(function_to_verify=add_datetime, variables_to_verify={'can':can, 'date':date, 'pos':pos, 'camp_name':camp_name, 'hours':hours, 'nullable':nullable, 'formated':formated, 'interval':interval, 'interval_between_numbers':interval_between_numbers})


        #Add to respective fields
        try:
            #Create a datetimeobject just to makesure the date is valid
            if hours:
                date_object = datetime.datetime.strptime(date, '%d/%m/%Y %H:%M')
            else:
                date_object = datetime.datetime.strptime(date, '%d/%m/%Y')
        except:
            if hours:
                raise Exception(f'Date doenst match dd/mm/yyyy HH:MM format')
            raise Exception(f'Date doenst match dd/mm/yyyy format')
        str_date = str('%02d/%02d/%d %02d:%02d:%02d') % (date_object.day, date_object.month, date_object.year, date_object.hour, date_object.minute, date_object.second)
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

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_UF(can:canvas.Canvas, uf:str, pos:tuple, camp_name:str, nullable:bool=False, interval:str='') -> canvas.Canvas:
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
        
    """    
    try:
        if nullable:
            if uf == None or str(uf).strip() == '':
                return can

        validate_func_args(function_to_verify=add_UF, variables_to_verify={'can':can, 'uf':uf, 'pos':pos, 'camp_name':camp_name, 'nullable':nullable, 'interval':interval})

        
        uf = uf.strip()
        if uf_exists(uf=uf):
            # Add empty spaces interval between averu character
            uf = add_interval_to_data(data=uf, interval=interval)
            can = add_data(can=can, data=uf, pos=pos)
            return can
        else:
            raise Exception(f'{camp_name} not exists in Brazil') 
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_document_cns_cpf_rg(can:canvas.Canvas, document:dict, camp_name:str, square_size:tuple=(9,9), pos_cpf:tuple=None, pos_cns:tuple=None, pos_rg:tuple=None, pos_square_cpf:tuple=None, pos_square_cns:tuple=None, pos_square_rg:tuple=None, nullable:bool=False, interval:str='', formated:bool=False) -> canvas.Canvas:
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
        
    """    
    try:
        if nullable:
            if document == None:
                return can

        
        validate_func_args(function_to_verify=add_document_cns_cpf_rg, variables_to_verify={'can':can, 'document':document, 'camp_name':camp_name, 'square_size':square_size, 'pos_cpf':pos_cpf, 'pos_cns':pos_cns, 'pos_rg':pos_rg, 'pos_square_cpf':pos_square_cpf, 'pos_square_cns':pos_square_cns, 'pos_square_rg':pos_square_rg, 'nullable':nullable, 'interval':interval, 'formated':formated}, nullable_variables=['pos_cpf', 'pos_cns', 'pos_rg', 'pos_square_cpf', 'pos_square_cns', 'pos_square_rg'])

        
        # See id document is CPF, CNS or RG
        all_document_keys = list(document.keys())
        #Make all keys bein lower
        for key in all_document_keys:
            document[f'{str(key).lower()}'] = document.pop(key)
            
        # updating all document keys
        all_document_keys = document.keys()
        if 'cns' in all_document_keys:
            if document['cns'] != None:
                if type(document['cns']) != type(str()):
                    raise Exception(f'{camp_name} value CNS has to be str')
                
                cns_validator = CNS()
                if cns_validator.validate(document['cns']):
                    if pos_square_cns != None:
                        can = add_square(can=can, pos=pos_square_cns, size=square_size)
                    # Add empty spaces interval between every character

                    cns = str(document['cns'])
                    cns = add_interval_to_data(data=cns, interval=interval)
                    if formated:
                        cns = cns[:3] + " " + cns[3:7] + " " + cns[7:11] + " " + cns[11:15]
                    can = add_data(can=can, data=cns, pos=pos_cns)
                    return can
                else:
                    raise Exception(f'{camp_name} CNS is not valid')
        
        if 'cpf' in all_document_keys:
            if document['cpf'] != None:
                if type(document['cpf']) != type(str()):
                    raise Exception(f'{camp_name} value CPF has to be str')
                #Format cpf to validate
                cpf_validator = CPF()
                cpf = document['cpf']
                if cpf_validator.validate(cpf):
                    if pos_square_cpf != None:
                        can = add_square(can=can, pos=pos_square_cpf, size=square_size)
                    # Add empty spaces interval between averu character
                    if formated:
                        formated_cpf = cpf[:3] + "." + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
                        cpf = add_interval_to_data(data=formated_cpf, interval=interval)
                    else:
                        cpf = add_interval_to_data(data=cpf, interval=interval)

                    can = add_data(can=can, data=cpf, pos=pos_cpf)
                    return can
                else:
                    raise Exception(f'{camp_name} CPF is not valid')
        
        if 'rg' in all_document_keys:
            if document['rg'] != None:
                rg = document['rg']
                if type(rg) != type(str()):
                    raise Exception(f'{camp_name} value RG has to be str')
                #The only verificatinon is that rg is not greater than 16 characteres
                if is_RG_valid(rg):
                    rg = str(document['rg'])
                    if pos_square_rg != None:
                        can = add_square(can=can, pos=pos_square_rg, size=square_size)
                    can = add_data(can=can, data=rg, pos=pos_rg)
                    return can
                else:
                    raise Exception(f'{camp_name} RG is not valid')
        
        raise Exception(f'{camp_name} was not CPF, CNS or RG')
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_markable_square(can:canvas.Canvas, option:str, valid_options:list, options_positions:tuple, camp_name:str, square_size:tuple=(9,9), nullable:bool=False) -> canvas.Canvas:
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
        
    """    
    try:
        if nullable:
            if option == None or len(str(option).strip()) == 0:
                return can

        validate_func_args(function_to_verify=add_markable_square, variables_to_verify={'can':can, 'option':option, 'valid_options':valid_options, 'options_positions':options_positions, 'camp_name':camp_name, 'square_size':square_size, 'nullable':nullable})

        option = option.upper()
        for opt in range(0, len(valid_options)):
            if option == valid_options[opt]:
                can = add_square(can=can, pos=options_positions[opt], size=square_size)
                return can
        raise Exception(f'Cannot add {camp_name} because the option choosed does not exists')

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_multiple_markable_square(can:canvas.Canvas, options:list, valid_options:list, options_positions:tuple, camp_name:str, square_size:tuple=(9,9), nullable:bool=False) -> canvas.Canvas:
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
        
    """    
    try:
        if nullable:
            if option == None or len(str(option).strip()) == 0:
                return can
        

        validate_func_args(function_to_verify=add_multiple_markable_square, variables_to_verify={'can':can, 'options':options, 'valid_options':valid_options, 'options_positions':options_positions, 'camp_name':camp_name, 'square_size':square_size, 'nullable':nullable})


        option = option.upper()
        exist = False
        for opt in range(0, len(valid_options)):
            if option == valid_options[opt]:
                can = add_square(can=can, pos=options_positions[opt], size=square_size)
                exist = True
        if exist:
            return can
        raise Exception(f'Cannot add {camp_name} because the option choosed does not exists')
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')



def add_markable_square_and_onelinetext(can:canvas.Canvas, option:str, valid_options:list, text_options:list, text_pos:tuple, options_positions:tuple, camp_name:str, len_max:int, text:str=None, len_min:int=0, interval:str='', square_size:tuple=(9,9), nullable:bool=False) -> canvas.Canvas:
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
        
    """    
    try:
        if nullable:
            if option == None or len(str(option).strip()) == 0:
                return can

        
        validate_func_args(function_to_verify=add_markable_square_and_onelinetext, variables_to_verify={'can':can, 'option':option, 'valid_options':valid_options, 'text_options':text_options, 'text_pos':text_pos, 'options_positions':options_positions, 'camp_name':camp_name, 'len_max':len_max, 'text':text, 'len_min':len_min, 'interval':interval, 'square_size':square_size, 'nullable':nullable}, nullable_variables=['text'])

        #Verify if option exist
        option = option.upper()
        for opt in range(0, len(valid_options)):
            if option == valid_options[opt]:
                #Verify if option requer a text
                if option in text_options:
                    if text == None or str(text).strip() == '':
                        raise Exception(f'Cannot add {camp_name} because a text is required for {option} option')
                    else:
                        #Add text line
                        can = add_oneline_text(can=can, text=text, pos=text_pos, camp_name=camp_name, len_max=len_max, len_min=len_min, interval=interval)
                can = add_square(can=can, pos=options_positions[opt], size=square_size)
                return can
        raise Exception(f'Cannot add {camp_name} because the option choosed does not exists in {valid_options}')

    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')


def add_markable_square_and_morelinestext(can:canvas.Canvas, option:str, valid_options:list, text_options:list, text_pos:tuple, options_positions:tuple, camp_name:str, len_max:int, decrease_ypos:int, char_per_lines:int, max_lines_amount:int=None, text:str=None, len_min:int=0, interval:str='', square_size:tuple=(9,9), nullable:bool=False) -> canvas.Canvas:
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
    """    
    try:
        if nullable:
            if option == None or len(str(option).strip()) == 0:
                return can

        validate_func_args(function_to_verify=add_markable_square_and_morelinestext, variables_to_verify={'can':can, 'option':option, 'valid_options':valid_options, 'text_options':text_options, 'text_pos':text_pos, 'options_positions':options_positions, 'camp_name':camp_name, 'len_max':len_max, 'decrease_ypos':decrease_ypos, 'char_per_lines':char_per_lines, 'max_lines_amount':max_lines_amount, 'text':text, 'len_min':len_min, 'interval':interval, 'square_size':square_size, 'nullable':nullable}, nullable_variables=['text', 'max_lines_amount'])


        #Verify if option exist
        option = option.upper()
        for opt in range(0, len(valid_options)):
            if option == valid_options[opt]:
                #Verify if option requer a text
                if option in text_options:
                    if text == None or str(text).strip() == '':
                        raise Exception(f'Cannot add {camp_name} because a text is required for {option} option')
                    else:
                        #Add text line
                        can = add_morelines_text(can=can, text=text, initial_pos=text_pos, camp_name=camp_name, len_max=len_max, len_min=len_min, decrease_ypos=decrease_ypos, interval=interval, char_per_lines=char_per_lines, max_lines_amount=max_lines_amount)
                can = add_square(can=can, pos=options_positions[opt], size=square_size)
                return can
        raise Exception(f'Cannot add {camp_name} because the option choosed does not exists in {valid_options}')
    
    except Exception as error:
        raise error
    except:
        raise Exception(f'Erro desconhecido enquando adicionava {camp_name}')

