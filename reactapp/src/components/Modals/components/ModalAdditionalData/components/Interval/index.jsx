import { useEffect } from "react";

const { default: Button } = require("components/Button");
const { default: Input } = require("components/Input");
const { ButtonContainer } = require("../../styles");

const Interval = ({ formik }) => {
  useEffect(() => {
    const currentDate = new Date();

    if (currentDate.getHours() > 7 && currentDate.getHours() < 24) {
      const initialDate = new Date();
      const finalDate = new Date();
      finalDate.setDate(initialDate.getDate() + 1);

      initialDate.setHours(7);
      finalDate.setHours(7);
      const finalDateFormat = `${finalDate.toISOString().split("T")[0]}T07:00`;
      const initalDateFormat = `${
        initialDate.toISOString().split("T")[0]
      }T07:00`;
      formik.setValues({
        extra: {
          interval: {
            startDatetimeStamp: initalDateFormat,
            endingDatetimeStamp: finalDateFormat,
          },
        },
      });
    } else {
      const initialDate = new Date();
      const finalDate = new Date();

      initialDate.setDate(initialDate.getDate() - 1);

      initialDate.setHours(7);
      finalDate.setHours(7);
      const finalDateFormat = `${finalDate.toISOString().split("T")[0]}T07:00`;
      const initalDateFormat = `${
        initialDate.toISOString().split("T")[0]
      }T07:00`;
      formik.setValues({
        extra: {
          interval: {
            startDatetimeStamp: initalDateFormat,
            endingDatetimeStamp: finalDateFormat,
          },
        },
      });
    }
  }, []);

  return (
    <>
      <Input
        type="datetime-local"
        placeholder="Data Inicial"
        onChange={formik.handleChange}
        value={formik.values.extra.interval.startDatetimeStamp}
        name="extra.interval.startDatetimeStamp"
      />
      <Input
        type="datetime-local"
        placeholder="Data Final"
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
