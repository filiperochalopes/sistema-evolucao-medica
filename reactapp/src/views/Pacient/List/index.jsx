/* eslint-disable import/order */
import Container, { PacientContent } from "./styles";

import printScreen from "helpers/printScreen";
import Button from "components/Button";
import Pacient from "components/ListOption";
import React from "react";
import { BiArchiveIn } from "react-icons/bi";
import { Link } from "react-router-dom";
import { useModalContext } from "services/ModalContext";
import EvolutionButton from "./components/EvolutionButton";
import { useQuery } from "@apollo/client";
import { INTERNMENTS } from "graphql/queries";
import { CONVERT_LABEL_SEX } from "constants/convertsexName";
import CheckRole from "routes/CheckRole";
import { useEffect } from "react";

const List = () => {
  const { data, refetch } = useQuery(INTERNMENTS, {
    fetchPolicy: "no-cache",
  });
  const { addModal } = useModalContext();

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

      <div className="pacients-container">
        <h2>Pacientes Internados</h2>
        <div className="pacients">
          {data &&
            data?.internments &&
            data?.internments.map((pacient) => (
              <Pacient key={pacient.id}>
                <PacientContent>
                  <p>
                    {pacient.patient.name} (
                    {CONVERT_LABEL_SEX[pacient.patient.sex]}){" "}
                    {pacient.patient.age}
                  </p>
                  <div className="container_buttons">
                    <Link to={`/prontuario/${pacient.id}`}>
                      <Button
                        type="button"
                        className="add_new_pacient"
                        customType="gray"
                      >
                        Visualizar
                      </Button>
                    </Link>
                    <EvolutionButton id={pacient.id} />
                    <CheckRole roles={["doc", "nur"]}>
                      <Button
                        onClick={() => {
                          addModal(printScreen(pacient.id));
                        }}
                        className="add_new_pacient"
                        customType="gray"
                      >
                        Imprimir
                      </Button>
                    </CheckRole>
                    <CheckRole roles={["nur"]}>
                      <Button customType="gray" alt="Arquivar" title="Arquivar">
                        <BiArchiveIn />
                      </Button>
                    </CheckRole>
                  </div>
                </PacientContent>
              </Pacient>
            ))}
        </div>
      </div>
    </Container>
  );
};

export default List;
