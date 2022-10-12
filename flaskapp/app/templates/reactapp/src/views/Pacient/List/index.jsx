import Container, { PacientContent } from "./styles";

import Button from "components/Button";
import Pacient from "components/ListOption";
import React from "react";
import { Link } from "react-router-dom";

const List = () => (
  <Container>
    <Link to="/">
      <Button className="add_new_pacient">+ Admitir paciente</Button>
    </Link>

    <div className="pacients-container">
      <h2>Pacientes Internados</h2>
      <div className="pacients">
        <Pacient>
          <PacientContent>
            <p>Nome Completo, masculino, 80 anos</p>
            <div className="container_buttons">
              <Button className="add_new_pacient" customType="gray">
                Visualizar
              </Button>
              <div className="container_button_relative">
                <Button className="add_new_pacient" customType="gray">
                  Evoluir
                </Button>
              </div>
              <Button className="add_new_pacient" customType="gray">
                Imprimir
              </Button>
            </div>
          </PacientContent>
        </Pacient>
      </div>
    </div>
    <Button className="config">Configurações</Button>
  </Container>
);

export default List;
