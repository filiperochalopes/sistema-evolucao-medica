import ModalPrintData from "components/Modals/components/ModalPrintData";

const printScreen = (id) => ({
  confirmButtonAction: () => {},
  content: <ModalPrintData id={id} />,
  returnButtonAction: () => {},
  title: "Impressão de Documentos",
});

export default printScreen;
