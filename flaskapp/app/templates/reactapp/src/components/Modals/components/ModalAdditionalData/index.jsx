import Container, {
  ButtonContainer,
  CheckBoxContainer,
  CheckBoxsContainer,
} from "./styles";

import React from "styled-components";
import TextArea from "components/TextArea";
import Button from "components/Button";
import Select from "components/Select";
import Input from "components/Input";
import { useFormik } from "formik";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { GENERATE_PDF_FICHA_INTERNAMENTO } from "graphql/mutations";
import { useMutation } from "@apollo/client";

/* Strategy pattern */

const strategies = {
  printPdf_FichaInternamento: ({ formik }) => (
    <>
      <p>Tem seguro/plano de saúde outro além do SUS?</p>
      <CheckBoxsContainer>
        <CheckBoxContainer>
          <label htmlFor="checkbox_true">Sim</label>
          <input
            id="checkbox_true"
            type="checkbox"
            value={formik.values.extra.hasAdditionalHealthInsurance}
            onChange={() =>
              formik.setFieldValue("extra", {
                hasAdditionalHealthInsurance: true,
              })
            }
          />
        </CheckBoxContainer>
        <CheckBoxContainer>
          <label htmlFor="checkbox_false">Não</label>
          <input
            id="checkbox_false"
            type="checkbox"
            value={!formik.values.extra.hasAdditionalHealthInsurance}
            onChange={() =>
              formik.setFieldValue("extra", {
                hasAdditionalHealthInsurance: false,
              })
            }
          />
        </CheckBoxContainer>
      </CheckBoxsContainer>
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
  printPdf_FichaInternamento: {
    extra: {
      hasAdditionalHealthInsurance: true,
    },
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

const b64toBlob = (b64Data, contentType = "", sliceSize = 512) => {
  const byteCharacters = atob(b64Data);
  const byteArrays = [];

  for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
    const slice = byteCharacters.slice(offset, offset + sliceSize);

    const byteNumbers = new Array(slice.length);
    for (let i = 0; i < slice.length; i++) {
      byteNumbers[i] = slice.charCodeAt(i);
    }

    const byteArray = new Uint8Array(byteNumbers);
    byteArrays.push(byteArray);
  }

  const blob = new Blob(byteArrays, { type: contentType });
  return blob;
};

const ModalAdditionalData = ({ type, confirmButton, id, ...rest }) => {
  const [getPDFFicha] = useMutation(GENERATE_PDF_FICHA_INTERNAMENTO);
  const Strategy = strategies[type];
  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: initialValuesStrategies[type],
    async onSubmit(values) {
      let request = undefined;
      if (type === "printPdf_FichaInternamento") {
        request = getPDFFicha;
      }
      if (!request) {
        return;
      }
      const response = await request({
        variables: {
          internmentId: Number(id),
          extra: values.extra,
        },
      });
      console.log("response.data.data.printPdf_FichaInternamento.base64Pdf");
      console.log(response.data.printPdf_FichaInternamento);
      const link = document.createElement("a");
      const file = b64toBlob(
        response.data.printPdf_FichaInternamento.base64Pdf,
        "application/pdf"
      );
      const url = URL.createObjectURL(file);
      link.href = url;
      link.setAttribute("target", "_blank");
      link.click();
    },
  });
  return (
    <Container onSubmit={formik.handleSubmit}>
      <Strategy confirmButton={confirmButton} formik={formik} />
    </Container>
  );
};

export default ModalAdditionalData;
