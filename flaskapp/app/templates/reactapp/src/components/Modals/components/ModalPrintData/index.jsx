import Container from "./styles";

import Button from "components/Button";
import React from "styled-components";

const ModalPrintData = () => (
  <Container>
    <Button customType="gray" type="button">
      Ficha de Internamento Hospitalar
    </Button>
    <Button customType="gray" type="button">
      Folha de Admissão do Hospital
    </Button>
    <Button customType="gray" type="button">
      Folha de Evolução
    </Button>
    <Button customType="gray" type="button">
      Folha Prescrição
    </Button>
    <Button customType="gray" type="button">
      Ficha de Alta
    </Button>
    <Button customType="gray" type="button">
      Balanço hídrico
    </Button>
    <Button customType="gray" type="button">
      APAC
    </Button>
    <Button customType="gray" type="button">
      Prescrição Externa
    </Button>
    <Button customType="gray" type="button">
      Solicitação de Exames
    </Button>
  </Container>
);

export default ModalPrintData;
