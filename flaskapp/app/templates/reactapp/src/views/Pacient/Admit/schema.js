import patientSchema from "schemas/patientSchema";
import * as Yup from "yup";

export default Yup.object().shape({
  hpi: Yup.string().required(),
  justification: Yup.string().required(),
  cid10Code: Yup.mixed().required(),
  patient: patientSchema.required(),
});
