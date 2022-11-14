/* eslint-disable import/order */
import Container, { PacientContent } from "./styles";

import printScreen from "helpers/printScreen";
import Button from "components/Button";
import Pacient from "components/ListOption";
import React from "react";
import { Link } from "react-router-dom";
import { useModalContext } from "services/ModalContext";
import EvolutionButton from "./components/EvolutionButton";
import { useQuery } from "@apollo/client";
import { PATIENTS } from "graphql/queries";

const List = () => {
  const { data } = useQuery(PATIENTS);
  const { addModal } = useModalContext();
  return (
    <Container>
      <Link to="/adimitir-paciente">
        <Button className="add_new_pacient">+ Admitir paciente</Button>
      </Link>

      <div className="pacients-container">
        <h2>Pacientes Internados</h2>
        <div className="pacients">
          {data &&
            data?.pacients &&
            data?.pacients.map((pacient) => (
              <Pacient key={pacient.id}>
                <PacientContent>
                  <p>Nome Completo, masculino, 80 anos</p>
                  <div className="container_buttons">
                    <Link to="/prontuario">
                      <Button
                        type="button"
                        className="add_new_pacient"
                        customType="gray"
                      >
                        Visualizar
                      </Button>
                    </Link>
                    <EvolutionButton />
                    <Button
                      onClick={() => {
                        addModal(printScreen);
                      }}
                      className="add_new_pacient"
                      customType="gray"
                    >
                      Imprimir
                    </Button>
                  </div>
                </PacientContent>
              </Pacient>
            ))}
        </div>
      </div>
      <Button className="config">Configurações</Button>
    </Container>
  );
};

export default List;
