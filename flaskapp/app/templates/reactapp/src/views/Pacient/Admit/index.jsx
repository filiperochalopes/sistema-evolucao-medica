import Container, { ContainerSearchInput, ContainerAddPacient } from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import TextArea from "components/TextArea";
import React from "react";
import { useFormik } from "formik";
import { CREATE_INTERNMENT } from "graphql/mutations";
import { useMutation } from "@apollo/client";
import Select from "components/Select";

const Admit = () => {
  const [createInternment] = useMutation(CREATE_INTERNMENT);
  const formik = useFormik({
    initialValues: {
      addPacient: false,
      admissionDatetime: "",
      hpi: "",
      justification: "",
      cid10Code: "",
      patient: {
        name: "",
        sex: "",
        birthday: "",
        cpf: "",
        cns: "",
        rg: "",
        commorbidities: [],
        allergies: [],
        address: {
          zipcode: "",
          street: "dd",
          complement: "",
          number: "32",
          city: "",
          uf: "",
        },
      },
    },
    onSubmit: (values) => {
      createInternment({ variables: values });
      console.log(values);
    },
  });

  return (
    <Container onSubmit={formik.handleSubmit}>
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
            <Input
              onChange={formik.handleChange}
              className="larger"
              name="patient.name"
              value={formik.values.patient.name}
              placeholder="Nome Completo"
            />
            <Input
              onChange={formik.handleChange}
              className="small"
              name="patient.birthday"
              value={formik.values.patient.birthday}
              placeholder="Data de Nascimento"
              type="date"
            />
            <Select
              onChange={(e) => {
                formik.setFieldValue("patient.sex", e);
              }}
              value={formik.values.patient.sex}
              placeholder="Sexo"
              className="small"
              options={[
                { label: "Masculino", value: "male" },
                { label: "Feminino", value: "female" },
              ]}
            />
          </div>
          <div className="row">
            <Input
              onChange={formik.handleChange}
              className="small"
              name="patient.address.complement"
              value={formik.values.patient.address.complement}
              placeholder="Endereço"
            />

            <Input
              onChange={formik.handleChange}
              className="small"
              name="patient.address.city"
              value={formik.values.patient.address.city}
              placeholder="Cidade"
            />
            <Input
              onChange={formik.handleChange}
              value={formik.values.patient.address.uf}
              className="small"
              name="patient.address.uf"
              placeholder="Estado"
            />
            <Input
              onChange={formik.handleChange}
              className="small"
              name="patient.address.zipcode"
              value={formik.values.patient.address.zipcode}
              placeholder="CEP"
            />
          </div>
          <div className="row">
            <Input
              onChange={formik.handleChange}
              className="small"
              value={formik.values.patient.address.street}
              name="patient.address.street"
              placeholder="Rua"
            />
            <Input
              onChange={formik.handleChange}
              className="small"
              name="patient.address.number"
              value={formik.values.patient.address.number}
              placeholder="Nº"
            />
          </div>
          <div className="row">
            <Input
              onChange={formik.handleChange}
              className="normal"
              name="patient.cns"
              value={formik.values.patient.cns}
              placeholder="CNS"
            />
            <Input
              onChange={formik.handleChange}
              className="normal"
              name="patient.cpf"
              value={formik.values.patient.cpf}
              placeholder="CPF"
            />
          </div>
          <Select
            onChange={(e) => {
              formik.setFieldValue("patient.allergies", e);
            }}
            value={formik.values.patient.allergies}
            placeholder="ALERGIAS"
            options={[
              { label: "Masculino", value: "male" },
              { label: "Feminino", value: "female" },
            ]}
            isMulti
          />
          <Select
            onChange={(e) => {
              formik.setFieldValue("patient.commorbidities", e);
            }}
            value={formik.values.patient.commorbidities}
            placeholder="COMORBIDADES"
            options={[
              { label: "Masculino", value: "male" },
              { label: "Feminino", value: "female" },
            ]}
            isMulti
          />
        </ContainerAddPacient>
      )}

      <div className="container_admit_data">
        <TextArea
          onChange={formik.handleChange}
          name="hpi"
          value={formik.values.hpi}
          placeholder="HISTÓRIA CLÍNICA"
        />
        <TextArea
          onChange={formik.handleChange}
          name="justification"
          value={formik.values.justification}
          placeholder="DADOS CLÍNICOS QUE DEMONSTRAM NECESSIDADE DE INTERNAMENTO"
        />
        <Input
          onChange={formik.handleChange}
          name="cid10Code"
          value={formik.values.cid10Code}
          placeholder="CID - SUSPEITA INICIAL"
        />
      </div>
      <Button type="submit" className="button_admit">
        Adimitir
      </Button>
    </Container>
  );
};

export default Admit;
