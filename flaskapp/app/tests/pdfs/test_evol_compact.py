from gql import gql
import pytest

from app.tests.pdfs.request_queries_examples import (
    evol_compact_request_string,
    evol_compact_required_data_request_string,
)


def data_to_use(
    client,
    datetime_with_timezone_to_use,
    patient_name="Patient Name",
    patient_cns="928976954930007",
    patient_birthday=None,
    patient_sex="F",
    patient_mother_name="Patient Mother Name",
    patient_address="Patient Adress street neighobourd",
    patient_address_city="Patient City",
    patient_address_city_ibge_code="1234567",
    patient_address_uf="SP",
    patient_address_cep="12345678",
    comorbidities='["Patient", "Commorbidites"]',
    allergies='["Patient", "Allergies"]',
    regulation_code="RegulaCode",
    admission_history="""{
    professional:{
        name: "Professional aaaa Name",
        category: "m",
        document: "54321/BA"
    },
    professionalCreatedDate: "2023-02-13T01:17:20.624559",
    admissionDate: "2021-10-23",
    internmentDay: 4,
    admissionText: "Admission text"
    }""",
    evolution="""{
        createdAt: "2023-02-12T23:59:24",
        text: "quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem. Cras tempus malesuada erat, eget lacinia sem ultrices id. Nulla pretium, massa nec aliquet mattis, erat felis egestas massa, eu lacinia ipsum ligula eu sapien. Mae",
        professional:
        {
            name: "Another Professional Name",
            category: "e",
            document: "1234534"
        }
    }""",
    prescription="""{
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        },
        {
        medicineName:"Dipirona 500mg", 
        amount:"4 comprimidos", 
        useMode:"1 comprimido, via oral, de 6/6h por 3 dias"
        }""",
    prescription_cares="Cuidados de Enfermagem",
    measures="""{
        createdAt: "2023-02-12T23:59:24",
        cardiacFrequency: 54,
        respiratoryFrequency: 15,
        sistolicBloodPressure: 152,
        diastolicBloodPressure: 84,
        glucose: "152",
        spO2: 96,
        celciusAxillaryTemperature: 37,
        pain: 2,
        fetalCardiacFrequency: 52,
        professional:{
            name: "Professional aaaa Name",
            category: "m",
            document: "54321/BA"
        }
        },
        {
        createdAt: "2023-02-12T22:59:24",
        cardiacFrequency: 32,
        respiratoryFrequency: 10,
        sistolicBloodPressure: 124,
        diastolicBloodPressure: 81,
        glucose: "400",
        spO2: 92,
        celciusAxillaryTemperature: 38,
        pain: 5,
        fetalCardiacFrequency: 52,
        professional:{
        name: "Another Professional name",
        category: "e",
        document: "4512788"
        }
    },
    {
        createdAt: "2023-02-12T23:59:24",
        cardiacFrequency: 54,
        respiratoryFrequency: 15,
        sistolicBloodPressure: 152,
        diastolicBloodPressure: 84,
        glucose: "152",
        spO2: 96,
        celciusAxillaryTemperature: 37,
        pain: 2,
        fetalCardiacFrequency: 52,
        professional:{
        name: "Professional aaaa Name",
        category: "m",
        document: "54321/BA"
        }
    },
    {
        createdAt: "2023-02-12T22:59:24",
        cardiacFrequency: 32,
        respiratoryFrequency: 10,
        sistolicBloodPressure: 124,
        diastolicBloodPressure: 81,
        glucose: "400",
        spO2: 92,
        celciusAxillaryTemperature: 38,
        pain: 5,
        professional:{
        name: "Another Professional name",
        category: "e",
        document: "4512788"
        }
    },
    {
        createdAt: "2023-02-12T23:59:24",
        cardiacFrequency: 54,
        respiratoryFrequency: 15,
        sistolicBloodPressure: 152,
        diastolicBloodPressure: 84,
        glucose: "152",
        spO2: 96,
        celciusAxillaryTemperature: 37,
        pain: 2,
        fetalCardiacFrequency: 52,
        professional:{
        name: "Professional aaaa Name",
        category: "m",
        document: "54321/BA"
        }
    }""",
):
    if patient_birthday == None:
        patient_birthday = datetime_with_timezone_to_use


    # patient_birthday = patient_birthday.isoformat()

    patient_address = "{"+ "street: "+ f'"{patient_address}"'+ ", city: "+ f'"{patient_address_city}"'+ ", ibgeCityCode: "+ f'"{patient_address_city_ibge_code}"'+ ", uf:"+ f'"{patient_address_uf}"'+ ", zipCode: "+ f'"{patient_address_cep}"'+ "},"

    patient = "{name: " + f'"{patient_name}"'+ ", cns: "+ f'"{patient_cns}"'+ ", birthdate: "+ f'"{patient_birthday}"'+ ", phone: "+ f'"10123456789"'+ ", sex: "+ f'"{patient_sex}"'+ ",weightKg:"+ "123"+ ", motherName: "+ f'"{patient_mother_name}"'+ ", comorbidities: "+ f"{comorbidities}"+ ", allergies: "+ f"{allergies}"+ ", address: "+ f"{patient_address}"+ "}"

    request_string = """
        mutation{
            generatePdf_EvolCompact("""

    campos_string = f"""
    patient: {patient},
    regulationCode: "{regulation_code}",
    documentCreatedAt: "{datetime_with_timezone_to_use}",
    admissionHistory: {admission_history},
    evolution:{evolution},
    prescription: [{prescription}],
    prescriptionCares: "{prescription_cares}",
    measures: [{measures}],
    """

    final_string = """
    ){base64Pdf}
    }
    """
    all_string = request_string + campos_string + final_string
    query = gql(all_string)
    #try:
        # When some exception is created in grphql he return a error
    print(all_string)
    client.execute(query)
    return True
    # except:
    #     return False


def test_with_data_in_function(client, datetime_with_timezone_to_use):
    assert data_to_use(client, datetime_with_timezone_to_use) == True


def test_answer_with_all_fields(client, datetime_with_timezone_to_use):
    assert data_to_use(client, datetime_with_timezone_to_use) == True


def test_awnser_with_only_required_data(client):
    query = gql(evol_compact_required_data_request_string)
    result = False
    try:
        # When some exception is created in grphql he return a error
        client.execute(query)
        result = True
    except:
        result = False

    assert result == True

# ? Esses testes foram feitos?
# TODO Remover esses comentários que são mais lembretes e não explicativos quando concluir
#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_date
# authorization_date
# test wrong type
# test valid datetime


def test_valid_patient_birthday(client, datetime_with_timezone_to_use):
    assert (
        data_to_use(client, datetime_with_timezone_to_use,
                    patient_birthday=datetime_with_timezone_to_use) == True
    )
