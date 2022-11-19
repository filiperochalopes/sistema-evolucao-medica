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
import { v4 as uuidv4 } from "uuid";
import schema from "./schema";

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
        <Input
          value={formik.values.drug.useMode}
          name="drug.useMode"
          onChange={formik.handleChange}
          placeholder="Modo de uso"
        />
        <Select
          options={dataDrugsRoutesInObject}
          className="medium_size"
          value={formik.values.drug.routeAdministration}
          placeholder="Via de Administração"
          onChange={(e) => formik.setFieldValue("drug.routeAdministration", e)}
        />
        <div className="container_checkbox">
          <CheckBox
            checked={formik.values.drug.isAntibiotic}
            id="checkbox"
            onClick={() =>
              formik.setFieldValue(
                "drug.isAntibiotic",
                !formik.values.drug.isAntibiotic
              )
            }
          />
          <label htmlFor="checkbox">É antibiótico.</label>
        </div>
        {formik.values.drug.isAntibiotic && (
          <div className="row">
            <Input
              onChange={formik.handleChange}
              value={formik.values.drug.initialDate}
              name="drug.initialDate"
              type="date"
              className="medium_size"
              placeholder="Data de início"
            />
            <Input
              value={formik.values.drug.finalDate}
              name="drug.finalDate"
              onChange={formik.handleChange}
              type="date"
              className="medium_size"
              placeholder="Data de fim"
            />
          </div>
        )}
      </>
    );
  },
  default: () => {
    return <></>;
  },
};

const ModalAddPrescription = ({ confirmButton }) => {
  const { data: prescriptionTypesData } = useQuery(PRESCRIPTION_TYPES);
  const [getDrugs] = useLazyQuery(DRUGS);
  const [getRestingActivities] = useLazyQuery(RESTING_ACTIVITIES);
  const [getDiets] = useLazyQuery(DIETS);
  const [getNusingActivities] = useLazyQuery(NURSING_ACTIVITIES);

  const [prescriptionType, setPrescriptionType] = useState(undefined);
  const [medicaments, setMedicaments] = useState([]);
  const formik = useFormik({
    initialValues: {
      type: "",
      medicament: "",
      drug: {
        useMode: "",
        routeAdministration: "",
        isAntibiotic: false,
        initialDate: "",
        finalDate: "",
      },
    },
    onSubmit: (values) => {
      confirmButton({ id: uuidv4(), ...values });
    },
    validationSchema: schema,
  });

  useEffect(() => {
    let request = null;
    if (!prescriptionType?.name) {
      return;
    }
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
    prescriptionTypesStrategies[prescriptionType?.name || ""] ||
    prescriptionTypesStrategies.default;

  return (
    <Container onSubmit={formik.handleSubmit}>
      <Select
        getOptionLabel={(option) => option.label}
        getOptionValue={(option) => option.name}
        options={prescriptionTypesData?.prescriptionTypes || []}
        className="medium_size"
        placeholder="Tipo de Prescrição"
        value={prescriptionType}
        onChange={(e) => setPrescriptionType(e)}
      />
      <div className="container_medicaments">
        <Select
          getOptionLabel={(option) => option.name}
          getOptionValue={(option) => option.id}
          options={medicaments}
          onChange={(e) => formik.setFieldValue("medicament", e)}
          placeholder="Campo que seleciona um ou adiciona novo"
          values={formik.values.medicament}
        />
        <PrescriptionComponent formik={formik} />
      </div>
      <Button className="medium_size">Adicionar Linha</Button>
    </Container>
  );
};

export default ModalAddPrescription;
