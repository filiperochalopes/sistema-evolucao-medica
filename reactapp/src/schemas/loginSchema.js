import { ERROR_LABEL } from "constants/errorText";
import * as Yup from "yup";

export default Yup.object().shape({
  email: Yup.string().email("Adicione um email válido").required(ERROR_LABEL),
  password: Yup.string().required(ERROR_LABEL),
});
