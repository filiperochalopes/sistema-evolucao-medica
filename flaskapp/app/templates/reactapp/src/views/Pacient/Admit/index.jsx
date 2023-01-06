import Container, { ContainerSearchInput, ContainerAddPacient } from "./styles";
import { createFilter, components } from "react-select";

import Button from "components/Button";
import Input from "components/Input";
import TextArea from "components/TextArea";
import React from "react";
import { useFormik } from "formik";
import { CREATE_INTERNMENT } from "graphql/mutations";
import { useLazyQuery, useMutation, useQuery } from "@apollo/client";
import Select from "components/Select";
import {
  ALLERGIES,
  CID10,
  COMORBIDITIES,
  GET_PATIENT,
  STATES,
} from "graphql/queries";
import { useEffect } from "react";
import getCepApiAdapter from "services/getCepApiAdapter";
import schema from "./schema";
import maskCpf from "utils/maskCpf";
import { useNavigate } from "react-router-dom";
import { useSnackbar } from "notistack";

const Admit = () => {
  const [createInternment] = useMutation(CREATE_INTERNMENT);
  const { data: allergiesData } = useQuery(ALLERGIES);
  const { data: comorbiditiesData } = useQuery(COMORBIDITIES);
  const { data: statesData } = useQuery(STATES);
  const { data: cid10Data } = useQuery(CID10);
  const [getPatient] = useLazyQuery(GET_PATIENT);
  const navigate = useNavigate();
  const { enqueueSnackbar } = useSnackbar();
  const formik = useFormik({
    initialValues: {
      addPacient: false,
      hpi: "",
      justification: "",
      cid10Code: null,
      patient: {
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
          zipCode: "",
          street: "dd",
          complement: "",
          number: "32",
          city: "",
          uf: null,
          neighborhood: "",
        },
      },
    },
    onSubmit: async (values) => {
      const { addPacient, cid10Code, ...rest } = values;
      const patient = {
        ...values.patient,
        sex: values.patient.sex.value,
        comorbidities: values.patient.comorbidities.map(
          (commorbiditie) => commorbiditie.id
        ),
        allergies: values.patient.allergies.map((allergie) => allergie.id),
        weightKg: parseFloat(values.patient.weightKg),
        address: {
          ...values.patient.address,
          uf: values.patient.address.uf.uf,
        },
      };
      const dateBirthDay = new Date(patient.birthdate);
      const birthday = `${dateBirthDay.getFullYear()}-${
        dateBirthDay.getMonth() + 1
      }-${dateBirthDay.getDate()}`;
      patient.birthdate = birthday;

      const date = new Date();
      const admissionDatetime = `${date.getFullYear()}-${
        date.getMonth() + 1
      }-${date.getDate()} ${date.getHours()}:${date.getMinutes()}`;

      try {
        await createInternment({
          variables: {
            ...rest,
            patient,
            admissionDatetime,
            cid10Code: cid10Code.code,
          },
        });
        enqueueSnackbar("Pendencia Cadastrada", { variant: "success" });
        navigate("/");
      } catch {
        enqueueSnackbar("Error: Tente novamente", { variant: "error" });
      }
    },
    validationSchema: schema,
  });
  const formikGetPatient = useFormik({
    initialValues: {
      patientName: "",
    },
    onSubmit(values) {
      getPatient({
        variables: {
          queryNameCnsCpf: values.patientName,
        },
      });
    },
  });

  useEffect(() => {
    async function getCep() {
      try {
        const response = await getCepApiAdapter(
          formik.values.patient.address.zipCode
        );
        const findUf = statesData.state.find(
          (state) => state.uf === response.data.uf
        );
        formik.setValues({
          ...formik.values,
          patient: {
            ...formik.values.patient,
            cpf: formik.values.patient.cpf.replace(/\D/gi, ""),
            address: { ...response.data, uf: findUf },
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
    <Container>
      <h2>Admitir Paciente</h2>
      <ContainerSearchInput onSubmit={formikGetPatient.handleSubmit}>
        <Input
          value={formikGetPatient.values.patientName}
          name="patientName"
          onChange={formikGetPatient.handleChange}
        />
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
      <form onSubmit={formik.handleSubmit}>
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
                name="patient.birthdate"
                value={formik.values.patient.birthdate}
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
                  { label: "Feminino", value: "fema" },
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

              <Select
                onChange={(e) => {
                  formik.setFieldValue("patient.address.uf", e);
                }}
                className="small"
                getOptionLabel={(option) => option.name}
                getOptionValue={(option) => option.uf}
                value={formik.values.patient.address.uf}
                placeholder="Estado"
                options={statesData?.state || []}
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
                onChange={(e) => {
                  const cpfMask = maskCpf(e.target.value);

                  formik.setFieldValue("patient.cpf", cpfMask);
                }}
                className="normal"
                name="patient.cpf"
                value={formik.values.patient.cpf}
                placeholder="CPF"
              />
              <Input
                onChange={formik.handleChange}
                className="normal"
                name="patient.rg"
                value={formik.values.patient.rg}
                placeholder="RG"
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
              formik.setFieldValue("cid10Code", e);
            }}
            components={{
              Option: ({ children, ...props }) => {
                const { onMouseMove, onMouseOver, ...rest } = props.innerProps;
                const newProps = Object.assign(props, { innerProps: rest });
                return (
                  <components.Option {...newProps}>
                    {children}
                  </components.Option>
                );
              },
            }}
            filterOption={createFilter({ ignoreAccents: false })}
            getOptionLabel={(option) => option.description}
            getOptionValue={(option) => option.code}
            options={cid10Data?.cid10 || []}
            value={formik.values.cid10Code}
            placeholder="CID - SUSPEITA INICIAL"
          />
        </div>
        <Button type="submit" className="button_admit">
          Adimitir
        </Button>
      </form>
    </Container>
  );
};

export default Admit;
