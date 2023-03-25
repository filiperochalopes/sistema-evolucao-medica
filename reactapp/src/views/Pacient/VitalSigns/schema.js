import * as Yup from "yup";

export default Yup.object().shape({
  spO2: Yup.number(),
  pain: Yup.number(),
  systolicBloodPressure: Yup.number(),
  diastolicBloodPressure: Yup.number(),
  cardiacFrequency: Yup.number(),
  respiratoryFrequency: Yup.number(),
  celciusAxillaryTemperature: Yup.number(),
  glucose: Yup.number(),
  fetalCardiacFrequency: Yup.number(),
});
