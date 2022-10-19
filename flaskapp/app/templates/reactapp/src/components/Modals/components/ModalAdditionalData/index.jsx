import Container, { ButtonContainer } from "./styles";

import React from "styled-components";
import TextArea from "components/TextArea";
import Button from "components/Button";
import Select from "components/Select";
import Input from "components/Input";
import { useFormik } from "formik";
import { useEffect } from "react";

/* Strategy pattern */

const strategies = {
  hospitalAdmissionForm: ({ formik }) => (
    <>
      <TextArea
        value={formik.values.examResults}
        onChange={formik.handleChange}
        placeholder="Resultados de exames solicitados"
        name="examResults"
      />
      <Select />
      <ButtonContainer>
        <Button type="submit">Confirmar</Button>
      </ButtonContainer>
    </>
  ),
  EvolutionForm: ({ formik }) => {
    useEffect(() => {
      const initialDate = new Date();
      initialDate.setDate(initialDate.getDate() - 1);
      initialDate.setHours(7);

      const finalDate = new Date();
      const finalDateFormat = `${finalDate.toISOString().split("T")[0]}T07:00`;
      const initalDateFormat = `${
        initialDate.toISOString().split("T")[0]
      }T07:00`;
      formik.setValues({
        initialDate: initalDateFormat,
        finalDate: finalDateFormat,
      });
    }, []);

    return (
      <>
        <Input
          type="date"
          value={formik.values.initialDate}
          onChange={formik.handleChange}
          name="initialDate"
        />
        <Input
          type="date"
          value={formik.values.finalDate}
          onChange={formik.handleChange}
          name="finalDate"
        />
        <ButtonContainer>
          <Button type="submit">Confirmar</Button>
        </ButtonContainer>
      </>
    );
  },
  APAC: ({ formik }) => (
    <>
      <Select />
      <ButtonContainer>
        <Button type="submit">Confirmar</Button>
      </ButtonContainer>
    </>
  ),
  DischargeForm: ({ formik }) => (
    <>
      <TextArea
        placeholder="orientações de alta"
        name="dischargeGuidelines"
        value={formik.values.dischargeGuidelines}
      />

      <ButtonContainer>
        <Button type="submit">Confirmar</Button>
      </ButtonContainer>
    </>
  ),
  PrescriptionSheet: ({ formik }) => {
    useEffect(() => {
      const initialDate = new Date();
      initialDate.setDate(initialDate.getDate() - 1);
      initialDate.setHours(7);

      const finalDate = new Date();
      const finalDateFormat = `${finalDate.toISOString().split("T")[0]}T07:00`;
      const initalDateFormat = `${
        initialDate.toISOString().split("T")[0]
      }T07:00`;
      formik.setValues({
        initialDate: initalDateFormat,
        finalDate: finalDateFormat,
      });
    }, []);

    return (
      <>
        <Input
          type="datetime-local"
          placeholder="Data Inicial"
          onChange={(e) => console.log(e.target.value)}
          value={formik.values.initialDate}
        />
        <Input
          type="datetime-local"
          placeholder="Data Final"
          value={formik.values.finalDate}
        />
        <ButtonContainer>
          <Button type="submit">Confirmar</Button>
        </ButtonContainer>
      </>
    );
  },
};

const initialValuesStrategies = {
  hospitalAdmissionForm: {
    examResults: "",
    cid: "",
  },
  EvolutionForm: {
    initialDate: "",
    finalDate: "",
  },
  APAC: {
    examRequest: "",
  },
  PrescriptionSheet: {
    initialDate: "",
    finalDate: "",
  },
  DischargeForm: {
    dischargeGuidelines: "",
  },
};

const ModalAdditionalData = ({ type, confirmButton, ...rest }) => {
  const Strategy = strategies[type];
  const formik = useFormik({
    initialValues: initialValuesStrategies[type],
    onSubmit(values) {
      console.log(values);
    },
  });
  return (
    <Container onSubmit={formik.handleSubmit}>
      <Strategy confirmButton={confirmButton} formik={formik} />
    </Container>
  );
};

export default ModalAdditionalData;
