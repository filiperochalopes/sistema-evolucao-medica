import * as Yup from "yup";

export default Yup.object().shape({
  restingActivity: Yup.string(),
  diet: Yup.string(),
  drugs: Yup.array().of(
    Yup.object().shape({
      drugName: Yup.string().required(),
      drugKind: Yup.string().required(),
      dosage: Yup.string().required(),
      route: Yup.string().required(),
      initialDate: Yup.string().required(),
      endingDate: Yup.string().required(),
    })
  ),
  nursingActivities: Yup.array().of(Yup.string()),
});
