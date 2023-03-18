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
import { useSnackbar } from "notistack";

const GENERS = [
  { label: "Masculino", value: "male" },
  { label: "Feminino", value: "fema" },
];

const ModalUpdatePacientData = ({ id }) => {
  const { data: allergiesData } = useQuery(ALLERGIES);
  const { data: comorbiditiesData } = useQuery(COMORBIDITIES);
  const [getPatientData, { data }] = useLazyQuery(GET_PATIENT);
  const [updatePatient] = useMutation(UPDATE_PATIENT);
  const { data: statesData } = useQuery(STATES);
  const { enqueueSnackbar } = useSnackbar();

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
    onSubmit: async (values) => {
      try {
        await updatePatient({
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
      } catch (e) {
        if (e?.graphQLErrors) {
          e?.graphQLErrors.forEach((erro) => {
            enqueueSnackbar(erro.message, { variant: "error" });
          });
        }
      }
    },
  });
  useEffect(() => {
    getPatientData({
      variables: {
        id: id,
      },
    });
  }, [id, getPatientData]);

  useEffect(() => {
    if (!data || !statesData) {
      return;
    }
    const findUf = statesData.state.find((state) => data.patient.address.uf);

    formik.setValues({
      allergies: data.patient.allergies,
      address: {
        zipcode: data.patient.address.zipCode,
        street: data.patient.address.street,
        complement: data.patient.address.complement,
        number: data.patient.address.number,
        city: data.patient.address.city,
        uf: findUf,
      },
      birthdate: data.patient.birthdate,
      cns: data.patient.cns,
      comorbidities: data.patient.comorbidities,
      cpf: data.patient.cpf,
      name: data.patient.name,
      rg: data.patient.rg,
      sex: GENERS.find((gener) => gener.value === data.patient.sex),
      weightKg: data.patient.weightKg,
    });
  }, [data, statesData]);

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
          value={formik.values.name}
          error={
            formik.errors.name && formik.touched.name ? formik.errors.name : ""
          }
        />
        <Input
          className="small"
          placeholder="Data de Nascimento"
          onChange={formik.handleChange}
          type="date"
          value={formik.values.birthdate}
          name="birthdate"
          error={
            formik.errors.birthdate && formik.touched.birthdate
              ? formik.errors.birthdate
              : ""
          }
        />
        <Select
          onChange={(e) => {
            formik.setFieldValue("sex", e);
          }}
          value={formik.values.sex}
          placeholder="Sexo"
          className="small"
          options={GENERS}
          error={
            formik.errors.sex && formik.touched.sex ? formik.errors.sex : ""
          }
        />
      </div>
      <div className="row">
        <Input
          className="small"
          placeholder="Endereço"
          onChange={formik.handleChange}
          name="address.complement"
          value={formik.values.address.complement}
          error={
            formik.errors?.address?.complement &&
            formik.touched?.address.complement
              ? formik.errors?.address?.complement
              : ""
          }
        />
        <Input
          className="small"
          placeholder="Cidade"
          onChange={formik.handleChange}
          value={formik.values.address.city}
          name="address.city"
          error={
            formik.errors?.address?.city && formik.touched?.address?.city
              ? formik.errors?.address?.city
              : ""
          }
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
          error={
            formik.errors?.address?.uf && formik.touched?.address?.uf
              ? formik.errors?.address?.uf
              : ""
          }
        />
        <Input
          className="small"
          placeholder="CEP"
          onChange={formik.handleChange}
          name="address.zipcode"
          value={formik.values.address.zipcode}
          error={
            formik.errors?.address?.zipcode && formik.touched?.address?.zipcode
              ? formik.errors?.address?.zipcode
              : ""
          }
        />
      </div>
      <div className="row">
        <Input
          onChange={formik.handleChange}
          className="small"
          name="weightKg"
          value={formik.values.weightKg}
          placeholder="Peso"
          error={
            formik.errors?.address?.weightKg &&
            formik.touched?.address?.weightKg
              ? formik.errors?.address?.weightKg
              : ""
          }
        />

        <Input
          onChange={formik.handleChange}
          className="small"
          name="rg"
          value={formik.values.rg}
          placeholder="RG"
          error={formik.errors.rg && formik.touched.rg ? formik.errors.rg : ""}
        />
      </div>
      <div className="row">
        <Input
          className="normal"
          placeholder="CNS"
          onChange={formik.handleChange}
          name="cns"
          value={formik.values.cns}
          error={
            formik.errors.cns && formik.touched.cns ? formik.errors.cns : ""
          }
        />
        <Input
          className="normal"
          placeholder="CPF"
          onChange={formik.handleChange}
          value={formik.values.cpf}
          name="cpf"
          error={
            formik.errors.cpf && formik.touched.cpf ? formik.errors.cpf : ""
          }
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
        error={
          formik.errors.allergies && formik.touched.allergies
            ? formik.errors.allergies
            : ""
        }
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
        error={
          formik.errors.comorbidities && formik.touched.comorbidities
            ? formik.errors.comorbidities
            : ""
        }
      />
      <Button type="submit">Atualizar Dados do Paciente</Button>
    </Container>
  );
};

export default ModalUpdatePacientData;
