import { ERROR_LABEL } from "constants/errorText";
import * as Yup from "yup";

export default Yup.object().shape({
  name: Yup.string(),
  sex: Yup.mixed().required(ERROR_LABEL),
  birthdate: Yup.string().required(ERROR_LABEL),
  cpf: Yup.string(),
  cns: Yup.string().required(ERROR_LABEL),
  rg: Yup.string(),
  phone: Yup.string(),
  comorbidities: Yup.array().of(Yup.mixed()),
  allergies: Yup.array().of(Yup.mixed()),
  weightKg: Yup.string().required(ERROR_LABEL),
  address: Yup.object().shape({
    zipCode: Yup.string(),
    street: Yup.string(),
    complement: Yup.string(),
    number: Yup.string(),
    city: Yup.string(),
    uf: Yup.mixed(),
    neighborhood: Yup.string(),
  }),
  motherName: Yup.string().required(ERROR_LABEL),
});
