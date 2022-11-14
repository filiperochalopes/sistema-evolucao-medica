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
            establishmentSolitcName: String!,
            "CNES do Estabelecimento Solicitante"
            establishmentSolitcCnes: Int!, 
            "Nome do Estabelecimento Executante, max:82 min:8 caracteres"
            establishmentExecName: String!, 
            "CNES do Estabelecimento Executante"
            establishmentExecCnes: Int!, 
            "Nome do paciente, max:79 min:7 caracteres"
            patientName: String!, 
            "Número do Cartão do SUS do paciente"
            patientCns: Int!,
            "Data de nascimento do paciente, em timestamp SEM fusohorario (utilizando o padrao UTC)"
            patientBirthday: String!,
            "Sexo do Paciente, opcao M ou F."
            patientSex: String!,
            "Nome da Mae do paciente, max:70 min:7 caracteres"
            patientMotherName: String!, 
            "Endereco do paciente, somente 'rua, numero, bairro', max: 101 min:7 caracteres"
            patientAdress: String!, 
            "Cidade do paciente, max:58 min:7 caracteres"
            patientAdressCity: String!, 
            "Codigo IBGE do municipio do paciente"
            patientAdressCityIbgeCode: Int!,
            "Sigla do estado, UF, da cidade do paciente, somente estados do Brasil"
            patientAdressUF: String!,
            "CEP do endereço do paciente"
            patientAdressCEP: Int!,
            "Principais sintomas e sintomas clinicos, max:1009 min:5 caracteres"
            mainClinicalSignsSymptoms: String!,
            "Condicoes que justificam a internacao, max:403 min:5 caracteres"
            conditionsJustifyHospitalization: String!,
            "Diagnostico inicial, max:44 min:5 caracteres"
            initialDiagnostic: String!,
            "Cid 10 princical, usando o formato padrao de CID, max:4 min:3 caracteres"
            principalCid10: String!, 
            "Procedimento solicitado, max:65 min:6 caracteres"
            procedureSolicited: String!,
            "Codigo do procedimento solcitado, deve ter exatamente 10 caracteres"
            procedureCode: String!,
            "Nome da clinica, max:18 min:6 caracteres"
            clinic: String!, 
            "Carater da internacao, max:19 min:6 caracteres"
            internationCarater: String!, 
            "Documento do profissional solicitante, cns ou cpf, a api python o trata como dicionario, entao envie como uma string no formato '{'CNS':928976954930007}', a primeira e o nome do documento, e o seguinte e o numero do documento como inteiro"
            profSolicitorDocument: String!, 
            "Nome do profissional solicitante, max:48 min:8 caracteres"
            profSolicitorName: String!,
            "Data e hora da solicitacao, somente dia/mes/ano"
            solicitationDatetime: String!,
            "Nome do profissional autorizador, max:48 min:8 caracteres" 
            autorizationProfName: String!,
            "Codigo da organizacao emissora, esse dado fica no campo de autorizacao, max:17 min:2 caracteres"
            emissionOrgCode: String!, 
            "Documento do profissional autorizador, cns ou cpf, a api python o trata como dicionario, entao envie como uma string no formato '{'CNS':928976954930007}', a primeira e o nome do documento, e o seguinte e o numero do documento como inteiro"
            autorizatonProfDocument: String!,
            "Data e hora da autorizacao, somente dia/mes/ano"
            autorizatonDatetime: String!,
            "Numero da autorizacao de internacao hospitalar, no maximo 18 digitos"
            hospitalizationAutorizationNumber: Int!,
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
            "Data do documento no formato DD/MM/YYYY"
            documentDatetime: String!,
            "Nome do paciente, max:34 min:7 caracteres"
            patientName: String!,
            """
            List de precicoes enviadas pelo medico, voce pode adicionar mais de uma utilizando uma lista de PrescriptionInput, veja as docs do input PrescriptionInput para mais informações"
            """
            prescription: [PrescriptionInput]!
        ): GeneratedPdf
    
        "Criação de documento de Relatorio de Alta"
        generatePdf_RelatorioAlta(
            "Data do documento no formato DD/MM/YYYY HH:mm"
            documentDatetime: String!,
            "Nome do paciente, max:64 min:7 caracteres"
            patientName: String!,
            "CNS do paciente, envie sem formatacao, apenas numeros. Exemplo XXXXXXXXXXXXXXX"
            patientCns: String!,
            "Data de Nascimento do paciente no formato DD/MM/YYYY"
            patientBirthday: String!,
            "Sexo do Paciente, opcao M ou F."
            patientSex: String!,
            "Nome da Mae do paciente, max:69 min 7 caracteres"
            patientMotherName: String!,
            "Documento do paciente, CPF ou RG, utilize o input DocumentInput"
            patientDocument: DocumentInput!,
            "Endereco do paciente, max:63 min:7 caracteres"
            patientAdress: String!,
            "Nome do Medico, max:49 min:7 caracteres"
            doctorName: String!,
            "CNS do medico, envie sem formatacao, apenas numeros. Exemplo XXXXXXXXXXXXXXX"
            doctorCns: String!,
            "CRM do medico, max:13 min:11"
            doctorCrm: String!,
            "Evolucao do paciente, max: 2100 min:10 caracteres"
            evolution: String!,
            "Orientacoes para o paciente, max:800 min:10 caracteres"
            orientations: String
        ): GeneratedPdf

        "Criação de documento de LME"
        generatePdf_Lme(
            "Nome do estabelecimento Solicitante, max:65 min:8 caracteres"
            establishmentSolitcName: String!,
            "CNES do estabelecimento Solicitante"
            establishmentSolitcCnes: Int!
            "Nome do paciente, max:79 min:7 caracteres"
            patientName: String!,
            "Nome da Mae do paciente, max:79 min:7 caracteres"
            patientMotherName: String!,
            """
            Peso do paciente, numero inteiro no maximo 3 digitos, sera entendido como um valor total.
            Exemplo:
                patientWeight: 54  // sera entedido como 54kg
            """
            patientWeight: Int!,
            """
            Altura do paciente, numero inteiro no maximo 3 digitos (e inteiro pois sera formatado com espacos e virgula depois no pdf)
            Exemplo: 
                patientHeight: 180 // sera entendido como 1.80 metros
            """
            patientHeight: Int!,
            "Cid 10 do diagnostico"
            cid10: String!,
            "Anamnese, max:485 min: 5 caracteres"
            anamnese: String!,
            "Nome do profissional solicitante, max:45 min:8 caracteres"
            profSolicitorName: String!,
            "Data da solicitacao no formato DD/MM/YYYY"
            solicitationDatetime: String!,
            "Documento do profissional solicitante, CNS ou CPF, utilize o DocumentInput"
            profSolicitorDocument: DocumentInput!,
            """
            Atestado de capacidade, envie como uma list com 2 opcoes. ['Sim'/'Nao', 'Nome do responsavel]. 
            Nome do responsavel deve ter no max:46 min:5(caso a opcao seja Sim) caracteres
            """
            capacityAttest: [String]!,
            """
            Informacoes de quem preencheu, envie um lista com as seguintes opcoes:
            [ 
                'PACIENTE'/'MAE'/'RESPONSAVEL'/'MEDICO'/'OUTRO',
                'Nome do outro', somente se for selecionado max: 42 min:5 caracteres
                '{'cpf':'12345678900'}, documento do outro, envie nesse formato o cpf'
            ]
            Exemplos:
                filledBy: ['PACIENTE', null, null]
                filledBy: ['OUTRO', 'Nome do Outro', "{'cpf':'12345678900'}"]
            """
            filledBy: [String]!,
            """
            Etinia do paciente, envie alguma dessas opcoes: 'BRANCA','PRETA', 'PARDA', 'AMARELA', 'INDIGENA', 'SEMINFO', 'INFORMAR'.
            Caso a opcaos escolhida for INFORMAR deve ser passar o texto, com no max: 31 e min: 4 caracteres.
            Exemplo:
                patientEthnicity: ['Parda', null]
                patientEthnicity: ['Informar', 'Etinia']

            """
            patientEthnicity: [String]!,
            """
            Informacoes do tramento anterior ou do tratamento atual, envie uma list com as opcoes ['SIM'/'NAO', 'Tratamento anterior'], Envie um texto com o tratamento anterior ou  caso a opcao SIM for escolhida, max: 170 min:4 caracteres. 
            Exemplo:
                previousTreatment: ['Nao', null]
                previousTreatment: ['Sim', 'tratamento anterior']
            """
            previousTreatment: [String]!,
            "Diagnostico, max: 84 min:4 caracteres"
            diagnostic: String,
            "Documento do Paciente, CPF, envie um DocumentInput"
            patientDocument: DocumentInput,
            "Email do paciente, max:62 min: 8 caracteres"
            patientEmail: String,
            """
            Numero de telegone para contato, envie no maximo 2 numeros, envie 10 digitos (contanto com o DDD)
            Exemplo: ["1034567654", "111234567890"]
            """
            contactsPhonenumbers: [String],
            """
            Lista com os medicamentos Solicitados, envie uma lista com no maximo 5 MedicineInput. 
            """  
            medicines: [MedicineInput]
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

    input PrescriptionInput{
        "Nome do medicamento, ele e o amount nao podem ser maiores que 61 caracteres juntos. Exemplo: Dipirona 500mg"
        medicineName: String
        "quantidade do medicamento, isso e medicineName nao podem ser maiores que 61 caracteres juntos. Exemplo: 4 comprimidos"
        amount: String
        "Modo de uso, max: 244 caracteres"
        useMode: String
    }

    input MedicineInput{
        "Nome do medicamento, max: 65 min:4 caracteres"
        medicineName: String
        "quantidade do medicamento no primeiro mes, max: 9 carateres, min:1"
        quant1month: String
        "quantidade do medicamento no segundo mes, max: 9 carateres, min:1"
        quant2month: String
        "quantidade do medicamento no terceiro mes, max: 8 carateres, min:1"
        quant3month: String
    }

    input DocumentInput{
        "CPF do Paciente sem formatacao, apenas numeros. Exemplo: xxxxxxxxxxx"
        cpf: String
        "RG do Paciente sem formatacao, apenas os numeros XXXXXXXXXXXX"
        rg: String
        "CNS do Paciente sem formatacao, apenas numeros. Exemplo: xxxxxxxxxxxxxxx"
        cns: String
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
