from ariadne import gql, QueryType, MutationType

# Define type definitions (schema) using SDL
type_defs = gql('''
    type Query {
       users: [User]
       cid10: [Cid10!]
       state: [State!]
       restingActivities: [NamedObject!]
       diets: [NamedObject!]
       drugs: [Drug!]
       drugPresets: [DrugPreset!]
       nursingActivities: [NamedObject!]
       drugRoutes: [String]
       prescriptionTypes: [Option]
       prescription: [Prescription!]
       patient(id:ID, queryNameCnsCpf:String): Patient
       patients(queryNameCnsCpf:String): [Patient]
       internment(id:ID!): Internment
       internments(active:Boolean, cns:String): [Internment]
       myUser: User
       "ValueObject Alergia"
       allergies: [ValueObject]
       "ValueObject Comorbidade"
       comorbidities: [ValueObject]
       "ValueObject Procedimentos de Alta Complexidade"
       highComplexityProcedures: [Procedure]
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
        Atualização de senha por parte do próprio usuário
        """
        updatePassword(password: String!): User
        """
        Reset de senha direto na requisição para em caso de esquecimento ou perda de senha, a senha será resetada para "senha@123"
        """
        resetPassword(
            masterKey:String!,
            cns: String!): User
        """
        Criar paciente para cadastro do 
        """
        createPatient(patient: PatientInput): Patient
        """
        Atualizar paciente
        """
        updatePatient(id: ID!, patient:PatientInput): Patient
        """
        Cria internamento básico
        """
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
        """
        Atualiza internamento: Serve para poder encerrar um internamento. Ele registra a data de encerramento da internação.
        """
        updateInternment(
            id: ID!
            "Data de alta/encerramento do internamento yyyy-mm-dd HH:MM"
            finishedAt: String
            "Para reabrir um internamento para algum tipo de acréscrimo, evolução em fase de teste passe o parâmetro como true"
            reOpen: Boolean
        ): Internment
        """
        Cria uma evolução textual de enfermagem ou médica
        """    
        createEvolution(
            "Id do internamento do paciente para o qual a evolução está sendo inserida"
            internmentId: Int!, 
            "Texto da evolução médica ou de enfermagem"
            text:String,
            "Diagnóstico caso tenha alterado durante o internamento"
            cid10Code: String
            ): Evolution
        """
        Cria um registro de prescrição que pode ser atualizado no mesmo dia.
        """    
        createPrescription(
            "Id do internamento do paciente para o qual a evolução está sendo inserida"
            internmentId: Int!, 
            restingActivity: String
            diet: String
            drugs: [DrugPrescriptionInput]
            nursingActivities: [String]
            ): Prescription
        """
        Cria um registro de pendências, útil para passagem de plantão, quando o colega necessita saber 
        """    
        createPending(
            "Id do internamento do paciente para o qual a evolução está sendo inserida"
            internmentId: Int!, 
            restingActivity: String
            diet: String
            drugs: [DrugPrescriptionInput]
            nursingActivities: [String]
            ): Prescription
        """
        É responsável por salvar os sinais vitais de um paciente, relacionado a um internamento
        """
        createMeasure(
            "Id do internamento do paciente para o qual a evolução está sendo inserida"
            internmentId: Int!, 
            "Saturação de Oxigênio"
            spO2: Int
            "Escala de dor de 0 a 10"
            pain: Int
            "Pressão arterial sistólica, número de 1 a 3 dígitos"
            systolicBloodPressure: Int
            "Pressão arterial diastólica, número de 1 a 3 dígitos"
            diastolicBloodPressure: Int
            "Frequencia cardíaca, de dois a 3 dígitos"
            cardiacFrequency: Int
            "Frequencia respiratória, dois dígitos"
            respiratoryFrequency: Int
            "Temperatura axilar em graus celcius, dois dígitos"
            celciusAxillaryTemperature: Int
            "Medida de glicemia no padrão mg/dL, chamada também de HGT ou glicemia periférica"
            glucose: Int
            "Batimentos cardíacos fetais, para uso em gestantes. De dois a três dígitos"
            fetalCardiacFrequency: Int
            ): Measure
        """
        É responsável por salvar um registro único de balanço hídrico, relacionado a um internamento
        """
        createFluidBalance(
            "Id do internamento do paciente para o qual a evolução está sendo inserida"
            internmentId: Int!, 
            "Volume que foi recebido ou desprezado no momento"
            volumeMl: Int
            "Essa string deve ser, de preferência, uma das disponibilizadas para FluidBalanceDescription"
            description: String
        ): Boolean
    }

    input DrugPrescriptionInput{
        "Nome da medicação"
        drugName: String
        "No momento só existem 2 tipos: `atb`  para antibióticos, pois com esse o campo de data inicial de uso dedve ser obrigatória e `oth` para outros"
        drugKind: String
        "Modo de uso"
        dosage: String
        "Via de administração"
        route: String
        "No formato %Y-%m-%d %H:%M:%S"
        initialDate: String
        "No formato %Y-%m-%d %H:%M:%S"
        endingDate: String
    }

    input AddressInput{
        zipCode: String
        street:String
        number:String
        neighborhood:String
        complement:String
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
        birthdate: String, 
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
        "Dado muito relevante para cáculos, peso em quilos"
        weightKg: Float!
        "Data de aniversário no formato `yyyy-mm-dd`"
        birthdate: String
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
        birthdate: String
        professionalCategory: String
        professionalDocumentUf: String
        professionalDocumentNumber: String
    }

    type UserToken {
        user: User
        token: String
    }

    type Address{
        zipCode: String
        street:String
        number:String
        neighborhood:String
        complement:String
        city: String
        uf: String
    }

    type Patient {
        id: ID!
        name: String
        birthdate: String
        sex: String
        age: String
        cns: String
        address: Address
    }

    type State {
        ibge_code: ID!
        name: String
        uf: String!
    }

    type Internment{
        id: ID
        admissionDatetime: String
        patient: Patient
        hpi: String
        justification: String
        cid10: Cid10
        createdAt: String
        finishedAt: String
        evolutions: [Evolution]
        measures: [Measure]
        prescriptions: [Prescription]
    }


    type Evolution{
        id: ID!
        text: String
        professional: User
        createdAt: String
    }

    type Pending{
        text: String
    }

    type Measure{
        id: ID!
        spO2: Int
        pain: Int
        systolicBloodPressure: Int
        diastolicBloodPressure: Int
        cardiacFrequency: Int
        respiratoryFrequency: Int
        celciusAxillaryTemperature: Int
        glucose: Int
        fetalCardiacFrequency: Int
        professional: User
        createdAt: String
    }

    type NamedObject{
        id: ID!
        name: String
    }

    type ValueObject{
        id: ID!
        value: String
    }

    type Procedure{
        id: ID!
        name: String
        code: String
    }

    type Drug{
        id: ID!
        name: String
        usualDosage: String
        comment: String
        kind: String
    }

    type DrugPreset{
        name: String
        label: String
        drugs: [Drug]
        createdAt: String
    }

    type Option{
        "Identificador único da option"
        name: String,
        "Identificador Human readable"
        label: String
        "Seed que preenche o campo de options"
        querySeed: String
    }

    type DrugPrescription{
        id: ID!
        drug: Drug
        dosage: String
        route: String
        kind: String
        initialDate: String
        endingDate: String
    }

    type Prescription{
        id: ID!
        "Note que a atividade de repouso é única"
        restingActivity: NamedObject
        "Note que a dieta é única"
        diet: NamedObject
        drugPrescriptions: [DrugPrescription]
        nursingActivities: [NamedObject]
        createdAt: String
    }

    type PrescriptionUnit{
        type: String,
        name: String
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
