import * as Yup from "yup";

export default Yup.object().shape({
  type: Yup.mixed().required(),
  medicament: Yup.mixed().required(),
  drug: Yup.object()
    .shape({
      useMode: Yup.string(),
      routeAdministration: Yup.mixed(),
      isAntibiotic: Yup.string(),
      initialDate: Yup.string().when("isAntibiotic", {
        is: "abt",
        otherwise: Yup.string(),
        then: Yup.string().required(),
      }),
      finalDate: Yup.string().when("isAntibiotic", {
        is: "abt",
        otherwise: Yup.string(),
        then: Yup.string().required(),
      }),
    })
    .test("is-drug-valid", "is required", (value, schema) => {
      if (
        schema.parent.type?.name !== "drug" ||
        ((value.finalDate || value.isAntibiotic === "oth") &&
          (value.initialDate || value.isAntibiotic === "oth") &&
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
