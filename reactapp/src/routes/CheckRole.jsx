import { useEffect } from "react";
import { useContextProvider } from "services/Context";
import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
// const { Navigate, useLocation, useNavigate } = require("react-router-dom");

const CheckRole = ({ children, roles, goBack }) => {
  const { decodedJWT } = useContextProvider();
  const [permited, setPermited] = useState("waiting");
  const navigate = useNavigate();

  useEffect(() => {
    if (!decodedJWT?.scope) {
      return;
    }
    if (roles.includes(decodedJWT?.scope)) {
      setPermited("checked");
      return;
    }
    setPermited("notPermitted");
    if (goBack) {
      navigate(-1);
    }
  }, [goBack, navigate, roles, decodedJWT]);

  if (permited === "waiting") {
    return <div />;
  }
  if (permited === "checked") {
    return children;
  }
};

export default CheckRole;
