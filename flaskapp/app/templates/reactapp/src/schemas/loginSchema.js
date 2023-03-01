import { ERROR_LABEL } from "constants/errorText";
import * as Yup from "yup";

export default Yup.object().shape({
  email: Yup.string().email().required(ERROR_LABEL),
  password: Yup.string().required(ERROR_LABEL),
});
