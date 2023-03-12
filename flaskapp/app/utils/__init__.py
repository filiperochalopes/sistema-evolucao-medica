import datetime
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

def get_default_timestamp_interval():
    # Avalia o horário atual, se estiver à frente de 7h da manhã captura o dia de hoje e amanhã, se estiver atrás de 7h da manhã captura o dia de ontem e hoje.
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    yesterday = now + datetime.timedelta(days=-1)

    tomorrow = tomorrow.replace(hour=7, minute=0, second=0)
    now = now.replace(hour=7, minute=0, second=0)
    yesterday = yesterday.replace(hour=7, minute=0, second=0)

    if datetime.datetime.now().hour > 7:
        _start_datetime_ISO_string = now.strftime('%Y-%m-%dT%H:%M:%S')
        _ending_datetime_ISO_string = tomorrow.strftime('%Y-%m-%dT%H:%M:%S')
    else:
        _start_datetime_ISO_string = yesterday.strftime('%Y-%m-%dT%H:%M:%S')
        _ending_datetime_ISO_string = now.strftime('%Y-%m-%dT%H:%M:%S')

    class DatetimeISOStringInterval:
        start_datetime_ISO_string = _start_datetime_ISO_string
        ending_datetime_ISO_string = _ending_datetime_ISO_string

    return DatetimeISOStringInterval

def get_default_timestamp_interval_with_extra_interval_options(extra:dict):
    timestamp_interval = get_default_timestamp_interval()
    start_datetime_stamp = extra['interval']['start_datetime_stamp'] if 'interval' in extra and 'start_datetime_stamp' in extra['interval'] else datetime.strptime(timestamp_interval.start_datetime_ISO_string, '%Y-%m-%dT%H:%M:%S')
    ending_datetime_stamp = extra['interval']['ending_datetime_stamp'] if 'interval' in extra and 'ending_datetime_stamp' in extra['interval'] else datetime.strptime(timestamp_interval.ending_datetime_ISO_string, '%Y-%m-%dT%H:%M:%S')

    return (start_datetime_stamp, ending_datetime_stamp)