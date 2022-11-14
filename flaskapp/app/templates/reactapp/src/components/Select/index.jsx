import React from "react";
import ReactSelect from "react-select";
import Container, { IconContainer } from "./styles";
import { MdArrowDropDown } from "react-icons/md";

const selectStyles = {
  container: (props) => ({
    ...props,
    background: "#D9D9D9",
    height: "2.5rem",
  }),
  indicatorSeparator: () => ({
    border: "0",
  }),
  control: (props) => ({
    ...props,
    background: "#D9D9D9",
    border: "0",
  }),
  placeholder: (props) => ({
    ...props,
    color: "#000",
    fontSize: "1rem",
  }),
};

const Select = ({ className, ...rest }) => (
  <Container className={className}>
    <ReactSelect
      components={{
        DropdownIndicator: () => (
          <IconContainer>
            <MdArrowDropDown size={24} />
          </IconContainer>
        ),
      }}
      styles={selectStyles}
      {...rest}
    />
  </Container>
);

export default Select;
