from ariadne import gql, QueryType, MutationType

# Define type definitions (schema) using SDL
type_defs = gql('''
    type Query {
       users: [User]
       cid10: [Cid10!]
       patients: [Patient]
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
