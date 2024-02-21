/* eslint-disable import/order */
import Container, { PatientContent } from "./styles";

import printScreen from "helpers/printScreen";
import Button from "components/Button";
import Pacient from "components/ListOption";
import React from "react";
import { BiArchiveIn } from "react-icons/bi";
import { Link } from "react-router-dom";
import { useModalContext } from "services/ModalContext";
import EvolutionButton from "./components/EvolutionButton";
import { useQuery, useMutation } from "@apollo/client";
import { INTERNMENTS } from "graphql/queries";
import { UPDATE_INTERNMENT } from "graphql/mutations";
import { CONVERT_LABEL_SEX } from "constants/convertsexName";
import CheckRole from "routes/CheckRole";
import { useEffect } from "react";
import { formatISO } from "date-fns";
import alertConfirmation from "helpers/alertConfirmation";

const List = () => {
  const { data, refetch } = useQuery(INTERNMENTS, {
    fetchPolicy: "no-cache",
  });
  const { addModal } = useModalContext();
  const [updateInternment] = useMutation(UPDATE_INTERNMENT);

  useEffect(() => {
    refetch();
  }, [refetch]);

  return (
    <Container>
      <CheckRole roles={["doc"]}>
        <Link to="/adimitir-paciente">
          <Button className="add_new_pacient">+ Admitir paciente</Button>
        </Link>
      </CheckRole>

      <div className="patients-container">
        <h2>Pacientes Internados</h2>
        <div className="patients">
          {data &&
            data?.internments &&
            data?.internments.map((internment) => (
              <Pacient key={internment.id}>
                <PatientContent>
                  <p>
                    {internment.patient.name} (
                    {CONVERT_LABEL_SEX[internment.patient.sex]}){" "}
                    {internment.patient.age}
                  </p>
                  <div className="container_buttons">
                    <Link to={`/prontuario/${internment.id}`}>
                      <Button
                        type="button"
                        className="add_new_pacient"
                        customType="gray"
                      >
                        Visualizar
                      </Button>
                    </Link>
                    <EvolutionButton id={internment.id} />
                    <CheckRole roles={["doc", "nur"]}>
                      <Button
                        onClick={() => {
                          addModal(printScreen(internment.id));
                        }}
                        className="add_new_pacient"
                        customType="gray"
                      >
                        Imprimir
                      </Button>
                    </CheckRole>
                    <CheckRole roles={["nur"]}>
                      <Button
                        onClick={() => {
                          addModal(
                            alertConfirmation({
                              question:
                                "Tem certeza que deseja arquivar o internamento? Só faça isso se o paciente tiver tido alta ou tiver sido regulado. Essa ação não poderá ser revertida.",
                              confirmCallback: async () => {
                                await updateInternment({
                                  variables: {
                                    id: internment.id,
                                    finishedAt: formatISO(new Date()),
                                  },
                                });
                              },
                            })
                          );
                        }}
                        customType="gray"
                        alt="Arquivar"
                        title="Arquivar"
                      >
                        <BiArchiveIn />
                      </Button>
                    </CheckRole>
                  </div>
                </PatientContent>
              </Pacient>
            ))}
        </div>
      </div>
      <CheckRole roles={["nur"]}>
        <div className="archived-patients">
          <h2>Pacientes Arquivados</h2>
          <div className="patients">
            <p>
              Entre em contato com o suporte para falar sobre internamentos
              fechados.
            </p>
          </div>
        </div>
      </CheckRole>
    </Container>
  );
};

export default List;
