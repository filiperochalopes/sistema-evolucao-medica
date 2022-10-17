import Container from "./styles";

import Button from "../../components/Button";
import Input from "../../components/Input";

import { useFormik } from "formik";
import React from "react";
import { useNavigate } from "react-router-dom";
import loginSchema from "schemas/loginSchema";

function Login() {
  const navigate = useNavigate();
  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validationSchema: loginSchema,
    onSubmit: (values) => {
      console.log(values);
      navigate("/pacientes");
    },
  });
  return (
    <Container onSubmit={formik.handleSubmit}>
      <h2>Realizar Login</h2>
      <Input
        placeholder="Login"
        name="email"
        value={formik.values.email}
        onChange={formik.handleChange}
      />
      <Input
        placeholder="Senha"
        name="password"
        value={formik.values.password}
        onChange={formik.handleChange}
      />
      <Button>Entrar</Button>
    </Container>
  );
}

export default Login;
