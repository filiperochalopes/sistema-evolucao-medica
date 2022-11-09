from ariadne import gql, QueryType, MutationType

# Define type definitions (schema) using SDL
type_defs = gql(
    '''
    type Query {
       users: [User]
       cid10: [Cid10!]
       patients(queryNameCnsCpf:String): [Patient]
       internments(active:Boolean): [Internment]
       evolutions(patientId:ID!): Evolution
    }  

    type Mutation {
        """
        Cria um usuário com a masterKey de superusuário, cadastrado internamente para fins de MVP, 
        o cadastro será feito via requisição em terminal ou via playground na rota /graphql
        """
        createUser(
            "Chave mestra do usuário `root` para poder realizar cadastro de usuários"
            masterKey:String!, 
            user: UserInput): User
        """
        Realizar login e receber o token
        """
        signin(email:String!, password:String!): UserToken
        """
        Mutation serve para atualizar dados que são passíveis de atualização do usuário mediante a senha `root` `masterKey`
        """
        updateUser(
            id: ID!, 
            "Chave mestra do usuário `root` para poder realizar cadastro de usuários"
            masterKey:String!, 
            user: UserInput): User
        """
        Criar paciente para cadastro do 
        """
        createPatient(patient: PatientInput): Patient
        """
        Atualizar paciente
        """
        updatePatient(is: ID!, patient:PatientInput): Patient
        createInternment(
            "No formato yyyy-mm-dd HH:MM"
            admissionDatetime:String,
            "Dados do paciente"
            patient:PatientInput, 
            "História da doença atual"
            hpi: String, 
            "Dados clínicos e de exames que justificam o internamento"
            justification:String,
            "Diagnóstico inicial de internamento"
            cid10Code: String
        ): Internment

        "Criação de documento de AIH"
        generatePdf_AihSus(
            "Nome do Estabelecimento Solicitante, max:82 min:7 caracteres"
            establishmentSolitcName: String,
            "CNES do Estabelecimento Solicitante"
            establishmentSolitcCnes: Int, 
            "Nome do Estabelecimento Executante, max:82 min:8 caracteres"
            establishmentExecName: String, 
            "CNES do Estabelecimento Executante"
            establishmentExecCnes: Int, 
            "Nome do paciente, max:79 min:7 caracteres"
            patientName: String, 
            "Número do Cartão do SUS do paciente"
            patientCns: Int,
            "Data de nascimento do paciente, em timestamp SEM fusohorario (utilizando o padrao UTC)"
            patientBirthday: String,
            "Sexo do Paciente, opcao M ou F."
            patientSex: String,
            "Nome da Mae do paciente, max:70 min:7 caracteres"
            patientMotherName: String, 
            "Endereco do paciente, somente 'rua, numero, bairro', max: 101 min:7 caracteres"
            patientAdress: String, 
            "Cidade do paciente, max:58 min:7 caracteres"
            patientAdressCity: String, 
            "Codigo IBGE do municipio do paciente"
            patientAdressCityIbgeCode: Int,
            "Sigla do estado, UF, da cidade do paciente, somente estados do Brasil"
            patientAdressUF: String,
            "CEP do endereço do paciente"
            patientAdressCEP: Int,
            "Principais sintomas e sintomas clinicos, max:1009 min:5 caracteres"
            mainClinicalSignsSymptoms: String,
            "Condicoes que justificam a internacao, max:403 min:5 caracteres"
            conditionsJustifyHospitalization: String,
            "Diagnostico inicial, max:44 min:5 caracteres"
            initialDiagnostic: String,
            "Cid 10 princical, usando o formato padrao de CID, max:4 min:3 caracteres"
            principalCid10: String, 
            "Procedimento solicitado, max:65 min:6 caracteres"
            procedureSolicited: String,
            "Codigo do procedimento solcitado, deve ter exatamente 10 caracteres"
            procedureCode: String,
            "Nome da clinica, max:18 min:6 caracteres"
            clinic: String, 
            "Carater da internacao, max:19 min:6 caracteres"
            internationCarater: String, 
            "Documento do profissional solicitante, cns ou cpf, a api python o trata como dicionario, entao envie como uma string no formato '{'CNS':928976954930007}', a primeira e o nome do documento, e o seguinte e o numero do documento como inteiro"
            profSolicitorDocument: String, 
            "Nome do profissional solicitante, max:48 min:8 caracteres"
            profSolicitorName: String,
            "Data e hora da solicitacao, somente dia/mes/ano, envie como timestamp SEM fusohorario (Padrao UTC)"
            solicitationDatetime: String,
            "Nome do profissional autorizador, max:48 min:8 caracteres" 
            autorizationProfName: String,
            "Codigo da organizacao emissora, esse dado fica no campo de autorizacao, max:17 min:2 caracteres"
            emissionOrgCode: String, 
            "Documento do profissional autorizador, cns ou cpf, a api python o trata como dicionario, entao envie como uma string no formato '{'CNS':928976954930007}', a primeira e o nome do documento, e o seguinte e o numero do documento como inteiro"
            autorizatonProfDocument: String,
            "Data e hora da autorizacao, somente dia/mes/ano, envie como timestamp SEM fusohorario (Padrao UTC)"
            autorizatonDatetime: String,
            "Numero da autorizacao de internacao hospitalar, no maximo 18 digitos"
            hospitalizationAutorizationNumber: Int,
            examResults: String, 
            chartNumber: Int, 
            patientEthnicity: String, 
            patientResponsibleName: String, 
            "Não seria melhor o telefone ser tipo string?"
            patientMotherPhonenumber: Int, 
            patientResponsiblePhonenumber: Int, 
            secondaryCid10: String, 
            cid10AssociatedCauses: String, 
            acidentType: String, 
            insuranceCompanyCnpj: Int, 
            insuranceCompanyTicketNumber: Int, 
            insuranceCompanySeries: String,
            companyCnpj: Int, 
            companyCnae: Int, 
            company_cbor: Int, 
            pension_status: Int
        ): GeneratedPdf

        "Criação de documento de Precricao medica"
        generatePdf_PrecricaoMedica(
            documentDatetime: String,
            patientName: String,
            prescription: [String]
        ): GeneratedPdf
    }

    input AddressInput{
        zipCode: String
        street:String
        complement:String
        number:String
        city: String!
        uf: String!
    }

    input UserInput{
        "Nome do usuário/profissional cadastrado"
        name: String!, 
        "Email do usuário cadastrado, será utilizado para realização de login"
        email: String!, 
        "Telefone do usuário, apenas dígitos 75986523256"
        phone: String,
        "Senha de cadastro, poderá ser atualizada depois pelo usuário, default `senha@123" 
        password: String, 
        "Apenas dígitos, para fins de testes pode gerar [nesse link](https://geradornv.com.br/gerador-cpf/)"
        cpf:String, 
        "Apenas dígitos, para fins de testes, pode gerar [nesse link](https://geradornv.com.br/gerador-cns/)"
        cns:String, 
        "Data de aniversário no formato `yyyy-mm-dd`"
        birthday: String, 
        "Categoria de profissional, um dedstes: `doc` para médicos, `nur` para enfermeira e `tec` para técnico de enfermagem"
        professionalCategory:String, 
        "UF do documento de conselho profissional"
        professionalDocumentUf:String, 
        "Número do documento de conselho profissional"
        professionalDocumentNumber:String
    }

    input PatientInput{
        name:String,
        "Sexo biológico binário `male` ou `female`"
        sex:String,
        "Data de aniversário no formato `yyyy-mm-dd`"
        birthday: String
        "Apenas dígitos, para fins de testes pode gerar [nesse link](https://geradornv.com.br/gerador-cpf/)"
        cpf:String, 
        "Apenas dígitos, para fins de testes, pode gerar [nesse link](https://geradornv.com.br/gerador-cns/)"
        cns:String!, 
        rg: String
        "Lista de doenças do paciente"
        comorbidities: [String]
        "Alergias"
        allergies: [String]
        address: AddressInput
    }

    type User {
        id: ID!
        email: String
        name: String
        birthday: String
        professionalCategory: String
        professionalDocumentUf: String
        professionalDocumentNumber: String
    }

    type UserToken {
        user: User
        token: String
    }

    type GeneratedPdf {
        base64Pdf: String
    }

    type Patient {
        id: ID!
        name: String
        cns: String
    }

    type Internment{
        id: ID!
        admissionDatetime: String
        patient: Patient
        hpi: String
        justification: String
        cid10Code: String
        createdAt: String
        evolutions: [Evolution]
        measures: [Measure]
        prescription: [Prescription]
    }


    type Evolution{
        id: ID!
        text: String
        professional: User
        createdAt: String
    }

    type Measure{
        id: ID!
        spO2: Int
        pain: Int
        sistolicBloodPressure: Int
        diastolicBloodPressure: Int
        cardiacFrequency: Int
        respiratoryFrequency: Int
        celciusAxillaryTemperature: Int
        glucose: Int
        fetalCardiacFrequency: Int
        professional: User
        createdAt: String
    }

    type RestingActivity{
        id: ID!
        name: String
    }

    type NursingActivity{
        id: ID!
        name: String
    }

    type Diet{
        id: ID!
        name: String
    }

    type Drug{
        id: ID!
        name: String
        usualDosage: String
        comment: String
        kind: String
    }

    type DrugPrescription{
        id: ID!
        drug: Drug
        dosage: String
        initialDate: String
        endingDate: String
    }

    type Prescription{
        resting: RestingActivity
        diet: Diet
        drugs: [DrugPrescription]
        nursing: [NursingActivity]
        createdAt: String
    }

    type Cid10 {
        code: String!
        description: String!
    }
''')

# Initialize query
query = QueryType()
# Initialize mutations
mutation = MutationType()

import app.graphql.resolvers
