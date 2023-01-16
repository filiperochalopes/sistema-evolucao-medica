# Exemplos de requests

## AIH SUS 
```graphql
# Write your query or mutation here
mutation{
	generatePdf_AihSus(
    establishmentSolitc: {
      name: "Establishmente Solict Name",
      cnes: "1234567"
    },
    establishmentExec: {
      name:"Establishment exec Name",
      cnes: "1234567"
    }
    patient: {
      name: "Patient Name",
      cns: "928976954930007",
      birthdate: "10/10/2022",
      sex: "M",
      ethnicity: "Etnia",
      weightKg: 123,
      motherName: "Patient Mother Name",
      address: {
        street: "Patient Adress",
        city: "Jau",
        ibgeCityCode: "1234567",
        uf: "SP",
        zipCode: "12345678"
      },
    },
    mainClinicalSignsSymptoms: "Patient main clinical signs sysmpthoms",
    conditionsJustifyHospitalization: "Patient Conditions justify hiospitalizaiton",
    initialDiagnostic: "initial Siagnostic",
    principalCid10: "A12",
    procedureSolicited: "Procedurew Solicited",
    procedureCode: "1234567890",
    clinic: "Clinic Name",
    internationCarater: "TYriste",
    professionalSolicitorDocument: {
    cns: "928976954930007",
    cpf: null,
    rg: null
    },
    professionalSolicitorName: "Professional Solicitor Name",
    solicitationDatetime: "10/02/2021",
    professionalAutorizationName: "Professional Autorizator Name",
    emissionOrgCode: "12aass",
    autorizatonProfessionalDocument: {
    cpf: "28445400070",
    cns: null,
    rg: null
    }
    autorizatonDatetime: "21/10/2022",
    hospitalizationAutorizationNumber: "1212",
    examResults: "Exam Results",
    chartNumber: "124",
    patientResponsibleName: "Responsible NAme",
    patientMotherPhonenumber: "4212344321",
    patientResponsiblePhonenumber: "1245875421",
    secondaryCid10: "S32",
    cid10AssociatedCauses: "A213",
    acidentType: "WORK",
    insuranceCompanyCnpj: "37549670000171",
    insuranceCompanyTicketNumber: "12354",
    insuranceCompanySeries: "1233",
    companyCnpj: "37549670000171",
    companyCnae: 5310501,
    companyCbor: 123456,
    pensionStatus: "WORKER"
  )
{base64Pdf}
}
```

## APAC
```graphql
# Write your query or mutation here
mutation{
	generatePdf_Apac(
		establishmentSolitc: {
        name: "Establishmente Solict Name",
        cnes: "1234567"
      },
    establishmentExec: {
      name:"Establishment exec Name",
      cnes: "1234567"
    },
    patient: {
        name: "Patient Patient Name",
        cns: "928976954930007",
        birthdate: "10/10/2022",
        sex: "M",
        ethnicity: "Etnia",
        motherName: "Patient Mother Name",
        weightKg: 123.00,
        address: {
          street: "Patient Adress",
          city: "Jau",
          ibgeCityCode: "1234567",
          uf: "SP",
          zipCode: "12345678"
        },
    },
		mainProcedure: {
      name: "teste procedimento",
      code: "hkmaug347s",
      quant: 1
      },
      secondariesProcedures:[
      {
      name: "teste procedimento",
      code: "hkmaug347s",
      quant: 1
      },
      {
      name: "segundo procedimento",
      code: "hkmhsa3s23",
      quant: 4
      }
		],
		patientMotherPhonenumber: "3412344321",
		patientResponsibleName: "Patient Responsible Name",
		patientResponsiblePhonenumber: "5425415864",
		patientColor: "BRANCA",
		documentChartNumber: "12345",
		procedureJustificationDescription: "Procedure Justification Description",
		procedureJustificationMainCid10: "A123",
		procedureJustificationSecCid10: "A31",
		procedureJustificationAssociatedCauseCid10: "B435",
		procedureJustificationComments: "Procedure Justification Comments",
		professionalSolicitorDocument: {
		cns: "928976954930007",
		cpf: null,
		rg: null
		},
		professionalSolicitorName: "Professional Solicitator",
		solicitationDatetime: "10/11/2021",
		professionalAutorizationName: "Professional Autorizaton",
		emissionOrgCode: "Cod121234",
		autorizatonProfessionalDocument: {
		cns: "928976954930007",
		cpf: null,
		rg: null
		},
		autorizatonDatetime: "10/10/2022",
		signatureDatetime: "15/10/2022",
		validityPeriodStart: "15/10/2022",
		validityPeriodEnd: "15/11/2022"
		)
{base64Pdf}
}
```

## Solicitação de Mamografia
```graphql
# Write your query or mutation here
mutation{
	generatePdf_SolicitMamografia(
      patient: {
      	name: "Pacient Name",
        cns: "928976954930007",
        birthdate: "10/10/2000",
        motherName: "Paciente Mother Name",
        cpf: "28445400070",
        sex: "M",
        weightKg: 123,
        nationality: "Brasileiro",
        address:{
          street: "Patient Adress",
          uf: "SP",
          neighborhood: "Adress Neubr",
          city: "Jau",
          complement: "Patient Adjunct",
          zipCode: "12345678",
          reference: "Reference"
          number: "123",
          ibgeCityCode: "1234567",
        },
        
      }
      mammogramBefore: ["SIM", "2020"],
      noduleLump: "SIMDIR",
      highRisk: "SIM",
      examinatedBefore: "NUNCA",
      healthUnitName: "heath Unit Name",
      patientSurname: "Lero",
      patientPhonenumber: "4212345678",
      radiotherapyBefore: ["NAO", null],
      breastSurgeryBefore: {
      didNot: "false",
      biopsiaInsinonal: ["2020", null],
      biopsiaLinfonodo: [null],
      biopsiaExcisional: [null],
      centraledomia: [null], 
      segmentectomia: ["2021", "2010"],
      dutectomia: [null],
      mastectomia: [null],
      mastectomiaPoupadoraPele: [null],
      mastectomiaPoupadoraPeleComplexoAreolo: [null],
      linfadenectomiaAxilar: [null],
      reconstrucaoMamaria: [null],
      mastoplastiaRedutora: [null],
      indusaoImplantes: [null]
      },
      healthUnitCnes: 1234567,
      protocolNumber: "1233",
      healthUnitCityIbgeCode: "1234567",
      documentChartNumber: "142",
      patientEthnicity: ["BRANCA", null],
      professionalSolicitorName: "Professional Soliciame",
      solicitationDatetime: "10/10/2012",
      examNumber: "4124",
      trackingMammogram: "POPALVO",
      diagnosticMammogram: {
      exameClinico:{
          direta: {
          papilar: true,
          descargaPapilar: ["CRISTALINA", "HEMORRAGICA"],
          nodulo: ["QSL", "QIL", "QSM", "QIM"],
          espessamento: ["QSL", "QIL", "QSM", "QIM"],
          linfonodoPalpavel: ["AXILAR", "SUPRACLAVICULAR"]
          },
          esquerda:{
          papilar: true,
          descargaPapilar: ["CRISTALINA", "HEMORRAGICA"],
          nodulo: ["QSL", "QIL", "QSM", "QIM"],
          espessamento: ["QSL", "QIL", "QSM", "QIM"],
          linfonodoPalpavel: ["AXILAR", "SUPRACLAVICULAR"]
          }
      },
      controleRadiologico:{
          direta: ["nodulo", "microca", "assimetria_focal"],
          esquerda: ["nodulo", "microca", "assimetria_focal"]
      },
      lesaoDiagnostico: {
          direta: ["nodulo", "microca", "assimetria_focal"],
          esquerda: ["nodulo", "microca", "assimetria_focal"] 
      },
      avaliacaoResposta: ["direita", "esquerda"],
      revisaoMamografiaLesao: {
          direta: ["0", "3", "4", "5"],
          esquerda: ["0", "3", "4", "5"]
      },
      controleLesao: {
          direta: ["nodulo", "microca", "assimetria_focal"],
          esquerda: ["nodulo", "microca", "assimetria_focal"]
      }

      }
){base64Pdf}
}
```

## Solicitacao de Exames
```graphql
# Write your query or mutation here
mutation{
	generatePdf_SolicitExames(
    patient: {
      name: "Patient NAme",
      cns: "928976954930007",
      birthdate: "10/10/2021",
      weightKg: 123.00,
      address: {
        street: "Patient Adress",
        city: "City",
        uf: "SP",
      },
    },
    solicitationReason: "Solicitation reason",
    professionalSolicitorName: "Professional solicitor Name",
    solicitationDatetime: "10/10/2014",
    exams: "Exames Solicitados",
    professionalAuthorizedName: "Prof Autorization Name", 
    documentPacientName: "Document Pacient NAme",
    autorizationDatetime: "10/10/2021",
    documentPacientDate: "10/08/2021"
  )
{base64Pdf}
}
```

## Ficha Internamento
```graphql
# Write your query or mutation here
mutation{
	generatePdf_FichaInternamento(
    documentDatetime: "10/10/2020 10:12",
    patient: {
      name: "Patient Name",
      cns: "928976954930007",
      cpf: "14383811744",
      rg: null,
      birthdate: "10/10/2021",
      nationality: "Brasileira",
      sex: "M",
      weightKg: 123.00,
      motherName: "Patient Mother Name",
      address: {
        street: "Patient Adress",
        number: "124",
        neighborhood: "Patient Neighbourhood",
        city: "Patient City",
        uf: "SP",
        zipCode: "12345678",
      },
      comorbidities: ["Patient", "Commorbidites"],
      allergies: ["Patient", "Drug", "Allergies"],
    }
    currentIllnessHistory: "Current Illness History",
    patientPhonenumber: "10123456789",
    hasAdditionalHealthInsurance: "SIM",
    initialDiagnosticSuspicion: "Initial Suspiction",
    doctorName: "Doctor Name",
    doctorCns: "928976954930007",
    doctorCrm: "CRM/UF 123456",
  )
{base64Pdf}
}
```

## LME
```graphql
# Write your query or mutation here
mutation{
	generatePdf_Lme(
    establishmentSolitc: {
      name: "Establishment Solicit Name",
      cnes: "1234567"
    },
    patient: {
      name: "Patient Name Name",
      motherName:"Patient Mother Name",
      cns: "928976954930007",
      cpf: null,
      weightKg: 123,
    }
    patientHeight: 180,
    cid10: "A123",
    anamnese: "Anamnese",
    professionalSolicitorName: "Professional Solicitor Name",
    solicitationDatetime: "17/11/2022",
    professionalSolicitorDocument: {cpf:"28445400070"},
    capacityAttest: ["nao", "Responsible Name"],
    filledBy: ["MEDICO", "Other name", "{'cpf':'28445400070'}"],
    patientEthnicity: ["SEMINFO", "Patient Ethnicity"],
    previousTreatment: ["SIM", "Previout Theatment"],
    diagnostic: "Diagnostic",
    patientEmail: "patietemail@gmail.com",
    contactsPhonenumbers: ["1254875652", "4578456598"],
    medicines: [
      {
        medicineName: "nome do Medicamneto",
        quant1month:"20 comp",        
        quant2month: "15 comp", 
        quant3month: "5 comp"
        },
      {
        medicineName: "nome do Medicamneto", 
        quant1month:"20 comp", 
        quant2month: "15 comp", 
        quant3month: "5 comp"
        }
    ]
){base64Pdf}
}
```

## Prescricao Medica
```graphql
# Write your query or mutation here
mutation{
	generatePdf_PrescricaoMedica(
    documentDatetime: "17/11/2022",
    professional:{
      name: "Professional Name",
      category: "m",
      document: "12345/BA"
    },
    patient: {
      name: "Pacient Name Name",
      cns: "928976954930007",
      weightKg: 123,
    },
    prescription: [
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
    ]
){base64Pdf}
}
```

## Relatorio de Alta

```graphql
# Write your query or mutation here
mutation{
	generatePdf_RelatorioAlta(
    documentDatetime: "17/11/2022 03:23",
    patient: {
      name:"Patient Namme",
      cns: "928976954930007",
      birthdate: "17/11/2022",
      sex: "F",
      weightKg: 123,
      motherName: "Patient Mother Name",
      cpf: "28445400070",
      rg: null,
      address: {
        street: "pacient street",
        neighborhood: "neighborhood",
        number: "41",
        city: "City",
        uf: "SP"
      }
    }    
    doctorName: "Doctor Name",
    doctorCns: "928976954930007",
    doctorCrm: "CRM/UF 123456",
    evolution: "Current illnes hsitoryaaaaaaaaaaaedqeqa",
    orientations: "Do not jump"
){base64Pdf}
}
```

## Folha de Prescrição

```graphql
# Write your query or mutation here
mutation{
	generatePdf_FolhaPrescricao(
    createdAt: "10/10/2022 10:21",
    printedAt: "10/10/2022 10:21",
    patient: {
      name: "Patient Test Name",
      cns: "928976954930007",
      weightKg: 123.00,
    },
    prescriptions: [
      {
        type: "Repouso",
        description: "Prescription description",
        route: "Endovenosa",
        startDate: "10/11/2022",
        endingDate: "21/11/2022"      
      },
      {
        type: "Dieta",
        description: "Dieta para hidratacao haahahah",
        route: "Dieta",
        startDate: "10/11/2022",
        endingDate: "21/11/2022"      
      },
      {
        type: "Repouso",
        description: "Prescription description",
        route: "Endovenosa",
        startDate: "10/11/2022",
        endingDate: "21/11/2022"      
      },
      {
        type: "Repouso",
        description: "Prescription description",
        route: "Endovenosa",
        startDate: "10/11/2022",
        endingDate: "21/11/2022"      
      },
      {
        type: "Dieta",
        description: "Dieta para hidratacao haahahah",
        route: "Dieta",
        startDate: "10/11/2022",
        endingDate: "21/11/2022"      
      },
      {
        type: "Repouso",
        description: "Prescription description",
        route: "Endovenosa",
        startDate: "10/11/2022",
        endingDate: "21/11/2022"      
      },
      {
        type: "Repouso",
        description: "Prescription description",
        route: "Endovenosa",
        startDate: "10/11/2022",
        endingDate: "21/11/2022"      
      },
      {
        type: "Repouso",
        description: "Prescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription descriptionPrescription description",
        route: "Endovenosa",
        startDate: "10/11/2022",
        endingDate: "21/11/2022"      
      },
      {
        type: "Repouso",
        description: "Prescription description",
        route: "Endovenosa",
        startDate: "10/11/2022",
        endingDate: "21/11/2022"      
      },
      {
        type: "Repouso",
        description: "Prescription description",
        route: "Endovenosa",
        startDate: "10/11/2022",
        endingDate: "21/11/2022"      
      }
    ]
){base64Pdf}
}
```

## Folha de Evolução

```graphql
# Write your query or mutation here
mutation{
	generatePdf_FolhaEvolucao(
    createdAt: "10/10/2022 20:10",
    patient: {
      name: "Patient Test Name",
      cns: "928976954930007",
      weightKg: 123.00,
    },
    evolutions:[
      {
        createdAt: "10/10/2022 20:10",
        description: "quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem. Cras tempus malesuada erat, eget lacinia sem ultrices id. Nulla pretium, massa nec aliquet mattis, erat felis egestas massa, eu lacinia ipsum ligula eu sapien. Maecenas posuere, felis sit amet viverra fini",
        professional:
        {
          name: "Professional Name",
          category: "m",
          document: "12345/BA"
        }
      },
      {
        createdAt: "10/10/2022 20:10",
        description: "quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem. Cras tempus malesuada erat, eget lacinia sem ultrices id. Nulla pretium, massa nec aliquet mattis, erat felis egestas massa, eu lacinia ipsum ligula eu sapien. Mae",
        professional:
        {
          name: "Another Professional Name",
          category: "e",
          document: "1234534"
        }
      },
      {
        createdAt: "10/10/2022 20:10",
        description: "quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem. Cras tempus malesuada erat, eget lacinia sem ultrices id.quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem. Cras tempus malesuada erat, eget lacinia sem ultrices id.quam, at commodo ligula. Suspendisse sed pulvinar arcu, vel fermentum leo. Ut ligula orci, dictum in elit sed, sodales sollicitudin sem.",
        professional:{
          name: "Professional aaaa Name",
          category: "m",
          document: "54321/BA"
        }
      },
      {
        createdAt: "10/10/2022 20:10",
        description: "quam, at commodo ligula. Suspendisse sed pulvinar arcu, ",
    	  professional:
        {
          name: "Last Professional Name",
          category: "e",
         document: "987654"
        }
      },
    ]
    measures: [
      {
        createdAt: "10/10/2022 20:10",
        cardiacFrequency: 54,
        respiratoryFrequency: 15,
        sistolicBloodPressure: 152,
        diastolicBloodPressure: 84,
        glucose: "152",
        spO2: 96,
        celciusAxillaryTemperature: 37,
        pain: 2,
        professional:{
          name: "Professional aaaa Name",
          category: "m",
          document: "54321/BA"
        }
      },
      {
        createdAt: "12/10/2022 12:40",
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
        createdAt: "10/10/2022 20:10",
        cardiacFrequency: 54,
        respiratoryFrequency: 15,
        sistolicBloodPressure: 152,
        diastolicBloodPressure: 84,
        glucose: "152",
        spO2: 96,
        celciusAxillaryTemperature: 37,
        pain: 2,
        professional:{
          name: "Professional aaaa Name",
          category: "m",
          document: "54321/BA"
        }
      },
      {
        createdAt: "12/10/2022 12:40",
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
        createdAt: "10/10/2022 20:10",
        cardiacFrequency: 54,
        respiratoryFrequency: 15,
        sistolicBloodPressure: 152,
        diastolicBloodPressure: 84,
        glucose: "152",
        spO2: 96,
        celciusAxillaryTemperature: 37,
        pain: 2,
        professional:{
          name: "Professional aaaa Name",
          category: "m",
          document: "54321/BA"
        }
      },
      {
        createdAt: "12/10/2022 12:40",
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
        createdAt: "10/10/2022 20:10",
        cardiacFrequency: 54,
        respiratoryFrequency: 15,
        sistolicBloodPressure: 152,
        diastolicBloodPressure: 84,
        glucose: "152",
        spO2: 96,
        celciusAxillaryTemperature: 37,
        pain: 2,
        professional:{
          name: "Professional aaaa Name",
          category: "m",
          document: "54321/BA"
        }
      },
      {
        createdAt: "12/10/2022 12:40",
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
        createdAt: "10/10/2022 20:10",
        cardiacFrequency: 54,
        respiratoryFrequency: 15,
        sistolicBloodPressure: 152,
        diastolicBloodPressure: 84,
        glucose: "152",
        spO2: 96,
        celciusAxillaryTemperature: 37,
        pain: 2,
        professional:{
          name: "Professional aaaa Name",
          category: "m",
          document: "54321/BA"
        }
      },
      {
        createdAt: "12/10/2022 12:40",
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
        createdAt: "10/10/2022 20:10",
        cardiacFrequency: 54,
        respiratoryFrequency: 15,
        sistolicBloodPressure: 152,
        diastolicBloodPressure: 84,
        glucose: "152",
        spO2: 96,
        celciusAxillaryTemperature: 37,
        pain: 2,
        professional:{
          name: "Professional aaaa Name",
          category: "m",
          document: "54321/BA"
        }
      },
      {
        createdAt: "12/10/2022 12:40",
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
      }
    ])
{base64Pdf}
}
```

## Balanço Hídrico

```graphql
# Write your query or mutation here
mutation{
	generatePdf_BalancoHidrico(
    createdAt: "10/10/2020",
    patient: {
      name: "Patient Test Name",
      cns: "928976954930007",
      weightKg: 123.00,
    },
    fluidBalance:[
      {
        createdAt: "20/12/2022 10:35",
        value: -600,
        description: "diurese"
      },
      {
        createdAt: "28/06/2022 3:10",
        value: 600,
        description: "Antibiótico"
      },
      {
        createdAt: "09/04/2022 8:54",
        value: -300,
        description: "Dreno de Tórax"
      },
      {
        createdAt: "20/12/2022 10:35",
        value: -600,
        description: "diurese"
      },
      {
        createdAt: "28/06/2022 3:10",
        value: 600,
        description: "Antibiótico"
      },
      {
        createdAt: "09/04/2022 8:54",
        value: -300,
        description: "Dreno de Tórax"
      },
      {
        createdAt: "20/12/2022 10:35",
        value: -600,
        description: "diurese"
      },
      {
        createdAt: "28/06/2022 3:10",
        value: 600,
        description: "Antibiótico"
      },
      {
        createdAt: "09/04/2022 8:54",
        value: -300,
        description: "Dreno de Tórax"
      },
      {
        createdAt: "20/12/2022 10:35",
        value: -600,
        description: "diurese"
      },
      {
        createdAt: "28/06/2022 3:10",
        value: 600,
        description: "Antibiótico"
      },
      {
        createdAt: "09/04/2022 8:54",
        value: -300,
        description: "Dreno de Tórax"
      },
      {
        createdAt: "20/12/2022 10:35",
        value: -600,
        description: "diurese"
      },
      {
        createdAt: "28/06/2022 3:10",
        value: 600,
        description: "Antibiótico"
      },
      {
        createdAt: "09/04/2022 8:54",
        value: -300,
        description: "Dreno de Tórax"
      },
      {
        createdAt: "20/12/2022 10:35",
        value: -600,
        description: "diurese"
      },
      {
        createdAt: "28/06/2022 3:10",
        value: 600,
        description: "Antibiótico"
      },
      {
        createdAt: "09/04/2022 8:54",
        value: -300,
        description: "Dreno de Tórax"
      },
      {
        createdAt: "20/12/2022 10:35",
        value: -600,
        description: "diurese"
      },
      {
        createdAt: "28/06/2022 3:10",
        value: 600,
        description: "Antibiótico"
      },
      {
        createdAt: "09/04/2022 8:54",
        value: -300,
        description: "Dreno de Tórax"
      },
    ]
	){base64Pdf}
}
```