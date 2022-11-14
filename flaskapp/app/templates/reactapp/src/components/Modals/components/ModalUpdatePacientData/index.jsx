import Container from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import React from "styled-components";
import { useFormik } from "formik";
import { useQuery } from "@apollo/client";
import { ALLERGIES, COMORBIDITIES } from "graphql/queries";
import { useEffect } from "react";
import getCepApiAdapter from "services/getCepApiAdapter";
import Select from "components/Select";

const ModalUpdatePacientData = () => {
  const { data: allergiesData } = useQuery(ALLERGIES);
  const { data: comorbiditiesData } = useQuery(COMORBIDITIES);
  const formik = useFormik({
    initialValues: {
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
  });

  useEffect(() => {
    async function getCep() {
      try {
        const response = await getCepApiAdapter(
          formik.values.patient.address.zipcode
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
  }, [formik.values.patient.address.zipcode]);

  return (
    <Container>
      <div className="row">
        <Input
          className="larger"
          placeholder="Nome Completo"
          onChange={formik.handleChange}
          name="name"
        />
        <Input
          className="small"
          placeholder="Data de Nascimento"
          onChange={formik.handleChange}
          type="date"
          name="birthday"
        />
        <Input
          className="small"
          placeholder="Sexo"
          onChange={formik.handleChange}
          name="sex"
        />
      </div>
      <div className="row">
        <Input
          className="small"
          placeholder="Endereço"
          onChange={formik.handleChange}
          name="address.complement"
        />
        <Input
          className="small"
          placeholder="Cidade"
          onChange={formik.handleChange}
          name="address.city"
        />
        <Input
          className="small"
          placeholder="Estado"
          onChange={formik.handleChange}
          name="address.uf"
        />
        <Input
          className="small"
          placeholder="CEP"
          onChange={formik.handleChange}
          name="address.zipcode"
        />
      </div>
      <div className="row">
        <Input
          className="normal"
          placeholder="CNS"
          onChange={formik.handleChange}
          name="cns"
        />
        <Input
          className="normal"
          placeholder="CPF"
          onChange={formik.handleChange}
          name="cpf"
        />
      </div>
      <Select
        onChange={(e) => {
          formik.setFieldValue("allergies", e);
        }}
        getOptionLabel={(option) => option.value}
        getOptionValue={(option) => option.id}
        value={formik.values.allergies}
        placeholder="ALERGIAS"
        options={allergiesData?.allergies || []}
        isMulti
      />
      <Select
        onChange={(e) => {
          formik.setFieldValue("commorbidities", e);
        }}
        value={formik.values.commorbidities}
        placeholder="COMORBIDADES"
        getOptionLabel={(option) => option.value}
        getOptionValue={(option) => option.id}
        options={comorbiditiesData?.comorbidities || []}
        isMulti
      />
      <Button type="submit">Atualizar Dados do Paciente</Button>
    </Container>
  );
};

export default ModalUpdatePacientData;
