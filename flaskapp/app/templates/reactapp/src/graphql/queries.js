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

export const ALLERGIES = gql`
  query getAllergies {
    allergies {
      id
      value
    }
  }
`;

export const COMORBIDITIES = gql`
  query getComorbidities {
    comorbidities {
      id
      value
    }
  }
`;

export const PRESCRIPTION_TYPES = gql`
  query getPrescriptionTypes {
    prescriptionTypes {
      name
      label
    }
  }
`;

export const DRUGS = gql`
  query getDrugs {
    drugs {
      name
      id
    }
  }
`;

export const DIETS = gql`
  query getDiets {
    diets {
      name
      id
    }
  }
`;
export const NURSING_ACTIVITIES = gql`
  query getNursingActivities {
    nursingActivities {
      name
      id
    }
  }
`;

export const RESTING_ACTIVITIES = gql`
  query getRestingActivities {
    restingActivities {
      name
      id
    }
  }
`;

export const DRUG_ROUTES = gql`
  query getDrugRoutes {
    drugRoutes
  }
`;
