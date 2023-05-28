import Container, { Header, Main } from "./styles";
import { BiLogOut } from "react-icons/bi";
import logo from "../../assets/logo.png";

import React, { useEffect } from "react";
import { Link } from "react-router-dom";
import { useContextProvider } from "services/Context";

function PageTemplate({ children, headerComponent }) {
  const { logout, decodedJWT, user } = useContextProvider();

  useEffect(() => {
    console.log(decodedJWT);
  }, [decodedJWT]);

  return (
    <Container>
      <Header defaultHeight={!headerComponent}>
        {headerComponent ? (
          headerComponent
        ) : (
          <>
            {decodedJWT && (
              <>
                <button onClick={() => logout()}>
                  <BiLogOut color="#fff" size={32} />
                </button>
                <Link to="/">
                  <img src={logo} alt="logo" />
                </Link>
                <div>{user?.name}</div>
                <span />
              </>
            )}
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
