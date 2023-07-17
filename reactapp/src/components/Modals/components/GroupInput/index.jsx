import React from "react";
import GroupInput from "./styles";

export default ({ optionId, name, id, description, onChange }) => {
  return (
    <GroupInput>
      <input
        type="radio"
        name={name}
        id={id}
        value={optionId}
        onChange={onChange}
      />
      <label htmlFor={id}>{description}</label>
    </GroupInput>
  );
};
