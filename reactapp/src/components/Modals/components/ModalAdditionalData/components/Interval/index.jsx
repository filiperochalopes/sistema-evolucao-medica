import { useEffect } from "react";

const { default: Button } = require("components/Button");
const { default: Input } = require("components/Input");
const { ButtonContainer } = require("../../styles");

export const get24ShiftDatetimeInterval = () => {
  const currentDate = new Date();
  const initialDate = new Date();
  const finalDate = new Date();
  let initalDateFormat, finalDateFormat;

  if (currentDate.getHours() > 7 && currentDate.getHours() < 24) {
    finalDate.setDate(initialDate.getDate() + 1);
    initialDate.setHours(7);
    finalDate.setHours(7);
    finalDateFormat = `${finalDate.toISOString().split("T")[0]}T07:00`;
    initalDateFormat = `${initialDate.toISOString().split("T")[0]}T07:00`;
  } else {
    initialDate.setDate(initialDate.getDate() - 1);

    initialDate.setHours(7);
    finalDate.setHours(7);
    finalDateFormat = `${finalDate.toISOString().split("T")[0]}T07:00`;
    initalDateFormat = `${initialDate.toISOString().split("T")[0]}T07:00`;
  }

  return {
    startDatetimeStamp: initalDateFormat,
    endingDatetimeStamp: finalDateFormat,
  };
};

const Interval = ({ formik }) => {
  useEffect(() => {
    formik.setValues({
      extra: {
        interval: get24ShiftDatetimeInterval(),
      },
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      <Input
        type="datetime-local"
        placeholder="Data e Hora inicial"
        onChange={formik.handleChange}
        value={formik.values.extra.interval.startDatetimeStamp}
        name="extra.interval.startDatetimeStamp"
      />
      <Input
        type="datetime-local"
        placeholder="Data e Hora Final"
        onChange={formik.handleChange}
        value={formik.values.extra.interval.endingDatetimeStamp}
        name="extra.interval.endingDatetimeStamp"
      />
      <ButtonContainer>
        <Button type="submit">Confirmar</Button>
      </ButtonContainer>
    </>
  );
};

export default Interval;
