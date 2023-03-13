import Container, { Inputs } from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import { useFormik } from "formik";
import { useMutation } from "@apollo/client";
import { CREATE_FLUID_BALANCE, CREATE_MEASURE } from "graphql/mutations";
import { useParams } from "react-router-dom";
import { useSnackbar } from "notistack";
import schema from "./schema";
import CheckRole from "routes/CheckRole";

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
          pain: Number(values.pain) ? Number(values.pain) : null,
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

  return (
    <Container onSubmit={formik.handleSubmit}>
      <h2>Adicionar Dados de Sinais vitais e Balanço Hídrico</h2>
      <div className="input">
        <p>FREQUENCIA CARDÍACA:</p>
        <Inputs>
          <div>
            <div className="small">
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
            </div>
            <p>BPM</p>
          </div>
        </Inputs>
      </div>
      <div className="input">
        <p>FREQUÊNCIA RESPIRATÓRIA:</p>
        <Inputs>
          <div>
            <div className="small">
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
            </div>
            <p>IPM</p>
          </div>
        </Inputs>
      </div>
      <div className="input">
        <p>DOR (ESCALA DE 1 A 10):</p>
        <Inputs>
          <div className="small">
            <Input
              name="pain"
              value={formik.values.pain}
              onChange={formik.handleChange}
              error={
                formik.errors.pain && formik.touched.pain
                  ? formik.errors.pain
                  : ""
              }
            />
          </div>
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
          <div className="small">
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
          </div>
        </Inputs>
      </div>
      <div className="input">
        <p>PRESSÃO ARTERIAL:</p>
        <Inputs>
          <div className="small">
            <Input
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
          <div className="small">
            <Input
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
      <CheckRole roles={["nur", "tec"]}>
        <div className="input">
          <p>DADO DE BALANÇO HÍDRICO:</p>
          <Inputs>
            <div>
              <div className="small">
                <Input
                  name="volumeMl"
                  value={formik.values.volumeMl}
                  onChange={formik.handleChange}
                  error={
                    formik.errors.volumeMl && formik.touched.volumeMl
                      ? formik.errors.volumeMl
                      : ""
                  }
                />
              </div>
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
      </CheckRole>
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
          <div className="small">
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
          </div>
        </Inputs>
      </div>

      <div className="input">
        <p>Frequência Cardíaca Fetal:</p>
        <Inputs>
          <div className="small">
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
          </div>
        </Inputs>
      </div>
      <Button>Adicionar Sinais Vitais</Button>
    </Container>
  );
};

export default VitalSign;
