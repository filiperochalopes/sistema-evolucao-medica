import { AiOutlineLoading3Quarters } from "react-icons/ai";
import Container, { ContainerLoading } from "./styles";

import React from "react";

function Button({ loading, children, ...props }) {
  return (
    <Container {...props}>
      {loading ? (
        <ContainerLoading loading={loading}>
          <AiOutlineLoading3Quarters />
        </ContainerLoading>
      ) : (
        children
      )}
    </Container>
  );
}

export default Button;
