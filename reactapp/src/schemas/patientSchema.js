import { ERROR_LABEL } from "constants/errorText";
import * as Yup from "yup";

export default Yup.object().shape({
  name: Yup.string().required(ERROR_LABEL),
  sex: Yup.mixed().required(ERROR_LABEL),
  birthdate: Yup.string().required(ERROR_LABEL),
  cpf: Yup.string().required(ERROR_LABEL),
  cns: Yup.string().required(ERROR_LABEL),
  rg: Yup.string().required("RG é Obrigatório"),
  comorbidities: Yup.array().of(Yup.mixed()),
  allergies: Yup.array().of(Yup.mixed()),
  weightKg: Yup.string().required(ERROR_LABEL),
  address: Yup.object().shape({
    zipCode: Yup.string().required(ERROR_LABEL),
    street: Yup.string().required(ERROR_LABEL),
    complement: Yup.string(),
    number: Yup.string().required(ERROR_LABEL),
    city: Yup.string().required(ERROR_LABEL),
    uf: Yup.mixed().required(ERROR_LABEL),
    neighborhood: Yup.string().required(ERROR_LABEL),
  }),
});
