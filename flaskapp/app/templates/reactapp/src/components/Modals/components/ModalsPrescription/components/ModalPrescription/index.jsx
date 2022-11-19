/* eslint-disable react-hooks/rules-of-hooks */
import { useQuery, useLazyQuery } from "@apollo/client";
import Button from "components/Button";
import CheckBox from "components/CheckBox";
import Input from "components/Input";
import Select from "components/Select";
import { useFormik } from "formik";
import {
  PRESCRIPTION_TYPES,
  DRUGS,
  RESTING_ACTIVITIES,
  DIETS,
  DRUG_ROUTES,
  NURSING_ACTIVITIES,
} from "graphql/queries";
import { useEffect, useState } from "react";
import Container from "./styles";

const prescriptionTypesStrategies = {
  drug: ({ formik }) => {
    const { data: drugRoutesData } = useQuery(DRUG_ROUTES);
    const [dataDrugsRoutesInObject, setDataDrugsRoutesInObject] = useState([]);

    useEffect(() => {
      if (drugRoutesData?.drugRoutes) {
        const transformDrugsRoutesInObject = drugRoutesData.drugRoutes.map(
          (drug) => ({ label: drug, value: drug })
        );
        setDataDrugsRoutesInObject(transformDrugsRoutesInObject);
      }
    }, [drugRoutesData]);
    return (
      <>
        <Input placeholder="Modo de uso" />
        <Select
          options={dataDrugsRoutesInObject}
          className="medium_size"
          placeholder="Via de Administração"
          onChange={(e) => formik.setFieldValue("drugs", e)}
        />
        <div className="container_checkbox">
          <CheckBox />
          <p>É antibiótico.</p>
        </div>
        <div className="row">
          <Input type="date" className="medium_size" />
          <Input type="date" className="medium_size" />
        </div>
      </>
    );
  },
  default: () => {
    return <></>;
  },
};

const ModalAddPrescription = ({ internmentId }) => {
  const { data: prescriptionTypesData } = useQuery(PRESCRIPTION_TYPES);
  const [getDrugs] = useLazyQuery(DRUGS);
  const [getRestingActivities] = useLazyQuery(RESTING_ACTIVITIES);
  const [getDiets] = useLazyQuery(DIETS);
  const [getNusingActivities] = useLazyQuery(NURSING_ACTIVITIES);

  const [prescriptionType, setPrescriptionType] = useState({});
  const [medicaments, setMedicaments] = useState([]);
  const formik = useFormik({
    initialValues: {
      restingActivity: "",
      diet: "",
      drugs: [],
      nursingActivities: [],
    },
  });

  useEffect(() => {
    let request = null;
    if (prescriptionType.name === "drug") {
      request = getDrugs;
    } else if (prescriptionType.name === "diet") {
      request = getDiets;
    } else if (prescriptionType.name === "restingActivity") {
      request = getRestingActivities;
    } else if (prescriptionType.name === "nursingActivity") {
      request = getNusingActivities;
    }
    if (request) {
      request().then((response) => {
        setMedicaments(response.data.drugs);
      });
    }
  }, [
    getDiets,
    getDrugs,
    getRestingActivities,
    getNusingActivities,
    prescriptionType,
  ]);

  const PrescriptionComponent =
    prescriptionTypesStrategies[prescriptionType.name || ""] ||
    prescriptionTypesStrategies.default;

  return (
    <Container>
      <Select
        getOptionLabel={(option) => option.label}
        getOptionValue={(option) => option.name}
        options={prescriptionTypesData?.prescriptionTypes || []}
        className="medium_size"
        placeholder="Tipo de Prescrição"
        onChange={(e) => setPrescriptionType(e)}
      />
      <div className="container_medicaments">
        <Select
          getOptionLabel={(option) => option.name}
          getOptionValue={(option) => option.id}
          options={medicaments}
          placeholder="Campo que seleciona um ou adiciona novo"
        />
        <PrescriptionComponent formik={formik} />
      </div>
      <Button className="medium_size" type="button">
        Adicionar Linha
      </Button>
    </Container>
  );
};

export default ModalAddPrescription;
