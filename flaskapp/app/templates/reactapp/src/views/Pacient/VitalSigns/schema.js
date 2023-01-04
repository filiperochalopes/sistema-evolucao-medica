import * as Yup from "yup";

export default Yup.object().shape({
  spO2: Yup.number().moreThan(0).required(),
  pain: Yup.number().moreThan(0).required(),
  systolicBloodPressure: Yup.number().required(),
  diastolicBloodPressure: Yup.number().required(),
  cardiacFrequency: Yup.number().required(),
  respiratoryFrequency: Yup.number().required(),
  celciusAxillaryTemperature: Yup.number().required(),
  glucose: Yup.number().required(),
  fetalCardiacFrequency: Yup.number().required(),
});
