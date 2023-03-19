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
import useHandleErrors from "hooks/useHandleErrors";
import maskPhone from "utils/maskPhone";
import maskCpf from "utils/maskCpf";

import { useSnackbar } from "notistack";
const GENERS = [
  { label: "Masculino", value: "male" },
  { label: "Feminino", value: "fema" },
];

const ETHNICITYS = [
  { label: "Negra", value: "negra" },
  { label: "Parda", value: "parda" },
  { label: "Amarela", value: "amarela" },
  { label: "Branca", value: "branca" },
];

const ModalUpdatePacientData = ({ id }) => {
  const { data: allergiesData } = useQuery(ALLERGIES);
  const { data: comorbiditiesData } = useQuery(COMORBIDITIES);
  const [getPatientData, { data }] = useLazyQuery(GET_PATIENT);
  const [updatePatient] = useMutation(UPDATE_PATIENT);
  const { data: statesData } = useQuery(STATES);
  const { handleErrors } = useHandleErrors();
  const { enqueueSnackbar } = useSnackbar();
  const formik = useFormik({
    initialValues: {
      name: "",
      sex: "",
      birthdate: "",
      cpf: "",
      cns: "",
      rg: "",
      motherName: "",
      phone: "",
      comorbidities: [],
      allergies: [],
      weightKg: "",
      address: {
        zipCode: "",
        street: "",
        complement: "",
        number: "",
        city: "",
        uf: "",
      },
      ethnicity: "",
      nationality: "",
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
              cpf: values.cpf.replace(/\D/g, ""),
              ethnicity: values.ethnicity?.value,
              phone: values.phone.replace(/\D/g, ""),
            },
          },
        });
        enqueueSnackbar("Paciente Atualizado", { variant: "success" });
      } catch (e) {
        handleErrors(e);
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
    const findUf = statesData.state.find(
      (state) => state.value === data.patients[0].address.uf
    );
    const findEthnicity = ETHNICITYS.find(
      (ethnicity) => ethnicity.value === data?.patients[0].ethnicity
    );

    formik.setValues({
      allergies: data.patients[0].allergies,
      address: {
        zipcode: data.patients[0].address.zipCode,
        street: data.patients[0].address.street,
        complement: data.patients[0].address.complement,
        number: data.patients[0].address.number,
        city: data.patients[0].address.city,
        uf: findUf,
      },
      birthdate: data.patients[0].birthdate,
      cns: data.patients[0].cns,
      comorbidities: data.patients[0].comorbidities,
      cpf: maskCpf(data.patients[0].cpf),
      name: data.patients[0].name,
      motherName: data.patients[0].motherName,
      rg: data.patients[0].rg,
      phone: maskPhone(data.patients[0].phone),
      sex: GENERS.find((gener) => gener.value === data.patients[0].sex),
      weightKg: data.patients[0].weightKg,
      ethnicity: findEthnicity,
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
  console.log("formik.values", formik.values);

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
          placeholder="Nome da Mãe"
          onChange={formik.handleChange}
          value={formik.values.motherName}
          name="motherName"
          error={
            formik.errors.motherName && formik.touched.motherName
              ? formik.errors.motherName
              : ""
          }
        />
        <Input
          className="small"
          placeholder="Telefone"
          onChange={(e) => {
            const phone = maskPhone(e.target.value);
            formik.setFieldValue("phone", phone);
          }}
          value={formik.values.phone}
          name="phone"
          error={
            formik.errors.phone && formik.touched.phone
              ? formik.errors.phone
              : ""
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
          value={formik.values.address.zipCode}
          error={
            formik.errors?.address?.zipCode && formik.touched?.address?.zipCode
              ? formik.errors?.address?.zipCode
              : ""
          }
        />
      </div>
      <div className="row">
        <Input
          onChange={formik.handleChange}
          name="nationality"
          value={formik.values.nationality}
          placeholder="Nacionalidade"
          error={
            formik.errors?.nationality && formik.touched?.nationality
              ? formik.errors?.nationality
              : ""
          }
        />
        <div className="small">
          <Select
            onChange={(e) => {
              formik.setFieldValue("ethnicity", e);
            }}
            value={formik.values.ethnicity}
            placeholder="Etnia"
            options={ETHNICITYS}
            error={
              formik.errors.ethnicity && formik.touched.ethnicity
                ? formik.errors.ethnicity
                : ""
            }
          />
        </div>
      </div>
      <div className="row">
        <Input
          onChange={formik.handleChange}
          className="small"
          name="weightKg"
          value={formik.values.weightKg}
          placeholder="Peso"
          error={
            formik.errors?.weightKg && formik.touched?.weightKg
              ? formik.errors?.weightKg
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
          onChange={(e) => {
            formik.setFieldValue("cpf", maskCpf(e.target.value));
          }}
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
