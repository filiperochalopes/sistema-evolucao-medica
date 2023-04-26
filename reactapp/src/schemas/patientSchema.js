import { ERROR_LABEL } from "constants/errorText";
import * as Yup from "yup";

export default Yup.object().shape({
  name: Yup.string().required(ERROR_LABEL),
  sex: Yup.mixed().required(ERROR_LABEL),
  birthdate: Yup.string().required(ERROR_LABEL),
  cpf: Yup.string(),
  cns: Yup.string().required(ERROR_LABEL),
  phone: Yup.string().required(ERROR_LABEL),
  comorbidities: Yup.array().of(Yup.mixed()),
  allergies: Yup.array().of(Yup.mixed()),
  weightKg: Yup.string().required(ERROR_LABEL),
  address: Yup.object().shape({
    zipCode: Yup.string(),
    street: Yup.string(),
    complement: Yup.string(),
    number: Yup.string().nullable(),
    city: Yup.string(),
    uf: Yup.mixed(),
    neighborhood: Yup.string().nullable(),
  }),
  motherName: Yup.string().required(ERROR_LABEL),
});
