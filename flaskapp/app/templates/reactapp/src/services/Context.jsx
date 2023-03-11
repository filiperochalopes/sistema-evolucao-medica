import React, { createContext, useContext, useEffect, useState } from "react";
import jwt_decode from "jwt-decode";

const Context = createContext(null);

const ContextProvider = ({ children }) => {
  const [user, setUser] = useState();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      return;
    }
    const decode = jwt_decode(token);
    console.log(decode);
    setUser({
      ...decode,
      token,
    });
  }, []);
  function updateUser(token) {
    const decode = jwt_decode(token);
    console.log(decode);
    setUser({
      ...decode,
      token,
    });
  }

  return (
    <Context.Provider value={{ user, updateUser }}>{children}</Context.Provider>
  );
};

const useContextProvider = () => useContext(Context);
export { useContextProvider };
export default ContextProvider;
