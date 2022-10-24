import { gql } from "@apollo/client";

export const PATIENTS = gql`
  query getPatients {
    patients {
      id
      name
      cns
    }
  }
`;

export const CID10 = gql`
  query getCid10 {
    cid10 {
      code
      description
    }
  }
`;
