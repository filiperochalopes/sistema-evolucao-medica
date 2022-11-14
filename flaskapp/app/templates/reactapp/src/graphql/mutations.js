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
  mutation updatePatient($is: ID!, $patient: PatientInput!) {
    updatePatient(is: $is, patient: $patient) {
      id
      name
      cns
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
