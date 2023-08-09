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
import {
  CID10,
  GET_HIGH_COMPLEXITY_PROCEDURES,
  INTERNMENT_PRESCRIPTIONS,
  INTERNMENT_EVOLUTIONS,
  INTERNMENT_PENDINGS,
} from "graphql/queries";
import { useState } from "react";
import b64toBlob from "utils/b64toBlob";
import useHandleErrors from "hooks/useHandleErrors";
import { useEffect } from "react";
import GroupInput from "../GroupInput";
import { get24ShiftDatetimeInterval } from "./components/Interval";
import { useContextProvider } from "services/Context";

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
  APAC: () => (
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
  printPdf_EvolucaoCompacta: ({ formik, extra: { internmentId } }) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks

    /**
     * Capturando as prescrições do internamento em questão
     */
    const { data: prescriptionsData } = useQuery(INTERNMENT_PRESCRIPTIONS, {
      variables: { internmentId },
    });
    // Todas as prescrições carregadas
    const [prescriptions, setPrescriptions] = useState([]);
    // Prescrições realizadas pelo usuário dentro do intervalo do turno/plantão
    const [inTimePrescriptions, setInTimePrescriptions] = useState([]);
    /**
     * Capturando as evoluções do internamento em questão
     */
    const { data: evolutionsData } = useQuery(INTERNMENT_EVOLUTIONS, {
      variables: { internmentId },
    });
    // Todas as evoluções carregadas
    const [evolutions, setEvolutions] = useState([]);
    // Evoluções realizadas pelo usuário dentro do intervalo do turno/plantão
    const [inTimeEvolutions, setInTimeEvolutions] = useState([]);
    /**
     * Capturando as pendências do internamento em questão
     */
    const { data: pendingsData } = useQuery(INTERNMENT_PENDINGS, {
      variables: { internmentId },
    });
    // Todas as pendências carregadas
    const [pendings, setPendings] = useState([]);
    // Prescrições realizadas dentro do intervalo do turno/plantão
    const [inTimePendings, setInTimePendings] = useState([]);
    // Usuárion logado
    const { user } = useContextProvider();

    useEffect(() => {
      // Realizando refatoração dos dados recebidos de prescrição, capturando e organizando apenas os dados do usuário logado no período do plantão
      if (prescriptionsData)
        setPrescriptions(
          prescriptionsData?.internment.prescriptions
            .filter((p) => p.professional.id === user.id)
            .reduce(
              (acc, cur) => [
                {
                  ...cur,
                  description: `${cur.restingActivity.name} - ${
                    cur.diet.name
                  } - ${cur.drugPrescriptions.map(
                    (dp) => `${dp.drug.name} - ${dp.drug.dosage} ·`
                  )}`,
                },
                ...acc,
              ],
              []
            )
        );
    }, [prescriptionsData]);

    useEffect(() => {
      // Realizando refatoração dos dados recebidos de evoluções, capturando e organizando apenas os dados do usuário logado no período do plantão
      if (evolutionsData)
        setEvolutions(
          evolutionsData?.internment.evolutions.filter(
            (p) => p.professional.id === user.id
          )
        );
    }, [evolutionsData]);

    useEffect(() => {
      // Realizando refatoração dos dados recebidos de pendências, capturando e organizando apenas os dados do usuário logado no período do plantão
      if (pendingsData)
        setPendings(
          pendingsData?.internment.pendings
            .filter((p) => p.professional.id === user.id)
            .reduce(
              (acc, cur) => [
                {
                  ...cur,
                  description: `${cur.text} - ${cur.createdAt}`,
                },
                ...acc,
              ],
              []
            )
        );
    }, [pendingsData]);

    useEffect(() => {
      if (prescriptions?.length) {
        // Filtrando por último período
        const fullShiftDatetimeInterval = get24ShiftDatetimeInterval();
        const getInTimeItems = (items) =>
          items.filter(
            (i) =>
              new Date(i.createdAt) >=
              new Date(fullShiftDatetimeInterval.startDatetimeStamp)
          );
        if (!inTimePrescriptions.length) {
          setInTimePrescriptions(getInTimeItems(prescriptions));
        }
        if (!inTimeEvolutions.length) {
          setInTimeEvolutions(getInTimeItems(evolutions));
        }
        if (!inTimePendings.length) {
          setInTimePendings(getInTimeItems(pendings));
        }
      }
    }, [prescriptions, evolutions, pendings]);

    // Retorna as prescrições realizadas
    return (
      <>
        <section>
          <h3>Prescrições</h3>
          {inTimePrescriptions.length ? (
            inTimePrescriptions?.map((p) => (
              <GroupInput
                optionId={p.id}
                name="extra.prescriptionId"
                id={`prescription-${p.id}`}
                onChange={formik.handleChange}
                description={
                  <div>
                    <h4>{p.createdAt}</h4>
                    <p>{p.description}</p>
                  </div>
                }
              />
            ))
          ) : (
            <p>
              Não existem prescrições realizadas nesse plantão por esse usuário,{" "}
              <a href={`/evoluir-paciente/${internmentId}`}>
                atualize a prescrição
              </a>{" "}
              para poder realizar a impressão.
            </p>
          )}
        </section>
        <section>
          <h3>Evoluções</h3>
          {inTimeEvolutions.length ? (
            inTimeEvolutions?.map((p) => (
              <GroupInput
                optionId={p.id}
                name="extra.evolutionId"
                id={`evolution-${p.id}`}
                onChange={formik.handleChange}
                description={
                  <div>
                    <h4>{p.createdAt}</h4>
                    <p>{p.text}</p>
                  </div>
                }
              />
            ))
          ) : (
            <p>
              Não existem evoluções realizadas nesse plantão por esse usuário,{" "}
              <a href={`/evoluir-paciente/${internmentId}`}>
                atualize a evolução
              </a>{" "}
              para poder realizar a impressão.
            </p>
          )}
        </section>
        <section>
          <h3>Pendências</h3>
          {inTimePendings.length ? (
            inTimePendings?.map((p) => (
              <GroupInput
                optionId={p.id}
                name="extra.pendingsId"
                id={`pendings-${p.id}`}
                onChange={formik.handleChange}
                description={
                  <div>
                    <h4>{p.createdAt}</h4>
                    <p>{p.text}</p>
                  </div>
                }
              />
            ))
          ) : (
            <p>
              Não existem pendências realizadas nesse plantão por esse usuário,{" "}
              <a href={`/evoluir-paciente/${internmentId}`}>
                atualize as pendências
              </a>{" "}
              para poder realizar a impressão.
            </p>
          )}
        </section>
        <ButtonContainer>
          <Button type="submit">Confirmar</Button>
        </ButtonContainer>
      </>
    );
  },
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

// Valores iniciais dos formulários e envios formik de cada formulário
const initialValuesStrategies = {
  printPdf_FichaInternamento: {
    extra: {
      hasAdditionalHealthInsurance: false,
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
  printPdf_EvolucaoCompacta: {
    extra: {
      prescriptionId: null,
      evolutionId: null,
      pendingsId: null,
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

/**
 * Modal de dados adicionais, reúne o grupo de modais disponíveis para impressão de arquivos que necessitam de dados adicionais para processamento.
 *
 * @param {*} props type = Tipo do Modal
 * @returns Modal com formulário útil
 */
const ModalAdditionalData = ({ type, id: internmentId, ...rest }) => {
  const { handleErrors } = useHandleErrors();
  const [getPDFFicha] = useMutation(GENERATE_PDF_FICHA_INTERNAMENTO);
  const [getPDFEvolucaoCompacta] = useMutation(GENERATE_PDF_EVOLUCAO_COMPACTA);
  const [getPDFRelatorioAlta] = useMutation(GENERATE_PDF_RELATORIO_ALTA);
  const [getPDFAihSus] = useMutation(GENERATE_PDF_AIH_SUS);
  const [getPDFBalancoHidrico] = useMutation(GENERATE_PDF_BALANCO_HIDRICO);
  const [getPDFApac] = useMutation(GENERATE_PDF_APAC);

  // TODO Otimizar nomes como strategy e organização de informações, para editar um modal está sendo necessário realizar muitos arrodeios, talvez um conteiner Wrap seja mais interessantes do que todo esse arrodeio de hooks
  // Configura estratégia usada na renderização que está mais para definição do conteúdo por mio da string
  const Strategy = strategies[type];

  // TODO FormikModalWrap?
  // Formik utilizado em todos os formulários.
  const formik = useFormik({
    initialValues: initialValuesStrategies[type],
    async onSubmit(values) {
      try {
        // ! Pq esse deep clone?
        const valuesDeepClone = cloneDeep(values);
        console.log(values, valuesDeepClone);
        let request = undefined;
        if (type === "printPdf_FichaInternamento") {
          request = getPDFFicha;
        }
        if (valuesDeepClone.extra && valuesDeepClone.extra.interval) {
          if (valuesDeepClone.extra.interval.startDatetimeStamp) {
            valuesDeepClone.extra.interval.startDatetimeStamp = `${valuesDeepClone.extra.interval.startDatetimeStamp}:00`;
          } else {
            valuesDeepClone.extra.interval.startDatetimeStamp = null;
          }
          if (valuesDeepClone.extra.interval.endingDatetimeStamp) {
            valuesDeepClone.extra.interval.endingDatetimeStamp = `${valuesDeepClone.extra.interval.endingDatetimeStamp}:00`;
          } else {
            valuesDeepClone.extra.interval.endingDatetimeStamp = null;
          }
        }
        if (type === "printPdf_EvolucaoCompacta") {
          valuesDeepClone.extra.pendingsId = parseInt(
            valuesDeepClone.extra.pendingsId
          );
          valuesDeepClone.extra.evolutionId = parseInt(
            valuesDeepClone.extra.evolutionId
          );
          valuesDeepClone.extra.prescriptionId = parseInt(
            valuesDeepClone.extra.prescriptionId
          );
          request = getPDFEvolucaoCompacta;
        }
        if (type === "printPdf_RelatorioAlta") {
          if (valuesDeepClone.extra.datetimeStamp) {
            valuesDeepClone.extra.datetimeStamp = `${valuesDeepClone.extra.datetimeStamp}:00`;
          } else {
            valuesDeepClone.extra.datetimeStamp = null;
          }
          if (!valuesDeepClone.extra.orientations) {
            valuesDeepClone.extra.orientations = null;
          }
          request = getPDFRelatorioAlta;
        }
        if (type === "printPdf_AihSus") {
          if (valuesDeepClone.extra.secondaryDiagnosis?.code) {
            valuesDeepClone.extra.secondaryDiagnosis = {
              code: valuesDeepClone.extra.secondaryDiagnosis.code,
              description: valuesDeepClone.extra.secondaryDiagnosis.description,
            };
          }
          request = getPDFAihSus;
        }
        if (type === "printPdf_BalancoHidrico") {
          request = getPDFBalancoHidrico;
        }
        if (type === "printPdf_Apac") {
          if (valuesDeepClone.extra.secondaryDiagnosis?.code) {
            valuesDeepClone.extra.secondaryDiagnosis = {
              code: valuesDeepClone.extra.secondaryDiagnosis.code,
              description: valuesDeepClone.extra.secondaryDiagnosis.description,
            };
          }
          if (valuesDeepClone.extra.ssociatedCause) {
            valuesDeepClone.extra.ssociatedCause = {
              code: valuesDeepClone.extra.ssociatedCause.code,
              description: valuesDeepClone.extra.ssociatedCause.description,
            };
          }
          if (valuesDeepClone.extra.diagnosis) {
            valuesDeepClone.extra.diagnosis = {
              code: valuesDeepClone.extra.diagnosis.code,
              description: valuesDeepClone.extra.diagnosis.description,
            };
          }
          if (valuesDeepClone.extra.procedure) {
            valuesDeepClone.extra.procedure = {
              code: valuesDeepClone.extra.procedure.code,
              name: valuesDeepClone.extra.procedure.name,
              quantity: valuesDeepClone.extra.procedure.quantity,
            };
          }
          request = getPDFApac;
        }
        if (!request) {
          return;
        }
        const response = await request({
          variables: {
            // id do internamento sempre é passado para todas as mutations
            internmentId: Number(internmentId),
            extra: { ...valuesDeepClone.extra },
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
      <Strategy formik={formik} extra={{ ...rest, internmentId }} />
    </Container>
  );
};

export default ModalAdditionalData;
