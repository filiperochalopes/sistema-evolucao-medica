## Requests strings
apac_request_string = """
# Write your query or mutation here
mutation{
	generatePdf_Apac(
		establishmentSolitcName: "Establihsment Name",
		establishmentSolitcCnes: 1234567,
		patientName: "Patient Name",
		patientCns: "928976954930007",
		patientSex: "M",
		patientBirthday: "22/10/2022",
		patientAdressCity: "Patient",
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
		patientMotherName: "Patient Mother Name",
		patientMotherPhonenumber: "3412344321",
		patientResponsibleName: "Patient Responsible Name",
		patientResponsiblePhonenumber: "5425415864",
		patientAdress: "Patient Adress ",
		patientEthnicity: "Etinia",
		patientColor: "BRANCA",
		patientAdressUF: "SP",
		patientAdressCEP: "12345678",
		documentChartNumber: "12345",
		patientAdressCityIbgeCode: "4528765",
		procedureJustificationDescription: "Procedure Justification Description",
		procedureJustificationMainCid10: "A123",
		procedureJustificationSecCid10: "A31",
		procedureJustificationAssociatedCauseCid10: "B435",
		procedureJustificationComments: "Procedure Justification Comments",
		establishmentExecName: "Etablishment Exec Name",
		establishmentExecCnes: 7654321,
		profSolicitorDocument: {
		cns: "928976954930007",
		cpf: null,
		rg: null
		},
		profSolicitorName: "Professional Solicitator",
		solicitationDatetime: "10/11/2021",
		profAutorizationName: "Professional Autorizaton",
		emissionOrgCode: "Cod121234",
		autorizatonProfDocument: {
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
"""

exam_request_request_string = """
# Write your query or mutation here
mutation{
	generatePdf_SolicitExames(
            patientName: "Patient NAme",
            patientCns: "928976954930007",
            patientBirthday: "10/10/2021",
            patientAdress: "Patient Adress",
            solicitationReason: "Solicitation reason",
            profSolicitorName: "Professional solicitor Name",
            solicitationDatetime: "10/10/2014",
            exams: "Exames Solicitados",
            profAuthorizedName: "Prof Autorization Name", 
            documentPacientName: "Document Pacient NAme",
            autorizationDatetime: "10/10/2021",
            documentPacientDate: "10/08/2021"
		){base64Pdf}
}
"""

exam_request_2_pages_request_string = """
# Write your query or mutation here
mutation{
	generatePdf_SolicitExames(
            patientName: "Patient NAme",
            patientCns: "928976954930007",
            patientBirthday: "10/10/2021",
            patientAdress: "Patient Adress",
            solicitationReason: "Solicitation reason",
            profSolicitorName: "Professional solicitor Name",
            solicitationDatetime: "10/10/2014",
            exams: "0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147148149150151152153154155156157158159160161162163164165166167168169",
            profAuthorizedName: "Prof Autorization Name", 
            documentPacientName: "Document Pacient NAme",
            autorizationDatetime: "10/10/2021",
            documentPacientDate: "10/08/2021"
		){base64Pdf}
}
"""










ficha_internamento_request_string = """
# Write your query or mutation here
mutation{
	generatePdf_FichaInternamento(
            documentDatetime: "10/10/2014 10:12",
            patientName: "Patient Name",
            patientCns: "928976954930007",
            patientBirthday: "10/10/2021",
            patientSex: "M",
            patientMotherName: "Patient Mother Name",
            patientDocument: {
            cpf: "28445400070",
            cns: null,
            rg: null
            },
            patientAdress: "Patient Adress",
            patientPhonenumber: "10123456789",
            patientDrugAllergies: "Patient Drug Allergies",
            patientComorbidities: "Patient Commorbidites",
            currentIllnessHistory: "Current Illness History",
            hasAdditionalHealthInsurance: "SIM",
            initialDiagnosticSuspicion: "Initial Suspiction",
            doctorName: "Doctor Name",
            doctorCns: "928976954930007",
            doctorCrm: "CRM/UF 123456",
            patientAdressNumber: 124,
            patientAdressNeigh: "Patient Neighbourhood",
            patientAdressCity: "Patient City",
            patientAdressUf: "SP",
            patientAdressCep: "12345678",
            patientNationality: "Brasileira",
            patientEstimateWeight: 140
		){base64Pdf}
}
"""

aih_sus_request_string = """
# Write your query or mutation here
mutation{
	generatePdf_AihSus(
            establishmentSolitcName: "Establishmente Solict Name",
            establishmentSolitcCnes: 1234567,
            establishmentExecName: "Establishment exec Name",
            establishmentExecCnes: 1234567,
            patientName: "Patient Name",
            patientCns: "928976954930007",
            patientBirthday: "10/10/2022",
            patientSex: "M",
            patientMotherName: "Patient Mother Name",
            patientAdress: "Patient Adress",
            patientAdressCity: "Jau",
            patientAdressCityIbgeCode: "1234567",
            patientAdressUF: "SP",
            patientAdressCEP: "12345678"
            mainClinicalSignsSymptoms: "Patient main clinical signs sysmpthoms",
            conditionsJustifyHospitalization: "Patient Conditions justify hiospitalizaiton",
            initialDiagnostic: "initial Siagnostic",
            principalCid10: "A12",
            procedureSolicited: "Procedurew Solicited",
            procedureCode: "1234567890",
            clinic: "Clinic Name",
            internationCarater: "TYriste",
            profSolicitorDocument: {
            cns: "928976954930007",
            cpf: null,
            rg: null
            },
            profSolicitorName: "Professional Solicitor Name",
            solicitationDatetime: "10/02/2021",
            profAutorizationName: "Professional Autorizator Name",
            emissionOrgCode: "12aass",
            autorizatonProfDocument: {
            cpf: "28445400070",
            cns: null,
            rg: null
            }
            autorizatonDatetime: "21/10/2022",
            hospitalizationAutorizationNumber: "1212",
            examResults: "Exam Results",
            chartNumber: "124",
            patientEthnicity: "Etnia",
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
    ){base64Pdf}
}
    """

lme_request_string = """
# Write your query or mutation here
mutation{
	generatePdf_Lme(
    establishmentSolitcName: "Establishment Solicit Name",
        establishmentSolitcCnes: 1234567,
        patientName: "Patient Name",
        patientMotherName: "Patient Mother Name",
        patientWeight: 142,
        patientHeight: 180,
        cid10: "A123",
        anamnese: "Anamnese",
        profSolicitorName: "Professional Solicitor Name",
        solicitationDatetime: "17/11/2022",
        profSolicitorDocument: {cpf:"28445400070"},
        capacityAttest: ["nao", "Responsible Name"],
        filledBy: ["MEDICO", "Other name", "{'cpf':'28445400070'}"],
        patientEthnicity: ["SEMINFO", "Patient Ethnicity"],
        previousTreatment: ["SIM", "Previout Theatment"],
        diagnostic: "Diagnostic",
        patientDocument: {cns: "928976954930007", rg: null, cpf: null},
        patientEmail: "patietemail@gmail.com",
        contactsPhonenumbers: ["1254875652", "4578456598"],
        medicines: [{medicineName: "nome do Medicamneto", quant1month:"20 comp",        quant2month: "15 comp", quant3month: "5 comp"},{medicineName: "nome do Medicamneto", quant1month:"20 comp", quant2month: "15 comp", quant3month: "5 comp"}]
){base64Pdf}
}
"""

prescricao_medica_request_string = """
# Write your query or mutation here
mutation{
	generatePdf_PrescricaoMedica(
    documentDatetime: "17/11/2022",
    patientName: "Pacient Name",
    prescription: [{medicineName:"Dipirona 500mg", amount:"4 comprimidos", useMode:"1 comprimido, via oral, de 6/6h por 3 dias"}]

){base64Pdf}
}
"""

relatorio_alta_request_string = """
# Write your query or mutation here
mutation{
	generatePdf_RelatorioAlta(
    documentDatetime: "17/11/2022 03:23",
    patientName: "Patient Name",
    patientCns: "928976954930007",
    patientBirthday: "17/11/2022",
    patientSex: "F",
    patientMotherName: "Patient Mother Name",
    patientDocument: {cpf: "28445400070", rg: null, cns: null},
    patientAdress: "pacient street, 43, paciten, USA",
    doctorName: "Doctor Name",
    doctorCns: "928976954930007",
    doctorCrm: "CRM/UF 123456",
    evolution: "Current illnes hsitoryaaaaaaaaaaaedqeqa",
    orientations: "Do not jump"
){base64Pdf}
}
"""

solicit_mamografia_request_string = """
# Write your query or mutation here
mutation{
	generatePdf_SolicitMamografia(
            patientCns: "928976954930007",
            patientBirthday: "10/10/2021",
            mammogramBefore: ["SIM", "2020"],
            patientAge: 24,
            patientName: "'Pacient Name",
            patientMotherName: "Paciente Mother Name",
            noduleLump: "SIMDIR",
            highRisk: "SIM",
            examinatedBefore: "NUNCA",
            healthUnitName: "heath Unit Name",
            healthUnitAdressUf: "SP",
            healthUnitAdressCity: "Jau",
            patientSurname: "Lero",
            patientAdress: "Patient Adress",
            patientAdressAdjunct: "Patient Adjunct",
            patientAdressNeighborhood: "Adress Neubr",
            patientAdressReference: "Reference",
            patientAdressCity: "CAi",
            patientAdressCep: "12345678",
            patientPhonenumber: "4212345678",
            radiotherapyBefore: ["NAO", null],
            breastSurgeryBefore: {
            didNot: "TRUE",
            biopsiaInsinonal: [null],
            biopsiaLinfonodo: [null],
            biopsiaExcisional: [null],
            centraledomia: [null], 
            segmentectomia: [null],
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
            patientDocumentCpf: {
            cns: null,
            rg: null,
            cpf: "28445400070"
            },
            patientAdressNumber: 12,
            patientAdressUf: "SP",
            healthUnitCityIbgeCode: "1234567",
            documentChartNumber: "142",
            patientSex: "M",
            patientNationality: "Brasileiro",
            patientCityIbgeCode: "1234567",
            patientEthnicity: ["BRANCA", null],
            profSolicitorName: "Professional Soliciame",
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
"""