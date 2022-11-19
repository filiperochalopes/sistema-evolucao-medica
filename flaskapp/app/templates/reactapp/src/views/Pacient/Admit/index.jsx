import Container, { ContainerSearchInput, ContainerAddPacient } from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import TextArea from "components/TextArea";
import React from "react";
import { useFormik } from "formik";
import { CREATE_INTERNMENT } from "graphql/mutations";
import { useMutation, useQuery } from "@apollo/client";
import Select from "components/Select";
import { ALLERGIES, CID10, COMORBIDITIES } from "graphql/queries";
import { useEffect } from "react";
import getCepApiAdapter from "services/getCepApiAdapter";

const Admit = () => {
  const [createInternment] = useMutation(CREATE_INTERNMENT);
  const { data: allergiesData } = useQuery(ALLERGIES);
  const { data: comorbiditiesData } = useQuery(COMORBIDITIES);
  const { data: cid10Data } = useQuery(CID10);
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
        comorbidities: [],
        allergies: [],
        weightKg: "",
        address: {
          zipCode: "",
          street: "dd",
          complement: "",
          number: "32",
          city: "",
          uf: "",
          neighborhood: "",
        },
      },
    },
    onSubmit: (values) => {
      const { addPacient, ...rest } = values;
      const patient = {
        ...values.patient,
        sex: values.patient.sex.value,
        comorbidities: values.patient.comorbidities.map(
          (commorbiditie) => commorbiditie.id
        ),
        allergies: values.patient.allergies.map((allergie) => allergie.id),
        weightKg: Number(values.patient.weightKg),
      };
      createInternment({
        variables: { ...rest, patient, admissionDatetime: new Date() },
      });
      console.log(values);
    },
  });

  useEffect(() => {
    async function getCep() {
      try {
        const response = await getCepApiAdapter(
          formik.values.patient.address.zipCode
        );
        formik.setValues({
          ...formik.values,
          patient: {
            ...formik.values.patient,
            address: response.data,
          },
        });
        // eslint-disable-next-line no-empty
      } catch (e) {
        console.log(e.message);
      }
    }
    getCep();
  }, [formik.values.patient.address.zipCode]);

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
              name="patient.weightKg"
              value={formik.values.patient.weightKg}
              placeholder="Peso"
            />
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
              name="patient.address.zipCode"
              value={formik.values.patient.address.zipCode}
              placeholder="CEP"
            />
          </div>
          <div className="row">
            <Input
              onChange={formik.handleChange}
              className="small"
              value={formik.values.patient.address.neighborhood}
              name="patient.address.neighborhood"
              placeholder="Bairro"
            />
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
            getOptionLabel={(option) => option.value}
            getOptionValue={(option) => option.id}
            value={formik.values.patient.allergies}
            placeholder="ALERGIAS"
            options={allergiesData?.allergies || []}
            isMulti
          />
          <Select
            onChange={(e) => {
              formik.setFieldValue("patient.comorbidities", e);
            }}
            value={formik.values.patient.comorbidities}
            placeholder="COMORBIDADES"
            getOptionLabel={(option) => option.value}
            getOptionValue={(option) => option.id}
            options={comorbiditiesData?.comorbidities || []}
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
        <Select
          onChange={(e) => {
            formik.setFieldValue("patient.cid10Code", e);
          }}
          getOptionLabel={(option) => option.description}
          getOptionValue={(option) => option.code}
          name="cid10Code"
          options={cid10Data?.cid10 || []}
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
