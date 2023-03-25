import Container, { ContainerInput, Label } from "./styles";

import React, { useRef, useState } from "react";
import TextError from "components/TextError";

function Input({ error, disabled, placeholder, value, ...props }) {
  const [select, setSelect] = useState(false);
  const ref = useRef(null);
  return (
    <ContainerInput disabled={disabled}>
      {placeholder && (
        <Label
          width={ref?.current?.clientWidth}
          disabled={disabled}
          select={select || value}
        >
          {placeholder}
        </Label>
      )}
      <Container
        ref={ref}
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
