/* eslint-disable import/order */
import Container from "./styles";

import Button from "components/Button";
import { useModalContext } from "services/ModalContext";
import React from "styled-components";
import additionalDataScreen from "helpers/additionalDataScreen";

const ModalPrintData = ({ confirmButton }) => {
  const { addModal } = useModalContext();

  return (
    <Container>
      <Button
        onClick={() =>
          addModal(additionalDataScreen({ type: "hospitalAdmissionForm" }))
        }
        customType="gray"
        type="button"
      >
        Ficha de Internamento Hospitalar
      </Button>
      <Button customType="gray" type="button">
        Folha de Admissão do Hospital
      </Button>
      <Button
        customType="gray"
        type="button"
        onClick={() =>
          addModal(additionalDataScreen({ type: "evolutionForm" }))
        }
      >
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
      <Button
        customType="gray"
        type="button"
        onClick={() => addModal(additionalDataScreen({ type: "APAC" }))}
      >
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
};

export default ModalPrintData;
