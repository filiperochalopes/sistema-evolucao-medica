from ariadne import gql

pdfs_schema_type_defs = gql(
    '''
    input ProfessionalInput{
        name: String!
        "Categoria do Profissional, envie 'M' ou 'E', sendo respectivamente Medico/a ou Enfermeiro/a"
        category: String!
        "Documento do profissional, se for medico envie o CRM no formato '12345/UF', case seja enfermeiro, envie somente o numero do COREM"
        document: String!
    }

    input EvolutionInput{
        "Data da criacao. String no formato de dd/mm/aaaa hh:mm"
        createdAt: String!
        "Categoria da evolucao. Opcoes M, E1, E2, E3 (medica, enfermagem1, enfermagem2, enfermagem3). Lembre-se que o nunmero apos o 'E' se refere ao bloco presente no documento, o bloco 2 possui um limite maior de caracteres"
        category: String!
        "Descricao da evolucao"
        description: String!
        "Profissional responsavel"
        professional: ProfessionalInput!
    }

    input MeasureInput{
        "Valores de saturação periférica de oxigênio de 20 a 99"
        spO2: Int
        "Escala de dor de 0 a 10"
        pain: Int
        "Pressão arterial sistólica"
        sistolicBloodPressure: Int
        "Pressão arterial diastólica"
        diastolicBloodPressure: Int
        "Frequencia cardiaca em bpm"
        cardiacFrequency: Int
        "Frequencia respiratoria em ipm"
        respiratoryFrequency: Int
        "Temperatura Axilar em graus Celsius"
        celciusAxillaryTemperature: Int
        "Aferição de glicemia capilar, pode ser um número de 0 a 500, ou 'HI'"
        glucose: String
        "Frequencia cardiaca fetal"
        fetalCardiacFrequency: Int
        "Data da criacao. String no formato de dd/mm/aaaa hh:mm"
        createdAt: String!
        "Profissional responsavel"
        professional: ProfessionalInput!
    }

    input FluidBalanceInput{
        "Data da criacao. String no formato de dd/mm/aaaa hh:mm"
        createdAt: String!
        "Valor em mililitros (ml), esse valor pode ser negativo ou positivo"
        value: Int!
        "Descricao"
        description: String!
    }

    input PrescriptionItemInput{
        "Medicação, Cuidados de Enfermagem, Repouso ou Dieta"
        type: String
        "Texto principal da prescrição, pode ser a medicação e forma de uso de uma medicação ou instruções de cuidados para enfermagem"
        description: String!
        "Seguintes exclusivos para o tipo de medicação"
        route: String
        "Em caso de ser um antibiótico ou AINES é necessário estabelecer data de início"
        startDate: String
        "Em caso de ser um antibiótico ou AINES é interessante estabelecer data de fim"
        endingDate: String
    }

    input EstablishmentInput{
        "Nome do Estabelecimento max:82 min:7 caracteres"
        name: String
        "CNES do Estabelecimento"
        cnes: String
    }

    type GeneratedPdf {
        base64Pdf: String
    }

    extend type Mutation {
        "Gerando página de evolução, sendo que na primeira página sempre mostra a tabela de evolução"
        generatePdf_FolhaEvolucao(
            "Data da criacao. String no formato de dd/mm/aaaa"
            createdAt: String!
            "Nome do paciente, o sistema ira abreviar os nomes do meio, exemplo: Joao da Silva -> JOAO D. SILVA"
            patientName: String!
            "Evolucoes, no maximo 4"
            evolutions: [EvolutionInput]
            "Medicoes"
            measures: [MeasureInput]
        ): GeneratedPdf

        "Gerando página de evolução, sendo que na primeira página sempre mostra a tabela de evolução"
        generatePdf_FolhaPrescricao(
            "Data da criacao. String no formato de dd/mm/aaaa hh:mm"
            createdAt: String!
            "Data da impressao. String no formato de dd/mm/aaaa hh:mm"
            printedAt: String
            "Nome do paciente, o sistema ira abreviar os nomes do meio, exemplo: Joao da Silva -> JOAO D. SILVA"
            patientName: String!
            prescriptions: [PrescriptionItemInput]
        ): GeneratedPdf

        "Gerando página de evolução, sendo que na primeira página sempre mostra a tabela de evolução"
        generatePdf_BalancoHidrico(
            "Data da criacao. String no formato de dd/mm/aaaa"
            createdAt: String!
            "Nome do paciente, o sistema ira abreviar os nomes do meio, exemplo: Joao da Silva -> JOAO D. SILVA"
            patientName: String!
            "Peso do paciente em kg"
            patientWeight: Int!
            fluidBalance: [FluidBalanceInput]
        ): GeneratedPdf
        
        "Criação de documento de AIH"
        generatePdf_AihSus(
            "Dados do Estabelecimento Solicitante"
            establishmentSolitc: EstablishmentInput!,
            "Dados do Estabelecimento Executante"
            establishmentExec: EstablishmentInput, 
            "Dados do Paciente"
            patient: PatientInput!
            mainClinicalSignsSymptoms: String!,
            "Condicoes que justificam a internacao, max:403 min:5 caracteres"
            conditionsJustifyHospitalization: String!,
            "Diagnostico inicial, max:44 min:5 caracteres"
            initialDiagnostic: String!,
            "Cid 10 princical, usando o formato padrao de CID, max:4 min:3 caracteres"
            principalCid10: String!, 
            "Procedimento solicitado, max:65 min:6 caracteres"
            procedureSolicited: String!,
            "Codigo do procedimento solicitado, deve ter exatamente 10 caracteres"
            procedureCode: String!,
            "Nome da clinica, max:18 min:6 caracteres"
            clinic: String!, 
            "Carater da internacao, max:19 min:6 caracteres"
            internationCarater: String!, 
            "Documento do profissional solicitante, cns ou cpf, utilize o input DocumentInput"
            profSolicitorDocument: DocumentInput!, 
            "Nome do profissional solicitante, max:48 min:8 caracteres"
            profSolicitorName: String!,
            "Data e hora da solicitacao, somente dia/mes/ano"
            solicitationDatetime: String!,
            "Nome do profissional autorizador, max:48 min:8 caracteres" 
            profAutorizationName: String!,
            "Codigo da organizacao emissora, esse dado fica no campo de autorizacao, max:17 min:2 caracteres"
            emissionOrgCode: String!, 
            "Documento do profissional autorizador, cns ou cpf, utilize o input DocumentInput"
            autorizatonProfDocument: DocumentInput!,
            "Data e hora da autorizacao, somente dia/mes/ano"
            autorizatonDatetime: String!,
            "Numero da autorizacao de internacao hospitalar, no maximo 18 digitos"
            hospitalizationAutorizationNumber: String!,
            "Resultados de exames, max: 403 min:5 caracteres"
            examResults: String,
            "Numero do Prontuario, max:20 min:1 caracteres"
            chartNumber: String, 
            "Nome do responsavel do paciente, max:70 min:7 caracteres"
            patientResponsibleName: String, 
            "Numero de telefone da mae do paciente, envie somente numeros, 10 ou 11 digitos"
            patientMotherPhonenumber: String, 
            "Numero de telefone do Responsavel do paciente, envie somente numeros, 10 ou 11 digitos"
            patientResponsiblePhonenumber: String,
            "CID10 secundario"
            secondaryCid10: String,
            "CID10 causas associadas"
            cid10AssociatedCauses: String,
            """
            Tipo do acidente, opcoes:
                'TRAFFIC'   -> Acidente de Transito
                'WORK'      -> Acidente de Trabalho tipico
                'WORK_PATH' -> Acidente de Trabalho trajeto
            """
            acidentType: String,
            "CNPJ da Seguradora, envie somente numeros"
            insuranceCompanyCnpj: String,
            "Codigo do bilhete da seguradora, somente numero max 16 digitos"
            insuranceCompanyTicketNumber: String, 
            "Serie da seguradora, max:10 min:1 caracteres"
            insuranceCompanySeries: String,
            "CNPJ da Empresa, somente numeros"
            companyCnpj: String,
            "CNAE da empresa, somente numeros"
            companyCnae: Int,
            "CBOR da empresa, somente numeros"
            companyCbor: Int,
            """
            Vinculo com a previdencia, Opcoes:
                'WORKER'      -> Empregado
                'EMPLOYER'    -> Empregador
                'AUTONOMOUS'  -> Autonomo
                'UNEMPLOYED'  -> Desempregado
                'RETIRED'     -> Aposentado
                'NOT_INSURED' -> Nao Segurado
            """
            pensionStatus: String
        ): GeneratedPdf

        "Criação de documento de APAC"
        generatePdf_Apac(
           "Dados do Estabelecimento Solicitante"
            establishmentSolitc: EstablishmentInput!,
            "Dados do Estabelecimento Executante"
            establishmentExec: EstablishmentInput, 
            "Dados do Paciente"
            patient: PatientInput!
            "Procedimento Solicitado, utilize o input ProcedimentoInput"
            mainProcedure: ProcedimentoInput!,
            "Procedimentos Secundarios, no maximo 5, envie uma lista de ProcedimentoInput"
            secondariesProcedures: [ProcedimentoInput],
            "Numero de telefone da mae do paciente, envie somente numeros, 10 ou 11 digitos"
            patientMotherPhonenumber: String, 
            "Nome do responsavel do paciente, max:67 min:7 caracteres"
            patientResponsibleName: String, 
            "Numero de telefone do Responsavel do paciente, envie somente numeros, 10 ou 11 digitos"
            patientResponsiblePhonenumber: String,
            "Cor do Paciente, max:10 min:4 caracteres"
            patientColor: String, 
            "Numero do Prontuario, max:14 min:1 caracteres"
            documentChartNumber: String,
            "Descricao do diagnostico do procedimento solicitado. max: 55 min: 4 caracteres"
            procedureJustificationDescription: String,
            "Cid 10 principal do diagnostico"
            procedureJustificationMainCid10: String,
            "Cid 10 secundario do diagnostico"
            procedureJustificationSecCid10: String,
            "Cid 10 de causas associadas do diagnostico"
            procedureJustificationAssociatedCauseCid10: String,
            "Observacoes do diagnostico, max: 776 min: 5 caracteres"  
            procedureJustificationComments: String,
            "Documento do profissional solicitante, cns ou cpf, utilize o input DocumentInput"
            profSolicitorDocument: DocumentInput, 
            "Nome do profissional solicitante, max:48 min:5 caracteres"
            profSolicitorName: String,
            "Data da solicitacao, somente dia/mes/ano"
            solicitationDatetime: String,
            "Nome do profissional autorizador, max:46 min:5 caracteres" 
            profAutorizationName:String,
            "Codigo da organizacao emissora, esse dado fica no campo de autorizacao, max:16 min:2 caracteres"
            emissionOrgCode: String, 
            "Documento do profissional autorizador, cns ou cpf, utilize o input DocumentInput"
            autorizatonProfDocument: DocumentInput,
            "Data da autorizacao, somente dia/mes/ano"
            autorizatonDatetime: String,
            "Data da Assinatura, somente DD/MM/YYYY"
            signatureDatetime: String,
            "Data do inicio do periodo de Validade da APAC, utilize a data no formato DD/MM/YYYY"
            validityPeriodStart: String,
            "Data do fim do periodo de Validade da APAC, utilize a data no formato DD/MM/YYYY"
            validityPeriodEnd: String
        ): GeneratedPdf

        "Criação de documento de Precricao medica"
        generatePdf_PrescricaoMedica(
            "Data do documento no formato DD/MM/YYYY"
            documentDatetime: String!,
            "Dados do Paciente, somente o nome e cns sao necessarios"
            patient: PatientInput!,
            """
            List de precicoes enviadas pelo medico, voce pode adicionar mais de uma utilizando uma lista de PrescriptionInput, veja as docs do input PrescriptionInput para mais informações"
            """
            prescription: [PrescriptionInput]!
        ): GeneratedPdf

        "Criação de documento de Relatorio de Alta"
        generatePdf_RelatorioAlta(
            "Data do documento no formato DD/MM/YYYY HH:mm"
            documentDatetime: String!,
            "Dados do Paciente"
            patient: PatientInput!
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
            "Dados do Estabelecimento Solicitante"
            establishmentSolitc: EstablishmentInput!,
            "Dados do Paciente"
            patient: PatientInput!
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
            "Dados do Paciente"
            patient: PatientInput
            "Motivo da Solicitacao, max: 216 min:7 caracteres"
            solicitationReason: String!,
            "Nome do profissional Solicitante, max:29 min:7 caracteres"
            profSolicitorName: String!,
            "Data da Solicitacao no formato DD/MM/YYYY"
            solicitationDatetime: String!,
            "Exames solicitados"
            exams: String!,
            "Nome do profissional autorizador, max:29 min:7 caracteres"
            profAuthorizedName: String,
            "Nome do paciente no final do documento, esse campo fica no fim do documento e tem um tamanho maximo diferente. max:46 min:7 caracteres"
            documentPacientName: String,
            "Data da Autorizacao no formato DD/MM/YYYY"
            autorizationDatetime: String,
            "Data do paciente, tambem no campo inferior no formato DD/MM/YYYY"
            documentPacientDate: String,
        ): GeneratedPdf

        "Criação de documento de Solicitacao de Mamografia"
        generatePdf_SolicitMamografia(
            "Dados do Paciente"
            patient: PatientInput!
            """
            Fez mamograma antes, envie uma lista com o primeiro valor ['SIM'/'NAO', 'Ano do mamograga']
            Exemplo: 
                ['SIM', '2020']
                ['NAO', null]
            """
            mammogramBefore: [String]!,
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
            "Nome da cidade aonde esta a unidade de saude, max:14 min:3"
            healthUnitAdressCity: String,
            "Apelido do paciente, max:18 min:4 caracteres" 
            patientSurname: String,
            """
            Escolaridade do paciente, opcoes:
            "ANALFABETO"  -> Analfabeto
            "FUNDINCOM"   -> Ensino Fundamental Incompleto
            "FUNDCOMPL"   -> Ensino Fundamental Completo
            "MEDIOCOMPL"  -> Ensino Medio Completo
            "SUPCOMPL"    -> Ensino Superior Completo
            """
            patientSchooling: String,
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
            "Codigo do IBGE do Município da Unidade de Saude"
            healthUnitCityIbgeCode: String,
            "Numero do protocolo, max: 10 caracteres"
            documentChartNumber: String,
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
            examNumber: String,
            """
            Mamografia de rasteramento. Opcoes:
                "POPALVO"       -> Populacao alvo
                "RISCOELEVADO"  -> Populacao de risco elevado
                "JATRATADO"     -> Paciente ja tratado de cancer de mama
            """
            trackingMammogram: String,
            "Adiconar Mamografia Diagnostica, utilize o input DiagnosticMamogramInput"
            diagnosticMammogram: DiagnosticMamogramInput
        ): GeneratedPdf

        "Criação de documento de Solicitacao de Mamografia"
        generatePdf_FichaInternamento(
            "Data Hora do documento no formato DD/MM/YYYY HH:mm"
            documentDatetime: String!,
            "Dados do Paciente"
            patient: PatientInput
            "Numero de telefone do paciente, envie somente os numeros sem formatacao, ex: XXXXXXXXXX, 10 ou 11 caracteres"
            patientPhonenumber: String!,
            "Historia da doenca atual/Exame fisico, max: 1600 min:10 caracteres"
            currentIllnessHistory: String!,
            "Supeita diagnostica Inicial (CID), max:100 min:5 caracteres"
            initialDiagnosticSuspicion: String!,
            "Nome do Medico, max: 49 min:7 caracteres"
            doctorName: String!,
            "CNS do Medico, envie somente numeros"
            doctorCns: String!,
            "CRM do medico, max:13 min:11"
            doctorCrm: String!,
            "Possui convenio suplementar, opcoes: 'SIM','NAO'"
            hasAdditionalHealthInsurance: String,
            """
            Peso estimado do paciente, numero inteiro no maximo 3 digitos, sera entendido como um valor total.
            Exemplo:
                patientEstimateWeight: 54  // sera entedido como 54kg
            """
            patientEstimateWeight: Int
        ): GeneratedPdf
    }
''')