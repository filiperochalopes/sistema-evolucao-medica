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
    }
''')