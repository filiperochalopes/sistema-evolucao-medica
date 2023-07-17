import { gql } from "@apollo/client";

export const MY_USER = gql`
  query getMyUser {
    myUser {
      id
      name
      email
      cns
      cpf
      birthdate
      professionalCategory
      professionalDocumentUf
      professionalDocumentNumber
    }
  }
`;

export const INTERNMENTS = gql`
  query getIntenments {
    internments {
      id
      patient {
        id
        name
        cns
        age
        sex
      }
    }
  }
`;

export const INTERNMENT_PRESCRIPTIONS = gql`
  query getInternmentPrescriptions($internmentId: ID!) {
    internment(id: $internmentId) {
      prescriptions {
        id
        createdAt
        professional {
          id
          name
        }
        restingActivity {
          name
        }
        diet {
          name
        }
        drugPrescriptions {
          drug {
            name
          }
          dosage
          route
        }
        nursingActivities {
          name
        }
      }
    }
  }
`;

export const INTERNMENT_PENDINGS = gql`
  query getInternmentPendings($internmentId: ID!) {
    internment(id: $internmentId) {
      pendings {
        id
        createdAt
        text
        professional {
          id
          name
        }
      }
    }
  }
`;

export const INTERNMENT_EVOLUTIONS = gql`
  query getInternmentEvolutions($internmentId: ID!) {
    internment(id: $internmentId) {
      evolutions {
        id
        createdAt
        text
        professional {
          id
          name
        }
      }
    }
  }
`;

export const CID10 = gql`
  query getCid10($query: String) {
    cid10(query: $query) {
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

export const FLUID_BALANCE_DESCRIPTIONS = gql`
  query getfluidBalanceDescriptions {
    fluidBalanceDescriptions {
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
      usualDosage
      comment
      usualRoute
      kind
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

export const GET_PATIENTS = gql`
  query patients($queryNameCnsCpf: String) {
    patients(queryNameCnsCpf: $queryNameCnsCpf) {
      id
      name
      birthdate
      sex
      age
      cns
      rg
      phone
      cpf
      weightKg
      motherName
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

export const GET_INITIAL_PATIENTS = gql`
  query patients {
    patients {
      id
      name
      birthdate
      sex
      age
      cns
      rg
      phone
      cpf
      weightKg
      motherName
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

export const GET_PATIENT = gql`
  query patient($id: ID) {
    patient(id: $id) {
      id
      name
      birthdate
      sex
      age
      cns
      rg
      phone
      cpf
      weightKg
      motherName
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
      patient {
        name
        age
        id
      }
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
            kind
          }
          dosage
          route
          initialDate
          endingDate
        }
        nursingActivities {
          name
        }
        createdAt
      }

      pendings {
        text
        createdAt
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

export const DRUG_PRESETS = gql`
  query drugPresets {
    drugPresets {
      name
      label
      drugs {
        id
        name
        usualDosage
        comment
        kind
        usualRoute
      }
    }
  }
`;

export const GET_ALL_CHART = gql`
  query internment($internment: ID!) {
    internment(id: $internment) {
      patient {
        age
        name
        id
      }
      hpi
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
            kind
            name
          }
          dosage
          route
          initialDate
          endingDate
        }
        nursingActivities {
          name
        }
        createdAt
      }

      pendings {
        text
        createdAt
      }
      fluidBalance {
        id
        volumeMl
        description {
          value
        }
        createdAt
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
        createdAt
      }
    }
  }
`;

export const GET_HIGH_COMPLEXITY_PROCEDURES = gql`
  query highComplexityProcedures {
    highComplexityProcedures {
      id
      name
      code
    }
  }
`;
