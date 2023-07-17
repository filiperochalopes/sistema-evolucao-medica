from ariadne import gql

print_pdf_type_defs = gql(
    '''
    input Cid10Input {
        "Cid 10, usando o formato padrao de CID, max:4 min:3 caracteres"
        code: String!
        "Descrição da doença, max:44 min:5 caracteres"
        description: String!
    }

    input PrintAihSusPdfExtraInput {
        "TODO: Diagnóstico inicial no padrão do CID"
        secondaryDiagnosis: Cid10Input
    }

    input PrintFichaInternamentoExtraInput {
        "Tem seguro/plano de saúde outro além do SUS"
        hasAdditionalHealthInsurance: Boolean
    }

    input PrintRelatorioAltaExtraInput {
        "Orientações de Alta"
        orientations: String
        "No formato ISO %Y-%m-%dT%H:%M:%S"
        datetimeStamp: String
    }

    input TimestampExtraInput{
        "No formato ISO %Y-%m-%dT%H:%M:%S"
        startDatetimeStamp: String!
        "No formato ISO %Y-%m-%dT%H:%M:%S"
        endingDatetimeStamp: String!
    }

    input PrintFolhaPrescricaoExtraInput{
        "Intervalo de exibição dos dados"
        interval: TimestampExtraInput
    }

    input PrintFolhaEvolucaoExtraInput{
        "Intervalo de exibição dos dados"
        interval: TimestampExtraInput
    }

    input PrintBalancoHidricoExtraInput{
        "Intervalo de exibição dos dados"
        interval: TimestampExtraInput
    }

    input ProcedureApacInput{
        "Código do procedimento"
        code: String!
        "Nome do procedimento"
        name: String!
        "Quantidade do procedimento solicitado, default 1"
        quantity: Int
    }

    input PrintApacExtraInput{
        "Procedimento de Alta Complexidade para seleção da lista"
        procedure: ProcedureApacInput!
        "Opcional: Lista de procedimentos secundários"
        secondaryProcedures: [ProcedureApacInput]
        "Opcional: Diagnóstico que motiva o exame, em caso de não preenchimento será utilizado o da última evolução com CID"
        diagnosis: Cid10Input
        "Opcional: Diagnóstico secundário"
        secondaryDiagnosis: Cid10Input
        "Opcional: Causa associada"
        ssociatedCause: Cid10Input
        "Opcional: Observações, em caso de não preenchimento será preenchido com História da Doença Atual"
        observations: String
    }

    input PrintEvolucaoCompactaInput{
        prescriptionId: Int!
        evolutionId: Int!
        pendingsId: Int!
    }

    extend type Mutation {
        """
        Gera PDF para impressão, por meio de dados em banco da aplicação, de documento de AIH

        O profissional solicitante é capturado por meio do usuário logado e os demais dados por meio do número de internamento.
        """
        printPdf_AihSus(
            "Id do internamento do referência"
            internmentId: Int!
            extra: PrintAihSusPdfExtraInput
        ): GeneratedPdf

        """
        Gera PDF para impressão, por meio de dados em banco da aplicação, de documento de Folha de Rosto do Internamento

        O profissional solicitante é capturado por meio do usuário logado e os demais dados por meio do número de internamento.
        """
        printPdf_FichaInternamento(
            "Id do internamento do referência"
            internmentId: Int!
            extra: PrintFichaInternamentoExtraInput
        ): GeneratedPdf

        """
        Gera PDF para impressão, por meio de dados em banco da aplicação, de documento de Relatório de Alta
        """
        printPdf_RelatorioAlta(
            "Id do internamento do referência"
            internmentId: Int!
            extra: PrintRelatorioAltaExtraInput
        ): GeneratedPdf

        """
        Gera PDF para impressão, documento de Prescrição Médica
        """
        printPdf_FolhaPrescricao(
            "Id da prescrição a ser impressa"
            prescriptionId: ID!
        ): GeneratedPdf

        """
        Gera PDF para impressão, documento de Prescrição Médica
        """
        printPdf_FolhaEvolucao(
            "Id do internamento do referência"
            internmentId: Int!
            extra: PrintFolhaEvolucaoExtraInput
        ): GeneratedPdf

        """
        Gera PDF para impressão, documento de Evolucao Compacta
        """
        printPdf_EvolucaoCompacta(
            internmentId: Int!
            extra: PrintEvolucaoCompactaInput
        ): GeneratedPdf

        """
        Gera PDF para impressão, documento de Prescrição Médica
        """
        printPdf_BalancoHidrico(
            "Id do internamento do referência"
            internmentId: Int!
            extra: PrintBalancoHidricoExtraInput
        ): GeneratedPdf

        """
        Gera PDF para impressão, documento de Prescrição Médica
        """
        printPdf_Apac(
            "Id do internamento do referência"
            internmentId: Int!
            extra: PrintApacExtraInput!
        ): GeneratedPdf
    }
''')