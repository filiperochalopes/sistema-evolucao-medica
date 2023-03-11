import Container, { Header, Main } from "./styles";
import { BiLogOut } from "react-icons/bi";
import logo from "../../assets/logo.png";

import React from "react";
import { Link } from "react-router-dom";
import { useContextProvider } from "services/Context";

function PageTemplate({ children, headerComponent }) {
  const { logout } = useContextProvider();
  return (
    <Container>
      <Header defaultHeight={!headerComponent}>
        {headerComponent ? (
          headerComponent
        ) : (
          <>
            <button onClick={() => logout()}>
              <BiLogOut color="#fff" size={32} />
            </button>
            <Link to="/">
              <img src={logo} alt="logo" />
            </Link>
            <span />
          </>
        )}
      </Header>
      <Main>
        <div>{children}</div>
      </Main>
    </Container>
  );
}

export default PageTemplate;
