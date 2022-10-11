import Container, { Header, Main } from "./styles";

import logo from "../../assets/logo.png";

import React from "react";

function PageTemplate({ children, headerComponent }) {
  return (
    <Container>
      <Header>
        {headerComponent ? headerComponent : <img src={logo} alt="logo" />}
      </Header>
      <Main>
        <div>{children}</div>
      </Main>
    </Container>
  );
}

export default PageTemplate;
