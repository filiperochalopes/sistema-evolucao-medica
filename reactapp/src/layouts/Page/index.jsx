import Container, { Header, Main } from "./styles";
import logo from "assets/logo.png";
import { AiFillCaretDown } from "react-icons/ai";

import React from "react";
import { useState } from "react";
import { Link } from "react-router-dom";
import { useContextProvider } from "services/Context";

function PageTemplate({ children }) {
  const { logout, decodedJWT, user } = useContextProvider();
  const [showMenu, setShowMenu] = useState(false);

  return (
    <Container>
      <Header>
        <>
          <Link to="/" title="Voltar para lista de internamentos">
            <img src={logo} alt="logo" />
          </Link>
          {decodedJWT && (
            <ul>
              <li
                onMouseOver={() => setShowMenu(true)}
                onFocus={() => setShowMenu(true)}
                onMouseOut={() => setShowMenu(false)}
                onBlur={() => setShowMenu(false)}
              >
                Olá {user?.name} <AiFillCaretDown />
                {showMenu && (
                  <ul>
                    <li>
                      <Link to="/editar-usuario">Editar dados</Link>
                    </li>
                    <li>
                      <button onClick={() => logout()}>Sair</button>
                    </li>
                  </ul>
                )}
              </li>
            </ul>
          )}
        </>
      </Header>
      <Main>
        <div>{children}</div>
      </Main>
    </Container>
  );
}

export default PageTemplate;
