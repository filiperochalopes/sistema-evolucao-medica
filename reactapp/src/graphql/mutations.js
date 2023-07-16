import { gql } from "@apollo/client";

export const CREATE_USER = gql`
  mutation createUser($masterKey: String!, $user: UserInput) {
    patients(masterKey: $masterKey, user: $use) {
      id
    }
  }
`;

export const SIGNING = gql`
  mutation signing($email: String!, $password: String!) {
    signin(email: $email, password: $password) {
      token
    }
  }
`;

export const UPDATE_PATIENT = gql`
  mutation updatePatient($id: ID!, $patient: PatientInput!) {
    updatePatient(id: $id, patient: $patient) {
      id
    }
  }
`;

export const CREATE_INTERNMENT = gql`
  mutation createInternment(
    $admissionDatetime: String
    $patient: PatientInput
    $hpi: String
    $justification: String
    $cid10Code: String
  ) {
    createInternment(
      admissionDatetime: $admissionDatetime
      patient: $patient
      hpi: $hpi
      justification: $justification
      cid10Code: $cid10Code
    ) {
      id
    }
  }
`;

export const CREATE_PRESCRIPTION = gql`
  mutation createPrescription(
    $internmentId: Int!
    $restingActivity: String
    $diet: String
    $drugs: [DrugPrescriptionInput]
    $nursingActivities: [String]
  ) {
    createPrescription(
      internmentId: $internmentId
      restingActivity: $restingActivity
      diet: $diet
      drugs: $drugs
      nursingActivities: $nursingActivities
    ) {
      id
    }
  }
`;

export const CREATE_EVOLUTION = gql`
  mutation createEvolution(
    $internmentId: Int!
    $text: String
    $cid10Code: String
  ) {
    createEvolution(
      internmentId: $internmentId
      text: $text
      cid10Code: $cid10Code
    ) {
      id
    }
  }
`;

export const CREATE_PENDING = gql`
  mutation createPending($internmentId: Int!, $text: String) {
    createPending(internmentId: $internmentId, text: $text) {
      text
    }
  }
`;

export const CREATE_FLUID_BALANCE = gql`
  mutation createFluidBalance(
    $internmentId: Int!
    $volumeMl: Int
    $description: String
  ) {
    createFluidBalance(
      internmentId: $internmentId
      volumeMl: $volumeMl
      description: $description
    ) {
      id
    }
  }
`;

export const CREATE_MEASURE = gql`
  mutation createMeasure(
    $internmentId: Int!
    $spO2: Int
    $pain: Int
    $systolicBloodPressure: Int
    $diastolicBloodPressure: Int
    $cardiacFrequency: Int
    $respiratoryFrequency: Int
    $celciusAxillaryTemperature: Float
    $glucose: Int
    $fetalCardiacFrequency: Int
  ) {
    createMeasure(
      internmentId: $internmentId
      spO2: $spO2
      pain: $pain
      systolicBloodPressure: $systolicBloodPressure
      diastolicBloodPressure: $diastolicBloodPressure
      cardiacFrequency: $cardiacFrequency
      respiratoryFrequency: $respiratoryFrequency
      celciusAxillaryTemperature: $celciusAxillaryTemperature
      glucose: $glucose
      fetalCardiacFrequency: $fetalCardiacFrequency
    ) {
      id
    }
  }
`;

export const GENERATE_PDF = gql`
  mutation generatePDF($internmentId: Int!) {
    printPdf_FichaInternamento(internmentId: $internmentId) {
      base64Pdf
    }
  }
`;
export const GENERATE_PDF_FICHA_INTERNAMENTO = gql`
  mutation printPdf_FichaInternamento(
    $internmentId: Int!
    $extra: PrintFichaInternamentoExtraInput
  ) {
    printPdf_FichaInternamento(internmentId: $internmentId, extra: $extra) {
      base64Pdf
    }
  }
`;

export const GENERATE_PDF_EVOLUCAO_COMPACTA = gql`
  mutation printPdf_EvolucaoCompacta(
    $internmentId: Int!
    $prescriptionId: Int!
    $evolutionId: Int!
    $pendingsId: Int!
  ) {
    printPdf_EvolucaoCompacta(
      internmentId: $internmentId
      prescriptionId: $prescriptionId
      evolutionId: $evolutionId
      pendingsId: $pendingsId
    ) {
      base64Pdf
    }
  }
`;

export const GENERATE_PDF_RELATORIO_ALTA = gql`
  mutation printPdf_RelatorioAlta(
    $internmentId: Int!
    $extra: PrintRelatorioAltaExtraInput
  ) {
    printPdf_RelatorioAlta(internmentId: $internmentId, extra: $extra) {
      base64Pdf
    }
  }
`;

export const GENERATE_PDF_AIH_SUS = gql`
  mutation printPdf_AihSus(
    $internmentId: Int!
    $extra: PrintAihSusPdfExtraInput
  ) {
    printPdf_AihSus(internmentId: $internmentId, extra: $extra) {
      base64Pdf
    }
  }
`;

export const GENERATE_PDF_BALANCO_HIDRICO = gql`
  mutation printPdf_BalancoHidrico(
    $internmentId: Int!
    $extra: PrintBalancoHidricoExtraInput
  ) {
    printPdf_BalancoHidrico(internmentId: $internmentId, extra: $extra) {
      base64Pdf
    }
  }
`;

export const GENERATE_PDF_APAC = gql`
  mutation printPdf_Apac($internmentId: Int!, $extra: PrintApacExtraInput!) {
    printPdf_Apac(internmentId: $internmentId, extra: $extra) {
      base64Pdf
    }
  }
`;
