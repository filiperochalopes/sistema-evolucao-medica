import Container, { ContainerInput, Label } from "./styles";

import React, { useRef, useState } from "react";
import TextError from "components/TextError";

function Input({ error, disabled, placeholder, value, className, ...rest }) {
  const [select, setSelect] = useState(false);
  const ref = useRef(null);
  return (
    <ContainerInput className={className} disabled={disabled}>
      {placeholder && (
        <Label
          width={ref?.current?.clientWidth}
          disabled={disabled}
          select={select || value}
        >
          {placeholder}
        </Label>
      )}
      <Container
        ref={ref}
        disabled={disabled}
        value={value}
        className={className}
        {...rest}
        onFocus={() => setSelect(true)}
        onBlur={() => setSelect(false)}
      />
      {error && <TextError>{error}</TextError>}
    </ContainerInput>
  );
}

function FormikInput({
  formik: { values, errors, touched, ...formik },
  name,
  ...rest
}) {
  const [isFocused, setIsFocused] = useState(false);
  const ref = useRef(null);
  return (
    <ContainerInput>
      <Label select={isFocused || !!values[name]}>{rest.label || name}</Label>
      <Container
        ref={ref}
        value={values[name]}
        name={name}
        {...rest}
        onChange={(e) => {
          if (rest.onChange) rest.onChange(e);
          formik.handleChange(e);
        }}
        onFocus={() => setIsFocused(true)}
        onBlur={(e) => {
          setIsFocused(false);
          formik.handleBlur(e);
        }}
      />
      {errors[name] && touched[name] && <TextError>{errors[name]}</TextError>}
    </ContainerInput>
  );
}

export default Input;
export { FormikInput };
