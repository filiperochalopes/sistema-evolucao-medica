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
import { CREATE_PRESCRIPTION } from "graphql/mutations";
import { useParams } from "react-router-dom";
import { CID10 } from "graphql/queries";

const Evolution = () => {
  const { addModal } = useModalContext();
  const [createPrescription] = useMutation(CREATE_PRESCRIPTION);
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

  return (
    <Container>
      <div className="evolution_pacient">
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
        <TextArea placeholder="EVOLUÇÃO" />
        <div className="row">
          <Input
            placeholder="RESPONSÁVEL PELA EVOLUÇÃO (NOME COMPLETO)"
            className="larger"
          />
          <Select className="normal" placeholder="FUNÇÃO" />
          <Input placeholder="N° CONSELHO" className="small" />
        </div>
        <div>
          <Select
            onChange={(e) => {
              formik.setFieldValue("cid10Code", e);
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
            value={formik.values.cid10Code}
            placeholder="CID - SUSPEITA INICIAL"
          />
          <p className="legend">
            ÚLTIMA EVOLUÇÃO ATUALIZADA POR FULANO EM DD/MM/AAAA HH:DD
          </p>
        </div>

        <Button className="evolution_button">Evoluir</Button>
      </div>

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
            <li>
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
            <li>
              <ListOption>
                <ContainerListOption key={drug.id}>
                  <p>{drug.medicament}</p>{" "}
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
          <li>
            <ListOption>REPOUSO RELATIVO NO LEITO À 30°</ListOption>
          </li>
          <li>
            <ListOption>REPOUSO RELATIVO NO LEITO À 30°</ListOption>
            <p className="error">
              PARA CADASTRAR UM ANTIBIÓTICO É NECESSÁRIO COLOCAR QUAL FOI O DIA
              INICIAL DE USO ESCREVENDO “D0 12/08/2022”
            </p>
          </li>
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
                  confirmButtonAction: (values) => {
                    const type = values.type.name;
                    if (type === "diet") {
                      formik.setFieldValue("diet", values.medicament.name);
                    } else if (type === "restingActivity") {
                      formik.setFieldValue(
                        "restingActivity",
                        values.medicament.name
                      );
                    } else if (type === "nursingActivity") {
                      formik.setFieldValue("nursingActivities", [
                        ...formik.values.nursingActivities,
                        values.medicament.name,
                      ]);
                    }
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
      <div className="pendencies_pacient">
        <h2>Pendências</h2>
        <TextArea placeholder="AQUI SEGUE UM TEXTO COM AS PENDÊNCIAS"></TextArea>
        <p className="legend">
          ÚLTIMA PENDÊNCIA ATUALIZADA EM DD/MM/AAAA HH:DD
        </p>
        <Button className="button_normal button-update_pendencies">
          Atualizar Pendências
        </Button>
      </div>
    </Container>
  );
};

export default Evolution;
