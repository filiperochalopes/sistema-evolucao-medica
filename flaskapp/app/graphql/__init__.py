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

        "Criação de documento de Solicitacao de Exames"
        generatePdf_SolicitExames(
            "Nome do paciente, max:70 min:7 caracteres"
            patientName: String!,
            "CNS do paciente"
            patientCns: String!,
            "Data de nascimento do paciente no formato DD/MM/YYYY"
            patientBirthday: String!,
            "Endereco do paciente, max: 216 min:7 caracteres"
            patientAdress: String!,
            "Motivo da Solicitacao, max: 216 min:7 caracteres"
            solicitationReason: String!,
            "Nome do profissional Solicitante, max:29 min:7 caracteres"
            profSolicitor: String!,
            "Data da Solicitacao no formato DD/MM/YYYY"
            solicitationDatetime: String!,
            "Exames solicitados"
            exams: String!,
            "Nome do profissional autorizador, max:29 min:7 caracteres"
            profAuthorized: String,
            "Nome do paciente no final do documento, esse campo fica no fim do documento e tem um tamanho maximo diferente. max:46 min:7 caracteres"
            documentPacientName: String,
            "Data da Autorizacao no formato DD/MM/YYYY"
            autorizationDatetime: String,
            "Data do paciente, tambem no campo inferior no formato DD/MM/YYYY"
            documentPacientDate: String,
        ): GeneratedPdf

        "Criação de documento de Solicitacao de Mamografia"
        generatePdf_SolicitMamografia(
            "CNS do paciente"
            patientCns: String!,
            "Data de nascimento do paciente no formato DD/MM/YYYY"
            patientBirthday: String!,
            """
            Fez mamograma antes, envie uma lista com o primeiro valor ['SIM'/'NAO', 'Ano do mamograga']
            Exemplo: 
                ['SIM', '2020']
                ['NAO', null]
            """
            mammogramBefore: [String]!,
            "Idade do paciente"
            patientAge: Int!,
            "Nome do Paciente, max:42 min:7 caracteres"
            patientName: String!,
            "Nome da mae do paciente, max:42 min:7 car"
            patientMotherName: String!,
            """
            Possui nodulo. Opcoes:
                - "SIMDIR" -> Sim direita
                - "SIMESQ" -> Sim esquerda
                - "NAO"    -> Nao possui
            """
            noduleLump: String!,
            """
            Tem risco elevado. Opcoes:
                - "SIM"
                - "NAO"
                - "NAOSABE"
            """
            highRisk: String!,
            """
            Ja foi examinada antes. Opcoes:
                - "SIM"
                - "NUNCA"
                - "NAOSABE"
            """
            examinatedBefore: String!,
            "Nome da Unidade de Saudes, max: 42 min:7"
            healthUnitName: String,
            "UF em que a Unidade de Saude esta, somente a sigla 2 caracteres"
            healthUnitAdressUf: String,
            "Nome da cidade aonde esta a unidade de saude, max:14 min:4"
            healthUnitAdressCity: String,
            "Apelido do paciente, max:18 min:4 caracteres" 
            patientSurname: String,
            "Endereco do Paciente, max:42 min:7 caracteres"
            patientAdress: String,
            "Complemento do endereco do paciente, max:25 min:7 caracteres"
            patientAdressAdjunct: String,
            "Bairro do endereco do paciente, max:14 min:7 caracteres"
            patientAdressNeighborhood: String,
            "Referencia do endereco do paciente, max:33 min:4 caracteres"
            patientAdressReference: String,
            "Cidade do endereco do paciente, max:15 min:4 caracteres"
            patientAdressCity: String,
            "CEP do endereco do paciente, envie somente numeros sem formatacao, Exemplo: XXXXXXXX"
            patientAdressCep: String,
            "Numero de telefone do paciente, envie somente textos sem formatacao. Deve ter 10 digitos somente."
            patientPhonenumber: String,
            """
            Ja fez radioterapia antes, lista com opcoes e ano caso seja sim.
            Opcoes:
                -'SIMDIR' -> Sim mama direita, deve inserir o ano, ex: ["SIMDIR", "2019"] 
                -'SIMESQ' -> Sim mama esquerda, deve inserir o ano, ex: ["SIMESQ", "2019"] 
                -'NAO' -> Nao, nao precisa enviar o ano, ex: ["NAO", null]
                -'NAOSABE' -> Nao sabe, nao precisa enviar o ano, ex: ["NAO", null]
            """
            radiotherapyBefore: [String],
            "Ja fez cirurgia nas mamas antes, utilize o SurgeryBeforeInput"
            breastSurgeryBefore: SurgeryBeforeInput,
            "CNES da unidade de saude"
            healthUnitCnes: Int,
            "Numero do protocolo, max:23 min:1 caracteres"        
            protocolNumber: String,
            "CPF do paciente, envie com o input DocumentInput"
            patientDocumentCpf: DocumentInput,
            "Numero do endereco do paciente, max: 6 digitos"
            patientAdressNumber: Int,
            "UF do endereco do paciente, envie somente a sigla"
            patientAdressUf: String,
            "Codigo do IBGE do Município da Unidade de Saude"
            healthUnitCityIbgeCode: String,
            "Numero do protocolo, max: 10 caracteres"
            documentChartNumber: Int,
            "Sexo do paciente, envie M ou F"
            patientSex: String,
            "Nacionalidade do paciente"
            patientNationality: String,
            "Codigo do IBGE do Município do paciente"
            pacientCityIbgeCode: String,
            """
            Etinia do paciente, envie uma lista com algumas das opcoes, e caso seja indigena especificar o nome com no max: 10 caracteres. Opcoes:
            'BRANCA','PRETA', 'PARDA', 'AMARELA', 'INDIGENA'.
            Exemplos:
                ["BRANCA", null]
                ["INDIGENA", "Guarani"]
            """
            patientEthnicity: [String],
            "Nome do Profissional Solicitante, max: 23 min:7 caracteres"
            profSolicitorName: String!,
            "Data da Solicitacao no formato DD/MM/YYYY"
            solicitationDatetime: String!,
            "Numero do exame, max: 16 caracteres"
            examNumber: Int,
            """
            Mamografia de rasteramento. Opcoes:
                "POPALVO"       -> Populacao alvo
                "RISCOELEVADO"  -> Populacao de risco elevado
                "JATRATADO"     -> Paciente ja tratado de cancer de mama
            """
            trackingMammogram: String,
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

    input SurgeryBeforeInput{
        "Nao fez nenhuma Cirurgia nas mamas, marque TRUE caso ela nunca tenha feito nenhuma cirugia, isso faz todos os outros serem descartados. Caso contario marque FALSE"
        didNot: String,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        biopsiaInsinonal: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        biopsiaExcisional: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        centraledomia: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        segmentectomia: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        dutectomia: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        mastectomia: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        mastectomiaPoupadoraPele: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        mastectomiaPoupadoraPeleComplexoAreolo: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        linfadenectomiaAxilar: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        biopsiaLinfonodo: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        reconstrucaoMamaria: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        mastoplastiaRedutora: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null]"""
        indusaoImplantes: [String]!
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
