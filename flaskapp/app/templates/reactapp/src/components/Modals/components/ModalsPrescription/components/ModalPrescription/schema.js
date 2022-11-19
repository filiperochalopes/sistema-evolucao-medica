import * as Yup from "yup";

export default Yup.object().shape({
  type: Yup.string().required(),
  medicament: Yup.string().required(),
  drug: Yup.object()
    .shape({
      useMode: Yup.string(),
      routeAdministration: Yup.mixed(),
      isAntibiotic: Yup.boolean(),
      initialDate: Yup.string().when("isAntibiotic", {
        is: true,
        otherwise: Yup.string(),
        then: Yup.string().required(),
      }),
      finalDate: Yup.string().when("isAntibiotic", {
        is: true,
        otherwise: Yup.string(),
        then: Yup.string().required(),
      }),
    })
    .test("is-drug-valid", "is required", (value, schema) => {
      if (
        schema.parent.type !== "drug" ||
        (value.finalDate &&
          value.initialDate &&
          value.isAntibiotic &&
          value.routeAdministration &&
          value.useMode)
      ) {
        return true;
      }
      return false;
    })
    .required(),
});
