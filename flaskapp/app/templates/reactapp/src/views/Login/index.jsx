import Container from "./styles";

import Button from "../../components/Button";
import Input from "../../components/Input";

import React from "react";
import { useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate();
  return (
    <Container>
      <h2>Realizar Login</h2>
      <Input placeholder="Login" />
      <Input placeholder="Senha" />
      <Button
        onClick={() => {
          navigate("/pacientes");
        }}
      >
        Entrar
      </Button>
    </Container>
  );
}

export default Login;
