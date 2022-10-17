import Container, { ContainerSearchInput, ContainerAddPacient } from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import TextArea from "components/TextArea";
import React from "react";
import { useFormik } from "formik";

const Admit = () => {
  const formik = useFormik({
    initialValues: {
      addPacient: false,
    },
  });

  return (
    <Container onSubmit={formik.handleChange}>
      <h2>Admitir Paciente</h2>
      <ContainerSearchInput>
        <Input />
        <Button customType="gray">Pesquisar</Button>
      </ContainerSearchInput>
      <Button
        className="add_pacient"
        type="button"
        onClick={() =>
          formik.setFieldValue("addPacient", !formik.values.addPacient)
        }
      >
        + Adicionar Paciente
      </Button>
      {formik.values.addPacient && (
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
      )}

      <div className="container_admit_data">
        <TextArea placeholder="HISTÓRIA CLÍNICA" />
        <TextArea placeholder="DADOS CLÍNICOS QUE DEMONSTRAM NECESSIDADE DE INTERNAMENTO" />
        <Input placeholder="CID - SUSPEITA INICIAL" />
      </div>
      <Button className="button_admit">Adimitir</Button>
    </Container>
  );
};

export default Admit;
