import * as Yup from "yup";

export default Yup.object().shape({
  name: Yup.string().required(),
  sex: Yup.mixed().required(),
  birthday: Yup.string().required(),
  cpf: Yup.string().required(),
  cns: Yup.string().required(),
  rg: Yup.string().required(),
  comorbidities: Yup.array().of(Yup.mixed()),
  allergies: Yup.array().of(Yup.mixed()),
  weightKg: Yup.string().required(),
  address: Yup.object().shape({
    zipCode: Yup.string().required(),
    street: Yup.string().required(),
    complement: Yup.string().required(),
    number: Yup.string().required(),
    city: Yup.string().required(),
    uf: Yup.string().required(),
    neighborhood: Yup.string().required(),
  }),
});
