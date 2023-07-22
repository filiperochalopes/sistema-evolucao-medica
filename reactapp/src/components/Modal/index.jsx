import Container, { ContainerContentModal, Header, Main } from "./styles";

import React, { cloneElement } from "react";
import { IoMdClose } from "react-icons/io";
import { useTheme } from "styled-components";

const Modal = ({
  children,
  confirmButton,
  goBack,
  headerTitle,
  headerStyle,
}) => {
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
          <Header headerStyle={headerStyle}>
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
          <Main>
            <div>{cloneElement(children, { confirmButton, goBack })}</div>
          </Main>
        </ContainerContentModal>
      </div>
    </Container>
  );
};

export default Modal;
