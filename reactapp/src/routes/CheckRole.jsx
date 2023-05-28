import { useEffect } from "react";
import { useContextProvider } from "services/Context";
import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
// const { Navigate, useLocation, useNavigate } = require("react-router-dom");

const CheckRole = ({ children, roles, goBack }) => {
  const { user } = useContextProvider();
  const [permited, setPermited] = useState("waiting");
  const navigate = useNavigate();

  useEffect(() => {
    if (!user?.scope) {
      return;
    }
    if (roles.includes(user?.scope)) {
      setPermited("checked");
      return;
    }
    setPermited("notPermitted");
    if (goBack) {
      navigate(-1);
    }
  }, [goBack, navigate, roles, user]);
  if (permited === "waiting") {
    return <div />;
  }
  if (permited === "checked") {
    return children;
  }
};

export default CheckRole;
