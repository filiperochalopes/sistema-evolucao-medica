import Container, { Header, Main } from "./styles";

import logo from "../../assets/logo.png";

import React from "react";
import { Link } from "react-router-dom";

function PageTemplate({ children, headerComponent }) {
  return (
    <Container>
      <Header defaultHeight={!headerComponent}>
        {headerComponent ? (
          headerComponent
        ) : (
          <Link to="/">
            <img src={logo} alt="logo" />
          </Link>
        )}
      </Header>
      <Main>
        <div>{children}</div>
      </Main>
    </Container>
  );
}

export default PageTemplate;
