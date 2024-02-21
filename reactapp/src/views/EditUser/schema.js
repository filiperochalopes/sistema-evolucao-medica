import { ERROR_LABEL } from "constants/errorText";
import cpfSchema from "utils/cpfSchema";
import * as Yup from "yup";

export default Yup.object().shape({
  name: Yup.string().required(ERROR_LABEL),
  cpf: cpfSchema.nullable(),
  cns: Yup.string().required(ERROR_LABEL),
  password: Yup.string().min(6, "Deve ter mais que 6 caracteres").nullable(),
  passwordConfirmation: Yup.string()
    .min(6, "Deve ter mais que 6 caracteres")
    .when("password", {
      is: (value) => !!value === true,
      then: Yup.string().oneOf(
        [Yup.ref("password"), null],
        "Senhas devem coincidir"
      ),
    }),
});
