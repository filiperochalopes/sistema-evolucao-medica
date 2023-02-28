import patientSchema from "schemas/patientSchema";
import * as Yup from "yup";

export default Yup.object().shape({
  hpi: Yup.string().required("História Clinica é obrigatória"),
  justification: Yup.string().required("Justificativa é obrigatório"),
  cid10Code: Yup.mixed().required("Adicione Um CID"),
  patient: patientSchema.required(),
});
