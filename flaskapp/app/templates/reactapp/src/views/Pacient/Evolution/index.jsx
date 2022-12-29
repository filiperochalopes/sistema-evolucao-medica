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
import { useMutation, useQuery } from "@apollo/client";
import {
  CREATE_EVOLUTION,
  CREATE_PENDING,
  CREATE_PRESCRIPTION,
} from "graphql/mutations";
import { useParams } from "react-router-dom";
import { CID10 } from "graphql/queries";

const Evolution = () => {
  const { addModal } = useModalContext();
  const [createPrescription] = useMutation(CREATE_PRESCRIPTION);
  const [createEvolution] = useMutation(CREATE_EVOLUTION);
  const [createPeding] = useMutation(CREATE_PENDING);
  const { data: cid10Data } = useQuery(CID10);
  const params = useParams();
  const theme = useTheme();
  const formik = useFormik({
    initialValues: {
      restingActivity: "",
      diet: "",
      drugs: [],
      nursingActivities: [],
    },
    onSubmit: (values) => {
      createPrescription({
        variables: { ...values, internmentId: Number(params.id) },
      });
    },
    validationSchema: schema,
  });

  const formikEvolution = useFormik({
    initialValues: {
      text: "",
      cid10Code: null,
    },
    onSubmit: (values) => {
      createEvolution({
        variables: { ...values, internmentId: Number(params.id) },
      });
    },
  });

  const formikPending = useFormik({
    initialValues: {
      text: "",
    },
    onSubmit: (values) => {
      createPeding({
        variables: {
          internmentId: Number(params.id),
          text: values.text,
        },
      });
    },
  });

  function chainHandleSetDrugs(values) {
    if (values.type.name === "drug") {
      formik.setFieldValue("drugs", [
        ...formik.values.drugs,
        {
          drugName: values.medicament.name,
          drugKind: values.drug.isAntibiotic,
          dosage: values.drug.useMode,
          route: values.drug.routeAdministration.value,
          initialDate: values.drug.initialDate,
          endingDate: values.drug.finalDate,
        },
      ]);
      return true;
    }
    throw new Error("tratamento não existe");
  }

  function chainHandleSetNursingActivity(values) {
    if (values.type.name === "nursingActivities") {
      formik.setFieldValue("nursingActivities", [
        ...formik.values.nursingActivities,
        values.medicament.name,
      ]);
      return true;
    }
    return chainHandleSetDrugs(values);
  }

  function chainHandleSetRestingActivity(values) {
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
              addModal(updatePacientData);
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
                    <button type="button">
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
          {formik.values.nursingActivities.map((nursingActivity) => (
            <li key={nursingActivity}>
              <ListOption>
                <ContainerListOption>
                  <p>{nursingActivity}</p>
                  <div>
                    <button type="button">
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
          {formik.values.drugs.map((drug) => (
            <li key={drug.drugName}>
              <ListOption>
                <ContainerListOption>
                  <p>{drug.drugName}</p>
                  <div>
                    <button type="button">
                      <MdModeEdit size={18} color={theme.colors.blue} />
                    </button>
                    <button
                      type="button"
                      onClick={() =>
                        addModal(
                          deletePrescription({
                            confirmButtonAction: () => console.log("oi"),
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
          <Button className="button_add_prescription">
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
