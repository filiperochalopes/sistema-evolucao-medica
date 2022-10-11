import Component from "./styles";

import React from "react";

const Pacient = ({ children, ...rest }) => {
  return <Component {...rest}>{children}</Component>;
};

export default Pacient;
