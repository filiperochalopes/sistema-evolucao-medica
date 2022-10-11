import Container, { ContainerContentModal } from "./styles";

import PageTemplate from "layouts/Page";
import React from "react";

const Modal = ({ children, confirmButton, goBack, headerTitle }) => {
  return (
    <Container>
      <button
        onClick={(e) => {
          if (goBack) {
            goBack(e);
          }
        }}
        className="button-modal"
      ></button>
      <div>
        <ContainerContentModal>
          <PageTemplate headerComponent={<></>}>{children}</PageTemplate>
        </ContainerContentModal>
      </div>
    </Container>
  );
};

export default Modal;
