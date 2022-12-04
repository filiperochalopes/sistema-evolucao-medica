from datetime import date
import sys

def calculate_age(birthdate:date):
    '''Captura a idade completa, dada uma data de nascimento'''

    today = date.today()
    birthday_not_passed = ((today.month, today.day) < (birthdate.month, birthdate.day))
    age_year = today.year - birthdate.year - birthday_not_passed
    age_month = (birthdate.month + today.month) if birthday_not_passed else (birthdate.month - today.month)
    age_day = (birthdate.day + today.day) if birthday_not_passed else (today.day - birthdate.day)
    age_string = ''
    print(age_year, age_month, age_day, file=sys.stderr)
    if age_year > 1:
        age_string += f'{age_year} anos'
    elif age_year == 1:
        age_string += f'{age_year} ano'
    if age_month > 1:
        age_string += f', {age_month} meses'
    elif age_month == 1:
        age_string += f', {age_month} mês'
    if age_day > 1:
        age_string += f', {age_day} dias'
    elif age_day == 1:
        age_string += f', {age_day} dia'
    return age_string