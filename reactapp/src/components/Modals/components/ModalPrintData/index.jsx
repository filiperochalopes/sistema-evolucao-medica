/* eslint-disable import/order */
import Container from "./styles";

import Button from "components/Button";
import { useModalContext } from "services/ModalContext";
import React from "styled-components";
import additionalDataScreen from "helpers/additionalDataScreen";
import CheckRole from "routes/CheckRole";

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
        Ficha de Internamento Hospitalar (Folha de Rosto)
      </Button>
      <Button
        customType="gray-300"
        type="button"
        onClick={() =>
          addModal(additionalDataScreen({ type: "printPdf_AihSus", id }))
        }
      >
        Folha de Admissão do Hospital (AIH)
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
      <CheckRole roles={["doc"]}>
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
      </CheckRole>
      <CheckRole roles={["doc"]}>
        <Button
          customType="gray-300"
          type="button"
          onClick={() =>
            addModal(
              additionalDataScreen({ type: "printPdf_RelatorioAlta", id })
            )
          }
        >
          Ficha de Alta
        </Button>
      </CheckRole>
      <Button
        customType="gray-300"
        type="button"
        onClick={() =>
          addModal(
            additionalDataScreen({ type: "printPdf_BalancoHidrico", id })
          )
        }
      >
        Balanço hídrico
      </Button>
      <Button
        customType="gray-300"
        type="button"
        onClick={() =>
          addModal(additionalDataScreen({ type: "printPdf_Apac", id }))
        }
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
