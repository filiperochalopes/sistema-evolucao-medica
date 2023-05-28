import * as Yup from "yup";
import validateCPF from "./validateCPF";

const cpfSchema = Yup.string().test(
  "test-validar-cpf",
  "CPF inválido",
  (value) => {
    try {
      if (!value) {
        // Se o valor não foi preenchido, não precisa validar
        return true;
      }
      const cpf = value.replace(/[^\d]+/g, "");
      validateCPF(cpf);

      return true;
    } catch {
      return false;
    }
  }
);

export default cpfSchema;
