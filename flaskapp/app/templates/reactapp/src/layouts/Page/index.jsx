import Container, { Header, Main } from "./styles";

import logo from "../../assets/logo.png";

import React from "react";
import { Outlet } from "react-router-dom";

function PageTemplate() {
  return (
    <Container>
      <Header>
        <img src={logo} alt="logo" />
      </Header>
      <Main>
        <div>
          <Outlet />
        </div>
      </Main>
    </Container>
  );
}

export default PageTemplate;
