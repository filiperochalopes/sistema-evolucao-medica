import Container from "./styles";

import Button from "../../components/Button";
import Input from "../../components/Input";

import { useFormik } from "formik";
import React from "react";
import { useNavigate } from "react-router-dom";
import loginSchema from "schemas/loginSchema";
import { useMutation } from "@apollo/client";
import { SIGNING } from "graphql/mutations";

function Login() {
  const navigate = useNavigate();
  const [signing] = useMutation(SIGNING);

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validationSchema: loginSchema,
    onSubmit: async (values) => {
      try {
        const response = await signing({ variables: values });
        localStorage.setItem("token", response.data.token);
        navigate("/pacientes");
      } catch {
        alert("error,tente novamente");
      }
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
