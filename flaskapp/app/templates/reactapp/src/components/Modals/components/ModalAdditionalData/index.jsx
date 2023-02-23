import Container, {
  ButtonContainer,
  CheckBoxContainer,
  CheckBoxsContainer,
} from "./styles";
import { createFilter, components } from "react-select";
import Buffer from "buffer";
import React from "styled-components";
import TextArea from "components/TextArea";
import Button from "components/Button";
import Select from "components/Select";
import Input from "components/Input";
import { useFormik } from "formik";
import { useNavigate } from "react-router-dom";
import {
  GENERATE_PDF_AIH_SUS,
  GENERATE_PDF_BALANCO_HIDRICO,
  GENERATE_PDF_FICHA_INTERNAMENTO,
  GENERATE_PDF_FOLHA_EVOLUCAO,
  GENERATE_PDF_FOLHA_PRESCRICAO,
  GENERATE_PDF_RELATORIO_ALTA,
} from "graphql/mutations";
import { useMutation, useQuery } from "@apollo/client";
import { cloneDeep } from "lodash";
import Interval from "./components/Interval";
import { CID10 } from "graphql/queries";
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
  printPdf_FolhaEvolucao: Interval,
  APAC: ({ formik }) => (
    <>
      <Select />
      <ButtonContainer>
        <Button type="submit">Confirmar</Button>
      </ButtonContainer>
    </>
  ),
  printPdf_RelatorioAlta: ({ formik }) => (
    <>
      <TextArea
        placeholder="orientações de alta"
        name="extra.orientations"
        onChange={formik.handleChange}
        value={formik.values.extra.orientations}
      />
      <Input
        type="datetime-local"
        placeholder="Data Inicial"
        onChange={formik.handleChange}
        value={formik.values.extra.datetimeStamp}
        name="extra.datetimeStamp"
      />
      <ButtonContainer>
        <Button type="submit">Confirmar</Button>
      </ButtonContainer>
    </>
  ),
  printPdf_BalancoHidrico: Interval,
  printPdf_FolhaPrescricao: Interval,
  printPdf_AihSus: ({ formik }) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const { data: cid10Data } = useQuery(CID10);

    return (
      <>
        <Select
          onChange={(e) => {
            formik.setFieldValue("extra.secondaryDiagnosis", e);
          }}
          components={{
            Option: ({ children, ...props }) => {
              const { onMouseMove, onMouseOver, ...rest } = props.innerProps;
              const newProps = Object.assign(props, { innerProps: rest });
              return (
                <components.Option {...newProps}>{children}</components.Option>
              );
            },
          }}
          filterOption={createFilter({ ignoreAccents: false })}
          getOptionLabel={(option) => option.description}
          getOptionValue={(option) => option.code}
          options={cid10Data?.cid10 || []}
          value={formik.values.extra.secondaryDiagnosis}
          placeholder="CID - SUSPEITA INICIAL"
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
  printPdf_FolhaPrescricao: {
    extra: {
      interval: {
        startDatetimeStamp: "",
        endingDatetimeStamp: "",
      },
    },
  },
  printPdf_BalancoHidrico: {
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
  printPdf_RelatorioAlta: {
    extra: {
      orientations: "",
      datetimeStamp: "",
    },
  },
  printPdf_AihSus: {
    extra: {
      secondaryDiagnosis: undefined,
    },
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
  const [getPDFFolhaPrescricao] = useMutation(GENERATE_PDF_FOLHA_PRESCRICAO);
  const [getPDFRelatorioAlta] = useMutation(GENERATE_PDF_RELATORIO_ALTA);
  const [getPDFAihSus] = useMutation(GENERATE_PDF_AIH_SUS);
  const [getPDFBalancoHidrico] = useMutation(GENERATE_PDF_BALANCO_HIDRICO);

  const Strategy = strategies[type];
  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: initialValuesStrategies[type],
    async onSubmit(values) {
      const newValues = cloneDeep(values);
      let request = undefined;
      if (type === "printPdf_FichaInternamento") {
        request = getPDFFicha;
      }
      if (newValues.extra.interval) {
        newValues.extra.interval.startDatetimeStamp = `${newValues.extra.interval.startDatetimeStamp}:00`;
        newValues.extra.interval.endingDatetimeStamp = `${newValues.extra.interval.endingDatetimeStamp}:00`;
      }
      if (type === "printPdf_FolhaEvolucao") {
        request = getPDFFolhaEvolucao;
      }
      if (type === "printPdf_FolhaPrescricao") {
        request = getPDFFolhaPrescricao;
      }
      if (type === "printPdf_RelatorioAlta") {
        newValues.extra.datetimeStamp = `${newValues.extra.datetimeStamp}:00`;
        request = getPDFRelatorioAlta;
      }
      if (type === "printPdf_AihSus") {
        newValues.extra.secondaryDiagnosis = {
          code: newValues.extra.secondaryDiagnosis.code,
          description: newValues.extra.secondaryDiagnosis.description,
        };
        request = getPDFAihSus;
      }
      if (type === "printPdf_BalancoHidrico") {
        request = getPDFBalancoHidrico;
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
