import React from "react";
import PrescriptionGroupInput from "./styles";

export default ({ optionId, name, id, description, onChange }) => {
  return (
    <PrescriptionGroupInput>
      <input
        type="radio"
        name={name}
        id={id}
        value={optionId}
        onChange={onChange}
      />
      <label htmlFor={id}>{description}</label>
    </PrescriptionGroupInput>
  );
};
