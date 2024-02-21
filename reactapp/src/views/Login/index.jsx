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
import { useContextProvider } from "services/Context";
import useHandleErrors from "hooks/useHandleErrors";

function Login() {
  const navigate = useNavigate();
  const [signing, { loading }] = useMutation(SIGNING);
  const { updateDecodedJWT, decodedJWT } = useContextProvider();
  const { handleErrors } = useHandleErrors();

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validationSchema: loginSchema,
    onSubmit: async (values) => {
      if (loading) {
        return;
      }
      try {
        const response = await signing({ variables: values });
        console.log(response.data);
        localStorage.setItem("token", response.data.signin.token);
        updateDecodedJWT(response.data.signin.token);
        navigate("/pacientes");
      } catch (e) {
        handleErrors(e);
      }
    },
  });

  useEffect(() => {
    const getToken = localStorage.getItem("token");
    // Verifica se tem o token validando o login e se
    if (getToken && new Date() <= new Date(decodedJWT?.exp * 1000)) {
      navigate("/pacientes", {
        replace: true,
      });
    }
  }, [decodedJWT]);

  return (
    <Container onSubmit={formik.handleSubmit}>
      <h2>Realizar Login</h2>
      <Input
        placeholder="Login"
        name="email"
        value={formik.values.email}
        onChange={formik.handleChange}
        data-testid="email"
        error={
          formik.errors.email && formik.touched?.email
            ? formik.errors.email
            : ""
        }
      />
      <Input
        placeholder="Senha"
        name="password"
        data-testid="password"
        type="password"
        value={formik.values.password}
        onChange={formik.handleChange}
      />
      <Button loading={loading} data-testid="button">
        Entrar
      </Button>
    </Container>
  );
}

export default Login;
