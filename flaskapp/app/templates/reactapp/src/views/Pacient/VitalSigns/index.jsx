import Container, { Inputs } from "./styles";

import Button from "components/Button";
import Input from "components/Input";
import { useFormik } from "formik";
import { useMutation } from "@apollo/client";
import { CREATE_MEASURE } from "graphql/mutations";
import { useParams } from "react-router-dom";
import { useSnackbar } from "notistack";

const VitalSign = () => {
  const [createMeasure] = useMutation(CREATE_MEASURE);
  const { enqueueSnackbar } = useSnackbar();
  const params = useParams();
  const formik = useFormik({
    initialValues: {
      spO2: null,
      pain: null,
      systolicBloodPressure: null,
      diastolicBloodPressure: null,
      cardiacFrequency: null,
      respiratoryFrequency: null,
      celciusAxillaryTemperature: null,
      glucose: null,
      fetalCardiacFrequency: null,
    },
    onSubmit: async (values) => {
      try {
        await createMeasure({
          variables: {
            internmentId: Number(params.id),
            spO2: Number(values.spO2),
            pain: Number(values.pain),
            systolicBloodPressure: Number(values.systolicBloodPressure),
            diastolicBloodPressure: Number(values.diastolicBloodPressure),
            cardiacFrequency: Number(values.cardiacFrequency),
            respiratoryFrequency: Number(values.respiratoryFrequency),
            celciusAxillaryTemperature: Number(
              values.celciusAxillaryTemperature
            ),
            glucose: Number(values.glucose),
            fetalCardiacFrequency: Number(values.fetalCardiacFrequency),
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
            <Input
              className="small"
              name="cardiacFrequency"
              value={formik.values.cardiacFrequency}
              onChange={formik.handleChange}
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
          />
        </Inputs>
      </div>
      <div className="input">
        <p>PRESSÃO ARTERIAL:</p>
        <Inputs>
          <Input
            className="small"
            name="cardiacFrequency"
            value={formik.values.cardiacFrequency}
            onChange={formik.handleChange}
          />
        </Inputs>
      </div>
      <div className="input">
        <p>DADO DE BALANÇO HÍDRICO:</p>
        <Inputs>
          <div>
            <Input
              className="small"
              name="cardiacFrequency"
              value={formik.values.cardiacFrequency}
              onChange={formik.handleChange}
            />
            <p>ML</p>
          </div>
          <Input
            placeholder="DESCRIÇÃO"
            onChange={formik.handleChange}
            disabled
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
          />
        </Inputs>
      </div>
      <Button>Adicionar Sinais Vitais</Button>
    </Container>
  );
};

export default VitalSign;
