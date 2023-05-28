import React, { createContext, useContext, useEffect, useState } from "react";
import jwt_decode from "jwt-decode";
import { useLazyQuery } from "@apollo/client";
import { MY_USER } from "graphql/queries";
import { useNavigate } from "react-router-dom";

const Context = createContext(null);

const ContextProvider = ({ children }) => {
  const [decodedJWT, setDecodedJWT] = useState();
  const [user, setUser] = useState();
  const navigate = useNavigate();
  const [getMyUser, { myUserData }] = useLazyQuery(MY_USER);

  useEffect(() => {
    // Captura o token da local storage
    const _encodedJWT = localStorage.getItem("token");
    if (!_encodedJWT) {
      return;
    }
    // Armazenar dados de token sem codificação
    const _decodedJWT = jwt_decode(_encodedJWT);
    setDecodedJWT({
      ..._decodedJWT,
      token: _encodedJWT,
    });
  }, []);

  useEffect(() => {
    // Em caso de alterações do token é preciso rever o usuário
    getMyUser();
  }, [decodedJWT, getMyUser]);

  useEffect(() => {
    // Setando dados de usuário em contexto
    console.log(myUserData);
    setUser(myUserData);
  }, [myUserData]);

  function updateDecodedJWT(token) {
    const _decodedJWT = jwt_decode(token);
    setDecodedJWT({
      ..._decodedJWT,
      token,
    });
  }

  function logout() {
    localStorage.removeItem("token");
    setDecodedJWT(undefined);
    navigate("/", { replace: true });
  }

  return (
    <Context.Provider value={{ decodedJWT, updateDecodedJWT, user, logout }}>
      {children}
    </Context.Provider>
  );
};

const useContextProvider = () => useContext(Context);
export { useContextProvider };
export default ContextProvider;
