import Container, { Inputs } from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import { useFormik } from "formik";
import { useLazyQuery, useMutation, useQuery } from "@apollo/client";
import { CREATE_FLUID_BALANCE, CREATE_MEASURE } from "graphql/mutations";
import { useParams } from "react-router-dom";
import { useSnackbar } from "notistack";
import { GET_SINALS } from "graphql/queries";
import { useEffect } from "react";
import schema from "./schema";

const initialValues = {
  spO2: null,
  pain: null,
  systolicBloodPressure: null,
  diastolicBloodPressure: null,
  cardiacFrequency: null,
  respiratoryFrequency: null,
  celciusAxillaryTemperature: null,
  glucose: null,
  fetalCardiacFrequency: null,
  volumeMl: null,
  descriptionVolumeMl: "",
};

const VitalSign = () => {
  const [createMeasure] = useMutation(CREATE_MEASURE);
  const [createFluidBalance] = useMutation(CREATE_FLUID_BALANCE);
  const [getSinals, { data }] = useLazyQuery(GET_SINALS);
  const { enqueueSnackbar } = useSnackbar();
  const params = useParams();
  const formik = useFormik({
    initialValues,
    validationSchema: schema,
    onSubmit: async (values) => {
      try {
        const variables = {
          internmentId: Number(params.id),
          spO2: values.spO2 > 0 ? Number(values.spO2) : null,
          pain: Number(values.pain),
          systolicBloodPressure: Number(values.systolicBloodPressure),
          diastolicBloodPressure: Number(values.diastolicBloodPressure),
          cardiacFrequency: Number(values.cardiacFrequency),
          respiratoryFrequency: Number(values.respiratoryFrequency),
          celciusAxillaryTemperature: Number(values.celciusAxillaryTemperature),
          glucose: Number(values.glucose),
          fetalCardiacFrequency: Number(values.fetalCardiacFrequency),
        };
        await createMeasure({
          variables,
        });
        await createFluidBalance({
          variables: {
            internmentId: Number(params.id),
            volumeMl: Number(values.volumeMl),
            description: values.descriptionVolumeMl,
          },
        });
        enqueueSnackbar("Prescrição Cadastrada", { variant: "success" });
      } catch {
        enqueueSnackbar("Error: Tente novamente", { variant: "error" });
      }
    },
  });

  useEffect(() => {
    if (!data) {
      return;
    }
    let object = initialValues;
    if (data.internment?.measures?.length > 0) {
      const measure = data.internment.measures[0];
      object = {
        cardiacFrequency: measure.cardiacFrequency,
        celciusAxillaryTemperature: measure.celciusAxillaryTemperature,
        diastolicBloodPressure: measure.diastolicBloodPressure,
        fetalCardiacFrequency: measure.fetalCardiacFrequency,
        glucose: measure.glucose,
        pain: measure.pain,
        respiratoryFrequency: measure.respiratoryFrequency,
        systolicBloodPressure: measure.systolicBloodPressure,
        spO2: measure.spO2,
        descriptionVolumeMl: "",
        volumeMl: 0,
      };
    }
    if (data.internment?.fluidBalance?.length > 0) {
      const fluidBalance = data.internment.fluidBalance[0];
      object.volumeMl = fluidBalance.volumeMl;
      object.descriptionVolumeMl = fluidBalance?.description?.value;
    }
    formik.setValues(object);
  }, [data]);

  useEffect(() => {
    getSinals({
      variables: {
        internment: params.id,
      },
    });
  }, []);

  return (
    <Container onSubmit={formik.handleSubmit}>
      <h2>Adicionar Dados de Sinais vitais e Balanço Hídrico</h2>
      <div className="input">
        <p>FREQUENCIA CARDÍACA:</p>
        <Inputs>
          <div>
            <Input
              className="small"
              name="cardiacFrequency"
              value={formik.values.cardiacFrequency}
              onChange={formik.handleChange}
              error={
                formik.errors.cardiacFrequency &&
                formik.touched.cardiacFrequency
                  ? formik.errors.cardiacFrequency
                  : ""
              }
            />
            <p>BPM</p>
          </div>
        </Inputs>
      </div>
      <div className="input">
        <p>FREQUÊNCIA RESPIRATÓRIA:</p>
        <Inputs>
          <div>
            <Input
              className="small"
              name="respiratoryFrequency"
              value={formik.values.respiratoryFrequency}
              onChange={formik.handleChange}
              error={
                formik.errors.respiratoryFrequency &&
                formik.touched.respiratoryFrequency
                  ? formik.errors.respiratoryFrequency
                  : ""
              }
            />
            <p>IPM</p>
          </div>
        </Inputs>
      </div>
      <div className="input">
        <p>DOR (ESCALA DE 1 A 10):</p>
        <Inputs>
          <Input
            className="small"
            name="pain"
            value={formik.values.pain}
            onChange={formik.handleChange}
            error={
              formik.errors.pain && formik.touched.pain
                ? formik.errors.pain
                : ""
            }
          />
          <Input
            placeholder="LOCALIZAÇÃO DA DOR"
            onChange={formik.handleChange}
            disabled
          />
        </Inputs>
      </div>
      <div className="input">
        <p>TEMPERATURA AXILAR:</p>
        <Inputs>
          <Input
            className="small"
            name="celciusAxillaryTemperature"
            value={formik.values.celciusAxillaryTemperature}
            onChange={formik.handleChange}
            error={
              formik.errors.celciusAxillaryTemperature &&
              formik.touched.celciusAxillaryTemperature
                ? formik.errors.celciusAxillaryTemperature
                : ""
            }
          />
        </Inputs>
      </div>
      <div className="input">
        <p>PRESSÃO ARTERIAL:</p>
        <Inputs>
          <div>
            <Input
              className="small"
              name="systolicBloodPressure"
              value={formik.values.systolicBloodPressure}
              onChange={formik.handleChange}
              error={
                formik.errors.systolicBloodPressure &&
                formik.touched.systolicBloodPressure
                  ? formik.errors.systolicBloodPressure
                  : ""
              }
            />
          </div>
          <div>
            <Input
              className="small"
              name="diastolicBloodPressure"
              value={formik.values.diastolicBloodPressure}
              onChange={formik.handleChange}
              error={
                formik.errors.diastolicBloodPressure &&
                formik.touched.diastolicBloodPressure
                  ? formik.errors.diastolicBloodPressure
                  : ""
              }
            />
          </div>
        </Inputs>
      </div>
      <div className="input">
        <p>DADO DE BALANÇO HÍDRICO:</p>
        <Inputs>
          <div>
            <Input
              className="small"
              name="volumeMl"
              value={formik.values.volumeMl}
              onChange={formik.handleChange}
              error={
                formik.errors.volumeMl && formik.touched.volumeMl
                  ? formik.errors.volumeMl
                  : ""
              }
            />
            <p>ML</p>
          </div>
          <Input
            placeholder="DESCRIÇÃO"
            onChange={formik.handleChange}
            name="descriptionVolumeMl"
            value={formik.values.descriptionVolumeMl}
            error={
              formik.errors.descriptionVolumeMl &&
              formik.touched.descriptionVolumeMl
                ? formik.errors.descriptionVolumeMl
                : ""
            }
          />
        </Inputs>
      </div>
      <div className="input">
        <p>GLICEMIA PERIFÉRICA:</p>
        <Inputs>
          <Input
            className="small"
            name="glucose"
            value={formik.values.glucose}
            onChange={formik.handleChange}
            error={
              formik.errors.glucose && formik.touched.glucose
                ? formik.errors.glucose
                : ""
            }
          />
        </Inputs>
      </div>

      <div className="input">
        <p>Saturação P. de O2:</p>
        <Inputs>
          <Input
            className="small"
            name="spO2"
            value={formik.values.spO2}
            onChange={formik.handleChange}
            error={
              formik.errors.spO2 && formik.touched.spO2
                ? formik.errors.spO2
                : ""
            }
          />
        </Inputs>
      </div>

      <div className="input">
        <p>Frequência Cardíaca Fetal:</p>
        <Inputs>
          <Input
            className="small"
            name="fetalCardiacFrequency"
            value={formik.values.fetalCardiacFrequency}
            onChange={formik.handleChange}
            error={
              formik.errors.fetalCardiacFrequency &&
              formik.touched.fetalCardiacFrequency
                ? formik.errors.fetalCardiacFrequency
                : ""
            }
          />
        </Inputs>
      </div>
      <Button>Adicionar Sinais Vitais</Button>
    </Container>
  );
};

export default VitalSign;
