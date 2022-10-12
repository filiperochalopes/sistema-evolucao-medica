import Component from "./styles";

import React from "react";

const ListOption = ({ children, ...rest }) => {
  return <Component {...rest}>{children}</Component>;
};

export default ListOption;
