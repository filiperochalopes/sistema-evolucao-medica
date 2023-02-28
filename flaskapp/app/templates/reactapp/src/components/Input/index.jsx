import Container from "./styles";

import React from "react";
import TextError from "components/TextError";

function Input({ error, ...props }) {
  return (
    <div>
      <Container {...props} />
      {error && <TextError>{error}</TextError>}
    </div>
  );
}

export default Input;
