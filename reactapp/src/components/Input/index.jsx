import Container, { ContainerInput } from "./styles";

import React from "react";
import TextError from "components/TextError";

function Input({ error, disabled, ...props }) {
  return (
    <ContainerInput disabled={disabled}>
      <Container disabled={disabled} {...props} />
      {error && <TextError>{error}</TextError>}
    </ContainerInput>
  );
}

export default Input;
