import * as Yup from "yup";

export default Yup.object().shape({
  name: Yup.string().required("Nome é Obrigatório"),
  sex: Yup.mixed().required("Genêro é obrigatório"),
  birthdate: Yup.string().required("Data de nascimento é obrigatório"),
  cpf: Yup.string().required("Cpf é Obrigatório"),
  cns: Yup.string().required("Cns é Obrigatório"),
  rg: Yup.string().required("RG é Obrigatório"),
  comorbidities: Yup.array().of(Yup.mixed()),
  allergies: Yup.array().of(Yup.mixed()),
  weightKg: Yup.string().required("Peso é Obrigatório"),
  address: Yup.object().shape({
    zipCode: Yup.string().required("Adicione um cep"),
    street: Yup.string().required("Adicione uma Rua"),
    complement: Yup.string(),
    number: Yup.string().required("Adicione um númro"),
    city: Yup.string().required("Adicione uma cidade"),
    uf: Yup.mixed().required("Adicione um estado"),
    neighborhood: Yup.string().required("Adicione um Bairro"),
  }),
});
