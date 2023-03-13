import Container from "./styles";

import Button from "../../components/Button";
import Input from "../../components/Input";

import { useFormik } from "formik";
import React from "react";
import { useNavigate } from "react-router-dom";
import loginSchema from "schemas/loginSchema";
import { useMutation } from "@apollo/client";
import { SIGNING } from "graphql/mutations";
import { useEffect } from "react";
import { useSnackbar } from "notistack";
import { useContextProvider } from "services/Context";

function Login() {
  const { enqueueSnackbar } = useSnackbar();
  const navigate = useNavigate();
  const [signing] = useMutation(SIGNING);
  const { updateUser } = useContextProvider();

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validationSchema: loginSchema,
    onSubmit: async (values) => {
      try {
        const response = await signing({ variables: values });
        localStorage.setItem("token", response.data.signin.token);
        updateUser(response.data.signin.token);
        navigate("/pacientes");
      } catch (e) {
        if (e?.graphQLErrors) {
          e?.graphQLErrors.forEach((erro) => {
            enqueueSnackbar(erro.message, { variant: "error" });
          });
        }
      }
    },
  });

  useEffect(() => {
    const getToken = localStorage.getItem("token");
    if (getToken) {
      navigate("/pacientes", {
        replace: true,
      });
    }
  }, [navigate]);

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
        type="password"
        value={formik.values.password}
        onChange={formik.handleChange}
      />
      <Button>Entrar</Button>
    </Container>
  );
}

export default Login;