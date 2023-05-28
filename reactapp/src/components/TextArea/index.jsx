import Container, { ContainerTextArea, Label } from "./styles";

import React, { useState } from "react";
import TextError from "components/TextError";

function TextArea({ error, placeholder, disabled, value, ...props }) {
  const [select, setSelect] = useState(false);
  return (
    <ContainerTextArea>
      {placeholder && (
        <Label disabled={disabled} select={select || value}>
          {placeholder}
        </Label>
      )}
      <Container
        disabled={disabled}
        {...props}
        value={value}
        onFocus={() => setSelect(true)}
        onBlur={() => setSelect(false)}
      />
      {error && <TextError>{error}</TextError>}
    </ContainerTextArea>
  );
}

export default TextArea;
