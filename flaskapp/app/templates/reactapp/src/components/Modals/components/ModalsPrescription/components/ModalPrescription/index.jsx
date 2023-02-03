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
import { useEffect, useMemo, useState } from "react";
import Container from "./styles";
import { v4 as uuidv4 } from "uuid";
import schema from "./schema";

const medicamentsAdapter = {
  drug: "drugs",
  diet: "diets",
  nursingActivity: "nursingActivities",
  restingActivity: "restingActivities",
};

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
          isDisabled={formik.values.block}
          onChange={(e) => formik.setFieldValue("drug.routeAdministration", e)}
        />
        <div className="container_checkbox">
          <CheckBox
            checked={formik.values.drug.isAntibiotic === "atb"}
            id="checkbox"
            onClick={() =>
              !formik.values.block &&
              formik.setFieldValue(
                "drug.isAntibiotic",
                formik.values.drug.isAntibiotic === "atb" ? "oth" : "atb"
              )
            }
          />
          <label htmlFor="checkbox">É antibiótico.</label>
        </div>
        {formik.values.drug.isAntibiotic === "atb" && (
          <div className="row">
            <Input
              onChange={formik.handleChange}
              value={formik.values.drug.initialDate}
              name="drug.initialDate"
              type="datetime-local"
              className="medium_size"
              placeholder="Data de início"
            />
            <Input
              value={formik.values.drug.finalDate}
              name="drug.finalDate"
              onChange={formik.handleChange}
              type="datetime-local"
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

const ModalAddPrescription = ({
  confirmButton,
  nursingActivities,
  drugs,
  currentMedicament,
  notChangeType,
}) => {
  const { data: prescriptionTypesData } = useQuery(PRESCRIPTION_TYPES);
  const [getDrugs] = useLazyQuery(DRUGS, {
    fetchPolicy: "network-only",
    nextFetchPolicy: "network-only",
  });
  const [getRestingActivities] = useLazyQuery(RESTING_ACTIVITIES, {
    fetchPolicy: "network-only",
    nextFetchPolicy: "network-only",
  });
  const [getDiets] = useLazyQuery(DIETS, {
    fetchPolicy: "network-only",
    nextFetchPolicy: "network-only",
  });
  const [getNusingActivities] = useLazyQuery(NURSING_ACTIVITIES, {
    fetchPolicy: "network-only",
    nextFetchPolicy: "network-only",
  });

  const [medicaments, setMedicaments] = useState([]);
  const formik = useFormik({
    initialValues: {
      type: null,
      medicament: "",
      drug: {
        useMode: "",
        routeAdministration: "",
        isAntibiotic: "oth",
        initialDate: "",
        finalDate: "",
      },
    },
    onSubmit: (values) => {
      confirmButton({ id: uuidv4(), ...values });
    },
    validationSchema: schema,
  });
  console.log(formik);

  useEffect(() => {
    if (!currentMedicament) {
      return;
    }

    formik.setValues(currentMedicament);
  }, [currentMedicament]);

  useEffect(() => {
    let request = null;
    if (!formik.values.type?.name) {
      return;
    }
    console.log("formik.values.type?.namee", formik.values.type?.name);

    if (formik.values.type.name === "drug") {
      request = getDrugs;
    } else if (formik.values.type.name === "diet") {
      request = getDiets;
    } else if (formik.values.type.name === "restingActivity") {
      request = getRestingActivities;
    } else if (formik.values.type.name === "nursingActivity") {
      request = getNusingActivities;
    }

    if (!request) {
      return;
    }

    request().then((response) => {
      console.log("formik.values.type", response.data);
      let newMedicaments =
        response.data[medicamentsAdapter[formik.values.type.name]];

      if (formik.values.type.name === "drug") {
        newMedicaments = newMedicaments.filter(
          (medicament) =>
            !drugs.find((drug) => drug.drugName === medicament.name) ||
            medicament.name === currentMedicament?.medicament.name
        );
      } else if (formik.values.type.name === "nursingActivity") {
        newMedicaments = newMedicaments.filter(
          (medicament) =>
            !nursingActivities.find(
              (nursingActivitie) => nursingActivitie === medicament.name
            ) || medicament.name === currentMedicament?.medicament.name
        );
        console.log("medicaments", newMedicaments);
      }
      setMedicaments(
        newMedicaments.map((medicament) => ({
          ...medicament,
          label: medicament.name,
          value: medicament.id,
        }))
      );
    });
  }, [
    getDiets,
    getDrugs,
    getRestingActivities,
    getNusingActivities,
    formik.values.type,
    drugs,
    nursingActivities,
    currentMedicament,
  ]);

  const PrescriptionComponent =
    prescriptionTypesStrategies[formik.values.type?.name || ""] ||
    prescriptionTypesStrategies.default;
  return (
    <Container onSubmit={formik.handleSubmit}>
      <Select
        isDisabled={notChangeType}
        getOptionLabel={(option) => option.label}
        getOptionValue={(option) => option.name}
        options={prescriptionTypesData?.prescriptionTypes || []}
        className="medium_size"
        placeholder="Tipo de Prescrição"
        value={formik.values.type}
        onChange={(e) => formik.setFieldValue("type", e)}
      />
      <div className="container_medicaments">
        <Select
          options={medicaments}
          created
          onChange={(e) => {
            if (!e.usualDosage) {
              formik.setFieldValue("medicament", {
                ...e,
                name: e.label,
                id: e.value,
              });

              formik.setFieldValue("block", false);
              return;
            }
            formik.setValues({
              ...formik.values,
              drug: {
                finalDate: "",
                initialDate: "",
                isAntibiotic: e.kind,
                routeAdministration: {
                  label: e.usualRoute,
                  value: e.usualRoute,
                },
                useMode: e.usualDosage,
              },
              block: true,
              medicament: e,
            });
          }}
          placeholder="Campo que seleciona um ou adiciona novo"
          value={
            formik.values.medicament.name
              ? {
                  label: formik.values.medicament.name,
                  value: formik.values.medicament.id,
                }
              : null
          }
        />
        <PrescriptionComponent formik={formik} />
      </div>
      <Button className="medium_size">
        {notChangeType ? "Atualizar Linha" : "Adicionar Linha"}
      </Button>
    </Container>
  );
};

export default ModalAddPrescription;
