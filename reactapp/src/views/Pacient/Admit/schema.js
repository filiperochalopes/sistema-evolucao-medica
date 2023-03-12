import { ERROR_LABEL } from "constants/errorText";
import patientSchema from "schemas/patientSchema";
import * as Yup from "yup";

export default Yup.object().shape({
  hpi: Yup.string().required(ERROR_LABEL),
  justification: Yup.string().required(ERROR_LABEL),
  cid10Code: Yup.mixed().required(ERROR_LABEL),
  patient: patientSchema.required(),
});
