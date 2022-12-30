import Container from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import React from "styled-components";
import { useFormik } from "formik";
import { useLazyQuery, useMutation, useQuery } from "@apollo/client";
import { ALLERGIES, COMORBIDITIES, GET_PATIENT, STATES } from "graphql/queries";
import { useEffect } from "react";
import getCepApiAdapter from "services/getCepApiAdapter";
import Select from "components/Select";
import { UPDATE_PATIENT } from "graphql/mutations";

const ModalUpdatePacientData = ({ id }) => {
  const { data: allergiesData } = useQuery(ALLERGIES);
  const { data: comorbiditiesData } = useQuery(COMORBIDITIES);
  const [getPatientData] = useLazyQuery(GET_PATIENT);
  const [updatePatient] = useMutation(UPDATE_PATIENT);
  const { data: statesData } = useQuery(STATES);

  const formik = useFormik({
    initialValues: {
      name: "",
      sex: "",
      birthdate: "",
      cpf: "",
      cns: "",
      rg: "",
      comorbidities: [],
      allergies: [],
      weightKg: "",
      address: {
        zipcode: "",
        street: "dd",
        complement: "",
        number: "32",
        city: "",
        uf: "",
      },
    },
    onSubmit: (values) => {
      updatePatient({
        variables: {
          id: id,
          patient: {
            ...values,
            sex: values.sex.value,
            comorbidities: values.comorbidities.map(
              (commorbiditie) => commorbiditie.id
            ),
            allergies: values.allergies.map((allergie) => allergie.id),
            weightKg: parseFloat(values.weightKg),
            address: {
              ...values.address,
              uf: values.address.uf.uf,
            },
          },
        },
      });
    },
  });
  useEffect(() => {
    getPatientData({
      variables: {
        id: id,
      },
    });
  }, []);

  useEffect(() => {
    async function getCep() {
      try {
        const response = await getCepApiAdapter(formik.values.address.zipcode);
        const findUf = statesData.state.find(
          (state) => state.uf === response.data.uf
        );
        formik.setValues({
          ...formik.values,
          address: { ...response.data, uf: findUf },
        });

        // eslint-disable-next-line no-empty
      } catch (e) {
        console.log(e.message);
      }
    }
    getCep();
  }, [formik.values.address.zipcode]);

  return (
    <Container onSubmit={formik.handleSubmit}>
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
          name="birthdate"
        />
        <Select
          onChange={(e) => {
            formik.setFieldValue("sex", e);
          }}
          value={formik.values.sex}
          placeholder="Sexo"
          className="small"
          options={[
            { label: "Masculino", value: "male" },
            { label: "Feminino", value: "fema" },
          ]}
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

        <Select
          onChange={(e) => {
            formik.setFieldValue("address.uf", e);
          }}
          className="small"
          getOptionLabel={(option) => option.name}
          getOptionValue={(option) => option.uf}
          value={formik.values.address.uf}
          placeholder="Estado"
          options={statesData?.state || []}
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
          onChange={formik.handleChange}
          className="small"
          name="weightKg"
          value={formik.values.weightKg}
          placeholder="Peso"
        />

        <Input
          onChange={formik.handleChange}
          className="small"
          name="rg"
          value={formik.values.rg}
          placeholder="RG"
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
          formik.setFieldValue("comorbidities", e);
        }}
        value={formik.values.comorbidities}
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
