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
import {
  GENERATE_PDF_FICHA_INTERNAMENTO,
  GENERATE_PDF_FOLHA_EVOLUCAO,
} from "graphql/mutations";
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
  printPdf_FolhaEvolucao: ({ formik }) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    useEffect(() => {
      const initialDate = new Date();
      initialDate.setDate(initialDate.getDate() - 1);
      initialDate.setHours(7);

      const finalDate = new Date();
      const finalDateFormat = `${finalDate.toISOString().split("T")[0]}T07:00`;
      const initalDateFormat = `${
        initialDate.toISOString().split("T")[0]
      }T07:00`;
      console.log({
        startDatetimeStamp: initalDateFormat,
        endingDatetimeStamp: finalDateFormat,
      });
      formik.setValues({
        extra: {
          interval: {
            startDatetimeStamp: initalDateFormat,
            endingDatetimeStamp: finalDateFormat,
          },
        },
      });
    }, []);

    return (
      <>
        <Input
          type="datetime-local"
          value={formik.values.extra.interval.startDatetimeStamp}
          onChange={formik.handleChange}
          name="extra.interval.startDatetimeStamp"
        />
        <Input
          type="datetime-local"
          value={formik.values.extra.interval.endingDatetimeStamp}
          onChange={formik.handleChange}
          name="extra.interval.endingDatetimeStamp"
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
  printPdf_FolhaEvolucao: {
    extra: {
      interval: {
        startDatetimeStamp: "",
        endingDatetimeStamp: "",
      },
    },
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
  const [getPDFFolhaEvolucao] = useMutation(GENERATE_PDF_FOLHA_EVOLUCAO);
  const Strategy = strategies[type];
  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: initialValuesStrategies[type],
    async onSubmit(values) {
      const newValues = { ...values, extra: { ...values.extra } };
      let request = undefined;
      if (type === "printPdf_FichaInternamento") {
        request = getPDFFicha;
      }
      if (type === "printPdf_FolhaEvolucao") {
        console.log(newValues.extra.interval);
        const initialDate =
          newValues.extra.interval.startDatetimeStamp.split("T");
        const finalDate =
          newValues.extra.interval.endingDatetimeStamp.split("T");
        newValues.extra.interval.startDatetimeStamp = `${initialDate[0]}T${initialDate[1]}:00`;
        newValues.extra.interval.endingDatetimeStamp = `${finalDate[0]}T${finalDate[1]}:00`;
        request = getPDFFolhaEvolucao;
      }
      if (!request) {
        return;
      }
      const response = await request({
        variables: {
          internmentId: Number(id),
          extra: newValues.extra,
        },
      });
      const link = document.createElement("a");
      const file = b64toBlob(response.data[type].base64Pdf, "application/pdf");
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
