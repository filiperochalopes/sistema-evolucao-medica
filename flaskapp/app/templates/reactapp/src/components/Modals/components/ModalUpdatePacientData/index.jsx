import Container from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import React from "styled-components";

const ModalUpdatePacientData = () => (
  <Container>
    <div className="row">
      <Input className="larger" placeholder="Nome Completo" />
      <Input className="small" placeholder="Data de Nascimento" />
      <Input className="small" placeholder="Sexo" />
    </div>
    <div className="row">
      <Input className="small" placeholder="Endereço" />
      <Input className="small" placeholder="Cidade" />
      <Input className="small" placeholder="Estado" />
      <Input className="small" placeholder="CEP" />
    </div>
    <div className="row">
      <Input className="normal" placeholder="CNS" />
      <Input className="normal" placeholder="CPF" />
    </div>
    <Input placeholder="ALERGIAS" />
    <Input placeholder="COMORBIDADES" />

    <Button type="submit">Atualizar Dados do Paciente</Button>
  </Container>
);

export default ModalUpdatePacientData;
