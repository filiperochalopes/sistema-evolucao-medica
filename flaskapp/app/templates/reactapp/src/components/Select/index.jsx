import React from "react";
import ReactSelect from "react-select";
import Container, { IconContainer } from "./styles";
import { MdArrowDropDown } from "react-icons/md";

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
      styles={{
        container: (props) => ({
          ...props,
          background: "#D9D9D9",
          height: "2.5rem",
        }),
        indicatorSeparator: (props) => ({
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
      }}
      {...rest}
    />
  </Container>
);

export default Select;
