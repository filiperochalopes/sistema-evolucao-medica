import Container, { ContainerListOption } from "./styles";
import { createFilter, components } from "react-select";

import Button from "components/Button";
import Input from "components/Input";
import ListOption from "components/ListOption";
import TextArea from "components/TextArea";
import Select from "components/Select";
import { useModalContext } from "services/ModalContext";
import updatePacientData from "helpers/updatePacientData";
import addPrescription from "helpers/addPrescription";
import { MdModeEdit } from "react-icons/md";
import trash from "assets/trash.svg";
import deletePrescription from "helpers/deletePrescription";
import { useTheme } from "styled-components";
import { useFormik } from "formik";
import schema from "./schema";
import { useLazyQuery, useMutation, useQuery } from "@apollo/client";
import {
  CREATE_EVOLUTION,
  CREATE_PENDING,
  CREATE_PRESCRIPTION,
} from "graphql/mutations";
import { useParams } from "react-router-dom";
import { CID10, GET_INTERNMENT } from "graphql/queries";
import { useSnackbar } from "notistack";
import { useEffect } from "react";
import addMedicamentGroup from "helpers/addMedicamentGroup";

const Evolution = () => {
  const { enqueueSnackbar } = useSnackbar();
  const { addModal } = useModalContext();
  const [createPrescription] = useMutation(CREATE_PRESCRIPTION);
  const [createEvolution] = useMutation(CREATE_EVOLUTION);
  const [createPeding] = useMutation(CREATE_PENDING);
  const { data: cid10Data } = useQuery(CID10);
  const [getInternment, { data }] = useLazyQuery(GET_INTERNMENT);
  const params = useParams();
  const theme = useTheme();

  useEffect(() => {
    getInternment({
      variables: {
        internment: Number(params.id),
      },
    });
  }, [params.id]);

  const formik = useFormik({
    initialValues: {
      restingActivity: "",
      diet: "",
      drugs: [],
      nursingActivities: [],
    },
    onSubmit: async (values) => {
      try {
        const newValues = { ...values };
        newValues.drugs = newValues.drugs.map(({ id, block, ...rest }) => rest);
        await createPrescription({
          variables: { ...newValues, internmentId: Number(params.id) },
        });
        enqueueSnackbar("Prescrição Cadastrada", { variant: "success" });
      } catch {
        enqueueSnackbar("Error: Tente novamente", { variant: "error" });
      }
    },
    validationSchema: schema,
  });

  const formikEvolution = useFormik({
    initialValues: {
      text: "",
      cid10Code: null,
    },
    onSubmit: async (values) => {
      try {
        await createEvolution({
          variables: {
            cid10Code: values.cid10Code.code,
            internmentId: Number(params.id),
            text: values.text,
          },
        });

        enqueueSnackbar("Evolução Cadastrada", { variant: "success" });
      } catch {
        enqueueSnackbar("Error: Tente novamente", { variant: "error" });
      }
    },
  });

  const formikPending = useFormik({
    initialValues: {
      text: "",
    },
    onSubmit: async (values) => {
      try {
        await createPeding({
          variables: {
            internmentId: Number(params.id),
            text: values.text,
          },
        });
        enqueueSnackbar("Pendencia Cadastrada", { variant: "success" });
      } catch {
        enqueueSnackbar("Error: Tente novamente", { variant: "error" });
      }
    },
  });

  useEffect(() => {
    if (!data) {
      return;
    }
    if (data.internment?.prescriptions?.length > 0) {
      const prescription =
        data.internment?.prescriptions[
          data.internment?.prescriptions.length - 1
        ];
      formik.setValues({
        diet: prescription?.diet?.name || "",
        drugs: prescription.drugPrescriptions.map((drug) => ({
          id: drug.id,
          drugName: drug.drug.name,
          drugKind: drug.drug.kind,
          dosage: drug.dosage,
          route: drug.route,
          initialDate: drug.initialDate ? `${drug.initialDate}` : undefined,
          endingDate: drug.initialDate ? `${drug.endingDate}` : undefined,
          block: true,
        })),
        nursingActivities: prescription.nursingActivities.map(
          (nursingActivity) => nursingActivity.name
        ),
        restingActivity: prescription.restingActivity?.name || "",
      });
    }

    if (data.internment?.pendings?.length > 0) {
      formikPending.setValues({
        text: data.internment.pendings[data.internment?.pendings?.length - 1]
          .text,
      });
    }

    if (data.internment?.pendings?.length > 0) {
      formikPending.setValues({
        text: data.internment.pendings[data.internment?.pendings?.length - 1]
          .text,
      });
    }
    if (data.internment?.evolutions?.length > 0) {
      formikEvolution.setValues({
        cid10Code: data.internment.cid10,
        text: data.internment.evolutions[
          data.internment?.evolutions?.length - 1
        ].text,
      });
    }
  }, [data]);

  function chainHandleSetDrugs(values) {
    if (values.type.name === "drug") {
      formik.setFieldValue("drugs", [
        ...formik.values.drugs,
        {
          block: values.block,
          id: values.medicament.id,
          drugName: values.medicament.name,
          drugKind: values.drug.isAntibiotic,
          dosage: values.drug.useMode,
          route: values.drug.routeAdministration.value,
          initialDate: values.drug.initialDate
            ? `${values.drug.initialDate}`
            : undefined,
          endingDate: values.drug.finalDate
            ? `${values.drug.finalDate}`
            : undefined,
        },
      ]);
      return true;
    }
    throw new Error("tratamento não existe");
  }

  function chainHandleSetNursingActivity(values) {
    console.log(values);
    if (values.type.name === "nursingActivity") {
      formik.setFieldValue("nursingActivities", [
        ...formik.values.nursingActivities,
        values.medicament.name,
      ]);
      return true;
    }
    return chainHandleSetDrugs(values);
  }

  function chainHandleSetRestingActivity(values) {
    console.log(values.type);
    if (values.type.name === "restingActivity") {
      formik.setFieldValue("restingActivity", values.medicament.name);
      return true;
    }

    return chainHandleSetNursingActivity(values);
  }

  function chainHandleSetDiet(values) {
    if (values.type.name === "diet") {
      formik.setFieldValue("diet", values.medicament.name);
      return true;
    }
    return chainHandleSetRestingActivity(values);
  }

  return (
    <Container>
      <form
        className="evolution_pacient"
        onSubmit={formikEvolution.handleSubmit}
      >
        <div className="header">
          <h2>Evoluir Paciente (João Miguel dos Santos Polenta, 83 anos)</h2>
          <Button
            type="button"
            onClick={() => {
              addModal(updatePacientData(params.id));
            }}
          >
            Atualizar Dados do Paciente
          </Button>
        </div>
        <TextArea
          placeholder="EVOLUÇÃO"
          value={formikEvolution.values.text}
          name="text"
          onChange={formikEvolution.handleChange}
        />
        <div>
          <Select
            onChange={(e) => {
              formikEvolution.setFieldValue("cid10Code", e);
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
            getOptionLabel={(option) => option.description}
            getOptionValue={(option) => option.code}
            options={cid10Data?.cid10 || []}
            value={formikEvolution.values.cid10Code}
            placeholder="CID - SUSPEITA INICIAL"
          />
          <p className="legend">
            ÚLTIMA EVOLUÇÃO ATUALIZADA POR FULANO EM DD/MM/AAAA HH:DD
          </p>
        </div>

        <Button className="evolution_button">Evoluir</Button>
      </form>

      <div className="prescriptions_pacient">
        <h2>Prescrição</h2>
        <ol>
          {formik.values.diet && (
            <li>
              <ListOption>
                <ContainerListOption>
                  <p>{formik.values.diet}</p>{" "}
                  <div>
                    <button
                      onClick={() => {
                        addModal(
                          addPrescription({
                            confirmButtonAction: (values) => {
                              console.log(values);
                              formik.setFieldValue(
                                "diet",
                                values.medicament.name
                              );
                            },
                            notChangeType: true,
                            currentMedicament: {
                              type: {
                                label: "Dieta",
                                name: "diet",
                              },
                              medicament: {
                                name: formik.values.diet,
                                id: formik.values.diet,
                              },
                              drug: {
                                useMode: "",
                                routeAdministration: "",
                                isAntibiotic: "oth",
                                initialDate: "",
                                finalDate: "",
                              },
                            },
                          })
                        );
                      }}
                      type="button"
                    >
                      <MdModeEdit size={18} color={theme.colors.blue} />
                    </button>
                    <button
                      type="button"
                      onClick={() =>
                        addModal(
                          deletePrescription({
                            confirmButtonAction: () =>
                              formik.setFieldValue("diet", ""),
                          })
                        )
                      }
                    >
                      <img src={trash} alt="remover" />
                    </button>
                  </div>
                </ContainerListOption>
              </ListOption>
            </li>
          )}
          {formik.values.restingActivity && (
            <li>
              <ListOption>
                <ContainerListOption>
                  <p>{formik.values.restingActivity}</p>{" "}
                  <div>
                    <button
                      type="button"
                      onClick={() => {
                        addModal(
                          addPrescription({
                            notChangeType: true,
                            drugs: formik.values.drugs,
                            nursingActivities: formik.values.nursingActivities,
                            confirmButtonAction: (values) => {
                              console.log(values);
                              formik.setFieldValue(
                                "restingActivity",
                                values.medicament.name
                              );
                            },
                            currentMedicament: {
                              type: {
                                label: "Atividades de descanso",
                                name: "restingActivity",
                              },
                              medicament: {
                                name: formik.values.restingActivity,
                                id: formik.values.restingActivity,
                              },
                              drug: {
                                useMode: "",
                                routeAdministration: "",
                                isAntibiotic: "oth",
                                initialDate: "",
                                finalDate: "",
                              },
                              routeAdministration: undefined,
                            },
                          })
                        );
                      }}
                    >
                      <MdModeEdit size={18} color={theme.colors.blue} />
                    </button>
                    <button
                      type="button"
                      onClick={() =>
                        addModal(
                          deletePrescription({
                            confirmButtonAction: () =>
                              formik.setFieldValue("restingActivity", ""),
                          })
                        )
                      }
                    >
                      <img src={trash} alt="remover" />
                    </button>
                  </div>
                </ContainerListOption>
              </ListOption>
            </li>
          )}
          {formik.values.nursingActivities.map((nursingActivity, index) => (
            <li key={nursingActivity}>
              <ListOption>
                <ContainerListOption>
                  <p>{nursingActivity}</p>
                  <div>
                    <button
                      type="button"
                      onClick={() => {
                        addModal(
                          addPrescription({
                            notChangeType: true,
                            drugs: formik.values.drugs,

                            nursingActivities: formik.values.nursingActivities,
                            confirmButtonAction: (values) => {
                              console.log(values);
                              formik.setFieldValue(
                                `nursingActivities[${index}]`,
                                values.medicament.name
                              );
                            },
                            currentMedicament: {
                              type: {
                                label: "Atividades de enfermagem",
                                name: "nursingActivity",
                              },
                              medicament: {
                                name: nursingActivity,
                                id: nursingActivity,
                              },
                              drug: {
                                useMode: "",
                                routeAdministration: "",
                                isAntibiotic: "oth",
                                initialDate: "",
                                finalDate: "",
                              },
                              routeAdministration: undefined,
                            },
                          })
                        );
                      }}
                    >
                      <MdModeEdit size={18} color={theme.colors.blue} />
                    </button>
                    <button
                      type="button"
                      onClick={() =>
                        addModal(
                          deletePrescription({
                            confirmButtonAction: () => {
                              const filterNursingActivities =
                                formik.values.nursingActivities.filter(
                                  (value) => value === nursingActivity
                                );
                              formik.setFieldValue(
                                "nursingActivities",
                                filterNursingActivities
                              );
                            },
                          })
                        )
                      }
                    >
                      <img src={trash} alt="remover" />
                    </button>
                  </div>
                </ContainerListOption>
              </ListOption>
            </li>
          ))}
          {formik.values.drugs.map((drug, index) => (
            <li key={drug.drugName}>
              <ListOption>
                <ContainerListOption>
                  <p>{drug.drugName}</p>
                  <div>
                    <button
                      onClick={() => {
                        addModal(
                          addPrescription({
                            notChangeType: true,
                            drugs: formik.values.drugs,
                            nursingActivities: formik.values.nursingActivities,
                            confirmButtonAction: (values) => {
                              console.log(values);
                              formik.setFieldValue(`drugs[${index}]`, {
                                id: values.medicament.id,
                                drugName: values.medicament.name,
                                drugKind: values.drug.isAntibiotic,
                                dosage: values.drug.useMode,
                                route: values.drug.routeAdministration.value,
                                initialDate: values.drug.initialDate
                                  ? `${values.drug.initialDate}`
                                  : undefined,
                                endingDate: values.drug.finalDate
                                  ? `${values.drug.finalDate}`
                                  : undefined,
                                block: values.block,
                              });
                            },
                            currentMedicament: {
                              block: drug.block,
                              type: {
                                label: "Medicação",
                                name: "drug",
                              },
                              medicament: { name: drug.drugName, id: drug.id },
                              drug: {
                                useMode: drug.dosage,
                                routeAdministration: drug.route,
                                isAntibiotic: drug.drugKind,
                                initialDate: drug.initialDate,
                                finalDate: drug.endingDate,
                              },
                              routeAdministration: {
                                label: drug.route,
                                value: drug.route,
                              },
                            },
                          })
                        );
                      }}
                      type="button"
                    >
                      <MdModeEdit size={18} color={theme.colors.blue} />
                    </button>
                    <button
                      type="button"
                      onClick={() =>
                        addModal(
                          deletePrescription({
                            confirmButtonAction: () => {
                              const filterDrugs = formik.values.drugs.filter(
                                (value) => value.drugName !== drug.drugName
                              );
                              formik.setFieldValue("drugs", filterDrugs);
                            },
                          })
                        )
                      }
                    >
                      <img src={trash} alt="remover" />
                    </button>
                  </div>
                </ContainerListOption>
              </ListOption>
            </li>
          ))}
        </ol>
        <p className="legend">
          ÚLTIMA PRESCRIÇÃO ATUALIZADA EM DD/MM/AAAA HH:DD
        </p>
        <div className="buttons">
          <Button
            className="button_add_prescription"
            type="button"
            onClick={() =>
              addModal(
                addMedicamentGroup({
                  confirmButtonAction: (values) => console.log(values),
                })
              )
            }
          >
            Adicionar medicações sintomáticas
          </Button>
          <Button
            className="button_normal"
            type="button"
            onClick={() =>
              addModal(
                addPrescription({
                  drugs: formik.values.drugs,
                  nursingActivities: formik.values.nursingActivities,
                  confirmButtonAction: (values) => {
                    console.log(values);
                    chainHandleSetDiet(values);
                  },
                })
              )
            }
          >
            Adicionar nova linha
          </Button>
        </div>
        <Button
          type="button"
          onClick={() => formik.handleSubmit()}
          className="button_normal button-update_prescription"
        >
          Atualizar prescrição
        </Button>
      </div>
      <form
        onSubmit={formikPending.handleSubmit}
        className="pendencies_pacient"
      >
        <h2>Pendências</h2>
        <TextArea
          name="text"
          onChange={formikPending.handleChange}
          value={formikPending.values.text}
          placeholder="AQUI SEGUE UM TEXTO COM AS PENDÊNCIAS"
        ></TextArea>
        <p className="legend">
          ÚLTIMA PENDÊNCIA ATUALIZADA EM DD/MM/AAAA HH:DD
        </p>
        <Button className="button_normal button-update_pendencies">
          Atualizar Pendências
        </Button>
      </form>
    </Container>
  );
};

export default Evolution;
