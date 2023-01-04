import { gql } from "@apollo/client";

export const INTERNMENTS = gql`
  query getIntenments {
    internments {
      id
      patient {
        id
        name
        cns
        age
      }
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

export const STATES = gql`
  query stateData {
    state {
      name
      uf
    }
  }
`;

export const GET_PATIENT = gql`
  query patient($id: ID, $queryNameCnsCpf: String) {
    patient(id: $id, queryNameCnsCpf: $queryNameCnsCpf) {
      id
      name
      birthdate
      sex
      age
      cns
      rg
      cpf
      weightKg
      comorbidities {
        id
        value
      }
      allergies {
        id
        value
      }
      address {
        zipCode
        street
        number
        neighborhood
        complement
        city
        uf
      }
    }
  }
`;

export const GET_INTERNMENT = gql`
  query internment($internment: ID!) {
    internment(id: $internment) {
      justification
      cid10 {
        code
        description
      }
      evolutions {
        text
        professional {
          name
        }
        createdAt
      }
      prescriptions {
        id
        restingActivity {
          name
        }
        diet {
          name
        }
        drugPrescriptions {
          id
          drug {
            name
          }
          dosage
          route
          kind
          initialDate
          endingDate
        }
        nursingActivities {
          name
        }
      }

      pendings {
        text
      }
    }
  }
`;

export const GET_SINALS = gql`
  query internment($internment: ID!) {
    internment(id: $internment) {
      fluidBalance {
        id
        volumeMl
        description {
          value
        }
      }
      measures {
        spO2
        pain
        systolicBloodPressure
        diastolicBloodPressure
        cardiacFrequency
        respiratoryFrequency
        celciusAxillaryTemperature
        glucose
        fetalCardiacFrequency
      }
    }
  }
`;
