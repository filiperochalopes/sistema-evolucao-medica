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
  GET_PATIENTS,
  STATES,
  GET_PATIENT,
} from "graphql/queries";
import { useEffect } from "react";
import getCepApiAdapter from "services/getCepApiAdapter";
import schema from "./schema";
import maskCpf from "utils/maskCpf";
import { useNavigate } from "react-router-dom";
import { useSnackbar } from "notistack";
import useHandleErrors from "hooks/useHandleErrors";
import maskPhone from "utils/maskPhone";

const SEX_OPTIONS = [
  { label: "Masculino", value: "male" },
  { label: "Feminino", value: "fema" },
];

const Admit = () => {
  const [createInternment] = useMutation(CREATE_INTERNMENT);
  const { data: allergiesData } = useQuery(ALLERGIES, {
    fetchPolicy: "no-cache",
  });
  const { data: comorbiditiesData } = useQuery(COMORBIDITIES, {
    fetchPolicy: "no-cache",
  });
  const { data: statesData } = useQuery(STATES);
  const { data: cid10Data } = useQuery(CID10);
  const [getPatients] = useLazyQuery(GET_PATIENTS);
  const [getPatient, { data }] = useLazyQuery(GET_PATIENT);
  const navigate = useNavigate();
  const { enqueueSnackbar } = useSnackbar();
  const { handleErrors } = useHandleErrors();
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
        motherName: "",
        address: {
          zipCode: "",
          street: "",
          complement: "",
          number: "",
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
        phone: values.patient.phone.replace(/\D/g, ""),
        cpf: values.patient.cpf.replace(/\D/g, ""),
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
      } catch (e) {
        handleErrors(e);
      }
    },
    validationSchema: schema,
  });
  const formikGetPatient = useFormik({
    initialValues: {
      patientName: "",
    },
    async onSubmit(values) {
      try {
        const response = await getPatient({
          variables: {
            queryNameCnsCpf: values.patientName,
          },
        });
        console.log(response?.data?.patients[0]?.address.complement);
      } catch {
        console.log("error");
      }
    },
  });
  console.log(formik.values);

  useEffect(() => {
    if (data && statesData?.state) {
      console.log("data", data);
      const findSex = SEX_OPTIONS.find(
        (sex) => data?.patient?.sex === sex.value
      );
      const findUf = statesData.state.find(
        (state) => state.uf === data?.patient?.address.uf
      );
      formik.setValues({
        ...formik.values,
        addPacient: true,
        patient: {
          name: data?.patient?.name,
          sex: findSex,
          birthdate: "",
          cpf: maskCpf(data?.patient?.cpf),
          cns: data?.patient?.cns,
          rg: data?.patient?.rg,
          motherName: data?.patient?.motherName,
          comorbidities: data?.patient?.comorbidities,
          allergies: data?.patient?.allergies,
          weightKg: data?.patient?.weightKg,
          phone: maskPhone(data?.patient?.phone),
          address: {
            zipCode: data?.patient?.address.zipCode,
            street: data?.patient?.address.street,
            complement: data?.patient?.address.complement,
            number: data?.patient?.address.number,
            city: data?.patient?.address.city,
            uf: findUf,
            neighborhood: data?.patient?.address.neighborhood,
          },
        },
      });
    }
  }, [data, statesData]);

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
            cpf: maskCpf(formik.values.patient.cpf),
            address: Object.assign(formik.values.patient.address, {
              ...response.data,
              uf: findUf,
            }),
          },
        });
        // eslint-disable-next-line no-empty
      } catch (e) {}
    }
    getCep();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [formik.values.patient.address.zipCode, statesData]);

  const promiseOptions = async (inputValue) => {
    const patients = await getPatients({
      variables: {
        queryNameCnsCpf: inputValue,
      },
    });
    return patients.data?.patients.map((patient) => ({
      label: patient.name,
      id: patient.id,
    }));
  };

  return (
    <Container>
      <h2>Admitir Paciente</h2>
      <ContainerSearchInput onSubmit={formikGetPatient.handleSubmit}>
        <Select
          loadOptions={promiseOptions}
          value={formikGetPatient.values.patientName}
          name="patientName"
          async
          onChange={(e) => {
            console.log("e", e);
            getPatient({
              variables: {
                id: e.id,
              },
            });
          }}
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
                error={
                  formik.errors.patient?.name && formik.touched?.patient?.name
                    ? formik.errors.patient?.name
                    : ""
                }
              />
              <Input
                onChange={formik.handleChange}
                className="small"
                name="patient.birthdate"
                value={formik.values.patient.birthdate}
                placeholder="Data de Nascimento"
                type="date"
                error={
                  formik.errors.patient?.birthdate &&
                  formik.touched?.patient?.birthdate
                    ? formik.errors.patient?.birthdate
                    : ""
                }
              />
              <Input
                onChange={formik.handleChange}
                className="small"
                name="patient.motherName"
                value={formik.values.patient.motherName}
                placeholder="Nome da Mãe"
                error={
                  formik.errors.patient?.motherName &&
                  formik.touched?.patient?.motherName
                    ? formik.errors.patient?.motherName
                    : ""
                }
              />
              <Input
                onChange={(e) => {
                  formik.setFieldValue(
                    "patient.phone",
                    maskPhone(e.target.value)
                  );
                }}
                className="small"
                name="patient.phone"
                value={formik.values.patient.phone}
                placeholder="Telefone"
                error={
                  formik.errors.patient?.phone && formik.touched?.patient?.phone
                    ? formik.errors.patient?.phone
                    : ""
                }
              />
              <Select
                onChange={(e) => {
                  formik.setFieldValue("patient.sex", e);
                  formik.setFieldTouched("patient.sex", true);
                }}
                value={formik.values.patient.sex}
                placeholder="Sexo"
                className="small"
                options={SEX_OPTIONS}
                error={
                  formik.errors.patient?.sex && formik.touched?.patient?.sex
                    ? formik.errors.patient?.sex
                    : ""
                }
              />
            </div>
            <div className="row">
              <Input
                onChange={formik.handleChange}
                className="small"
                name="patient.weightKg"
                value={formik.values.patient.weightKg}
                placeholder="Peso"
                error={
                  formik.errors.patient?.weightKg &&
                  formik.touched.patient?.weightKg
                    ? formik.errors.patient?.weightKg
                    : ""
                }
              />
              <Input
                onChange={formik.handleChange}
                className="small"
                name="patient.address.complement"
                value={formik.values.patient.address.complement}
                placeholder="Endereço"
                error={
                  formik.errors.patient?.address?.complement &&
                  formik.touched?.patient?.address?.complement
                    ? formik.errors?.patient?.address?.complement
                    : ""
                }
              />

              <Input
                onChange={formik.handleChange}
                className="small"
                name="patient.address.city"
                value={formik.values.patient.address.city}
                placeholder="Cidade"
                error={
                  formik.errors?.patient?.address?.city &&
                  formik.touched?.patient?.address?.city
                    ? formik.errors?.patient?.address?.city
                    : ""
                }
              />

              <Select
                onChange={(e) => {
                  formik.setFieldValue("patient.address.uf", e);
                  formik.setFieldTouched("patient.address.uf", true);
                }}
                className="small"
                getOptionLabel={(option) => option.name}
                getOptionValue={(option) => option.uf}
                value={formik.values?.patient?.address?.uf}
                placeholder="Estado"
                options={statesData?.state || []}
                error={
                  formik.errors?.patient?.address?.uf &&
                  formik.touched?.patient?.address?.uf
                    ? formik.errors?.patient?.address?.uf
                    : ""
                }
              />
              <Input
                onChange={formik.handleChange}
                className="small"
                name="patient.address.zipCode"
                value={formik.values?.patient?.address?.zipCode}
                placeholder="CEP"
                error={
                  formik.errors?.patient?.address?.zipCode &&
                  formik.touched?.patient?.address?.zipCode
                    ? formik.errors?.patient?.address?.zipCode
                    : ""
                }
              />
            </div>
            <div className="row">
              <Input
                onChange={formik.handleChange}
                className="small"
                value={formik.values.patient.address.neighborhood}
                name="patient.address.neighborhood"
                placeholder="Bairro"
                error={
                  formik.errors.patient?.address?.neighborhood &&
                  formik.touched?.patient?.address?.neighborhood
                    ? formik.errors?.patient?.address?.neighborhood
                    : ""
                }
              />
              <Input
                onChange={formik.handleChange}
                className="small"
                value={formik.values.patient.address.street}
                name="patient.address.street"
                placeholder="Rua"
                error={
                  formik.errors?.patient?.address?.street &&
                  formik.touched?.patient?.address?.street
                    ? formik.errors?.patient?.address?.street
                    : ""
                }
              />
              <Input
                onChange={formik.handleChange}
                className="small"
                name="patient.address.number"
                value={formik.values.patient.address.number}
                placeholder="Nº"
                error={
                  formik.errors?.patient?.address?.number &&
                  formik.touched?.patient?.address?.number
                    ? formik.errors?.patient?.address?.number
                    : ""
                }
              />
            </div>
            <div className="row">
              <Input
                onChange={formik.handleChange}
                className="normal"
                name="patient.cns"
                value={formik.values.patient.cns}
                placeholder="CNS"
                error={
                  formik.errors?.patient?.cns && formik?.touched?.patient?.cns
                    ? formik.errors?.patient?.cns
                    : ""
                }
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
                error={
                  formik.errors?.patient?.cpf && formik.touched?.patient?.cpf
                    ? formik.errors?.patient?.cpf
                    : ""
                }
              />
              <Input
                onChange={formik.handleChange}
                className="normal"
                name="patient.rg"
                value={formik.values.patient.rg}
                placeholder="RG"
                error={
                  formik.errors?.patient?.rg && formik.touched?.patient?.rg
                    ? formik.errors?.patient?.rg
                    : ""
                }
              />
            </div>
            <Select
              onChange={(e) => {
                formik.setFieldValue("patient.allergies", e);
                formik.setFieldTouched("patient.allergies", true);
              }}
              getOptionLabel={(option) => option.value}
              getOptionValue={(option) => option.id}
              value={formik.values.patient.allergies}
              placeholder="ALERGIAS"
              options={allergiesData?.allergies || []}
              isMulti
              error={
                formik.errors?.patient?.allergies &&
                formik.touched?.patient?.allergies
                  ? formik.errors?.patient?.allergies
                  : ""
              }
            />
            <Select
              onChange={(e) => {
                formik.setFieldValue("patient.comorbidities", e);
                formik.setFieldTouched("patient.comorbidities", true);
              }}
              value={formik.values.patient.comorbidities}
              placeholder="COMORBIDADES"
              getOptionLabel={(option) => option.value}
              getOptionValue={(option) => option.id}
              options={comorbiditiesData?.comorbidities || []}
              isMulti
              error={
                formik.errors?.patient?.comorbidities &&
                formik.touched?.patient?.comorbidities
                  ? formik.errors?.patient?.comorbidities
                  : ""
              }
            />
          </ContainerAddPacient>
        )}

        <div className="container_admit_data">
          <TextArea
            onChange={formik.handleChange}
            name="hpi"
            value={formik.values.hpi}
            placeholder="HISTÓRIA CLÍNICA"
            error={
              formik.errors?.hpi && formik.touched?.hpi
                ? formik.errors?.hpi
                : ""
            }
          />
          <TextArea
            onChange={formik.handleChange}
            name="justification"
            value={formik.values.justification}
            placeholder="DADOS CLÍNICOS QUE DEMONSTRAM NECESSIDADE DE INTERNAMENTO"
            error={
              formik.errors.justification && formik.touched.justification
                ? formik.errors.justification
                : ""
            }
          />
          <Select
            onChange={(e) => {
              formik.setFieldValue("cid10Code", e);
              formik.setFieldTouched("cid10Code", true);
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
            error={
              formik.errors.cid10Code && formik.touched.cid10Code
                ? formik.errors.cid10Code
                : ""
            }
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
