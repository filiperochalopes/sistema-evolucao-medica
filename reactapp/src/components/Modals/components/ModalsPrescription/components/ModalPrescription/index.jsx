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

const DrugPrescriptionForm = ({ formik }) => {
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
        error={
          formik.errors.drug?.useMode && formik.touched?.drug?.useMode
            ? formik.errors.drug?.useMode
            : ""
        }
      />
      <Select
        options={dataDrugsRoutesInObject}
        className="medium_size"
        value={formik.values.drug?.routeAdministration}
        placeholder="Via de Administração"
        onChange={(e) => formik.setFieldValue("drug.routeAdministration", e)}
        error={
          formik.errors?.drug?.routeAdministration &&
          formik.touched?.drug?.routeAdministration
            ? formik.errors?.drug?.routeAdministration
            : ""
        }
      />
      <div className="container_checkbox">
        <CheckBox
          checked={formik.values.drug.isAntibiotic === "atb"}
          id="checkbox"
          onClick={() =>
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
            error={
              formik.errors?.drug?.initialDate &&
              formik.touched?.drug?.initialDate
                ? formik.errors.drug.initialDate
                : ""
            }
          />
          <Input
            value={formik.values.drug.finalDate}
            name="drug.finalDate"
            onChange={formik.handleChange}
            type="datetime-local"
            className="medium_size"
            placeholder="Data de fim"
            error={
              formik.errors?.drug?.finalDate && formik.touched?.drug?.finalDate
                ? formik.errors.drug.finalDate
                : ""
            }
          />
        </div>
      )}
    </>
  );
};

const ModalAddPrescription = ({
  confirmCallback,
  nursingActivities,
  drugs,
  currentPrescription,
  update,
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

  const [prescriptionNameOptions, setPrescriptionNameOptions] = useState([]);

  const formik = useFormik({
    initialValues: {
      // type.name determina o tipo de entradas: drug, restingActivity...
      type: null,
      // A prescrição no momento
      prescription: "",
      // A prescrição no momento para medicações
      drug: {
        useMode: "",
        routeAdministration: "",
        isAntibiotic: "oth",
        initialDate: "",
        finalDate: "",
      },
    },
    onSubmit: (values) => {
      console.log(values);
      let existMedicament;
      if (values.type.name === "drug") {
        existMedicament = drugs.find(
          (drug) =>
            drug.drugName === values.prescription.name &&
            drug.routeAdministration === values.drug.routeAdministration.value
        );
      }

      if (existMedicament) {
        return;
      }
      confirmCallback({ id: uuidv4(), ...values });
    },
    validationSchema: schema,
  });

  useEffect(() => {
    if (currentPrescription) {
      formik.setValues(currentPrescription);
    }

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currentPrescription]);

  useEffect(() => {
    // preenchendo o campo de select da prescrição
    let request = null;
    if (!formik.values.type?.name) {
      return;
    }

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
      const prescriptinResponseMap = {
        drug: "drugs",
        diet: "diets",
        nursingActivity: "nursingActivities",
        restingActivity: "restingActivities",
      };
      let _prescription =
        response.data[prescriptinResponseMap[formik.values.type.name]];
      if (formik.values.type.name === "nursingActivity") {
        _prescription = _prescription.filter(
          (p) =>
            !nursingActivities.find(
              (nursingActivity) => nursingActivity === p.name
            ) || p.name === currentPrescription?.prescription.name
        );
      }
      setPrescriptionNameOptions(
        _prescription.map((p) => ({
          ...p,
          label: p.name,
          value: p.id,
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
    currentPrescription,
  ]);

  return (
    <Container onSubmit={formik.handleSubmit}>
      <Select
        isDisabled={update}
        getOptionLabel={(option) => option.label}
        getOptionValue={(option) => option.name}
        options={prescriptionTypesData?.prescriptionTypes || []}
        className="medium_size"
        placeholder="Tipo de Prescrição"
        value={formik.values.type}
        onChange={(e) => {
          formik.setFieldValue("prescription", "");
          formik.setFieldValue("type", e);
        }}
      />
      <br />
      {formik.values.type && (
        <div className="container_options">
          <Select
            options={prescriptionNameOptions}
            created
            onChange={(e) => {
              if (!e.usualDosage) {
                formik.setFieldValue("prescription", {
                  ...e,
                  name: e.label,
                  id: e.value,
                });
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
                prescription: e,
              });
            }}
            placeholder="Selecione ou adicione um novo item"
            value={
              formik.values.prescription.name
                ? {
                    label: formik.values.prescription.name,
                    value: formik.values.prescription.id,
                  }
                : null
            }
          />
          {formik.values.type?.name === "drug" && (
            <DrugPrescriptionForm formik={formik} />
          )}
        </div>
      )}
      <Button
        className="medium_size"
        type="submit"
        onClick={() => {
          console.log(formik);
        }}
      >
        {update ? "Atualizar Linha" : "Adicionar Linha"}
      </Button>
    </Container>
  );
};

export default ModalAddPrescription;
