import Container, { ContainerInput } from "./styles";

import React from "react";
import TextError from "components/TextError";

function Input({ error, ...props }) {
  return (
    <ContainerInput>
      <Container {...props} />
      {error && <TextError>{error}</TextError>}
    </ContainerInput>
  );
}

export default Input;
