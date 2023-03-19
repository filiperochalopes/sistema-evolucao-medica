import Container, { ContainerInput, Label } from "./styles";

import React, { useState } from "react";
import TextError from "components/TextError";

function Input({ error, disabled, placeholder, value, ...props }) {
  const [select, setSelect] = useState(false);
  return (
    <ContainerInput disabled={disabled}>
      {placeholder && (
        <Label disabled={disabled} select={select || value}>
          {placeholder}
        </Label>
      )}
      <Container
        disabled={disabled}
        value={value}
        {...props}
        onFocus={() => setSelect(true)}
        onBlur={() => setSelect(false)}
      />
      {error && <TextError>{error}</TextError>}
    </ContainerInput>
  );
}

export default Input;
