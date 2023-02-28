import Container from "./styles";

import React from "react";
import TextError from "components/TextError";

function TextArea({ error, ...props }) {
  return (
    <div>
      <Container {...props} />
      {error && <TextError>{error}</TextError>}
    </div>
  );
}

export default TextArea;
