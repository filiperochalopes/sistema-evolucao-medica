import { ERROR_LABEL } from "constants/errorText";
import * as Yup from "yup";

export default Yup.object().shape({
  restingActivity: Yup.string(),
  diet: Yup.string(),
  drugs: Yup.array().of(
    Yup.object()
      .shape({
        drugName: Yup.string().required(ERROR_LABEL),
        drugKind: Yup.string().required(ERROR_LABEL),
        dosage: Yup.string().required(ERROR_LABEL),
        route: Yup.string().required(ERROR_LABEL),
        initialDate: Yup.string(ERROR_LABEL),
        endingDate: Yup.string(ERROR_LABEL),
      })
      .required()
  ),
  nursingActivities: Yup.array().of(Yup.string()),
});
