from ariadne import gql, QueryType, MutationType

# Define type definitions (schema) using SDL
type_defs = gql(
    '''
    type Query {
       users: [User]
       cid10(query:String, perPage:Int, page:Int): [Cid10!]
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
       patients(queryNameCnsCpf:String, perPage:Int, page:Int): [Patient]
       internment(id:ID!): Internment
       alembicVersion: AlembicVersion
       internments(active:Boolean, cns:String): [Internment]
       myUser: User
       "ValueObject Descrição de registro de Balanço Hídrico"
       fluidBalanceDescriptions: [ValueObject]
       "ValueObject Alergia"
       allergies: [ValueObject]
       "ValueObject Comorbidade"
       comorbidities: [ValueObject]
       "ValueObject Procedimentos de Alta Complexidade"
       highComplexityProcedures: [Procedure]
       "Query para fins de teste"
       hello: String
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
        Atualiza o usuário logado
        """
        updateMyUser(
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
            "Texto com relatório sucinto de pendências para o paciente"
            text: String
            ): Pending
        """
        É responsável por salvar os sinais vitais de um paciente, relacionado a um internamento
        """
        createMeasure(
            "Id do internamento do paciente para o qual a evolução está sendo inserida"
            internmentId: Int!, 
            "Saturação de Oxigênio, deve ser maior que 0 e menor que 100"
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
            celciusAxillaryTemperature: Float
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
        ): FluidBalance
    }

    input DrugPrescriptionInput{
        "Nome da medicação"
        drugName: String!
        "No momento só existem 2 tipos: `atb`  para antibióticos, pois com esse o campo de data inicial de uso dedve ser obrigatória e `oth` para outros"
        drugKind: String!
        "Modo de uso"
        dosage: String!
        "Via de administração"
        route: String!
        "No formato ISO %Y-%m-%dT%H:%M:%S"
        initialDate: String
        "No formato ISO %Y-%m-%dT%H:%M:%S"
        endingDate: String
    }

    input AddressInput{
            "CEP do endereco"
            zipCode: String
            "Nome da Rua"
            street:String
            "Complemento"
            complement:String
            "Bairro do endereco"
            neighborhood:String
            "Numero do endereco"
            number:String
            "Nome da Cidade"
            city: String!
            "Codigo IGBE do municipio"
            ibgeCityCode: String
            "Sigla do estado"
            uf: String!
            "Pontos de Referencia"
            reference: String
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
        birthdate: String, 
        "Categoria de profissional, um dedstes: `doc` para médicos, `nur` para enfermeira e `tec` para técnico de enfermagem"
        professionalCategory:String, 
        "UF do documento de conselho profissional"
        professionalDocumentUf:String, 
        "Número do documento de conselho profissional"
        professionalDocumentNumber:String
    }

    input PatientInput{
        "Nome completo do paciente"
        name:String!,
        "Nome completo da mãe do paciente"
        motherName: String!
        "Sexo biológico binário `male` ou `female`"
        sex:String!,
        "Dado muito relevante para cáculos, peso em quilos"
        weightKg: Float!
        "Data de nascimento no formato `yyyy-mm-dd`"
        birthdate: String!
        "Apenas dígitos, para fins de testes pode gerar [nesse link](https://geradornv.com.br/gerador-cpf/)"
        cpf:String, 
        "Apenas dígitos, para fins de testes, pode gerar [nesse link](https://geradornv.com.br/gerador-cns/)"
        cns:String!, 
        "Apenas dígito do Documento de Registro Geral"
        rg: String
        "Telefone de contato do paciente, de preferência WhatsApp"
        phone: String!
        "Nacionalidade do Paciente"
        nationality: String
        "Etnia do Paciente"
        ethnicity: String
        "Lista de doenças do paciente"
        comorbidities: [String]
        "Alergias"
        allergies: [String]
        "Dados de endereço"
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

    type AlembicVersion{
        version: String
    }

    type User {
        id: ID!
        email: String
        name: String
        cns: String
        cpf: String
        rg: String
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
        rg: String
        cpf: String
        phone: String
        weightKg: Float
        comorbidities: [ValueObject]
        allergies: [ValueObject]
        motherName: String
        address: Address
    }

    type FluidBalance{
        id: ID!
        volumeMl: Int
        description: ValueObject    
        createdAt: String
        professional: User
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
        pendings: [Pending]
        fluidBalance: [FluidBalance]
    }


    type Evolution{
        id: ID!
        text: String
        professional: User
        createdAt: String
    }

    type Pending{
        id: ID!
        text: String
        professional: User
        createdAt: String
    }

    type Measure{
        id: ID!
        spO2: Int
        pain: Int
        systolicBloodPressure: Int
        diastolicBloodPressure: Int
        cardiacFrequency: Int
        respiratoryFrequency: Int
        celciusAxillaryTemperature: Float
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
        usualRoute: String
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
        initialDate: String
        endingDate: String
    }

    type Prescription{
        id: ID!
        "Note que a atividade de repouso é única"
        restingActivity: NamedObject
        "Note que a dieta é única"
        diet: NamedObject
        "Prescrições de medicamentos"
        drugPrescriptions: [DrugPrescription]
        "Atividades de enfermagem"
        nursingActivities: [NamedObject]
        "Timestamp ISO de criação da prescrição"
        createdAt: String
        "Profissional que criou a prescrição"
        professional: User
    }

    type Cid10 {
        "Cid 10, usando o formato padrao de CID, max:4 min:3 caracteres"
        code: String!
        "Descrição da doença, max:44 min:5 caracteres"
        description: String!
    }
''')

# Initialize query
query = QueryType()
# Initialize mutations
mutation = MutationType()

import app.graphql.resolvers