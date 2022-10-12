import Container, {
  ContainerSearchInput,
  ContainerAddPacient,
  ContainerInputs,
} from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import TextArea from "components/TextArea";
import React from "react";

const Admit = () => (
  <Container>
    <h2>Admitir Paciente</h2>
    <ContainerSearchInput>
      <Input />
      <Button customType="gray">Pesquisar</Button>
    </ContainerSearchInput>
    <Button className="add_pacient">+ Adicionar Paciente</Button>
    <ContainerAddPacient>
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
    </ContainerAddPacient>

    <div className="container_admit_data">
      <TextArea placeholder="HISTÓRIA CLÍNICA" />
      <TextArea placeholder="DADOS CLÍNICOS QUE DEMONSTRAM NECESSIDADE DE INTERNAMENTO" />
      <Input placeholder="CID - SUSPEITA INICIAL" />
    </div>
    <h2>Profissional responsável</h2>
    <ContainerInputs>
      <div className="row">
        <Input className="normal" placeholder="Nome Completo" />
        <Input className="normal" placeholder="Data de Nascimento" />
        <Input className="normal" placeholder="Sexo" />
      </div>
    </ContainerInputs>
    <Button className="button_admit">Adimitir</Button>
  </Container>
);

export default Admit;
