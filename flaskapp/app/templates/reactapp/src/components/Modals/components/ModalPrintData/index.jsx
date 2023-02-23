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
      <Button
        customType="gray-300"
        type="button"
        onClick={() =>
          addModal(additionalDataScreen({ type: "printPdf_AihSus", id }))
        }
      >
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
          addModal(
            additionalDataScreen({ type: "printPdf_FolhaPrescricao", id })
          )
        }
      >
        Folha Prescrição
      </Button>
      <Button
        customType="gray-300"
        type="button"
        onClick={() =>
          addModal(additionalDataScreen({ type: "printPdf_RelatorioAlta", id }))
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
