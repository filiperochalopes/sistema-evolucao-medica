import React, { createContext, useContext, useEffect, useState } from "react";
import jwt_decode from "jwt-decode";
import { useNavigate } from "react-router-dom";

const Context = createContext(null);

const ContextProvider = ({ children }) => {
  const [user, setUser] = useState();
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      return;
    }
    const decode = jwt_decode(token);
    setUser({
      ...decode,
      token,
    });
  }, []);

  function updateUser(token) {
    const decode = jwt_decode(token);
    setUser({
      ...decode,
      token,
    });
  }

  function logout() {
    localStorage.removeItem("token");
    setUser(undefined);
    navigate("/", { replace: true });
  }

  return (
    <Context.Provider value={{ user, updateUser, logout }}>
      {children}
    </Context.Provider>
  );
};

export const useContextProvider = () => useContext(Context);

export default ContextProvider;
