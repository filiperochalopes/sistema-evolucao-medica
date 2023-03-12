import { ERROR_LABEL } from "constants/errorText";
import * as Yup from "yup";

export default Yup.object().shape({
  spO2: Yup.number().moreThan(0).required(ERROR_LABEL),
  pain: Yup.number().moreThan(0).required(ERROR_LABEL),
  systolicBloodPressure: Yup.number().required(ERROR_LABEL),
  diastolicBloodPressure: Yup.number().required(ERROR_LABEL),
  cardiacFrequency: Yup.number().required(ERROR_LABEL),
  respiratoryFrequency: Yup.number().required(ERROR_LABEL),
  celciusAxillaryTemperature: Yup.number().required(ERROR_LABEL),
  glucose: Yup.number().required(ERROR_LABEL),
  fetalCardiacFrequency: Yup.number().required(ERROR_LABEL),
});
