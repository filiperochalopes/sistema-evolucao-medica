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
    }

    input AddressInput{
        zipCode: String
        street:String
        complement:String
        number:String
        city: String!
        uf: String!
    }

    input ProcedimentoInput{
        "Nome do procedimento, max:50 min: 7 caracteres"
        name: String!
        "Codigo do procedimento, deve ter 10 caracteres"
        code: String!,
        "Quantidade do procedimento, max: 8 digitos"
        quant: Int!
    }

    input SurgeryBeforeInput{
        "Nao fez nenhuma Cirurgia nas mamas, marque TRUE caso ela nunca tenha feito nenhuma cirugia, isso faz todos os outros serem descartados. Caso contario marque FALSE"
        didNot: String!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        biopsiaInsinonal: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        biopsiaExcisional: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        centraledomia: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        segmentectomia: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        dutectomia: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        mastectomia: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        mastectomiaPoupadoraPele: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        mastectomiaPoupadoraPeleComplexoAreolo: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        linfadenectomiaAxilar: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        biopsiaLinfonodo: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        reconstrucaoMamaria: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
        mastoplastiaRedutora: [String]!,
        """Lista com 2 anos, o primeiro para o lado esquerdo e o segundo para o lado direito, null para casa nao tenha cirugia. Ex: ["2020", null] ou somente [null]"""
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

    input DiagnosticMamogramInput{
        "Exame clinico, utilize o input ExameClinicoOpcoesMamasInput"
        exameClinico: ExameClinicoOpcoesMamasInput,
        """
        Controle Radiologico, utilize o input OpcoesMamasInput, as opcoes sao
        'nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo'
        """
        controleRadiologico: OpcoesMamasInput,
        """
        Lesao Diagnostico, utilize o input OpcoesMamasInput, as opcoes sao:
        'nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo'
        """
        lesaoDiagnostico: OpcoesMamasInput,
        "Avaliacao da Resposta de QT, envie uma lista de String com Direito e Esquerda, Exemplos: ['direita', 'esquerda']  / [null, 'esquerda'] / [null, null]"
        avaliacaoResposta: [String],
        "Revisao de mamogramafia com lesao, opcoes: '0', '3', '4', '5'"
        revisaoMamografiaLesao: OpcoesMamasInput,
        "Controle de lesao apos biopsia de fragmento, opcoes: 'nodulo', 'microca', 'assimetria_focal', 'assimetria_difusa', 'area_densa', 'distorcao', 'linfonodo'"
        controleLesao: OpcoesMamasInput

    }

    input OpcoesMamasInput{
        "Lista com as opcoes da mama direita"
        direta: [String]!,
        "Lista com as opcoes da mama esquerda"
        esquerda: [String]!
    }

    input ExameClinicoOpcoesMamasInput{
        "Lista com as opcoes da mama direita"
        direta: ExameClinicoInput!,
        "Lista com as opcoes da mama esquerda"
        esquerda: ExameClinicoInput!
    }

    input ExameClinicoInput{
        "Lesao Papilar"
        papilar: Boolean,
        "Descarga papilar, as opcoes: 'CRISTALINA', 'HEMORRAGICA'"
        descargaPapilar: [String],
        "Nodulo localizacao opcoes: 'QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'"
        nodulo: [String],
        "Espessamento localizacao, opcoes: 'QSL', 'QIL', 'QSM', 'QIM', 'UQLAT', 'UQSUP', 'UQMED', 'UQINF', 'RRA', 'PA'"
        espessamento: [String],
        "Linfonodo palpavel, opcoes: 'AXILAR', 'SUPRACLAVICULAR'"
        linfonodoPalpavel: [String]
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
