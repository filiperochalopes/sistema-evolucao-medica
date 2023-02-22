/* eslint-disable import/order */
import Container from "./styles";

import Button from "components/Button";
import { useModalContext } from "services/ModalContext";
import React from "styled-components";
import additionalDataScreen from "helpers/additionalDataScreen";

const ModalPrintData = ({ confirmButton, id }) => {
  const { addModal } = useModalContext();

  return (
    <Container>
      <Button
        onClick={() =>
          addModal(
            additionalDataScreen({ type: "printPdf_FichaInternamento", id })
          )
        }
        customType="gray-300"
        type="button"
      >
        Ficha de Internamento Hospitalar
      </Button>
      <Button customType="gray-300" type="button">
        Folha de Admissão do Hospital
      </Button>
      <Button
        customType="gray-300"
        type="button"
        onClick={() =>
          addModal(additionalDataScreen({ type: "printPdf_FolhaEvolucao", id }))
        }
      >
        Folha de Evolução
      </Button>
      <Button
        customType="gray-300"
        type="button"
        onClick={() =>
          addModal(additionalDataScreen({ type: "PrescriptionSheet" }))
        }
      >
        Folha Prescrição
      </Button>
      <Button
        customType="gray-300"
        type="button"
        onClick={() =>
          addModal(additionalDataScreen({ type: "DischargeForm" }))
        }
      >
        Ficha de Alta
      </Button>
      <Button customType="gray-300" type="button">
        Balanço hídrico
      </Button>
      <Button
        customType="gray-300"
        type="button"
        onClick={() => addModal(additionalDataScreen({ type: "APAC" }))}
      >
        APAC
      </Button>
      <Button customType="gray-300" type="button">
        Prescrição Externa
      </Button>
      <Button customType="gray-300" type="button">
        Solicitação de Exames
      </Button>
    </Container>
  );
};

export default ModalPrintData;
