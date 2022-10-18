import Container, { ButtonContainer } from "./styles";

import React from "styled-components";
import TextArea from "components/TextArea";
import Button from "components/Button";
import Select from "components/Select";
import Input from "components/Input";
import { useFormik } from "formik";

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
  evolutionForm: ({ formik }) => (
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
  ),
  APAC: ({ formik }) => (
    <>
      <Select />
      <ButtonContainer>
        <Button type="submit">Confirmar</Button>
      </ButtonContainer>
    </>
  ),
};

const initialValuesStrategies = {
  hospitalAdmissionForm: {
    examResults: "",
    cid: "",
  },
  evolutionForm: {
    initialDate: "",
    finalDate: "",
  },
  APAC: {
    examRequest: "",
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
