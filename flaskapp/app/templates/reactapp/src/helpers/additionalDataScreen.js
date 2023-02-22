import ModalAdditionalData from "components/Modals/components/ModalAdditionalData";

const additionalDataScreen = ({ type = "printPdf_FichaInternamento", id }) => ({
  confirmButtonAction: () => {},
  content: <ModalAdditionalData type={type} id={id} />,
  returnButtonAction: () => {},
  title: "Preencha os campos adicionais",
});

export default additionalDataScreen;
