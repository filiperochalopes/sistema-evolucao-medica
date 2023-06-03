from gql import gql
import pytest
# from app.tests.pdfs.request_queries_examples import aih_sus_required_data_request_string

def data_to_use(client, datetime_to_use, requesting_establishment_name='Establishment Solicit Name',requesting_establishment_cnes="1234567",establishment_exec_name='Establshment Exec Name',establishment_exec_cnes="7654321",patient_name='Patient Name',patient_cns="928976954930007",patient_birthday=None,patient_sex='F',patient_mother_name='Patient Mother Name',patient_address='Patient Adress street neighobourd',patient_address_city='Patient City',patient_address_city_ibge_code='1234567', patient_address_uf='SP',patient_address_cep='12345678', evolution_description="Description"):

    if patient_birthday == None:
        patient_birthday = datetime_to_use
    # if solicitation_date == None:
    #     solicitation_date = datetime_to_use
    # if authorization_date == None:
    #     authorization_date = datetime_to_use

    patient_address = '{' + 'street: ' + f'"{patient_address}"' + ', city: ' + f'"{patient_address_city}"' + ', ibgeCityCode: ' + f'"{patient_address_city_ibge_code}"' + ', uf:' + f'"{patient_address_uf}"' + ', zipCode: ' + f'"{patient_address_cep}"' + '},'

    patient = '{name: ' + f'"{patient_name}"' + ', cns: ' + f'"{patient_cns}"' + ', birthdate: ' + f'"{patient_birthday}"' + 'phone: ' + f'"10123456789"' + ', sex: ' + f'"{patient_sex}"' + ',weightKg:' + '123' +', motherName: ' + f'"{patient_mother_name}"' + ', address: ' + f'{patient_address}' + '}'

    request_string = """
        mutation{
            generatePdf_EvolCompact("""
    
    campos_string = f"""
    patient: {patient},
    evolutionDescription: "{evolution_description}"
    """

    final_string = """
    ){base64Pdf}
    }
    """
    all_string = request_string + campos_string + final_string
    query = gql(all_string)
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        return True
    except:
        return False 


def test_with_data_in_function(client, datetime_to_use):
    assert data_to_use(client, datetime_to_use) == True
