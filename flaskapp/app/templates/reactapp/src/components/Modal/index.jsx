import Container, { ContainerContentModal, Header } from "./styles";

import PageTemplate from "layouts/Page";
import React, { cloneElement } from "react";
import { IoMdClose } from "react-icons/io";
import { useTheme } from "styled-components";

const Modal = ({ children, confirmButton, goBack, headerTitle }) => {
  const theme = useTheme();

  return (
    <Container>
      <button
        type="button"
        onClick={(e) => {
          if (goBack) {
            goBack(e);
          }
        }}
        className="button-modal"
      ></button>
      <div>
        <ContainerContentModal>
          <PageTemplate
            headerComponent={
              <Header>
                <p>{headerTitle}</p>
                <button
                  type="button"
                  onClick={(e) => {
                    if (goBack) {
                      goBack(e);
                    }
                  }}
                >
                  <IoMdClose size={36} color={theme.colors.white} />
                </button>
              </Header>
            }
          >
            {cloneElement(children, { confirmButton }, null)}
          </PageTemplate>
        </ContainerContentModal>
      </div>
    </Container>
  );
};

export default Modal;
