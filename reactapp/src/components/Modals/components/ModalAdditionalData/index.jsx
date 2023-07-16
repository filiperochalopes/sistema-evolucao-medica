/* eslint-disable react-hooks/rules-of-hooks */
import Container, {
  ButtonContainer,
  CheckBoxContainer,
  CheckBoxsContainer,
  ContainerProcessSecondaty,
} from "./styles";
import { createFilter, components } from "react-select";
import React from "styled-components";
import TextArea from "components/TextArea";
import Button from "components/Button";
import Select from "components/Select";
import Input from "components/Input";
import { useFormik } from "formik";
import {
  GENERATE_PDF_AIH_SUS,
  GENERATE_PDF_APAC,
  GENERATE_PDF_BALANCO_HIDRICO,
  GENERATE_PDF_FICHA_INTERNAMENTO,
  GENERATE_PDF_RELATORIO_ALTA,
  GENERATE_PDF_EVOLUCAO_COMPACTA,
} from "graphql/mutations";
import { useLazyQuery, useMutation, useQuery } from "@apollo/client";
import { cloneDeep } from "lodash";
import Interval from "./components/Interval";
import { CID10, GET_HIGH_COMPLEXITY_PROCEDURES } from "graphql/queries";
import { useState } from "react";
import b64toBlob from "utils/b64toBlob";
import useHandleErrors from "hooks/useHandleErrors";
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
            checked={formik.values.extra.hasAdditionalHealthInsurance}
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
            checked={!formik.values.extra.hasAdditionalHealthInsurance}
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
        placeholder="Data e Hora da Alta"
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
    const [getCid10] = useLazyQuery(CID10);

    return (
      <>
        <Select
          onChange={(e) => {
            formik.setFieldValue("extra.secondaryDiagnosis", e);
          }}
          loadOptions={async (inputValue) => {
            const response = await getCid10({
              variables: {
                query: inputValue,
              },
            });
            return response?.data.cid10;
          }}
          async
          filterOption={createFilter({ ignoreAccents: false })}
          getOptionLabel={(option) => option.description}
          getOptionValue={(option) => option.code}
          defaultOptions={cid10Data?.cid10}
          value={formik.values.extra.secondaryDiagnosis}
          placeholder="CID - SUSPEITA SECUNDÁRIA"
        />
        <ButtonContainer>
          <Button type="submit">Confirmar</Button>
        </ButtonContainer>
      </>
    );
  },
  printPdf_Apac: ({ formik }) => {
    const [currentSecondaryProced, setCurrentSecondaryProcedure] =
      useState(undefined);
    const [currentQuantity, setCurrentQuantity] = useState(1);
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const { data: cid10Data } = useQuery(CID10);
    const [getCid10] = useLazyQuery(CID10);
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const { data: procedures } = useQuery(GET_HIGH_COMPLEXITY_PROCEDURES);

    return (
      <>
        <Select
          onChange={(e) => {
            formik.setFieldValue("extra.procedure", {
              ...e,
              quantity: formik.values.extra.procedure?.quantity || 1,
            });
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
          getOptionLabel={(option) => option.name}
          getOptionValue={(option) => option.code}
          options={procedures?.highComplexityProcedures || []}
          value={
            formik.values.extra.procedure.name
              ? formik.values.extra.procedure
              : null
          }
          placeholder="Procedimento"
        />
        <Input
          type="number"
          placeholder="Quantidade"
          onChange={formik.handleChange}
          value={formik.values.extra.procedure.quantity}
          name="extra.procedure.quantity"
        />
        <h2>Procedimentos Secundários</h2>
        <ContainerProcessSecondaty>
          {formik.values.extra.secondaryProcedures.map((procedure, index) => (
            <div key={index}>
              <Select
                onChange={(e) => {
                  formik.setFieldValue(`extra.secondaryProcedures[${index}]`, {
                    name: e.name,
                    code: e.code,
                    quantity: procedure.quantity,
                  });
                }}
                components={{
                  Option: ({ children, ...props }) => {
                    const { onMouseMove, onMouseOver, ...rest } =
                      props.innerProps;
                    const newProps = Object.assign(props, {
                      innerProps: rest,
                    });
                    return (
                      <components.Option {...newProps}>
                        {children}
                      </components.Option>
                    );
                  },
                }}
                filterOption={createFilter({ ignoreAccents: false })}
                getOptionLabel={(option) => option.name}
                getOptionValue={(option) => option.code}
                options={procedures?.highComplexityProcedures || []}
                value={procedure}
                placeholder="Procedimento Secundário"
              />
              <br />
              <Input
                type="number"
                placeholder="Quantidade"
                name={`extra.secondaryProcedures[${index}].quantity`}
                onChange={formik.handleChange}
                value={procedure.quantity}
              />
              <ButtonContainer>
                <Button
                  customType="red"
                  type="button"
                  onClick={() => {
                    const filterProcedures =
                      formik.values.extra.secondaryProcedures.filter(
                        (procedure, indexPro) => indexPro !== index
                      );
                    formik.setFieldValue(
                      "extra.secondaryProcedures",
                      filterProcedures
                    );
                  }}
                >
                  Remover Procedimento
                </Button>
              </ButtonContainer>
              <br />
            </div>
          ))}
          <Select
            onChange={(e) => {
              setCurrentSecondaryProcedure({
                name: e.name,
                code: e.code,
              });
            }}
            components={{
              Option: ({ children, ...props }) => {
                const { onMouseMove, onMouseOver, ...rest } = props.innerProps;
                const newProps = Object.assign(props, { innerProps: rest });
                return (
                  <components.Option {...newProps}>
                    {children}
                  </components.Option>
                );
              },
            }}
            filterOption={createFilter({ ignoreAccents: false })}
            getOptionLabel={(option) => option.name}
            getOptionValue={(option) => option.code}
            options={procedures?.highComplexityProcedures || []}
            value={currentSecondaryProced}
            placeholder="Procedimento Secundário"
          />
          <br />
          <Input
            type="number"
            placeholder="Quantidade"
            onChange={(e) => setCurrentQuantity(e.target.value)}
            value={currentQuantity}
          />
          <ButtonContainer>
            <Button
              type="button"
              onClick={() => {
                formik.setFieldValue("extra.secondaryProcedures", [
                  ...formik.values.extra.secondaryProcedures,
                  {
                    quantity: currentQuantity,
                    name: currentSecondaryProced.name,
                    code: currentSecondaryProced.code,
                  },
                ]);
                setCurrentQuantity(1);
                setCurrentSecondaryProcedure(undefined);
              }}
            >
              Adicionar
            </Button>
          </ButtonContainer>
        </ContainerProcessSecondaty>
        <Select
          onChange={(e) => {
            formik.setFieldValue("extra.diagnosis", e);
          }}
          loadOptions={async (inputValue) => {
            const response = await getCid10({
              variables: {
                query: inputValue,
              },
            });
            return response?.data.cid10;
          }}
          async
          filterOption={createFilter({ ignoreAccents: false })}
          getOptionLabel={(option) => `${option.code} - ${option.description}`}
          getOptionValue={(option) => option.code}
          defaultOptions={cid10Data?.cid10}
          value={formik.values.extra.diagnosis}
          placeholder="Diagnóstico"
        />
        <Select
          onChange={(e) => {
            formik.setFieldValue("extra.secondaryDiagnosis", e);
          }}
          loadOptions={async (inputValue) => {
            const response = await getCid10({
              variables: {
                query: inputValue,
              },
            });
            return response?.data.cid10;
          }}
          async
          filterOption={createFilter({ ignoreAccents: false })}
          getOptionLabel={(option) => `${option.code} - ${option.description}`}
          getOptionValue={(option) => option.code}
          defaultOptions={cid10Data?.cid10}
          value={formik.values.extra.secondaryDiagnosis}
          placeholder="Diagnóstico secundário"
        />
        <Select
          onChange={(e) => {
            formik.setFieldValue("extra.ssociatedCause", e);
          }}
          loadOptions={async (inputValue) => {
            const response = await getCid10({
              variables: {
                query: inputValue,
              },
            });
            return response?.data.cid10;
          }}
          async
          filterOption={createFilter({ ignoreAccents: false })}
          getOptionLabel={(option) => `${option.code} - ${option.description}`}
          getOptionValue={(option) => option.code}
          defaultOptions={cid10Data?.cid10}
          value={formik.values.extra.ssociatedCause}
          placeholder="Causa Associada"
        />
        <TextArea
          placeholder="Observações"
          name="extra.observations"
          onChange={formik.handleChange}
          value={formik.values.extra.observations}
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
      hasAdditionalHealthInsurance: false,
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
  printPdf_Apac: {
    extra: {
      procedure: {
        quantity: 1,
      },
      secondaryProcedures: [],
      diagnosis: undefined,
      secondaryDiagnosis: undefined,
      ssociatedCause: undefined,
      observations: undefined,
    },
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

const ModalAdditionalData = ({ type, confirmButton, id, ...rest }) => {
  const { handleErrors } = useHandleErrors();
  const [getPDFFicha] = useMutation(GENERATE_PDF_FICHA_INTERNAMENTO);
  const [getPDFEvolucaoCompacta] = useMutation(GENERATE_PDF_EVOLUCAO_COMPACTA);
  const [getPDFRelatorioAlta] = useMutation(GENERATE_PDF_RELATORIO_ALTA);
  const [getPDFAihSus] = useMutation(GENERATE_PDF_AIH_SUS);
  const [getPDFBalancoHidrico] = useMutation(GENERATE_PDF_BALANCO_HIDRICO);
  const [getPDFApac] = useMutation(GENERATE_PDF_APAC);

  const Strategy = strategies[type];

  const formik = useFormik({
    initialValues: initialValuesStrategies[type],
    async onSubmit(values) {
      try {
        const newValues = cloneDeep(values);
        let request = undefined;
        if (type === "printPdf_FichaInternamento") {
          request = getPDFFicha;
        }
        if (newValues.extra.interval) {
          if (newValues.extra.interval.startDatetimeStamp) {
            newValues.extra.interval.startDatetimeStamp = `${newValues.extra.interval.startDatetimeStamp}:00`;
          } else {
            newValues.extra.interval.startDatetimeStamp = null;
          }
          if (newValues.extra.interval.endingDatetimeStamp) {
            newValues.extra.interval.endingDatetimeStamp = `${newValues.extra.interval.endingDatetimeStamp}:00`;
          } else {
            newValues.extra.interval.endingDatetimeStamp = null;
          }
        }
        if (type === "printPdf_EvolucaoCompacta") {
          request = getPDFEvolucaoCompacta;
        }
        if (type === "printPdf_RelatorioAlta") {
          if (newValues.extra.datetimeStamp) {
            newValues.extra.datetimeStamp = `${newValues.extra.datetimeStamp}:00`;
          } else {
            newValues.extra.datetimeStamp = null;
          }
          if (!newValues.extra.orientations) {
            newValues.extra.orientations = null;
          }
          request = getPDFRelatorioAlta;
        }
        if (type === "printPdf_AihSus") {
          if (newValues.extra.secondaryDiagnosis?.code) {
            newValues.extra.secondaryDiagnosis = {
              code: newValues.extra.secondaryDiagnosis.code,
              description: newValues.extra.secondaryDiagnosis.description,
            };
          }
          request = getPDFAihSus;
        }
        if (type === "printPdf_BalancoHidrico") {
          request = getPDFBalancoHidrico;
        }
        if (type === "printPdf_Apac") {
          if (newValues.extra.secondaryDiagnosis?.code) {
            newValues.extra.secondaryDiagnosis = {
              code: newValues.extra.secondaryDiagnosis.code,
              description: newValues.extra.secondaryDiagnosis.description,
            };
          }
          if (newValues.extra.ssociatedCause) {
            newValues.extra.ssociatedCause = {
              code: newValues.extra.ssociatedCause.code,
              description: newValues.extra.ssociatedCause.description,
            };
          }
          if (newValues.extra.diagnosis) {
            newValues.extra.diagnosis = {
              code: newValues.extra.diagnosis.code,
              description: newValues.extra.diagnosis.description,
            };
          }
          if (newValues.extra.procedure) {
            newValues.extra.procedure = {
              code: newValues.extra.procedure.code,
              name: newValues.extra.procedure.name,
              quantity: newValues.extra.procedure.quantity,
            };
          }
          request = getPDFApac;
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
        const file = b64toBlob(
          response.data[type].base64Pdf,
          "application/pdf"
        );
        const url = URL.createObjectURL(file);
        link.href = url;
        link.setAttribute("target", "_blank");
        link.click();
      } catch (e) {
        console.log(e);
        handleErrors(e);
      }
    },
  });
  return (
    <Container onSubmit={formik.handleSubmit}>
      <Strategy confirmButton={confirmButton} formik={formik} />
    </Container>
  );
};

export default ModalAdditionalData;
